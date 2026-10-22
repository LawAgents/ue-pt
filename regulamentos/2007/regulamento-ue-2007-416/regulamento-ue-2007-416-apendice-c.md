---
id: "regulamento-ue-2007-416-apendice-c"
celex: "32007R0416"
title: "Regulamento (CE) n. o 416/2007 da Comissão, de 22 de Março de 2007 , relativo às especificações técnicas dos avisos à navegação a que se refere o artigo 5. o da Directiva 2005/44/CE do Parlamento Europeu e do Conselho relativa a serviços de informação fluvial (RIS) harmonizados nas vias navegáveis interiores da Comunidade — Apêndice C"
type: "Regulamento"
number: "416/2007"
year: 2007
date: 2007-03-13
status: "em vigor"
text_version: "consolidado"
last_amended: 2018-12-29
consolidated_celex: "02007R0416-20181229"
source: "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:02007R0416-20181229"
eli: "http://data.europa.eu/eli/reg/2007/416/oj"
retrieved: 2026-10-21
legal_notice: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
part_of: "regulamento-ue-2007-416"
part: "Apêndice C"
---

# Regulamento (CE) n. o 416/2007 da Comissão, de 22 de Março de 2007 , relativo às especificações técnicas dos avisos à navegação a que se refere o artigo 5. o da Directiva 2005/44/CE do Parlamento Europeu e do Conselho relativa a serviços de informação fluvial (RIS) harmonizados nas vias navegáveis interiores da Comunidade — Apêndice C

## Apêndice C

