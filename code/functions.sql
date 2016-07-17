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

----------------------------------------------------------------------------------------
-- FUNKTIONEN
----------------------------------------------------------------------------------------


-- UMWANDLUNG DATENTYPEN (ALLGEMEIN)

	-- ISREAL UND ISINT

-- Die beiden Funktionen bekommen String als Input und untersuchen, ob der Wert ein Real (isreal) oder Integer ist (isint)
-- ... und returnen Boolean
CREATE OR REPLACE FUNCTION otg_isreal (TEXT) RETURNS BOOLEAN 
AS $$
DECLARE
	x REAL;
BEGIN
	x = $1::REAL;
	RETURN TRUE;
EXCEPTION WHEN others THEN -- Exception ist eine Erweiterung des Begin-Blocks und wird ausgeführt, wenn ein Error vorkommt
	RETURN FALSE; -- others steht für alle Arten von Fehlern (sammelt alles auf)
END;
$$
LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION otg_isint (TEXT) RETURNS BOOLEAN 
AS $$
DECLARE
	x INT;
BEGIN
	x = $1::INT;
	RETURN TRUE;
EXCEPTION WHEN others THEN -- Exception ist eine Erweiterung des Begin-Blocks und wird ausgeführt, wenn ein Error vorkommt
	RETURN FALSE; -- others steht für alle Arten von Fehlern (sammelt alles auf)
END;
$$
LANGUAGE plpgsql IMMUTABLE;


-- Function that gets max ID of specified table and specified column
CREATE OR REPLACE FUNCTION otg_get_max_id(v_table TEXT, v_column TEXT) RETURNS BIGINT
AS $$
DECLARE
v_max_id BIGINT;

BEGIN
EXECUTE 'SELECT max('|| v_column ||') FROM ' || v_table INTO v_max_id;
IF v_max_id IS NULL THEN v_max_id := 0; END IF;
RETURN v_max_id;	
END; 
$$
LANGUAGE plpgsql;



-- CREATE OR REPLACE FUNCTION otg_update_osm (v_date date) RETURNS void
-- AS $$
-- DECLARE
-- v_object RECORD;
-- 
-- BEGIN
-- FOR v_object IN
-- 	SELECT * FROM nodes
-- LOOP
-- 	IF NOT v_object.id IN (SELECT id FROM osm_data.nodes)
-- 	THEN	INSERT INTO osm_data.nodes (id, version, user_id, tstamp, changeset_id, tags, db_id)
-- 			VALUES (v_object.id,
-- 				v_object.version, 
-- 				v_object.user_id, 
-- 				v_object.tstamp, 
-- 				v_object.changeset_id, 
-- 				v_object.tags,
-- 				otg_get_max_id('osm_data.nodes', 'db_id') + 1);
-- 		END IF;
-- END LOOP;
-- 
-- 	
-- END; 
-- $$
-- LANGUAGE plpgsql;



	-- NUMBER_OF_PART_CHAR

-- Anzahl eines bestimmten Characters in einem String
CREATE OR REPLACE FUNCTION otg_numb_of_cert_char (inp_text text, part_char text) RETURNS int
	AS $$ 
	SELECT length(inp_text)-length(replace(inp_text, part_char, ''))
	$$
	LANGUAGE SQL
	RETURNS null on null INPUT;

	
	-- GET_INT_FROM_SEMIC_STRING

-- Gibt für das Textfeld v_my_string die Spannung / CaBLE des (in v_position) angegeben Levels (der Leitung) zurück.
-- Wenn Spannungen nicht als Integer angegeben sind, oder leer sind, wird NULL zurückgegeben.
-- 0 als WERT bleibt 0.
-- Funktion könnte mit otg_isint() deutlich vereinfacht werden
CREATE OR REPLACE FUNCTION otg_get_int_from_semic_string (v_my_string TEXT, v_position INT) RETURNS INT
AS $$
DECLARE 
v_volt_text TEXT;
v_volt_int INT;
BEGIN
v_volt_text := split_part(v_my_string,';',v_position);

v_volt_int := CASE 	WHEN 
			v_volt_text NOT SIMILAR TO '%[^0-9]%' --doppelt negativ (NOT und ^)
			AND 
			v_volt_text != ''
			
			THEN CAST (v_volt_text AS int)
			ELSE NULL END;
RETURN v_volt_int;
END;
$$ LANGUAGE plpgsql;


	-- GET_REAL_FROM_SEMIC_STRING

-- Gibt für das Textfeld v_my_string den Eintrag des (in v_position) angegeben Levels (der Leitung) als REAL zurück.
-- RETURNT NULL wenn kein REAL
-- 0 als WERT bleibt 0.
CREATE OR REPLACE FUNCTION otg_get_real_from_semic_string (v_my_string TEXT, v_position INT) RETURNS REAL
AS $$
DECLARE 
v_volt_text TEXT;
v_volt_real REAL;
BEGIN
v_volt_text := split_part(v_my_string,';',v_position);

IF otg_isreal(v_volt_text) THEN 
	v_volt_real := v_volt_text :: REAL; END IF;

RETURN v_volt_real;
END;
$$ LANGUAGE plpgsql;	


	-- GET_REAL_ARRAY_FROM_SEMIC_STRING

-- Bekommt Semicolon-String als Input und Returnt diesen als Real-Array
-- Returnt NULL, wenn String ist NULL oder leer ('')


CREATE OR REPLACE FUNCTION otg_get_real_array_from_semic_string (v_semic TEXT) RETURNS REAL []
AS $$
DECLARE
	v_array REAL [];
BEGIN
	
	IF NOT v_semic IS NULL AND NOT v_semic = '' THEN
	
		FOR i IN 1..(otg_numb_of_cert_char (v_semic, ';') + 1) 
		LOOP
			v_array [i] := otg_get_real_from_semic_string (v_semic, i);
		END LOOP;
		RETURN v_array;
	ELSE
		RETURN NULL; 
	END IF;




END;
$$ LANGUAGE plpgsql;


	-- GET_INT_FROM_WIRES_STRING

-- Zerteilt den Wires String (v_string) an der in v_position agegebene Stelle und gibt einen Integer mit der Wire-Anzahl zurück
-- Nur quad, triple, double oder single möglich!!
CREATE OR REPLACE FUNCTION otg_get_int_from_wires_string (v_string text, v_postition INT) RETURNS INT
AS $$
DECLARE
v_string_part text := split_part(v_string,';',v_postition);
BEGIN
RETURN CASE 	WHEN v_string_part = 'quad'	THEN 4
		WHEN v_string_part = 'triple'	THEN 3
		WHEN v_string_part = 'double'	THEN 2
		WHEN v_string_part = 'single'	THEN 1
		ELSE NULL END;	
END;
$$ LANGUAGE plpgsql;


	-- CALCULATE_SEMIC_SUM_FROM_STRING

-- Gibt die Summe der einzelnen zwischen den Semicolon stehenden Zahlen zurück
-- Für leere Strings ('') und NULL gibt die Funktion NULL zurück
-- für leere, von Semicolon getrennte "felder" wird Zahl 0 angenommen und die Summe wird nicht berechnet
CREATE OR REPLACE FUNCTION otg_calc_sum_from_semic_string (v_my_string TEXT) RETURNS INT
AS $$
DECLARE 
v_sum INT;
v_semic_numb INT;
BEGIN
	IF v_my_string = '' OR v_my_string IS NULL THEN v_sum := NULL; --Weil leere Daten nicht stimmen können, werden auch diesen NULL zugeordnet
		ELSE

		v_sum := 0;
		v_semic_numb := otg_numb_of_cert_char(v_my_string, ';');
		
		FOR i IN 1..(v_semic_numb + 1) LOOP
		v_sum := v_sum + otg_get_int_from_semic_string(v_my_string, i);	 
		END LOOP;
	END IF;
RETURN v_sum;
END;
$$ LANGUAGE plpgsql;

	-- POWER_LINE_READ_WIRES

-- Füllt die Spalte wires_array 
-- Das Array wird nur gefüllt, es nur eine Wires-Information gibt.	
CREATE OR REPLACE FUNCTION otg_read_wires () RETURNS VOID
AS $$
DECLARE 
	v_line RECORD;
BEGIN 
	FOR v_line IN 
	SELECT id, voltage, cables, wires, numb_volt_lev FROM power_line WHERE power = 'line'
	LOOP
				
		CASE 	-- Falls wires nicht NULL ist und nicht durch Semikolon getrennte Werte besitzt (Auflistung)
			WHEN 	NOT v_line.wires IS NULL AND
				otg_numb_of_cert_char (v_line.wires, ';') = 0 THEN 
				
				FOR i IN 1..v_line.numb_volt_lev 
				LOOP
					UPDATE power_line SET wires_array [i] = otg_get_int_from_wires_string (wires, 1)
						WHERE id = v_line.id;
				END LOOP;

			ELSE END CASE;
	END LOOP;
	
END;
$$ LANGUAGE plpgsql;


	-- POWER_LINE_READ_CIRCUITS

-- Falls Cables unbekannt sind und der Circuit-Eintrag bestimmte kriterien erfüllt (siehe Kommentare)
-- Kann die anzahl Leiterstränge berechnet werden, mit der später weitergerechnet wird.	
CREATE OR REPLACE FUNCTION otg_read_circuits () RETURNS VOID
AS $$
DECLARE 
	v_line RECORD;
	v_cables_per_circuit INT;
BEGIN 
	FOR v_line IN 
	-- Die Circuit-Abfrage muss nur für power = cable gemacht werden
	-- ...da sie für Freileitungen nur dann sinnvoll ist, falls z.B. 6 Leiderseile eigentlich nur 1 Stromkreise sind.
	-- Dies wird im Modell aber entweder durch Relations abgedeckt, oder überbleibende Leitungen verbinden sich ohnehin.
	SELECT id, voltage, numb_volt_lev, cables, circuits, frequency_array FROM power_line WHERE power = 'cable'
	LOOP
				
		 IF 	-- Wenn es noch keinen Cables-Eintrag gibt 
			-- (Generell wird über den Cables-Eintrag gearbeitet)
			v_line.cables IS NULL
			-- ... und es einen Circuit-Eintrag gibt
			AND NOT v_line.circuits IS NULL
			-- ... und dieser eindeutig ist (Keine Auflistung möglich)
			AND otg_numb_of_cert_char (v_line.circuits, ';') = 0 

			-- Wenn es nur eine Spannungsebene gibt ODER
			-- Die Anzahl der Spannungsebenen gleich der Anzahl der Circuits ist und
			-- auch die Frequenz jeder Spannungsebene der Leitung bekannt ist
			AND 	(v_line.numb_volt_lev = 1
				OR (v_line.numb_volt_lev = otg_get_int_from_semic_string (v_line.circuits, 1)
					AND array_length(v_line.frequency_array, 1) = v_line.numb_volt_lev))
					
			
			THEN
			-- Setzt Anzahl cable pro Stromkreis.
			-- Nur, wenn die Frequenz auf jeder Spannungsebene gleich ist 
			-- (sonst können die Stromkreise nicht zugeordnet werden)
			CASE 	WHEN 50 = ALL (v_line.frequency_array)
					THEN v_cables_per_circuit := 3;
				WHEN 0  = ALL (v_line.frequency_array)
					OR 16.7 = ALL (v_line.frequency_array)
					THEN v_cables_per_circuit := 2;
				-- Kann die Anzahl cables pro Stromkreis nicht gesetzt werden,
				-- ... wird unten (wieder) NULL in cables geschrieben.
				ELSE v_cables_per_circuit := NULL; 
			END CASE;
			
			CASE 	WHEN 	v_line.numb_volt_lev = 1
					THEN
					UPDATE power_line
						SET cables_array [1] = v_cables_per_circuit * otg_get_int_from_semic_string (v_line.circuits, 1)
						WHERE id = v_line.id;
				-- Falls mehrere eindeutig zuzuordnende Circuits (anzahl Circuits = Anzahl Spannungsebenen) 
				-- bekannt sind. Können Cables verteilt werden.	
				WHEN	v_line.numb_volt_lev > 1
					AND v_line.numb_volt_lev = otg_get_int_from_semic_string (v_line.circuits, 1)
					THEN
					FOR i IN 1..v_line.numb_volt_lev
					LOOP
						UPDATE power_line
							SET cables_array [i] = v_cables_per_circuit
							WHERE id = v_line.id;
					END LOOP;
					
				ELSE END CASE;
				
		END IF;
			
	END LOOP;
	
END;
$$ LANGUAGE plpgsql;


	-- POWER_LINE_READ_FREQUENCY 

-- Füllt die Spalte frequency_array 
	
CREATE OR REPLACE FUNCTION otg_read_frequency () RETURNS VOID
AS $$
DECLARE 
	v_line RECORD;
BEGIN 
	FOR v_line IN 
	SELECT id, voltage, cables, frequency, numb_volt_lev FROM power_line
	LOOP
			-- Wenn frequency nicht NULL ist und nur aus einem Wert besteht (keine Semicolons etc.)
			-- ... dann wird dieser Wert für alle Spannungsebenen übernommen
			-- (häufig bei 50 der FAll)
		CASE 	WHEN 	NOT v_line.frequency IS NULL AND
				otg_isreal(v_line.frequency) THEN 
				
				FOR i IN 1..v_line.numb_volt_lev 
				LOOP
					UPDATE power_line SET frequency_array [i] = frequency :: REAL
						WHERE id = v_line.id;
				END LOOP;

			-- Dieser Teil kann so nicht verwendet werden, da Frequency (ähnlich Wires) nur eine Auflistung der auf der...
			-- ...Freileitung vorhandenen Frequenzen darstellt. 
			-- Bei mehreren Einträgen könne diese nur verhältnismäßig aufwendig zugeordnet werden
				
			-- Falls die Informationen wirklich konsisten sind (Anzahl Spannungsebenen, Cables Einträge und Frequenzen)
			-- WHEN 	-- otg_numb_of_cert_char (v_line.voltage, ';') = otg_numb_of_cert_char (v_line.cables, ';') AND
-- 				otg_numb_of_cert_char (v_line.voltage, ';') = otg_numb_of_cert_char (v_line.frequency, ';') AND
-- 				NOT otg_isreal(v_line.frequency) THEN
-- 
-- 				UPDATE power_line SET frequency_array = otg_get_real_array_from_semic_string (v_line.frequency)
-- 					WHERE id = v_line.id;
			ELSE END CASE;
	END LOOP;
	
END;
$$ LANGUAGE plpgsql;


	-- INT_SUM

-- Berechnet die Summe von 4 Integern
-- NULL wird wir Zahl 0 berechnet!!!!
CREATE OR REPLACE FUNCTION otg_int_sum (int_1 INT, int_2 INT, int_3 INT, int_4 INT) RETURNS INT
AS $$
DECLARE 
v_sum INT := 0;
BEGIN
	IF NOT int_1 IS NULL THEN v_sum := v_sum + int_1; END IF;
	IF NOT int_2 IS NULL THEN v_sum := v_sum + int_2; END IF;
	IF NOT int_3 IS NULL THEN v_sum := v_sum + int_3; END IF;
	IF NOT int_4 IS NULL THEN v_sum := v_sum + int_4; END IF;

RETURN v_sum;
 
END;
$$ LANGUAGE plpgsql;


	-- ARRAY_SEARCH

-- Sucht wo ein Element in einem ARRAY zu finden ist.
CREATE OR REPLACE FUNCTION otg_array_search (v_element ANYELEMENT, v_array ANYARRAY) RETURNS INT
AS $$
	SELECT i
		FROM generate_subscripts ($2, 1) AS i 
		WHERE $2 [i] = $1
		ORDER BY i
$$ LANGUAGE sql STABLE;


	-- otg_array_search_2

-- Returnt ein INT [] mit den Indizes, wo das Element im Array zu finden ist (Element kann also mehrfach gefunden werden)
CREATE OR REPLACE FUNCTION otg_array_search_2 (v_element ANYELEMENT, v_array ANYARRAY) RETURNS INT []
AS $$
DECLARE
v_sub INT [] := NULL::int[];
v_count INT;
BEGIN 

	v_count := 0;
	FOR i IN 1..array_length(v_array, 1)
	LOOP
		IF v_array [i] = v_element THEN
			v_count := v_count + 1;
			v_sub [v_count] := i; 
		END IF;
	END LOOP;
RETURN v_sub;
END;	
$$ LANGUAGE plpgsql;


	-- ARRAY_REORDER_BY_MATCH

-- Ordnet ein Array neu. Und zwar so, dass die Werte, die auch im 2. Array auftauchen als erstes im Array stehen.
CREATE OR REPLACE FUNCTION otg_array_reorder_by_match (v_first INT [], v_sec INT []) RETURNS INT []
AS $$

DECLARE
v_in INT [];
v_out INT [];
n INT;
BEGIN
IF 	true = ALL (SELECT unnest (v_sec) IS NULL) --Alle einträge NULL
	OR v_sec IS NULL 
	THEN RETURN v_first; END IF;

FOREACH n IN ARRAY v_first
LOOP
	CASE 
	WHEN n = ANY (v_sec)
		THEN v_in := array_append(v_in, n);

	WHEN n != ANY (v_sec)
		THEN v_out := array_append(v_out, n);
	ELSE END CASE;
END LOOP;
RETURN v_in || v_out;

END
$$
LANGUAGE plpgsql;


-- ENTNORMALISIERUNG TABELLEN

	-- SEPERATE_POWER_RELATION_MEMBERS ()

-- Trennt die Members aus power_relations wieder aus dem Array auf...
CREATE OR REPLACE FUNCTION otg_seperate_power_relation_members () RETURNS void
AS $$ 
DECLARE 
v_members RECORD;
BEGIN
	
	FOR v_members IN
	SELECT id, members FROM power_circuits -- also alle
		
		LOOP

		FOR i IN 1..array_length(v_members.members, 1) 
			LOOP
				INSERT INTO  power_circ_members (relation_id, member_id)
							
					VALUES	(v_members.id, 
						v_members.members [i]);
			END LOOP;
		END LOOP;
				
END; 
$$
LANGUAGE plpgsql;


-- DATEN-ÜBERPRÜFUNG CABLES (POWER_LINE)	

	-- POWER_LINE_ALL-CABLE_COMPLETE

