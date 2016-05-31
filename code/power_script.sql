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

------------------------------------------------------------------------------------------------
-- POWER OSM DATENUMWANDLUNG
------------------------------------------------------------------------------------------------

-- Konvention:
-- Alle Werte von Variablen sind in üblichen S.I. Einheiten, falls im Variablenname keine (abweichende) Einheit angegeben ist.

-- DROP TABELLEN

DROP TABLE IF EXISTS power_circ_members;
DROP TABLE IF EXISTS power_circuits;

DROP TABLE IF EXISTS power_line;
DROP TABLE IF EXISTS power_substation;

DROP TABLE IF EXISTS power_line_sep;

DROP TABLE IF EXISTS branch_data;
DROP TABLE IF EXISTS bus_data;
DROP TABLE IF EXISTS dcline_data;

DROP TABLE IF EXISTS problem_log;

-- This table can optionally be used for debugging
CREATE TABLE IF NOT EXISTS debug_vals (explanation TEXT, value TEXT);
DELETE FROM debug_vals;
--Example usage:
--INSERT INTO debug_vals VALUES ('Explanation', 'whatever_value'::TEXT);


-- ERSTELLUNG ALLGEMEINER TABELLEN (DEKLARIERUNG EINIGER VARIABLEN)


	-- ERSTELLEN DER TOPOLOGIE-TABELLEN
	-- (Diese werden später mit der topologischen Netzstruktur gefüllt)

		-- BUS_DATA	

CREATE TABLE bus_data (	
	id BIGINT PRIMARY KEY,
	cnt INT,
	the_geom geometry (Point, 4326),
	voltage INT,
	frequency REAL,
	substation_id BIGINT,
	buffered BOOLEAN
);
		
CREATE INDEX bus_id_idx ON bus_data(id);
CREATE INDEX bus_the_geom_idx ON bus_data(the_geom);

		-- BRANCH_DATA

CREATE TABLE branch_data (	
	branch_id serial NOT NULL PRIMARY KEY,
	relation_id BIGINT,
	line_id BIGINT,
	length REAL,
	way geometry (LineString),
	f_bus BIGINT,
	t_bus BIGINT,
	voltage INT,
	cables INT,
	wires INT,
	frequency REAL,
	power TEXT
);
				

CREATE INDEX branch_f_bus_idx ON branch_data (f_bus);
CREATE INDEX branch_t_bus_idx ON branch_data (t_bus);


	-- ERSTELLEN DER PROBLEM_LOG-TABELLE UND COUNT-LOG
	-- (in diese Tabelle werden alle Probleme eingetragen, die explizit über Trigger oder Inserts in diese Tabelle eingefügt werden)
	
CREATE TABLE problem_log (	object_type TEXT, -- Objekt-Typ des dargestellten Elements
				line_id BIGINT [], -- Alle im Objekt enthaltenen lines (ways)
				relation_id BIGINT, -- Relation_id des Objekts (0 für Branches, die aus ways stammen)
				way geometry (MultiLineString, 4326), 
				voltage INT,
				cables INT,
				wires INT, 
				frequency REAL,
				problem TEXT); -- Beschreibung des entsprechenden Problems


-- DATENUMWANDLUNG POWER_LINE 
-- (Untersuchung aller in den OSM-ways enthaltenen Informationen)

	-- ERSTELLEN DER TABELLE POWER_LINE	
	-- (Diese Tabelle wird die way-Informationen über Leitungen (Freileitungen und Kabel) enthalten)
SELECT *
	INTO power_line
	FROM power_ways_applied_changes
	WHERE 	power = 'line' OR
		power = 'cable';

-- Erstellt normalen Index auf ID und  spatial Index (räumlichen Index) auf way
CREATE INDEX power_line_id_idx ON power_line(id);
CREATE INDEX power_line_way_gix ON power_line USING GIST (way);

			
	-- ERSTELLEN DER TABELLE POWER_SUBSTATION
	-- (Diese Tabelle wird die way-Informationen über Umspannwerke enthalten)

SELECT *
	INTO power_substation
	FROM power_ways_applied_changes
	WHERE 	power = ANY (ARRAY ['substation','sub_station','station']); 

-- Erstellt einen normalen Index auf ID
CREATE INDEX substation_id_idx ON power_substation(id);

-- Es werden diejenigen ways gelöscht, die kein Polygon darstellen können
-- (in der power_ways- Tabelle liegen alle wege als linestring vor)
DELETE FROM power_substation WHERE ST_NumPoints (way) <= 3; -- Polygone brauchen mindestens 4 Punkte

-- Aus der way-Spalte wird Geometrie polygon gemacht.
ALTER TABLE power_substation ADD COLUMN poly geometry(Polygon, 4326);
-- Aus Linestrings werden Polygone gemacht
-- (Um sicherzugehen, dass Linestrings geschlossen sind wird ihr Startpunk als Endpunkt hinzugefügt)
UPDATE power_substation 
	SET poly = ST_MakePolygon(ST_AddPoint(way, ST_StartPoint(way))); 
-- Spalte way (linestrings) wird gelöscht
ALTER TABLE power_substation DROP COLUMN way; 

-- Macht einen spatial Index auf Geometriespalte poly
CREATE INDEX substation_poly_gix ON power_substation USING GIST (poly);


	-- GEOMETRIE POWER_LINE
	-- (Zunächst handelt es sich lediglich um geometrische Informationen - keine Topologie)

-- Macht zwei neue Geometrie-Spalten, in die die Start- und Endpunkte eingetragen werden...
ALTER TABLE power_line ADD COLUMN startpoint geometry (Point);
ALTER TABLE power_line ADD COLUMN endpoint geometry (Point);
-- ...und erstellt Indizes auf diese
CREATE INDEX startpoint_gix ON power_line USING GIST (startpoint);
CREATE INDEX endpoint_gix ON power_line USING GIST (endpoint);

-- Start- und Endpunkte werden eingetragen
UPDATE power_line
	SET
	startpoint = st_startpoint(way),
	endpoint = st_endpoint(way);


-- Es werden alle Leitungen gelöscht, die Anfang und Ende außerhalb Deutschlands haben.	
DELETE FROM power_line WHERE 	NOT id IN	(SELECT line.id 
						FROM power_line line, nuts_poly
						WHERE 	ST_Within(line.startpoint, nuts_poly.geom) AND
							nuts_poly.nuts_id = 'DE') AND
						
				NOT id IN	(SELECT line.id 
						FROM power_line line, nuts_poly
						WHERE 	ST_Within(line.endpoint, nuts_poly.geom) AND
							nuts_poly.nuts_id = 'DE');


	-- BEZIEHUNG POWER_LINE/POWER SUBSTATION



-- Macht eine neue Spalte, die die mögliche Substation-ID der Start- und Endpunkte der Leitung erhält.
-- Untersuchung ob Anfangs- und Endpunkte der Leitungen innerhalb einer Substation liegen
ALTER TABLE power_line ADD COLUMN point_substation_id BIGINT [2];
UPDATE power_line SET 	point_substation_id [1] = (SELECT power_substation.id
							FROM power_substation
							WHERE ST_Within(startpoint, power_substation.poly)
							LIMIT 1),
			point_substation_id [2] = (SELECT power_substation.id
							FROM power_substation
							WHERE ST_Within(endpoint, power_substation.poly)
							LIMIT 1);