| No | Tag (Group headers and closers are boldly printed) | Description | Occ. | Rule |
|---|---|---|---|---|
|  | xmlns:nts="http://www.ris.eu/nts/4.0.4.0" |  |  |  |
|  | <RIS_Message> | Notice to Skippers |  |  |
| 1s | <identification> | Identification section | M | 1 |
| 1.1 | <internal_id>xs:string (64)</internal_id> | Internal ID | C |  |
| 1.2 | <from>xs:string (64)</from> | Sender (System) of the message | M |  |
| 1.3 | <originator>xs:string (64)</originator> | Originator (initiator) of the information in this message | M |  |
| 1.4 | <country_code>nts:country_code_enum</country_code> | Country where message is valid | M |  |
| 1.5 | <language_code>nts:language_code_enum</language_code> | Original language used in the textual info. (contents) | M |  |
| 1.6 | <district>xs:string (64)</district> | District / Region within the specified country, where the message is applicable | C |  |
| 1.7 | <date_issue>xs:dateTime<date_issue> | Date and time of publication including time zone (yyyy-mm-ddThh:mm:ss+hh:mm) | M |  |
| 1e | </identification> |  |  |  |
| 2s | <ftm> | Fairway and traffic related section | C | 1 |
| 2.1 | <internal_id>xs:string (64)</internal_id> | Internal ID | C |  |
| 2.2s | <nts_number> | NtS Number | M |  |
| 2.2.1 | <organisation>xs:string (64)</organisation | Name of the publishing organisation (NtS Provider) | M |  |
| 2.2.2 | <year>xs:gYear (1900-9999)</year> | Year of first issuing of the notice | M |  |
| 2.2.3 | <number>xs:integer (0-99999999)</number> | Number of the notice (per year, starting with: 1, 0 shall not be used for published notices) | M |  |
| 2.2.4 | <serial_number>xs:integer (0-99)</serial_number> | Serial number of notice (replacements and withdrawals), original notice: 0 | M |  |
| 2.2e | </nts_number> |  |  |  |
| 2.3s | <target_group> | Target group information | C |  |
| 2.3.1 | <target_group_code>nts:target_group_code_enum</target_group_code> | Target group (vessel type) for this message | M | 5 |
| 2.3.2 | <direction_code>nts:direction_code_enum</direction_code> | Upstream or downstream traffic, or both | M | 5 |
| 2.3e | </target_group> |  |  |  |
| 2.4 | <subject_code>nts:subject_code_enum</subject_code> | Subject code | M |  |
| 2.5s | <validity_period> | Overall period of validity | M |  |
| 2.5.1 | <date_start>xs:date</date_start> | Start date of validity period including time zone (yyyy-mm-dd+hh:mm) | M |  |
| 2.5.2 | <date_end>xs:date</date_end> | End date of validity period including time zone (yyyy-mm-dd+hh:mm) | C |  |
| 2.5e | </validity_period> |  |  |  |
| 2.6 | <contents>xs:string (500)</contents> | Additional information in local language | C |  |
| 2.7 | <source>xs:string (64)</source> | Notice source (name of authority) | C |  |
| 2.8 | <reason_code>nts:reason_code_enum</reason_code> | Reason / justification of notice | C |  |
| 2.9s | <communication> | Communication channel information | C |  |
| 2.9.1 | <reporting_code>nts:reporting_code_enum</reporting_code> | Reporting regime (information or duty to report) | M | 5 |
| 2.9.2 | <communication_code>nts:communication_code_enum</communication_code> | Communication code (telephone, VHF etc.) | M | 5 |
| 2.9.3 | <number>xs:string (128)</number> | Telephone, VHF number (including callsign), e-mail address, URL or teletext | C |  |
| 2.9.4 | <label>xs:string (256)</label> | Name of the attachment or additional information | C |  |
| 2.9.5 | <remark>xs:string (1024)</remark> | Additional remarks concerning the communication | C |  |
| 2.9e | </communication> |  |  |  |
| 2.10s | <fairway_section> | Fairway section, also available for objects (no 2.11) | C | 2 |
| 2.10.1s | <geo_object> | Geo information of fairway | M | 5 |
| 2.10.1.1 | <id>nts:isrs_code_type</id> | ISRS Location Code of the fairway section (2x) <br> Pattern=[A-Z]{2}[A-Z]{3}[A-Z0-9]{5}[A-Z0-9]{5}[0-9]{5} | M | 7 |
| 2.10.1.2 | <name>xs:string (256)</name> | Local name of the fairway section (f.e.: Rhine between bridge A and bridge B) | M |  |
| 2.10.1.3 | <type_code>nts:type_code_enum</type_code> | Type of geographical object (default=FWY) | M |  |
| 2.10.1.4 | <position_code>nts:position_code_enum</position_code> | Describes the position related to the fairway | C |  |
| 2.10.1.5s | <coordinate> | Fairway section begin and end coordinates (2x) | C | 7 |
| 2.10.1.5.1 | <lat>xs:string (10-12)</lat> | [d]d mm.mmm[m] N | M | 5 |
| 2.10.1.5.2 | <long>xs:string (10-13)</long> | [d][d]d mm.mmm[m] E | M | 5 |
| 2.10.1.5e | </coordinate> |  |  |  |
| 2.10.1.6 | <fairway_name>xs:string (256)</fairway_name> | Waterway name (usefull if no RIS Index is available). | C |  |
| 2.10.1e | </geo_object> |  |  |  |
| 2.10.2s | <limitation> | Fairway section limitations | C |  |
| 2.10.2.1s | <limitation_period> | Limitation periods / intervals (All limitations have to include a limitation period with an interval code in order to allow proper calculations within voyage planning applications) | C |  |
| 2.10.2.1.1 | <date_start>xs:date</date_start> | Start date of limitation period (overall) INCLUDING time zone <br> format=yyyy-mm-dd+hh:mm | M | 5 |
| 2.10.2.1.2 | <date_end>xs:date</date_end> | End date of limitation period INCLUDING time zone <br> format=yyyy-mm-dd+hh:mm | C |  |
| 2.10.2.1.3 | <time_start>xs:time</time_start> | Start time of limitation period WITHOUT time zone <br> format=hh:mm:ss [whereas ss=00] | C |  |
| 2.10.2.1.4 | <time_end>xs:time</time_end> | End time of limitation period WITHOUT time zone <br> format=hh:mm:ss [whereas ss=00] | C |  |
| 2.10.2.1.5 | <interval_code>nts:interval_code_enum</interval_code> | Interval for limitation (mandatory M(5) but is set to C to be compatible with former XSD version) | C |  |
| 2.10.2.1e | </limitation_period> |  |  |  |
| 2.10.2.2 | <limitation_code>nts:limitation_code_enum</limitation_code> | Kind of limitation | M | 5 |
| 2.10.2.3 | <position_code>nts:position_code_enum</position_code> | Describes the position of the limitation related to the fairway | C |  |
| 2.10.2.4 | <value>xs:float</value> | Value of limitation (i.e. max draught) | C |  |
| 2.10.2.5 | <unit>nts:unit_enum</unit> | Unit of the value of the limitation | C |  |
| 2.10.2.6 | <reference_code>nts:reference_code_enum</reference_code> | Value reference | C |  |
| 2.10.2.7 | <indication_code>nts:indication_code_enum</indication_code> | Minimum or maximum or reduced by | C |  |
| 2.10.2.8s | <target_group> | Target group information | C |  |
| 2.10.2.8.1 | <target_group_code>nts:target_group_code_enum</target_group_code> | Target group (vessel type) for this limitation | M | 5 |
| 2.10.2.8.2 | <direction_code>nts:direction_code_enum</direction_code> | Upstream or downstream traffic, or both | M | 5 |
| 2.10.2.8e | </target_group> |  |  |  |
| 2.10.2e | </limitation> |  |  |  |
| 2.10e | </fairway_section> |  |  |  |
| 2.11s | <object> | Object section | C | 2 |
| 2.11.1s | <geo_object> | Geo Information of object | M | 5 |
| 2.11.1.1 | <id>nts:isrs_code_type</id> | ISRS Location Code of the object (1x) <br> Pattern=[A-Z]{2}[A-Z]{3}[A-Z0-9]{5}[A-Z0-9]{5}[0-9]{5} | M | 8 |
| 2.11.1.2 | <name>xs:string (256)</name> | Local name of the aggregated object | M |  |
| 2.11.1.3 | <type_code>nts:type_code_enum</type_code> | Type of geographical object | M |  |
| 2.11.1.4 | <position_code>nts:position_code_enum</position_code> | Describes the position related to the object | C |  |
| 2.11.1.5s | <coordinate> | Object coordinates (1x) | C | 8 |
| 2.11.1.5.1 | <lat>xs:string (10-12)</lat> | [d]d mm.mmm[m] N | M | 5 |
| 2.11.1.5.2 | <long>xs:string (10-13)</long> | [d][d]d mm.mmm[m] E | M | 5 |
| 2.11.1.5e | </coordinate> |  |  |  |
| 2.11.1.6 | <fairway_name>xs:string (256)</fairway_name> | Waterway name (usefull if no RIS Index is available). | C |  |
| 2.11.1e | </geo_object> |  |  |  |
| 2.11.2s | <limitation> | Object limitation section | C |  |
| 2.11.2.1s | <limitation_period> | Limitation periods / intervals (All limitations have to include a limitation period with an interval code in order to allow proper calculations within voyage planning applications) | C |  |
| 2.11.2.1.1 | <date_start>xs:date</date_start> | Start date of limitation period (overall) INCLUDING time zone <br> format=yyyy-mm-dd+hh:mm | M | 5 |
| 2.11.2.1.2 | <date_end>xs:date</date_end> | End date of limitation period INCLUDING time zone <br> format=yyyy-mm-dd+hh:mm | C |  |
| 2.11.2.1.3 | <time_start>xs:time</time_start> | Start time of limitation period WITHOUT time zone <br> format=hh:mm:ss [whereas ss=00] | C |  |
| 2.11.2.1.4 | <time_end>xs:time</time_end> | End time of limitation period WITHOUT time zone <br> format=hh:mm:ss [whereas ss=00] | C |  |
| 2.11.2.1.5 | <interval_code>nts:interval_code_enum</interval_code> | Interval for limitation (mandatory M(5) but is set to C to be compatible with former XSD version) | C |  |
| 2.11.2.1e | </limitation_period> |  |  |  |
| 2.11.2.2 | <limitation_code>nts:limitation_code_enum</limitation_code> | Kind of limitation | M | 5 |
| 2.11.2.3 | <position_code>nts:position_code_enum</position_code> | Describes the position of the limitation related to the fairway | C |  |
| 2.11.2.4 | <value>xs:float</value> | Value of limitation (i.e. max draught) | C |  |
| 2.11.2.5 | <unit>nts:unit_enum</unit> | Unit of the value of the limitation | C |  |
| 2.11.2.6 | <reference_code>nts:reference_code_enum</reference_code> | Value reference | C |  |
| 2.11.2.7 | <indication_code>nts:indication_code_enum</indication_code> | Minimum or maximum or reduced by | C |  |
| 2.11.2.8s | <target_group> | Target group information | C |  |
| 2.11.2.8.1 | <target_group_code>nts:target_group_code_enum</target_group_code> | Target group (vessel type) for this limitation | M | 5 |
| 2.11.2.8.2 | <direction_code>nts:direction_code_enum</direction_code> | Upstream or downstream traffic, or both | M | 5 |
| 2.11.2.8e | </target_group> |  |  |  |
| 2.11.2e | </limitation> |  |  |  |
| 2.11e | </object> |  |  |  |
| 2e | </ftm> |  |  |  |
| 3s | <wrm> | Water related section | C | 1 |
| 3.1 | <internal_id>xs:string (64)</internal_id> | Internal ID | C |  |
| 3.2s | <nts_number> | NtS Number | C |  |
| 3.2.1 | <organisation>xs:string (64)</organisation | Name of the publishing organisation (NtS Provider) | M | 5 |
| 3.2.2 | <year>xs:gYear (1900-9999)</year> | Current year of the notice | M | 5 |
| 3.2.3 | <number>xs:integer (0-99999999)</number> | Number of the notice <br> (see Developers Guide for WRM-Message Number generation) | M | 5 |
| 3.2.4 | <serial_number>xs:integer (0-99)</serial_number> | Serial number of the notice <br> (see Developers Guide for WRM-Message Serial Number generation) | M | 5 |
| 3.2e | </nts_number> |  |  |  |
| 3.3s | <validity_period> | Overall period of validity | M |  |
| 3.3.1 | <date_start>xs:date</date_start> | Start date of validity period including time zone (yyyy-mm-dd+hh:mm) | M |  |
| 3.3.2 | <date_end>xs:date</date_end> | End date of validity period including time zone (yyyy-mm-dd+hh:mm) | C |  |
| 3.3e | </validity_period> |  |  |  |
| 3.4s | <geo_object> | Geo Information of measurement location | M | 5 |
| 3.4.1 | <id>nts:isrs_code_type</id> | ISRS Location Code of the object/fairway (1x or 2x) <br> Pattern=[A-Z]{2}[A-Z]{3}[A-Z0-9]{5}[A-Z0-9]{5}[0-9]{5} | M | 9 |
| 3.4.2 | <name>xs:string (256)</name> | Local name of the object/fairway | M |  |
| 3.4.3 | <type_code>nts:type_code_enum</type_code> | Type of geographical object/fairway | M |  |
| 3.4.4 | <position_code>nts:position_code_enum</position_code> | Describes the position related to the object/fairway | C |  |
| 3.4.5s | <coordinate> | Object/Fairway coordinates (1x or 2x) | C | 9 |
| 3.4.5.1 | <lat>xs:string (10-12)</lat> | [d]d mm.mmm[m] N | M | 5 |
| 3.4.5.2 | <long>xs:string (10-13)</long> | [d][d]d mm.mmm[m] E | M | 5 |
| 3.3.5e | </coordinate> |  |  |  |
| 3.3.6 | <fairway_name>xs:string (256)</fairway_name> | Waterway name (usefull if no RIS Index is available). | C |  |
| 3.4e | </geo_object> |  |  |  |
| 3.5 | <reference_code>nts:reference_code_enum</reference_code> | Value reference (measurement reference) | C | 6 |
| 3.6s | <measure> | Measurements (normal or predicted values) | M | 5 |
| 3.6.1 | <predicted>xs:boolean</predicted> | Predicted measurement (1 or true) or real measurement (0 or false) | M |  |
| 3.6.2 | <measure_code>nts:measure_code_enum</measure_code> | Kind of water related information | M |  |
| 3.6.3 | <value>xs:float</value> | Measured or predicted value | C | 10 |
| 3.6.4 | <value_min>xs:float</value_min> | Lowest value of confidence interval | C |  |
| 3.6.5 | <value_max>xs:float</value_max> | Highest value of confidence interval | C |  |
| 3.6.6 | <unit>nts:unit_enum</unit> | Unit of the water related value | C |  |
| 3.6.7 | <barrage_code>nts:barrage_code_enum</barrage_code> | Barrage status | C | 11 |
| 3.6.8 | <regime_code>nts:regime_code_enum</regime_code> | Regime applicable | C | 12 |
| 3.6.9 | <measuredate>xs:dateTime</measuredate> | Date and Time of measurement or predicted value including time zone <br> Format=yyyy-mm-ddThh:mm:ss+hh:mm | M |  |
| 3.6.10s | <difference> | Difference with comparative value | C |  |
| 3.6.10.1 | <value_difference>xs:float</value_difference> | Difference with comparative value | M | 5 |
| 3.6.10.2 | <time_difference>xs:duration</time_difference> | Time difference to measuredate of comparative value | M | 5 |
| 3.6.10e | </difference> |  |  |  |
| 3.6e | </measure> |  |  |  |
| 3e | </wrm> |  |  |  |
| 4s | <icem> | Ice related section | C | 1 |
| 4.1 | <internal_id>xs:string (64)</internal_id> | Internal ID | C |  |
| 4.2s | <nts_number> | NtS Number | M |  |
| 4.2.1 | <organisation>xs:string (64)</organisation | Name of the publishing organisation (NtS Provider) | M |  |
| 4.2.2 | <year>xs:gYear (1900-9999)</year> | Current year of the notice | M |  |
| 4.2.3 | <number>xs:integer (0-99999999)</number> | Number of the notice (per year, starting with: 1, 0 shall not be used for published notices) | M |  |
| 4.2.4 | <serial_number>xs:integer (0-99)</serial_number> | Serial number of notice, original notice: 0 | M |  |
| 4.2e | </nts_number> |  |  |  |
| 4.3s | <validity_period> | Overall period of validity | M |  |
| 4.3.1 | <date_start>xs:date</date_start> | Start date of validity period including time zone (yyyy-mm-dd+hh:mm) | M |  |
| 4.3.2 | <date_end>xs:date</date_end> | End date of validity period including time zone (yyyy-mm-dd+hh:mm) | C |  |
| 4.3e | </validity_period> |  |  |  |
| 4.4s | <fairway_section> | Fairway section — the limitation inside the fairway section cannot be used in the ICEM | M | 5 |
| 4.4.1s | <geo_object> | Geo Information of fairway | M | 5 |
| 4.4.1.1 | <id>nts:isrs_code_type</id> | ISRS Location Code of the fairway section (2x) <br> Pattern=[A-Z]{2}[A-Z]{3}[A-Z0-9]{5}[A-Z0-9]{5}[0-9]{5} | M |  |
| 4.4.1.2 | <name>xs:string (256)</name> | Local Name of the fairway section (f.e.: Rhine between bridge A and bridge B) | M |  |
| 4.4.1.3 | <type_code>nts:type_code_enum</type_code> | Type of geographical object (default=FWY) | M |  |
| 4.4.1.4 | <position_code>nts:position_code_enum</position_code> | Describes the position related to the fairway | C |  |
| 4.4.1.5s | <coordinate> | Fairway section begin and end coordinates (2x) | C | 7 |
| 4.4.1.5.1 | <lat>xs:string (10-12)</lat> | [d]d mm.mmm[m] N | M | 5 |
| 4.4.1.5.2 | <long>xs:string (10-13)</long> | [d][d]d mm.mmm[m] E | M | 5 |
| 4.4.1.5e | </coordinate> |  |  |  |
| 4.4.1.6 | <fairway_name>xs:string (256)</fairway_name> | Waterway name (usefull if no RIS Index is available). | C |  |
| 4.4.1e | </geo_object> |  |  |  |
| 4.4e | </fairway_section> |  |  |  |
| 4.5s | <ice_condition> | Ice conditions | M |  |
| 4.5.1 | <measuredate>xs:dateTime</measuredate> | Date and Time of measurement or prediction including time zone <br> Format=yyyy-mm-ddThh:mm:ss+hh:mm | M |  |
| 4.5.2 | <ice_condition_code>nts:ice_condition_code_enum</ice_condition_code> | Condition code | C | 4 |
| 4.5.3 | <ice_accessibility_code>nts:ice_accessibility_code_enum</ice_accessibility_code> | Accessibility code | C | 4 |
| 4.5.4 | <ice_classification_code>nts:ice_classification_code_enum</ice_classification_code> | Classification code | C | 4 |
| 4.5.5 | <ice_situation_code>nts:ice_situation_code_enum</ice_situation_code> | Situation code | C | 4 |
| 4.5e | </ice_condition> |  |  |  |
| 4e | </icem> |  |  |  |
| 5s | <werm> | Weather related section | C | 1 |
| 5.1 | <internal_id>xs:string (64)</internal_id> | Internal ID | C |  |
| 5.2s | <nts_number> | NtS Number | C |  |
| 5.2.1 | <organisation>xs:string (64)</organisation | Name of the publishing organisation (NtS Provider) | M | 5 |
| 5.2.2 | <year>xs:gYear (1900-9999)</year> | Year of issuing of the notice | M | 5 |
| 5.2.3 | <number>xs:integer (0-99999999)</number> | Number of the notice (per year, starting with: 1, 0 shall not be used for published notices) | M | 5 |
| 5.2.4 | <serial_number>xs:integer (0-99)</serial_number> | Serial number of notice, original notice: 0 | M | 5 |
| 5.2e | </nts_number> |  |  |  |
| 5.3s | <validity_period> | Overall period of validity | M | 13 |
| 5.3.1 | <date_start>xs:date</date_start> | Start date of validity period including time zone (yyyy-mm-dd+hh:mm) | M |  |
| 5.3.2 | <date_end>xs:date</date_end> | End date of validity period including time zone (yyyy-mm-dd+hh:mm) | C |  |
| 5.3e | </validity_period> |  |  |  |
| 5.4s | <fairway_section> | Fairway section | M |  |
| 5.4.1s | <geo_object> | Geo Information of fairway | M |  |
| 5.4.1.1 | <id>nts:isrs_code_type</id> | ISRS Location Code of the fairway section (2x) <br> Pattern=[A-Z]{2}[A-Z]{3}[A-Z0-9]{5}[A-Z0-9]{5}[0-9]{5} | M | 7 |
| 5.4.1.2 | <name>xs:string (256)</name> | Local name of the fairway section (f.e.: Rhine between bridge A and bridge B) | M |  |
| 5.4.1.3 | <type_code>nts:type_code_enum</type_code> | Type of geographical object (default=FWY) | M |  |
| 5.4.1.4 | <position_code>nts:position_code_enum</position_code> | Describes the position related to the fairway | C |  |
| 5.4.1.5s | <coordinate> | Fairway section begin and end coordinates (2x) | C | 7 |
| 5.4.1.5.1 | <lat>xs:string (10-12)</lat> | [d]d mm.mmm[m] N | M | 5 |
| 5.4.1.5.2 | <long>xs:string (10-13)</long> | [d][d]d mm.mmm[m] E | M | 5 |
| 5.4.1.5e | </coordinate> |  |  |  |
| 5.4.1.6 | <fairway_name>xs:string (256)</fairway_name> | Waterway name (usefull if no RIS Index is available). | C |  |
| 5.4.1e | </geo_object> |  |  |  |
| 5.4e | </fairway_section> |  |  |  |
| 5.5s | <weather_report> | Weather Report (1x or 2x) | M |  |
| 5.5.1 | <measuredate>xs:dateTime</measuredate> | Date and Time of measurement or predicted value including time zone <br> Format=yyyy-mm-ddThh:mm:ss+hh:mm | C |  |
| 5.5.2 | <forecast>xs:boolean</forecast> | Forecast (true or 1) OR Actual report (false or 0) | M |  |
| 5.5.3 | <weather_class_code>nts:weather_class_code_enum</weather_class_code> | Classification of weather report (0..Nx) | M | 3 |
| 5.5.4s | <weather_item> | Weather items (0..Nx) | C |  |
| 5.5.4.1 | <weather_item_code>nts:weather_item_code_enum</weather_item_code> | Weather item type (Wind, Wave etc) | M | 5 |
| 5.5.4.2 | <value_min>xs:float</value_min> | Actual or Minimum value | M | 5 |
| 5.5.4.3 | <value_max>xs:float</value_max> | Maximum value | C |  |
| 5.5.4.4 | <value_gusts>xs:float</value_gusts> | Gusts value (Wind) | C |  |
| 5.5.4.5 | <unit>nts:unit_enum</unit> | Unit of the value | C |  |
| 5.5.4.6 | <weather_category_code>nts:weather_category_code_enum</weather_category_code> | Classification of wind report | C |  |
| 5.5.4.7 | <direction_code_min>nts:weather_direction_code_enum</direction_code_min> | Direction of wind or wave | C |  |
| 5.5.4.8 | <direction_code_max>nts:weather_direction_code_enum</direction_code_max> | Direction of wind or wave | C |  |
| 5.5.4e | </weather_item> |  |  |  |
| 5.5e | </weather_report> |  |  |  |
| 5e | </werm> |  |  |  |
| Legend for Occurrence (Occ.): <br> Mandatory (M) <br> Conditional (C) |  |  |  |  |