-- Untersucht, ob alle Cable-Informationen vollständig sind!
-- Wenn es zu einer vorhandenen Spannung keine Cable-Angabe gibt, dann RETURN false!
CREATE OR REPLACE FUNCTION otg_check_all_cables_complete (v_id bigint) RETURNS boolean
AS $$
DECLARE
ok BOOLEAN;
BEGIN
ok :=	(SELECT NOT(	NOT voltage_array [1] IS NULL AND cables_array [1] IS NULL 
			OR
			NOT voltage_array [2] IS NULL AND cables_array [2] IS NULL
			OR
			NOT voltage_array [3] IS NULL AND cables_array [3] IS NULL
			OR
			NOT voltage_array [4] IS NULL AND cables_array [4] IS NULL) 
	FROM power_line --OB dies Summe aufgeht wird in cable-conflic Funktion untersucht!
	WHERE id = v_id); 	
RETURN ok;				
END;
$$ LANGUAGE plpgsql;


	-- POWER_LINE_CABLE_COMPLETE 

-- Untersucht, ob die Cable-Information am angegeben Level (v_lev) der Leitung (v_id) vollständig ist
-- Ist das Leitungslevel nicht vorhanden (und daher auch kein Cable-Eintrag vorgesehen) wird true zurückgegeben.
CREATE OR REPLACE FUNCTION otg_check_cable_complete (v_id bigint, v_lev INT) RETURNS boolean
AS $$
BEGIN	
RETURN (SELECT NOT (NOT voltage_array [v_lev] IS NULL AND cables_array [v_lev] IS NULL) FROM power_line WHERE id = v_id);				
END;
$$ LANGUAGE plpgsql;


	-- KNOWN_CABLES_SUM 

-- Berechnet die Summe der bereits bekannten cable 
-- nicht zu verwechseln mit der cables_sum Spalte in der TAbelle!!!!! Diese wird direkt aus OSM-cables-string gelesen!!!!!
CREATE OR REPLACE FUNCTION otg_known_cables_sum (v_id BIGINT) RETURNS INT
AS $$
BEGIN
RETURN (SELECT otg_int_sum (cables_array [1], cables_array [2], cables_array [3], cables_array [4]) from power_line WHERE id= v_id);
END;
$$ LANGUAGE plpgsql;


	-- POWER_LINE_NUMB_UNKNOWN_CABLE_LEV

-- Gibt die Anzahl der noch unbekannten cable-levels zurück
CREATE OR REPLACE FUNCTION otg_numb_unknown_cables_lev (v_id BIGINT) RETURNS INT
AS $$
DECLARE
v_numb_known_cable_lev INT;
BEGIN
	v_numb_known_cable_lev := (SELECT 	  (NOT cables_array [1] IS NULL)::int 
						+ (NOT cables_array [2] IS NULL)::int 
						+ (NOT cables_array [3] IS NULL)::int 
						+ (NOT cables_array [4] IS NULL)::int
					FROM power_line
					WHERE id = v_id);
	

RETURN (SELECT (numb_volt_lev - v_numb_known_cable_lev) FROM power_line WHERE id = v_id); --Die Anzahl der Spannungsebenen minus Anzahl der bekannten Cable-Level sind die noch unbekannten...
END;
$$ LANGUAGE plpgsql;


	-- POWER_LINE_NUMB_UNKNOWN_FREQ_LEV

-- Gibt die Anzahl der noch unbekannten frequency-levels zurück
CREATE OR REPLACE FUNCTION otg_numb_unknown_freq_lev (v_id BIGINT) RETURNS INT
AS $$
DECLARE
v_numb_known_freq_lev INT;
BEGIN
	v_numb_known_freq_lev := (SELECT 	  (NOT frequency_array [1] IS NULL)::int 
						+ (NOT frequency_array [2] IS NULL)::int 
						+ (NOT frequency_array [3] IS NULL)::int 
						+ (NOT frequency_array [4] IS NULL)::int
					FROM power_line
					WHERE id = v_id);
	
--Die Anzahl der Spannungsebenen minus Anzahl der bekannten Frequency-Level sind die noch unbekannten...
RETURN (SELECT (numb_volt_lev - v_numb_known_freq_lev) FROM power_line WHERE id = v_id); 
END;
$$ LANGUAGE plpgsql;


	-- ALL_FREQ_LIKE

-- Bekommt voltage_array und frequency_array und gewünschte Frequenz und untersucht,
--...ob alle Frequenzen vergeben sind und = gewünschte Frequenz sind.
-- Dann wird true returnt. sonst false.
CREATE OR REPLACE FUNCTION otg_all_freq_like (	v_voltage_array INT [], 
						v_frequency_array REAL [], 
						v_freq REAL) RETURNS BOOLEAN
AS $$
BEGIN
	IF v_voltage_array IS NULL THEN RETURN FALSE; END IF;
	
	FOR i IN 1..array_length(v_voltage_array, 1)
	LOOP
		-- Falls Spannungs-level vorhanden UND frequenz NULL oder, nicht gleich v_freq, dann Return FALSE
		IF 	NOT v_voltage_array [i] IS NULL AND
			(v_frequency_array [i] IS NULL OR
			v_frequency_array [i] != v_freq) THEN
				RETURN FALSE; END IF;
	END LOOP;
RETURN TRUE;
END
$$ LANGUAGE plpgsql;


	-- POWER_LINE_CHECK_CABLE_CONFLICT 

--Guckt, ob es an einer Leitung zu einem CAble-Informationen-Konflikt kommt.
-- REturnt true, wenn entweder geeignete Nachbarn unterschiedliche cable-Informationen haben, oder...
--... falls alle spannungsebenen einen Cables-Eintrag haben dann true, wenn sie cable-Summen nicht stimmen

-- Zusammengefasst: Falls Summe nicht stimmt, oder Nachbarn verschiedene Infos!!

-- Nachbarinfo wird nicht untersucht, falls ein Ende innerhalb einer Substation liegt.
CREATE OR REPLACE FUNCTION otg_check_cable_conflict (v_id BIGINT) RETURNS BOOLEAN
AS $$
DECLARE 
v_id_line RECORD;
v_cables_neighbour INT [2]; 
v_volt INT; 
v_id_neighbour BIGINT;
v_lev_neighbour INT;

BEGIN
	SELECT id, all_neighbours, point_substation_id, cables_sum, voltage_array, power INTO v_id_line FROM power_line WHERE id = v_id;

	IF 	v_id_line.power = 'line' AND 
		otg_check_all_cables_complete (v_id) AND 
		v_id_line.cables_sum != otg_known_cables_sum (v_id)
		
		THEN RETURN true; END IF; -- Zuerst wird untersucht, ob die Cable-Summe stimmt.
	
	--IF (NOT v_id_line.point_substation_id [1] IS NULL) OR (NOT v_id_line.point_substation_id [2] IS NULL) THEN RETURN NULL; END IF; -- Wenn einer der Punke in einer Substation liegt, wird die Nachbarschafts-Cable-Abfrage nicht gestellt.
	
	FOR i in 1..4 LOOP -- i ist Level!
		v_volt := v_id_line.voltage_array [i]; --Spannung der Leitung an dem Leitungslevel
		v_cables_neighbour := '{NULL, NULL}'; -- Array wird auf NULL gesetzt, damit keine werte von der alten Interation übernommen werden.
		CONTINUE WHEN v_volt IS NULL; --Wenn es Spannungsebenen nicht gibt, dann nächsten Iterationsschritt
			FOR j in 1..2 LOOP -- j ist loc (1 = start)
				v_id_neighbour := v_id_line.all_neighbours [i][j][1][1]; 
				CONTINUE WHEN (v_id_neighbour IS NULL) OR (NOT v_id_line.all_neighbours [i][j][2][1] IS NULL); -- In den nächsten Iterationsschritt gehen, wenn garkein Nachbar, oder mehr als einer
				v_lev_neighbour := v_id_line.all_neighbours [i][j][1][2]; --Leitungs-Level auf der die Spannung zu finden ist.

				v_cables_neighbour [j]:= (SELECT cables_array [v_lev_neighbour] FROM power_line
								WHERE id = v_id_neighbour);
				
			END LOOP;
	
		IF v_cables_neighbour [1] != v_cables_neighbour [2]
			THEN RETURN true; -- Wenn ein Fehler auf irgendeiner Spannungseben auftritt, dann wird true zurückgegeben.	
		END IF;		
			
	END LOOP;

RETURN NULL;		
END;
$$ LANGUAGE plpgsql;



-- NACHBARSCHAFTSUNTERSUCHUNG

	-- POWER_LINE_GET_ALL_NEIGHBOURS

-- Funktion sucht für die Angegeben Leitung (v_id) alle Nachbarn (start und Ende) pro Spannungsebene.
-- Diese wird als ID (bigint) ARRAY zurückgegeben
CREATE OR REPLACE FUNCTION otg_get_all_neighbours (v_id BIGINT) RETURNS BIGINT [][][][]
AS $$
DECLARE

v_all_neighbours BIGINT [4][2][10][2] := 	'{{{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}}, 
		{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}}},
		{{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}},
		{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}}},
		{{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}},
		{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}}},
		{{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}},
		{{NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}, {NULL,NULL}}}}';
v_id_line RECORD;
v_volt INT ;
v_count INT := 0;
v_current_line RECORD;
v_lev INT [];
n INT; -- Spannungsebenen Variable der untersuchten Nachbarleitung
--v_no_frequency BOOLEAN;

BEGIN
	SELECT id, startpoint, endpoint, voltage_array, frequency_array INTO v_id_line FROM  power_line WHERE id = v_id;
	
	FOR i IN 1..4 LOOP -- geht die Spannungsebenen durch

	-- IF v_id_line.frequency_array [i] IS NULL THEN
-- 		v_no_frequency := true; 
-- 		ELSE 
-- 		v_no_frequency := false; 
-- 	END IF;

		
	v_volt := v_id_line.voltage_array [i]; -- Falls Spannungsebene i nicht vorhanden, brauch für diese kein Nachbar gesucht werden
	CONTINUE WHEN v_volt IS NULL; 

	v_count := 0;
		FOR v_current_line IN 
			SELECT id, power, voltage_array, frequency_array FROM power_line	
				WHERE 		
				(st_equals (power_line.startpoint, v_id_line.startpoint) OR 	
				st_equals (power_line.endpoint, v_id_line.startpoint)) --Start oder Endpunkt der gessuchten Leitung muss mit Startpunkt meiner Leitung überenstimmen
						
				AND id != v_id_line.id -- Soll nicht sich selbst auswählen
				AND NOT otg_array_search (v_volt, voltage_array) IS NULL -- Spannung muss in gesuchter Leitung (mindestens einmal) vorhanden sein vorhanden sein!
 
		LOOP
			v_lev := otg_array_search_2 (v_volt, v_current_line.voltage_array); -- Alle möglichen spannugns-Nachbarn der benachbarten Leitung (Array)
			-- v_lev kann hier nicht NULL sein, da bereits als Bedingung für diese Schleife nicht NULL ist
			FOREACH n IN ARRAY v_lev -- Soll durch die Werte des Arrays gehen
			LOOP	
			-- Frequenz soll an dieser stelle (doch) nicht untersucht werden. Diese Abfrage muss bei
			-- der konkreten Nachbarschaftsabfrage ohnehin noch gestellt werden und ist daher doppelt
				-- IF 	v_current_line.frequency_array [n] IS NULL OR 
-- 					v_id_line.frequency_array [i] IS NULL OR
-- 					v_current_line.frequency_array [n] = v_id_line.frequency_array [i] 
					-- Dann als Nachbarn anerkennen, wenn entweder eigene Frequenz oder Frequenz des Nachbarn noch unbekannt sind
					-- ... oder beide Frequenzen gleich sind.
-- 					THEN
					v_count := v_count + 1;
					v_all_neighbours [i][1][v_count][1]:= v_current_line.id;
					v_all_neighbours [i][1][v_count][2]:= n; -- Trägt im zweiten Feld ein, wo die Spannung zu finden ist.
-- 				END IF;
			END LOOP;
		END LOOP;
		
	v_count := 0;
		FOR v_current_line IN 
			SELECT id, power, voltage_array, frequency_array FROM power_line	
				WHERE 		
				(st_equals (power_line.startpoint, v_id_line.endpoint) OR 	
				st_equals (power_line.endpoint, v_id_line.endpoint)) --Start oder Endpunkt der gessuchten Leitung muss mit Startpunkt meiner Leitung überenstimmen
						
				AND id != v_id_line.id -- Soll nicht sich selbst auswählen
				AND NOT otg_array_search (v_volt, voltage_array) IS NULL -- Spannung muss in gesuchter Leitung vorhanden sein vorhanden sein!

		LOOP
			v_lev := otg_array_search_2 (v_volt, v_current_line.voltage_array); -- Alle möglichen spannugns-Nachbarn der benachbarten Leitung (Array)
			-- v_lev kann hier nicht NULL sein, da bereits als Bedingung für diese Schleife nicht NULL ist
			FOREACH n IN ARRAY v_lev -- Soll durch die Werte des Arrays gehen
			LOOP	
			-- 	IF 	v_current_line.frequency_array [n] IS NULL OR 
-- 					v_id_line.frequency_array [i] IS NULL OR
-- 					v_current_line.frequency_array [n] = v_id_line.frequency_array [i] 
					-- Dann als Nachbarn anerkennen, wenn entweder eigene Frequenz oder Frequenz des Nachbarn noch unbekannt sind
					-- ... oder beide Frequenzen gleich sind.
					--THEN
					v_count := v_count + 1;
					v_all_neighbours [i][2][v_count][1]:= v_current_line.id;
					v_all_neighbours [i][2][v_count][2]:= n; -- Trägt im zweiten Feld ein, wo die Spannung zu finden ist.
				--END IF;
			END LOOP;
		END LOOP;
	END LOOP;
RETURN v_all_neighbours;
END;
$$
LANGUAGE plpgsql;



-- CABLE-ANNAHMEN

	-- UNKNOWN_VALUE_HEURISTIC

--Führt alle Cable-Annahme Funktionen gemeinsam aus

CREATE OR REPLACE FUNCTION otg_unknown_value_heuristic () RETURNS void
AS $$
DECLARE
v_count_start INT;
v_count_end INT;
BEGIN
	v_count_end:=  (SELECT sum (otg_numb_unknown_cables_lev (id)) + sum (otg_numb_unknown_freq_lev (id))
					FROM power_line);
	LOOP
		v_count_start := v_count_end;
		
		PERFORM otg_3_cables_heuristic ();
		
		PERFORM otg_neighbour_heuristic ();
		
		PERFORM otg_sum_heuristic ();

		-- Zählt alle insgesamt vorhandenen unknown cables
		-- (sollte noch Frequenz abfragen)
		v_count_end:=  (SELECT sum (otg_numb_unknown_cables_lev (id)) + sum (otg_numb_unknown_freq_lev (id))
					FROM power_line);
		
	EXIT WHEN v_count_start - v_count_end = 0;
	END LOOP;

END;
$$ LANGUAGE plpgsql;


	-- otg_3_cables_heuristic 

-- "3 cables rule" (Frequenzabhängig gültig)
-- Schreibt alle Cables = 3, wo noch nicht vergebene Cables aus Calbes_sum durch Anzahl noch nicht berücksichtigter Spannugnsebenen 3 ergibt!
-- (Wenn alle Frequenzen = 50hz sind)
CREATE OR REPLACE FUNCTION otg_3_cables_heuristic () RETURNS void
AS $$
DECLARE 
v_line RECORD;
BEGIN

FOR v_line IN 
	SELECT id, voltage_array, cables_sum, frequency_array 
		FROM power_line
		-- Annahme wird benötigt, wo cables noch nicht komplett sind und...
		-- ...gilt nur für Freileitungen
		WHERE 	otg_check_all_cables_complete (id) = false AND 
			power = 'line'
		
LOOP
	-- Falls alle frequenzen bekannt sind und = 50 UND
	-- die 3 calbes-rule erfüllt ist, dann cables = 3 schreiben
	IF otg_all_freq_like (v_line.voltage_array, v_line.frequency_array, 50) AND
	(v_line.cables_sum - otg_known_cables_sum (v_line.id))/otg_numb_unknown_cables_lev (v_line.id) = 3 

		THEN 
			FOR i IN 1..4 
			LOOP
				-- Über all dort, wo cables noch unbekannt ist wird dann cables=3 geschrieben.
				IF NOT otg_check_cable_complete (v_line.id, i) THEN 
					UPDATE power_line 
						SET cables_array [i] = 3 WHERE id = v_line.id;
				END IF;
			END LOOP;
	END IF;

END LOOP;
END;
$$ LANGUAGE plpgsql;



	-- otg_neighbour_heuristic

-- Guckt alle Nachbarn (die in der Tabelle stehen) durch, ob geeignete Informationen enthalten. 
-- Wenn ja, dann schreibe Cable-Informationen und Frequenz
-- Frequenz kann auch dann übernommen werden, wenn alle Nachbarn dieselbe Frequenz haben. 
CREATE OR REPLACE FUNCTION otg_neighbour_heuristic () RETURNS void
AS $$
DECLARE 

v_id_line RECORD;
v_cables_neighbour INT; 
-- v_volt INT; 
v_id_neighbour BIGINT;
--v_lev_neighbour INT;

BEGIN

-- In die Tabelle all_neighbours sollen pro Leitung und Spannungsebene alle Nachbarn gespeichert werden...
-- ...die anschließend untersucht werden.
CREATE TABLE all_neighbours (
	id BIGINT,
	cables INT,
	frequency INT);

-- Geht alle Leitungen durch, die noch nicht komplett sind
FOR v_id_line IN 
	SELECT id, all_neighbours, voltage_array, cables_array, frequency_array 
		FROM power_line 
		-- An dieser Stelle reicht es nicht aus zu untersuchen, ob alle Cables vorhanden sind.
		-- Auch ob alle Frequencys vorhanden sind müsste untersucht werden
		-- Dies geschieht aber bereits am Anfang der 1. Schleife und sollte daher schnell genug sein.
		
