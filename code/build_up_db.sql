-----------------------------------------------------------------------------------
--                                                                                 
--  Copyright "2015" "Wuppertal Institut"                                         
--                                                                                
--  Licensed under the Apache License, Version 2.0 (the "License");               
--  you may not use this file except in compliance with the License.              
--  You may obtain a copy of the License at                                       
--                                                                                
--      http://www.apache.org/licenses/LICENSE-2.0                                
--                                                                                
--  Unless required by applicable law or agreed to in writing, software           
--  distributed under the License is distributed on an "AS IS" BASIS,             
--  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.      
--  See the License for the specific language governing permissions and           
--  limitations under the License.                                                
--                                                                                
-----------------------------------------------------------------------------------  
                 
CREATE SCHEMA IF NOT EXISTS results;

DROP VIEW IF EXISTS results.view_bus_data;
DROP VIEW IF EXISTS results.view_branch_data;
DROP VIEW IF EXISTS results.view_dcline_data;
DROP VIEW IF EXISTS results.view_substations;
DROP VIEW IF EXISTS results.view_problem_log;

DROP TABLE IF EXISTS results.view_results;
CREATE TABLE results.view_results (result_id INT);
INSERT INTO results.view_results VALUES (NULL);


CREATE TABLE IF NOT EXISTS results.results_metadata(
	id INT NOT NULL PRIMARY KEY,
	osm_date DATE,
	abstraction_date DATE,
	applied_plans TEXT,
	applied_year INT,
	user_comment TEXT);

CREATE TABLE IF NOT EXISTS results.bus_data(


		result_id INT,
		view_id SERIAL NOT NULL PRIMARY KEY,
		
		---------Matpower information---------
		
                bus_i BIGINT,            --bus number
                bus_type INTEGER,   --bus type (1 = PQ, 2 = PV, 3 = ref, 4 = isolated)
                pd NUMERIC,               --real power demand (MW)
                qd NUMERIC,               --reactive power demand (MVAr)
                gs NUMERIC,             --shunt conductance (MW demanded at V = 1.0 p.u.)
                bs NUMERIC,             --shunt susceptance (MVAr injected at V = 1.0 p.u.)
                bus_area INTEGER,   --area number (positive integer)
                vm NUMERIC,               --voltage magnitude (p.u.)
                va NUMERIC,               --voltage angle (degrees)
                base_kv NUMERIC,   --base voltage (kV) (des jeweiligen Knotens (hieruber wird auch Trafoubersetzung bestimmt))
                zone INTEGER,           --loss zone (positive integer)
                vmax NUMERIC,           --maximum voltage magnitude (p.u.) (optional)
                vmin NUMERIC,           --minimum voltage magnitude (p.u.) (optional)

		---------extra information---------

                osm_substation_id BIGINT, -- OSM-Substation ID
                cntr_id CHARACTER VARYING(2),     -- Country ID
                frequency NUMERIC, --frequency
                geom geometry(Point, 4326),        -- Point Geometry (Not simplified) WGS84
                osm_name TEXT);

ALTER TABLE results.bus_data DROP CONSTRAINT IF EXISTS result_fk;		
ALTER TABLE results.bus_data
	ADD CONSTRAINT result_fk foreign key (result_id) references results.results_metadata (id) ON DELETE CASCADE;

CREATE OR REPLACE VIEW results.view_bus_data AS 
	SELECT * FROM results.bus_data 
	WHERE result_id = (SELECT result_id FROM results.view_results);
                       
CREATE TABLE IF NOT EXISTS results.branch_data(

		result_id INT,
		view_id SERIAL NOT NULL PRIMARY KEY,
		branch_id BIGINT,
		
		---------Matpower information---------
		
                f_bus BIGINT,         --from bus number
                t_bus BIGINT,         --to bus number
                br_r NUMERIC,           --resistance (p.u.)
                br_x NUMERIC,           --reactance (p.u.)
                br_b NUMERIC,           --total line charging susceptance (p.u.)
                rate_a NUMERIC, --MVA rating A (long term rating) (optional)
                rate_b NUMERIC,         --MVA rating B (short term rating) (optional)
                rate_c NUMERIC,         --MVA rating C (emergency rating) (optional)
                tap NUMERIC,	            --transformer off nominal turns ratio, (taps at from bus)
                                                    --(impedance at to bus), i.e. if r = x = 0, tap = ...
                shift NUMERIC,	        --transformer phase shift angle (degrees), positive ) delay
                br_status INTEGER,         --initial branch status, 1 = in-service, 0 = out-of-service

		---------extra information---------

                link_type TEXT,     -- Transformer, Line, Cable...
                branch_voltage INT, --Branch voltage
                cables INT,
                frequency NUMERIC, 
                geom geometry (MultiLineString, 4326),-- Line Geometry (Not simplified) WGS84
                topo geometry (LineString, 4326));     -- Line Geometry (simplified) WGS84

ALTER TABLE results.branch_data DROP CONSTRAINT IF EXISTS result_fk;		
ALTER TABLE results.branch_data 
	ADD CONSTRAINT result_fk foreign key (result_id) references results.results_metadata (id) ON DELETE CASCADE;

CREATE OR REPLACE VIEW results.view_branch_data AS 
	SELECT * FROM results.branch_data 
	WHERE result_id = (SELECT result_id FROM results.view_results);
		
