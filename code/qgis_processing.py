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

# Writes QGis Processing Scripts into QGis-Processing-Folder. Scripts get Connection Information from Conn-File (created when Grid_model is initialized)

## Processing for grid development
def write_processing(qgis_processing_path):


    new_relation ='''##voltage=number 220000
##cables=number 3
##wires=string double
##frequency=number 50

# Importiert Module
from qgis.core import *
from PyQt4.QtCore import *
import psycopg2

fh = open("''' + qgis_processing_path + '''conn.txt","r")
conn_str = fh.read()
fh.close()


# Creates Database Connection
conn = psycopg2.connect(conn_str)
cur = conn.cursor()

# loads power_ways and vw_change_log into variables
power_ways = processing.getObject('power_ways')
vw_change_log = processing.getObject('vw_change_log')

 # Schreibt Mitgliederinformationen in Liste (Listen werden in SQL zu Arrays - translation)
v_members = []
for i in power_ways.selectedFeatures():
    v_members.append(i['id'])

for i in vw_change_log.selectedFeatures():
    v_members.append(i['osm_id'])

# Rxecutes SQL to write in vw_power_relations
cur.execute("""
INSERT INTO edit_power_relations
        (   voltage,
            cables,
            wires,
            frequency,
            members)
            VALUES (%s, %s, %s, %s, %s);
""", (voltage, cables, wires, frequency, v_members))
conn.commit()

print ('Relation wurde gespeichert')
'''

    fh = open(qgis_processing_path + "new_relation.py","w")
    fh.write(new_relation)
    fh.close()


    metadata_grid_development = '''##plan_id=string 1;2
##year=number 2020
##plan_intern_id=string 1a;1a
##description=string
##user_comment=string

import psycopg2

fh = open("''' + qgis_processing_path + '''conn.txt","r")
conn_str = fh.read()
fh.close()

# Creates Database Connection
conn = psycopg2.connect(conn_str)
cur = conn.cursor()

# Executes SQL query toool
cur.execute("""
UPDATE zuordnung
    SET   plan_id = %s,
            jahr = %s,
            plan_intern_id = %s,
            description = %s,
            user_comment = %s;
""", (plan_id, year, plan_intern_id, description, user_comment))
conn.commit()

print ('Zuordnung wurde gespeichert und Change_log-View erneuert') '''

    fh = open(qgis_processing_path + "metadata_grid_development.py","w")
    fh.write(metadata_grid_development)
    fh.close()


## Processing for result visualisation

    show_results = '''##result_id=number 1

import psycopg2

fh = open("''' + qgis_processing_path + '''conn.txt","r")
conn_str = fh.read()
fh.close()

# Creates Database Connection
conn = psycopg2.connect(conn_str)
cur = conn.cursor()

# Executes SQL query toool
cur.execute("""
UPDATE results.view_results
    SET   result_id = %s;
""", (result_id,))
conn.commit()

print ('Result Nr. %s is displayed.' %(result_id)) '''

    fh = open(qgis_processing_path + "show_results.py","w")
    fh.write(show_results)
    fh.close()