-- Alle Leitungen, die Anfang und Ende innerhalb einer Substation liegen werden gelöscht.							
DELETE FROM power_line WHERE point_substation_id [1] = point_substation_id [2];	

-- DELETE FROM power_line 
-- 	WHERE  id IN (SELECT power_line.id 
-- 			FROM power_line, power_substation
-- 			WHERE ST_Within(power_line.way, power_substation.poly));

	
	-- UNTERSUCHUNG SPANNUNGSEBENEN
--UPDATe power_line SET frequency = '0' WHERE id = 316867863

-- Mach Neue Spalte mit Anzahl Spannungs-level...
-- ...und füllt diese mit der Anzahl Voltage levels
ALTER TABLE power_line ADD COLUMN numb_volt_lev INT;

UPDATE power_line 
	SET numb_volt_lev = otg_numb_of_cert_char (voltage, ';') + 1;
	
-- Jede Zeile des ARRAYs (neue Spalte voltage_array) enthält die Spannung der jeweiligen Leitungs-Ebene
-- (Es werden die 4 oberen Leitungsebenen einer Leitung betrachtet)
ALTER TABLE power_line ADD COLUMN voltage_array INT [4];
CREATE INDEX volt_idx ON power_line(voltage_array);
UPDATE power_line 
	SET 
	voltage_array [1] = otg_get_int_from_semic_string (voltage, 1),
	voltage_array [2] = otg_get_int_from_semic_string (voltage, 2), 
	voltage_array [3] = otg_get_int_from_semic_string (voltage, 3), 
	voltage_array [4] = otg_get_int_from_semic_string (voltage, 4);

	
		-- PROBLEM: NULL_voltage
		-- (Es werden alle power_lines gelöscht, die keine Spannungsinformationen besitzen)
	
	CREATE TRIGGER problem_log_trigger
		AFTER DELETE ON power_line
		FOR EACH ROW 
		EXECUTE PROCEDURE otg_power_line_problem_tg ('NULL_voltage');

		DELETE FROM power_line
			WHERE 		voltage_array [1] IS NULL
				AND 	voltage_array [2] IS NULL
				AND 	voltage_array [3] IS NULL
				AND 	voltage_array [4] IS NULL;
			
	DROP TRIGGER problem_log_trigger ON power_line;
	
	
	-- UNTERSUCHUNG CABLES

-- Spalte cables_sum in die die aus cables (TEXT-Datentyp) stammenden Kabelsummen der Leitungen eingetragen wird
-- (Siehe Funktion otg_calc_sum_from_semic_string () für Verständnis der Berechnung)
ALTER TABLE power_line ADD COLUMN cables_sum INT;
UPDATE power_line
	SET cables_sum = otg_calc_sum_from_semic_string (cables)
	WHERE power = 'line'; -- Für Kabel nicht definiert!
	
-- Neue Spalte cables_array, die ähnlich voltage_array die Anzahl der Leiterseile pro Spannungsebene enthält
ALTER TABLE power_line ADD COLUMN cables_array INT [4];
UPDATE power_line 
	SET 
	cables_array [1] = otg_get_int_from_semic_string (cables, 1),
	cables_array [2] = otg_get_int_from_semic_string (cables, 2),
	cables_array [3] = otg_get_int_from_semic_string (cables, 3),
	cables_array [4] = otg_get_int_from_semic_string (cables, 4)
	WHERE 
	numb_volt_lev - 1 = otg_numb_of_cert_char (cables, ';'); -- Dort, wo die Cables pro Spannungsebene genau identifizierbar sind (Anzahl ';' übereinsimmen)

	

	-- UNTERSUCHUNG WIRES
	
-- Neue Spalte wires_array, die ähnlich voltage_array und cables_array die Anzahl der Leiterseile im Bündelleiter pro Spannungsebene enthält
ALTER TABLE power_line ADD COLUMN wires_array INT [4];

SELECT otg_read_wires ();


	-- UNTERSUCHUNG FREQUENCY
	
ALTER TABLE power_line ADD COLUMN frequency_array REAL [4]; 

-- Mit dieser Funktion wird die Frequenz (String-Spalte) in ein Frequenz-Array (Spannungsebenen) überführt.
-- Die Werte der Frequency werden nur verwertet, falls es nur einen Wert gibt (meist 50 Hz).
-- Frequency-key stellt nur Auflistug dar (nicht zu Spannungsebenen zuzuordnen),...
-- ... daher: Alle weiteren Informationen müssen von Relations kommen
SELECT otg_read_frequency ();



	-- UNTERSUCHUNG CIRCUITS
	-- (In der Tabelle power_line enthaltene Stromkreis-Informationen)
	-- (Diese Beschränken sich idR. auf Erdkabel, da bei diesen die Anzahl "Leiterseile" für OSM-Mapper in diesem Fall nicht zu ermitteln ist)

-- Die Informationen von circuits und cables werden bei Erdkabeln zusammengeführt...
-- ... Ein circuit ist dabei äquivalent 2 oder 3 cables
-- Der Circuit-Eintrag wird nur betrachtet, falls cables noch unbekannt ist
-- (Cables ist damit der "wichtigere" Tag

-- Zukünftig könnte noch komplett aus Circuits umgestellt werden um diese als zentralen wert zu betrachten.
-- Die Stromkreise werden kann nicht von den Cables, sondern der Anzahl Stromkreise abgezogen werden.

SELECT otg_read_circuits ();


	-- UNTERSUCHUNG LEITUNGSLÄNGE

-- Neue Spalte (length) die tatsächliche Länge in metern der Leiterseile (nicht Mastabstände) enthält
ALTER TABLE power_line ADD COLUMN length real; 
-- Durch de Funktion st_length wird die Länge der Leitungen in m berechnet.
-- Hierfür wird way ("geometry") in "geography" umgewandelt...
--... st_length erkennt geography-types (als WGS 84) und gibt Werte in m zurück
-- Die von QGis (Visualisiertung) berechneten Längen scheinen nicht zu stimmen
UPDATE power_line
	SET length = st_length(way::geography);
	-- WHERE power = 'cable';
-- Für alle Freileitungen wird eine mittleres Verhältnis zwischen tatsächlicher Länge und Mastabstand...
-- ... (aufgrund von Seildurchhang) von 1.07 angenommen
-- Für diesen Wert kann z.Z. keine Quelle gefunden werden		
-- UPDATE power_line
-- 	SET length = st_length(way::geography) * 1.07 --gilt so nicht!
-- 	WHERE power = 'line';	
	

	-- UNTERSUCHUNG NACHBARSCHAFT
	-- (Untersuchung der Nachbarschaft wird unternommen, um eindeutige Leitungsinformationen vollständig gemappter Leitungen an benachbarte Leitung mit fehlenden Einträgen (mapping-Fehler) zu übergeben)
	
-- Neue Spalte (all_neighbours BIGINT ARRAY), in die alle geeignete Nachbarn eingetragen werden
ALTER TABLE power_line ADD COLUMN all_neighbours BIGINT [4][2][10][2] -- Kann maximal 10 Nachbarn pro Spannungsebene aufnehmen
	DEFAULT '{{{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}}, 
		{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}}},
		{{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}},
		{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}}},
		{{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}},
		{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}}},
		{{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}},
		{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}}}}';