Rules applicable to table "NtS XSD V.4.0.4.0":

1. In one <RIS Message> at least two sections have to be filled in:

— the <identification> section (1),

— one of the following sections:

—

— <ftm> (fairway and traffic related messages) (2),

— <wrm> (water related message) (3),

— <icem> (ice message) (4),

— <werm> (weather related message) (5).

2. At least one of the Group 2.10 (<fairway section>) or Group 2.11 (<object>) has to be given within <ftm>.

3. A combinations of <weather_class_code> tags (5.5.3) in section <weather_report> can be given.

4. In group 4.5 (<ice condition>) at least one of the conditional elements 4.5.2 to 4.5.5 have to be given.

5. If a conditional group contains mandatory subgroups or elements these will only be mandatory if the group on the higher level is applied.

6. Element <reference_code> is only mandatory for "WAL" (water level) in <wrm> (3.5).

7. A <geo_object> in <fairway section> (<ftm> 2.10.1 , <icem> 4.4.1, <werm> 5.4.1) is defined by the begin and end

ISRS Location Codes and coordinates (2 ISRS Location Codes and 2 sets of coordinates).

8. A <geo_object> in <object> section (<ftm> 2.11.1) is defined by the ISRS Location Code and coordinates of its center point (1 ISRS Location Code 1 set of coordinates).