CREATE TABLE IF NOT EXISTS results.dcline_data (

		result_id INT,
		view_id SERIAL NOT NULL PRIMARY KEY,
		dcline_id BIGINT,

		---------Matpower information---------
		
                f_bus BIGINT,
                t_bus BIGINT,
                br_status INTEGER,
                pf NUMERIC, -- Power has to be adjusted!!
                pt NUMERIC,
                qf NUMERIC,
                qt NUMERIC,
                vf NUMERIC,
                vt NUMERIC,
		pmin NUMERIC,
		pmax NUMERIC,
		qminf NUMERIC,
		qmaxf NUMERIC,
		qmint NUMERIC,
		qmaxt NUMERIC,
		loss0 NUMERIC,
		loss1 NUMERIC,

                ---------extra information---------

               link_type TEXT,     -- Transformer, Line, Cable...
               branch_voltage INT, --Branch voltage
               cables INT,
               frequency NUMERIC, 
               geom geometry (MultiLineString, 4326), -- Line Geometry (Not simplified) WGS84
               topo geometry (LineString, 4326));    

ALTER TABLE results.dcline_data DROP CONSTRAINT IF EXISTS result_fk;		
ALTER TABLE results.dcline_data 
	ADD CONSTRAINT result_fk foreign key (result_id) references results.results_metadata (id) ON DELETE CASCADE;

CREATE OR REPLACE VIEW results.view_dcline_data AS 
	SELECT * FROM results.dcline_data 
	WHERE result_id = (SELECT result_id FROM results.view_results);

		
CREATE TABLE IF NOT EXISTS results.nuts3_subst(
		result_id INT,
		nuts_id Character Varying (14),
		substation_id BIGINT,
		percentage NUMERIC,
		distance NUMERIC);

ALTER TABLE results.nuts3_subst DROP CONSTRAINT IF EXISTS result_fk;		
ALTER TABLE results.nuts3_subst 
	ADD CONSTRAINT result_fk foreign key (result_id) references results.results_metadata (id) ON DELETE CASCADE;
	
CREATE TABLE IF NOT EXISTS results.plz_subst(
		result_id INT,
		plz INTEGER,
		substation_id BIGINT,
		percentage NUMERIC,
		distance NUMERIC);

ALTER TABLE results.plz_subst DROP CONSTRAINT IF EXISTS result_fk;		
ALTER TABLE results.plz_subst
	ADD CONSTRAINT result_fk foreign key (result_id) references results.results_metadata (id) ON DELETE CASCADE;


CREATE TABLE IF NOT EXISTS results.substations(
		result_id INT,
		view_id SERIAL NOT NULL PRIMARY KEY,
		
		osm_id BIGINT,
		voltage TEXT,
		s_long NUMERIC,
		name TEXT,
		geom geometry (Polygon, 4326),
		center_geom geometry (Point, 4326));

ALTER TABLE results.substations DROP CONSTRAINT IF EXISTS result_fk;		
ALTER TABLE results.substations
	ADD CONSTRAINT result_fk foreign key (result_id) references results.results_metadata (id) ON DELETE CASCADE;
	
CREATE OR REPLACE VIEW results.view_substations AS 
	SELECT * FROM results.substations
	WHERE result_id = (SELECT result_id FROM results.view_results);

	
CREATE TABLE IF NOT EXISTS results.problem_log (	
		result_id INT,
		view_id SERIAL NOT NULL PRIMARY KEY,
		
		object_type TEXT, -- Objekt-Typ des dargestellten Elements
		line_id BIGINT [], -- Alle im Objekt enthaltenen lines (ways)
		relation_id BIGINT, -- Relation_id des Objekts (0 für Branches, die aus ways stammen)
		way geometry (MultiLineString, 4326), 
		voltage INT,
		cables INT,
		wires INT, 
		frequency REAL,
		problem TEXT); -- Beschreibung des entsprechenden Problems

ALTER TABLE results.problem_log DROP CONSTRAINT IF EXISTS result_fk;		
ALTER TABLE results.problem_log
	ADD CONSTRAINT result_fk foreign key (result_id) references results.results_metadata (id) ON DELETE CASCADE;
	
CREATE OR REPLACE VIEW results.view_problem_log AS 
	SELECT * FROM results.problem_log
	WHERE result_id = (SELECT result_id FROM results.view_results);
	
-- DROP TABLE IF EXISTS main_station;
-- CREATE TABLE main_station (main_station_id BIGINT);
-- INSERT INTO main_station VALUES (NULL);

-- Table for important abstraction values (still not entirely in use)
DROP TABLE IF EXISTS abstr_values;
CREATE TABLE abstr_values (	val_id SERIAL NOT NULL PRIMARY KEY,
				val_description TEXT,
				val_int BIGINT,
				val_bool BOOLEAN);
INSERT INTO abstr_values VALUES (	DEFAULT,
					'min_voltage',
					NULL,
					NULL); 
INSERT INTO abstr_values VALUES (	DEFAULT,
					'main_station',
					NULL,
					NULL);
INSERT INTO abstr_values VALUES (	DEFAULT,
					'base_MVA',
					100,
					NULL);
INSERT INTO abstr_values VALUES (	DEFAULT,
					'graph_dfs',
					NULL,
					NULL);
INSERT INTO abstr_values VALUES (	DEFAULT,
					'conn_subgraphs',
					NULL,
					NULL);

--Other functions access this osm_metadata
DROP TABLE IF EXISTS osm_metadata;
CREATE TABLE osm_metadata (downloaded date, imported date);
INSERT INTO osm_metadata (downloaded, imported) VALUES (NULL, NULL);

 