CREATE INDEX all_neighbour_idx ON power_line(all_neighbours);

-- Nachbarn werden Frequenzunabhängig zugeordnet...
UPDATE power_line SET all_neighbours = otg_get_all_neighbours (id);


	-- CABLE- UND FREQUENCY-ANNAHME-ALGORITHMEN

-- Neue Spalte cables_from_neighbour, in die true eingetragen wird, sobald eine Leitung Informationen vom Nachbarn erhalten hat
-- Should be renamed to info_from_neighbour
ALTER TABLE power_line ADD COLUMN cables_from_neighbour BOOLEAN;


-- Annahme-Algorithmen werden ausgeführt
-- Die Annahme-Algorithmen müssen vor der Subtraktion durch die circuits stattfinden...
-- ... da diese Veränderungen an den power_lines vornehmen
-- (Ein Problem, stellen hierbei z.B. cable=NULL einträge dar, bei denen keine cables abgezogen werden können...
-- ... und damit auch cables_sum nicht eindeutig bleiben kann)

SELECT otg_unknown_value_heuristic ();

-- ASSUMPTION
-- Assumes that lines with 110kV with cables (at 110kV) IS NULL and freuq IS NULL or 50...
-- receive cables=3
SELECT otg_110kv_cables ();


-- DATENUMWANDLUNG CIRCUIT_MEMBERS
-- (Es werden die in den OSM-Relations enthaltenen Stromkreis-Informationen untersucht)

	-- IMPORT DER RELEVANTEN CIRCUITS / CIRCUIT MEMBERS
	
SELECT*
	INTO power_circuits
	FROM power_relations_applied_changes; 
	
ALTER TABLE power_circuits
	ADD CONSTRAINT circuit_id_pk primary key (id); 
CREATE INDEX circuit_id_idx ON power_circuits(id);

CREATE TABLE power_circ_members (relation_id BIGINT, member_id BIGINT);

SELECT otg_seperate_power_relation_members ();	

ALTER TABLE power_circ_members
	ADD CONSTRAINT circuit_members_fk foreign key (relation_id) references power_circuits (id) ON DELETE CASCADE;
CREATE INDEX members_circuit_id_idx ON power_circ_members (relation_id);

-- Spaltenname meber_id ist irreführend dieser wird daher zu line_id umbenannt
ALTER TABLE power_circ_members RENAME COLUMN member_id TO line_id;


	-- UMWANDLUNG DATENTYPEN
		
-- Spalten voltage, cables, wires und circuits werden vom TEXT-Datentyp in INT-Datentyp umgewandelt	
ALTER TABLE power_circuits RENAME COLUMN voltage TO voltage_text;
ALTER TABLE power_circuits RENAME COLUMN cables TO cables_text;
ALTER TABLE power_circuits RENAME COLUMN wires TO wires_text;
ALTER TABLE power_circuits RENAME COLUMN circuits TO circuits_text;
ALTER TABLE power_circuits RENAME COLUMN frequency TO frequency_text;
ALTER TABLE power_circuits ADD COLUMN voltage INT;
ALTER TABLE power_circuits ADD COLUMN cables INT;
ALTER TABLE power_circuits ADD COLUMN wires INT;
ALTER TABLE power_circuits ADD COLUMN circuits INT;
ALTER TABLE power_circuits ADD COLUMN frequency REAL;

UPDATE power_circuits
	SET	voltage = 	otg_get_int_from_semic_string (voltage_text, 1),
		cables = 	otg_get_int_from_semic_string (cables_text, 1),
		wires = 	otg_get_int_from_wires_string (wires_text, 1),
		circuits = 	otg_get_int_from_semic_string (circuits_text, 1),
		frequency = 	otg_get_real_from_semic_string (frequency_text, 1);
		
ALTER TABLE power_circuits DROP COLUMN voltage_text;
ALTER TABLE power_circuits DROP COLUMN cables_text;
ALTER TABLE power_circuits DROP COLUMN wires_text;
ALTER TABLE power_circuits DROP COLUMN circuits_text;
ALTER TABLE power_circuits DROP COLUMN frequency_text;



 	-- MAXIMALE SPANNUNG


	-- INFORMATIONSÜBERGABE POWER_LINE -> power_circ_members
	-- (Ebenfalls um die Prozessierung zu erleichtern, werden den power_circ_members weitere Informationen übergeben)
	-- (Dies ermöglich unabhängige Erstellung der Topologie)
	
-- Es werden diejenigen circuit Members gelöscht, die nicht in der power_line Tabelle auftreten...
-- ... (über diese members gibt es keinen Informationen)
DELETE FROM power_circ_members mem
	WHERE mem.line_id NOT IN (SELECT id FROM power_line);	


		-- PROBLEM: NULL_voltage
		-- (Löscht alle power_circuits, die keine Spannungsinformation haben)

	CREATE TRIGGER problem_log_trigger
		AFTER DELETE ON power_circuits
		FOR EACH ROW 
		EXECUTE PROCEDURE otg_power_circuits_problem_tg ('NULL_voltage');

		DELETE FROM power_circuits -- Impliziert Cascadenlöschung der Members... 
			WHERE voltage IS NULL;
			
	DROP TRIGGER problem_log_trigger ON power_circuits;
	

	
-- Löscht alle power_circ_members, deren Spannung unter min_volt liegt.
-- (Bei den Subtraktionen (der Stromkreise von den Leitungen) werden die nicht untersuchten Spannugsebenen nicht benötigt)
DELETE FROM power_circuits
	WHERE voltage < (SELECT val_int 
				FROM abstr_values 
				WHERE val_description = 'min_voltage');

		-- ANNAHME (frequency): 
		-- Alle Stromkreise, die keinen Frequenzwert haben (und 220kv oder 380kv), bekommen frequency = 50
UPDATE power_circuits
	SET frequency = 50
	WHERE 	frequency IS NULL 
		AND (voltage = 220000 OR voltage = 380000);

		-- ASSUMPTION (frequency):
		-- Only 110kV circuits with 3, 6, 9 or 12 cables (not 2 nor 4) get frequency 50
		-- Also without cable information, frequency is set to 50!!
UPDATE power_circuits
	SET frequency = 50
	WHERE frequency IS NULL
		AND voltage = 110000
		AND (	cables IS NULL OR 
			cables = 3 OR 
			cables = 6 OR 
			cables = 9 OR 
			cables = 12); -- Needs to be checked!