9. A <geo_object> in <wrm> has 2 ISRS Location Codes and 2 sets of coordinates in case the <type_code> (3.4.3) is "FWY", "RIV" or "CAN", otherwise only 1 ISRS Location Code and 1 set of coordinates has to be given.

10. If there is a measurement the elements <value> (3.6.3) or <value_min> (3.6.4) and <value_max> (3.6.5) is/are mandatory if <measure_code> (3.6.2) is either "DIS", "VER", "LSD" or "WAL".

In case there is no measurement (and a message should be sent anyhow) the value elements shall be omitted.

11. Element <barrage_code> (3.6.7) is mandatory if <measure code> (3.6.2) is "BAR".

12. Element <regime_code> (3.6.8) is mandatory if <measure code> (3.6.2) is "REG".

13. Predictions for more than one <validity_period> (5.3) require individual <werm> messages.

14. In case of <icem> (4.4.2) and <werm> a <limitation> section is not applicable. Limitations shall be provided via FTM notices.

<?xml version="1.0" encoding="UTF-8"?>

<xs:schema xmlns:nts="http://www.ris.eu/nts/4.0.4.0" xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace=">http://www.ris.eu/nts/4.0.4.0" elementFormDefault="qualified" attributeFormDefault="unqualified" version="4.0.4.0">

<!--

\===========================================

= definition of main element RIS_Message =

= and corresponding type RIS_Message_Type =

\===========================================

-->

<xs:element name="RIS_Message" type="nts:RIS_Message_Type">

<xs:annotation>

<xs:documentation>River Information Service Message</xs:documentation>

</xs:annotation>

</xs:element>

<xs:complexType name="RIS_Message_Type">

<xs:sequence>

<xs:element name="identification" type="nts:identification_type">

<xs:annotation>

<xs:documentation>Identification section</xs:documentation>

</xs:annotation>

</xs:element>

<xs:choice>

<xs:annotation>

<xs:documentation>One msg contains one of these sections</xs:documentation>

</xs:annotation>

<xs:element name="ftm" type="nts:ftm_type" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Fairway and traffic related section</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="wrm" type="nts:wrm_type" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Water related section</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="icem" type="nts:icem_type" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Ice related section</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="werm" type="nts:werm_type" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Weather related section</xs:documentation>

</xs:annotation>

</xs:element>

</xs:choice>

</xs:sequence>

</xs:complexType>

<!--

\==========================================

= definition of identification_type, =

= used in definition of RIS_Message_Type =

\==========================================

-->

<xs:complexType name="identification_type">

<xs:sequence>

<xs:element name="internal_id" type="nts:internal_id_type" minOccurs="0">

<xs:annotation>

<xs:documentation>Internal ID</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="from">

<xs:annotation>

<xs:documentation>Sender (System) of the message</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:maxLength value="64"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

<xs:element name="originator">

<xs:annotation>

<xs:documentation>Originator (initiator) of the information in this message</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:maxLength value="64"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

<xs:element name="country_code" type="nts:country_code_enum">

<xs:annotation>

<xs:documentation>Country where message is valid</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="language_code" type="nts:language_code_enum">

<xs:annotation>

<xs:documentation>Original language used in the textual info. (contents)</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="district" minOccurs="0">

<xs:annotation>

<xs:documentation>District / Region within the specified country, where the message is applicable</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:maxLength value="64"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

<xs:element name="date_issue" type="xs:dateTime">

<xs:annotation>

<xs:documentation>Date and time of publication including time zone</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<!--

\===================================================

= types used in definition of identification_type =

\===================================================

-->

<xs:simpleType name="country_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="2"/>

<xs:enumeration value="AT"/>

<xs:enumeration value="BE"/>

<xs:enumeration value="BG"/>

<xs:enumeration value="CH"/>

<xs:enumeration value="CY"/>

<xs:enumeration value="CZ"/>

<xs:enumeration value="DE"/>

<xs:enumeration value="DK"/>

<xs:enumeration value="EE"/>

<xs:enumeration value="ES"/>

<xs:enumeration value="FI"/>

<xs:enumeration value="FR"/>

<xs:enumeration value="GB"/>

<xs:enumeration value="GR"/>

<xs:enumeration value="HR"/>

<xs:enumeration value="HU"/>

<xs:enumeration value="IE"/>

<xs:enumeration value="IT"/>

<xs:enumeration value="LT"/>

<xs:enumeration value="LU"/>

<xs:enumeration value="LV"/>

<xs:enumeration value="MD"/>

<xs:enumeration value="ME"/>

<xs:enumeration value="MT"/>

<xs:enumeration value="NL"/>

<xs:enumeration value="PL"/>

<xs:enumeration value="PT"/>

<xs:enumeration value="RO"/>

<xs:enumeration value="RS"/>

<xs:enumeration value="SE"/>

<xs:enumeration value="SI"/>

<xs:enumeration value="SK"/>

<xs:enumeration value="RU"/>

<xs:enumeration value="UA"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="language_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="2"/>

<xs:enumeration value="DE"/>

<xs:enumeration value="EN"/>

<xs:enumeration value="FR"/>

<xs:enumeration value="NL"/>

<xs:enumeration value="SK"/>

<xs:enumeration value="HU"/>

<xs:enumeration value="HR"/>

<xs:enumeration value="SR"/>

<xs:enumeration value="BG"/>

<xs:enumeration value="RO"/>

<xs:enumeration value="RU"/>

<xs:enumeration value="CS"/>

<xs:enumeration value="PL"/>

<xs:enumeration value="PT"/>

<xs:enumeration value="ES"/>

<xs:enumeration value="SV"/>

<xs:enumeration value="FI"/>

<xs:enumeration value="DA"/>

<xs:enumeration value="ET"/>

<xs:enumeration value="LV"/>

<xs:enumeration value="LT"/>

<xs:enumeration value="IT"/>

<xs:enumeration value="MT"/>

<xs:enumeration value="EL"/>

<xs:enumeration value="SL"/>

</xs:restriction>

</xs:simpleType>

