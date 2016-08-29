###################################################################################
#                                                                                 #
#   Copyright "2015" "Wuppertal Institut"                                         #
#                                                                                 #
#   Licensed under the Apache License, Version 2.0 (the "License");               #
#   you may not use this file except in compliance with the License.              #
#   You may obtain a copy of the License at                                       #
#                                                                                 #
#       http://www.apache.org/licenses/LICENSE-2.0                                #
#                                                                                 #
#   Unless required by applicable law or agreed to in writing, software           #
#   distributed under the License is distributed on an "AS IS" BASIS,             #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.      #
#   See the License for the specific language governing permissions and           #
#   limitations under the License.                                                #
#                                                                                 #
###################################################################################

# Grid_Model main Module


# Imports Database Modules
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT as _il # Needed for creating Databases

import subprocess
import os
import csv

import datetime
import sys
import stat
import platform

if (sys.version_info >= (3, 0)):
    # Python 3 only import
    import urllib.request
else:
    # Python 2 only import
    import urllib
    from urllib2 import urlopen

    try:
        from  builtins import input # First check if future module has been installed
    except ImportError:
        if hasattr(__builtins__, 'raw_input'):
            input=raw_input
    import io


import general_funcs
import build_up_db
import qgis_processing
import qgis_projects


class grid_model:

    def __init__(   self,
                    database,
                    password,
                    qgis_processing_path,
                    host,
                    port,
                    user):

        self.host=host
        self.port=port
        self.osmosis_host = str(self.host) + ':' + str(self.port)
        
        self.user=user
        self.password=password
        self.database = database

        self.standard_db = 'postgres'

        self.platform = None # Platform specific variable


        ## General Platform Check 
        if platform.system() == "Darwin":
            self.platform = 'mac'
            print("Detected platform: Darwin")

        elif platform.system() == "Linux" or platform.system() == "Linux2":
            self.platform = 'lin'
            print("Detected platform: Linux")
        
        elif platform.system().lower() == "win32" or platform.system().lower() == "windows":
            self.platform = 'win'
            print("Detected platform: Windows")
            
        else:
            print("Detected platform: None")


        ## Osmosis Path and Activation
        if self.platform == 'win':
            self.osmosis_path = os.getcwd() + '\\osmosis\\bin\\osmosis.bat' # The provided Osmosis Version is always used
        else:
            self.osmosis_path = os.getcwd() + '/osmosis/bin/osmosis' # The provided Osmosis Version is always used
            st = os.stat(self.osmosis_path)
            os.chmod(self.osmosis_path, st.st_mode | stat.S_IEXEC) # Set the osmosis file as executable

        ## Setting osmTGmod folder structure:
        print("Checking/Creating file directories")
        self.raw_data_dir = os.path.dirname(os.getcwd()) + "/raw_data"
        self.result_dir = os.path.dirname(os.getcwd()) + "/results"
        self.qgis_projects_dir = os.path.dirname(os.getcwd()) + "/qgis_projects"
        self.transfer_busses_dir = os.path.dirname(os.getcwd()) + "/transfer_busses"


        ## Basic folders are created if not existent
        if not os.path.exists(self.raw_data_dir):
            os.makedirs(self.raw_data_dir)

        if not os.path.exists(self.result_dir):
            os.makedirs(self.result_dir)

        if not os.path.exists(self.qgis_projects_dir):
            os.makedirs(self.qgis_projects_dir)

        if not os.path.exists(self.transfer_busses_dir):
            os.makedirs(self.transfer_busses_dir)

        ## Server connection:
        print ("Connecting to Server...")

        try:
            # Standard database connection is used to check out server connection
            conn_server = psycopg2.connect( host=self.host,
                                            port=self.port,
                                            database=self.standard_db,
                                            user=self.user,
                                            password=self.password)
            cur_server = conn_server.cursor()
            print ("Connected to Server!")
        except:
            # Get the most recent exception
            exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
            sys.exit(exceptionValue)

        print ("Connecting to Database...")

        try:
            self.conn = psycopg2.connect(host=self.host,
                                port=self.port,
                                database=self.database,
                                user=self.user,
                                password=self.password)
            # conn.cursor will return a cursor object, used to perform queries
            self.cur = self.conn.cursor()
            print ("Connected to Database!")

        except:
            # Get the most recent exception
            # exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
            # Can be improved by listing the existing databases and make a choice
            print ("There is no Database named '%s'!" % (self.database))
            choice = input("Do you wish to create Database '%s' and build up "\
                "osmTgmod-database?:" % (self.database)).lower()

            if general_funcs.ask_yes_no(choice) == True:
                print ("Creating Database...")

                # Creates new Database
                conn_server.set_isolation_level(_il)
                cur_server.execute('CREATE DATABASE %s' %self.database)
                conn_server.close()
                print ("New Database Created!")

                # Connects to new Database
                print ("Connecting to new Database...")
                try:
                    
                    self.conn = psycopg2.connect(host=self.host,
                                port=self.port,
                                database=self.database,
                                user=self.user,
                                password=self.password)

                    self.cur = self.conn.cursor()
                    print ("Connected to Database!")

                    print ("Creating Status-Table...")
                    
                    # Creates table _db_status... 
                    # ...for documenting database module status
                    # status = FALSE by default
                    self.cur.execute ("""
DROP TABLE IF EXISTS _db_status;
CREATE TABLE _db_status (module TEXT, status BOOLEAN);
INSERT INTO _db_status (module, status) VALUES ('grid_model', FALSE);
                                        """)
                    self.conn.commit()

                except:
                    # Get the most recent exception
                    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                    sys.exit(exceptionValue)

            else:
                sys.exit("NO Database is created - Programm cancelled by user!")


        # checks if Database is ready to use!
        print ("Checking Database-Status...")
        self.cur.execute("SELECT status FROM _db_status WHERE module = 'grid_model';")
        status = self.cur.fetchone()[0]
        if status == False:

            print ("Database not ready! Building up Database...")

            ## builds up database
            build_up_db.build_up_db(self.conn, self.cur) # See PDF

        elif status == True:
            print ("Database ready to use!")
        else:
            sys.exit("Database could not be checked. Grid Model is NOT ready to use!")


        # Checking if OSM-Data is available
        print ("Checking OSM-Data")
        self.cur.execute("SELECT downloaded FROM osm_metadata")
        downloaded = self.cur.fetchone()[0]

        if downloaded == None:
            print ("No OSM-Data found in Database!")
            choice = input("Do you wish to load OSM-Data into Database?: ").lower()

            if general_funcs.ask_yes_no(choice) == True:
                self.update_osm_data()
            else:
                sys.exit("No OSM-Data is imported. Grid Model is NOT ready to use!")

        else:
            print ("OSM-Data downloaded: %s" %downloaded)


        # Copying QGis-Processing Scripts
            # Writing conn-File
        print ("Writing QGis-processing files...")
        conn_str = "host=%s port=%s user=%s dbname=%s password=%s" \
            %(self.host,self.port,self.user,self.database,self.password)

        if (sys.version_info >= (3, 0)):
            # Python 3 open
            fh = open(qgis_processing_path + "conn.txt","w")
        else:
            # Python 2 io.open to process data as binary, not as str
            fh = io.open(qgis_processing_path + "conn.txt","wb")

        fh.write(conn_str)
        fh.close()

            # Writing Processing files
        qgis_processing.write_processing(qgis_processing_path)

        # this can be disabled, due to version problems in QGis
        print ("Writing QGis-poject files...")
        qgis_projects.write_projects(database, password, host, port, user)

        print ("Grid Model is ready to use!")



    # Function to download OSM-Data
    # existing data is overwritten
    def download_osm_data(self, filename):
        if (sys.version_info >= (3, 0)):
            # Python 3 download
            urllib.request.urlretrieve("http://ftp5.gwdg.de/pub/misc/openstreetmap/download.geofabrik.de/germany-latest.osm.pbf", self.raw_data_dir + "/" + filename)
        else:
            # Python 2 download
            osm_data = urllib.URLopener()
            osm_data.retrieve("http://ftp5.gwdg.de/pub/misc/openstreetmap/download.geofabrik.de/germany-latest.osm.pbf", self.raw_data_dir + "/" + filename)

    # Function to filter OSM-Data
    def osmosis_filter(self, filename_raw, filename_filter):

        # Input and Output file_paths
        file_path = self.raw_data_dir + "/" + filename_raw
        output_file_path = self.raw_data_dir + "/" + filename_filter

        proc = subprocess.Popen('%s --rbf %s --tf accept-ways power=* --tf accept-relations route=power --used-node --wb %s'
                    %(self.osmosis_path, file_path, output_file_path), shell=True)

        print ("Filtering OSM-Data...")
        proc.wait() # To make sure Script waits until Osmosis is ready...

        print ("Filtering Complete!")

    # Function to import OSM-Data into Postgres Database and Create Tables
    def osmosis_import(self, filename, osm_date):

        # first, all OSM-Data is deleted
        self.cur.execute("""
        DELETE FROM users;
        DELETE FROM nodes;
        DELETE FROM relation_members;
        DELETE FROM relations;
        DELETE FROM way_nodes;
        DELETE FROM ways;
        """)
        self.conn.commit()

        file_path = self.raw_data_dir + "/" + filename

        # BUG: Python continues (and sets osm_metadata) even in case osmosis fails!!!
        proc = subprocess.Popen('%s --read-pbf %s --write-pgsql database=%s host=%s user=%s password=%s'
                         %(self.osmosis_path, 
                           file_path, 
                           self.database, 
                           self.osmosis_host, 
                           self.user, 
                           self.password), shell=True)
        print ('Importing OSM-Data...')
        proc.wait()

        # After updating OSM-Data, power_tables (for editing) have to be updated as well
        print ("Creating power-tables...")
        self.cur.execute("SELECT otg_create_power_tables ();")
        self.conn.commit()

        # Updates OSM Metadata
        v_now = datetime.datetime.now()
        v_date = str(v_now.year) + '-' + str(v_now.month) + '-' + str(v_now.day)

        self.cur.execute("UPDATE osm_metadata SET downloaded = '%s', imported = '%s'" %(osm_date, v_date)) # No good translation
        self.conn.commit()

        print ("Import Complete!")



    # Function to update database
    def update_osm_data(self):

        print ("Loading/updating OSM Data...")

        print ("""
        1. Download, filter and import OSM-Data \n
        2. Filter OSM-Data \n
        3. Import an existing (filtered) OSM-file into Database
        """)

        not_valid = True
        while not_valid:
            choice = input("What would you like to do?")

            if choice == '1':

                # date for file-naming
                v_now = datetime.datetime.now()
                if v_now.day < 10:
                    v_day = '0'+ str(v_now.day)
                else:
                    v_day = str(v_now.day)
                if v_now.month < 10:
                    v_month = '0'+ str(v_now.month)
                else:
                    v_month = str(v_now.month)

                v_date = str(v_now.year) + '-' + v_month + '-' + v_day

                filename_raw = "osm_germany_%s.osm.pbf" %v_date
                filename_filter = "powerfilter_" + filename_raw


                print ("Downloading OSM Data...")
                self.download_osm_data(filename_raw)

                print ("Filtering OSM Data...")
                self.osmosis_filter(filename_raw, filename_filter)

                self.osmosis_import(filename_filter, v_date)

                not_valid = False

                print ("Import/Update complete!")


            elif choice == '2':

                print ("""Info: Unfiltered osm.pbf-File needs to be in "raw_data"-Directory""")

                filename_raw = input("Name of raw OSM-file (e.g. germany-latest.osm.pbf):")
                filename_filter = input("Name of filtered (destination) OSM-file (e.g. germany-latest-filtered.osm.pbf):")


                self.osmosis_filter(filename_raw, filename_filter)

                not_valid = False


            elif choice == '3':

                print ("""Info: Filtered osm.pbf-File needs to be in "raw_data"-Directory""")

                filename_filter = input("Name of filtered OSM-file:")
                v_date = input("Download Date (E.g. 2015-10-23):")

                self.osmosis_import(filename_filter, v_date)

                not_valid = False


            else:
                print ("Not a valid answer!")





    def execute_abstraction(self,
                            v_plan_ids,
                            v_year,
                            min_voltage,
                            main_station,
                            graph_dfs,
                            conn_subgraphs,
                            transfer_busses,
                            comment = None): # None is 'translated' to NULL in Postgres (See: Adaptation of Python values to SQL types in Docu!)
        """
        Executes the abstraction.
        Takes 2 arguments: 1. Plan_IDs (String), 2. Year (INT).
        If no arguments are provided, abstraction will be executed without "Zubau".
        """

        # Applies Zubau to power_tables
        print ("Applies Zubau...")
        self.cur.execute("SELECT otg_apply_changes(%s, %s);", (v_plan_ids, v_year))
        self.conn.commit()

        # Updates (Inserts) abstraction parameters
                # Should be done in for-loop
        print ("Sets min_voltage...")
        self.cur.execute("""
            UPDATE abstr_values
                SET val_int = %s
                WHERE val_description = 'min_voltage'""", (min_voltage,))
        self.conn.commit()

        print ("Sets main_station...")
        self.cur.execute("""
            UPDATE abstr_values
                SET val_int = %s
                WHERE val_description = 'main_station'""", (main_station,))
        self.conn.commit()

        print ("Sets graph_dfs...")
        self.cur.execute("""
            UPDATE abstr_values
                SET val_bool = %s
                WHERE val_description = 'graph_dfs'""", (graph_dfs,))
        self.conn.commit()

        print ("Sets conn_subgraphs...")
        self.cur.execute("""
            UPDATE abstr_values
                SET val_bool = %s
                WHERE val_description = 'conn_subgraphs'""", (conn_subgraphs,))
        self.conn.commit()

        print ("Sets transfer_busses...") # Netzinseln
        self.cur.execute("""
            UPDATE abstr_values
                SET val_bool = %s
                WHERE val_description = 'transfer_busses'""", (transfer_busses,))
        self.conn.commit()
        
        if transfer_busses:
            tb_file_path = self.transfer_busses_dir + "/transfer_busses.csv"
            self.read_transfer_busses(tb_file_path)
    
        # Executes power_script
        print ("Executes Abstraction...")
        general_funcs.execute_sql(self.conn, self.cur, 'power_script.sql')

        print ("Saving Results...")
        self.cur.execute("SELECT otg_save_results (%s, %s, %s);", (v_plan_ids, v_year, comment))
        self.conn.commit()

        print ("Abstraction complete!")



    def write_to_csv (self, result_id, path):

        tables = ['bus_data', 'branch_data', 'dcline_data', 'substations', 'problem_log', 'plz_subst', 'nuts3_subst']
        for table in tables:

            print ('writing %s...' % table)

            filename = path + str(result_id) + '_' + table + ".csv"

            query = 'SELECT * FROM results.%s WHERE result_id = %s' %(table, str(result_id))

            outputquery = "COPY ({0}) TO STDOUT WITH DELIMITER ',' CSV HEADER".format(query)

            if (sys.version_info > (3, 0)):
                fh = open(filename, encoding='utf-8', mode = "w")
            else:
                fh = open(filename, "w")


            self.cur.copy_expert(outputquery, fh)

            fh.close()

        print ('All tables written to %s!' %path)


    def read_transfer_busses (self, file_path):

        # Deletes all entries of transfer_busses table
        self.cur.execute("""
DELETE FROM transfer_busses;
        """)
        self.conn.commit()

        reader = csv.reader(open(file_path, 'r'))
        next(reader, None) # Skips header

        print ("Copying transfer-busses from CSV to database...")
        for row in reader:
            osm_id = str(row[10])
        
            if osm_id[:1] == 'w':
                object_type = 'way'
            elif osm_id[:1] == 'n':
                object_type = 'node'
            else:
                object_type = None
        
            osm_id_int = int(osm_id[1:])
            
            center_geom = str(row[5])
        
            self.cur.execute("""
INSERT INTO transfer_busses (osm_id, object_type, center_geom)
    VALUES (%s, %s, %s);
            """, (osm_id_int, object_type, center_geom))
            self.conn.commit()


    def insert_plan(self, id, name, comment):
        self.cur.execute ("INSERT INTO entwicklungsplan (id, plan, comment) VALUES (%s, %s, %s)", (id, name, comment))
        self.conn.commit()

        print ("Plan successfully inserted!")


    def copy_plan(self, plan_id_old, plan_id_new):

        self.cur.execute ("""
            INSERT INTO anwendung_aenderung (aenderungs_id, plan_id, jahr, plan_intern_id, copied, copied_from)
                SELECT aenderungs_id, %s, jahr, plan_intern_id, TRUE, %s
                    FROM anwendung_aenderung
                    WHERE plan_id = %s""", (plan_id_new, plan_id_old, plan_id_old))
        self.conn.commit()

        print ("Plan successfully copied!")


    def information (self):

        print ("""
        You can display the following information: \n
        1. OSM - Metadata \n
        2. Grid-Development-Plans \n
        3. Result-Metadata \n
        4. Quit
        """)

        choice = input("Make a choice:")

        if choice == '1':

            try:
                self.cur.execute("SELECT downloaded, imported FROM osm_metadata;")
                table =  self.cur.fetchall()
                for record in table:
                    print ("Downloaded: ", record[0])
                    print ("Imported:", record[1])
            except:
                # Get the most recent exception
                exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                print ('Error while fetching Data! Error: %s' %(exceptionValue))

        if choice == '2':

            try:
                self.cur.execute("SELECT id, plan, comment FROM entwicklungsplan;")
                table =  self.cur.fetchall()
                for record in table:
                    print ("ID: ", record[0])
                    print ("Grid-Development-Plan:", record[1])
                    print ("Comment:", record[2])
            except:
                # Get the most recent exception
                exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                print ('Error while fetching Data! Error: %s' %(exceptionValue))

        if choice == '3':

            try:
                self.cur.execute("SELECT id, osm_date, abstraction_date, applied_plans, applied_year, user_comment FROM results.results_metadata;")
                table =  self.cur.fetchall()
                for record in table:
                    print ("ID: ", record[0])
                    print ("OSM-Downloaded:", record[1])
                    print ("Abstraction Date:", record[2])
                    print ("Applied Devel. Plans:", record[3])
                    print ("Applied Devel. Year:", record[4])
                    print ("User Comment:", record[5])
                    print ('--------------------------')
            except:
                # Get the most recent exception
                exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                print ('Error while fetching Data! Error: %s' %(exceptionValue))

        elif choice == '4':

            print ("Quit!")