LOOP
	
	-- i geht alle Spannungs-levels durch
	FOR i in 1..4 
	LOOP 
		-- Überspringen, falls Spannungs-Level nicht vorhanden...
		--... Und/oder cables und Frequenz schon bekannt
		CONTINUE WHEN 	v_id_line.voltage_array [i] IS NULL OR
		
				(NOT v_id_line.cables_array [i] IS NULL AND
				NOT v_id_line.frequency_array [i] IS NULL);
				
	
		FOR j in 1..2 LOOP -- j stehen für Anfang und Ende der Leitung (1 = start)

			-- Falls kein Nachbar vorhanden (erster Eintrag leer) dann diesen Schritt überspringen
			CONTINUE WHEN v_id_line.all_neighbours [i][j][1][1] IS NULL; 

			 
			-- Die folgende Schleife füllt die Tabelle all_neighbours
			-- (Tabelle wird vorher geleert)
			DELETE FROM all_neighbours; 
			FOR k in 1..10 LOOP --k ist "count" des Nachbarn (Auflistung)
			
				-- soll mit dem Füllen der Tabelle aufhören, falls ein Eintrag NULL ist 
				-- (dann gibt es auch keine Nachfolgenden)
				EXIT WHEN v_id_line.all_neighbours [i][j][k][1] IS NULL;

				-- Füllt mit jedem k eine Zeile der Nachbartabelle
				INSERT INTO all_neighbours (	id, 
								cables, 
								frequency)  
					SELECT id, 
						cables_array [v_id_line.all_neighbours [i][j][k][2]], 
						frequency_array [v_id_line.all_neighbours [i][j][k][2]]
					FROM power_line
					WHERE id = v_id_line.all_neighbours [i][j][k][1];
					
			END LOOP;

			-- Wenn die Frequenz der eigenen Leitung NULL ist ... 
			-- ... und die Frequenz aller Nachbarn gleich ist (count der Distincts = 1)
			-- kann diese übernommen werden 
			IF 	v_id_line.frequency_array [i] IS NULL AND
				(SELECT count (*) = 1 
					FROM (SELECT distinct on (frequency) frequency from all_neighbours) as freq)
				THEN
				UPDATE power_line 
					SET frequency_array [i] = (SELECT frequency FROM all_neighbours LIMIT 1)
					WHERE id = v_id_line.id;
			END IF;
			
			IF NOT v_id_line.frequency_array [i] IS NULL 
				THEN
				-- Alle Nachbarn mit nicht passender Frequenz werden gelöscht.
				-- (frequency IS NULL bleibt dabei noch erhalten)
				DELETE FROM all_neighbours 
					WHERE frequency != v_id_line.frequency_array [i];
			END IF;
			-- Alle überbleibenden könnten passende Nachbarn darstellen

			-- Nur wenn die Tabelle an dieser Stelle genau eine Zeile hat...
			-- ... kann eine Nachbarschaftsinformation abgerufen werden
			CONTINUE WHEN (SELECT COUNT (*) FROM all_neighbours) != 1;

			-- Aus Schleife ausbrechen, falls der (eine) Nachbar keinen Frequenzeintrag hat
			-- (in diesem Fall können auch keine cables übernommen werden
			CONTINUE WHEN (SELECT frequency FROM all_neighbours) IS NULL;

			
	
			-- Wenn die Cables der eigenen Leitung NULL ist UND Calbes der einen Nacharleitung nicht NULL ist,
			--... dann cables vom (einen) Nacharn übernehmen
			IF 	v_id_line.cables_array [i] IS NULL AND
				NOT (SELECT cables FROM all_neighbours) IS NULL
				THEN
				UPDATE power_line 
					SET cables_array [i] = (SELECT cables FROM all_neighbours)
					WHERE id = v_id_line.id;
				UPDATE power_line 
					SET cables_from_neighbour = true WHERE id = v_id_line.id;
			END IF;
				
		END LOOP;
				 
	END LOOP;
END LOOP;
DROP TABLE IF EXISTS all_neighbours;		
END;
$$ LANGUAGE plpgsql;


	-- otg_sum_heuristic

-- Überall, wo nur noch ein Cable-Level unbekannt ist und "cables_sum" nicht Null ist, wir über die Summe der letzte fehlende Cables-Eintrag vervollständigt.
-- Gilt Frequenzunabhängig
CREATE OR REPLACE FUNCTION otg_sum_heuristic () RETURNS void
AS $$
DECLARE 
v_line RECORD;
v_cables_left INT;

BEGIN
FOR v_line IN	
	SELECT id, cables_sum 
		FROM power_line 
		WHERE 	otg_check_all_cables_complete (id) = false 
			AND power = 'line' -- Annahme gilt nur für Freileitungen und nicht vollständige cables
LOOP
	-- Falls nur noch 1 Level unbekannt und cables_sum existiert	
	IF (otg_numb_unknown_cables_lev (v_line.id) = 1) AND (NOT v_line.cables_sum IS NULL)
		THEN
		-- Berechnet noch "übrige" cables
		v_cables_left := v_line.cables_sum - otg_known_cables_sum (v_line.id);
		FOR i IN 1..4 
		-- Geht alle level durch und findet so das noch unbekannte
		LOOP
			IF NOT otg_check_cable_complete (v_line.id, i) THEN 
				UPDATE power_line 
					SET cables_array [i] = v_cables_left WHERE id = v_line.id;
			END IF;
		END LOOP;

	END IF;
END LOOP;
END;
$$ LANGUAGE plpgsql;


-- WIRE ANNAHMEN

	-- otg_wires_assumption

-- Füllt alle noch nicht bekannten Wires des 380kv und 220kv Spannungsebene mit 4 bzw. 2 wires.
CREATE OR REPLACE FUNCTION otg_wires_assumption () RETURNS void
AS $$
DECLARE
v_min_voltage INT;
BEGIN
v_min_voltage := (SELECT val_int 
				FROM abstr_values 
				WHERE val_description = 'min_voltage');

UPDATE branch_data
	SET 	wires = 4 -- 4 als Srandard für 380kv	
	WHERE 	wires IS NULL AND
		voltage >= 380000 AND
		frequency = 50 AND
		power = 'line';
UPDATE branch_data
	SET 	wires = 2
	WHERE 	wires IS NULL AND
		voltage >= v_min_voltage AND
		voltage < 380000 AND
		voltage > 110000 AND
		frequency = 50 AND
		power = 'line';
UPDATE branch_data
	SET 	wires = 1 -- Standard für 110kv??
	WHERE 	wires IS NULL AND
		voltage >= v_min_voltage AND
		voltage <= 110000 AND
		frequency = 50 AND
		power = 'line';
UPDATE branch_data 
	SET wires = 1 -- Why that? HGÜ??
	WHERE wires IS NULL AND
	power = 'line';
	
END;
$$ LANGUAGE plpgsql;


-- Special Assumptions for 110kV

	--otg_110kV_cables()
CREATE OR REPLACE FUNCTION otg_110kv_cables () RETURNS VOID
AS $$
DECLARE 
	v_line RECORD;
	v_volt_idx INT[];
	i INT;
BEGIN 
	FOR v_line IN 
	-- Every power_line will be searched for 110kV voltage and then its cable entry will be checked
	-- This is not only done for power=line, because cable-circuits hav allready been translated to calbes
	SELECT id, voltage_array, cables_array, frequency_array FROM power_line 
	LOOP
		-- searches qhere 110kV is in voltage_array		
		v_volt_idx := otg_array_search_2 (110000, v_line.voltage_array);

		IF v_volt_idx IS NULL THEN CONTINUE; -- If 110kV can not be found -> next loop.
		END IF;
		
		FOREACH i IN ARRAY v_volt_idx
		LOOP
			IF  	v_line.cables_array[i] IS NULL AND
				(v_line.frequency_array[i] IS NULL OR
				v_line.frequency_array[i] = 50) -- Assumption only with frequency NULL or 50
			THEN
				UPDATE power_line 
					SET cables_array[i] = 3
					WHERE 	id = v_line.id; 
			END IF;
		END LOOP;
			
	END LOOP;
	
END;
$$ LANGUAGE plpgsql;


-- VORBEREITUNG POWER_LINE FÜR TOPOLOGIEBERECHNUNG

	-- SEPERATE_VOLTAGE_LEVELS

-- Trennt die Tabelle power_line auf und schreibt eine neue Zeile...
-- ... in die Tabelle power_line_sep für jede Spannungsebene einer Leitung
-- Lines bekommen Relation_id = 0

CREATE OR REPLACE FUNCTION otg_seperate_voltage_levels () RETURNS void
AS $$
DECLARE
v_line RECORD;
BEGIN
FOR v_line IN	
	SELECT 	id, 
		way, 
		power, 
		numb_volt_lev, 
		voltage_array, 
		cables_array,
		wires_array, 
		frequency_array,
		length,
		startpoint,
		endpoint
		FROM power_line
LOOP
	FOR i IN 1..v_line.numb_volt_lev LOOP
		INSERT INTO  power_line_sep (relation_id, 
						line_id,
						length,
						way,
						voltage,
						cables,
						wires,
						frequency,
						power,
						startpoint,
						endpoint)
			SELECT 	0,  -- Es wird Relation_id = 0 vergeben
				v_line.id,
				v_line.length,
				v_line.way,
				v_line.voltage_array [i],
				v_line.cables_array [i],
				v_line.wires_array [i],
				v_line.frequency_array [i],
				v_line.power,
				v_line.startpoint,
				v_line.endpoint;
	END LOOP;
				
END LOOP;	
END
$$
LANGUAGE plpgsql;



-- TOPOLOGIE-BERECHNUNG

	-- CREATE_GRID_TOPOLOGY

-- Hier werden die Topologien der Spannungsebenen / Stromkreise berechnet.
-- Dabei werden alle circuits bzw. line (pro spannungsebne) zunächst einzeln durchgegangen ...
--- ...und deren Topologie wird unabhängig berechnet

CREATE OR REPLACE FUNCTION otg_create_grid_topology (v_table TEXT) RETURNS void
AS $$
DECLARE
v_circuit RECORD;
v_params RECORD;
v_max_id BIGINT;
v_test RECORD;
BEGIN 

	DROP TABLE IF EXISTS branch_data_topo;
	EXECUTE 'CREATE TABLE branch_data_topo
		AS 
			SELECT relation_id, line_id, way, voltage, frequency, f_bus as source, t_bus as target
			FROM '|| v_table || ' LIMIT 0'; -- Leere Tabelle
	CREATE INDEX topo_source_idx ON branch_data_topo (source);
	CREATE INDEX topo_target_idx ON branch_data_topo (target);
	
FOR v_params IN
		-- Geht alle Kombinationen von Spannung und Frequenz (und relation_id) durch 
		-- Dadurch werden circuits nur einzeln betrachtet
		-- alle Ways haben die selbe relation_id und werde daher (automatisch) nicht nach dieser unterschieden
	EXECUTE 'SELECT relation_id as id, voltage, frequency FROM '|| v_table ||' GROUP BY relation_id, voltage, frequency' 
LOOP	

	-- Diese Tabelle wird von creatTopology automatisch erstellt und muss vorher gelöscht werden			
	DROP TABLE IF EXISTS branch_data_topo_vertices_pgr;
	
	-- Alle Circuit-members oder ways werden in die Tabelle branch_data_topo importiert...
	--... die der aktuellen Kombination aus id, voltage und frequency entsprechen
	EXECUTE 'INSERT INTO branch_data_topo (	relation_id, 
						line_id, 
						way, 
						voltage, 
						frequency, 
						source, 
						target)
			SELECT 	relation_id, 
				line_id, 
				way, 
				voltage, 
				frequency, 
				f_bus, 
				t_bus
			FROM '|| v_table || ' as main
			WHERE 	main.relation_id = '|| v_params.id ||' 
				AND main.voltage = '|| v_params.voltage ||'
				AND main.frequency = '|| v_params.frequency;

	-- pgr_createTopology should not be used.
	PERFORM pgr_createTopology (	'branch_data_topo', --source und target werden immer wieder auf NULL gesetzt und Topologie neu berechnet.
					0.0005, -- Is this a good buffer?
					'way', 
					'line_id');
			

	SELECT max(id) INTO v_max_id FROM bus_data; -- Höchste bereits in der Tabelle bus-data vrohandene ID
	IF v_max_id IS NULL THEN v_max_id := 0; END IF; -- Wenn Tabelle bus_data leer, dann...
	
	UPDATE branch_data_topo
 		SET 	source = source + v_max_id, -- Alle sources und targets werden um die maximal bereits vorhandenen ID erhöht
			target = target + v_max_id;
			
	
	EXECUTE 'UPDATE '|| v_table ||' as main SET 	
			f_bus = branch_data_topo.source,
			t_bus = branch_data_topo.target
		FROM branch_data_topo
		WHERE 	main.relation_id = branch_data_topo.relation_id AND
			main.line_id = branch_data_topo.line_id AND
			main.voltage = branch_data_topo.voltage AND
			main.frequency = branch_data_topo.frequency';		

		DELETE FROM branch_data_topo;

	-- Ob die Tabelle für Vertices erstellt wurde muss überprüft werden.
	-- (Wenn keine Topologie vorhande, wird diese Tabelle nicht erstellt)	
	IF EXISTS (SELECT relname FROM pg_class WHERE relname='branch_data_topo_vertices_pgr') -- Wenn die Tabelle existiert
		THEN
		-- Erhöhung muss in zwei Schritten geschehen, damit keine vorrübergehenden Doppelungen auftreten...
		-- ...branch_data_topo_vertices_pgr bestitz unique constraint der kurzzeitig verletzt würde
		UPDATE branch_data_topo_vertices_pgr
			SET id = -(id + v_max_id);
		UPDATE branch_data_topo_vertices_pgr 
			SET id = -id;

		ALTER TABLE branch_data_topo_vertices_pgr
			ADD COLUMN voltage INT;
		ALTER TABLE branch_data_topo_vertices_pgr
			ADD COLUMN frequency INT;
			
		UPDATE branch_data_topo_vertices_pgr 
			SET 	voltage = v_params.voltage,
				frequency = v_params.frequency;
				
		-- Komplette, geupdatete Tabelle wird in bus_data geschrieben...
		INSERT INTO bus_data (id, the_geom, voltage, frequency)
			SELECT id, the_geom, voltage, frequency
			FROM branch_data_topo_vertices_pgr;
	END IF;
	
END LOOP;
DROP TABLE IF EXISTS branch_data_topo_vertices_pgr;
DROP TABLE IF EXISTS branch_data_topo;
END; 
$$
LANGUAGE plpgsql;


	-- SET_COUNT

--Berechnet cnt (Anzahl der an einen Knoten angeschlossenen Branches)...
--... der angegebenen Tabelle (Herkunft: v_origin)
CREATE OR REPLACE FUNCTION otg_set_count (v_table TEXT, v_origin character varying (3)) RETURNS void
AS $$
BEGIN
EXECUTE 'UPDATE bus_data 
	SET cnt = (SELECT count (*) 
			FROM '||v_table||' as main 
			WHERE main.f_bus = bus_data.id OR main.t_bus = bus_data.id)
	WHERE origin = '|| quote_literal(v_origin);
END
$$
LANGUAGE plpgsql;

	-- HEURISTIK ANSCHLUSS STROMKREISE
	
		-- otg_connect_dead_ends_with_substation

-- Diese Funktion untersucht offene Enden und gibt dem offenen bus die Substation_id einer im Radius von ca 300m liegenden Substation
CREATE OR REPLACE FUNCTION otg_connect_dead_ends_with_substation () RETURNS void
AS $$
DECLARE
--v_circuits INT;
BEGIN

UPDATE bus_data
SET 	substation_id = 
	(SELECT power_substation.id AS substation_id 
		FROM power_substation, bus_data bus
		WHERE 	ST_Intersects (ST_Buffer(bus.the_geom, 0.003), power_substation.poly) AND -- 0.004° (breite) = 443m Buffer
			bus.id = bus_data.id LIMIT 1), -- verbessern: wenn Buffer mehrer findet soll er nähere nehmen!
	buffered = true
	WHERE cnt = 1 AND substation_id IS NULL AND origin = 'rel';
-- Das obere Update wird immer durchgeführt, auch wenn keine Überschneidung stattfindet
UPDATE bus_data
	SET buffered = false WHERE buffered = true AND substation_id IS NULL AND origin = 'rel'; -- Also alle nicht erfolgreichen Buffer
END
$$
LANGUAGE plpgsql;


		-- SUBSTRACT_CABLES_WITHIN_BUFFER

-- Zieht von den power_lines, die von einem gebufferten bus bis in die entsprechende Substation führen..
--... nach und nach die Cable der vorher offenen circuit ab
-- ist cables auf der Spannungsebene der power_line NULL, wird nichts unternommen!! (Wo sollte abgezogen werden?)
CREATE OR REPLACE FUNCTION otg_substract_cables_within_buffer (v_bus_id BIGINT) RETURNS void
AS $$

DECLARE

v_bus RECORD;
--v_member RECORD;
v_line RECORD;
v_lev INT [];
v_freq INT [];
v_cables_relation INT;
n INT;