<!--

\==========================================

= definition of ftm_type, =

= used in definition of RIS_Message_Type =

\==========================================

-->

<xs:complexType name="ftm_type">

<xs:sequence>

<xs:element name="internal_id" type="nts:internal_id_type" minOccurs="0">

<xs:annotation>

<xs:documentation>Internal ID</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="nts_number" type="nts:nts_number_type">

<xs:annotation>

<xs:documentation>NtS Number</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="target_group" type="nts:target_group_type" minOccurs="0" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Target group information</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="subject_code" type="nts:subject_code_enum">

<xs:annotation>

<xs:documentation>Subject code must contain one of the following: Announcement (ANNOUN), Warning (WARNIN), Notice withdrawn (CANCEL) or Information service (INFSER). More information on the use of codes can be found in the NtS Encoding Guide.</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="validity_period" type="nts:validity_period_type">

<xs:annotation>

<xs:documentation>Overall period of validity</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="contents" minOccurs="0">

<xs:annotation>

<xs:documentation>Additional information in local language</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:maxLength value="500"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

<xs:element name="source" minOccurs="0">

<xs:annotation>

<xs:documentation>Notice source (name of authority)</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:maxLength value="64"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

<xs:element name="reason_code" type="nts:reason_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Reason / justification of the notice</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="communication" type="nts:communication_type" minOccurs="0" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Communication channel information</xs:documentation>

</xs:annotation>

</xs:element>

<xs:choice maxOccurs="unbounded">

<xs:element name="fairway_section" type="nts:fairway_section_type">

<xs:annotation>

<xs:documentation>Fairway section</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="object" type="nts:object_type">

<xs:annotation>

<xs:documentation>Object section</xs:documentation>

</xs:annotation>

</xs:element>

</xs:choice>

</xs:sequence>

</xs:complexType>

<!--

\========================================

= types used in definition of ftm_type =

\========================================

-->

<xs:simpleType name="subject_code_enum">

<xs:restriction base="xs:string">

<xs:minLength value="3"/>

<xs:maxLength value="6"/>

<xs:enumeration value="ANNOUN"/>

<xs:enumeration value="WARNIN"/>

<xs:enumeration value="CANCEL"/>

<!-- the following values are added due to CR 128 -->

<xs:enumeration value="INFSER"/>

<!-- obsolete values due to CR 128 but still valid for backwards compatibility -->

<xs:enumeration value="OBSTRU"/>

<xs:enumeration value="PAROBS"/>

<xs:enumeration value="DELAY"/>

<xs:enumeration value="VESLEN"/>

<xs:enumeration value="VESHEI"/>

<xs:enumeration value="VESBRE"/>

<xs:enumeration value="VESDRA"/>

<xs:enumeration value="AVALEN"/>

<xs:enumeration value="CLEHEI"/>

<xs:enumeration value="CLEWID"/>

<xs:enumeration value="AVADEP"/>

<xs:enumeration value="NOMOOR"/>

<xs:enumeration value="SERVIC"/>

<xs:enumeration value="NOSERV"/>

<xs:enumeration value="SPEED"/>

<xs:enumeration value="WAVWAS"/>

<xs:enumeration value="PASSIN"/>

<xs:enumeration value="ANCHOR"/>

<xs:enumeration value="OVRTAK"/>

<xs:enumeration value="MINPWR"/>

<xs:enumeration value="DREDGE"/>

<xs:enumeration value="WORK"/>

<xs:enumeration value="EVENT"/>

<xs:enumeration value="CHGMAR"/>

<xs:enumeration value="CHGSER"/>

<xs:enumeration value="SPCMAR"/>

<xs:enumeration value="EXERC"/>

<xs:enumeration value="LEADEP"/>

<xs:enumeration value="LEVDEC"/>

<xs:enumeration value="LEVRIS"/>

<xs:enumeration value="LIMITA"/>

<xs:enumeration value="MISECH"/>

<xs:enumeration value="ECDISU"/>

<xs:enumeration value="NEWOBJ"/>

<xs:enumeration value="CHWWY"/>

<xs:enumeration value="CONWWY"/>

<xs:enumeration value="DIVER"/>

<xs:enumeration value="SPECTR"/>

<xs:enumeration value="LOCRUL"/>

<xs:enumeration value="VHFCOV"/>

<xs:enumeration value="HIGVOL"/>

<xs:enumeration value="TURNIN"/>

<xs:enumeration value="CONBRE"/>

<xs:enumeration value="CONLEN"/>

<xs:enumeration value="REMOBJ"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="reason_code_enum">

<xs:restriction base="xs:string">

<xs:minLength value="3"/>

<xs:maxLength value="6"/>

<xs:enumeration value="EVENT"/>

<xs:enumeration value="WORK"/>

<xs:enumeration value="DREDGE"/>

<xs:enumeration value="EXERC"/>

<xs:enumeration value="HIGWAT"/>

<xs:enumeration value="HIWAI"/>

<xs:enumeration value="HIWAII"/>

<xs:enumeration value="LOWWAT"/>

<xs:enumeration value="SHALLO"/>

<xs:enumeration value="CALAMI"/>

<xs:enumeration value="LAUNCH"/>

<xs:enumeration value="DECLEV"/>

<xs:enumeration value="FLOMEA"/>

<xs:enumeration value="BLDWRK"/>

<xs:enumeration value="REPAIR"/>

<xs:enumeration value="INSPEC"/>

<xs:enumeration value="FIRWRK"/>

<xs:enumeration value="LIMITA"/>

<xs:enumeration value="CHGFWY"/>

<xs:enumeration value="CONSTR"/>

<xs:enumeration value="DIVING"/>

<xs:enumeration value="SPECTR"/>

<xs:enumeration value="EXT"/>

<xs:enumeration value="MIN"/>

<xs:enumeration value="SOUND"/>

<xs:enumeration value="OTHER"/>

<xs:enumeration value="STRIKE"/>

<xs:enumeration value="FLOMAT"/>

<xs:enumeration value="EXPLOS"/>

<xs:enumeration value="ICE"/>

<xs:enumeration value="OBSTAC"/>

<!--the following values are added due to CR 128-->

<xs:enumeration value="CHGMAR"/>

<xs:enumeration value="DAMMAR"/>

<xs:enumeration value="FALMAT"/>

<xs:enumeration value="MISECH"/>

<xs:enumeration value="HEARIS"/>

<xs:enumeration value="HIGVOL"/>

<xs:enumeration value="ECDISU"/>

<xs:enumeration value="LOCRUL"/>

<xs:enumeration value="NEWOBJ"/>

<xs:enumeration value="OBUNWA"/>

<xs:enumeration value="VHFCOV"/>

<xs:enumeration value="REMOBJ"/>

<xs:enumeration value="LEVRIS"/>

<xs:enumeration value="SPCMAR"/>

<!--the following value is added due to CR 155-->

<xs:enumeration value="WERMCO"/>

<!--obsolete values due to CR 128 but still valid for backwards compatibility -->

<xs:enumeration value="INFSER"/>

</xs:restriction>

</xs:simpleType>

<xs:complexType name="communication_type">

<xs:sequence>

<xs:element name="reporting_code" type="nts:reporting_code_enum">

<xs:annotation>

<xs:documentation>Reporting regime (information, or duty to report)</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="communication_code" type="nts:communication_code_enum">

<xs:annotation>

<xs:documentation>Communication code (telephone, VHF etc.)</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="number" minOccurs="0">

<xs:annotation>

<xs:documentation>Telephone, VHF number (including callsign), e-mail address, URL or teletext</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:maxLength value="128"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

<xs:element name="label" minOccurs="0">

<xs:annotation>

<xs:documentation>Name of the attachment or additional information</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:maxLength value="256"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

<xs:element name="remark" minOccurs="0">

<xs:annotation>

<xs:documentation>Additional remarks concerning the communication</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:maxLength value="1024"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:simpleType name="reporting_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="3"/>

<xs:enumeration value="INF"/>

<xs:enumeration value="ADD"/>

<xs:enumeration value="REG"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="communication_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="3"/>

<xs:enumeration value="TE"/>

<xs:enumeration value="AP"/>

<xs:enumeration value="EM"/>

<xs:enumeration value="AH"/>

<xs:enumeration value="TT"/>

<xs:enumeration value="FX"/>