UPDATE power_circuits
	SET frequency = 16.7
	WHERE frequency IS NULL
		AND voltage = 110000
		AND (	cables = 2 OR 
			cables = 4); -- Needs to be checked!

	-- PROBLEM: NULL_frequency
	-- (Löscht alle power_circuits, die keine Frequenz haben)
	CREATE TRIGGER problem_log_trigger
		AFTER DELETE ON power_circuits
		FOR EACH ROW 
		EXECUTE PROCEDURE otg_power_circuits_problem_tg ('NULL_frequency');

		DELETE FROM power_circuits -- Impliziert Cascadenlöschung der Members... 
			WHERE frequency IS NULL;
			
	DROP TRIGGER problem_log_trigger ON power_circuits;

-- 16.7 should not be deleted (at this point), because frequency info can be written in to power_lines, when substracting!!!
-- 	-- PROBLEM: 16.7 frequency (not really a problem, just docu)
-- 	-- (Löscht alle power_circuits, die Frequenz = 16.7 haben)
-- 	CREATE TRIGGER problem_log_trigger
-- 		AFTER DELETE ON power_circuits
-- 		FOR EACH ROW 
-- 		EXECUTE PROCEDURE otg_power_circuits_problem_tg ('frequency=16.7');
-- 
-- 		DELETE FROM power_circuits -- Impliziert Cascadenlöschung der Members... 
-- 			WHERE frequency = 16.7;
-- 			
-- 	DROP TRIGGER problem_log_trigger ON power_circuits;

	
-- Annahme: Stromkreise, die keinen Cable-Eintrag haben (cables = NULL)
-- bekommen bestimmte cables
-- (Es sind nun nurnoch circuit_members mit für das Modell gebrauchter Spannung enthalten)
UPDATE power_circuits
	SET cables = 3
	WHERE cables IS NULL AND
	frequency = 50; 
-- ... Alle HGÜ-Leitungen ohne Cable-Eintrag bekommen cables = 2
UPDATE power_circuits
	SET cables = 2
	WHERE cables IS NULL AND
	frequency = 0; 
-- ... Alle Bahnstromleitungen (freq. = 16.7) ohne Cable-Eintrag bekommen cables = 2
UPDATE power_circuits
	SET cables = 2
	WHERE cables IS NULL AND
	frequency = 16.7; 

-- At this point, all circuit should have (valid) cable-information!	

	-- PROBLEM: NULL_cables
	-- (Löscht alle power_circuits, die keine Cable-Anzahl haben)
	CREATE TRIGGER problem_log_trigger
		AFTER DELETE ON power_circuits
		FOR EACH ROW 
		EXECUTE PROCEDURE otg_power_circuits_problem_tg ('NULL_cables');

		DELETE FROM power_circuits -- Impliziert Cascadenlöschung der Members... 
			WHERE cables IS NULL;
			
	DROP TRIGGER problem_log_trigger ON power_circuits;


	-- ENT-NORMALISIERUNG POWER_CIRCUITS
	-- (Um die Prozessierung der Daten zu vereinfachen wird die Tabelle entnormalisiert...
	-- ... d.h. den power_circ_members werden Informationen der übergeordneten Tabelle power_circuits übergeben)
			
-- length, way und power wird für alle circuit_members aus der Tabelle power_line übernommen
ALTER TABLE power_circ_members ADD COLUMN length real;
ALTER TABLE power_circ_members ADD COLUMN way geometry(LINESTRING);
ALTER TABLE power_circ_members ADD COLUMN power text;
UPDATE power_circ_members 
	SET 	length = power_line.length,
		way = power_line.way, 
		power = power_line.power
	FROM power_line
	WHERE power_line.id = power_circ_members.line_id;
		
ALTER TABLE power_circ_members ADD COLUMN voltage INT;
ALTER TABLE power_circ_members ADD COLUMN cables INT;
ALTER TABLE power_circ_members ADD COLUMN wires INT;
ALTER TABLE power_circ_members ADD COLUMN circuits INT;
ALTER TABLE power_circ_members ADD COLUMN frequency REAL;
CREATE INDEX members_voltage_idx ON power_circ_members (voltage);

UPDATE power_circ_members 
	SET	voltage = 	rels.voltage,
		cables = 	rels.cables,
		wires = 	rels.wires,
		circuits = 	rels.circuits,
		frequency = 	rels.frequency
	FROM power_circuits rels
	WHERE rels.id = relation_id;


-- Circuits-Tag braucht bei Stromkreisen nicht untersucht werden, 
-- ...da diese nach Konvention genau einen Stromkreis repräsentieren.


-- Es werden diejenigen circuits gelöscht, die keine Members mehr haben
DELETE FROM power_circuits 
	WHERE id NOT IN (SELECT relation_id FROM power_circ_members);


-- CIRCUIT TOPOLOGIE
-- (Unabhängige Untersuchung der Topologie der Stromkreise (power_relation_members))


-- Die neuen Spalten f_bus und t_bus werden für die Berechnung der Topologie benötigt
ALTER TABLE power_circ_members ADD COLUMN f_bus BIGINT;
ALTER TABLE power_circ_members ADD COLUMN t_bus BIGINT;

-- Hier werden die Topologien der noch vorhandenen Spannungen berechnet.
-- Dabei werden alle circuits zunächst einzeln durchgegangen und deren Topologie wird unabhängig berechnet
-- Vertices werden in die Tabelle bus_data geschrieben...
-- Die Sortierung anch Spannung und Frequenz ist an dieser Stelle irelevant, da ohnehin Realtions-weise gerechnet wird.
-- Aufteilen der Tabelle 'power_circ_members' um DB-Servern mit wenig RAM oder wenigen max_locks_per transaction die Berechnung zu ermöglichen.

-- The Split does good things, but is not beautiful!
-- Nessesary for memory reasons
SELECT otg_split_table('power_circ_members', 'relation_id');

SELECT otg_create_grid_topology ('split_table_1');
SELECT otg_create_grid_topology ('split_table_2');
SELECT otg_create_grid_topology ('split_table_3');
SELECT otg_create_grid_topology ('split_table_4');
SELECT otg_create_grid_topology ('split_table_5');
SELECT otg_create_grid_topology ('split_table_6');
SELECT otg_create_grid_topology ('split_table_7');
SELECT otg_create_grid_topology ('split_table_8');
SELECT otg_create_grid_topology ('split_table_9');
SELECT otg_create_grid_topology ('split_table_10');

-- Nach der Berechnung wird die Tabelle wieder zusammengefügt
ALTER TABLE split_table_1 RENAME TO power_circ_members;
INSERT INTO power_circ_members SELECT * FROM split_table_2;
INSERT INTO power_circ_members SELECT * FROM split_table_3;
INSERT INTO power_circ_members SELECT * FROM split_table_4;
INSERT INTO power_circ_members SELECT * FROM split_table_5;
INSERT INTO power_circ_members SELECT * FROM split_table_6;
INSERT INTO power_circ_members SELECT * FROM split_table_7;
INSERT INTO power_circ_members SELECT * FROM split_table_8;
INSERT INTO power_circ_members SELECT * FROM split_table_9;
INSERT INTO power_circ_members SELECT * FROM split_table_10;