BEGIN
	-- Speichert alle relevanten Information des gebufferten Knotens im Record v_bus
	SELECT the_geom, voltage, frequency, substation_id INTO v_bus FROM bus_data WHERE id = v_bus_id;
	
	-- Sucht den (einen) Stromkreis, der neu verbunden wurde und Speichert die Cables in v-cables_relation
	-- (Kann nur einen geben, da Bus vorher nur einen Anschluss hatte und Busses noch nicht verbunden wurden (nur "verschoben" in Substation)
	SELECT cables INTO v_cables_relation FROM power_circ_members WHERE f_bus = v_bus_id OR t_bus = v_bus_id;
	--v_cables_relation := v_member.cables;

	-- Geht alle power_lines durch, die (geometrisch) an diesem Bus und zudem mit derselben substation verbunden sind
	FOR v_line IN
		SELECT id, voltage_array, cables_array, frequency_array, cables_sum FROM power_line
			WHERE 	((v_bus.the_geom = power_line.startpoint AND
				v_bus.substation_id = point_substation_id [2]) OR
				(v_bus.the_geom = power_line.endpoint AND
				v_bus.substation_id = point_substation_id [1]))
			
			
	LOOP
		-- Speichert bei jeder Leitung alle möglichen Spannungsebenen in v_lev (InT [])
		v_lev := otg_array_search_2 (v_bus.voltage, v_line.voltage_array);
		
		-- zur nächsten Leitung springen, wenn Spannung auf dieser garnicht gefunden wurde
		CONTINUE WHEN v_lev IS NULL;

		-- Speichert bei jeder Leitung alle möglichen Frequenzen
		IF NOT v_line.frequency_array IS NULL 
			THEN
			v_freq := otg_array_search_2 (v_bus.frequency, v_line.frequency_array); 	
		END IF;

		-- Falls v_lev mehr als einen Eintrag hat werden die Einträge neu geordnet...
		--... und zwar so, dass in v_freq auftrtende Level zuerst im Array stehen.
		-- Dadurch werden zunächst die am besten passenden Levels ausgewählt
		IF array_length (v_lev, 1) > 1 
			THEN v_lev := otg_array_reorder_by_match (v_lev, v_freq); END IF;
		
		-- Durch diese Level wird wieder geloopt.
		-- (es können mehrere Leitungsebenen die selbe Spannung haben!)
		FOREACH n IN ARRAY v_lev
		LOOP 
			-- Zum nächsten Level springen, falls Frequenz nicht passend
			-- Exit geht nicht, da noch NULL frequency kommen kann.
			CONTINUE WHEN 	v_line.frequency_array [n] != v_bus.frequency;

			-- Falls keine Frequenz auf diesem Level vorhanden ist, können cables abgezogen werden
			-- Dann wird die Frequenz reingeschrieben
			IF v_line.frequency_array [n] IS NULL THEN
				UPDATE power_line 
					SET frequency_array [n] = v_bus.frequency
					WHERE id = v_line.id; END IF;
	
			CASE -- v_line.cables_array [n] = NULL muss nicht betrachtet werden, da keine subtraktion durchführbar
			WHEN v_line.cables_array [n] >= v_cables_relation
				THEN 
				UPDATE power_line 
					SET 	cables_array [n] = v_line.cables_array [n] - v_cables_relation,
						cables_sum = cables_sum - v_cables_relation
					WHERE id = v_line.id;
				RETURN; -- Es bleiben keine abziehbaren Relation_cables mehr über...
				
			WHEN v_line.cables_array [n] < v_cables_relation
				THEN
				UPDATE power_line	
					SET	cables_array [n] = 0, 
						cables_sum = cables_sum - v_line.cables_array [n]
					WHERE id = v_line.id;
				v_cables_relation := v_cables_relation - v_line.cables_array [n];
			ELSE	
			END CASE;
		END LOOP;
	END LOOP;
				
				
END
$$
LANGUAGE plpgsql;


	-- otg_connect_dead_ends_to_cont_lines

-- This function connects dead ends that are close to a transmission line...
-- to one of the transmission line vertices. 
-- Until now this is quick and dirty and needs to be improved.	

-- This function is now disabled, because the connection will be covered by the new
-- transfer-bus connection algorithm.
-- Can later be activated after improving this algorithm

-- CREATE OR REPLACE FUNCTION otg_connect_dead_ends_to_cont_lines () RETURNS void
-- AS $$
-- DECLARE
-- v_bus RECORD;
-- v_hit_line RECORD;
-- v_max_line_id BIGINT;
-- v_associated_line BIGINT;
-- BEGIN
-- v_max_line_id := (SELECT max(line_id) FROM power_line_sep);
-- FOR v_bus IN	
-- 	SELECT id, the_geom, voltage, frequency 
-- 		FROM bus_data WHERE 	origin = 'lin' AND
-- 					cntr_id = 'DE' AND
-- 					substation_id IS NULL AND
-- 					cnt = 1 AND 
-- 					voltage = 110000 -- unitl now only for 110kV
-- LOOP
-- 
-- 	-- Hit another line with this bus + buffer
-- 	SELECT f_bus, t_bus 
-- 				INTO v_hit_line 
-- 				FROM power_line_sep 
-- 				WHERE 	NOT f_bus = v_bus.id AND
-- 					NOT t_bus = v_bus.id AND -- Must not find itself
-- 					voltage = v_bus.voltage AND
-- 					frequency = v_bus.frequency AND
-- 					ST_intersects(way, ST_Buffer(v_bus.the_geom, 0.0005)) -- Same buffer as in CreateTopology
-- 					LIMIT 1; -- Include ORDER BY!!
-- 
-- 	CONTINUE WHEN v_hit_line IS NULL;
-- 
-- 	-- transmission lines with dead ends get... 
-- 	-- a new connection (with one of hit_line's bus)
-- 	-- This should be improved (distances, choice of bus etc....)
-- 	UPDATE power_line_sep SET f_bus = v_hit_line.f_bus 
-- 				WHERE f_bus = v_bus.id;
-- 	UPDATE power_line_sep SET t_bus = v_hit_line.t_bus
-- 				WHERE t_bus = v_bus.id;
-- 				
-- END LOOP;	
-- END
-- $$
-- LANGUAGE plpgsql;


	-- otg_cut_off_dead_ends_iteration

-- Diese Funktion löscht iterativ alle Knoten an welche nur eine Line angeschlossen ist.
CREATE OR REPLACE FUNCTION otg_cut_off_dead_ends_iteration (v_table TEXT, v_origin character varying (3)) RETURNS void
AS $$
DECLARE
v_count INT := 0;

BEGIN
	
	LOOP
	EXECUTE 'DELETE FROM '|| v_table ||' WHERE f_bus = t_bus';
	
	EXECUTE 'UPDATE bus_data 
	SET cnt = (SELECT count (*) 
			FROM '||v_table||' as main 
			WHERE main.f_bus = bus_data.id OR main.t_bus = bus_data.id)
	WHERE origin = '|| quote_literal(v_origin);
			
	
	SELECT count (*) INTO v_count FROM bus_data WHERE origin = v_origin AND cnt = 1 AND substation_id IS NULL;
	EXIT WHEN v_count = 0; -- Abbrechen, wenn keine neuen 1er mehr gefunden werden.

	-- Deletes all lines with endbus cnt=1
	EXECUTE 'DELETE FROM '||v_table||' WHERE 	(f_bus IN (SELECT id FROM bus_data 
								WHERE 	origin = '|| quote_literal(v_origin) ||' AND 
									cnt = 1 AND 
									substation_id IS NULL) OR
							t_bus IN (SELECT id FROM bus_data 
								WHERE 	origin = '|| quote_literal(v_origin) ||' AND 
									cnt = 1 AND 
									substation_id IS NULL))';
					
	
	END LOOP;
	
END
$$
LANGUAGE plpgsql;


	-- otg_bus_analysis

-- Ergänzt die Tabelle bus_data (Länderkennung, Substation_id, Auslands-Substation)
CREATE OR REPLACE FUNCTION otg_bus_analysis (v_origin character varying (3)) RETURNS void
AS $$
BEGIN

-- Jedem Knoten wird eine Länderkennung gegeben
UPDATE bus_data
	SET cntr_id = 	(SELECT nuts.nuts_id
			FROM nuts_poly nuts, bus_data bus
			WHERE 	ST_Within (bus.the_geom, nuts.geom) AND
				nuts.stat_levl_ = 0 AND -- Damit nur komplette Länder berücksichtigt werden (erste Ebene)
				bus.id = bus_data.id LIMIT 1)
	WHERE origin = v_origin;


-- untersuchung Substations
UPDATE bus_data
	SET substation_id = 
		(SELECT power_substation.id
		FROM power_substation, bus_data bus
		WHERE ST_Within (bus.the_geom, power_substation.poly) AND
			bus.id = bus_data.id LIMIT 1)
	WHERE origin = v_origin;
		


-- Alle offenen Enden im Ausland bekommen die Substation_id = 0
UPDATE bus_data 
	SET substation_id = 0
	WHERE 	cnt = 1 AND 
		substation_id IS NULL AND 
		cntr_id != 'DE' AND 
		origin = v_origin;
	

END
$$
LANGUAGE plpgsql;



-- ÜBERLAGERUNG STROMKREISE ÜBER LEITUNGEN

	-- otg_substract_circuits

-- Diese Funktion zieht cables-Wert der Stormkreise (circuits) von den...
--... entsprechenden Leitungen (power_line) ab.
-- Dadurch wird die Redundanz der beiden Tabellen entfernt.
CREATE OR REPLACE FUNCTION otg_substract_circuits () RETURNS void
AS $$
DECLARE 
v_member RECORD;
v_line RECORD;
v_lev INT [];
v_freq INT [];
n INT;
BEGIN
	-- Es wird durch alle power_circ_members geloopt
	FOR v_member IN
		SELECT line_id as id, relation_id, voltage, cables, wires, frequency, way FROM power_circ_members
		
	LOOP
		-- Für jeden Stromkreis-Member wird die zugehörige Power_line ausgewählt
		SELECT id, cables_array, voltage_array, frequency_array INTO v_line 
			FROM power_line 
			WHERE id = v_member.id;

		
		
		-- Speichert bei jeder Leitung alle möglichen Spannungsebenen in v_lev (InT [])
		v_lev := otg_array_search_2 (v_member.voltage, v_line.voltage_array);
			

		-- Wenn es die Spannung auf der Leitung nicht gibt, wird problem gemeldet. 
		-- Es wird kein Wert abgezogen (Stromkreise wird mehr vertraut)
		IF v_lev IS NULL THEN 
			INSERT INTO problem_log (object_type,
						line_id,
						relation_id,
						way, 
						voltage,
						cables,
						wires, 
						frequency,
						problem)
						
				VALUES ('circuit_member',
					ARRAY [v_member.id], 
					v_member.relation_id, 
					ST_Multi(v_member.way), 
					v_member.voltage, v_member.cables, v_member.wires, v_member.frequency,
					'voltage_missing_on_power_line');
				
			CONTINUE; 
		END IF;

		-- Speichert bei jeder Leitung alle möglichen Frequenzen
		IF NOT v_line.frequency_array IS NULL 
			THEN
			v_freq := otg_array_search_2 (v_member.frequency, v_line.frequency_array); 	
		END IF;

		-- Falls v_lev mehr als einen Eintrag hat werden die Einträge neu geordnet...
		--... und zwar so, dass in v_freq auftrtende Level zuerst im Array stehen.
		-- Dadurch werden zunächst die am besten passenden Levels ausgewählt
		IF array_length (v_lev, 1) > 1 
			THEN v_lev := otg_array_reorder_by_match (v_lev, v_freq); END IF;

		
		-- Durch diese Level wird wieder geloopt.
		-- (es können mehrere Leitungsebenen die selbe Spannung haben!)
		-- Am besten passende zuerst (Reihenfolge)
		FOREACH n IN ARRAY v_lev
		LOOP
			-- Wenn cables an diesem Level = NULL, wird die Leitungs-level (power_line as branch)
			-- ... später mit der Action "missing cables" gelöscht. 
			-- (Weitere Informationen über Cables können nun nicht hinzukommen, 
			-- da Annahme Algorithmen schon durchgelaufen sind)
			CONTINUE WHEN v_line.cables_array [n] IS NULL; 

			-- Falls Frequenz verschieden werden keine cables abgezogen
			CONTINUE WHEN 	v_line.frequency_array [n] != v_member.frequency;
			
			-- Falls keine Frequenz auf diesem Level vorhanden ist, können cables abgezogen werden
			-- Dann wird die Frequenz reingeschrieben
			-- Zuerst werden alle Level mit passender Frequenz durchgegangen 
			-- Durch das Schreiben der FRequenz kann kein Fehler entstehen
			IF v_line.frequency_array [n] IS NULL THEN
				UPDATE power_line 
					SET frequency_array [n] = v_member.frequency
					WHERE id = v_line.id; END IF;
					
			UPDATE power_line 
				SET 	cables_array [n] = cables_array [n] - v_member.cables,
					cables_sum = cables_sum - v_member.cables
				WHERE id = v_member.id;
			EXIT; -- Wenn Schleife einmal erfolgreich muss diese beendet werden.
		END LOOP;
	END LOOP;		
	
END; 
$$
LANGUAGE plpgsql;


-- BEARBEITUNG UMSPANNWERKE

	--CONNECT_SUBSTATION_VERTICES

-- Ändert die Topologie, sodass Alle Punkte innerhalb einer Substation (je Spannungsebene und Frequenz)... 
-- ... zu einem vereinigt werden
-- An dieser Stelle sind nurnoch Frequenzen 50Hz und 0 Hz vorhanden
CREATE OR REPLACE FUNCTION otg_connect_substation_vertices () RETURNS void
AS $$
DECLARE
v_subst_bus RECORD;
v_new_id BIGINT = (SELECT max(id) + 1 FROM bus_data);
BEGIN
	-- Geht alle Knoten (verschiedene Spannungen und Frequenzen) pro Umspannwerk durch
	FOR v_subst_bus IN
		SELECT distinct on (substation_id, voltage, frequency) voltage, substation_id, frequency, cntr_id 
		FROM bus_data
		WHERE NOT substation_id IS NULL 
	LOOP
	CONTINUE WHEN v_subst_bus.substation_id = 0; --Auslands-Umspannwerke bestehen aus "offenen Enden" und können nicht ineinander verbunden werden

	-- Alle Busses innerhalb einer Substation, die die selbe Spannung und Frequenz haben werden durch 
	-- einen gemeinsamen, neuen Knoten ersetzt.
	UPDATE branch_data 
		SET f_bus = v_new_id
		FROM bus_data
		WHERE 	branch_data.f_bus = bus_data.id AND
			bus_data.voltage = v_subst_bus.voltage AND
			bus_data.frequency = v_subst_bus.frequency AND
			bus_data.substation_id = v_subst_bus.substation_id;

	UPDATE branch_data 
		SET t_bus = v_new_id
		FROM bus_data
		WHERE 	branch_data.t_bus = bus_data.id AND
			bus_data.voltage = v_subst_bus.voltage AND
			bus_data.frequency = v_subst_bus.frequency AND
			bus_data.substation_id = v_subst_bus.substation_id;

	-- Nun nicht mehr verwendete (übergangene) Busses werden gelöscht.
	DELETE FROM bus_data WHERE 	voltage = v_subst_bus.voltage AND
					frequency = v_subst_bus.frequency AND
					substation_id = v_subst_bus.substation_id;

	-- An dieser Stelle wird der neue Knoten (v_new_id) erstellt und mit den entsprechenden Werten gefüllt	
	INSERT INTO bus_data (id, the_geom, voltage, frequency, substation_id, cntr_id)
		SELECT 	v_new_id, 
			-- Mittelpunkt der Station
			ST_Centroid(power_substation.poly), 
			v_subst_bus.voltage, 
			v_subst_bus.frequency,
			v_subst_bus.substation_id, 
			v_subst_bus.cntr_id
			
		-- Für den Mittelpunkt der Station
		FROM power_substation
		WHERE power_substation.id = v_subst_bus.substation_id;
	-- Neue ID für den nächten Punkt wird erhöht
	v_new_id = v_new_id + 1;
	END LOOP;
END
$$
LANGUAGE plpgsql;


	-- CONNECT_TRANSFORMERS ()

-- Erstellt innerhalb der Umspannwerke Tranformator-Leitungen, die die Substation-Knoten verbinden
CREATE OR REPLACE FUNCTION otg_connect_transformers () RETURNS void
AS $$

DECLARE 
v_substation RECORD;
v_buses INT [];
v_numb_buses INT;
i INT;

BEGIN
FOR v_substation IN 
	SELECT id FROM power_substation 
		WHERE id IN (SELECT substation_id FROM bus_data WHERE NOT substation_id IS NULL) -- Dadurch fallen die offenen Auslands-Enden raus (diese brauchen auch nicht betrachtet zu werden)
	LOOP
	-- v_busus ist Array mit den IDs der Knoten innerhalb eines Umspannwerks
	-- Dieses wird nach Spannung geordnet, damit Spannungsebenen der Reihe nach verbunden werden.
	v_buses := (SELECT ARRAY (SELECT id FROM bus_data WHERE substation_id = v_substation.id ORDER BY voltage)); --v_substation.id);
	v_numb_buses := array_length (v_buses, 1);
	IF v_numb_buses > 1 THEN -- Also verschiedene, betrachtete Spannungsebenen im Umspannwerk ankommen
		FOR i IN 1..(v_numb_buses - 1)
			LOOP
				INSERT INTO branch_data (way, f_bus, t_bus, power)
					VALUES ( ST_MakeLine (	(SELECT the_geom FROM bus_data WHERE id = v_buses [i]),
								(SELECT the_geom FROM bus_data WHERE id = v_buses [i+1])),
						v_buses[i],
						v_buses[i+1],
						'transformer');
				
			END LOOP; 
		END IF;
	END LOOP;
END
$$
LANGUAGE plpgsql;


-- LEITUNGS- VEREINFACHUNG

	-- SIMPLIFY_BRANCHES

-- Löscht alle Knoten, an die genau 2 identische Leitungen angeshclossen sind...
-- ... und erstellt eine neue Leitung mit der Summer der Längen der alten Leitungen.
CREATE OR REPLACE FUNCTION otg_simplify_branches (v_vertex_id BIGINT) RETURNS void 
AS $$
DECLARE
v_vertex RECORD;
v_line RECORD;
v_length REAL := 0;
v_f_bus_t_bus BIGINT [];
v_voltage INT [];
v_cables INT [];
v_frequency REAL [];
v_wires INT [];
v_power TEXT [];
v_line_ids BIGINT [];
v_circuit_ids BIGINT [];
v_ways geometry (Linestring) [];

v_branch_max_id BIGINT;

