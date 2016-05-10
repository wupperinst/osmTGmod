# -*- coding: utf-8 -*-
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

import codecs # Necessary in Python 3 (no standard String encoding)

# Function to execute entire SQL file
def execute_sql (conn, cur, filepath):
    # Can't remember why one has to use utf-8-sig
    fd = codecs.open(filepath, 'r', "utf-8-sig")
    
    sqlfile = fd.read()
    
    fd.close()

    print ('Executing SQL-file %s...' %filepath)
    cur.execute(sqlfile)
    conn.commit()

    print ('SQL-file %s executed!' %filepath)


# Yes-No function
def ask_yes_no(choice):

    yes = set(['yes','y', 'ye', '']) # Enter means yes!
    no = set(['no','n'])

    while True:
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            choice = input("Please answer Yes or No:").lower()