-- Und die nicht benötigten Tabellen werden wieder gelöscht
DROP TABLE IF EXISTS split_table_1;
DROP TABLE IF EXISTS split_table_2;
DROP TABLE IF EXISTS split_table_3;
DROP TABLE IF EXISTS split_table_4;
DROP TABLE IF EXISTS split_table_5;
DROP TABLE IF EXISTS split_table_6;
DROP TABLE IF EXISTS split_table_7;
DROP TABLE IF EXISTS split_table_8;
DROP TABLE IF EXISTS split_table_9;
DROP TABLE IF EXISTS split_table_10;

-- Neue Spalte origin in Tabelle bus_data soll kennzeichnen, das die bis jetzt in bus_data eingetragenen Knoten aus den Stromkreisinformationen stammen (origin = 'rel')
-- Die Knoten aus den (überbleibenden) power_lines wird auch in diese Knotentabelle gespeichert (origin = 'lin')
ALTER TABLE bus_data ADD COLUMN origin character varying (3);
UPDATE bus_data SET origin = 'rel';


	-- KNOTENUNTERSUCHUNG UND LÖSCHUNG OFFENER ENDEN
	
-- Berechnet die Anzahl der Links pro Knoten in der bus_data Tabelle
SELECT otg_set_count ('power_circ_members', 'rel');
-- Diese Löschung nochmal überdenken!!
	-- PROBLEM cnt_>_2
	-- (An dieser Stelle werden diejenigen circuits gelöscht, die mindestens an einem Knoten cnt>2 haben.
	-- Denn oft sind die circuits dann falsch gemappt (insbesondere in der Nähe der Substations)
	CREATE TRIGGER problem_log_trigger
		AFTER DELETE ON power_circuits
		FOR EACH ROW 
		EXECUTE PROCEDURE otg_power_circuits_problem_tg ('branch_off_(cables_>_3)');
		-- Die in das Log eingetragenen Werte für z.B. cables sind die aus der Datenbanke erhaltenen Werte (und nicht die über Annahmen veränderten)
		-- auch bei cables = 3 führt branch off oft zu fehlern!!!!
	DELETE FROM power_circuits 
		WHERE 	--cables > 3 AND 
			id IN (SELECT relation_id FROM power_circ_members 
			WHERE 	f_bus IN (SELECT id FROM bus_data WHERE cnt > 2 AND origin = 'rel') OR
				t_bus IN (SELECT id FROM bus_data WHERE cnt > 2 AND origin = 'rel')
			GROUP BY relation_id);

	DROP TRIGGER problem_log_trigger ON power_circuits;

-- Neue Spalte, die die Länderkennung des Knotens enthält
-- (wird druch otg_bus_analysis () gefüllt)
ALTER TABLE bus_data ADD COLUMN cntr_id character varying (2);

-- Macht allgemeine Knotenuntersuchung
--(setzt Länderkennung, substation_id und Offene Enden im Ausland bekommen Substation_id = 0)
SELECT otg_bus_analysis ('rel');


-- Heuristik: Funktion otg_connect_dead_ends_with_substation () versucht offene Stromkreisendenin der Nähe von Umspannwerken über Puffer zu schließen
SELECT otg_connect_dead_ends_with_substation ();

-- Löscht alle circuit_members, die (nun aufgrund des Puffers) Anfang und Ende innerhalb derselben Substation haben
-- (Dies kann bei Leitungen die fälschlicherweise so gemappt sind, dass mit einem Ende innerhalb eines Umspannwerks liegen, das andere jedoch offen, aber in der Nähe derselbe Umspannstation liegt (Mapping-Fehler))
DELETE FROM power_circ_members 
	WHERE 	(SELECT substation_id FROM bus_data WHERE id = power_circ_members.f_bus) =  
		(SELECT substation_id FROM bus_data WHERE id = power_circ_members.t_bus);
		
-- Es können aufgrund von Mappingfehlern power_circ_members auftreten, die Anfang und Ende im selben Punkt besitzen
-- ... diese werden gelöscht
DELETE FROM power_circ_members WHERE f_bus = t_bus;


	-- PROBLEM dead_end
	-- Es werden alle Stromkreise gelöscht, die irgendwo ein offenes Ende haben 
	-- Dies ist notwendig, da bei einer teilweisen Löschung falsche Stromkreise entstehen könnten
	CREATE TRIGGER problem_log_trigger
		AFTER DELETE ON power_circuits
		FOR EACH ROW 
		EXECUTE PROCEDURE otg_power_circuits_problem_tg ('dead_end');

	SELECT otg_set_count ('power_circ_members', 'rel');
	-- Sobald bei einer Relation ein offenes Ende festegestellt wird, wird diese gelöscht
	DELETE FROM power_circuits -- On delete cascade
		WHERE id IN (SELECT relation_id FROM power_circ_members 
				WHERE 	(f_bus IN (SELECT id FROM bus_data 
							WHERE 	origin = 'rel' AND 
								cnt = 1 AND 
								substation_id IS NULL) OR
					t_bus IN (SELECT id FROM bus_data 
							WHERE 	origin = 'rel' AND 
								cnt = 1 AND 
								substation_id IS NULL)));
	DROP TRIGGER problem_log_trigger ON power_circuits;


-- Anschließend werden alle Knoten gelöscht, an die aufgrund der Sromkreis-Löschung keine Leitungen mehr angeschlossen sind	
SELECT otg_set_count ('power_circ_members', 'rel');
DELETE FROM bus_data WHERE origin = 'rel' AND cnt = 0; 


-- SUBTRAKTION DER STROMKREISE (power_circ_members) VON DEN LEITUNGEN (POWER_LINES)
-- Die in den power_circ_members enthaltenen Informationen werden genutzt und quasi über die Leitungen "gelegt"
-- ... bzw. von diesen subtrahiert
-- Frequenz kann hier zunächst unberücksichtigt bleiben. Die abgezogenen Leitungen haben ja ihre Frequenz in den power_circuits

-- Ist die Spannung des Stromkreises auf der Leitung nicht vorhanden (Mappingfehler) wird in problem_log geschrieben
-- Grundlegend wird den Stromkreisspannung mehr "vertraut" als den Leitungsspannungen
-- Frequenzen können von circuits unter bestimmten Bedingungn in power_lines geschrieben werden.
SELECT otg_substract_circuits() ;


-- Durch den Puffer (otg_connect_dead_ends_with_substation) "Übergangene" Leitungen (Tabelle power_line) werden angepasst.
-- Dies kann erst an dieser Stelle geschehen, damit nicht unkontrolliert cables von den power_line abgezogen werden
-- (sondern nur die bis hier überbleibenden betrachtet werden)
-- Zudem können für das "Abziehen" verantwortliche Stromkreise evtl. gelöscht werden (z.B. wegen dead end).
SELECT otg_substract_cables_within_buffer (id) FROM bus_data WHERE buffered = true AND origin = 'rel'; -- Also alle erfolgreichen Buffer


	-- PROBLEM: CABLE CONFLICE
	-- wieder nach oben packen!!!
	-- Cable conflict sollte noch verbessert werden (und in Summenfehler und Nachabarschaftsfehler aufgeteilt werden)
	-- (Ein Problem wird gemeldet, sobald Leitungs-Nachabarschafts-Informationen nicht konsistent sind)
	-- Dies kann Gründe wie falsches Mapping der ways (Anzahl cables) oder falschen Mapping der Relations haben 
	INSERT INTO problem_log (	object_type,
					line_id,
					relation_id,
					way, 
					voltage,
					cables,
					wires, 
					frequency,
					problem)
					
		SELECT 'power_line', ARRAY [id], NULL, ST_Multi(way), NULL, NULL, NULL, NULL, 'cable_conflict'
		FROM power_line
		WHERE otg_check_cable_conflict (id) AND voltage_array [1]>= (SELECT val_int 
										FROM abstr_values 
										WHERE val_description = 'min_voltage');




-- DATENUMWANDLUNG UND TOPOLOGIE POWER_LINE
-- (Unabhängige Untersuchung der einzelnen Spannungsebenen)

	-- ERSTELLEN DER ZWISCHENTABELLE power_line_sep
	
CREATE TABLE power_line_sep AS SELECT * FROM branch_data LIMIT 0; 
-- Aufgetrennte power_lines werden in power_line_sep geschrieben
-- Lines bekommen Relation_id = 0

-- These columns are still needed for separation of continuous lines	
ALTER TABLE power_line_sep ADD COLUMN startpoint geometry (Point);
ALTER TABLE power_line_sep ADD COLUMN endpoint geometry (Point); 
	
SELECT otg_seperate_voltage_levels ();
--DROP TABLE power_line;

	-- LÖSCHUNGEN
	
-- Es werden branches gelöscht, deren Spannung nicht Untersucht werden soll
DELETE FROM power_line_sep 
	WHERE 	voltage < (SELECT val_int 
				FROM abstr_values 
				WHERE val_description = 'min_voltage'); --NOT IN (SELECT voltage FROM voltage_levels); 
	
		-- PROBLEM: Missing Cables
		-- (Es werden diejenigen power_line_sep gelöscht, die cables IS NULL aufweisen)
	CREATE TRIGGER problem_log_trigger
		AFTER DELETE ON power_line_sep
		FOR EACH ROW 
		EXECUTE PROCEDURE otg_power_line_as_branch_problem_tg ('missing_cables');

	DELETE FROM power_line_sep  --Problemlos solange (zufälligerweise) die darüberliegenden circuits alle Cables abdecken (Es kann aber eben auch sein, dass circuits fehlen und daher noch cables übrig wären)
		WHERE 	cables IS NULL; -- Später noch Circuit beachten und besser machen!!!

	DROP TRIGGER problem_log_trigger ON power_line_sep;


-- Löscht diejenigen power_line_sep, die cables = 0 aufweisen. 
-- Dies Stellt kein Problem dar, da es sich um "Überlagerung" durch Stromkreise handeln kann.
DELETE FROM power_line_sep 
	WHERE 	cables = 0; 

		-- PROBLEM: too_many_circuits_on_power_line
		-- (Es werden diejenigen power_line_sep gelöscht, die cables < 0 aufweisen) 
		-- (Diese wurden von zu vielen Stromkreisen überlagert).
	CREATE TRIGGER problem_log_trigger
		AFTER DELETE ON power_line_sep
		FOR EACH ROW 
		EXECUTE PROCEDURE otg_power_line_as_branch_problem_tg ('too_many_circuits_on_power_line');

	DELETE FROM power_line_sep 
		WHERE 	cables < 0;

	DROP TRIGGER problem_log_trigger ON power_line_sep;

	
-- Annahme: Alle noch unbekannten Frequenzen der Spannugnen 220 und 380kv werden 50Hz gesetzt
-- Da mehrer Frequenzen pro Freileitung vom Tag her nicht berücksichtigt werden können, kann an dieser Stelle ein Fehler
-- entstehen. 
-- 16.7 hz liegen i.d.R. auf 110kV.
-- Problematisch sind zukünfig geplante HGÜ Leitungen gemeinsam mit 50Hz auf einer Freileitung 
UPDATE power_line_sep 
	SET frequency = 50
	WHERE 	frequency IS NULL 
		AND (voltage = 220000 OR voltage = 380000);

-- ASSUMPTION: For 110kV, frequency = 50 can be assumed under the following conditions
UPDATE power_line_sep 
	SET frequency = 50
	WHERE 	frequency IS NULL AND 
		voltage = 110000 AND
		(	cables IS NULL OR 
			cables = 3 OR 
			cables = 6 OR 
			cables = 9 OR 
			cables = 12); 

-- ASSUMPTION: For 110kV, frequency = 16.7 can be assumed under the following conditions
UPDATE power_line_sep 
	SET frequency = 16.7
	WHERE 	frequency IS NULL AND 
		voltage = 110000 AND
		(	cables = 2 OR 
			cables = 4); 
		
-- Alle noch übekannten Frequenzen werden 50Hz gesetzt.
UPDATE power_line_sep
	SET frequency = 50 
	WHERE frequency IS NULL; -- this needs to be checked
		-- there may be still many train-lines (in theory 16.7Hz) among the power-lines

-- I will give it a try and leave 16.7 inside till the end...
-- 		-- PROBLEM: frequency=16.7 (not really a problem, just docu)
-- 		-- (Es werden diejenigen power_line_sep gelöscht, die frequency = 16.7 aufweisen) 
-- 	CREATE TRIGGER problem_log_trigger
-- 		AFTER DELETE ON power_line_sep
-- 		FOR EACH ROW 
-- 		EXECUTE PROCEDURE otg_power_line_as_branch_problem_tg ('frequency=16.7');
-- 
-- 	DELETE FROM power_line_sep 
-- 		WHERE 	frequency = 16.7;
-- 
-- 	DROP TRIGGER problem_log_trigger ON power_line_sep;


	-- TOPOLOGIE
	-- (Hier werden die Topologien der Spannungsebenen berechnet)


-- Knoteninformationen werde wieder in Tabelle bus_data geschrieben
-- An dieser Stelle sollte evtl. noch nach Frequenzen getrennt werden (damit sich übernander liegende HGÜ und Drehstromleitung nicht verbinden können)
-- (dies ist kein Problem, solange Circuits gut gemappt sind)
SELECT otg_create_grid_topology ('power_line_sep');
-- Die neu hinzugekommenen Knoten (von power_lines) werden mit origin = 'lin' gekennzeichnet
UPDATE bus_data SET origin = 'lin' WHERE origin IS NULL;

-- Anzahl der Leitungen pro Knoten wird gezählt
SELECT otg_set_count ('power_line_sep', 'lin');

-- S.o. (bei power_circuits) - Analyse der neuen Knoten
SELECT otg_bus_analysis ('lin');

-- This function connects dead ends that are close to a transmission line...
-- to one of the transmission line vertices. 
-- Until now this is quick and dirty and needs to be improved.
SELECT otg_connect_dead_ends_to_cont_lines ();

	-- PROBLEM: dead_end
	-- (bei den noch überbleibendne power_lines werden diejenigen iterativ gelöscht, die ein offenes Ende haben)
	-- (Diese Leitungen stellen keine realistischen Netzabschnitte dar)
	CREATE TRIGGER problem_log_trigger
		AFTER DELETE ON power_line_sep
		FOR EACH ROW 
		EXECUTE PROCEDURE otg_power_line_as_branch_problem_tg ('dead_end');
		
-- Löscht iterativ Leitungen mit offenem End
SELECT otg_cut_off_dead_ends_iteration ('power_line_sep', 'lin'); 

	DROP TRIGGER problem_log_trigger ON power_line_sep;

-- Alle nun nicht mehr verbundenen Knoten werden gelöscht.
SELECT otg_set_count ('power_line_sep', 'lin');
DELETE FROM bus_data WHERE origin = 'lin' AND cnt = 0;

	
-- ZUSAMMENFASSUNG DER DATEN IN TOPOLIGIE-TABELLE BRANCH-DATA
-- (Die Tabelle Branch-Data soll alle Leitungs-Topologien (power_line und power_cirucit_members) vereinigen)

INSERT INTO  branch_data (	relation_id, 
				line_id,
				f_bus,
				t_bus,
				length,
				way,
				voltage,
				cables,
				wires,
				frequency, 
				power)
	SELECT relation_id, line_id, f_bus, t_bus, length, way, voltage, cables, wires, frequency, power 
		FROM power_circ_members;
		
INSERT INTO  branch_data (	relation_id, 
				line_id,
				f_bus,
				t_bus,
				length,
				way,
				voltage,
				cables,
				wires,
				frequency,
				power)
	SELECT relation_id, line_id, f_bus, t_bus, length, way, voltage, cables, wires, frequency, power 
		FROM power_line_sep ;


-- Die folgenden Tabellen werden nicht mehr benötigt
-- (Alle für das Netzmodell benötigten Informationen wurden in branch_data und bus_data vereinigt)
--DROP TABLE power_circ_members;
--DROP TABLE power_circuits;
--DROP TABLE power_line_sep;
-- Die Spalten buffered und origin sind nur für Prozessierung von Bedeutung und können gelöcscht werden
ALTER TABLE bus_data DROP COLUMN buffered;
ALTER TABLE bus_data DROP COLUMN origin;


-- ANNAHMEN / UMSPANNWERKE / VEREINFACHUNGEN BRANCH DATA
-- (Die Branch-Informationen sind noch nicht vollständig, bzw. Leitungsabschnitte können vereinfacht werden...)

	-- ANNAHMEN

-- Füllt alle noch nicht bekannten Wires der 380kv, 220kv und 110kV Spannungsebene mit 4, 2 bzw. 1 wires.
-- (Bei frequenz von 50) 
-- Alle weiteren noch unbekannten wires von power = 'line' bekommen wires = 1
SELECT otg_wires_assumption ();

	-- BETRACHTETE FREQUENZEN / ANZAHL CABLE

-- Es werden alle nicht betrachteten Frequenzen (nicht 50 oder 0 HZ) gelöscht.
-- Here, 16.7Hz (train) transmission lines (branches) are deleted
DELETE FROM branch_data WHERE 	frequency != 50 AND 
				frequency != 0;

-- Cables<=1 wird von otg_calc_branch_specifications nicht als System betrachtet und 
-- Bekommt dahe Anzahl Systeme = 0. 
-- Dies führt zur Division durch 0
DELETE FROM branch_data WHERE cables <= 1;

-- ... und die dazugehörigen Busses müssen ebenfalls gelöscht werden
DELETE FROM bus_data WHERE 	NOT id IN (SELECT f_bus FROM branch_data) AND
				NOT id IN (SELECT t_bus FROM branch_data);




	-- VERSCHALTUNG UMSPANNWERKE
	-- (In diesem Abschnitt wird die Verschaltung in den Umspannwerken modelliert, sowie Transformatoren eingesetzt)
	
-- Ändert die Topologie, sodass Alle Punkte innerhalb einer Substation (je Spannungsebene) zu einem vereinigt werden
SELECT otg_connect_substation_vertices(); -- für außerhalb Deutschland ignoriert

--Fügt den Branches am anfang und Ende noch ein Wegstückchen zum Substation-node hinzu um die Visualisierung zu verbessern.
UPDATE branch_data
	SET way = ST_AddPoint (way, (SELECT the_geom FROM bus_data WHERE branch_data.f_bus = id), 0);
UPDATE branch_data
	SET way = ST_AddPoint (way, (SELECT the_geom FROM bus_data WHERE branch_data.t_bus = id));

	
	
-- Erstellt innerhalb der Umspannwerke Tranformator-Leitungen, die die Substation-Knoten verbinden
SELECT otg_connect_transformers ();

	-- LEITUNGS ZUSAMMENFASSUNG
	-- (Einige Leitungsabscnitte können mit dem Ziel die Berechnung zu Beschleunigen zusammengefasst werden)

		-- UMWANDLUNG DATENTYPEN
		-- (Für die Zusammenfassung müssen einige Datentypen angepasst werden...
		-- Z.B. sollen alle enthaltenen Lines in ein Array geschrieben werden)
		
-- Spalten line_id und ways werden zu Arrays gemacht, damit lines zusammengefasst werden können
ALTER TABLE branch_data ADD COLUMN line_ids BIGINT [];
UPDATE branch_data
	SET line_ids [1] = line_id;
ALTER TABLE branch_data DROP column line_id;

ALTER TABLE branch_data ADD COLUMN ways geometry (LineString) [];
UPDATE branch_data
	SET ways [1] = way;
ALTER TABLE branch_data DROP column way;


		-- ZUSAMMEFASSUNG VON BRANCHES
		
SELECT otg_simplify_branches_iteration ();


		-- UMWANDLUNG DATENTYPEN
		
ALTER TABLE branch_data ADD COLUMN multiline geometry (MULTILINESTRING, 4326); --evtl. wieder auf MultiLineStirng festlegen
UPDATE branch_data
	SET multiline = ST_Multi(ST_union(ways));
ALTER TABLE branch_data DROP column ways; 


-- GRAPHEN UNTERSUCHUNG (CLUSTER)

-- Neue Spalte discovered, in der true steht, wenn der Knoten zum Slack-Knoten Graph gehört (Zusammenhang)
ALTER TABLE bus_data ADD COLUMN discovered BOOLEAN DEFAULT false;

SELECT otg_graph_analysis (); -- If in Python Input graph_dfs is selected True, then disconnected graphs will be deleted

-- Erweitert branch_data um einfache Topologische Geometrie
ALTER TABLE branch_data ADD COLUMN simple_geom GEOMETRY (LINESTRING, 4326);
UPDATE branch_data
	SET simple_geom = (SELECT ST_MakeLine(	(SELECT the_geom FROM bus_data WHERE id=f_bus), 
						(SELECT the_geom FROM bus_data WHERE id=t_bus)));


-- AUSKOPPLUNG VON DC-LINES AUS BRANCH_DATA TABELLE
-- branch_id bleibt eindeutig erhalten (Gibts nur einmal, entweder in branch_data oder dc_line_data)

CREATE TABLE dcline_data AS SELECT * FROM branch_data LIMIT 0;
-- Alle Leitungen mit frequency = 0 werden in neue Tabelle sc_line_data übertragen.
INSERT INTO dcline_data SELECT * FROM branch_data WHERE frequency = 0;
DELETE FROM branch_data WHERE frequency = 0;


-- BERECHNUNG DER LEITUNGS-/TRAFOKENNWERTE 
-- (Über die Leitungsdatentabelle und Transformatortabelle werden genaue Leitungskennwerte berechnet)

		-- ZUORDNUNG DER KENNWERTE ZU BRANCHES UND DC-LEITUNGEN
		
-- Neue Spalte spec_id, die die ID der Leitung in der Leitungsdatentabelle enthält
ALTER TABLE branch_data ADD COLUMN spec_id INT;
-- Ist die gesuchte Spannung in der Tabelle nicht zu finden, wird diejenige Spannung verwendet, die am geringsten abweicht)
UPDATE branch_data 
	SET spec_id = (SELECT spec_id FROM branch_specifications
				WHERE 	branch_specifications.power = branch_data.power
				ORDER BY @((branch_data.voltage/1000) - branch_specifications.voltage_kv) -- Nach kleinstem Abstand zur Angegenen Spannung
					 LIMIT 1)
		WHERE power = 'line' OR power = 'cable';