<xs:enumeration value="LS"/>

<xs:enumeration value="FS"/>

<xs:enumeration value="SO"/>

<xs:enumeration value="EI"/>

</xs:restriction>

</xs:simpleType>

<xs:complexType name="object_type">

<xs:sequence>

<xs:element name="geo_object" type="nts:geo_object_type">

<xs:annotation>

<xs:documentation>Geo Information of object</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="limitation" type="nts:limitation_type" minOccurs="0" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Object limitation section</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<!--

\==========================================

= definition of wrm_type, =

= used in definition of RIS_Message_Type =

\==========================================

-->

<xs:complexType name="wrm_type">

<xs:sequence>

<xs:element name="internal_id" type="nts:internal_id_type" minOccurs="0">

<xs:annotation>

<xs:documentation>Internal ID</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="nts_number" type="nts:nts_number_type" minOccurs="0">

<xs:annotation>

<xs:documentation>NtS Number</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="validity_period" type="nts:validity_period_type">

<xs:annotation>

<xs:documentation>Overall period of validity</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="geo_object" type="nts:geo_object_type">

<xs:annotation>

<xs:documentation>Object section</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="reference_code" type="nts:reference_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Value reference (measurement reference)</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="measure" type="nts:measure_type" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Measurements (normal or predicted values)</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<!--

\========================================

= types used in definition of wrm_type =

\========================================

-->

<xs:complexType name="measure_type">

<xs:sequence>

<xs:element name="predicted" type="xs:boolean">

<xs:annotation>

<xs:documentation>Predicted measurement (1 or true) or real measurement (0 or false)</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="measure_code" type="nts:measure_code_enum">

<xs:annotation>

<xs:documentation>Kind of water related information</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="value" type="xs:float" minOccurs="0">

<xs:annotation>

<xs:documentation>Measured or predicted value</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="value_min" type="xs:float" minOccurs="0">

<xs:annotation>

<xs:documentation>Lowest value of confidence interval</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="value_max" type="xs:float" minOccurs="0">

<xs:annotation>

<xs:documentation>Highest value of confidence interval</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="unit" type="nts:unit_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Unit of the water related value</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="barrage_code" type="nts:barrage_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Barrage status</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="regime_code" type="nts:regime_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Regime applicable</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="measuredate" type="xs:dateTime">

<xs:annotation>

<xs:documentation>Date and Time of measurement or predicted value including time zone</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="difference" type="nts:difference_type" minOccurs="0">

<xs:annotation>

<xs:documentation>Difference with comparative value</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:simpleType name="measure_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="3"/>

<xs:enumeration value="DIS"/>

<xs:enumeration value="REG"/>

<xs:enumeration value="BAR"/>

<xs:enumeration value="VER"/>

<xs:enumeration value="LSD"/>

<xs:enumeration value="WAL"/>

<!-- obsolete values due to CR 151 but still valid for backwards compatibility -->

<xs:enumeration value="NOM"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="barrage_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="3"/>

<xs:enumeration value="CLD"/>

<xs:enumeration value="OPG"/>

<xs:enumeration value="CLG"/>

<xs:enumeration value="OPD"/>

<xs:enumeration value="OPN"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="regime_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="2"/>

<xs:enumeration value="NO"/>

<xs:enumeration value="HI"/>

<xs:enumeration value="II"/>

<xs:enumeration value="I"/>

<xs:enumeration value="NN"/>

<xs:enumeration value="LO"/>

</xs:restriction>

</xs:simpleType>

<xs:complexType name="difference_type">

<xs:sequence>

<xs:element name="value_difference" type="xs:float">

<xs:annotation>

<xs:documentation>Difference with comparative value</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="time_difference" type="xs:duration">

<xs:annotation>

<xs:documentation>Time difference with measuredata of comparative measurement</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<!--

\==========================================

= definition of icem_type, =

= used in definition of RIS_Message_Type =

\==========================================

-->

<xs:complexType name="icem_type">

<xs:sequence>

<xs:element name="internal_id" type="nts:internal_id_type" minOccurs="0">

<xs:annotation>

<xs:documentation>Internal ID</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="nts_number" type="nts:nts_number_type">

<xs:annotation>

<xs:documentation>NtS Number</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="validity_period" type="nts:validity_period_type">

<xs:annotation>

<xs:documentation>Overall period of validity</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="fairway_section" type="nts:fairway_section_type">

<xs:annotation>

<xs:documentation>Fairway section — the limitation inside the fairway section cannot be used in the ICEM</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="ice_condition" type="nts:ice_condition_type" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Ice conditions</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<!--

\=========================================

= types used in definition of icem_type =

\=========================================

-->

<xs:complexType name="ice_condition_type">

<xs:sequence>

<xs:element name="measuredate" type="xs:dateTime">

<xs:annotation>

<xs:documentation>Date and Time of measurement or prediction including time zone</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="ice_condition_code" type="nts:ice_condition_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Condition code</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="ice_accessibility_code" type="nts:ice_accessibility_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Accessibility code </xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="ice_classification_code" type="nts:ice_classification_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Classification code </xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="ice_situation_code" type="nts:ice_situation_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Situation code </xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:simpleType name="ice_condition_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="1"/>

<xs:enumeration value="A"/>

<xs:enumeration value="B"/>

<xs:enumeration value="C"/>

<xs:enumeration value="D"/>

<xs:enumeration value="E"/>

<xs:enumeration value="F"/>

<xs:enumeration value="G"/>

<xs:enumeration value="H"/>

<xs:enumeration value="K"/>

<xs:enumeration value="L"/>

<xs:enumeration value="M"/>

<xs:enumeration value="P"/>

<xs:enumeration value="R"/>

<xs:enumeration value="S"/>

<xs:enumeration value="U"/>

<xs:enumeration value="O"/>

<xs:enumeration value="V"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="ice_accessibility_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="1"/>

<xs:enumeration value="A"/>

<xs:enumeration value="B"/>

<xs:enumeration value="F"/>

<xs:enumeration value="L"/>

<xs:enumeration value="C"/>

<xs:enumeration value="D"/>

<xs:enumeration value="E"/>

<xs:enumeration value="G"/>

<xs:enumeration value="H"/>

<xs:enumeration value="M"/>

<xs:enumeration value="K"/>

<xs:enumeration value="T"/>

<xs:enumeration value="P"/>

<xs:enumeration value="V"/>

<xs:enumeration value="X"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="ice_classification_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="1"/>

<xs:enumeration value="A"/>

<xs:enumeration value="B"/>

<xs:enumeration value="C"/>

<xs:enumeration value="D"/>

<xs:enumeration value="E"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="ice_situation_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="3"/>

<xs:enumeration value="NOL"/>

<xs:enumeration value="LIM"/>

<xs:enumeration value="NON"/>

</xs:restriction>

</xs:simpleType>

<!--

\===========================================

= definition of werm_type, =

= used in definition of RIS_Message_Type =

\===========================================

-->

<xs:complexType name="werm_type">

<xs:sequence>

<xs:element name="internal_id" type="nts:internal_id_type" minOccurs="0">

<xs:annotation>

<xs:documentation>Internal ID</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="nts_number" type="nts:nts_number_type" minOccurs="0">

<xs:annotation>

<xs:documentation>NtS Number</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="validity_period" type="nts:validity_period_type">

<xs:annotation>

<xs:documentation>Overall period of validity</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="fairway_section" type="nts:fairway_section_werm_type">

<xs:annotation>

<xs:documentation>Fairway section</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="weather_report" type="nts:weather_report_type" maxOccurs="2">

<xs:annotation>

<xs:documentation>Actual or Forecast report sections</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<!--

\=========================================

= types used in definition of werm_type =

\=========================================

-->

<xs:complexType name="fairway_section_werm_type">

<xs:sequence>

<xs:element name="geo_object" type="nts:geo_object_type">

<xs:annotation>

<xs:documentation>Geo Information of fairway</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:complexType name="weather_report_type">

<xs:sequence>

<xs:element name="measuredate" type="xs:dateTime" minOccurs="0">

<xs:annotation>

<xs:documentation>Date and time of measurement or predicted value including time zone</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="forecast" type="xs:boolean">

<xs:annotation>