BEGIN

		
	FOR v_line IN
		SELECT line_ids, ways, f_bus, t_bus, length, relation_id, voltage, cables, frequency, wires, power 
		FROM branch_data
		WHERE branch_data.f_bus = v_vertex_id OR branch_data.t_bus = v_vertex_id
	LOOP 
	IF v_line.f_bus <> v_vertex_id THEN v_f_bus_t_bus := v_f_bus_t_bus || v_line.f_bus; END IF;
	IF v_line.t_bus <> v_vertex_id THEN v_f_bus_t_bus := v_f_bus_t_bus || v_line.t_bus; END IF;

	-- einfach ADDITION
	v_length := v_length + v_line.length; --Länge wird addiert
	-- ARRAY wird durch value erweitert
	v_circuit_ids = v_circuit_ids || v_line.relation_id;
	v_voltage = v_voltage || v_line.voltage;
	v_cables = v_cables || v_line.cables;
	v_frequency = v_frequency || v_line.frequency;
	v_wires = v_wires || v_line.wires;	
	v_power = v_power || v_line.power;
	
	-- ARRAYS werden durch ARRAYS erweitert
	v_line_ids = v_line_ids || v_line.line_ids;
	v_ways = v_ways || v_line.ways;
	
	END LOOP;
	IF 	array_length (v_f_bus_t_bus, 1) = 2 AND 
		array_length (v_voltage, 1 ) = 2 AND --Redundant!
		v_cables [1] = v_cables [2] AND 
		v_frequency [1] = v_frequency [2] AND
		--v_wires [1] = v_wires [2] AND -- wires wird nicht als Bedingung verwendet, da später keinen Einfluss auf Kennwert!
		v_circuit_ids [1] = v_circuit_ids [2] AND
		v_voltage [1] = v_voltage [2] AND
		v_power [1] = v_power [2]
		THEN

	DELETE FROM bus_data WHERE id = v_vertex_id; -- LInes werden nicht automatisch mitgelöscht
	DELETE FROM branch_data WHERE branch_data.f_bus = v_vertex_id OR branch_data.t_bus = v_vertex_id;
	
	INSERT INTO branch_data (	relation_id, 
					line_ids,
					length,
					f_bus,
					t_bus,
					voltage,
					cables,
					frequency,
					wires,
					power,
					ways)
		SELECT  v_circuit_ids [1], 
			v_line_ids, 
			v_length, 
			v_f_bus_t_bus [1],
			v_f_bus_t_bus [2],
			v_voltage [1],
			v_cables [1],
			v_frequency [1],
			NULL, --v_wires [1], -- wires wird nicht verwendet...
			v_power [1],
			v_ways;
			
	END IF;

END
$$
LANGUAGE plpgsql;


	-- SIMPLIFY_BRANCHES_ITERATION

--Führt die notwendigen Schritte in der Interation durch.
CREATE OR REPLACE FUNCTION otg_simplify_branches_iteration () RETURNS void
AS $$
DECLARE
v_count_old INT;
v_count_new INT;
BEGIN
	v_count_new := (SELECT count (*) FROM bus_data Where cnt = 2 AND substation_id IS NULL);
	
	LOOP
	PERFORM otg_simplify_branches (id) FROM bus_data WHERE cnt = 2 AND substation_id IS NULL; 
	DELETE FROM branch_data WHERE f_bus = t_bus;
	UPDATE bus_data 
	SET cnt = (SELECT count (*) 
			FROM branch_data 
			WHERE branch_data.f_bus = bus_data.id OR branch_data.t_bus = bus_data.id);
	DELETE from bus_data WHERE cnt = 0;
	v_count_old := v_count_new;
	v_count_new := (SELECT count (*) FROM bus_data Where cnt = 2 AND substation_id IS NULL);
	EXIT WHEN v_count_old - v_count_new = 0;
	END LOOP;
END
$$
LANGUAGE plpgsql;


-- GRAPHENANALYSE

	-- GRAPH_DFS

-- Unersucht den Graph auf Zusammenhang. Knoten, die nicht zum Hauptgraph gehören behalten discovered = false
CREATE OR REPLACE FUNCTION otg_graph_dfs (v_vertex BIGINT) RETURNS void
AS $$ 
DECLARE 
v_neighbours BIGINT [];
v_array_length INT;
BEGIN
UPDATE bus_data SET discovered = true WHERE id = v_vertex;

-- Alle vorhandenen Nachbarknoten werden im Array gespeichert
v_neighbours := ARRAY (SELECT t_bus FROM branch_data WHERE f_bus = v_vertex); 
v_neighbours := v_neighbours || ARRAY (SELECT f_bus FROM branch_data WHERE t_bus = v_vertex);

v_array_length := (SELECT array_length (v_neighbours, 1));
FOR i IN 1..v_array_length
	LOOP
	IF (SELECT discovered FROM bus_data WHERE id = v_neighbours [i]) = false -- Also noch nicht discovered
		THEN PERFORM otg_graph_dfs (v_neighbours [i]); END IF;
	END LOOP;
END; 
$$
LANGUAGE plpgsql;


	-- otg_graph_analysis ()

-- Checks if graph_dfs is selected true. Then deletes disconnected Graphs
CREATE OR REPLACE FUNCTION otg_graph_analysis () RETURNS void
AS $$ 
BEGIN
IF (SELECT val_bool 
	FROM abstr_values
	WHERE val_description = 'graph_dfs') -- Only if graph_dfs is selected True (Python Script)
	THEN
	
-- Evtl. vorher untersuchen
-- Untersucht den Graph auf Zusammenhang (beginnt beim Slack-knoten)
	PERFORM otg_graph_dfs ((SELECT id FROM bus_data 
			WHERE substation_id = (SELECT val_int FROM abstr_values WHERE val_description = 'main_station')
			LIMIT 1));

-- Es werden die Branches und Busses gelöscht, die zu abgetrennten Netzbereichen gehören.
-- Diese werde zur Zeit nicht ins Problem-Log aufgenommen
	DELETE FROM branch_data WHERE 	f_bus IN (SELECT id FROM bus_data WHERE discovered = false) OR
					t_bus IN (SELECT id FROM bus_data WHERE discovered = false);
	DELETE FROM bus_data WHERE discovered = false;
END IF;
END
$$
LANGUAGE plpgsql;


	-- otg_transfer_busses ()
	
-- This is the new tranfer-bus function
-- The old one can be used for the subgrid connection...

CREATE OR REPLACE FUNCTION otg_transfer_busses () RETURNS void
AS $$ 
DECLARE


v_search_area geometry (Polygon, 4326);

v_cnt INT;
v_smallest_dist FLOAT;
v_this_dist FLOAT;

v_trans_bus_id BIGINT;
v_trans_bus_geom geometry (Point, 4326);
v_branch_id BIGINT;
v_branch_way geometry (Linestring, 4326);
v_branch_voltage FLOAT;
v_branch_f_bus BIGINT;
v_branch_t_bus BIGINT;
v_branch_cables INT;
v_branch_power TEXT;
v_branch_length FLOAT;

v_transfer_bus_bus_data_id BIGINT;

v_trans_bus RECORD;
v_branch RECORD;

v_closest_point_loc FLOAT;
v_closest_point_geom geometry (Point, 4326);

v_new_connection_geom geometry (Linestring, 4326);
v_new_connection_length FLOAT;

v_new_way_geom_start geometry (Linestring, 4326);
v_new_way_length_start FLOAT;
v_new_way_geom_end geometry (Linestring, 4326);
v_new_way_length_end FLOAT;

v_closest_bus_id BIGINT;

v_max_bus_id BIGINT;
v_max_branch_id BIGINT;

BEGIN

IF (SELECT val_bool 
	FROM abstr_values
	WHERE val_description = 'transfer_busses') -- Only if transfer_busses is selected True (Python Script)
	THEN

	-- All the substations that are allready found can be ignored
	DELETE FROM transfer_busses
		WHERE osm_id IN (SELECT substation_id FROM bus_data);

	LOOP -- Loops until all transfer busses are connected.
		v_cnt := (SELECT count(*) FROM transfer_busses);
		EXIT WHEN v_cnt = 0;

		v_smallest_dist := 500000; -- Initial buffer size in meters

		-- Loops through all (left) transfer busses
		FOR v_trans_bus IN
			SELECT osm_id, center_geom
				FROM transfer_busses

		LOOP
			-- Geography allows to set the buffer radius in meters.
			-- ...Then casted back to geometry.
			v_search_area := ST_Buffer(	v_trans_bus.center_geom::geography, 
							v_smallest_dist)::geometry;
							
		
		 	FOR v_branch IN
				SELECT branch_id, voltage, way, f_bus, t_bus, cables, power, length
					FROM branch_data
					WHERE 	ST_Intersects(way, v_search_area) AND -- Just the lines/branches within that intersect the buffer
						frequency = 50
			LOOP

				v_this_dist := ST_Distance(	v_trans_bus.center_geom::geography, 
								v_branch.way::geography); -- in meters

				
				IF (v_this_dist < v_smallest_dist)
					THEN 
					v_smallest_dist := v_this_dist;
					v_trans_bus_id := v_trans_bus.osm_id;
					v_trans_bus_geom := v_trans_bus.center_geom;
					v_branch_id := v_branch.branch_id;
					v_branch_way := v_branch.way;
					v_branch_voltage := v_branch.voltage;
					v_branch_f_bus := v_branch.f_bus;
					v_branch_t_bus := v_branch.t_bus;
					v_branch_cables := v_branch.cables;
					v_branch_power := v_branch.power;
					v_branch_length := v_branch.length;

				END IF;
-- 				
			END LOOP;
		END LOOP;

		-- Here, all values for the new branches and busses are calculated
		-- for new bus:
		v_closest_point_loc := ST_LineLocatePoint(	v_branch_way, 
								v_trans_bus_geom); --FLOAT between 0 and 1 (Point location on Linesting)

		v_closest_point_geom := ST_LineInterpolatePoint(v_branch_way, 
								v_closest_point_loc); -- Geometry of closest point

		-- Checks if some bus is less than 75m away
		v_closest_bus_id := NULL;
		IF v_branch_length * v_closest_point_loc < 75
			THEN
			v_closest_bus_id := v_branch_f_bus;
			END IF;
		IF v_branch_length * (1 - v_closest_point_loc) < 75
			THEN
			v_closest_bus_id := v_branch_t_bus;
			END IF;

		-- In every case a new bus (transfer bus) needs to be added:
		v_max_bus_id := (SELECT max(id) FROM bus_data);	

		v_transfer_bus_bus_data_id := v_max_bus_id + 1;
		INSERT INTO bus_data (	id, 
					the_geom, 
					voltage, 
					frequency, 
					substation_id, 
					cntr_id)
			VALUES (v_transfer_bus_bus_data_id, 
				v_trans_bus_geom,
				v_branch_voltage,
				50,
				v_trans_bus_id,
				'DE');
				
		IF NOT v_closest_bus_id IS NULL --thus, there is a close bus/substation
			THEN

			v_new_connection_geom := ST_MakeLine(	v_trans_bus_geom, (SELECT the_geom 
								FROM bus_data 
								WHERE id = v_closest_bus_id));
			v_new_connection_length := ST_Length(v_new_connection_geom::geography);
			
				--make new line here and use this distance!!!!	
			v_max_branch_id := (SELECT max(branch_id) FROM branch_data);
			INSERT INTO branch_data (	branch_id, 
							length,
							f_bus,
							t_bus,
							voltage,
							cables,
							frequency,
							power,
							way)
				VALUES(	v_max_branch_id + 1,
					v_new_connection_length,
					v_transfer_bus_bus_data_id, --f_bus
					v_closest_bus_id, --t_bus
					v_branch_voltage, -- of the found branch
					3,
					50,
					'cable',
					v_new_connection_geom);
				
			
		ELSE -- no direct connection to any bus...

			--... the other bus represents the new grid-bus (Muffe)
			INSERT INTO bus_data (	id, 
						the_geom, 
						voltage, 
						frequency, 
						substation_id, 
						cntr_id)
				VALUES (v_max_bus_id + 2, -- the new grid-bus
					v_closest_point_geom,
					v_branch_voltage,
					50,
					NULL,
					'DE');
										
			-- for new (split-up) branches
			v_new_way_geom_start := ST_Line_Substring(	v_branch_way, 
									0, 
									v_closest_point_loc); -- New line Substring (first part)
									
			v_new_way_length_start := ST_length(v_new_way_geom_start::geography);
									
			v_new_way_geom_end := ST_Line_Substring(	v_branch_way, 
									v_closest_point_loc, 
									1); -- New line Substring (second part)

			v_new_way_length_end := ST_length(v_new_way_geom_end::geography);

				
			DELETE FROM branch_data WHERE branch_id = v_branch_id; -- Old branch needs to be deleted
				
			v_max_branch_id := (SELECT max(branch_id) FROM branch_data);
			-- 3 branches are inserted: the 2 substrings, and the new one to connect the transfer bus:
			
			-- Start Substring Branch:
			INSERT INTO branch_data (	branch_id, 
							length,
							f_bus,
							t_bus,
							voltage,
							cables,
							frequency,
							power,
							way)
				VALUES(	v_max_branch_id + 1,
					v_new_way_length_start,
					v_branch_f_bus, --from old "from-bus" to new closest point
					v_max_bus_id + 2, --the new grid bus
					v_branch_voltage,
					v_branch_cables,
					50,
					v_branch_power,
					v_new_way_geom_start);

			-- End Substring Branch:
			INSERT INTO branch_data (	branch_id, 
							length,
							f_bus,
							t_bus,
							voltage,
							cables,
							frequency,
							power,
							way)
				VALUES(	v_max_branch_id + 2,
					v_new_way_length_end,
					v_max_bus_id + 2, -- from new closest point to old "to-bus"
					v_branch_t_bus,
					v_branch_voltage,
					v_branch_cables,
					50,
					v_branch_power,
					v_new_way_geom_end);

				
			-- New branch (connection) from closest point to transfer bus
			v_new_connection_geom := ST_MakeLine(	v_trans_bus_geom, 
								v_closest_point_geom);
			v_new_connection_length := ST_Length(v_new_connection_geom::geography);
			
			INSERT INTO branch_data (	branch_id, 
							length,
							f_bus,
							t_bus,
							voltage,
							cables,
							frequency,
							power,
							way)
				VALUES(	v_max_branch_id + 3,
					v_new_connection_length,
					v_max_bus_id + 1,
					v_max_bus_id + 2,
					v_branch_voltage,
					3,
					50,
					v_branch_power,
					v_new_connection_geom);
		END IF;
				
		DELETE FROM transfer_busses
			WHERE osm_id = v_trans_bus_id;
	END LOOP;

	UPDATE bus_data 
	SET cnt = (SELECT count (*) 
			FROM branch_data 
			WHERE branch_data.f_bus = bus_data.id OR branch_data.t_bus = bus_data.id);
END IF;

END
$$
LANGUAGE plpgsql;


	-- otg_transfer_busses ()
	
-- This function like it is can later better be used to connect disconnected subgrids
-- It takes the closest substation (unused transfer-bus to grid bus) and connects sequentially.
-- This can easily be changed to be used for disconnected subgrids

-- The transfer-bus connection should be improved in the way described in GitHub.
-- CREATE OR REPLACE FUNCTION otg_transfer_busses () RETURNS void
-- AS $$ 
-- DECLARE
-- 
-- v_cnt INT;
-- v_smallest_dist FLOAT;
-- v_this_dist FLOAT;
-- v_trans_bus_id BIGINT;
-- v_substation_id BIGINT;
-- 
-- v_trans_bus_geom geometry (Point, 4326);
-- v_substation_geom geometry (Point, 4326);
-- v_substation_voltage INT;
-- 
-- v_trans_bus RECORD;
-- v_substation RECORD;
-- 
-- v_max_bus_id BIGINT;
-- v_max_branch_id BIGINT;
-- BEGIN
-- IF (SELECT val_bool 
-- 	FROM abstr_values
-- 	WHERE val_description = 'transfer_busses') -- Only if transfer_busses is selected True (Python Script)
-- 	THEN
-- 
-- 	-- All the substations that are allready found can be ignored
-- 	DELETE FROM transfer_busses
-- 		WHERE osm_id IN (SELECT substation_id FROM bus_data);
-- 
-- 	LOOP
-- 		v_cnt := (SELECT count(*) FROM transfer_busses);
-- 		EXIT WHEN v_cnt = 0;
-- 
-- 		v_smallest_dist := 1000000;
-- 		FOR v_trans_bus IN
-- 			SELECT osm_id, center_geom
-- 				FROM transfer_busses
-- 		LOOP
-- 			FOR v_substation IN
-- 				SELECT id, voltage, the_geom
-- 					FROM bus_data
-- 					WHERE 	frequency = 50 AND
-- 						NOT substation_id IS NULL -- Only substations no grid busses (Muffen)
-- 					ORDER BY voltage -- Will be conected with 110 preferred
-- 			LOOP
-- 				v_this_dist := ST_Distance(	v_trans_bus.center_geom, 
-- 								v_substation.the_geom);
-- 				IF (v_this_dist < v_smallest_dist)
-- 					THEN 
-- 					v_smallest_dist := v_this_dist;
-- 					v_trans_bus_id := v_trans_bus.osm_id;
-- 					v_trans_bus_geom := v_trans_bus.center_geom;
-- 					v_substation_id := v_substation.id;
-- 					v_substation_voltage := v_substation.voltage;
-- 					v_substation_geom := v_substation.the_geom;
-- 				END IF;
-- 				
-- 			END LOOP;
-- 		END LOOP;
-- 
-- 		v_max_bus_id := (SELECT max(id) FROM bus_data);
-- 		INSERT INTO bus_data (	id, 
-- 					cnt, 
-- 					the_geom, 
-- 					voltage, 
-- 					frequency, 
-- 					substation_id, 
-- 					cntr_id)
-- 			VALUES (v_max_bus_id + 1, 
-- 				1,
-- 				v_trans_bus_geom,
-- 				v_substation_voltage,
-- 				50,
-- 				v_trans_bus_id,
-- 				'DE');
-- 				
-- 		v_max_branch_id := (SELECT max(branch_id) FROM branch_data);
-- 		INSERT INTO branch_data (	branch_id, 
-- 						length,
-- 						f_bus,
-- 						t_bus,
-- 						voltage,
-- 						cables,
-- 						frequency,
-- 						power,
-- 						multiline)
-- 			VALUES(	v_max_branch_id + 1,
-- 				v_smallest_dist,
-- 				v_max_bus_id + 1,
-- 				v_substation_id,
-- 				v_substation_voltage,
-- 				3,
-- 				50,
-- 				'cable',
-- 				ST_Multi(ST_MakeLine(	v_trans_bus_geom,
-- 							v_substation_geom)));
-- 		DELETE FROM transfer_busses
-- 			WHERE osm_id = v_trans_bus_id;
-- 	END LOOP;
-- END IF;
-- 
-- END
-- $$
-- LANGUAGE plpgsql;


-- FUNKTIONEN ZUR BERECHNUNG DER LEITUNGS/TRAFO SPEZIFIKATIONEN

	-- CALC_BRANCH_SPECIFICATIONS

-- Berechnet die genauen Leitungsspezifikationen
CREATE OR REPLACE FUNCTION otg_calc_branch_specifications () RETURNS void
AS $$

