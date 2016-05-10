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

--------------------------------------------------------------------------------------------
-- ZUBAU-DATENBANK
--------------------------------------------------------------------------------------------

DROP VIEW IF EXISTS vw_change_log;
	-- Erstellung der LOG-Tabelle
--DROP TABLE change_log

CREATE TABLE IF NOT EXISTS change_log (	

				id SERIAL NOT NULL PRIMARY KEY,
				-- Verwendung wie OSM-id
				osm_id BIGINT,

				-- Change-Parameter
				tstamp TIMESTAMP WITHOUT TIME ZONE,
				table_ident CHARACTER VARYING (3),
				action CHARACTER VARYING (4),

				-- Leitungsinformationen
				members BIGINT [],
				way GEOMETRY (MultiLineString, 4326), --(MultiLineString),
				power TEXT,
				voltage TEXT,
				cables TEXT,
				wires TEXT,
				circuits TEXT,
				frequency TEXT,
				
				hinweis TEXT);


				
	-- Change-Log-Trigger	
	
		-- Metadaten

-- Trigger für direkten Metadata-Update (BEFORE)
-- Timestamp wird bei jedem Update eines Change-Log Objektes vergebe
DROP TRIGGER IF EXISTS otg_set_timestamp_tg ON change_log;
CREATE TRIGGER otg_set_timestamp_tg
	BEFORE INSERT OR UPDATE ON change_log
	FOR EACH ROW EXECUTE PROCEDURE otg_set_timestamp_tg ();

-- Trigger der untersucht, ob eine Objekt (osm) id vorhanden ist. Wenn nicht wird eine negative ID erstellt
DROP TRIGGER IF EXISTS otg_set_id_tg ON change_log;
CREATE TRIGGER otg_set_id_tg
	BEFORE INSERT ON change_log
	FOR EACH ROW EXECUTE PROCEDURE otg_set_id_tg ();

-- Bei jedem neuen Eintrag in change log wird durch diesen Trigger der aktuell ausgwählte Plan und das Jahr in 
-- anwendung änderung gespeichert.	
DROP TRIGGER IF EXISTS otg_set_anwendung_tg ON change_log;
CREATE TRIGGER otg_set_anwendung_tg
	AFTER INSERT ON change_log
	FOR EACH ROW EXECUTE PROCEDURE otg_set_anwendung_tg ();
	
		-- Lock-Trigger

-- Direkte Inserts in Change_log sollen verhindert werden.
-- Auf diese Weise muss man sich keine Gedanken über table_ident etc. machen.
DROP TRIGGER IF EXISTS otg_prevent_direct_inserts_tg ON change_log;
CREATE TRIGGER otg_prevent_direct_inserts_tg 
	BEFORE INSERT ON change_log
	FOR EACH ROW 
	EXECUTE PROCEDURE otg_prevent_direct_inserts_tg ();



-- Tabelle für die Speicherung der Entwicklungspläne und Gesetze
CREATE TABLE IF NOT EXISTS entwicklungsplan (
	id SERIAL NOT NULL PRIMARY KEY,
	plan TEXT,
	comment TEXT);


-- Tabelle zur Zuordnung der Änderungen zu den Entwicklungsplänen und Gesetzen
-- Wird die zugeordnete Änderung gelöscht, wird auch die Anwendung gelöscht.

--DROP TABLE anwendung_aenderung
CREATE TABLE IF NOT EXISTS anwendung_aenderung(
	id SERIAL NOT NULL PRIMARY KEY,
	aenderungs_id INT,
	plan_id INT,
	jahr INT,
	plan_intern_id TEXT,
	description TEXT,
	user_comment TEXT,
	tstamp TIMESTAMP WITHOUT TIME ZONE,
	copied BOOLEAN,
	copied_from INT);
	
DROP TRIGGER IF EXISTS otg_set_timestamp_tg ON anwendung_aenderung;
CREATE TRIGGER otg_set_timestamp_tg
	BEFORE INSERT OR UPDATE ON anwendung_aenderung
	FOR EACH ROW EXECUTE PROCEDURE otg_set_timestamp_tg ();

ALTER TABLE anwendung_aenderung DROP CONSTRAINT IF EXISTS change_fk;	
ALTER TABLE anwendung_aenderung
	ADD CONSTRAINT change_fk foreign key (aenderungs_id) references change_log (id) ON DELETE CASCADE;
	
ALTER TABLE anwendung_aenderung DROP CONSTRAINT IF EXISTS plan_fk;		
ALTER TABLE anwendung_aenderung
	ADD CONSTRAINT plan_fk foreign key (plan_id) references entwicklungsplan (id);


-- Tabelle in der currently anwendungs-Wert gespeichert wird
DROP TABLE IF EXISTS zuordnung;
CREATE TABLE zuordnung(
	plan_id TEXT,
	jahr INT,
	plan_intern_id TEXT,
	description TEXT,
	user_comment TEXT);
INSERT INTO zuordnung VALUES (NULL, NULL, NULL, NULL, NULL); -- Immer genau eine Zeile steht in der Tabelle


-- View auf change_log (hängt von den eingegebenen Metadaten ab!)
CREATE VIEW vw_change_log AS
	SELECT  * FROM change_log
	WHERE change_log.id IN (SELECT aenderungs_id
					FROM anwendung_aenderung
					WHERE plan_id = ANY (otg_zuordung_as_array ((SELECT plan_id 
											FROM zuordnung))));
															
-- CREATE VIEW vw_change_log AS
-- 	SELECT DISTINCT ON (cl.id) 	cl.id, cl.osm_id, cl.tstamp, cl.table_ident, cl.action, cl.members, cl.way, cl.power, 
-- 					cl.voltage, cl.cables, cl.wires, cl.circuits, cl.frequency, cl.hinweis,
-- 					aa.description, aa.user_comment, (SELECT plan_id FROM zuordnung) as devel_plans  
-- 		FROM change_log as cl, anwendung_aenderung as aa
-- 		
-- 	WHERE 	cl.id = aa.aenderungs_id AND
-- 		aa.aenderungs_id = ANY (otg_zuordung_as_array ((SELECT plan_id FROM zuordnung))));
		

CREATE TRIGGER otg_vw_change_log_edit_delete_tg 
	INSTEAD OF DELETE ON vw_change_log
	FOR EACH ROW EXECUTE PROCEDURE otg_vw_change_log_edit_delete_tg  ();

CREATE TRIGGER otg_vw_change_log_edit_update_tg
	INSTEAD OF UPDATE ON vw_change_log
	FOR EACH ROW EXECUTE PROCEDURE otg_vw_change_log_edit_update_tg  ();