<xs:documentation>Forecast (true or 1) OR Actual report (false or 0)</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="weather_class_code" type="nts:weather_class_code_enum" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Classification of weather report</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="weather_item" type="nts:weather_item_type" minOccurs="0" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Weather items</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:simpleType name="weather_class_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="6"/>

<xs:enumeration value="CLR"/>

<xs:enumeration value="CLDY"/>

<xs:enumeration value="OCST"/>

<xs:enumeration value="DZZL"/>

<xs:enumeration value="RAIN"/>

<xs:enumeration value="LRAIN"/>

<xs:enumeration value="ORAIN"/>

<xs:enumeration value="HRAIN"/>

<xs:enumeration value="SLEET"/>

<xs:enumeration value="SNOW"/>

<xs:enumeration value="SNFALL"/>

<xs:enumeration value="HAIL"/>

<xs:enumeration value="SHWRS"/>

<xs:enumeration value="THSTRM"/>

<xs:enumeration value="HAZY"/>

<xs:enumeration value="FOG"/>

<xs:enumeration value="FOGPAT"/>

<xs:enumeration value="GALE"/>

<xs:enumeration value="STRM"/>

<xs:enumeration value="HURRC"/>

<xs:enumeration value="FZRA"/>

</xs:restriction>

</xs:simpleType>

<xs:complexType name="weather_item_type">

<xs:sequence>

<xs:element name="weather_item_code" type="nts:weather_item_code_enum">

<xs:annotation>

<xs:documentation>Weather item type (Wind, Wave etc)</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="value_min" type="xs:float">

<xs:annotation>

<xs:documentation>Actual or Minimum value</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="value_max" type="xs:float" minOccurs="0">

<xs:annotation>

<xs:documentation>Maximum value</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="value_gusts" type="xs:float" minOccurs="0">

<xs:annotation>

<xs:documentation>Gusts value (Wind)</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="unit" type="nts:unit_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Unit of the value</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="weather_category_code" type="nts:weather_category_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Classification of wind report</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="direction_code_min" type="nts:weather_direction_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Direction of wind or wave</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="direction_code_max" type="nts:weather_direction_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Direction of wind or wave</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:simpleType name="weather_item_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="2"/>

<xs:enumeration value="WI"/>

<xs:enumeration value="WA"/>

<xs:enumeration value="FG"/>

<xs:enumeration value="RN"/>

<xs:enumeration value="SN"/>

<xs:enumeration value="AT"/>

<xs:enumeration value="WT"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="weather_category_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="2"/>

<xs:enumeration value="0"/>

<xs:enumeration value="1"/>

<xs:enumeration value="2"/>

<xs:enumeration value="3"/>

<xs:enumeration value="4"/>

<xs:enumeration value="5"/>

<xs:enumeration value="6"/>

<xs:enumeration value="7"/>

<xs:enumeration value="8"/>

<xs:enumeration value="9"/>

<xs:enumeration value="10"/>

<xs:enumeration value="11"/>

<xs:enumeration value="12"/>

<xs:enumeration value="13"/>

<xs:enumeration value="14"/>

<xs:enumeration value="15"/>

<xs:enumeration value="16"/>

<xs:enumeration value="17"/>

<xs:enumeration value="18"/>

<xs:enumeration value="19"/>

<xs:enumeration value="20"/>

<xs:enumeration value="21"/>

<xs:enumeration value="22"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="weather_direction_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="3"/>

<xs:enumeration value="N"/>

<xs:enumeration value="NE"/>

<xs:enumeration value="E"/>

<xs:enumeration value="SE"/>

<xs:enumeration value="S"/>

<xs:enumeration value="SW"/>

<xs:enumeration value="W"/>

<xs:enumeration value="NW"/>

<xs:enumeration value="WRB"/>

</xs:restriction>

</xs:simpleType>

<!--

\=====================================

= types used in several definitions =

\=====================================

-->

<xs:simpleType name="internal_id_type">

<xs:annotation>

<xs:documentation>Internal ID — best practice: global unique identifier</xs:documentation>

</xs:annotation>

<xs:restriction base="xs:string">

<xs:maxLength value="64"/>

</xs:restriction>

</xs:simpleType>

<xs:complexType name="nts_number_type">

<xs:sequence>

<xs:element name="organisation">

<xs:annotation>

<xs:documentation>Name of the publishing organisation (NtS Provider)</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:maxLength value="64"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

<xs:element name="year">

<xs:annotation>

<xs:documentation>Year of first issuing of the notice</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:gYear">

<xs:minInclusive value="1900"/>

<xs:maxInclusive value="9999"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

<xs:element name="number">

<xs:annotation>

<xs:documentation>Number of the notice (per year, starting with: 1, 0 shall not be used for published notices)</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:integer">

<xs:minInclusive value="00000000"/>

<xs:maxInclusive value="99999999"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

<xs:element name="serial_number">

<xs:annotation>

<xs:documentation>Serial number of notice (replacements and withdrawals), original notice: 0</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:integer">

<xs:minInclusive value="00"/>

<xs:maxInclusive value="99"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:complexType name="validity_period_type">

<xs:sequence>

<xs:element name="date_start" type="xs:date">

<xs:annotation>

<xs:documentation>Start date of validity period including time zone</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="date_end" type="xs:date" minOccurs="0">

<xs:annotation>

<xs:documentation>End date of validity period including time zone</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:complexType name="fairway_section_type">

<xs:sequence>

<xs:element name="geo_object" type="nts:geo_object_type">

<xs:annotation>

<xs:documentation>Geo information of fairway</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="limitation" type="nts:limitation_type" minOccurs="0" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Fairway section limitations</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:complexType name="geo_object_type">

<xs:sequence>

<xs:element name="id" type="nts:isrs_code_type" maxOccurs="2">

<xs:annotation>

<xs:documentation>ISRS Location Code of the fairway/object</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="name">

<xs:annotation>

<xs:documentation>Local name of the fairway section</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:maxLength value="256"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

<xs:element name="type_code" type="nts:type_code_enum" default="FWY">

<xs:annotation>

<xs:documentation>Type of geographical object</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="position_code" type="nts:position_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Describes the position related to the fairway</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="coordinate" type="nts:coordinate_type" minOccurs="0" maxOccurs="2">

<xs:annotation>

<xs:documentation>Fairway section begin and end coordinates</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="fairway_name" minOccurs="0">

<xs:annotation>

<xs:documentation>Waterway name (usefull if no RIS Index is available)</xs:documentation>

</xs:annotation>

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:maxLength value="256"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:simpleType name="isrs_code_type">

<xs:annotation>

<xs:documentation>ISRS location code, unique identification of the geo object as defined in RIS Index encoding guide</xs:documentation>

</xs:annotation>

<xs:restriction base="xs:string">

<xs:length value="20"/>

<xs:pattern value="[A-Z]{2}[A-Z]{3}[A-Z0-9]{5}[A-Z0-9]{5}[0-9]{5}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="type_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="3"/>

<xs:enumeration value="RIV"/>

<xs:enumeration value="CAN"/>

<xs:enumeration value="LAK"/>

<xs:enumeration value="FWY"/>

<xs:enumeration value="LCK"/>

<xs:enumeration value="BRI"/>

<xs:enumeration value="RMP"/>

<xs:enumeration value="BAR"/>

<xs:enumeration value="BNK"/>

<xs:enumeration value="GAU"/>

<xs:enumeration value="BUO"/>

<xs:enumeration value="BEA"/>

<xs:enumeration value="ANC"/>

<xs:enumeration value="BER"/>

<xs:enumeration value="MOO"/>

<xs:enumeration value="TER"/>

<xs:enumeration value="HAR"/>

<xs:enumeration value="FDO"/>

<xs:enumeration value="CAB"/>

<xs:enumeration value="FER"/>

<xs:enumeration value="PIP"/>

<xs:enumeration value="PPO"/>

<xs:enumeration value="HFA"/>

<xs:enumeration value="HMO"/>

<xs:enumeration value="SHY"/>

<xs:enumeration value="REF"/>

<xs:enumeration value="MAR"/>

<xs:enumeration value="LIG"/>

<xs:enumeration value="SIG"/>

<xs:enumeration value="TUR"/>

<xs:enumeration value="CBR"/>

<xs:enumeration value="TUN"/>

<xs:enumeration value="BCO"/>

<xs:enumeration value="REP"/>

