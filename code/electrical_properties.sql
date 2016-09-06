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

--------------------------------------------------------------
-- SPEZIFIKATIONEN 
--------------------------------------------------------------

SET SCHEMA 'public';
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;

-- AC-LEITUNGEN 

DROP TABLE IF EXISTS branch_specifications;	
CREATE TABLE branch_specifications (	spec_id serial NOT NULL PRIMARY KEY,
					voltage_kV INT, 
					power TEXT, 
					AL_mm2 TEXT, -- Aluminium Stahl -- Anpassen!!!  
					Stherm_MVA INT, -- Thermische Grenzleistung (in diesem Fall mögliche Dauerbelastung)
					Snat_MVA INT, -- Natürliche Leistung
					R_Ohm_per_km REAL, -- Ohmscher Belag (längs)
					L_mH_per_km REAL, -- Induktiver Belag (längs)
					G_nS_per_km REAL, -- Ableitungsbelag (Verluste an Kabelisolierungen etc.)
					C_nF_per_km REAL, -- Kapazitätsbelag (Quer)
					Zw_Ohm INT); -- Wellenwiderstand (wird die Leitung mit diesem Widerstand geschlossen, so fließt natürliche Leistung. Leitung nimmt keine Blindleistung auf (kompensation))

-- Die folgenden Daten wurden der Quelle "Freileitung vs. Kabel" der Uni Duisburg-Essen entnommen.
-- Theoretisch müssten die Werte für jede Freileitung berechnet werden, da die Ergebnisse stark von Faktoren wie Leiterabstände etc. abhängen
-- Die Beläge beziehen sich auf ein Leiterseil des 3-Leitersystems
-- Stherm und Snat beziehen sich auf das gesamte System (3 Leiter)
-- Diese Konvention wird auch von Matpower verwendet					

INSERT INTO branch_specifications 
	VALUES (DEFAULT, 110, 'line', '2*265/35', 260, 34, 0.109, 1.2, 40, 9.5, 355);
INSERT INTO branch_specifications 
	VALUES (DEFAULT, 110, 'cable', '1400', 280, 347, 0.0177, 0.3, 78, 250, 35);
INSERT INTO branch_specifications 
	VALUES (DEFAULT, 220, 'line', '2*265/35', 520, 136, 0.109, 1.0, 30, 11, 302);
INSERT INTO branch_specifications 
	VALUES (DEFAULT, 220, 'cable', '1400', 550, 1250, 0.0176, 0.3, 67, 210, 39);
INSERT INTO branch_specifications 
	VALUES (DEFAULT, 380, 'line', '4*265/35', 1790, 600, 0.028, 0.8, 15, 14, 240);
INSERT INTO branch_specifications 
	VALUES (DEFAULT, 380, 'cable', '1400', 925, 3290, 0.0175, 0.3, 56, 180, 44);


-- DC-LEITUNGEN 

DROP TABLE IF EXISTS dcline_specifications;	
CREATE TABLE dcline_specifications (
			spec_id serial NOT NULL PRIMARY KEY,
			power TEXT,
			r_ohm_per_km REAL,
			I_A_therm REAL,	
			leitertyp TEXT);

-- Die folgenden DAten werden aus der Quelle "Szenarien für eine langfristige Netzentwicklung" BMWI übernommen.
-- Die Quelle unterscheided CSC Kabel und FReileiung und VSC. Jedoch sind die fürs Netzmodell relevanten Kennwerte gleich
-- Die thermisch maximale übertragungsleistung wird über den thermischen Grenzstrom berechnet.
-- Bei HGÜ Leitungen ist wichtig zu verstehen, wie die spannung angegeben wird. Bei hin- und Rückleiter (Bipolar) wird i.d.R. +- angegeben
-- (Spannung ist dann also doppelt so hocht)

INSERT INTO dcline_specifications
	VALUES (DEFAULT, 'line', 0.0159, 3840, '4er Buendel 490-Al1/64-ST1A');
INSERT INTO dcline_specifications
	VALUES (DEFAULT, 'cable', 0.0132, 1875, '1x2500 Al Mass impregnated');



-- TRAFOS

DROP TABLE IF EXISTS transformer_specifications;	
CREATE TABLE transformer_specifications (	
					spec_id serial NOT NULL PRIMARY KEY,
					S_MVA INT, -- Bemessungsscheinleistung
					U_OS REAL, -- Oberspannung (Volt)
					U_US REAL, -- Unterspannung (Volt)
					u_kr REAL); -- relative Kurzschlussspannung (%)
--Trafodaten aus:					
-- Springer: Elektrische Kraftwerke und Netze S. 228					

INSERT INTO transformer_specifications 
	VALUES (DEFAULT, 1000, 380000, 220000, 13.5); -- Springer: Elektrische Kraftwerke und Netze S. 228/219
INSERT INTO transformer_specifications 
	VALUES (DEFAULT, 300, 380000, 110000, 14);
INSERT INTO transformer_specifications 
	VALUES (DEFAULT, 200, 220000, 110000, 12);