-- Neue Spalte spec_id, die die ID der Leitung in der Leitungsdatentabelle enthält
ALTER TABLE dcline_data ADD COLUMN spec_id INT;
-- Die passende Zeile der Kennwerttabelle wird zugeordnet (Bei HgÜ wird z.Z. nur nach Freileitung oder Kabel unterschieden)
UPDATE dcline_data 
	SET spec_id = (SELECT spec_id FROM dcline_specifications specs
				WHERE dcline_data.power = specs.power);

		-- KENNWERTBERECHNUGN
		
			-- AC
-- Neue Spalten für Leitungsdaten
ALTER TABLE branch_data ADD COLUMN br_r real; --resistance (p.u.)
ALTER TABLE branch_data ADD COLUMN br_x real; --reactance (p.u.)
ALTER TABLE branch_data ADD COLUMN br_b real; --total line charging susceptance (p.u.)
ALTER TABLE branch_data ADD COLUMN S_long real; -- long_term rating Power (MVA)
ALTER TABLE branch_data ADD COLUMN tap real; -- Transformer Tap
ALTER TABLE branch_data ADD COLUMN shift real; -- Phasenverschiebung (Trafoverschaltung)

-- Berechnet die Leitungsdaten br_r (p.u.), br_x (p.u.), br_b (p.u.), und s_long (VA) und setzt shift und tap
SELECT otg_calc_branch_specifications ();