<xs:enumeration value="FLO"/>

<xs:enumeration value="SLI"/>

<xs:enumeration value="DUK"/>

<xs:enumeration value="VTC"/>

<xs:enumeration value="RES"/>

<xs:enumeration value="LKB"/>

<xs:enumeration value="BRO"/>

<!--the following value is added due to CR 157-->

<xs:enumeration value="BNS"/>

</xs:restriction>

</xs:simpleType>

<xs:complexType name="coordinate_type">

<xs:sequence>

<xs:element name="lat">

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:minLength value="10"/>

<xs:maxLength value="12"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

<xs:element name="long">

<xs:simpleType>

<xs:restriction base="xs:string">

<xs:minLength value="10"/>

<xs:maxLength value="13"/>

</xs:restriction>

</xs:simpleType>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:complexType name="limitation_type">

<xs:sequence>

<xs:element name="limitation_period" type="nts:limitation_period_type" minOccurs="0" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Limitation periods / intervals</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="limitation_code" type="nts:limitation_code_enum">

<xs:annotation>

<xs:documentation>Kind of limitation</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="position_code" type="nts:position_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Describes the position of the limitation related to the fairway</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="value" type="xs:float" minOccurs="0">

<xs:annotation>

<xs:documentation>Value of limitation (i.e. max draught)</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="unit" type="nts:unit_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Unit of the value of the limitation</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="reference_code" type="nts:reference_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Value reference</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="indication_code" type="nts:indication_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Minimum or maximum or reduced by</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="target_group" type="nts:target_group_type" minOccurs="0" maxOccurs="unbounded">

<xs:annotation>

<xs:documentation>Target group information</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:complexType name="limitation_period_type">

<xs:sequence>

<xs:element name="date_start" type="xs:date">

<xs:annotation>

<xs:documentation>Start date of limitation period including time zone</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="date_end" type="xs:date" minOccurs="0">

<xs:annotation>

<xs:documentation>End date of limitation period including time zone</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="time_start" type="xs:time" minOccurs="0">

<xs:annotation>

<xs:documentation>Start time of limitation period without time zone</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="time_end" type="xs:time" minOccurs="0">

<xs:annotation>

<xs:documentation>End time of limitation period without time zone</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="interval_code" type="nts:interval_code_enum" minOccurs="0">

<xs:annotation>

<xs:documentation>Interval for limitation if applicable</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:simpleType name="interval_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="3"/>

<xs:enumeration value="CON"/>

<xs:enumeration value="DAY"/>

<xs:enumeration value="WRK"/>

<xs:enumeration value="WKN"/>

<xs:enumeration value="SUN"/>

<xs:enumeration value="MON"/>

<xs:enumeration value="TUE"/>

<xs:enumeration value="WED"/>

<xs:enumeration value="THU"/>

<xs:enumeration value="FRI"/>

<xs:enumeration value="SAT"/>

<xs:enumeration value="DTI"/>

<xs:enumeration value="NTI"/>

<xs:enumeration value="RVI"/>

<xs:enumeration value="EXC"/>

<xs:enumeration value="WRD"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="limitation_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="6"/>

<xs:enumeration value="OBSTRU"/>

<xs:enumeration value="PAROBS"/>

<xs:enumeration value="DELAY"/>

<xs:enumeration value="VESLEN"/>

<xs:enumeration value="VESHEI"/>

<xs:enumeration value="VESBRE"/>

<xs:enumeration value="VESDRA"/>

<xs:enumeration value="AVALEN"/>

<xs:enumeration value="CLEHEI"/>

<xs:enumeration value="CLEWID"/>

<xs:enumeration value="AVADEP"/>

<xs:enumeration value="NOMOOR"/>

<xs:enumeration value="SERVIC"/>

<xs:enumeration value="NOSERV"/>

<xs:enumeration value="SPEED"/>

<xs:enumeration value="WAVWAS"/>

<xs:enumeration value="PASSIN"/>

<xs:enumeration value="ANCHOR"/>

<xs:enumeration value="OVRTAK"/>

<xs:enumeration value="MINPWR"/>

<xs:enumeration value="ALTER"/>

<xs:enumeration value="CAUTIO"/>

<xs:enumeration value="NOLIM"/>

<xs:enumeration value="TURNIN"/>

<xs:enumeration value="NOSHORE"/>

<xs:enumeration value="CONBRE"/>

<xs:enumeration value="CONLEN"/>

<!-- the following value is added due to CR 128 -->

<xs:enumeration value="LEADEP"/>

<!-- the following value is added due to CR 148 -->

<xs:enumeration value="NOBERT"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="position_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="2"/>

<xs:enumeration value="AL"/>

<xs:enumeration value="LE"/>

<xs:enumeration value="MI"/>

<xs:enumeration value="RI"/>

<xs:enumeration value="LB"/>

<xs:enumeration value="RB"/>

<xs:enumeration value="N"/>

<xs:enumeration value="NE"/>

<xs:enumeration value="E"/>

<xs:enumeration value="SE"/>

<xs:enumeration value="S"/>

<xs:enumeration value="SW"/>

<xs:enumeration value="W"/>

<xs:enumeration value="NW"/>

<xs:enumeration value="BI"/>

<xs:enumeration value="SM"/>

<xs:enumeration value="OL"/>

<xs:enumeration value="EW"/>

<xs:enumeration value="MP"/>

<xs:enumeration value="FP"/>

<xs:enumeration value="VA"/>

<xs:enumeration value="RY"/>

<xs:enumeration value="GY"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="reference_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="4"/>

<xs:enumeration value="NAP"/>

<xs:enumeration value="KP"/>

<xs:enumeration value="FZP"/>

<xs:enumeration value="ADR"/>

<xs:enumeration value="TAW"/>

<xs:enumeration value="PUL"/>

<xs:enumeration value="NGM"/>

<xs:enumeration value="ETRS"/>

<xs:enumeration value="POT"/>

<xs:enumeration value="LDC"/>

<xs:enumeration value="HDC"/>

<xs:enumeration value="ZPG"/>

<xs:enumeration value="GLW"/>

<xs:enumeration value="HSW"/>

<xs:enumeration value="LNW"/>

<xs:enumeration value="HNW"/>

<xs:enumeration value="IGN"/>

<xs:enumeration value="WGS"/>

<xs:enumeration value="RN"/>

<xs:enumeration value="HBO"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="indication_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="3"/>

<xs:enumeration value="MAX"/>

<xs:enumeration value="MIN"/>

<xs:enumeration value="RED"/>

</xs:restriction>

</xs:simpleType>

<xs:complexType name="target_group_type">

<xs:sequence>

<xs:element name="target_group_code" type="nts:target_group_code_enum" default="ALL">

<xs:annotation>

<xs:documentation>Target group (vessel type)</xs:documentation>

</xs:annotation>

</xs:element>

<xs:element name="direction_code" type="nts:direction_code_enum" default="ALL">

<xs:annotation>

<xs:documentation>Upstream or downstream traffic, or both</xs:documentation>

</xs:annotation>

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:simpleType name="target_group_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="3"/>

<xs:enumeration value="ALL"/>

<xs:enumeration value="CDG"/>

<xs:enumeration value="COM"/>

<xs:enumeration value="PAX"/>

<xs:enumeration value="PLE"/>

<xs:enumeration value="CNV"/>

<xs:enumeration value="PUS"/>

<xs:enumeration value="NNU"/>

<xs:enumeration value="LOA"/>

<xs:enumeration value="SMA"/>

<xs:enumeration value="CND"/>

<xs:enumeration value="WOC"/>

<xs:enumeration value="MOV"/>

<xs:enumeration value="NMV"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="direction_code_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="3"/>

<xs:enumeration value="ALL"/>

<xs:enumeration value="UPS"/>

<xs:enumeration value="DWN"/>

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="unit_enum">

<xs:restriction base="xs:string">

<xs:maxLength value="4"/>

<xs:enumeration value="cm"/>

<xs:enumeration value="m3/s"/>

<xs:enumeration value="h"/>

<xs:enumeration value="km/h"/>

<xs:enumeration value="kW"/>

<xs:enumeration value="m/s"/>

<xs:enumeration value="mm/h"/>

<xs:enumeration value="°C"/>

</xs:restriction>

</xs:simpleType>

</xs:schema>