## Loads grid model if executed as script...
if __name__ == '__main__':

    print ('osmTGmod executed as Script')
    print ('Please provide connection-parameters:')

    database = input('Database name:')
    password = input('Server password:')

    if platform.system().lower() == "win32" or platform.system().lower() == "windows":
        if os.path.exists(os.getenv("USERPROFILE") + "/.qgis2/processing/scripts/"):
           qgis_processing_path = os.getenv("USERPROFILE") + "/.qgis2/processing/scripts/"
           # In case the processing path cannot be found it must be manually definded
        else:
            qgis_processing_path = input("No QGis processing path found! Provide QGis-Processing Path:")
    else:
         if os.path.exists(os.getenv("HOME") + "/.qgis2/processing/scripts/"):
            qgis_processing_path = os.getenv("HOME") + "/.qgis2/processing/scripts/"
            # In case the processing path cannot be found it must be manually definded
        else:
            qgis_processing_path = input("No QGis processing path found! Provide QGis-Processing Path:")

    host = input('host (default localhost):') or 'localhost' #'192.168.0.46'
    port = input('port (default 5432):') or '5432'
    user = input('user (default postgres):') or 'postgres'


    print ('Grid Model Object is created...')
    grid_model = grid_model(database, password, qgis_processing_path, host, port, user)

    not_valid = True
    while not_valid:
        print ("""
        Options: \n
        1. Import/Update/Filter OSM-Data \n
        2. Start an Abstraction \n
        3. Export Results to CSV \n
        4. View Results/OSM - Metadata, Grid-Devel.-Plans \n
        5. Insert new (empty) Grid Development Plan \n
        6. Copy Development-Measure from one Grid-Development-Plan to another (expert) \n
        7. Quit
        """)

        choice = input("What would you like to do?")

        if choice == '1':

            try:
                grid_model.update_osm_data()

            except:
                # Get the most recent exception
                exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                print ('Error while updating/importing! Error: %s' %(exceptionValue))

        elif choice == '2':

            plan_ids = input("Development plan IDs (e.g. 1;2) (default None):") or None

            year = input("Year of application (e.g. 2020) (default None):") or None

            min_voltage = input("Minimal considered voltage (default 220000):") or 220000

            main_station = input("Substation with slack node (OSM-ID) (default 35176751):") or 35176751

            graph_dfs_input = input("Delete disconnected (sub-)graphs (default No)?:") or 'no'
            graph_dfs = general_funcs.ask_yes_no(graph_dfs_input) # Returns True for yes input

            if graph_dfs == False: # If Disconnected Graphs are not deleted
                conn_subgraphs_input = input("Connect subgrids (disconnected subgraphs) to main grid (dafault No)?:") or 'no'
                conn_subgraphs = general_funcs.ask_yes_no(conn_subgraphs_input) # Returns True for yes input
            else:
                conn_subgraphs = False # In case Subgraphs are deleted, a connection of these doesn't make sense


            transfer_busses_input = input( \
            "Connect disconnected transfer busses (predefined 'Netzinseln') to nearest grid-connected " \
            "substation (default No)?:") or 'no'
            transfer_busses = general_funcs.ask_yes_no(transfer_busses_input)