DECLARE
v_branch RECORD;
v_spec RECORD;
v_Z_base REAL; -- Basiswiderstand für jede Leitung (Abhängig von der Spannung am to- (t_bus) bus
v_R REAL; -- Ohmscher Widerstand der Leitung in Ohm (Eines Leiters im 3-Leitersystem)
v_X REAL; -- Induktiver Blindwiderstand (In Reihe mit R) in Ohm (Eines Leiters im 3-Leitersystem)
v_B REAL; -- Kapazitiver Blindleitwert in 1/Ohm (Eines Leiters im 3-Leitersystem)
v_S_long REAL; -- Langzeit Scheinleistung der Leitung (über alle 3 Leiter des Systems) in VA

v_numb_syst INT; -- Anzahl 3-Leitersysteme
BEGIN
FOR v_branch IN
	SELECT branch_id, spec_id, length, f_bus, t_bus, cables, wires, power FROM branch_data
		WHERE power = 'line' OR power = 'cable'
	LOOP
		SELECT * INTO v_spec FROM branch_specifications WHERE spec_id = v_branch.spec_id;

		-- Die Anzahl der Systeme wird durch die Anzahl der Leiterseile (Cables) bestimmt.
		-- Bei 50 Hz. stellen 3 Leiterseile ein System dar.
		v_numb_syst := round(v_branch.cables::REAL / 3); 
		
		v_Z_base := (SELECT voltage::REAL 
				FROM bus_data 
				WHERE id = v_branch.t_bus)^2 / (SELECT val_int * 10^6 
									FROM abstr_values 
									WHERE val_description = 'base_MVA'); --Basiswiderstand in Ohm

		-- Gesamter Ohmscher Widerstand und Induktiver Widerstand
		-- Da die (mehreren) Systeme identisch sind, können Ohmscher und Induktiver Widerstand
		-- ... durch die Anzhal Systeme geteilt werden
		v_R := (v_branch.length * v_spec.R_Ohm_per_km * 10^(-3)) / v_numb_syst;
		
		v_X := (v_branch.length * 2 * pi() * 50 * v_spec.L_mH_per_km * 10^(-6)) / v_numb_syst;
		
		-- Kapazitiver Blindleitwert kann entsprechend multipliziert werden
		v_B := v_branch.length * 2 * pi() * 50 * v_spec.C_nF_per_km * 10^(-12) * v_numb_syst;

		--Stherm_MVA bezieht sich auf ein gesamtes System (alle 3 Leiter des 3-Leitersystems)
		v_S_long := v_numb_syst * v_spec.Stherm_MVA * (10^6);
		
		UPDATE branch_data
			SET 	br_r = v_R / v_Z_base, -- p.u. Widerstand
				br_x = v_X / v_Z_base, -- p.u. Widerstand
				br_b = v_B / v_Z_base, -- p.u. Widerstand
				S_long = v_S_long
			WHERE  branch_id = v_branch.branch_id;
	END LOOP;
END
$$
LANGUAGE plpgsql;


	--CALC_DCLINE_SPECIFICATIONS ()

-- Berechnet die für Matpower notwendigen Wert für Gleichstrom-leitungen
CREATE OR REPLACE FUNCTION otg_calc_dcline_specifications () RETURNS void
AS $$

DECLARE
v_dcline RECORD;
v_spec RECORD;

v_R REAL; -- Ohmscher Widerstand der Leitung
v_loss1_max REAL; -- Maximaler linearer Verlustfaktor
v_loss1_max_test REAL; -- Maximaler linearer Verlustfaktor
v_pmax REAL; --Maximal von der Leitung aufnehmbare Leistug
v_numb_syst INT; -- Anzahl Systeme
BEGIN
FOR v_dcline IN
	-- Geht alle dc-Leitungen durch
	SELECT branch_id, spec_id, length, voltage, cables FROM dcline_data
	LOOP
	-- Lädt die entsprechenden Spezifikationen in v_spec
	SELECT r_ohm_per_km, i_a_therm INTO v_spec FROM dcline_specifications specs 
		WHERE specs.spec_id = v_dcline.spec_id;

	v_numb_syst := round(v_dcline.cables::REAL / 2);

	-- Maximal von der Leitung aufnehmbare Leistung (abhängig von Spannung und maximaler Strombelastung)
	v_pmax := 2 * v_dcline.voltage * v_spec.i_a_therm;  -- Mal Zwei, da i.d.R bibolare Leitung, bei der voltage +- angegeben wird!

	v_R := (v_spec.r_ohm_per_km / 1000) * v_dcline.length;

	-- Linearer Verlustfaktor ist abhängig von der Stromkstärke. Dies wird in Matpower vernachlässigt
	-- Aus diesem Grund wird der Verlustfaktor für den Fall maximaler Strombelastung angenommen.
	-- l = I*R/U oder l = I^2 * R / P
	v_loss1_max := v_spec.i_a_therm * v_R / (2 * v_dcline.voltage);

	UPDATE dcline_data
		SET 	loss1 = v_loss1_max,
			pmax = v_pmax
		WHERE branch_id = v_dcline.branch_id;

	END LOOP;
END
$$
LANGUAGE plpgsql;

	-- CALC_MAX_NODE_POWER ()

-- Berechnet für jeden Knoten innerhalb eines Umspannwerks die maximal übertragbare Leistunge
-- (Diese wird vereinfachend als Summe der Beträge von Stherm und Pmax berechnet).
CREATE OR REPLACE FUNCTION otg_calc_max_node_power () RETURNS void
AS $$

DECLARE
v_bus RECORD;
v_s_long_sum REAL;
v_s_long_sum_branch REAL;
v_s_long_sum_dcline REAL;

BEGIN
FOR v_bus IN
	SELECT id FROM bus_data WHERE NOT substation_id IS NULL
	LOOP
	v_s_long_sum := 0;
	v_s_long_sum_branch := (SELECT sum (S_long) 
						FROM branch_data 
						WHERE 	(f_bus = v_bus.id OR t_bus = v_bus.id)
							AND (power = 'line' OR power = 'cable'));
	IF NOT v_s_long_sum_branch IS NULL 
		THEN v_s_long_sum := v_s_long_sum + v_s_long_sum_branch; END IF;
		
	v_s_long_sum_dcline := (SELECT sum (pmax)
						FROM dcline_data
						WHERE f_bus = v_bus.id OR t_bus = v_bus.id);
	IF NOT v_s_long_sum_dcline IS NULL 
		THEN v_s_long_sum := v_s_long_sum + v_s_long_sum_dcline; END IF;

	UPDATE bus_data
		SET s_long_sum = v_s_long_sum
		WHERE id = v_bus.id;
		
	END LOOP;
END;
$$ LANGUAGE plpgsql;

	-- CALC_TRANSFORMER_SPECIFICATIONS
	
-- Berechnet die genauen Trafospezifikationen		
CREATE OR REPLACE FUNCTION otg_calc_transformer_specifications () RETURNS void
AS $$

DECLARE
v_branch RECORD;

v_U_OS REAL; -- Oberspannung (Volt)
v_u_kr REAL; -- relative Kurzschlussspannung (%)
v_Z_TOS REAL; -- Transformatorimpedanz (Ohm)
v_X_TOS REAL; -- Blindwiderstand  (Ohm)
v_Srt REAL; --Trafobemessungsleistung (VA)
v_Z_base REAL; -- Basisimpedanz (Ohm)
v_Bl_TOS REAL; -- Blindleitwert (1/Ohm) eines Trafos der angegebenen Spezifikationen
v_Bl_TOS_all REAL; -- Gesamter Blindleitwert der zwischen zwei Knoten parallel geschalteten Transformatoren
v_X_TOS_all REAL; -- Gesamter Blindwiderstand der zwischen zwei Knoten parallel geschalteten Transformatoren

v_S_long_MVA_sum_max REAL; -- Größere der von den beiden Verbindungsknoten zu übertragenden Leistung (Für Bemessung des Transformators)
v_numb_transformers INT; -- Anzahl der einzubauenden Transformatoren pro Knotenpaar

BEGIN 
FOR v_branch IN
	SELECT branch_id, f_bus, t_bus FROM branch_data WHERE power = 'transformer'
	LOOP
		
		

		v_S_long_MVA_sum_max := (10^(-6))*(SELECT max (S_long_sum) 
						FROM bus_data 
						WHERE id = v_branch.f_bus OR id = v_branch.t_bus);
		v_numb_transformers := (SELECT ceil( v_S_long_MVA_sum_max/(SELECT S_MVA FROM transformer_specifications))); -- Wird auf nächste ganze Zahl aufgerundet.

		
		v_U_OS := (SELECT max(voltage) FROM bus_data 
					WHERE 	id = v_branch.f_bus OR 
						id = v_branch.t_bus);
		
		v_Srt := (SELECT S_MVA * 10^6 FROM transformer_specifications);
		v_u_kr := (SELECT u_kr FROM transformer_specifications);
		
		v_Z_TOS := v_u_kr/100 * v_u_OS^2 / v_Srt;
		
		v_X_TOS := v_Z_TOS; -- Kann nach Flosdorff angenommen werden

		v_Bl_TOS := -1/v_X_TOS;

		v_Bl_TOS_all := v_numb_transformers * v_Bl_TOS;

		v_X_TOS_all := -1/v_Bl_TOS_all;
		
		v_Z_base := v_u_OS^2 / (SELECT val_int * 10^6 
						FROM abstr_values 
						WHERE val_description = 'base_MVA'); -- Basiswiderstand in Ohm (Oberspannungsseite)

		UPDATE branch_data
			SET	br_r = 0,
				br_x = v_X_TOS_all / v_Z_base, --(p.u.)
				br_b = 0,
				S_long = (10^6) * v_numb_transformers * (SELECT S_MVA FROM transformer_specifications),
				tap = 1,
				shift = 0,
				numb_transformers = v_numb_transformers
			WHERE branch_id = v_branch.branch_id;

	END LOOP;
END
$$
LANGUAGE plpgsql;
		
			
	
-- PROBLEM_LOG TRIGGER
-- Trigger verschiedener Tabellen, um einen Fehler in problem_log zu schreiben

	-- POWER_LINE_PROBLEM

CREATE OR REPLACE FUNCTION otg_power_line_problem_tg () RETURNS TRIGGER
AS $$
BEGIN



	INSERT INTO problem_log (object_type,
				line_id,
				relation_id,
				way, 
				voltage,
				cables,
				wires, 
				frequency,
				problem)
				
		VALUES ('power_line',
			ARRAY [OLD.id],
			NULL,
			ST_Multi(OLD.way),
			NULL,
			NULL,
			NULL,
			NULL,
			TG_ARGV[0]);

RETURN NULL;
END; $$
LANGUAGE plpgsql;

	-- POWER_LINE_AS_BRANCH_PROBLEM
	
CREATE OR REPLACE FUNCTION otg_power_line_as_branch_problem_tg () RETURNS TRIGGER
AS $$
BEGIN



	INSERT INTO problem_log (object_type,
				line_id,
				relation_id,
				way, 
				voltage,
				cables,
				wires, 
				frequency,
				problem)
				
		VALUES ('power_line_as_branch',
			ARRAY [OLD.line_id],
			0,
			ST_Multi(OLD.way),
			OLD.voltage,
			OLD.cables,
			OLD.wires,
			OLD.frequency,
			TG_ARGV[0]);

RETURN NULL;
END; $$
LANGUAGE plpgsql;

	-- POWER_CIRCUITS_PROBLEM
	
CREATE OR REPLACE FUNCTION otg_power_circuits_problem_tg () RETURNS TRIGGER
AS $$
BEGIN



	INSERT INTO problem_log (object_type,
				line_id,
				relation_id,
				way, 
				voltage,
				cables,
				wires, 
				frequency,
				problem)
				
		VALUES ('circuit',
			OLD.members,
			OLD.id,
			ST_Multi(ST_Union (ARRAY (SELECT way FROM power_line WHERE id = ANY (OLD.members)))),
			OLD.voltage,
			OLD.cables,
			OLD.wires,
			OLD.frequency,
			TG_ARGV[0]);

RETURN NULL;
END; $$
LANGUAGE plpgsql;



-- OTG_PLZ_SUBSTATION () 

-- Function to assign substations to plz
CREATE OR REPLACE FUNCTION otg_plz_substation () RETURNS void
AS $$

DECLARE
v_plz_area RECORD;
v_numb_subst INT;
v_total_plz_power NUMERIC;

BEGIN
-- Creates new table for assignment of substations to plz
DROP TABLE IF EXISTS plz_substation;
CREATE TABLE plz_substation (
	plz INT,
	substation_id INT,
	percentage NUMERIC,
	distance NUMERIC
	);


FOR v_plz_area IN SELECT plz::INT as plz, geom FROM plz_poly
LOOP
	INSERT INTO plz_substation (plz, substation_id)
		SELECT v_plz_area.plz, id
				FROM power_substation
				WHERE 	ST_Within(center_geom, v_plz_area.geom);

	v_numb_subst := (SELECT count(*) FROM plz_substation WHERE plz = v_plz_area.plz);	
			
	IF v_numb_subst = 0
	THEN 
		INSERT INTO plz_substation (	plz, 
						substation_id, 
						distance)
				SELECT 	v_plz_area.plz, 
					id, 
					ST_Distance(ST_Centroid(v_plz_area.geom), center_geom) as dist
					FROM power_substation
					ORDER BY dist ASC
					LIMIT 1;
		RAISE NOTICE 'remote added';							
	END IF;

	v_total_plz_power := (SELECT sum(s_long) 
				FROM power_substation 
				WHERE id = ANY (SELECT substation_id
							FROM plz_substation
							WHERE plz = v_plz_area.plz));
			
	UPDATE plz_substation 
		SET percentage = (((SELECT s_long 
					FROM power_substation
					WHERE id = substation_id) / v_total_plz_power) * 100) 	
		WHERE plz = v_plz_area.plz;

RAISE NOTICE 'done';
END LOOP;

END;
$$ LANGUAGE plpgsql;



-- OTG_NUTS3_SUBSTATION () 

-- Function to assign substations to plz
CREATE OR REPLACE FUNCTION otg_nuts3_substation () RETURNS void
AS $$

DECLARE
v_nuts3_area RECORD;
v_numb_subst INT;
v_total_nuts3_power NUMERIC;

BEGIN
-- Creates new table for assignment of substations to plz
DROP TABLE IF EXISTS nuts3_substation;
CREATE TABLE nuts3_substation (
	nuts_id CHARACTER VARYING (14),
	substation_id INT,
	percentage NUMERIC,
	distance NUMERIC
	);


FOR v_nuts3_area IN SELECT nuts_id, geom 
			FROM nuts_poly
			WHERE 	nuts_id ILIKE '%DE%' AND -- Only Germany
				stat_levl_ = 3 -- Only Nuts3
LOOP
	INSERT INTO nuts3_substation (nuts_id, substation_id)
		SELECT v_nuts3_area.nuts_id, id
				FROM power_substation
				WHERE 	ST_Within(center_geom, v_nuts3_area.geom);

	v_numb_subst := (SELECT count(*) FROM nuts3_substation WHERE nuts_id = v_nuts3_area.nuts_id);	
			
	IF v_numb_subst = 0
	THEN 
		INSERT INTO nuts3_substation (	nuts_id, 
						substation_id, 
						distance)
				SELECT 	v_nuts3_area.nuts_id, 
					id, 
					ST_Distance(ST_Centroid(v_nuts3_area.geom), center_geom) as dist
					FROM power_substation
					ORDER BY dist ASC
					LIMIT 1;
		RAISE NOTICE 'remote added';							
	END IF;

	v_total_nuts3_power := (SELECT sum(s_long) 
				FROM power_substation 
				WHERE id = ANY (SELECT substation_id
							FROM nuts3_substation
							WHERE nuts_id = v_nuts3_area.nuts_id));
			
	UPDATE nuts3_substation 
		SET percentage = (((SELECT s_long 
					FROM power_substation
					WHERE id = substation_id) / v_total_nuts3_power) * 100) 	
		WHERE nuts_id = v_nuts3_area.nuts_id;

RAISE NOTICE 'done';
END LOOP;

END;
$$ LANGUAGE plpgsql;



-----------------------------------------------------------------------------
-- EDITIERUNG (ZUBAU)
-----------------------------------------------------------------------------


-- SET_TIMESTAMP

-- Update der Metadata bei eingefügten / veränderten Objekten	
CREATE OR REPLACE FUNCTION otg_set_timestamp_tg () RETURNS TRIGGER
AS $$
BEGIN
	NEW.tstamp := now ();-- at time zone 'utc';
 	
RETURN NEW;
END; $$
LANGUAGE plpgsql;


-- SET_ID

-- Gibt Objekten beim (manuellen) Einfügen neue ID, falls noch keine vorhanden
CREATE OR REPLACE FUNCTION otg_set_id_tg () RETURNS TRIGGER
AS $$
DECLARE
v_min BIGINT;
BEGIN
	IF NEW.osm_id IS NULL THEN
		SELECT min (change_log.osm_id) INTO v_min FROM change_log;
		IF v_min < 0 THEN 
			NEW.osm_id := v_min - 1; ELSE 
			NEW.osm_id := -1; END IF;
		END IF;
		
RETURN NEW;
END; $$
LANGUAGE plpgsql;

-- SET_ANWENDUNG ()

-- Bei jedem neuen Eintrag in change log wird durch diesen Trigger der aktuell ausgwählte Plan und das Jahr in 
-- anwendung änderung gespeichert.
CREATE OR REPLACE FUNCTION otg_set_anwendung_tg () RETURNS TRIGGER
AS $$
DECLARE
v_numb_plan_ids INT;
v_numb_plan_intern_ids INT;
v_zuordnung RECORD;
BEGIN

-- aktuelle Zuordnung wird in Record gespeichert
SELECT plan_id, jahr, plan_intern_id, description, user_comment INTO v_zuordnung FROM zuordnung;
-- Bestimmt die Anzahl IDs (der Pläne und Planintern)
v_numb_plan_ids := otg_numb_of_cert_char(v_zuordnung.plan_id, ';') + 1;
v_numb_plan_intern_ids := otg_numb_of_cert_char(v_zuordnung.plan_intern_id, ';') + 1;

IF v_numb_plan_ids IS NULL OR v_numb_plan_intern_ids IS NULL
	THEN RAISE EXCEPTION 'IDs wurden falsch eingegeben';
END IF;

IF NOT v_numb_plan_ids = v_numb_plan_ids
	THEN RAISE EXCEPTION 'Die Anzahl Plan-IDs stimmt nicht mit der Anzahl Plan-interner IDs ueberein'; 
END IF;

FOR i IN 1..v_numb_plan_ids
LOOP
	INSERT INTO anwendung_aenderung (
				aenderungs_id,
				plan_id,
				jahr,
				plan_intern_id,
				description,
				user_comment)
		VALUES (
			NEW.id,
			(SELECT (otg_get_int_from_semic_string(v_zuordnung.plan_id, i))),
			v_zuordnung.jahr,
			(SELECT (split_part(v_zuordnung.plan_intern_id,';',i))),
			v_zuordnung.description,
			v_zuordnung.user_comment); -- Plan_intern_id ist TEXT!!
END LOOP;
			
RETURN NULL;
END; $$
LANGUAGE plpgsql;


-- PREVENT_DIRECT_INSERTS_TRIGGER

-- Verhinderung von direkten inserts in change_log
CREATE OR REPLACE FUNCTION otg_prevent_direct_inserts_tg () RETURNS TRIGGER
AS $$
BEGIN
	IF 	NEW.table_ident IS NULL OR 
		NEW.action IS NULL 
		THEN 
			RAISE EXCEPTION 'No direct inserts into table "%"', TG_TABLE_NAME 
				USING HINT = 'Use table power_ways to apply changes';
			RETURN NULL;
		ELSE RETURN NEW; 
	END IF;
END;
$$
LANGUAGE 'plpgsql';



-- READ-ONLY TRIGGER

-- Ermöglicht den Schreibschutz von Tabellen.

CREATE OR REPLACE FUNCTION otg_readonly_tg () RETURNS TRIGGER
AS $$
BEGIN
	RAISE EXCEPTION 'table "%" is read-only', TG_TABLE_NAME; -- USING HINT = 'Use table ... to apply changes';
	RETURN NULL;
END;
$$
LANGUAGE 'plpgsql';	


-- Um für neu erstellte Relations neuen Way zu bekommen (nur für die Visualisierung)
CREATE OR REPLACE FUNCTION otg_get_relation_way(way_ids BIGINT []) 
	RETURNS geometry (MultiLINESTRING, 4326)
AS $$
DECLARE
v_way_ids_length INT;
v_ways geometry(LINESTRING, 4326)[];

BEGIN
v_way_ids_length := array_length(way_ids, 1);
FOR i IN 1..v_way_ids_length
LOOP
	IF way_ids[i] < 0
		-- Falls der referenzierte Way im change_log zu finden ist, dann daher den Way beziehen 
		THEN v_ways[i] := (SELECT ST_Linemerge(way) FROM change_log WHERE osm_id = way_ids[i]);
		-- ... sonst aus der normalen Way-Tabelle
		ELSE 
			v_ways[i] := (SELECT way FROM power_ways WHERE id = way_ids[i]); END IF; 
END LOOP;
RETURN ST_Multi(ST_union (v_ways));

END; $$
LANGUAGE plpgsql;


	-- EDIT_POWER_WAYS 
	-- (Zur Bearbeitung der Leitungen im Rahmen des Zubaus)

		-- EDIT_POWER_WAYS_UPDATE_LOG 

-- Sobald Objekte (manuell) in edit_power_ways geupdatet werden, wird statt das Objekt selbst zu ändern...
-- ...die Änderung im change_log festgehalten
CREATE OR REPLACE FUNCTION otg_edit_power_ways_update_tg () RETURNS TRIGGER
AS $$
DECLARE
BEGIN
	
	INSERT INTO change_log (	osm_id,
					table_ident,
					action,
					way,
					power,
					voltage,
					cables,
					wires,
					circuits,
					frequency)
		VALUES(	NEW.id,
			'way',
			'updt',
			ST_Multi(OLD.way),
			NEW.power,
			NEW.voltage,
			NEW.cables,
			NEW.wires,
			NEW.circuits,
			NEW.frequency);
RETURN NULL;
END; $$
LANGUAGE plpgsql;



		-- POWER_WAYS_EDIT_INSERT
		
-- Sobald neue Objekte in power_ways eingefügt werden, werden... 
-- ...(statt die neuen Objekte in power_ways zu speichern) die Änderung im Change_log festgehalten	

CREATE OR REPLACE FUNCTION otg_power_ways_edit_insert_tg () RETURNS TRIGGER
AS $$
DECLARE
BEGIN
	
	
	INSERT INTO change_log (		osm_id,
						table_ident,
						action,
						way,
						power,
						voltage,
						cables,
						wires,
						circuits,
						frequency)
		VALUES(	NULL,
			'way',
			'isrt',
			ST_Multi(NEW.way),
			NEW.power,
			NEW.voltage,
			NEW.cables,
			NEW.wires,
			NEW.circuits,
			NEW.frequency);
RETURN NULL;
END; $$
LANGUAGE plpgsql;


		

		-- POWER_WAYS_EDIT_DELETE

-- Sobald Objekte von power_ways gelöscht werden, wird die Änderung im Change_log festgehalten		
CREATE OR REPLACE FUNCTION otg_power_ways_edit_delete_tg() RETURNS TRIGGER
AS $$
DECLARE
BEGIN
	
	INSERT INTO change_log (	osm_id,
					table_ident,
					action,
					way,
					power,
					voltage,
					cables,
					wires,
					circuits,
					frequency)
		VALUES(	OLD.id,
			'way',
			'dlt',
			ST_Multi(OLD.way),
			OLD.power,
			OLD.voltage,
			OLD.cables,
			OLD.wires,
			OLD.circuits,
			OLD.frequency);
RETURN NULL;
END; $$
LANGUAGE plpgsql;




	-- POWER_RELATIONS
	-- (Funktionen für die Bearbeitung der Tabelle power_relations (für den Zubau)


		-- POWER_RELATIONS_EDIT_UPDATE

-- Werden Relations aus der Tabelle power_relations geupdatet, wird die Änderung festgehalten
CREATE OR REPLACE FUNCTION otg_power_relations_edit_update_tg () RETURNS TRIGGER
AS $$
DECLARE
BEGIN
	
	INSERT INTO change_log (	osm_id,
					table_ident,
					action,
					members,
					way,
					voltage,
					cables,
					wires,
					circuits,
					frequency)
		VALUES(	NEW.id,
			'rel',
			'updt',
			NEW.members,
			ST_Multi(ST_union (ARRAY (SELECT way FROM power_ways WHERE id = ANY (NEW.members)))),
			NEW.voltage,
			NEW.cables,
			NEW.wires,
			NEW.circuits,
			NEW.frequency);
RETURN NULL;
END; $$
LANGUAGE plpgsql;


		-- POWER_RELATIONS_EDIT_DELETE

-- Werden Relations aus der Tabelle power_relations gelöscht, wird die Änderung festgehalten
CREATE OR REPLACE FUNCTION otg_power_relations_edit_delete_tg () RETURNS TRIGGER
AS $$
DECLARE
BEGIN
	
	INSERT INTO change_log (		osm_id,
						table_ident,
						action,
						members,
						way,
						voltage,
						cables,
						wires,
						circuits,
						frequency)
		VALUES(	OLD.id,
			'rel',
			'dlt',
			OLD.members,
			ST_Multi(ST_union (ARRAY (SELECT way FROM power_ways WHERE id = ANY (OLD.members)))),
			OLD.voltage,
			OLD.cables,
			OLD.wires,
			OLD.circuits,
			OLD.frequency);
RETURN NULL;
END; $$
LANGUAGE plpgsql;



		-- POWER_RELATIONS_EDIT_INSERT

-- Werden neue Objekte (Relations) eingefügt, wird die Änderung im change_log gespeichert
CREATE OR REPLACE FUNCTION otg_power_relations_edit_insert_tg () RETURNS TRIGGER
AS $$
DECLARE
BEGIN
	
	INSERT INTO change_log (		osm_id,
						table_ident,
						action,
						members,
						way,
						voltage,
						cables,
						wires,
						circuits,
						frequency)
		VALUES(	NEW.id,
			'rel',
			'isrt',
			NEW.members,
			ST_Multi(otg_get_relation_way(NEW.members)),
			NEW.voltage,
			NEW.cables,
			NEW.wires,
			NEW.circuits,
			NEW.frequency);
RETURN NULL;
END; $$
LANGUAGE plpgsql;


		-- CHANGE-LOG EDIT Direct DELETE

-- Wird im vw_change_log ein Eintrag gelöscht, so wird dieser auch aus change_log gelöscht
CREATE OR REPLACE FUNCTION otg_vw_change_log_edit_delete_tg () RETURNS TRIGGER
AS $$
DECLARE
BEGIN
	DELETE FROM change_log 
		WHERE id = OLD.id;
RETURN NULL;	
END; $$
LANGUAGE plpgsql;

		-- CHANGE-LOG EDIT DIRECT UPDATE

-- Wird im vw_change_log ein Eintrag (direkt) geupdated, so wird dieser auch in change_log geupdated
CREATE OR REPLACE FUNCTION otg_vw_change_log_edit_update_tg () RETURNS TRIGGER
AS $$
DECLARE
BEGIN
	-- Nur einige, bestimmte Werte können geändert werden.
	UPDATE change_log
		SET 	members = NEW.members,
			power = NEW.power,
			voltage = NEW.voltage,
			cables = NEW.cables,
			wires = NEW.wires,
			circuits = NEW.circuits,
			frequency = NEW.frequency,
			hinweis = NEW.hinweis
		WHERE id = NEW.id;
			
RETURN NULL;	
END; $$
LANGUAGE plpgsql;




------------------------------------------------------------------------------------------------
-- UPDATE
-- (Funktionen für Anwendung von OSM-Updates)
------------------------------------------------------------------------------------------------

	-- CREATE_POWER_TABLES

CREATE OR REPLACE FUNCTION otg_create_power_tables () RETURNS void
AS $$
BEGIN

	DROP TABLE IF EXISTS edit_power_relations;
	DROP TABLE IF EXISTS power_relation_members;
	DROP TABLE IF EXISTS power_relations;
	
	DROP TABLE IF EXISTS power_ways;
	DROP TABLE IF EXISTS power_way_nodes;
	
	-- ways

	-- import der relevanten ways
	CREATE TABLE power_ways AS 
		SELECT * FROM ways
		WHERE exist (tags, 'power'); -- Nur die mit power=* getagten Ways sind interessant
	ALTER TABLE power_ways
		ADD CONSTRAINT way_id_pk primary key (id); 
	CREATE INDEX way_id_idx ON power_ways(id);

	CREATE TABLE power_way_nodes AS
		SELECT way_nodes.*
		FROM way_nodes, power_ways
		WHERE way_nodes.way_id = power_ways.id; -- Nur die in power_ways auftauchenden weg_ids werden behalten

		
	-- geometrie der ways
	ALTER TABLE power_way_nodes ADD COLUMN geom geometry(Point);
	UPDATE power_way_nodes --power_way_nodes bekommt eigenen Geometrie, statt Verweis auf Punkte.
		SET geom = nodes.geom
		FROM nodes -- Aus der Nodes Tabelle (nicht power_nodes)
		WHERE nodes.id = power_way_nodes.node_id;

	ALTER TABLE power_ways ADD COLUMN geom geometry(LINESTRING, 4326); -- evlt. mit oben zusammenfassen (und power_way_nodes überspringen)
	UPDATE power_ways
		SET geom = new_way.way
		FROM (	select way_id, st_MakeLine (power_way_nodes.geom ORDER BY sequence_id) as way FROM power_way_nodes --st_makeline ist aggregierte Funktion
			group by way_id) as new_way	
		WHERE new_way.way_id = power_ways.id; 

			
	DROP TABLE power_way_nodes; -- Da Geometrie übernommen wurde, wird diese Tabelle nicht mehr gebraucht
	ALTER TABLE power_ways DROP COLUMN nodes;
	ALTER TABLE power_ways RENAME COLUMN geom TO way;

	-- wichtige hstore-Einträge werden zu (bearbeitbaren) Spalten umgewandelt
	ALTER TABLE power_ways ADD COLUMN power TEXT;
	ALTER TABLE power_ways ADD COLUMN voltage TEXT;
	ALTER TABLE power_ways ADD COLUMN cables TEXT;
	ALTER TABLE power_ways ADD COLUMN wires TEXT;
	ALTER TABLE power_ways ADD COLUMN circuits TEXT;
	ALTER TABLE power_ways ADD COLUMN frequency TEXT;
	ALTER TABLE power_ways ADD COLUMN name TEXT;
	UPDATE power_ways
		SET 	power = (tags -> 'power'),
			voltage = (tags -> 'voltage'),
			cables = (tags -> 'cables'),
			wires = (tags -> 'wires'),
			circuits = (tags -> 'circuits'),
			frequency = (tags -> 'frequency'),
			name = (tags -> 'name');
	ALTER TABLE power_ways DROP COLUMN tags;


	--relations

	CREATE TABLE power_relations
		AS SELECT * FROM relations
		WHERE (tags -> 'route') = 'power'; -- Nur Relationen mit route = Power sind interessant
	ALTER TABLE power_relations
		ADD CONSTRAINT relation_id_pk primary key (id); 
	CREATE INDEX relation_id_idx ON power_relations(id);

	CREATE TABLE power_relation_members AS SELECT * FROM relation_members, power_relations
		WHERE 	relation_members.relation_id = power_relations.id
			AND relation_members.member_type = 'W'; -- Nur die in power_relations auftauchenden Members werden behalten
			--nur Ways (sonst können sich Stromkreise selber auswählen!!!)

	ALTER TABLE power_relations ADD COLUMN voltage TEXT;
	ALTER TABLE power_relations ADD COLUMN cables TEXT;
	ALTER TABLE power_relations ADD COLUMN wires TEXT;
	ALTER TABLE power_relations ADD COLUMN circuits TEXT;
	ALTER TABLE power_relations ADD COLUMN frequency TEXT;
	UPDATE power_relations
		SET 	voltage = 	tags -> 'voltage',
			cables = 	tags -> 'cables',
			wires = 	tags -> 'wires',
			circuits = 	tags -> 'circuits',
			frequency = 	tags -> 'frequency';
	ALTER TABLE power_relations DROP COLUMN tags;

	-- Relations werden entnormalisiert
	ALTER TABLE power_relations ADD COLUMN members BIGINT [];

	UPDATE power_relations 
		SET members = 	ARRAY (	SELECT member_id 
					FROM power_relation_members mem
					WHERE mem.relation_id = power_relations.id);
	DROP TABLE power_relation_members;
	-- Müssen gelöscht werden, da oben nur nach W gefiltert wurde. Manche Rels enthalten jedoch rels
	-- Diese werden so gelöscht. Stromkreise könnten sich sonst selber enthalten.
	DELETE FROM power_relations WHERE array_length (members,1) IS NULL;

		-- neue Tabelle edit_power_relations
	CREATE TABLE edit_power_relations AS 
		SELECT 	id,
			voltage,
			cables,
			wires,
			circuits,
			frequency,
			members,
			ST_union (ARRAY (SELECT way FROM power_ways WHERE id = ANY (members))) --as way 
				--FROM power_relation_members mem 
				--WHERE mem.relation_id = ANY (rels.members)))
		FROM power_relations rels;

	-- Improves Geometry-Column
	ALTER TABLE edit_power_relations
		ALTER COLUMN st_union TYPE geometry(MULTILINESTRING, 4326) USING ST_Multi(st_union);

	ALTER TABLE edit_power_relations
		ADD CONSTRAINT edit_relation_id_pk primary key (id);
			 
	-- Quasi Sperrung der Tabelle power_relations
	CREATE TRIGGER power_relations_otg_readonly_tg 
		BEFORE INSERT OR UPDATE OR DELETE OR TRUNCATE ON power_relations
		FOR EACH STATEMENT
		EXECUTE PROCEDURE otg_readonly_tg ();