-- Alle Leitungen bekommen Tap = 0 und Shift = 0
UPDATE branch_data 
	SET 	tap = 0,
		shift = 0
		WHERE power != 'transformer';

			-- DC
-- Neue Spalten für Leitungsdaten
ALTER TABLE dcline_data ADD COLUMN pmax REAL; --maximale Leistung am from-Knoten
ALTER TABLE dcline_data ADD COLUMN loss1 REAL; -- Linearer Verlustfaktor

SELECT otg_calc_dcline_specifications ();

			-- MAXIMALE KNOTENLEISTUNG
			
-- Neue Spalte S_long_MVA_sum, die für Knoten im Umspannwerk die Maximal aufnehmbare/abgebbare
-- Scheinleistung enthält. Vereinfachend werden die Beträge der Scheinleistung addiert. 
-- ... um die Bemessung der Trafos zu ermöglichen.
ALTER TABLE bus_data ADD COLUMN S_long_sum REAL; 

SELECT otg_calc_max_node_power ();
	
			-- TRAFOS
			
-- Berechnet die Spezifikationen für Trafos
-- Spalte für Anzahl an Standard-Trafos
ALTER TABLE branch_data ADD COLUMN numb_transformers INT;

SELECT otg_calc_transformer_specifications ();


-- BUS-TYPE / SLACK_KNOTEN-UNTERSUCHUNG