#            cond_file_good = False
#            while not cond_file_good:
#                # Better if file exists:, dann machen und weiter, sonst input...
#                try:
#                    grid_model.read_transfer_busses(file_path)
#                    cond_file_good = True
#                except:
#                    input("Press Enter to continue...")
#
#            print ("geht weiter...")
             # Ich sollte mich nochmal mit Try und Except beschäftigen
             # Besser nicht verwenden, da Stabili

            user_comment = input("User comment:") or None

            try:
                grid_model.execute_abstraction(plan_ids,
                                               year,
                                               min_voltage,
                                               main_station,
                                               graph_dfs,
                                               conn_subgraphs,
                                               transfer_busses,
                                               user_comment)
            except:
                # Get the most recent exception
                exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                print ('Error while abstracting! Error: %s' %(exceptionValue))

        elif choice == '3':
            result_dir = os.path.dirname(os.getcwd()) + "/results/"
            result_id = input("Result ID:")
            path = input("Result Path (default: "+result_dir+"):") or result_dir

            try:
                grid_model.write_to_csv(result_id, path)
            except:
                # Get the most recent exception
                exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                print ('Error while exporting CSV! Error: %s' %(exceptionValue))

        elif choice == '4':

            grid_model.information()


        elif choice == '5':
            print ('Existing Development-Plans:')
            try:
                grid_model.cur.execute("SELECT id, plan, comment FROM entwicklungsplan;")
                table =  grid_model.cur.fetchall()
                for record in table:
                    print ("ID: ", record[0])
                    print ("Grid-Development-Plan:", record[1])
                    print ("Comment:", record[2])
            except:
                # Get the most recent exception
                exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                print ('Error while fetching Data! Error: %s' %(exceptionValue))

            id = input("New ID of Development-Plan: ")
            name = input("Name of new (empty) Development-Plan (e.g. EnlaG):")
            comment= input("Comment:")

            try:
                grid_model.insert_plan(id, name, comment)
            except:
                # Get the most recent exception
                exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                print ('Error while inserting Plan! Error: %s' %(exceptionValue))


        elif choice == '6':
            old = input("ID of Plan FROM witch Measurements will be copied:")
            new = input("ID of Plan TO witch Measurements will be copied (Plan must exist):")

            try:
                grid_model.copy_plan(old, new)
            except:
                # Get the most recent exception
                exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                print ('Error while copying Plan! Error: %s' %(exceptionValue))

        elif choice == '7':

            not_valid = False
            print ("Quit!")

        else:
            print ("Not a valid answer!")