-- Trigger
	
	-- edit_power_ways Trigger 
	-- (zum Einfügen, Updaten und Löschen von Leitungen)

-- Trigger returnen NULL und verhindern dadurch, dass Änderungen an der tatsächlichen Tabelle power_ways durchgeführt werden
CREATE TRIGGER power_ways_update
	BEFORE UPDATE ON power_ways
	FOR EACH ROW
	EXECUTE PROCEDURE otg_edit_power_ways_update_tg ();

CREATE TRIGGER otg_power_ways_edit_insert_tg
	BEFORE INSERT ON power_ways
	FOR EACH ROW
	EXECUTE PROCEDURE otg_power_ways_edit_insert_tg ();

CREATE TRIGGER otg_power_ways_edit_delete_tg
	BEFORE DELETE ON power_ways
	FOR EACH ROW
	EXECUTE PROCEDURE otg_power_ways_edit_delete_tg ();


	-- edit_power_relations Trigger 
	-- (zum Einfügen, Updaten und Löschen von Stromkreisen)

-- These trigger-procedures all return NULL in order make sure nothing is applied to edit_power_relation itself
CREATE TRIGGER otg_power_relations_edit_update_tg
	BEFORE UPDATE ON edit_power_relations
	FOR EACH ROW 
	EXECUTE PROCEDURE otg_power_relations_edit_update_tg ();
	
CREATE TRIGGER otg_power_relations_edit_delete_tg
	BEFORE DELETE ON edit_power_relations
	FOR EACH ROW 
	EXECUTE PROCEDURE otg_power_relations_edit_delete_tg ();

CREATE TRIGGER otg_power_relations_edit_insert_tg
	BEFORE INSERT ON edit_power_relations
	FOR EACH ROW 
	EXECUTE PROCEDURE otg_power_relations_edit_insert_tg ();


END; 
$$
LANGUAGE plpgsql;


	-- APPLY_CHANGES()