-- Neue Spalte bus_type (Matpower bus_type)
-- Zunächst werden alle Knoten asl PQ-Knoten angenommen bus_type = 1 (Last oder Einspeisung mit fester Wirk- und Blindleistung)
ALTER TABLE bus_data ADD COLUMN bus_type INT default 1;

-- Sucht die als "main_station" deklarierte Substation (OSM-ID) heraus...
--... und macht aus dem Knoten der höchsten Spannungsebene innerhalb dieser Substation den Slack-bus
UPDATE bus_data 
	SET bus_type = 3 
	WHERE id = (SELECT id
			FROM bus_data 
			WHERE substation_id = (SELECT val_int 
						FROM abstr_values 
						WHERE val_description = 'main_station')
			ORDER BY voltage DESC
			LIMIT 1);
	

		-- LÖSCHUNG NICHT RELEVANTER UMSPANNWERKE
		
-- Alle Substations, die keine relevanten Punkte enthalten werden gelöscht.
DELETE FROM power_substation WHERE id NOT IN (SELECT substation_id FROM bus_data WHERE NOT substation_id IS NULL);

		-- PLZ UND NUTS3 ZUORDNUNG UMSPANNWERKE
		
-- Neue Spalte für Leistung (maximalleistung der Knoten)		
ALTER TABLE power_substation ADD COLUMN s_long NUMERIC;
UPDATE power_substation SET s_long = (SELECT sum(s_long_sum) --sum instead of max!
					FROM bus_data 
					WHERE substation_id = power_substation.id);
-- additional column for center					
SELECT AddGeometryColumn('power_substation', 'center_geom', 4326, 'Point', 2);
UPDATE power_substation SET center_geom = ST_Centroid(poly);

-- Executes functions to create assignment-tables for plz and nut3 to substations
SELECT otg_plz_substation ();
SELECT otg_nuts3_substation ();


-- ZUSÄTZLICHE DATEN ZUR ÜBERGABE AN MATPOWER

-- Die Werte bus_area und zone können für die Summierung der Einspeisung verwendet werden. Dies wird hier vernachlässigt
-- (Alle Knoten bekommen dieselbe Zone)
ALTER TABLE bus_data ADD COLUMN bus_area INT;
ALTER TABLE bus_data ADD COLUMN zone INT;
UPDATE bus_data SET bus_area = 1; 
UPDATE bus_data SET zone = 1; 

-- Die Werte vm (voltage_magnitute) und va (voltage_angle) stellen Startwerte der Iteration dar
ALTER TABLE bus_data ADD COLUMN vm REAL;
ALTER TABLE bus_data ADD COLUMN va REAL;
UPDATE bus_data SET vm = 1;
UPDATE bus_data SET va = 0;

-- New columns for loads
ALTER TABLE bus_data ADD COLUMN pd REAL;
ALTER TABLE bus_data ADD COLUMN qd REAL;

 -- Zu Beachten:
 -- Slack Bus benötigt Generator
 -- pd und qd der Buses von außerhalb vorgeben.
 -- Gleichstromleitung darf nur netzintegriert verwendet werden, damit GLS lösbar bleibt.


