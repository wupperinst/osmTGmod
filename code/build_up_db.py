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

import general_funcs

# Function to load (first time) the model
def build_up_db(conn, cur):

    # LOADS FUNCTIONS AND RESULT SCHEMA

    print "Loading Functions and Result-Schema..."
    # Loads Extensions, Functions, Boundaries, Electrical Properties and Zubau_DB
    # Sripts can be executed again when "reloading" Grid Model
    scripts = ['extensions.sql', 'functions.sql', 'admin_boundaries.sql', 'electrical_properties.sql', 'grid_development.sql', 'build_up_db.sql']

    for script in scripts:
        general_funcs.execute_sql(conn, cur, script)

    cur.execute ("""UPDATE _db_status SET status = TRUE WHERE module = 'grid_model'; """)

    conn.commit()

    print 'osmTGmod-database has been built up!'