-- Wendet die Änderungen auf die Tabelle power_ways an. (Wird bei jedem CREATE OR REPLACE von power_ways durchgeführt!
CREATE OR REPLACE FUNCTION otg_apply_changes(v_plan_ids TEXT, v_jahr INT) RETURNS void
AS $$
DECLARE 

v_change RECORD;
v_plan_ids_array INT[];
v_numb_plan_ids INT; --Anzahl angegebener Pläne

BEGIN

-- Erstellt neue Tabelle in der alle Datan nach Zubau vorliegen
DROP TABLE IF EXISTS power_ways_applied_changes;
CREATE TABLE power_ways_applied_changes AS SELECT * FROM power_ways;

DROP TABLE IF EXISTS power_relations_applied_changes;
CREATE TABLE power_relations_applied_changes AS SELECT * FROM power_relations;

-- Falls plan_id NULL oder 0 eingegeben wird, werden nur Tabellen kopiert, aber nicht bearbeitet
IF v_plan_ids = '0' OR v_plan_ids IS NULL 
	THEN RETURN; END IF;

-- TEXT Datentyp v_plan_ids wird ausgewertet und in Array umgewandelt
v_numb_plan_ids := otg_numb_of_cert_char(v_plan_ids, ';') + 1;
FOR i IN 1..v_numb_plan_ids
LOOP
	v_plan_ids_array [i] := (SELECT (otg_get_int_from_semic_string(v_plan_ids, i)));
	IF NOT v_plan_ids_array [i] IN (SELECT id FROM entwicklungsplan) 
		THEN RAISE EXCEPTION 'Plan ID % not in Plan-Table!', v_plan_ids_array [i]; END IF;
END LOOP;

-- Schleift durch alle Zeilen des change_log, die in anwendung_aenderung
-- (unter v_plan_id) aufgeführt sind und deren Anwendungsdatum vor dem in vJahre angegebenen Jahr liegt)
FOR v_change IN
	SELECT 	DISTINCT ON (change_log.id) osm_id, change_log.tstamp, table_ident, action,
		members, way, power, voltage, cables, wires, circuits, frequency, 
		hinweis, plan_id, jahr 
		
		FROM change_log, anwendung_aenderung
		WHERE change_log.id = aenderungs_id AND
			plan_id = ANY (v_plan_ids_array) AND
			jahr <= v_jahr
	ORDER BY change_log.id ASC, tstamp ASC

	LOOP

	-- Falls die Change-Zeile ein Way ist:
	CASE 
		WHEN v_change.action = 'isrt' AND v_change.table_ident = 'way'-- hat negative ID und kann in power_ways nicht auftauchen (es muss also kein Abgleich gemacht werden)
		THEN 

		INSERT INTO power_ways_applied_changes (	id,
								tstamp,
								changeset_id,
								way,
								power,
								voltage,
								cables,
								wires,
								circuits,
								frequency)
			VALUES(	v_change.osm_id,
				v_change.tstamp,
				-1,
				ST_LineMerge(v_change.way),
				v_change.power,
				v_change.voltage,
				v_change.cables,
				v_change.wires,
				v_change.circuits,
				v_change.frequency);

		-- Wenn eine Leitung nach Plan gelöscht werden soll
		WHEN v_change.action = 'dlt' AND v_change.table_ident = 'way'
		THEN 
		-- Wenn die osm_id aus dem Change_log nicht in power_ways vorhanden ist wird ein Fehler gemeldet.
		-- In diesem Fall ist die Leitung in OSM evtl. gelöscht worden. Zubau muss dann neu angepasst werden.
			IF NOT v_change.osm_id IN (SELECT id FROM power_ways_applied_changes) THEN
				RAISE EXCEPTION 'ID % nicht in power_ways zu finden. ', v_change.osm_id
					USING HINT = 'Möglicherweise wurde Leitung in OSM ersetzt'; END IF;

			DELETE FROM power_ways_applied_changes WHERE id = v_change.osm_id; 

		-- Wenn eine Leitung geupdatet werden soll
		WHEN v_change.action = 'updt' AND v_change.table_ident = 'way'
		THEN 
			IF NOT v_change.osm_id IN (SELECT id FROM power_ways_applied_changes) THEN
				RAISE EXCEPTION 'ID % nicht in power_ways zu finden. ', v_change.osm_id
					USING HINT = 'Möglicherweise wurde Leitung in OSM ersetzt'; END IF;

			UPDATE power_ways_applied_changes
				SET 	
					tstamp = v_change.tstamp,
					changeset_id = -1,
					version = NULL,
					user_id = NULL,
					way = ST_LineMerge(v_change.way),
					power = v_change.power,
					voltage = v_change.voltage,
					cables = v_change.cables,
					wires = v_change.wires,
					circuits = v_change.circuits,
					frequency = v_change.frequency
				WHERE power_ways_applied_changes.id = v_change.osm_id; 


		WHEN v_change.action = 'isrt' AND v_change.table_ident = 'rel'
		THEN INSERT INTO power_relations_applied_changes (id,
						tstamp,
						changeset_id,
						members,
						voltage,
						cables,
						wires,
						circuits,
						frequency)
			VALUES(	v_change.osm_id,
				v_change.tstamp,
				-1,
				v_change.members,
				v_change.voltage,
				v_change.cables,
				v_change.wires,
				v_change.circuits,
				v_change.frequency);
				
		WHEN v_change.action = 'dlt' AND v_change.table_ident = 'rel'
			THEN
			IF NOT v_change.osm_id IN (SELECT id FROM power_relations_applied_changes) THEN
				RAISE EXCEPTION 'ID % nicht in power_ways zu finden. ', v_change.osm_id
					USING HINT = 'Möglicherweise wurde Stromkreis in OSM ersetzt'; END IF;
					
			DELETE FROM power_relations_applied_changes WHERE id = v_change.osm_id; -- user-Delete geht also unabhängig vom Timestamp immer vor!

		WHEN v_change.action = 'updt' AND v_change.table_ident = 'rel'
		THEN 

			IF NOT v_change.osm_id IN (SELECT id FROM power_relations_applied_changes) THEN
				RAISE EXCEPTION 'ID % nicht in power_ways zu finden. ', v_change.osm_id
					USING HINT = 'Möglicherweise wurde Stromkreis in OSM ersetzt'; END IF;
					
		
			UPDATE power_relations_applied_changes
				SET 	version = NULL,
					user_id = NULL,
					tstamp = v_change.tstamp,
					changeset_id = -1,
					members = v_change.members,
					voltage = v_change.voltage,
					cables = v_change.cables,
					wires = v_change.wires,
					circuits = v_change.circuits,
					frequency = v_change.frequency
				WHERE power_relations_applied_changes.id = v_change.osm_id; 
		
	END CASE;
	END LOOP;
END; 
$$
LANGUAGE plpgsql;



	-- OTG_ZUORDUNG_AS_ARRAY () 
	-- Returnt aus den Plänen des Zubaus (TEXT) ein Integer-Array
	
CREATE OR REPLACE FUNCTION otg_zuordung_as_array (v_plan_ids TEXT) RETURNS INT[]
AS $$

DECLARE
v_numb_plan_ids INT;
v_plans INT [];

BEGIN
-- NULL output with NULL input
IF v_plan_ids IS NULL
	THEN RETURN NULL;
END IF;

-- Bestimmt die Anzahl IDs (der Pläne und Planintern)
v_numb_plan_ids := otg_numb_of_cert_char(v_plan_ids, ';') + 1;

FOR i IN 1..v_numb_plan_ids
LOOP
	v_plans[i] := (SELECT (otg_get_int_from_semic_string(v_plan_ids, i)));
END LOOP;
RETURN v_plans;
END; 
$$
LANGUAGE plpgsql;

		-- OTG_SAVE_RESULTS () 
		-- Saves results and deletes tables

CREATE OR REPLACE FUNCTION otg_save_results (v_plans TEXT, v_year INT, v_comment TEXT) RETURNS void 
AS $$
DECLARE

v_downloaded DATE;
v_abstracted DATE;
v_new_id INT;

BEGIN

v_downLoaded := (SELECT downloaded FROM osm_metadata);
v_abstracted := current_date;

v_new_id := (SELECT max(id) + 1 FROM results.results_metadata);
IF v_new_id IS NULL 
	THEN v_new_id := 1; END IF;

INSERT INTO results.results_metadata(id, osm_date, abstraction_date, applied_plans, applied_year, user_comment) 
	VALUES (v_new_id, v_downloaded, v_abstracted, v_plans, v_year, v_comment);


INSERT INTO results.bus_data (
	result_id, 
	bus_i, 
	bus_type, 
	pd, 
	qd, 
	bus_area, 
	vm, 
	va, 
	base_kv, 
	zone, 
	osm_substation_id, 
	cntr_id, 
	frequency,
	geom, 
	osm_name)
       
	SELECT   	v_new_id,
			id as bus_i,            --bus number
			bus_type as bus_type,   --bus type (1 = PQ, 2 = PV, 3 = ref, 4 = isolated)
			pd as pd,               --real power demand (MW)
			qd as qd,               --reactive power demand (MVAr)
			bus_area as bus_area,   --area number (positive integer)
			vm as vm,               --voltage magnitude (p.u.)
			va as va,               --voltage angle (degrees)
			voltage::NUMERIC/1000 as base_kv,   --base voltage (kV) (des jeweiligen Knotens (hieruber wird auch Trafoubersetzung bestimmt))
			zone as zone,           --loss zone (positive integer)
			substation_id as osm_substation_id, -- OSM-Substation ID
			cntr_id as cntr_id,     -- Country ID
			frequency,
			the_geom as geom,        -- Point Geometry (Not simplified) WGS84
			(SELECT name FROM power_substation WHERE power_substation.id = substation_id LIMIT 1) as osm_name
				FROM bus_data;            

 INSERT INTO results.branch_data(
	result_id,
	branch_id,
	f_bus,
	t_bus,
	br_r,
	br_x,
	br_b,
	rate_a,
	tap,
	shift,
	br_status,
	link_type,
	branch_voltage,
	cables,
	frequency,
	geom,
	topo)

	SELECT   	v_new_id,
			branch_id,
			f_bus as f_bus,         --from bus number
			t_bus as t_bus,         --to bus number
			br_r as br_r,           --resistance (p.u.)
			br_x as br_x,           --reactance (p.u.)
			br_b as br_b,           --total line charging susceptance (p.u.)
                       (s_long/(10^6))::INT as rate_a, --MVA rating A (long term rating) (optional)
                                   --MVA rating C (emergency rating) (optional)
			tap as tap,	            --transformer off nominal turns ratio, (taps at from bus)
                                                    --(impedance at to bus), i.e. if r = x = 0, tap = ...
			shift as shift,	        --transformer phase shift angle (degrees), positive ) delay
			1 as br_status,         --initial branch status, 1 = in-service, 0 = out-of-service

                            ---------extra information---------

			power as link_type,     -- Transformer, Line, Cable...
			voltage,
			cables,
			frequency,
			multiline as geom,       -- Line Geometry (Not simplified) WGS84
			ST_MakeLine(
			(SELECT the_geom FROM bus_data 	
					WHERE id = f_bus),
			(SELECT the_geom FROM bus_data 	
					WHERE id = t_bus)) -- Topo
					
				FROM branch_data;
 

INSERT INTO results.dcline_data(
	result_id,
	dcline_id,
	f_bus,
	t_bus,
	br_status,
	vf,
	vt,
	pmax,
	loss0,
	loss1,
	link_type,
	branch_voltage,
	cables,
	frequency,
	geom,
	topo)
	
	SELECT   	v_new_id,
			branch_id,
			f_bus as f_bus,
			t_bus as t_bus,
			1 as br_status,
                   
			1 as vf,
			1 as vt,
                           
			pmax / (10^6) as pmax,
                         
			0 as loss0,
			loss1,

                            ---------extra information---------

			power as link_type,     -- Transformer, Line, Cable...
			voltage,
			cables,
			frequency,
			multiline as geom,       -- Line Geometry (Not simplified) WGS84
			ST_MakeLine(
			(SELECT the_geom FROM bus_data 	
					WHERE id = f_bus),
			(SELECT the_geom FROM bus_data 	
					WHERE id = t_bus)) -- Topo

				FROM dcline_data;

DROP TABLE bus_data;
DROP TABLE branch_data; 
DROP TABLE dcline_data;  

INSERT INTO results.nuts3_subst (
	result_id,
	nuts_id,
	substation_id,
	percentage,
	distance)
	
	SELECT	v_new_id,
		nuts_id,
		substation_id,
		percentage,
		distance
		FROM nuts3_substation;
DROP TABLE nuts3_substation;  


INSERT INTO results.plz_subst (
	result_id,
	plz,
	substation_id,
	percentage,
	distance)
	
	SELECT	v_new_id,
		plz,
		substation_id,
		percentage,
		distance
		FROM plz_substation;
DROP TABLE plz_substation;  
	
INSERT INTO results.substations(
	result_id ,
	osm_id,
	voltage,
	s_long,
	name,
	geom,
	center_geom)

	SELECT 	v_new_id,
		id,
		voltage,
		s_long,
		name,
		poly,
		center_geom
			FROM power_substation;
DROP TABLE power_substation;  


INSERT INTO results.problem_log(
	result_id,
	object_type, -- Objekt-Typ des dargestellten Elements
	line_id, -- Alle im Objekt enthaltenen lines (ways)
	relation_id, -- Relation_id des Objekts (0 für Branches, die aus ways stammen)
	way, 
	voltage,
	cables,
	wires, 
	frequency,
	problem ) -- Beschreibung des entsprechenden Problems

	SELECT v_new_id,
		object_type,
		line_id,
		relation_id,
		way,
		voltage,
		cables,
		wires,
		frequency,
		problem
			FROM problem_log;
DROP TABLE problem_log;         
END;
$$
LANGUAGE plpgsql;

-- OTG_split_table () Teilt eine Tabelle v_table in 10 Einzeltabellen auf. Dabei ist die in v_parameter spezifizierte Spalte das Unterscheidungsmerkmal. Die Ursprüngliche Tabelle wird nach der Aufteilung gelöscht.

CREATE OR REPLACE FUNCTION otg_split_table (v_table TEXT, v_parameter TEXT) RETURNS void
AS $$

DECLARE
number_of_rows INT;
part_end_1 INT;
part_end_2 INT;
part_end_3 INT;
part_end_4 INT;
part_end_5 INT;
part_end_6 INT;
part_end_7 INT;
part_end_8 INT;
part_end_9 INT;

BEGIN

-- Eine Hilfstabelle, in welcher die Rheinfolge der 10 Einzeltabellen bestimmt wird wird erstellt.
EXECUTE 'CREATE TABLE table_order AS
SELECT DISTINCT ' || v_parameter || ' FROM ' || v_table ||'
ORDER BY ' || v_parameter;
ALTER TABLE table_order ADD COLUMN indx serial NOT NULL PRIMARY KEY;

number_of_rows := (SELECT COUNT (*)
FROM table_order);

part_end_1 := (SELECT indx FROM table_order WHERE (SELECT FLOOR (number_of_rows/10)) = indx);
EXECUTE 'CREATE TABLE split_table_1 AS
SELECT *
FROM '|| v_table ||'
WHERE '|| v_parameter ||' <= (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_1 ||')
ORDER BY '|| v_parameter;

part_end_2 := (SELECT indx FROM table_order WHERE (SELECT FLOOR (2*number_of_rows/10)) = indx);
EXECUTE 'CREATE TABLE split_table_2 AS
SELECT *
FROM '|| v_table ||'
WHERE '|| v_parameter ||' > (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_1 ||') AND '|| v_parameter ||' <= (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_2 ||')
ORDER BY '|| v_parameter;

part_end_3 := (SELECT indx FROM table_order WHERE (SELECT FLOOR (3*number_of_rows/10)) = indx);
EXECUTE 'CREATE TABLE split_table_3 AS
SELECT *
FROM '|| v_table ||'
WHERE '|| v_parameter ||' > (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_2 ||') AND '|| v_parameter ||' <= (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_3 ||')
ORDER BY '|| v_parameter;

part_end_4 := (SELECT indx FROM table_order WHERE (SELECT FLOOR (4*number_of_rows/10)) = indx);
EXECUTE 'CREATE TABLE split_table_4 AS
SELECT *
FROM '|| v_table ||'
WHERE '|| v_parameter ||' > (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_3 ||') AND '|| v_parameter ||' <= (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_4 ||')
ORDER BY '|| v_parameter;

part_end_5 := (SELECT indx FROM table_order WHERE (SELECT FLOOR (5*number_of_rows/10)) = indx);
EXECUTE 'CREATE TABLE split_table_5 AS
SELECT *
FROM '|| v_table ||'
WHERE '|| v_parameter ||' > (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_4 ||') AND '|| v_parameter ||' <= (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_5 ||')
ORDER BY '|| v_parameter;

part_end_6 := (SELECT indx FROM table_order WHERE (SELECT FLOOR (6*number_of_rows/10)) = indx);
EXECUTE 'CREATE TABLE split_table_6 AS
SELECT *
FROM '|| v_table ||'
WHERE '|| v_parameter ||' > (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_5 ||') AND '|| v_parameter ||' <= (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_6 ||')
ORDER BY '|| v_parameter;

part_end_7 := (SELECT indx FROM table_order WHERE (SELECT FLOOR (7*number_of_rows/10)) = indx);
EXECUTE 'CREATE TABLE split_table_7 AS
SELECT *
FROM '|| v_table ||'
WHERE '|| v_parameter ||' > (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_6 ||') AND '|| v_parameter ||' <= (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_7 ||')
ORDER BY '|| v_parameter;

part_end_8 := (SELECT indx FROM table_order WHERE (SELECT FLOOR (8*number_of_rows/10)) = indx);
EXECUTE 'CREATE TABLE split_table_8 AS
SELECT *
FROM '|| v_table ||'
WHERE '|| v_parameter ||' > (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_7 ||') AND '|| v_parameter ||' <= (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_8 ||')
ORDER BY '|| v_parameter;

part_end_9 := (SELECT indx FROM table_order WHERE (SELECT FLOOR (9*number_of_rows/10)) = indx);
EXECUTE 'CREATE TABLE split_table_9 AS
SELECT *
FROM '|| v_table ||'
WHERE '|| v_parameter ||' > (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_8 ||') AND '|| v_parameter ||' <= (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_9 ||')
ORDER BY '|| v_parameter;

EXECUTE 'CREATE TABLE split_table_10 AS
SELECT *
FROM '|| v_table ||'
WHERE '|| v_parameter ||' > (SELECT '|| v_parameter ||' FROM table_order WHERE indx = '|| part_end_9 ||')
ORDER BY '|| v_parameter;

DROP TABLE table_order;
-- Löschung der Ursprünglichen Tabelle um Doppelungen zu vermeiden.
EXECUTE 'DROP TABLE '|| v_table;

END
$$
LANGUAGE plpgsql;
