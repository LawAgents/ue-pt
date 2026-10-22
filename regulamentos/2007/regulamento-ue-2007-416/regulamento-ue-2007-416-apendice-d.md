---
id: "regulamento-ue-2007-416-apendice-d"
celex: "32007R0416"
title: "Regulamento (CE) n. o 416/2007 da Comissão, de 22 de Março de 2007 , relativo às especificações técnicas dos avisos à navegação a que se refere o artigo 5. o da Directiva 2005/44/CE do Parlamento Europeu e do Conselho relativa a serviços de informação fluvial (RIS) harmonizados nas vias navegáveis interiores da Comunidade — Apêndice D"
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
part: "Apêndice D"
---

# Regulamento (CE) n. o 416/2007 da Comissão, de 22 de Março de 2007 , relativo às especificações técnicas dos avisos à navegação a que se refere o artigo 5. o da Directiva 2005/44/CE do Parlamento Europeu e do Conselho relativa a serviços de informação fluvial (RIS) harmonizados nas vias navegáveis interiores da Comunidade — Apêndice D

## Apêndice D

<?xml version="1.0" encoding="UTF-8"?>

<wsdl:definitions

xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"

xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"

xmlns:http=

"http://schemas.xmlsoap.org/wsdl/http/"

xmlns:xs=

"http://www.w3.org/2001/XMLSchema"

xmlns:soapenc=

"http://schemas.xmlsoap.org/soap/encoding/"

xmlns:mime=

"http://schemas.xmlsoap.org/wsdl/mime/"

xmlns:nts=

"http://www.ris.eu/nts/4.0.4.0"

xmlns:tns=

"http://www.ris.eu/nts.ms/2.0.4.0"

targetNamespace=

"http://www.ris.eu/nts.ms/2.0.4.0"

name="NtS-Message-Service">

<!--

= specification of types =

-->

<wsdl:types>

<!--

= xml-schema for types =

-->

<xs:schema

targetNamespace="http://www.ris.eu/nts.ms/2.0.4.0"

xmlns:xs="http://www.w3.org/2001/XMLSchema"

xmlns:nts=

"http://www.ris.eu/nts/4.0.4.0"

xmlns:nts-ms=

"http://www.ris.eu/nts.ms/2.0.4.0"

elementFormDefault="qualified"

attributeFormDefault="unqualified"

version="2.0.4.0">

<!-- import NtS schema -->

<xs:import

namespace="http://www.ris.eu/nts/4.0.4.0"

schemaLocation="http://

www.ris.eu/nts/4.0/NtS_XSD_V.4.0.4.0.xsd"

/>

<!-- query with filters, parameters according to the NtS standard -->

<xs:element name="get_messages_query">

<xs:complexType>

<xs:sequence>

<!-- type of message (FTM, WRM, ICEM, WERM) -->

<xs:element name="message_type" type="nts-ms:message_type_type"/>

<!-- ISRS codes for fairway sections or objects -->

<xs:element name="ids" type="nts-ms:id_pair" minOccurs="0" maxOccurs="unbounded"/>

<!-- time of validity -->

<xs:element name="validity_period" type="nts:validity period type"

minOccurs="0"/>

<!-- date of publication of the notice -->

<xs:element name="dates_issue" type="nts-ms:date_pair" minOccurs="0" maxOccurs="unbounded"/>

<!-- optional parameter for paging mechanism -->

<xs:element name="paging_request" type="nts-ms:paging_request_type" minOccurs="0"/>

</xs:sequence>

</xs:complexType>

</xs:element>

<!-- result to query — can contain

— "nts:RIS_MessageType", arbitrary number, defined in the NtS-xsd (see www.ris.eu)

— "nts-ms:error_code_type", arbitrary number, defined in this schema

— "nts-ms:paging_result_type", optional, defined in this schema -->

<xs:element name="get_messages_result">

<xs:complexType>

<xs:sequence>

<xs:element name="result_message" type="nts:RIS_Message_Type" minOccurs= "0" maxOccurs="unbounded"/>

<xs:element name="result_error" type="nts-ms:error_code_type" minOccurs= "0" maxOccurs="unbounded"/>

<xs:element name="paging_result" type="nts-ms:paging_result_type" minOccurs="0"/>

</xs:sequence>

</xs:complexType>

</xs:element>

<!-- type definitions used in request -->

<xs:simpleType name="message_type_type">

<xs:restriction base="xs:string">

<xs:enumeration value="FTM"/>

<xs:enumeration value="WRM"/>

<xs:enumeration value="ICEM"/>

<xs:enumeration value="WERM"/>

</xs:restriction>

</xs:simpleType>

<xs:complexType name="id_pair">

<xs:sequence>

<xs:element name="id" type="nts:isrs_code_type" minOccurs="1" maxOccurs="2" />

</xs:sequence>

</xs:complexType>

<xs:complexType name="date_pair">

<xs:sequence>

<xs:element name="date_start" type="xs:date"/>

<xs:element name="date_end" type="xs:date" minOccurs="0"/>

</xs:sequence>

</xs:complexType>

<xs:complexType name="paging_request_type">

<xs:sequence>

<xs:element name="offset" type="xs:nonNegativeInteger"/>

<xs:element name="limit" type="xs:nonNegativeInteger"/>

<xs:element name="total_count" type="xs:boolean"/>

</xs:sequence>

</xs:complexType>

<!-- type definitions used in response -->

<xs:simpleType name="error_code_type">

<xs:restriction base="xs:string">

<xs:enumeration value="e010">

<xs:annotation>

<xs:documentation>Description: message type not supported, Explanation: web service does not support the requested message type</xs:documentation>

</xs:annotation>

</xs:enumeration>

<xs:enumeration value="e030">

<xs:annotation>

<xs:documentation>Description: paging parameters inconsistent with messages, Explanation: parameters for paging mechanism do not fit the available messages, e.g. Offset >= Total Count</xs:documentation>

</xs:annotation>

</xs:enumeration>

<xs:enumeration value="e100">

<xs:annotation>

<xs:documentation>Description: syntax error in request, Explanation: request violates the schema for requests</xs:documentation>

</xs:annotation>

</xs:enumeration>

<xs:enumeration value="e110">

<xs:annotation>

<xs:documentation>Description: incorrect message type, Explanation: given message type is not known</xs:documentation>

</xs:annotation>

</xs:enumeration>

<xs:enumeration value="e120">

<xs:annotation>

<xs:documentation>Description: incorrect type-specific parameters, Explanation: type-specific parameters are erroneous</xs:documentation>

</xs:annotation>

</xs:enumeration>

<xs:enumeration value="e130">

<xs:annotation>

<xs:documentation>Description: incorrect paging parameters, Explanation: given parameters for the paging mechanism are erroneous</xs:documentation>

</xs:annotation>

</xs:enumeration>

<xs:enumeration value="e200">

<xs:annotation>

<xs:documentation>Description: operation not known, Explanation: the requested operation is unknown</xs:documentation>

</xs:annotation>

</xs:enumeration>

<xs:enumeration value="e300">

<xs:annotation>

<xs:documentation>Description: data source unavailable, Explanation: data source of the web service for the NtS data is temporarily unavailable</xs:documentation>

</xs:annotation>

</xs:enumeration>

<xs:enumeration value="e310">

<xs:annotation>

<xs:documentation>Description: too many results for request, Explanation: server is unable to handle number of results</xs:documentation>

</xs:annotation>

</xs:enumeration>

</xs:restriction>

</xs:simpleType>

<xs:complexType name="paging_result_type">

<xs:sequence>

<xs:element name="offset" type="xs:nonNegativeInteger"/>

<xs:element name="count" type="xs:nonNegativeInteger"/>

<xs:element name="total_count" type="xs:nonNegativeInteger" minOccurs="0"/>

</xs:sequence>

</xs:complexType>

</xs:schema>

</wsdl:types>

<!--

= specification of messages =

-->

<wsdl:message name="get_messages_request">

<wsdl:part name="parameters" element="tns:get_messages_query"/>

</wsdl:message>

<wsdl:message name="get_messages_response">

<wsdl:part name="parameters" element="tns:get_messages_result"/>

</wsdl:message>

<!--

= specification of port type =

-->

<wsdl:portType name="NtS_message_service">

<wsdl:operation name="get_messages">

<wsdl:input message="tns:get_messages_request"/>

<wsdl:output message="tns:get_messages_response"/>

</wsdl:operation>

</wsdl:portType>

<!--

= specification of binding =

-->

<wsdl:binding name="NtS_message_service_soap_binding" type="tns:NtS_message_service">

<soap:binding style="document" transport=

"http://schemas.xmlsoap.org/soap/http"

/>

<wsdl:operation name="get_messages">

<soap:operation soapAction=

"http://www.ris.eu/nts.ms/get_messages"

/>

<wsdl:input>

<soap:body use="literal"/>

</wsdl:input>

<wsdl:output>

<soap:body use="literal"/>

</wsdl:output>

</wsdl:operation>

</wsdl:binding>

<!--

= specification of service =

-->

<wsdl:service name="NtS_message_service_service">

<wsdl:port name="NtS_message_service" binding="tns:NtS_message_service_soap_binding">

<soap: address location=

"http://nts-ms.example.org/NtS_message_service"

/>

</wsdl:port>

</wsdl:service>

</wsdl:definitions>

**TAGS**

| RIS_message | NtS message | NtS съобщение | Mensaje NtS | Zpráva NtS | NtS-meddelelse | NtS Nachricht | NtS teade | Mήνυμα NtS (Σύστ. Πληρ. Εσ. Ναυσ.) | Message NtS | NtS poruka | messaggio NtS | NtS ziņojums | NtS pranešimas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Identification | Identification section | Идентификационен раздел | Sección de identificación | Identifikační úsek | Identifikationsrubrik | Identifikationsabschnitt | Identifitseerimise jaotis | Τμήμα αναγνώρισης | Identification | Identifikacijski dio | identificazione del tratto | Identifikācija | Identifikavimas |
| From | Sender of the message | Подател | Remitente | Odesilatel | Afsender | Absender | Teate saatja | Αποστολέας του μηνύματος | Expéditeur du message | Pošiljatelj | mittente del messaggio | Nosūtītājs | Pranešimo siuntėjas |
| Originator | Originator of the information | Автор на информацията | Origen de la información | Autor zprávy | Informationskilde | Urheber der Nachricht | Teavitaja | Προέλευση των πληροφοριών | Origine de l’information | Izvor informacija | origine dell'informazione | Informācijas autors | Informacijos pateikėjas |
| Country_code | Country where message is valid | Държава, в която е валидно съобщението | País en que el mensaje es válido | Dotčená země | Berørt land | Betroffenes Land | Riik, kus teade kehtib | Χώρα ισχύος του μηνύματος | Pays où le message est valide | Država gdje poruka vrijedi | Stato interessato | Ziņojuma valsts | Šalis, kurioje galioja pranešimas |
| Language_code | Original language | Оригинален език | Lengua original | Originální jazyk | Originalsprog | Originalsprache | Algkeel | Πρωτότυπη γλώσσα | Langue d'origine | Originalni jezik | lingua originale | Ziņojuma valoda | Originalo kalba |
| District | District/region within country | Регион от държавата | Región del país | Dotčená oblast v zemi | Berørt region/område | Betroffenes Gebiet im Land | Riigi piirkond | Περιοχή/περιφέρεια χώρας | Région | Područje unutar države | area/regione interessata | Rajons/ valsts reģions | Rajonas / regionas šalyje |
| Date_issue | Date of issue | Дата на издаване | Fecha de emisión | Datum vydání | Offentliggørelsesdato | Herausgabedatum | Väljaandmise kuupäev | Ημερομηνία έκδοσης | Date de publication | Datum izdavanja | data di emissione | Sastādīšanas datums | Išdavimo data |
| Time_issue | Time of issue | Час на издаване | Hora de emisión | Čas vydání | Offentliggørelsestidspunkt | Herausgabezeit | Väljaandmise kellaaeg | Ώρα έκδοσης | Heure de publication | Vrijeme izdavanja | orario di emissione | Sastādīšanas laiks | Išdavimo laikas |
| Ftm | Fairway and traffic related message | Известие до корабоводителите | Mensaje sobre vía navegable y tráfico | Zpráva týkající se vodních cest a provozu | Farvands- og trafikrelaterede meddelelser | Wasserstraßen- und verkehrsbezogene Nachricht | Teated faaravaatri ja liikluse kohta | Μήνυμα σχετικά με δίαυλο και κυκλοφορία | Message lié à la voie d’eau et au trafic | Priopćenje brodarstvu | messaggio relativo a canale navigabile e traffico | Ziņojums par kuģu ceļu un satiksmi | Su farvateriu ir laivų eismu susijęs pranešimas |
| NtS_number | Number section | Номер на секция | Número de la sección | Číslo sekce | Nummerrubrik | Nummerierungsabschnitt | Numbri osa | Tμήμα αρίθμησης | Numéro | Odjeljak za broj poruke | numero del tratto | Numuru sadaļa | Numeris |
| Organisation | Publishing organisation | Издаваща организация | Organización que publica el mensaje | Vydávající organizace | Offentliggørende organisation | Herausgebende Organisation | Väljaandev organisatsioon | Οργανισμός έκδοσης | Entité émettrice | Organizacija | organizzazione emittente | Publicējošā organizācija | Skelbianti organizacija |
| Year | Year | Година | Año | Rok | År | Jahr | Aasta | Έτος | Année | Godina | anno | Gads | Metai |
| Number | Number (of the notice) | Номер | Número (del aviso) | Číslo zprávy | (Meddelelsens) nr. | Nummer (der Nachricht) | (Teatise) number | Αριθμός (μηνύματος) | Numéro (de l'avis) | Broj (poruke) | numero (dell'avviso) | (Ziņojuma) numurs | Numeris (pranešimo) |
| Serial_number | Serialnumber | Сериен номер | Número de serie | Číslo verze | Serienummer | Versionsnummer | Seerianumber | Αύξων αριθμός | Numéro de série | Serijski broj | numero progressivo | Sērijas numurs | Serijos numeris |
| Target_group | Information about target group | Информация за група получатели | Información sobre el usuario destinatario | Cílová skupina | Målgruppe — strækning | Information zur Zielgruppe | Sihtrühma jaotis | Τμήμα στοχευόμενης ομάδας | Type d'usagers concernés | Ciljana skupina | gruppo destinatario | Mērķgrupa | Tikslinė grupė |
| Target_group_code | Target group | Код на групата получатели | Código usuario destinatario | Kód cílové skupiny | Kode for målgruppe | Zielgruppe | Sihtrühma kood | Κωδικός στοχευόμενης ομάδας | Code usagers concernés | Oznaka ciljane skupine | codice gruppo destinatario | Mērķgrupas kods | Tikslinės grupės kodas |
| Direction_code | Affected direction | Код за направление | Dirección tráfico | Směr | Kode for sejlretning | Betroffene Richtung | Sõidusuuna kood | Κωδικός κατεύθυνσης κυκλοφορίας | Sens de parcours | Oznaka smjera prometa | codice direzione traffico | Satiksmes virziena kods | Eismo krypties kodas |
| Subject_code | Subject | Тема | Asunto | Předmět | Emne | Betrifft | Teema | Θέμα | Sujets de l'avis | Predmet | codice oggetto | Ziņojuma temats | Tema |
| Validity_period | Period of validity | Срок на валидност | Período de validez | Doba platnosti | Gyldighedsperiode | Gültigkeitszeitraum | Kehtivusaeg | Περίοδος ισχύος | Période de validité | Rok valjanosti | periodo di validità | Derīguma termiņš | Galiojimo laikas |
| Date_start | From | От дата | De | Od | Startdato | Ab | Alates | Από | Date de début | Od | da (aaaammgg) | No | Nuo |
| Date_end | Until | До дата | Α | Do | Slutdato | Bis | Kuni | Έως | Date de fin | Do | fino a (aaaammgg) | Līdz | Iki |
| Contents | Additional information | Съдържание | Contenido | Text | Indhold | Ergänzende Informationen | Sisu | Περιεχόμενα | Contenu | Sadržaj | testo | Saturs | Turinys |
| Source | Notice source (authority) | Официален източник на известието | Fuente del aviso (autoridad) | Vydavatel zprávy | Infokilde (myndighed) | Herausgeber der Nachricht | Teatise allikas (ametiasutus) | Προέλευση μηνύματος (Αρχή) | Source | Izvor priopćenja | fonte dell'avviso (autorità) | Informācijas avots (iestāde) | Pranešimo šaltinis (institucija) |
| Reason_code | Reason of notice | Причина за известието | Motivo del aviso | Důvod zprávy | Årsag til meddelelse | Grund der Nachricht | Teatise põhjus | Αιτία μηνύματος | Evènement | Razlog priopćenja | motivazione | Ziņojuma iemesls | Pranešimo paskirtis |
| Communication | Communication information | Информация за комуникация | Sección comunicación | Informace o komunikačním kanále | Kommunikationsdel | Information zu Kommunikationswegen | Teabevahetuse jaotis | Τμήμα επικοινωνίας | Canal d'information | Informacije o komunikacijskom kanalu | comunicazione | Paziņojums | Ryšio kanalas |
| Reporting_code | Reporting regime | Режим за известяване | Régimen de notificación | Režim hlášení | Rapporteringskanal | Meldungsart | Aruandluse kord | Καθεστώς αναφοράς | Obligation de s'annoncer | Režim javljanja | regime di segnalazione | Paziņojuma veids | Pranešimo režimas |
| Communication_code | Means of communication | Средство за свръзка | Medio de comunicación | Prostředky komunikace | Kommunikationsmiddel | Kommunikationsweg | Sidevahendid | Μέσο επικοινωνίας | Moyen de communication | Sredstvo komunikacije | mezzo di comunicazione | Saziņas līdzekļi | Ryšio priemonės |
| Number (Communication section) | Number or address | Номер или адрес | Número o dirección | Číslo nebo adresa | Nr. eller adresse | Nummer oder Adresse | Number või aadress | Αριθμός ή διεύθυνση | Numéro ou adresse | Broj ili adresa | numero o indirizzo | Numurs vai adrese | Numeris arba adresas |
| Fairway_section | Waterway or waterway section | Плавателен воден път или негов участък | Vía navegable o tramo | Úsek vodní cesty | Vandvejs- eller farvandsstrækning | Wasserstraße oder -abschnitt | Veetee või faarvaatri jaotis | Τμήμα πλωτής οδού ή διαύλου | Voie ou section de voie | Dionica vodnog ili plovnog puta | tratto idrovia o canale navigabile | Ūdensceļš vai kuģu ceļš | Vandens kelias arba vandens kelio ruožas |
| Geo_object | Location | Географска информация за водния път или обекта | Ubicación | Geografické informace o vodní cestě nebo objektu | Position | Geoinformation | Geo-teave veetee või objekti kohta | Γεωγραφικές πληροφορίες πλωτής οδού ή αντικειμένου | Objet géo-référencé | Geografske informacije o vodnom putu ili objektu | definizione geografica dell'idrovia o dell'oggetto | Ģeogrāfiskā informācija par ūdensceļu vai objektu | Geografinė informacija apie vandens kelią arba objektą |
| Id (Geo_Object section) | ISRS Location Code | Идентификация (на географския обект) | Código de posición ISRS | Identifikace | ISRS Location Code | ISRS Location Code | Identifitseerimine | Στοιχεία αναγνώρισης | Identifiant | Identifikacija | identificativo oggetto geografico | Identifikācija | Identifikavimo kodas |
| Name (Geo_Object section) | Name of object | Наименование на географския обект | Denominación de objeto geográfico | Název geografického objektu | Navn på objekt | Name | Geo-objekti nimi | Ονομασία γεωγραφικού αντικειμένου | Toponyme | Ime geo objekta | denominazione dell'oggetto geografico | Ģeogrāfiskā objekta nosaukums | Geografinio objekto pavadinimas |
| Type_code (Geo_Object section) | Type | Тип на географския обект | Tipo de vía navegable | Typ objektu | Type | Objekttyp | Veetee tüüp | Τύπος πλωτής οδού | Type | Vrsta objekta | tipo di idrovia | Ūdensceļa veids | Vandens kelio tipas |
| Coordinate | Coordinates | Координати на началото и края на участъка от фарватера | Coordenadas | Souřadnice počátečních a koncových bodů | Koordinater | Koordinaten | Faarvaatri algus- ja lõppkoordinaadid | Γεωγραφικές συντεταγμένες αρχής και τέλους διαύλου | Coordonnées | Koordinate početka i kraja plovnog puta | coordinate dei punti di delimitazione del tratto navigabile | Kuģu ceļa sākuma un beigu koordinātas | Farvaterio pradžios ir pabaigos koordinatės |
| Lat (Coordinate) | Latitude | Географска ширина (в десетична стойност) | Latitud | Zeměpisná šířka (desetinné číslo) | Breddegrad | Breitengrad | Laiuskraad (kümnendmurd) | Γεωγραφικό πλάτος (δεκαδικά) | Latitude (décimale) | Geografska širina (decimalno) | latitudine (decimali) | Platums (decimāldaļskaitlis) | Platuma (dešimtųjų tikslumu) |
| Long (Coordinate) | Longitude | Географска дължина (в десетична стойност) | Longitud | Zeměpisná délka (desetinné číslo) | Længdegrad | Längengrad | Pikkuskraad (kümnendmurd) | Γεωγραφικό μήκος (δεκαδικά) | Longitude (décimale) | Geografska dužina (decimalno) | longitudine (decimali) | Garums (decimāldaļskaitlis) | Ilguma (dešimtųjų tikslumu) |
| Limitation | Limitation | Раздел за ограничения | Limitación | Druh omezení | Begrænsning | Einschränkung | Piirangu jaotis | Τμήμα περιορισμών | Restriction | Ograničenja | limitazione | Ierobežojums | Apribojimo būdas |
| Limitation_period | (Limitation) periods/intervals | Срок на действие на ограничението | (Limitación) períodos /intervalos | (omezení) období/interval | (Begrænsning) perioder/tidsintervaller | Zeitliche Gültigkeit der Einschränkung | (Piirangu) perioodid/intervallid | (Περιορισμοί) περίοδοι/διαστήματα | Période de restriction | Trajanje (ograničenja) | durata della limitazione | (Ierobežojuma) darbības laiks/ intervāli | (Apribojimo) laikotarpis / intervalas |
| Date_start (Limitation_period) | From | От дата | De | Od | Fra | Ab | Alates | Από | Date de début | Od | da (aaaammgg) | No | Nuo |
| Date_end (Limitation_period) | Until | До дата | A | Do | Til | Bis | Kuni | Έως | Date de fin | Do | fino a (aaaammgg) | Līdz | Iki |
| Time_start (Limitation_period) | From (hh:mm) | От час (ччмм) | De (hhmm) | Od (hhmm) | Fra kl. (tt:mm) | Ab (hh:mm) | Alates (ttmm) | Από (ωωλλ) | Heure de début (hh:mm) | Od (hh:mm) | dalle (hhmm) | No (hhmm) | Nuo (hh:mm) |
| Time_end (Limitation_period) | Until (hh:mm) | До час (ччмм) | A (hhmm) | Do (hhmm) | Til kl. (tt:mm) | Bis (hh:mm) | Kuni (ttmm) | Έως (ωωλλ) | Heure de fin (hh:mm) | Do (hh:mm) | alle (hhmm) | Līdz (hhmm) | Iki (hh:mm) |
| Interval_code (Limitation_period) | Interval | Интервал | Intervalo | Interval | Interval | Intervall | Intervall | Συχνότητα | Périodicité | Interval | periodicità | Intervāls | Intervalas |
| Limitation_code | Kind of limitation | Вид на ограничението | Tipo de limitación | Druh omezení | Begrænsningens art | Art der Einschränkung | Piirangu liik | Είδος περιορισμών | Code de la restriction | Vrsta ograničenja | tipo di limitazione | Ierobežojuma veids | Apribojimo rūšis |
| Position_code | Position | Позиция | Posición | Poloha (omezení) | Position | Lage | (Piirangu) positsioon | Στίγμα των περιορισμών | Position | Pozicija (ograničenja) | localizzazione (della limitazione) | (Ierobežojuma) pozīcija | (Apribojimo) pozicija |
| Value | Numerical value | Числова стойност | Valor numérico | Číselný hodnota (omezení) | Numerisk værdi | Zahlenwert | (Piirangu) arvväärtus | Αριθμητική τιμή (περιορισμών) | Valeur | Brojčana vrijednost (ograničenja) | attributo numerico (della limitazione) | (Ierobežojuma) skaitliskā vērtība | (Apribojimo) skaitinė vertė |
| Unit | Unit | Мерна единица | Unidad | Jednotka | Enhed | Einheit | Ühik | Μονάδα | Unité | Jedinica | unità di misura | Mērvienība | Vienetai |
| Fairway_name | Waterway | Име на воден път | Vía navegable | Vodní cesta | Vandvej | Wasserstraße | Veetee | Ονομασία της πλωτής οδού | Nom de la voie d’eau | Plovni put | via navigabile | Ūdensceļš | Vandens kelias |
| Reference_code | Value reference | Код за справка | Referencia | Jednotka | Referenceværdi | Bezugssystem | Väärtuse viide | Τιμή αναφοράς | Référentiel de la valeur | Referentna vrijednost | parametro di riferimento | Atsauces vērtība | Atskaitos sistema |
| Indication_code | Indication of limitation | Означение за ограничение | Indicación de limitación | Indikace omezení | Angivelse af begrænsning | Hinweis zum Einschränkungswert | Märge piirangu kohta | Ένδειξη περιορισμών | Indication de la restriction | Oznaka ograničenja | indicazione del valore di limitazione | Ierobežojuma norāde | Apribojimo rodmenys |
| Object | Object | Обект | Objeto | Objekt | Objekt | Objekt | Objekt | Αντικείμενο | Objet | Objekt | oggetto | Objekts | Objektas |
| Geo_object section for an Object | Location | Географска информация за обекта | Ubicación | Geografická informace o objektu | Position | Geografische Definition des Objekts | Objekti geo-teave | Γεωγραφικές πληροφορίες αντικειμένου | Géo-Objet de référence pour l'objet | Geografske informacije o objektu | oggetto — informazione geografica | Ģeogrāfiskā informācija par objektu | Objekto geografinė informacija |
| Type_code (Geo_object section) | Type of object | Тип на обекта | Tipo objeto | Typ objektu | Objekttype | Objekttyp | Objekti liik | Τύπος αντικειμένου | Type | Vrsta objekta | tipo di oggetto | Objekta tips | Objekto tipas |
| Coordinate (Geo_object section) | Object coordinates | Координати на географския обект | Coordenadas objeto | Souřadnice objektu | Objektets koordinater | Koordinaten des Objekts | Objekti koordinaadid | Γεωγραφικές συντεταγμένες αντικειμένου | Coordonnées * | Koordinate objekta | coordinate dell'oggetto | Objekta koordinātas | Objekto koordinatės |
| Wrm | Water related message | Съобщения за нивото на водата | Mensaje relativo al agua | Hlášení o vodním stavu | Vandstandsrelateret meddelelse | Wasserstandsmeldung | Teade veeolude kohta | Μήνυμα όσον αφορά τα ύδατα | Message de niveau d'eau | Poruka o stanju vodostaja | messaggio riguardante le acque | Informācija par ūdens līmeni | Informacija apie vandens lygį |
| Measure | Measurements (normal or predicted) | Измерени стойности (типични или прогнозни) | Medidas (reales o previstas) | Měření (normální nebo předpovědní) | Målingens art (målt eller prognose) | Messwerte bzw. Prognosewerte | Mõõtmised (tavapärased või prognoositavad) | Μετρήσεις (κανονικές ή προβλεπόμενες) | Mesures (réelles ou prévues) | Mjerenja (izmjerena ili prognozirana) | livello idrometrico (normale o previsto) | Mērījumu veids (normālais vai prognozētais) | Vandens lygio vertės (įprastos arba numatomos) |
| Predicted | Prediction | Прогноза | Previsión | Předpověď | Prognose | Vorhersage | Eeldus | Πρόβλεψη | prévu | Prognoza | previsione | Prognoze | Prognozė |
| Measure_code | Kind of water related information | Тип на измерванията на водата | Tipo de información relativa al agua | Druh hlášení o vodním stavu | Art vandstandsoplysning | Art der Wasserstandsmeldung | Veeolusid käsitleva teate liik | Πληροφορίες όσον αφορά το είδος των υδάτων | Code de la mesure | Vrsta informacije o vodostaju | tipo di informazione idrometrica | Veids informācijai par ūdens līmeni | Pranešimo apie vandens lygį rūšis |
| Difference | Difference to previous value | Разлика спрямо предишна стойност | Diferencia con respecto al valor anterior | Rozdíl vůči předcházející hodnotě | Ændring i forhold til forrige | Abweichung zum vorherigen Wert | Erinevus | Διαφορά | Différence | Razlika | differenza | Starpība | Skirtumas |
| Value_difference | value difference to comparative measurement | Разлика в стойността спрямо сравнителното измерване | Diferencia de valor con respecto a la medida comparativa | Rozdíl vůči porovnávacímu měření | Værdiforskel i forhold til komparativ måling | Differenz zur Vergleichsmessung | Väärtuse erinevus võrdlusmõõdust | Διαφορά τιμής ως προς συγκριτική μέτρηση | Différence de valeur | Razlika u vrijednosti | differenza di valore in seguito a misurazione comparativa | Salīdzinošā mērījuma vērtību starpība | lyginamojo matavimo verčių skirtumas |
| Time_difference | time difference to comparative measurement | Разлика във времето спрямо сравнително измерване | Diferencia de tiempo con respecto a la medida comparativa | Časový rozdíl vůči porovnávacímu měření | Tidsforskel i forhold til komparativ måling | Zeitdifferenz zur Vergleichsmessung | Aja erinevus võrdlusmõõdust | Χρονική διαφορά ως προς συγκριτική μέτρηση | Différence de temps | Razlika u vremenu | differenza di tempo in seguito a misurazione comparativa | Salīdzinošā mērījuma laika starpība | lyginamojo matavimo laiko skirtumas |
| Barrage_code | Barrage | Бараж | Presa | Jez | Dæmning | Wehrstellung | Pais | Υδατοφράκτης | Barrage | Pregrada | sbarramento | Aizsprosts | Užtvara |
| Regime_code | Water regime | Воден режим | Régimen | Odtokový režim | Vandregime | Abflussregime | Veerežiim | Ροή υδάτων | Débit | Režim vodnog toka | regime idrico | Ūdens režīms | Vandens režimas |
| Measuredate | Measuredate | Дата на измерване | Fecha de medición | Datum měření | Dato for målingen | Messdatum | Mõõtmise kuupäev | Ημερομηνία μέτρησης | Date de mesure | Datum mjerenja | data del rilievo | Mērījuma datums | Matavimo data |
| Measuretime | Measuretime | Час на измерване | Hora de medición | Čas měření | Tidspunkt for målingen | Messzeit | Mõõtmise kellaaeg | Ώρα μέτρησης | Heure de mesure | Vrijeme mjerenja | orario del rilievo | Mērījuma laiks | Matavimo laikas |
| Icem | Ice message | Съобщения във връзка с ледохода | Mensaje hielo | Zpráva týkající se ledových jevů | Ismelding | Eismeldung | Teade jää kohta | Μήνυμα σχηματισμού πάγου | Message concernant la glace | Poruka o ledu | messaggio relativo alla presenza di ghiaccio | Ziņojums par ledu | Pranešimas apie ledą |
| Ice_condition | Ice condition on fairway | Състояние на леда | Estado hielo en vía navegable | Ledové podmínky | Isforhold for farvand | Eisverhältnisse im Fahrwasser | Jää seisund | Συνθήκες πάγου | Condition de glace | Stanje leda | condizione del ghiaccio sul canale navigabile | Ledus apstākļi | Ledo sąlygos farvateryje |
| Ice_condition_code | Ice condition | Код за състоянието на леда | Estado hielo | Ledové podmínky | Isforhold | Eisbeschaffenheit | Jää seisund | Συνθήκες πάγου | Condition de glace | Stanje leda | condizione del ghiaccio | Ledus apstākļi | Ledo sąlygos |
| Ice_accessibility_code | Accessibility | Условия за корабоплаване при наличие на ледоход | Accesibilidad | Splavnost | Farbarhed | Befahrbarkeit | Juurdepääsetavus | Προσβασιμότητα | Accessibilité | Plovnost | accessibilità | Pieejamība | Tinkamumas laivybai |
| Ice_classification_code | Ice classification | Класификация (описание) на леда | Clasificación hielo | Klasifikace ledu | Isklasse | Eisklasse | Jää klassifitseerimine | Ταξινόμηση πάγου | Classification de la glace | Klasifikacija leda | tipo di ghiaccio | Ledus klasifikācija | Ledo tipas |
| Ice_situation_code | Ice situation | Ледова обстановка | Situación hielo | Situace týkající se ledu | Issituation | Eissituation | Jää olukord | Κατάσταση πάγου | Limitations dues à la glace | Stanje leda | stato del ghiaccio | Ledus stāvoklis | Ledo būklė |
| Werm | Weather message | Съобщения за метеорологичната обстановка | Mensaje sobre condiciones meteorológicas | Zpráva o počasí | Vejrmeddelelse | Wettermeldung | Ilmasõnum | Μετεωρολογικό μήνυμα | Message météo | Vremenska poruka | messaggio meteorologico | Laikapstākļu ziņojums | Meteorologinis pranešimas |
| Weather_report | Weather report | Доклад за метеорологичната обстановка | Informe meteorológico | Stav počasí | Vejrrapport | Wetterbericht | Ilmateade | Μετεωρολογικό δελτίο | Bulletin météo | Vremenski izvještaj | bollettino meteorologico | Laikapstākļu pārskats | Meteorologinė suvestinė |
| Forecast | Forecast | Прогноза | Previsión | Předpověď | Forudsigelse | Vorhersage | Prognoos | Πρόγνωση | Prévision | Prognoza | previsioni meteorologiche | Prognoze | Prognozė |
| Weather_class_code | Weather classification | Класификация за метеорологичната обстановка | Clasificación de las condiciones meteorológicas | Klasifikace počasí | Vejrklassificering | Wetterklassifizierung | Ilma klassifitseerimine | Ταξινόμηση καιρού | Classification de la météo | Klasifikacija vremena | classificazione meteorologica | Laikapstākļu klasifikācija | Oro sąlygų kodas |
| Weather_item | Weather information | Информация за метеорологичната обстановка | Información de las condiciones meteorológicas | Jednotka počasí | Vejroplysninger | Wetterinformation | Ilmateave | Πληροφορίες καιρού | Point météo | Podatak o vremenu | informazioni meteorologiche | Laikapstākļu informācija | Meteorologinis parametras |
| Weather_item_code | Weather item | Код на елемента на метеорологичната обстановка | Elemento meteorológico | Jednotka počasí | Vejrelement | Wettergegenstand | Ilma komponent | Στοιχείο καιρού | Code du point météo | Kod podatka o vremenu | codice informazioni meteorologiche | Laikapstākļu elements | Meteorologinio parametro kodas |
| Value_min | Minimal value | Минимална стойност | Valor mínimo | Minimální hodnota | Minimumsværdi | Tiefstwert | Miinimumväärtus | Minimal value | Valeur minimale | Minimalna vrijednost | valore minimo | Minimālā vērtība | Minimali vertė |
| Value_max | Maximal value | Максимална стойност | Valor máximo | Maximální hodnota | Maksimumsværdi | Höchstwert | Maksimumväärtus | Μέγιστη τιμή | Valeur maximale | Maksimalna vrijednost | valore massimo | Maksimālā vērtība | Maksimali vertė |
| Value_gusts | Gusts value | Стойност на поривите на вятъра | Valor ráfagas | Nárazová hodnota | Vindstødsværdi | Spitzenwert | Puhangute tugevus | Τιμή ριπών ανέμου | Valeur des rafales | Vrijednost udara vjetra | valore delle raffiche | Vēja brāzmu vērtība | Gūsių vertė |
| Weather_category_code | Weather category | Категория на метеорологичната обстановка | Categoría meteorológica | Kategorie počasí | Vejrkategori | Wetterkategorie | Ilma kategooria | Κατηγορία καιρού | Catégorie météo | Kategorija vremena | categoria condizioni meteorologiche | Laikapstākļu kategorija | Oro sąlygų kategorija |
| Direction_code_min | Direction from | Направление от | Dirección de | Směr od | Retning fra | Richtung von | Lähtesuund | Διεύθυνση από | Direction de | Smjer od | direzione da | Virziens no | Kryptis nuo |
| Direction_code_max | Direction to | Направление към | Dirección a | Směr k (ku) | Retning mod | Richtung bis | Sihtsuund | Διεύθυνση προς | Direction vers | Smjer prema | direzione verso | Virziens uz | Kryptis iki |

**TAGS**

| RIS_message | NtS üzenet | Messaġġ tal-NtS | NtS-bericht | Komunikat NtS | Mensagem NtS | Mesaj NtS | Správa NtS | sporočilo NtS | NtS-sanoma | NtS-meddelande | Сообщение NtS | NtS порука |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Identification | Azonosítási szakasz | Sezzjoni ta’ identifikazzjoni | Identificatiesectie | Sekcja identyfikacyjna | Secção identificação | Element de identificare | Identifikačná sekcia | segment za identifikacijo | Tunnisteosio | Identifieringsavsnitt | Идентификация | (Идентификациони део) |
| From | Az üzenet feladója | Speditur tal-messaġġ | Afzender van het bericht | Nadawca | Remetente | Expeditorul mesajului | Odosielateľ správy | pošiljatelj sporočila | Sanoman lähettäjä | Avsändare | Отправитель | Пошиљалац поруке |
| Originator | Az információ forrása | Oriġinatur tal-informazzjoni | Oorsprong van de informatie | Autor informacji | Autor | Autorul informațiilor | Pôvodca správy | izvor informacije | Tiedon lähde | Uppgiftslämnare | Источник информации | Порекло-извор информације |
| Country_code | Az ország, amelyben az üzenet érvényes | Pajjiż fejn il-messaġġ huwa validu | Land waar het bericht geldt | Kraj, którego dotyczy komunikat | País em que a mensagem é válida | Țara în care mesajul este valabil | Krajina platnosti správy | država, v kateri je sporočilo veljavno | Maa, jota sanoma koskee | Berört land | Код страны сообщения | Држава у којој порука важи |
| Language_code | Eredeti nyelv | Lingwa oriġinali | Oorspronkelijke taal | Język oryginału | Língua original | Limba de origine | Originálny jazyk | izvirni jezik | Alkuperäkieli | Originalspråk | Язык сообщения | Изворни језик |
| District | Az országon belüli terület/ régió | Distrett/reġjun fil-pajjiż | District/regio in een land | Region kraju | Divisão administrativa (do país) | Regiune | Región | okrožje/regija znotraj države | Kyseinen alue maassa | Distrikt/region | Область в стране | Област-регион у држави |
| Date_issue | Kiadás dátuma | Data tal-ħruġ | Datum van uitgifte | Data nadania | Data de emissão | Data emiterii | Dátum vydania | datum izdaje | Antamispäivä | Datum för utfärdande | Дата составления | Датум издавања |
| Time_issue | Kiadás ideje | Ħin tal-ħruġ | Tijd van uitgifte | Godzina nadania | Hora de emissão | Ora emiterii | Čas vydania | čas izdaje | Antamisaika | Tidpunkt för utfärdande | Время составления | Време издавања |
| Ftm | Hajósoknak szóló hirdetmény | Messaġġ relatat mal-kanali navigabbli u t-traffiku | Bericht met betrekking tot vaarwegen en verkeer | Komunikat dotyczący toru wodnego i ruchu | Mensagem via navegável e tráfego | Aviz către navigatori | Správa týkajúca sa vodnej cesty a premávky | sporočilo v zvezi s plovno potjo in prometom | Väylää tai liikennettä koskeva sanoma | Farleds- och trafikrelaterat meddelande | Сообщения касательно фарватера и движения судов | Порука у вези са пловним путем и саобраћајем |
| NtS_number | Számozási szakasz | Sezzjoni tan-numru | Nummersectie | Numer sekcji | Secção relativa ao número | Numărul avizului către navigatori | Číslo | segment za številko | Sanoman numero | Numreringsavsnitt | Номер извещения |  |
| Organisation | Közzétevő szervezet | Organizzazzjoni pubblikatriċi | Uitgevende organisatie | Organ wydający | Organização de publicação | Organizația | Vydávajúca organizácia | organizacija, ki objavi sporočilo | Organisaatio | Utfärdare | Организация |  |
| Year | Év | Sena | Jaar | Rok | Ano | Anul | Rok | leto | Vuosi | År | год | Година |
| Number | (A hirdetmény száma) | Numru (tal-avviż) | Nummer (van het bericht) | Numer (komunikatu) | Número (do aviso) | Numărul (avizului) | Číslo správy | številka (obvestila) | (Ilmoituksen) numero | (Meddelandets) nummer | номер | Број (Саопштења) |
| Serial_number | Sorozatszám | Numru tas-serje | Serienummer | Numer kolejny (wersji) | Número de série | Numărul de serie | Číslo verzie (série) | zaporedna številka | Sarjanumero | Serienummer | серийный номер | Серијски број |
| Target_group | Célcsoport szakasz | Informazzjoni dwar il-grupp fil-mira | Informatie over de doelgroep | Informacje o grupie odbiorców | Secção grupo-alvo | Grupul de utilizatori avuți în vedere | Informácie o cieľovej skupine | segment za ciljno skupino | Kohderyhmäosio | Målgrupp | группа получателей | (Део циљне групе) |
| Target_group_code | Célcsoport kód | Grupp fil-mira | Doelgroep | Kod grupy odbiorców | Código grupo-alvo | Codul grupului de utilizatori avuți în vedere | Cieľová skupina | koda ciljne skupine | Kohderyhmäkoodi | Kod för målgrupp | код группы получателей | Код циљне групе |
| Direction_code | Forgalmi irány kód | Direzzjoni affettwata | Desbetreffende richting | Kod kierunku ruchu | Sentido do tráfego | Codul sensului de circulație | Dotknutý smer | koda usmerjanja prometa | Liikenteen suunnan koodi | Kod för trafikriktning | код направления движения | Код смера пловидбе |
| Subject_code | Tárgy | Suġġett | Onderwerp | Temat | Matéria | Subiectul avizului | Predmet | predmet | Aihe | Ämne | тема сообщения | Код предмета |
| Validity_period | Érvényességi időszak | Perjodu ta’ validità | Geldigheidsperiode | Okres ważności | Período de validade | Perioada de valabilitate | Doba platnosti | čas veljavnosti | Voimassaolo | Giltighetsperiod | срок действия | Рок важности |
| Date_start | Tól | Minn | Vanaf | od | De | Data de început | Od | od | Alkaa | Från | дата начала | Од (yyyymmdd) |
| Date_end | Ig | Sa | Tot | do | A | Data de sfârșit | Do | do | Päättyy | Till | дата окончания | До (yyyymmdd) |
| Contents | Tartalom | Informazzjoni addizzjonali | Aanvullende informatie | Treść | Conteúdo | Conținut | Text / Obsah | dodatne informacije | Sisältö | Innehåll | содержание | Садржај |
| Source | A hirdetmény kibocsátója (hatóság) | Sors tal-avviż (awtorità) | Bron van het bericht (autoriteit) | Źródło komunikatu (organ) | Fonte do aviso (autoridade) | Sursa avizului (autoritatea) | Zdroj správy | izvor obvestila (organ) | Ilmoituksen lähde (viranomainen) | Källa (myndighet) | Источник информации (официальный) | Извор Саопштења (орган) |
| Reason_code | A hirdetmény indoka | Raġuni għall-avviż | Reden van het bericht | Przyczyna komunikatu | Motivo do aviso | Codul evenimentului | Dôvod správy | razlog za obvestilo | Ilmoituksen syy | Orsak till meddelandet | Причина извещения | Разлог Саопштења |
| Communication | Kommunikációs csatorna info szakasz | Informazzjoni ta’ komunikazzjoni | Communicatie-informatie | Informacje o kanale łączności | Secção comunicação | Mijloc de comunicație | Informácie o komunikačnom kanáli | segment za sporočila | Viestintäosio | Kommunikationsavsnitt | Информация о средствах связи | Информације о комуникационом каналу |
| Reporting_code | A jelentést küldő rendszer | Sistema ta’ rappurtar | Meldingsregime | Sposób meldowania | Regime de transmissão | Modul de raportare | Režim hlásení | način poročanja | Raportointijärjestelmä | Rapporteringsordning | Необходимость ответного сообщения | Режим извештавања |
| Communication_code | Kommunikációs eszköz | Mezz ta’ komunikazzjoni | Communicatiemiddel | Środek łączności | Meio de comunicação | Codul mijlocului de comunicație | Komunikačné prostriedky | komunikacijska sredstva | Viestintävälineet | Kommunikationsmedel | Средства связи | Средство комуникације |
| Number (Communication section) | Szám vagy cím | Numru jew indirizz | Nummer of adres | Numer lub adres | Número ou endereço | Numărul adresei | Číslo alebo adresa | številka ali naslov | Numero tai osoite | Nummer eller adress | Контакты для связи | Број или адреса |
| Fairway_section | Víziút vagy hajóút szakasz | Passaġġ fuq l-ilma jew sezzjoni ta’ passaġġ fuq l-ilma | Waterweg of waterwegsectie | Odcinek kanału żeglownego lub toru wodnego | Via navegável ou troço | Secțiunea de cale navigabilă sau șenal | Vodná cesta (alebo úsek plavebnej dráhy) | vodna pot ali odsek vodne poti | Vesiväylä tai väylänosa | Vattenväg eller avsnitt av vattenväg | Участок фарватера или навигационного пути | Деоница водног или пловног пута |
| Geo_object | a víziút vagy objektum geo információja | Pożizzjoni | Locatie | Dane geograficzne kanału żeglownego lub obiektu | Dados geográficos via navegável ou objeto | Informația geografică despre calea navigabilă sau obiect | Geografické informácie o vodnej ceste alebo o objekte | geo-informacije o vodni poti ali objektu | vesiväylän tai kohteen maantieteelliset tiedot | Geografisk information om vattenväg eller objekt | информация по данной части фарватера или навигационного пути | (Гео информација o водном путу или објекту) |
| Id (Geo_Object section) | Azonosítás | Kodiċi tal-Pożizzjoni ISRS | ISRS-locatiecode | Oznaczenie | Identificação | Identificator | Kód lokality ISRS | identifikacija ISRS | Tunnistetiedot | Identifiering | Обозначение | Идентификација |
| Name (Geo_Object section) | A földrajzi objektum neve | Isem l-oġġett | Naam van het object | Nazwa obiektu geograficznego | Designação do objeto georreferenciado | Numele obiectului geografic | Názov objektu | ime geo-objekta | Maantieteellisen kohteen nimi | Namn på geografiskt objekt | Название объекта | Назив гео објекта |
| Type_code (Geo_Object section) | Objektum típusa | Tip | Type | Typ obiektu | Tipo de via navegável | Tipul obiectului | Typ objektu | vrsta vodne poti | Vesiväylän tyyppi | Typ av vattenväg | Тип объекта | Тип гео објекта |
| Coordinate | A hajóút kezdetének és végének koordinátái | Koordinati | Coördinaten | Współrzędne początku i końca toru wodnego | Coordenadas extremos via navegável | Coordonatele începutului și sfârșitului secțiunii | Súradnice | koordinate začetka in konca plovne poti | Väylän alku- ja loppukoordinaatit | Koordinater | Координаты начала и окончания части фарватера или навигационного пути | Почетне и крајње координате пловног пута |
| Lat (Coordinate) | Szélesség (decimális) | Latitudni | Breedtegraad | Szerokość (do dziesiętnej) | Latitude (decimal) | Latitudine (fracțiuni zecimale) | Zemepisná šírka (desatinné číslo) | zemljepisna širina | Leveysaste (desimaaliluku) | Latitud (decimal) | Широта | Географска ширина (децимално) |
| Long (Coordinate) | Hosszúság (decimális) | Lonġitudni | Lengtegraad | Długość (do dziesiętnej) | Longitude (decimal) | Longitudine (fracțiuni zecimale) | Zemepisná dĺžka (desatinné číslo) | zemljepisna dolžina | Pituusaste (desimaaliluku) | Longitud (decimal) | Долгота | Географска дужина (децимално) |
| Limitation | Korlátozott szakasz | Restrizzjoni | Beperking | Informacje o ograniczeniach | Secção restrições | Limitarea secțiunii | Obmedzenie | segment za omejitve | Rajoitusosio | Begränsningsavsnitt | Раздел ограничений | Ограничење |
| Limitation_period | Korlátozási időszak/időtartam/időköz | Perjodi/intervalli ta’ (restrizzjoni) | Periode/tussentijd (van de beperking) | Czas obowiązywania ograniczeń | Restrição (período/intervalo) | Durata limitării | Čas (obdobie) obmedzenia | (omejitev) obdobja/intervali | (Rajoitus-)jaksot/aikavälit | (Begränsning) perioder/intervaller | срок/интервал действия ограничений | (Ограничење) период/интервал |
| Date_start (Limitation_period) | Tól | Minn | Vanaf | od | De | Data începerii | Od | od | Alkaa | Från | начало действия ограничения | Од (yyyymmdd) |
| Date_end (Limitation_period) | Ig | Sa | Tot | do | A | Data sfârșirii | Do | do | Päättyy | Till | Дата окончания действия ограничения | До (yyyymmdd) |
| Time_start (Limitation_period) | Tól (óra, perc) | Minn (hh:mm) | Vanaf (hh:mm) | od (hhmm) | De (hhmm) | Ora începerii (oomm) | Od (hhmm) | od (hhmm) | Alkaa (hhmm) | Från (hhmm) | Время (ччмм) начала | Од (hhmm) |
| Time_end (Limitation_period) | Ig (óra, perc) | Sa (hh:mm) | Tot (hh:mm) | do (hhmm) | A (hhmm) | Ora terminării (oomm) | Do (hhmm) | do (hhmm) | Päättyy (hhmm) | Till (hhmm) | Время (ччмм) окончания | До (hhmm) |
| Interval_code (Limitation_period) | Időköz | Intervall | Tussentijd | Okres | Intervalo | Interval | Interval | interval | Aikaväli | Intervall | Период ограничения | Интервал |
| Limitation_code | Korlátozás jellege | Tip ta’ restrizzjoni | Soort beperking | Rodzaj ograniczenia | Tipo de restrição | Felul limitării | Druh obmedzenia | vrsta omejitve | Rajoituksen laatu | Typ av begränsning | Тип ограничения | Тип ограничења |
| Position_code | Korlátozás helye | Pożizzjoni | Positie | Położenie ograniczenia | Localização (da restrição) | Poziția | Poloha | položaj | (Rajoituksen) sijainti | (Begränsningens) position | Местоположение | Позиција (ограничења) |
| Value | Korlátozás számértéke | Valur numeriku | Numerieke waarde | Wartość numeryczna (ograniczenia) | Valor numérico (da restrição) | Valoare numerică | Číselná hodnota | numerična vrednost | (Rajoituksen) numeroarvo | (Begränsningens) numeriska värde | Величина ограничения | Нумеричка вредност (ограничења) |
| Unit | Mértékegység | Unità | Eenheid | jednostka | Unidade | Unitate | Jednotka | enota | Yksikkö | Enhet | Единица измерения величины |  |
| Fairway_name | Vízi út | Passaġġ fuq l-ilma | Waterweg | Nazwa toru wodnego | Via navegável | Numele căii navigabile | Vodná cesta | vodna pot | Vesiväylän nimi | Vattenväg | Обозначение водного пути |  |
| Reference_code | Egység | Referenza għall-valur | Waarde referentie | Układ odniesienia | Referência | Valoare de referință | Referencia | vrednost reference | Arvon referenssi | Referensvärde | Эталонная величина | Референтна вредност |
| Indication_code | Korlátozás jelzése | Indikazzjoni tar-restrizzjoni | Indicatie van de beperking | Oznaczenie ograniczenia | Indicação da restrição | Cod de indicare | Indikácia obmedzenia | označitev omejitve | (Rajoituksen) osoitus | Uppgift om begränsning | Индикация ограничения | Индикација ограничења |
| Object | Objektum | Oġġett | Object | Obiekt | Objeto | Obiect | Objekt | objekt | Kohde | Objekt | Объект | Објекат |
| Geo_object section for an Object | Az objektum földrajzi adatai | Pożizzjoni | Locatie | Dane geograficzne obiektu | Dados geográficos do objeto | Poziționarea obiectului | Geografické informácie o objekte | geo-informacije o vodni poti ali objektu | kohteen maantieteelliset tiedot | Geografisk information om objekt | Геоинформация об объекте | (Гео информације објекта) |
| Type_code (Geo_object section) | Objektum típusa | Tip ta’ oġġett | Soort object | Rodzaj obiektu | Tipo de objeto | Tipul obiectului | Typ objektu | vrsta objekta | kohteen tyyppi | Typ av objekt | Тип объекта | Тип гео објекта |
| Coordinate (Geo_object section) | Objektum koordinátái | Koordinati tal-oġġett | Coördinaten van het object | Współrzędne obiektu | Coordenadas do objeto | Coordonatele obiectului | Súradnice objektu | koordinate objekta | Kohteen koordinaatit | Objektets koordinater | Координаты объекта | Координате објекта |
| Wrm | Vízállás jelentés | Messaġġ relatat mal-ilma | Bericht met betrekking tot de waterstand | Komunikat dotyczący stanu wody | Mensagem relativa à água | Date despre apă | Správa o vodnom stave | sporočilo v zvezi z vodo | Vedenkorkeuteen liittyvä sanoma | Meddelande om vattennivån | Информация об уровне воды | Порука у вези са водостајем |
| Measure | Értékek meghatározása (mért v. előrejelzett) | Kejl (valuri normali jew imbassar) | Meetwaarden (normaal of voorspeld) | Rodzaj wartości (pomiar czy prognoza) | Valores (reais ou previstos) | Secțiunea de măsurare | Merania (normálne alebo predpovedané) | meritve (običajne ali predvidene) | Mittaukset (normaalit tai ennusteet) | Mätning (mätvärde eller beräkning) | Значение уровня воды (фактическое или ожидаемое) | Мерења (стварна или прогноза) |
| Predicted | Előrejelzés | Tbassir | Voorspelling | Prognoza | Previsão | Prognozat | Predpoveď | predvidevanje | Ennuste | Beräkning | Прогноз | Прогноза |
| Measure_code | A vízállás információ fajtája | Tip ta’ informazzjoni relatata mal-ilma | Soort informatie over de waterstand | Rodzaj komunikatu o stanie wody | Tipo de informação relativa à água | Codul măsurătorilor | Druh správy o vodnom stave | informacije v zvezi z vrsto vode | Veteen liittyvän sanoman laji | Typ av meddelande om vattennivån | Тип информации об уровне воды | Врста информације у вези са водостајем |
| Difference | Eltérés | Differenza bi tqabbil mal-valur preċedenti | Verschil t.o.v. de vorige meting | Różnica | Diferença | Diferența | Rozdiel voči predchádzajúcej hodnote | razlika | Ero | Skillnad | Разница | Разлика |
| Value_difference | Értékbeli eltérés az összehasonlító méréshez képest | differenza fil-valur bi tqabbil mal-kejl kumparattiv | Waardeverschil t.o.v. vergelijkbare meting | Różnica wartości | Diferença de valor em relação à medição comparativa | Diferență de valoare | Rozdiel voči porovnávaciemu meraniu | razlika v vrednosti glede na primerjalno meritev | arvon ero vertailukelpoiseen mittaukseen nähden | Skillnad i värde mot jämförande mätning | Разница значений для сравнительной оценки |  |
| Time_difference | Időbeli eltérés az összehasonlító méréshez képest | differenza fil-ħin bi tqabbil mal-kejl kumparattiv | Tijdsverschil t.o.v. vergelijkbare meting | Różnica czasu | Diferença horária em relação à medição comparativa | Interval de timp | Časový rozdiel voči porovnávaciemu meraniu | razlika v času glede na primerjalno meritev | aikaero vertailukelpoiseen mittaukseen nähden | Skillnad i tid mot jämförande mätning | Временное различие для сравнительной оценки |  |
| Barrage_code | Duzzasztómű | Milqgħa | Stuw | Stan zapory | Barragem | Baraj | Hať | zapora | Avattava pato | Fördämning | Плотина | Преграда |
| Regime_code | Vízjárás | Rata tal-fluss tal-ilma | Waterregime | Stan wody | Regime | Nivelul apei | Vodný režim | vodni režim | Vedenkorkeussuhteet | Vattenordning | Водный режим | Водни режим |
| Measuredate | Mérés dátuma | Data tal-kejl | Meetdatum | Data pomiaru | Data medição | Data măsurării | Dátum merania | datum merjenja | Mittauspäivä | Datum för mätning | Дата измерения | Датум мерења (yyyymmdd) |
| Measuretime | Mérés időpontja | Ħin tal-kejl | Meettijd | Godzina pomiaru | Hora medição | Ora măsurării | Čas merania | čas merjenja | Mittausaika | Tidpunkt för mätning | Время измерения | Време мерења (hhmm) |
| Icem | Jégjelentés | Messaġġ dwar is-silġ | IJsbericht | Komunikat o lodzie | Mensagem gelo | Date privind gheața | Správy o ľadochode | sporočilo o ledu | Jäätilannetta koskeva sanoma | Meddelande om isförhållanden | Ледовые сообщения | Порука у вези са ледом |
| Ice_condition | Jégállapot | Kundizzjoni tas-silġ fuq il-kanal navigabbli | IJsconditie op de vaarweg | Lód | Estado do gelo | Condițiile gheții | Ľadové podmienky | stanje ledu na plovni poti | Jäätilanne | Isförhållanden | Ледовые условия | Стање леда |
| Ice_condition_code | Jégállapot | Kundizzjoni tas-silġ | IJsconditie | Stan lodu | Estado do gelo | Condițiile gheții | Ľadové podmienky | stanje ledu | Jäätilanne | Isförhållanden | Ледовая обстановка | Стање леда |
| Ice_accessibility_code | Hajózhatóság | Aċċessibbiltà | Toegankelijkheid | Dostępność | Acessibilidade | Accesibilitate | Dostupnosť | dostopnost | Ajettavuus | Farbarhet | Условия плавания во льдах | Пловност у условима леда |
| Ice_classification_code | Jég osztályozás | Klassifikazzjoni tas-silġ | IJsclassificatie | Klasyfikacja lodu | Classificação do gelo | Clasificarea gheții | Klasifikácia ľadochodu | klasifikacija ledu | Jään luokittelu | Isklassificering | Тип плавания во льдах | Класификација леда |
| Ice_situation_code | Jéghelyzet | Sitwazzjoni tas-silġ | IJssituatie | Sytuacja lodowa | Restrições devidas à presença de gelo | Starea gheții | Situácia ľadochodu | položaj ledu | Jäätilanne | Isläge | Ограничения плавания во льдах | Стање пловидбе у случају леда |
| Werm | Időjárás üzenet | Messaġġ relatat mat-temp | Bericht met betrekking tot het weer | Komunikat pogodowy | Mensagem meteorológica | Mesaj meteo | Správa o počasí | sporočilo o vremenu | Sääsanoma | Vädermeddelande | Метеорологические сообщения | Поруке у вези времена |
| Weather_report | Időjárás jelentés | Rapport tat-temp | Weerbericht | Raport pogodowy | Boletim meteorológico | Buletin meteo | Stav počasia | vremensko poročilo | Sääraportti | Väderrapport | Метеосводка | Извештај о времену |
| Forecast | Előrejelzés | Tbassir | Voorspelling | Prognoza | Previsão meteorológica | Prognoză | Predpoveď | napoved | Ennuste | Prognos | Прогноз | Прогноза |
| Weather_class_code | Időjárás besorolás | Klassifikazzjoni tat-temp | Weerclassificatie | Klasyfikacja pogody | Classificação meteorológica | Clasificarea vremii | Klasifikácia počasia | klasifikacija vremena | Sään luokittelu | Väderklassificering | Классификация метеоусловий | Класификација времена |
| Weather_item | Időjárás elem | Informazzjoni dwar it-temp | Weersinformatie | Prognoza pogody | Informação meteorológica | Felul vremii | Informácie o počasí | informacije o vremenu | Säätiedot | Väderinformation | Метеорологические элементы | Податак о времену |
| Weather_item_code | Időjárás elem kód | Attribut tat-temp | Weerelement | Przedmiot pogody | Elemento meteorológico | Componentă meteo | Predmet počasia | vremenski pojav | Sääelementti | Väderparameter | Тип метеорологического элемента | Код податка о времену |
| Value_min | Legkisebb érték | Valur minimu | Minimumwaarde | Wartość minimalna | Valor mínimo | Valoarea minimă | Minimálna hodnota | najnižja vrednost | Alin arvo | Minimivärde | Величина на данный момент или минимальная величина | Минимална вредност |
| Value_max | Legnagyobb érték | Valur massimu | Maximumwaarde | Wartość maksymalna | Valor máximo | Valoarea maximă | Maximálna hodnota | najvišja vrednost | Ylin arvo | Maximivärde | Максимальная величина | Максимална вредност |
| Value_gusts | Csúcsérték | Valur tal-buffuri riħ | Windvlagen | Wartość podmuchu | Valor rajadas de vento | Valoarea în rafale | Nárazová hodnota | moč sunkov | Tuulen puuska | Värde för vindbyar | Величина порывов ветра | Јачина удара ветра |
| Weather_category_code | Időjárás típus | Kategorija tat-temp | Weercategorie | Kategoria pogody | Categoria meteorológica | Categoriile vremii | Kategória počasia | kategorija vremena | Säätyyppi | Väderkategori | Категория метеоусловий | Код категорије времена |
| Direction_code_min | Irányba | Direzzjoni minn | Vanuit richting | Z kierunku | Direção de | Direcția de la | Smer od | iz | Suunta (mistä) | Riktning från | Направление (ветра или волны) от | Смер од |
| Direction_code_max | Irányból | Direzzjoni lejn | Naar richting | W kierunku | Direção para | Direcția către | Smer k | v | Suunta (mihin) | Riktning mot | Направление (ветра или волны) к | Смер до |

**CÓDIGO BARRAGENS**

| CLD | Barrage Closed | Баражът е затворен | Presa cerrada | jez je uzavřen | Dæmning er lukket | Wehr ist geschlossen | Pais suletud | Κλειστός υδατοφράκτης | Barrage relevé | Brana zatvorena | sbarramento chiuso | Aizsprosts slēgts | Užtvara uždaryta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OPG | Barrage Opening | Баражът се отваря | Apertura de presa | jez se otvírá | Dæmning åbner | Wehr wird geöffnet | Paisu avamine | Υδατοφράκτης σε φάση ανοίγματος | Barrage se couchant | Brana se otvara | sbarramento in fase di apertura | Aizsprosts atveras | Užtvara atidaroma |
| CLG | Barrage Closing | Баражът се затваря | Cierre de presa | jez se zavírá | Dæmning lukker | Wehr wird geschlossen | Paisu sulgemine | Υδατοφράκτης σε φάση κλεισίματος | Barrage se relevant | Brana se zatvara | sbarramento in fase di chiusura | Aizsprosts aizveras | Užtvara uždaroma |
| OPD | Barrage Opened, no navigation through barrage | Баражът е отворен, но преминаването е забранено | Presa abierta, paso prohibido | jez je otevřen, zákaz plavby přes jez | Dæmning er åben, men gennemsejling er forbudt | Wehr ist geöffnet, keine Schifffahrt durch/über das Wehr | Pais avatud, laevatamist paisu kaudu ei toimu | Ανοικτός υδατοφράκτης, απαγόρευση ναυσιπλοΐας μέσω υδατοφράκτη | Barrage fermé à la navigation | Brana otvorena, nije dopuštena plovidba | sbarramento aperto, nessun transito consentito | Aizsprosts atvērts, kuģošana caur aizsprostu aizliegta | Užtvara atidaryta, laivyba draudžiama |
| OPN | Barrage laid, opened for navigation through barrage | Баражът е отворен за плаване | Presa abierta, paso autorizado | jez je pro plavbu otevřen | Dæmning er åben for sejlads | Wehr ist geöffnet, Schifffahrt durch/über das Wehr | Pais avatud laevatmiseks | Ανοικτός υδατοφράκτης, επιτρέπεται η ναυσιπλοΐα | Barrage ouvert à la navigation | Brana otvorena za plovidbu | sbarramento aperto, transito consentito | Aizsprosts atvērts kuģošanai caur aizsprostu | Užtvara atidaryta laivybai |

**CÓDIGO BARRAGENS**

| CLD | Duzzasztómű zárva | Milqgħa Magħluqa | Stuw is gesloten | Zapora zamknięta | Barragem fechada | Baraj închis | hať je zatvorená | zapora zaprta | Avattava pato suljettu | Fördämningen stängd | Плотина закрыта | Преграда затворена |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OPG | Duzzasztóművet nyitják | Milqgħa Qed Tinfetaħ | Stuw wordt geopend | Otwieranie zapory | Barragem a abrir | Baraj în deschidere | hať sa otvára | odpiranje zapore | Avattava pato avautuu | Fördämningen öppnas | Плотина открывается | Преграда се отвара |
| CLG | Duzzasztóművet zárják | Milqgħa Qed Tingħalaq | Stuw wordt gesloten | Zamykanie zapory | Barragem a fechar | Baraj în închidere | hať sa zatvára | zapiranje zapore | Avattava pato sulkeutuu | Fördämningen stängs | Плотина закрывается | Преграда се затвара |
| OPD | Duzzasztómű nyitva, de áthajózás a duzzasztóművön nem megengedett | Milqgħa Miftuħa, navigazzjoni minn ġol-milqgħa projbita | Stuw is geopend, maar geen doorvaart via stuw | Zapora otwarta, zamknięta dla żeglugi | Barragem aberta, passagem proibida | Baraj deschis, nu se navighează | hať je otvorená, preplávanie cez hať zakázané | zapora odprta, plovba skozi zaporo ni dovoljena | Avattava pato avattu, ei vesiliikennettä padon kautta | Fördämningen öppen, men sjöfart förbjuden | Плотина открыта, но движение судов запрещено | Преграда отворена |
| OPN | Duzzasztómű az áthajózás számára megnyitva | Milqgħa mifruxa, tista’ ssir navigazzjoni minn ġol-milqgħa | Stuw is geopend voor scheepvaart via stuw | Zapora otwarta dla żeglugi | Barragem aberta, passagem autorizada | Baraj deschis pentru navigație | hať je otvorená pre plavbu | zapora postavljena, odprta za plovbo skozi zaporo | Avattava pato avattu liikenteelle | Fördämningen öppen för sjöfart | Плотина открыта для движения судов | Преграда спуштена, пловидба слободна |

**CÓDIGO COMUNICAÇÕES**

| TE | telephone | Телефон | Teléfono | telefon | Telefon | Telefon | Telefon | Τηλέφωνο | Téléphone | Telefon | telefono | Tālrunis | Telefonas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AP | VHF | Метров обхват | VHF | VKV | VHF | UKW | VHF | VHF | VHF | VHF | VHF | UĪV | VHF |
| EM | e-mail | Електронна поща (e-mail) | Correo electrónico | E-mail | E-mail | E-Mail | E-post | Ηλεκτρονικό ταχυδρομείο | e-mail | E-mail | e-mail | e-pasts | E. paštas |
| AH | internet | Интернет | Internet | Internet | Internet | Internet | Internet | Διαδίκτυο | Internet | Internet | Internet | Internets | Internetas |
| TT | teletext | Телетекст | Teletexto | Teletext | Teletekst | Teletext | Teletekst | Tελετέξτ | Télétexte | Teletekst | teletesto | Teleteksts | Teletekstas |
| FX | telefax | Факс | Fax | Fax | Telefax | Telefax | Telefaks | Τηλεομοιοτυπία | Télécopie | Telefaks | telefax | Telefakss | Telefaksas |
| LS | light signalling | Светлинна сигнализация | Señal luminosa | světelná signalizace | Lyssignal | Lichtsignal | Valgus-signaalid | Φωτεινή σηματοδότηση | signalisation lumineuse | Svjetlosna signalizacija | segnalazione con fanali | Gaismas signāli | Šviesos signalai |
| FS | flag signalling | Флагова сигнализация | Bandera | vlajková signalizace | Flagsignal | Flaggensignal | Lipu-signaalid | Σήματα με σημαίες | pavillon | Signalizacija zastavama | segnalazione con bandiere | Signāli ar karodziņiem | Signalai vėliavėlėmis |
| SO | sound signalling | Звукова сигнализация | Señal acústica | zvuková signalizace | Lydsignal | Tonsignal | Heli-signaalid | Ηχητικά σήματα | signalisation sonore | Zvučna signalizacija | segnalazione acustica | Skaņas signāli | Garsiniai signalai |
| EI | EDI mailbox number | Номер на пощенската кутия EDI | Número de buzón EDI | číslo EDI schránky | EDI-mailboksnummer | EDI Mailbox Nummer | EDI postkasti number | Αριθμός ηλεκτρονικής θυρίδας EDI | Numéro de boîte EDI | EDI broj pretinca | casella postale EDI | EDI pastkastītes numurs | EDI pašto dėžutės numeris |

**CÓDIGO COMUNICAÇÕES**

| TE | telefon | telefown | Telefoon | Telefon | Telefone | telefon | Telefón | telefon | Puhelin | Telefon | Телефон | Телефон |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AP | rádiótelefon | VHF | Marifoon | VHF | VHF | VHF | VHF | VHF | VHF | VHF | Радиосвязь на ОВЧ | VHF |
| EM | e-mail | posta elettronika | E-mail | E-mail | Correio eletrónico | e-mail | E-mail | e-pošta | Sähköposti | E-post | E-mail | E-mail |
| AH | Internet | internet | Internet | Internet | Internet | internet | Internet | internet | Internet | Internet | Интернет | Интернет |
| TT | teletext | teletext | Teletekst | Teletekst | Teletexto | teletext | Teletex | teletekst | Tekstitelevisio | Teletext | Телетекст | Телетекст |
| FX | telefax | telefax | Fax | Telefaks | Telefax | telefax | Telefax | telefaks | Faksi | Fax | Факс | Телефакс |
| LS | fényjelzés | sinjalar bid-dawl | Lichtsignaal | sygnalizacja świetlna | Sinal luminoso | semnal luminos | svetelná signalizácia | svetlobno signaliziranje | valo-opasteet | Ljus-signalering | Световые сигналы | Светлосна сигнализација |
| FS | lobogójelzés | sinjalar bil-bnadar | Vlagsignaal | sygnalizacja flagowa | Sinal de bandeira | semnal cu stegulețe | vlajková signalizácia | signaliziranje z zastavicami | lippuopasteet | Flagg-signalering | Сигналы флагами | Сигнализација заставом |
| SO | hangjelzés | sinjalar bil-ħoss | Geluidssein | sygnalizacja dźwiękowa | Sinal sonoro | semnal sonor | zvuková signalizácia | zvočno signaliziranje | ääniopasteet | Ljud-signalering | Звуковые сигналы | Звучна сигнализација |
| EI | EDI postafiók szám | Numru tal-kaxxa postali EDI | EDI-mailboxnummer | Numer skrzynki pocztowej EDI | Número caixa postal EDI | număr căsuță poștală EDI | číslo schránky EDI | Številka poštnega predala EDI | EDI mailbox-numero | EDI-postlådenummer | Номер почтового ящика EDI | Број EDI сандучета |

**CÓDIGO PAÍS**

| AT | Austria | Австрия | Austria | Rakousko | Østrig | Österreich | Austria | Αυστρία | Autriche | Austrija | Austria | Austrija | Austrija |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BE | Belgium | Белгия | Bélgica | Belgie | Belgien | Belgien | Belgia | Βέλγιο | Belgique | Belgija | Belgio | Beļģija | Belgija |
| BG | Bulgaria | България | Bulgaria | Bulharsko | Bulgarien | Bulgarian | Bulgaaria | Βουλγαρία | Bulgarie | Bugarska | Bulgaria | Bulgārija | Bulgarija |
| CH | Switzerland | Швейцария | Suiza | Švýcarsko | Schweiz | Schweiz | Šveits | Ελβετία | Suisse | Švicarska | Svizzera | Šveice | Šveicarija |
| RS | Serbia | Сърбия | Serbia | Srbsko | Serbien | Serbien | Serbia | Σερβία | Serbie | Srbija | Serbia | Serbija | Serbija |
| CY | Cyprus | Кипър | Chipre | Kypr | Cypern | Zypern | Küpros | Κύπρος | Chypre | Cipar | Cipro | Kipra | Kipras |
| CZ | Czech Republic | Република Чехия | Chequia | Česká republika | Tjekkiet | Tschechien | Tšehhi Vabariik | Τσεχική Δημοκρατία | République Tchèque | Češka | Repubblica ceca | Čehija | Čekija |
| DE | Germany | Германия | Alemania | Německo | Tyskland | Deutschland | Saksamaa | Γερμανία | Allemagne | Njemačka | Germania | Vācija | Vokietija |
| DK | Denmark | Дания | Dinamarca | Dánsko | Danmark | Dänemark | Taani | Δανία | Danemark | Danska | Danimarca | Dānija | Danija |
| EE | Estonia | Естония | Estonia | Estonsko | Estland | Estland | Eesti | Εσθονία | Estonie | Estonija | Estonia | Igaunija | Estija |
| ES | Spain | Испания | España | Španělsko | Spanien | Spanien | Hispaania | Ισπανία | Espagne | Španjolska | Spagna | Spānija | Ispanija |
| FI | Finland | Финландия | Finlandia | Finsko | Finland | Finnland | Soome | Φινλανδία | Finlande | Finska | Finlandia | Somija | Suomija |
| FR | France | Франция | Francia | Francie | Frankrig | Frankreich | Prantsusmaa | Γαλλία | France | Francuska | Francia | Francija | Prancūzija |
| GB | United Kingdom | Великобритания | Reino Unido | Velká Británie | Det Forenede Kongerige | Großbritannien | Ühend-kuningriik | Ηνωμένο Βασίλειο | Royaume-Uni | Ujedinjena Kraljevina | Regno Unito | Apvienotā Karaliste | Jungtinė Karalystė |
| GR | Greece | Гърция | Grecia | Řecko | Grækenland | Griechenland | Kreeka | Ελλάδα | Grèce | Grčka | Grecia | Grieķija | Graikija |
| HR | Croatia | Хърватия | Croacia | Chorvatsko | Kroatien | Kroatien | Horvaatia | Κροατία | Croatie | Hrvatska | Croazia | Horvātija | Kroatija |
| HU | Hungary | Унгария | Hungría | Maďarsko | Ungarn | Ungarn | Ungari | Ουγγαρία | Hongrie | Mađarska | Ungheria | Ungārija | Vengrija |
| IE | Ireland | Ирландия | Irlanda | Irsko | Irland | Irland | Iirimaa | Ιρλανδία | Irlande | Irska | Irlanda | Īrija | Airija |
| IT | Italy | Италия | Italia | Itálie | Italien | Italien | Itaalia | Ιταλία | Italie | Italija | Italia | Itālija | Italija |
| LT | Lithuania | Литва | Lituania | Litva | Litauen | Litauen | Leedu | Λιθουανία | Lituanie | Litva | Lituania | Lietuva | Lietuva |
| LU | Luxembourg | Люксембург | Luxemburgo | Lucembursko | Luxembourg | Luxemburg | Luksemburg | Λουξεμβούργο | Luxembourg | Luksemburg | Lussemburgo | Luksemburga | Liuksemburgas |
| LV | Latvia | Латвия | Letonia | Lotyšsko | Letland | Lettland | Läti | Λετονία | Lettonie | Latvija | Lettonia | Latvija | Latvija |
| MD | Moldova | Молдова | Moldavia | Moldavsko | Moldova | Moldawien | Moldaavia | Μολδαβία | Moldavie | Moldova | Moldova | Moldova | Moldova |
| MT | Malta | Малта | Malta | Malta | Μalta | Malta | Malta | Μάλτα | Malte | Malta | Malta | Malta | Мalta |
| NL | Netherlands | Нидерландия | Países Bajos | Nizozemsko | Nederlandene | Niederlande | Madalmaad | Κάτω Χώρες | Pays-Bas | Nizozemska | Paesi Bassi | Nīderlande | Nyderlandai |
| PL | Poland | Полша | Polonia | Polsko | Polen | Polen | Poola | Πολωνία | Pologne | Poljska | Polonia | Polija | Lenkija |
| PT | Portugal | Португалия | Portugal | Portugalsko | Portugal | Portugal | Portugal | Πορτογαλία | Portugal | Portugal | Portogallo | Portugāle | Portugalija |
| RO | Romania | Румъния | Rumanía | Rumunsko | Rumænien | Rumänien | Rumeenia | Ρουμανία | Roumanie | Rumunjska | Romania | Rumānija | Rumunija |
| RU | Russia | Русия | Rusia | Rusko | Rusland | Russland | Venemaa | Ρωσσία | Russie | Rusija | Russia | Krievija | Rusija |
| SE | Sweden | Швеция | Suecia | Švédsko | Sverige | Schweden | Rootsi | Σουηδία | Suède | Švedska | Svezia | Zviedrija | Švedija |
| SI | Slovenia | Словения | Eslovenia | Slovinsko | Slovenien | Slowenien | Sloveenia | Σλοβενία | Slovénie | Slovenija | Slovenia | Slovēnija | Slovėnija |
| SK | Slovakia | Словакия | Eslovaquia | Slovensko | Slovakiet | Slowakei | Slovakkia | Σλοβακία | Slovaquie | Slovačka | Slovacchia | Slovākija | Slovakija |
| UA | Ukraine | Украина | Ucrania | Ukrajina | Ukraine | Ukraine | Ukraina | Ουκρανία | Ukraine | Ukrajina | Ucraina | Ukraina | Ukraina |
| ME | Montenegro | Черна гора | Montenegro | Černá Hora | Montenegro | Montenegro | Montenegro | Μαυροβούνιο | Monténégro | Crna Gora | Montenegro | Melnkalne | Juodkalnija |

**CÓDIGO PAÍS**

| AT | Ausztria | L-Awstrija | Oostenrijk | Austria | Áustria | Austria | Rakúsko | Avstrija | Itävalta | Österrike | Австрия | Аустрија |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BE | Belgium | Il-Belġju | België | Belgia | Bélgica | Belgia | Belgicko | Belgija | Belgia | Belgien | Бельгия | Белгија |
| BG | Bulgária | Il-Bulgarija | Bulgarije | Bułgaria | Bulgária | Bulgaria | Bulharsko | Bolgarija | Bulgaria | Bulgarien | Болгария | Бугарска |
| CH | Svájc | L-Iżvizzera | Zwitserland | Szwajcaria | Suíça | Elveția | Švajčiarsko | Švica | Sveitsi | Schweiz | Швейцария | Швајцарска |
| RS | Szerbia | Is-Serbja | Servië | Serbia | Sérvia | Serbia | Srbsko | Srbija | Serbia | Serbien | Сербия | Србија |
| CY | Ciprus | Ċipru | Cyprus | Cypr | Chipre | Cipru | Cyprus | Ciper | Kypros | Cypern | Кипр | Кипар |
| CZ | Cseh Köztársaság | Ir-Repubblika Ċeka | Tsjechië | Republika Czeska | República Checa | Republica Cehă | Česko | Češka | Tšekki | Tjeckien | Чешская республика | Чешка Република |
| DE | Németország | Il-Ġermanja | Duitsland | Niemcy | Alemanha | Germania | Nemecko | Nemčija | Saksa | Tyskland | Германия | Немачка |
| DK | Dánia | Id-Danimarka | Denemarken | Dania | Dinamarca | Danemarca | Dánsko | Danska | Tanska | Danmark | Дания | Данска |
| EE | Észtország | L-Estonja | Estland | Estonia | Estónia | Estonia | Estónsko | Estonija | Viro | Estland | Эстония | Естонија |
| ES | Spanyolország | Spanja | Spanje | Hiszpania | Espanha | Spania | Španielsko | Španija | Espanja | Spanien | Испания | Шпанија |
| FI | Finnország | Il-Finlandja | Finland | Finlandia | Finlândia | Finlanda | Fínsko | Finska | Suomi | Finland | Финляндия | Финска |
| FR | Franciaország | Franza | Frankrijk | Francja | França | Franța | Francúzsko | Francija | Ranska | Frankrike | Франция | Француска |
| GB | Egyesült Királyság | Ir-Renju Unit | Verenigd Koninkrijk | Wielka Brytania | Reino Unido | Regatul Unit | Veľká Británia | Združeno kraljestvo | Yhdistynyt kuningaskunta | Förenade kungariket | Великобритания | Велика Британија |
| GR | Görögország | Il-Greċja | Griekenland | Grecja | Grécia | Grecia | Grécko | Grčija | Kreikka | Grekland | Греция | Грчка |
| HR | Horvátország | Il-Kroazja | Kroatië | Chorwacja | Croácia | Croația | Chorvátsko | Hrvaška | Kroatia | Kroatien | Хорватия | Хрватска |
| HU | Magyarország | L-Ungerija | Hongarije | Węgry | Hungria | Ungaria | Maďarsko | Madžarska | Unkari | Ungern | Венгрия | Мађарска |
| IE | Írország | L-Irlanda | Ierland | Irlandia | Irlanda | Irlanda | Írsko | Irska | Irlanti | Irland | Ирландия | Ирска |
| IT | Olaszország | L-Italja | Italië | Włochy | Itália | Italia | Taliansko | Italija | Italia | Italien | Италия | Италија |
| LT | Litvánia | Il-Litwanja | Litouwen | Litwa | Lituânia | Lituania | Litva | Litva | Liettua | Litauen | Литва | Литванија |
| LU | Luxemburg | Il-Lussemburgu | Luxemburg | Luksemburg | Luxemburgo | Luxemburg | Luxembursko | Luksemburg | Luxemburg | Luxemburg | Люксембург | Луксембург |
| LV | Lettország | Il-Latvja | Letland | Łotwa | Letónia | Letonia | Lotyšsko | Latvija | Latvia | Lettland | Латвия | Летонија |
| MD | Moldávia | Il-Moldova | Moldavië | Mołdawia | Moldávia | Moldova | Moldavsko | Moldavija | Moldova | Moldavien | Молдавия | Молдавија |
| MT | Málta | Malta | Malta | Malta | Malta | Malta | Malta | Malta | Malta | Malta | Мальта | Малта |
| NL | Hollandia | In-Netherlands | Nederland | Holandia | Países Baixos | Țările de Jos | Holandsko | Nizozemska | Alankomaat | Nederländerna | Нидерланды | Холандија |
| PL | Lengyelország | Il-Polonja | Polen | Polska | Polónia | Polonia | Poľsko | Poljska | Puola | Polen | Польша | Пољска |
| PT | Portugália | Il-Portugall | Portugal | Portugalia | Portugal | Portugalia | Portugalsko | Portugalska | Portugali | Portugal | Португалия | Португал |
| RO | Románia | Ir-Rumanija | Roemenië | Rumunia | Roménia | România | Rumunsko | Romunija | Romania | Rumänien | Румыния | Румунија |
| RU | Oroszország | Ir-Russja | Rusland | Rosja | Rússia | Rusia | Rusko | Rusija | Venäjä | Ryssland | Россия | Русија |
| SE | Svédország | L-Iżvezja | Zweden | Szwecja | Suécia | Suedia | Švédsko | Švedska | Ruotsi | Sverige | Швеция | Шведска |
| SI | Szlovénia | Is-Slovenja | Slovenië | Słowenia | Eslovénia | Slovenia | Slovinsko | Slovenija | Slovenia | Slovenien | Словения | Словенија |
| SK | Szlovákia | Is-Slovakkja | Slowakije | Słowacja | Eslováquia | Slovacia | Slovensko | Slovaška | Slovakia | Slovakien | Словакия | Словачка |
| UA | Ukrajna | L-Ukrajna | Oekraïne | Ukraina | Ucrânia | Ucraina | Ukrajina | Ukrajina | Ukraina | Ukraina | Украина | Украјина |
| ME | Montenegró | Il-Montenegro | Montenegro | Czarnogóra | Montenegro | Muntenegru | Čierna Hora | Črna gora | Montenegro | Montenegro | Черногория | Црна Гора |

**CÓDIGO DE DIREÇÃO**

| ALL | all directions | Всички посоки | Todas las direcciones | všechny směry | Alle retninger | alle Richtungen | Kõik suunad | Όλες οι κατευθύνσεις | toutes les directions | Svi smjerovi | tutte le direzioni | Visi virzieni | Visomis kryptimis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UPS | upstream | Срещу течението | Aguas arriba | proti proudu | Opstrøms | Bergfahrt | Ülesvoolu | Ανάντη | montant | Uzvodno | in ascesa | Pret straumi | Prieš srovę |
| DWN | downstream | По течението | Aguas abajo | po proudu | Nedstrøms | Talfahrt | Allavoolu | Κατάντη | avalant | Nizvodno | in discesa | Pa straumi | Pasroviui |

**CÓDIGO DE DIREÇÃO**

| ALL | minden irányba | id-direzzjonijiet kollha | Alle richtingen | Wszystkie kierunki | Todas as direções | toate direcțiile | všetky smery | vse smeri | Kaikki suunnat | Alla riktningar | Движение во всех направлениях | Сви смерови |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UPS | hegymenet | upstream | Opvaart | Pod prąd | Montante | în amonte | proti prúdu | proti toku | Vastavirtaan | Uppströms | Движение вверх по течению | Узводно |
| DWN | völgymenet | downstream | Afvaart | Z prądem | Jusante | în aval | po prúde | v smeri toka | Myötävirtaan | Nedströms | Движение вниз по течению | Низводно |

**CÓDIGO DE LÍNGUA**

| EN | English | Английски | Inglés | anglicky | Engelsk | englisch | inglise | Αγγλικά | Anglais | engleski | inglese | Angļu | Anglų |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BG | Bulgarian | Български | Búlgaro | bulharsky | Bulgarsk | bulgarisch | bulgaaria | Βουλγαρικά | Bulgare | bugarski | bulgaro | Bulgāru | Bulgarų |
| ES | Spanish | Испански | Español | španělsky | Spansk | spanisch | hispaania | Ισπανικά | Espagnol | španjolski | spagnolo | Spāņu | Ispanų |
| CS | Czech | Чешки | Checo | česky | Tjekkisk | tschechisch | tšehhi | Τσεχικά | Tchèque | češki | ceco | Čehu | Čekų |
| DA | Danish | Датски | Danés | dánsky | Dansk | dänisch | taani | Δανικά | Danois | danski | danese | Dāņu | Danų |
| DE | German | Немски | Alemán | německy | Tysk | deutsch | saksa | Γερμανικά | Allemand | njemački | tedesco | Vācu | Vokiečių |
| ET | Estonian | Естонски | Estonio | estonsky | Estisk | estnisch | eesti | Εσθονικά | Estonien | estonski | estone | Igauņu | Estų |
| EL | Greek | Гръцки | Griego | řecky | Græsk | griechisch | kreeka | Ελληνικά | Grec | grčki | greco | Grieķu | Graikų |
| FR | French | Френски | Francés | francouzsky | Fransk | französisch | prantsuse | Γαλλικά | Français | francuski | francese | Franču | Prancūzų |
| GA | Gaelic | Ирландски | Irlandés | irsky | Irsk | gälisch | iiri | Ιρλανδικά | Gaélique | irski | gaelico | Gēlu | Gėlų |
| HR | Croatian | Хърватски | Croata | chorvatsky | Kroatisk | kroatisch | horvaatia | Κροατικά | Croate | hrvatski | croato | Horvātu | Kroatų |
| IT | Italian | Италиански | Italiano | italsky | Italiensk | italienisch | itaalia | Ιταλικά | Italien | talijanski | italiano | Itāliešu | Italų |
| LV | Latvian | Латвийски | Letón | lotyšsky | Lettisk | lettisch | läti | Λετονικά | Letton | latvijski | lettone | Latviešu | Latvių |
| LT | Lithuanian | Литовски | Lituano | litevsky | Litauisk | litauisch | leedu | Λιθουανικά | Lituanien | litavski | lituano | Lietuviešu | Lietuvių |
| HU | Hungarian | Унгарски | Húngaro | maďarsky | Ungarsk | ungarisch | ungari | Ουγγρικά | Hongrois | mađarski | ungherese | Ungāru | Vengrų |
| MT | Maltese | Малтийски | Maltés | maltsky | Maltesisk | maltesisch | malta | Μαλτέζικα | Maltais | malteški | maltese | Maltiešu | Maltiečių |
| NL | Dutch | Холандски | Neerlandés | nizozemsky | Nederlandsk | niederländisch | hollandi | Ολλανδικά | Néerlandais | nizozemski | neerlandese | Holandiešu | Nyderlandų |
| PL | Polish | Полски | Polaco | polsky | Polsk | polnisch | poola | Πολωνικά | Polonais | poljski | polacco | Poļu | Lenkų |
| PT | Portuguese | Португалски | Portugués | portugalsky | Portugisisk | portugiesisch | portugali | Πορτογαλικά | Portugais | portugalski | portoghese | Portugāļu | Portugalų |
| RO | Romanian | Румънски | Rumano | rumunsky | Rumænsk | rumänisch | rumeenia | Ρουμανικά | Roumain | rumunjski | rumeno | Rumāņu | Rumunų |
| SK | Slovak | Словашки | Eslovaco | slovensky | Slovakisk | slowakisch | slovaki | Σλοβακικά | Slovaque | slovački | slovacco | Slovāku | Slovakų |
| SL | Slovenian | Словенски | Eslovaco | slovinsky | Slovensk | slowenisch | sloveenia | Σλοβενικά | Slovène | slovenski | sloveno | Slovēņu | Slovėnų |
| FI | Finnish | Финландски | Finés | finsky | Finsk | finnisch | soome | Φινλανδικά | Finnois | finski | finlandese | Somu | Suomių |
| SV | Swedish | Шведски | Sueco | švédsky | Svensk | schwedisch | rootsi | Σουηδικά | Suédois | švedski | svedese | Zviedru | Švedų |
| RU | Russian | Руски | Ruso | rusky | Russisk | russisch | vene | Ρωσσικά | Russe | ruski | russo | Krievu | Rusų |
| SR | Serbian | Сръбски | Serbio | srbsky | Serbisk | serbisch | serbia | Σερβικά | Serbe | srpski | serbo | Serbu | Serbų |

**CÓDIGO DE LÍNGUA**

| EN | angol | Ingliż | Engels | angielski | Inglês | Engleză | anglicky | angleščina | Englanti | Engelska | Английский | енглески |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BG | bolgár | Bulgaru | Bulgaars | bułgarski | Búlgaro | Bulgară | bulharsky | bolgarščina | Bulgaria | Bulgariska | Болгарский | бугарски |
| ES | spanyol | Spanjol | Spaans | hiszpański | Espanhol | Spaniolă | španielsky | španščina | Espanja | Spanska | Испанский | шпански |
| CS | cseh | Ċek | Tsjechisch | czeski | Checo | Cehă | česky | češčina | Tšekki | Tjeckiska | Чешский | чешки |
| DA | dán | Daniż | Deens | duński | Dinamarquês | Daneză | dánsky | danščina | Tanska | Danska | Датский | дански |
| DE | német | Ġermaniż | Duits | niemiecki | Alemão | Germană | nemecky | nemščina | Saksa | Tyska | Немецкий | немачки |
| ET | észt | Estonjan | Ests | estoński | Estónio | Estonă | estónsky | estonščina | Viro | Estniska | Эстонский | естонски |
| EL | görög | Grieg | Grieks | grecki | Grego | Greacă | grécky | grščina | Kreikka | Grekiska | Греческий | грчки |
| FR | francia | Franċiż | Frans | francuski | Francês | Franceză | francúzsky | francoščina | Ranska | Franska | Французский | француски |
| GA | ír | Gaelic | Iers | irlandzki | Gaélico | Irlandeză | írsky | irščina | Iiri | Iriska |  |  |
| HR | horvát | Kroat | Kroatisch | chorwacki | Croata | Croată | chorvátsky | hrvaščina | Kroatia | Kroatiska | Хорватский | хрватски |
| IT | olasz | Taljan | Italiaans | włoski | Italiano | Italiană | taliansky | italijanščina | Italia | Italienska | Итальянский | италијански |
| LV | lett | Latvjan | Lets | łotewski | Letão | Letonă | lotyšsky | latvijščina | Latvia | Lettiska | Латвийский | летонски |
| LT | litván | Litwen | Litouws | litewski | Lituano | lituaniană | litovsky | litovščina | Liettua | Litauiska | Литовский | литвански |
| HU | magyar | Ungeriż | Hongaars | węgierski | Húngaro | Maghiară | maďarsky | madžarščina | Unkari | Ungerska | Венгерский | мађарски |
| MT | máltai | Malti | Maltees | maltański | Maltês | Malteză | maltsky | malteščina | Malta | Maltesiska | Мальтийский | Malteski |
| NL | holland | Netherlandiż | Nederlands | holenderski | Neerlandês | Olandeză | holandsky | nizozemščina | Hollanti | Nederländska | Голландский | пољски |
| PL | lengyel | Pollakk | Pools | polski | Polaco | Poloneză | poľsky | poljščina | Puola | Polska | Польский | португалски |
| PT | portugál | Portugiż | Portugees | portugalski | Português | Portugheză | portugalsky | portugalščina | Portugali | Portugisiska | Португальский | румунски |
| RO | román | Rumen | Roemeens | rumuński | Romeno | Română | rumunsky | romunščina | Romania | Rumänska | Румынский | руски |
| SK | szlovák | Slovakk | Slowaaks | słowacki | Eslovaco | Slovacă | slovensky | slovaščina | Slovakki | Slovakiska | Словацкий | словачки |
| SL | szlovén | Sloven | Sloveens | słoweński | Esloveno | Slovenă | slovinsky | slovenščina | Sloveeni | Slovenska | Словенский | словеначки |
| FI | finn | Finlandiż | Fins | fiński | Finlandês | Finlandeză | fínsky | finščina | Suomi | Finska | Финский | фински |
| SV | svéd | Żvediż | Zweeds | szwedzki | Sueco | Suedeză | švédsky | švedščina | Ruotsi | Svenska | Шведский | шведски |
| RU | orosz | Russu | Russisch | rosyjski | Russo | Rusă | rusky | ruščina | Venäjä | Ryska | Русский | словачки |
| SR | szerb | Serb | Servisch | serbski | Sérvio | Sârbă | srbsky | srbščina | Serbia | Serbiska | Сербский | српски |

**CÓDIGO DE INDICAÇÃO**

| MAX | maximum | максимум | máximo | maximum | Maksimum | höchstens | maksimum | Μέγιστο | maximum | Najviše | massimo | maksimāli | didžiausia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MIN | minimum | минимум | mínimo | minimum | Minimum | mindestens | miinimum | Ελάχιστο | minimum | Najmanje | minimo | minimāli | mažiausia |
| RED | reduced by | намалено с | Reducido en | redukován o | Reduceret med | verringert um | vähendatud | Μειωμένο κατά | réduit de | Smanjeno za | diminuito di | samazināts par | sumažinama |

**CÓDIGO DE INDICAÇÃO**

| MAX | Maximum | massima | Maximaal | maksimum | Máximo | maxim | maximum | največje | maksimi | Maximum | максимальный | максимум |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MIN | Minimum | minima | Minimaal | minimum | Mínimo | minim | minimum | najmanjše | minimi | Minimum | минимальный | минимум |
| RED | által csökkentve | imnaqqsa b’ | Verminderd met | ograniczenie o (wartość) | Reduzido de | redus cu | znížený o | zmanjšano za | vähennetty seuraavalla: | Reducerat med | уменьшено на | умањен за |

**CÓDIGO DE INTERVALO**

| CON | continuous | Непрекъснато | Continuo | nepřetržitě | Kontinuerligt | durchgehend | Pidev | Συνεχής | Permanent | Neprekidno | permanente | Nepārtraukti | Nuolat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DAY | daily | Ежедневно | Diario | denně | Dagligt | täglich | Iga päev | Ημερήσια | Journalier | Dnevno | giornaliero | Ik dienas | Kasdien |
| WRK | Monday to Friday | От понеделник до петък | Lunes a viernes | pondělí až pátek | Mandag til fredag | Montag bis Freitag | Esmaspäevast reedeni | Δευτέρα έως Παρασκευή | Lundi au Vendredi | Od ponedjeljka do petka | da lunedì a venerdì | No pirmdienas līdz piektdienai | Nuo pirmadienio iki penktadienio |
| WKN | Saturday and Sunday | Събота и неделя | Sábado y domingo | sobota a neděle | Lørdag og søndag | Samstag und Sonntag | Laupäev ja pühapäev | Σάββατο έως Κυριακή | Samedi et Dimanche | Subotom i nedjeljom | sabato e domenica | Sestdiena un svētdiena | Šeštadienis ir sekmadienis |
| SUN | Sunday | Неделя | Domingo | neděle | Søndag | Sonntag | Pühapäev | Κυριακή | Dimanche | Nedjeljom | domenica | Svētdiena | Sekmadienis |
| MON | Monday | Понеделник | Lunes | pondělí | Mandag | Montag | Esmaspäev | Δευτέρα | Lundi | Ponedjeljkom | lunedì | Pirmdiena | Pirmadienis |
| TUE | Tuesday | Вторник | Martes | úterý | Tirsdag | Dienstag | Teisipäev | Τρίτη | Mardi | Utorkom | martedì | Otrdiena | Antradienis |
| WED | Wednesday | Сряда | Miércoles | středa | Onsdag | Mittwoch | Kolmapäev | Τετάρτη | Mercredi | Srijedom | mercoledì | Trešdiena | Trečiadienis |
| THU | Thursday | Четвъртък | Jueves | čtvrtek | Torsdag | Donnerstag | Neljapäev | Πέμπτη | Jeudi | Četvrtkom | giovedì | Ceturtdiena | Ketvirtadienis |
| FRI | Friday | Петък | Viernes | pátek | Fredag | Freitag | Reede | Παρασκευή | Vendredi | Petkom | venerdì | Piektdiena | Penktadienis |
| SAT | Saturday | Събота | Sábado | sobota | Lørdag | Samstag | Laupäev | Σάββατο | Samedi | Subotom | sabato | Sestdiena | Šeštadienis |
| DTI | day-time | През деня | Período diurno | ve dne | Om dagen | bei Tag | päeval | Κατά τη διάρκεια της ημέρας | en journée | Preko dana | diurno | dienā | Dienos metas |
| NTI | night-time | През нощта | Período nocturno | v noci | Om natten | bei Nacht | öösel | Κατά της διάρκεια της νύχτας | de nuit | Preko noći | notturno | naktī | Nakties metas |
| RVI | in case of restricted visibility | При ограничена видимост | Con visibilidad reducida | za snížené viditelnosti | Ved nedsat sigt | bei beschränkten Sichtverhältnissen | piiratud nähtavuse korral | Σε περίπτωση περιορισμένης ορατότητας | par mauvaise visibilité | U slučaju smanjene vidljivosti | in caso di visibilità ridotta | ierobežotas redzamības apstākļos | Riboto matomumo atveju |
| EXC | with the exception of | С изключение на | salvo | s výjimkou | Med undtagelse af | mit Ausnahme von | välja arvatud | Εξαιρουμένου του | à l'exception de | S izuzetkom | ad eccezione di | izņemot | Išskyrus |
| WRD | Monday to Friday except public holidays | От понеделник до петък, с изключение на официални празници | De lunes a viernes excepto festivos | pondělí až pátek kromě státních svátků | Mandag til fredag undtagen helligdage | Montag bis Freitag ausgenommen Feiertage | Esmaspäevast reedeni, v.a riigipühad | Δευτέρα έως Παρασκευή εκτός επίσημων αργιών | Lundi au vendredi excepté jours fériés | Od ponedjeljka do petka osim praznika | da lunedì a venerdì, eccetto i giorni festivi | No pirmdienas līdz piektdienai, izņemot oficiāli svinamās dienas | Nuo pirmadienio iki penktadienio, išskyrus valstybinių švenčių dienas |

**CÓDIGO DE INTERVALO**

| CON | folyamatos | (kontinwu) | Onafgebroken | ciągłe | Contínuo | permanent | nepretržite | neprekinjeno | Jatkuva | Fortlöpande | Постоянно | Непрекидан |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DAY | naponta | kuljum | Dagelijks | codziennie | Diário | zilnic | denne | dnevno | Päivittäinen | Dagligen | ежедневно | Дневно |
| WRK | hétfőtől péntekig | Mit-Tnejn sal-Ġimgħa | Van maandag tot en met vrijdag | od poniedziałku do piątku | Segunda a sexta | de luni până vineri | pondelok až piatok | od ponedeljka do petka | Maanantaista perjantaihin | Måndag till fredag | с понедельника по пятницу | Од понедељка до петка |
| WKN | szombaton és vasárnap | Is-Sibt u l-Ħadd | Zaterdag en zondag | sobota i niedziela | Sábado e domingo | sâmbăta și duminica | sobota a nedeľa | sobota in nedelja | Lauantai ja sunnuntai | Lördag till söndag | суббота и воскресенье | Субота и недеља |
| SUN | vasárnap | Il-Ħadd | Zondag | niedziela | Domingo | duminică | nedeľa | nedelja | Sunnuntai | Söndag | воскресенье | Недеља |
| MON | hétfő | It-Tnejn | Maandag | poniedziałek | Segunda | luni | pondelok | ponedeljek | Maanantai | Måndag | понедельник | Понедељак |
| TUE | kedd | It-Tlieta | Dinsdag | wtorek | Terça | marți | utorok | torek | Tiistai | Tisdag | вторник | Уторак |
| WED | szerda | L-Erbgħa | Woensdag | środa | Quarta | miercuri | streda | sreda | Keskiviikko | Onsdag | среда | Среда |
| THU | csütörtök | Il-Ħamis | Donderdag | czwartek | Quinta | joi | štvrtok | četrtek | Torstai | Torsdag | четверг | Четвртак |
| FRI | péntek | Il-Ġimgħa | Vrijdag | piątek | Sexta | vineri | piatok | petek | Perjantai | Fredag | пятница | Петак |
| SAT | szombat | Is-Sibt | Zaterdag | sobota | Sábado | sâmbătă | sobota | sobota | Lauantai | Lördag | суббота | Субота |
| DTI | nappal | matul il-ġurnata | Overdag | w porze dziennej | Período diurno | în timpul zilei | cez deň | podnevi | päivisin | Dagtid | Дневное время | Дању |
| NTI | éjszaka | matul il-lejl | 's Nachts | w porze nocnej | Período noturno | în timpul nopții | v noci | ponoči | öisin | Nattetid | Ночное время | Ноћу |
| RVI | korlátozott látási viszonyok esetén | f’każ ta’ viżibbiltà ristretta | Bij beperkt zicht | w przypadku ograniczonej widoczności | Com visibilidade reduzida | în caz de vizibilitate redusă | pri zníženej viditeľnosti | v primeru omejene vidljivosti | näkyvyyden ollessa rajallinen | Vid begränsad sikt | в случае ограниченой видимости | При ограниченој видљивости |
| EXC | kivéve | bl-eċċezzjoni ta’ | Met uitzondering van | z wyjątkiem | Excetuando | cu excepția | okrem | razen | lukuun ottamatta: | Med undantag av | За исключением | Са изузетком |
| WRD | hétfőtől péntekig, kivéve ünnepnapokon | Mit-Tnejn sal-Ġimgħa minbarra btajjel pubbliċi | Van maandag tot en met vrijdag, uitgezonderd feestdagen | od poniedziałku do piątku z wyjątkiem świąt | Segunda a sexta exceto feriados | de luni până vineri exceptând sărbătorile | pondelok až piatok okrem sviatkov | od ponedeljka do petka razen v času praznikov | Maanantaista perjantaihin yleisiä vapaapäiviä lukuun ottamatta | Måndag till fredag, utom allmänna helgdagar | C понедельника по пятницу, кроме праздничных дней | Од понедељка до петка, осим празницима |

**CÓDIGO DE RESTRIÇÕES**

| OBSTRU | blockage | Препятствие | Obstrucción | uzávěra | Blokering | Sperre | Blokeering | Φράγμα | Restriction | Prepreka | ostruzione totale | Bloķēts | Blokavimas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PAROBS | partial obstruction | Частично препятствие | Obstrucción parcial | částečná uzávěra | Delvis blokering | teilweise Sperre | Osaline takistus | Μερική παρεμπόδιση | Restriction partielle | Djelomična prepreka | ostruzione parziale | Daļēji bloķēts | Dalinis blokavimas |
| DELAY | delay | Закъснение | Retraso | zpoždění | Forsinkelse | Verzögerung | Hilinemine | Καθυστέρηση | Délai | Kašnjenje | ritardo | Aizkavēšanās | Delsa |
| VESLEN | vessel length | Дължина на кораба | Eslora | délka plavidla | Fartøjets længde | Schiffslänge | Laeva pikkus | Μήκος σκάφους | Longueur du bateau | Duljina broda | lunghezza natante | Kuģa garums | Laivo ilgis |
| VESHEI | vessel air draught | Височина на кораба | Altura de la obra muerta | výška plavidla nad hladinou | Fartøjets højde over vandlinjen | Schiffshöhe | Laeva kõrgus veepinnast | Μέγιστο ύψος άνωθεν της ισάλου γραμμής | tirant d'air du bateau | Visina najviše fiksne točke broda iznad vode | altezza natante dal pelo dell'acqua | Kuģa virsūdens augstums | Laivo aukštis virš vandens |
| VESBRE | vessel breadth | Ширина на кораба | Manga | šířka plavidla | Fartøjets bredde | Schiffsbreite | Laeva laius | Μέγιστο πλάτος σκάφους | Largeur du bateau | Širina broda | larghezza del natante | Kuģa platums | Laivo plotis |
| VESDRA | vessel draught | Газене на кораба | Calado | ponor plavidla | Fartøjets dybgang | Schiffstiefgang | Laeva süvis | Βύθισμα σκάφους | Tirant d'eau du bateau | Gaz broda | pescaggio natante | Kuģa iegrime | Laivo grimzlė |
| AVALEN | available length | Допустима дължина | Eslora disponible | povolená délka | Disponibel længde | verfügbare Länge | Kasutatav pikkus | Διαθέσιμο μήκος | Longueur disponible | Raspoloživa duljina | lunghezza disponibile | Pieļaujamais garums | Leidžiamas ilgis |
| CLEHEI | clearance height | Свободна височина | Gálibo vertical | podjezdná výška | Frigang i højden | Durchfahrtshöhe | Kuja kõrgus | Ελεύθερο ύψος διέλευσης | Hauteur libre | Visina plovnog otvora | tirante d'aria | Pieļaujamais augstums | Leidžiamas aukštis |
| CLEWID | clearance width | Свободна ширина | Gálibo horizontal | průjezdná šířka | Frigang, bredde | Durchfahrtsbreite | Kuja laius | Ελεύθερο πλάτος διέλευσης | Largeur disponible | Širina plovnog otvora | larghezza della via navigabile | Pieļaujamais platums | Leidžiamas plotis |
| AVADEP | available depth | Допустимо газене | Profundidad disponible | využitelná hloubka | Vanddybde | verfügbare Tiefe | Kasutatav sügavus | Διαθέσιμο πλάτος | Mouillage disponible | Raspoloživa dubina | pescaggio massimo | Ūdens dziļums | Esamas gylis |
| NOMOOR | no mooring | Забранено швартоване | Prohibición de amarre | zákaz vyvazování | Fortøjning forbudt | Festmacheverbot | Sildumine keelatud | Απαγόρευση αγκυροβολίας | Interdiction d'amarrage | Zabranjen vez | divieto di ormeggio | Pietauvošanās aizliegta | Draudžiama švartuotis |
| SERVIC | changed service | Променено обслужване | Servicio limitado | omezení provozu | Ændret betjening | geänderte Betriebszeiten | Piiratud teenindus | Περιορισμένη υπηρεσία | Exploitation limitée | Ograničena usluga | servizio / esercizio limitato | Ierobežots pakalpojums | Ribotas aptarnavimas |
| NOSERV | no service | Няма обслужване | Interrupción del servicio | zastavení provozu | Ingen betjening | kein Betrieb | Ei teenindata | Καμία υπηρεσία | Navigation interrompue | Nema usluge | nessun servizio / esercizio | Pakalpojums nav pieejams | Neaptarnaujama |
| SPEED | speed limit | Ограничение на скорост | Límite de velocidad | omezení rychlosti | Hastighedsbegrænsning | Höchstgeschwindigkeit | Kiiruspiirang | Όριο ταχύτητας | Limite de Vitesse | Ograničenje brzine | limite di velocità | Ātruma ierobežojums | Ribojamas greitis |
| WAVWAS | no wash of waves | Забранено създаване на вълни | No crear oleaje | zákaz vytvářet vlnobití a sání | Undgå at lave efterdønninger | Sog und Wellenschlag vermeiden | Voolu tekitamine keelatud | Απαγόρευση πρόκλησης κυματισμών | Remous interdits | Zabranjeno pravljenje valova | divieto di moto ondoso | Neradīt viļņus | Nekelti bangų |
| PASSIN | no passing | Забранено преминаване | Prohibido el paso | zákaz potkávání | Passage er ikke tilladt | Begegnungsverbot | Läbimine keelatud | Απαγόρευση διέλευσης | Interdiction de croiser | Zabranjen prolaz | divieto di transito | Aizliegts šķērsot | Plaukti draudžiama |
| ANCHOR | no anchoring | Забранено заставането на котва | Prohibido fondear | zákaz kotvení | Opankring ikke tilladt | Ankerverbot | Ankrusse jäämine keelatud | Απαγόρευση αγκυροβολίας | Ancrage interdit | Zabranjeno sidrenje | divieto di ancoraggio | Noenkuroties aizliegts | Draudžiama nuleisti inkarą |
| OVRTAK | no overtaking | Забранено изпреварване | Prohibido adelantar | zákaz předjíždění | Overhaling ikke tilladt | Überholverbot | Möödasõit keelatud | Απαγόρευση προσπέρασης | Dépassement interdit | Zabranjeno pretjecanje | divieto di sorpasso | Apdzīt aizliegts | Lenkti draudžiama |
| MINPWR | minimum power | Минимална мощност | Potencia mínima | minimální výkon | Minimum kraft | Mindestantriebsleistung | Minimaalne võimsus | Ελάχιστη ισχύς | Puissance minimum | Minimalna snaga | potenza minima | Minimālā jauda | Mažiausia galia |
| ALTER | alternate traffic direction | Еднопосочно движение | Tráfico en sentido alterno | střídavý směr plavby | Skiftende færdselsretning | Einbahnverkehr | Asendus-liiklussuund | Εναλλασσόμενη κατεύθυνση κυκλοφορίας | navigation alternée | Naizmjeničan smjer prometa | traffico in senso alternato | divvirzienu satiksme | Keičiama laivų eismo kryptis |
| CAUTIO | special caution | Особено внимание | Precaución especial | zvýšená opatrnost | Særlig agtpågivenhed | besondere Vorsicht | Äärmine ettevaatus | Ιδιαίτερη προσοχή | attention spéciale | Poseban oprez | particolare cautela | īpaša piesardzība | Ypatingas perspėjimas |
| NOLIM | no limitation | Без ограничение | Sin limitaciones | bez omezení | Ingen begrænsninger | keine Einschränkung | Piirang puudub | Κανένας περιορισμός | pas de limitation | Bez ograničenja | nessuna limitazione | bez ierobežojumiem | Apribojimų pabaiga |
| TURNIN | no turning | Забранено извършване на поворот | Prohibido girar | zákaz provádět obrat | Vending ikke tilladt | Wendeverbot | Pööramine keelatud | Απαγόρευση στροφής | Interdiction de virer | Zabranjeno okretanje | divieto di manovra | pagriezties aizliegts | Apsisukti draudžiama |
| NOSHORE | not allowed to go ashore | Забранено слизането на брега | Prohibido desembarcar | zákaz vystupovat na břeh | Ikke tilladt at gå i land | Landgangverbot | Maaleminek keelatud | Απαγόρευση αποβίβασης | Interdiction de débarquer | Zabranjen izlazak na obalu | divieto di approdo | doties krastā aizliegts | Išlipti į krantą draudžiama |
| CONBRE | convoy breadth | Ширина на състава | Manga del convoy | šířka sestavy | Konvojbredde | Verbandsbreite | Konvoi laius | Πλάτος νηοπομπής | Largeur du convoi | Širina sastava | larghezza del convoglio | karavānas platums | Laivų vilkstinės plotis |
| CONLEN | convoy length | Дължина на състава | Eslora del convoy | délka sestavy | Konvojlængde | Verbandslänge | Konvoi pikkus | Μήκος νηοπομπής | Longueur du convoi | Duljina sastava | lunghezza del convoglio | karavānas garums | Laivų vilkstinės ilgis |
| LEADEP | least depth sounded | Минимална дълбочина | Profundidad mínima medida | minimální změřená hloubka | Mindste loddede dybde | minimale Tiefe | Looditud väikseim sügavus | Μικρότερο μετρηθέν βάθος | Profondeur minimale | Minimalna dubina | profondità minima rilevata | Mazākais izmērītais dziļums | Mažiausias gylis |
| NOBERT | no berthing | Забранена стоянка (на котва или на вързала към брега) | Prohibido atracar | zákaz stání | Ikke tilladt at lægge til kaj | Stillliegeverbot | Sildumine keelatud | Απαγόρευση πρόσδεσης | Interdiction de stationner | Zabranjeno pristajanje | divieto di attracco | doties uz piestātni aizliegts | Švartuotis draudžiama |

**CÓDIGO DE RESTRIÇÕES**

| OBSTRU | zárlat | ostaklu | Stremming | Zamknięcie | Obstrução | blocaj | blokáda | zapora | Este | Blockering | Закрыто | Препрека |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PAROBS | részleges tilalom | ostaklu parzjali | Gedeeltelijke stremming | Częściowe zamknięcie | Obstrução parcial | restricție parțială | čiastočné prekážky | delna zapora | Osittainen este | Delvis obstruktion | Частично закрыто | Делимична препрека |
| DELAY | késedelem | dewmien | Oponthoud | Opóźnienie | Demora | întârziere | meškanie | zamuda | Viivästys | Försening | Задержка | Кашњење |
| VESLEN | hajóhossz | tul tal-bastiment | Scheepslengte | Długość statku | Comprimento (embarcação) | lungimea navei | dĺžka plavidla | dolžina plovila | Aluksen pituus | Fartygslängd | Длина судна | Дужина пловила |
| VESHEI | hajó magassága | għoli tal-bastiment | Scheepshoogte | Wysokość statku | Altura acima da linha de água (embarcação) | înălțimea deasupra liniei de plutire | výška plavidla nad hladinou | prosta višina plovila | Aluksen suurin korkeus vedenpinnasta | Fartygets höjd över vattenytan | Высота судна | Максимална висина пловила над водом |
| VESBRE | hajó szélessége | wisa’ tal-bastiment | Scheepsbreedte | Szerokość statku | Boca (embarcação) | lățimea navei | šírka plavidla | širina plovila | Aluksen leveys | Fartygsbredd | Ширина судна | Ширина пловила |
| VESDRA | hajó merülése | fundar meħtieġ għall-bastiment | Diepgang | Zanurzenie statku | Calado (embarcação) | pescajul navei | ponor plavidla | ugrez plovila | Aluksen syväys | Fartygets djupgående | Осадка | Газ пловила |
| AVALEN | rendelkezésre álló hosszúság | tul disponibbli | Doorvaartlengte | Długość użytkowa | Comprimento disponível | lungimea admisă | dostupná dĺžka | razpoložljiva dolžina | Käytettävissä oleva pituus | Tillgänglig längd | Ограничение длины | Расположива дужина |
| CLEHEI | szabad űrszelvény magasság | fond ta’ spazju ħieles | Doorvaarthoogte | Wysokość w świetle | Altura livre | gabaritul de înălțime | podjazdná výška | prosta višina prehoda | Alikulkukorkeus | Frihöjd | ограничение высоты | Слободна висина |
| CLEWID | rendelkezésre álló szélesség | wisa’ ta’ spazju ħieles | Doorvaartbreedte | Szerokość w świetle | Largura livre | gabaritul de lățime | prejazdná šírka | prosta širina prehoda | Käytettävissä oleva leveys | Farledsbredd | Ограничение ширины | Слободна ширина |
| AVADEP | rendelkezésre álló vízmélység | fond disponibbli | Beschikbare diepte | Głębokość użytkowa | Profundidade disponível | adâncimea disponibilă | dostupná hĺbka | razpoložljiva globina | Käytettävissä oleva syväys | Tillgängligt djup | Существующая глубина | Расположива дубина |
| NOMOOR | veszteglési tilalom | irmiġġ projbit | Afmeerverbod | Zakaz cumowania | Proibição de amarrar | interdicție de acostare | zákaz vyväzovania | prepovedan privez | Kiinnittyminen kielletty | Förtöjning förbjuden | Швартовка запрещена | Забрањено везивање |
| SERVIC | megváltozott üzem | servizz modifikat | Beperkte service | Usługa ograniczona | Serviço limitado | manevră restricționată | zmenená prevádzka | spremenjena storitev | Rajoitettu palvelu | Begränsad service | Изменения в обслуживании | Измењена услуга |
| NOSERV | üzemszünet | servizz sospiż | Geen bediening | Usługa niedostępna | Interrupção do serviço | manevră interzisă | zastavená prevádzka | ni storitve | Ei palvelua | Ingen service | Не обслуживаемое | Без услуге |
| SPEED | sebességkorlátozás | limitu tal-veloċità | Snelheidsbeperking | Ograniczenie prędkości | Limite de velocidade | limită de viteză | najvysššia povolená rýchlosť | omejitev hitrosti | Nopeusrajoitus | Hastighets-begränsning | Ограничение скорости | Ограничење брзине |
| WAVWAS | hullámkeltést elkerülni | tranja tal-mewġ projbita | Golfslag vermijden | Zakaz tworzenia fal | Não causar ondulação | formarea valurilor interzisă | zákaz vlnobitia a sania | prepovedano povzročanje valov | Voimakkaan aallokon tuottaminen kielletty | Undvik svall | Не создавай волнения | Забрањено прављење таласа |
| PASSIN | találkozás tilos | passaġġ projbit | Ontmoeten verboden | Zakaz wymijania | Proibição de passar | traversarea interzisă | zákaz stretávania | prepovedan prehod | Ei läpikulkua | Passering förbjuden | Нет прохода | Забрањен пролаз |
| ANCHOR | horgonyozni tilos | ankraġġ projbit | Ankeren verboden | Zakaz kotwiczenia | Proibição de ancorar | ancorarea interzisă | zákaz kotvenia | prepovedano sidranje | Ei ankkuroitumista | Ankring förbjuden | Якорная стоянка запрещена | Забрањено сидрење |
| OVRTAK | előzni tilos | projbit il-qbiż ta’ bastimenti oħra | Voorbijlopen verboden | Zakaz wyprzedzania | Proibição de cruzar ou ultrapassar | depășirea interzisă | zákaz predchádzania | prepovedano prehitevanje | Ei ohittamista | Omkörning förbjuden | Обгон запрещен | Забрањено престизање |
| MINPWR | minimális teljesítmény | potenza minima | Minimaal vermogen | Minimalna moc napędu | Potência mínima | putere minimă | minimálny výkon | najmanjša moč | Vähimmäisteho | Minsta motoreffekt | минимальная мощность | Минимална снага |
| ALTER | váltakozó forgalmi irány | direzzjoni alternata tat-traffiku | Beurtelings verkeer | Ruch naprzemienny | Sentido alternado | trafic cu sensuri alternative | striedajúci sa smer premávky | izmenično usmerjanje prometa | vaihteleva liikenteen suunta | Alternerande farleds-riktning | Встречное движение | Наизменични смер кретања |
| CAUTIO | kiemelt óvatosság | attenzjoni speċjali | Bijzondere voorzichtigheid | Szczególna ostrożność | Atenção especial | vigilență mărită | zvýšená opatrnosť | posebna pozornost | erikoisvaroitus | Varning | Соблюдай осторожность | Посебан опрез |
| NOLIM | nincs korlátozás | ebda restrizzjoni | Geen beperking | Koniec ograniczeń | Sem restrições | fără restricții | bez obmedzenia | brez omejitve | ei rajoitusta | Ingen begränsning | Без ограничений | Без ограничења |
| TURNIN | megfordulni tilos | dawran projbit | Draaien verboden | Zakaz zawracania | Proibição de inverter marcha | întoarcerea interzisă | zákaz vykonávania obratov | prepovedano obračanje | Kääntyminen kielletty | Vändning förbjuden | Поворот запрещен | Забрањено окретање |
| NOSHORE | partfuttatás tilos | żbark projbit | Aan wal gaan verboden | Brak pozwolenia wejścia na ląd | Proibição de ir a terra | nu este permis accesul la mal | zákaz vystupovať na breh | prepovedano izkrcanje | Maihinnousu kielletty | Ej tillåtelse att gå i land | Запрещен выход на берег | Забрањен излазак на обалу |
| CONBRE | kötelék szélesség | wisa’ tal-konvoj | Breedte van de duwsleep | Szerokość zestawu | Largura do comboio | lățimea convoiului | šírka zostavy | širina konvoja | kytkyeen leveys | Konvojbredd | Ширина состава судов | Ширина састава |
| CONLEN | kötelék hossz | tul tal-konvoj | Lengte van de duwsleep | Długość zestawu | Comprimento do comboio | lungimea convoiului | dĺžka zostavy | dolžina konvoja | kytkyeen pituus | Konvojlängd | Длина состава судов | Дужина састава |
| LEADEP | minimális mélység | l-inqas fond imkejjel | Minst gepeilde diepte | Najmniejsza zmierzona głębokość | Profundidade mínima medida | adâncimea minimă | najnižšia nameraná hĺbka | najmanjša izmerjena globina | matalin luodattu syvyys | Minsta lodade djup | Минимальная глубина | Најмања измерена дубина |
| NOBERT | veszteglési tilalom | irmiġġ projbit | Aanleggen verboden | Zakaz cumowanie | Proibição de atracar | amararea interzisă | zákaz státia | prepovedan pristanek | Laituriin kiinnittäminen kielletty | Tilläggning förbjuden | Швартовка запрещена | Забрана пристајања |

**CÓDIGO DE MEDIDA**

| DIS | discharge | Отток | Descarga | průtok | Udledning | Abfluss | Lossimine | Εκφόρτωση | Débit | Protok | portata | Ūdens novadīšana | Vandens išleidimas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| REG | regime | Режим | Régimen | režim | Vandregime | Regime | Kord | Κατάσταση ροής υδάτων | Régime | Režim | regime | Darba režīms | Režimas |
| BAR | barrage status | Състояние на бента | Estado presa | stav vzdutí | Status for dæmning | Wehrstellung | Paisu asend | Κατάσταση φράγματος | Statuts des barrages | Status brane | stato sbarramento | Aizsprosta stāvoklis | Užtvaros padėtis |
| VER | vertical clearance | Свободна височина (габарит) | Gálibo libre | podjezdná výška | Lodret frigang | Durchfahrthöhe | Läbisõidu-kõrgus | Ελεύθερο ύψος | Hauteur libre maximum | Visina slobodnog prolaza | tirante d'aria | Pieļaujamais augstums | Laivo kelio aukštis |
| LSD | least sounded depth | Минимална дълбочина | Profundidad mínima medida | minimální změřená hloubka | Mindste loddede dybde | minimale Tiefe | Looditud väikseim sügavus | Μικρότερο μετρηθέν βάθος | Profondeur minimale | Minimalna dubina | profondità minima rilevata | Minimālais dziļums | Mažiausias gylis |
| WAL | water level | Водно ниво | Nivel de agua | vodní stav | Vandstand | Wasserstand | Veetase | Στάθμη υδάτων | Niveaux des eaux | Vodostaj | livello idrometrico | Ūdens līmenis | Vandens lygis |
| NOM | no measurement | Няма измерване | Sin medida | žádné měření | Ingen måling | kein Messwert | Ei mõõdeta | Καμία μέτρηση | Pas de mesure | Nema mjerenja | nessuna misurazione | nav mērījuma | Neišmatuota |

**CÓDIGO DE MEDIDA**

| DIS | lefolyás | ħruġ ta’ ilma | Afvoer | Spust | Descarga | debit | prietok | pretok | Virtaus | Utsläpp | Спуск воды | Протицај |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| REG | vízjárás | rata tal-fluss | Regime | Reżim | Regime | regim | režim | režim | Vedenkorkeussuhteet | Ordning | Судоходный режим | Режим |
| BAR | duzzasztási állapot | status tal-milqgħa | Stuwstand | Stan zapory | Status da barragem | starea barajului | stav hate | položaj zapor | Avattavan padon tilanne | Fördämningsstatus | Состояние плотины | Статус преграде |
| VER | szabad űrszelvény-magasság | fond ħieles | Doorvaarthoogte | Prześwit pionowy | Altura livre | înălțime liberă de trecere | podjazdná výška | prosta višina prehoda | Alikulkukorkeus | Frihöjd | Высота судоходного пролёта | Расположива висина пролаза |
| LSD | legkisebb vízmélység | l-inqas fond imkejjel | Minst gepeilde diepte | Głębokość minimalna | Profundidade mínima medida | adâncimea minimă | najnižšia nameraná hĺbka | najmanjša izmerjena globina | Matalin luodattu syvyys | Minsta lodade djup | Минимальная глубина | Најмања измерена дубина |
| WAL | vízállás | livell tal-ilma | Waterstand | Stan wody | Nível da água | nivelul apei | vodný stav | vodostaj | Vedenkorkeus | Vattennivå | Уровень воды | Ниво воде |
| NOM | nincs mérési adat | ebda kejl | Geen meting | Brak pomiaru | Sem medição | măsurători lipsă | žiadna nameraná hodnota | ni meritve | ei mitattu | Ingen mätning | Нет измерений | Нема мерења |

**POSITION CODE**

| AL | all | Навсякъде (всички направления) | Todo | vše | Alt | ganz | Kõik | Ολόκληρη η πλωτή οδός | Tout le chenal | Svi smjerovi | intero canale navigabile | Laba redzamība | Visur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LE | left | Ляво | Izquierda | vlevo | Venstre | links | Vasakpoolne | Αριστερά | Gauche | Lijevo | sinistra | Pa kreisi | Kairė |
| MI | middle | В средата | Centro | střed | Midten | Mitte | Keskmine | Στο μέσο | Milieu | Sredina | centro | Vidū | Vidurys |
| RI | right | Дясно | Derecha | vpravo | Højre | rechts | Parempoolne | Δεξιά | Droite | Desno | destra | Pa labi | Dešinė |
| LB | left bank | Ляв бряг | Margen izquierda | levý břeh | Venstre bred | linkes Ufer | Vasak kallas | Αριστερή όχθη | Rive gauche | Lijeva obala | sponda sinistra | Kreisais krasts | Kairysis krantas |
| RB | right bank | Десен бряг | Margen derecha | pravý břeh | Højre bred | rechtes Ufer | Parem kallas | Δεξιά όχθη | Rive droite | Desna obala | sponda destra | Labais krasts | Dešinysis krantas |
| N | north | Северно | Norte | sever | Nord | Nord | põhi | Βόρεια | Nord | Sjeverno | nord | Uz ziemeļiem | Šiaurė |
| NE | north-east | Североизточно | Noreste | severovýchod | Nordøst | Nord-Ost | kirre | Βορειοανατολικά | Nord-est | Sjeveroistočno | nord-est | Uz ziemeļaustrumiem | Šiaurės rytai |
| E | east | Източно | Este | východ | Øst | Ost | ida | Ανατολικά | Est | Istočno | est | Uz austrumiem | Rytai |
| SE | south-east | Югоизточно | Sureste | jihovýchod | Sydøst | Süd-Ost | kagu | Νοτιοανατολικά | Sud-est | Jugoistočno | sud-est | UZ dienvidaustrumiem | Pietryčiai |
| S | south | Южно | Sur | jih | Syd | Süd | lõuna | Νότια | Sud | Južno | sud | Uz dienvidiem | Pietūs |
| SW | south-west | Югозападно | Suroeste | jihozápad | Sydvest | Süd-West | edel | Νοτιοδυτικά | Sud-ouest | Jugozapadno | sud-ovest | Uz dienvidrietumiem | Pietvakariai |
| W | west | Западно | Oeste | západ | Vest | West | lääs | Δυτικά | Ouest | Zapadno | ovest | Uz rietumiem | Vakarai |
| NW | north-west | Северозападно | Noroeste | severozápad | Nordvest | Nord-West | loe | Βορειοδυτικά | Nord-ouest | Sjeverozapadno | nord-ovest | Uz ziemeļrietumiem | Šiaurės vakarai |
| BI | big | Голям | Grande | velký | Stor | groß | suur | Μεγάλο | grand | Velik | grande | liels | Didelis |
| SM | small | Малък | Pequeño | malý | Lille | klein | väike | Μικρό | petit | Mali | piccolo | mazs | Mažas |
| OL | old | Стар | Antiguo | starý | Gammel | alt | vana | Παλαιό | vieux | Star | vecchio | vecs | Senas |
| EW | new | Нов | Nuevo | nový | Ny | neu | uus | Νέο | nouveau | Nov | nuovo | jauns | Naujas |
| MP | movable part | Подвижна част | Parte móvil | pohyblivá část | Bevægelig del | beweglicher Teil | avatav osa | Κινητό τμήμα | partie amovible | Pokretni dio | parte mobile | kustīgā daļa | Slankioji dalis |
| FP | fixed part | Неподвижна част | Parte fija | pevná část | Fast del | fester Teil | fikseeritud osa | Σταθερό τμήμα | partie fixe | Nepokretni dio | parte fissa | nekustīgā daļa | Stacionarioji dalis |
| VA | variable | променлив | Variable | proměnlivé | Variabel | veränderlich | muutuv | Μεταβλητό | variable | Promjenjivo | variabile | mainīgs | Kintamas |
| GY | green buoy | Зелен буй | Boya verde | zelená bóje | Grøn bøje | grüne Boje | roheline poi | Πράσινος σημαντήρας | bouée verte | Zelena plutača | boa verde | zaļa boja | Žalias plūduras |
| RY | red buoy | Червен буй | Boya roja | červená bóje | Rød bøje | rote Boje | punane poi | Κόκκινος σημαντήρας | bouée rouge | Crvena plutača | boa rossa | sarkana boja | Raudonas plūduras |

**POSITION CODE**

| AL | mind/teljesen | kollha | Geheel | wszędzie | Todas | toată calea navigabilă / întregul obiect | všetky | vse | Kaikki | Hela | Все направления | Све |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LE | bal | xellug | Links | po lewej | Esquerda | stânga | vľavo | levo | Vasen | Vänster | Слева | Лево |
| MI | közép | nofs | Midden | pośrodku | Centro | mijloc | v strede | sredina | Keskimmäinen | Mitten | В середине | Средина |
| RI | jobb | lemin | Rechts | po prawej | Direita | dreapta | vpravo | desno | Oikea | Höger | Справа | Десно |
| LB | bal part | xatt tax-xellug | Linkeroever | lewy brzeg | Margem esquerda | malul stâng | ľavý breh | levi breg | Vasen ranta | Vänstra banken | Левый берег | Лева обала |
| RB | jobb part | xatt tal-lemin | Rechteroever | prawy brzeg | Margem direita | malul drept | pravý breh | desni breg | Oikea ranta | Högra banken | Правый берег | Десна обала |
| N | észak | it-Tramuntana | Noord | północ | Norte | nord | severne | severno | Pohjoinen | Nord | К северу | Север |
| NE | észak-kelet | il-Grigal | Noordoost | północny wschód | Nordeste | nord-est | severo-východne | severovzhodno | Koillinen | Nordost | К северо-востоку | Североисток |
| E | kelet | il-Lvant | Oost | wschód | Leste | est | východne | vzhodno | Itä | Öst | К востоку | Исток |
| SE | dél-kelet | ix-Xlokk | Zuidoost | południowy wschód | Sudeste | sud-est | juho-východne | jugovzhodno | Kaakko | Sydost | К юго-востоку | Југоисток |
| S | dél | in-Nofsinhar | Zuid | południe | Sul | sud | južne | južno | Etelä | Syd | К югу | Југ |
| SW | dél-nyugat | il-Lbiċ | Zuidwest | południowy zachód | Sudoeste | sud-vest | juho-západne | jugozahodno | Lounas | Sydväst | К юго-западу | Југозапад |
| W | nyugat | il-Punent | West | zachód | Oeste | vest | západne | zahodno | Länsi | Väst | К западу | Запад |
| NW | észak-nyugat | il-Majjistral | Noordwest | północny zachód | Noroeste | nord-vest | severo-západne | severozahodno | Luode | Nordväst | К северо-западу | Северозапад |
| BI | nagy | kbir | Groot | duży | Grande | mare | veľký | velik | iso | Stor | большой | Велики |
| SM | kicsi | żgħir | Klein | mały | Pequeno | mic | malý | majhen | pieni | Liten | малый | Мали |
| OL | régi | qadim | Oud | stary | Antigo | vechi | starý | star | vanha | Gammal | старый | Стари |
| EW | új | ġdid | Nieuw | nowy | Novo | nou | nový | nov | uusi | Ny | новый | Нови |
| MP | mozgatható rész | parti mobbli | Beweegbaar deel | część ruchoma | Parte móvel | parte amovibilă | pohyblivá časť | premični del | liikkuva osa | Rörlig del | подвижная часть | Покретан део |
| FP | rögzített rész | parti fissa | Vast deel | część stała | Parte fixa | parte fixã | pevná časť | fiksni del | kiinteä osa | Fast del | неподвижная часть | Непокретан део |
| VA | változó | varjabbli | Variabel | zmienny | Variável | parte variabilă | premenlivá | spremenljiv | vaihtelee | Variabel | переменный | Променљива |
| GY | zöld úszó | baga ħadra | Groene boei | zielona pława | Boia verde | geaman- dura verde | zelená bója | zelena boja | vihreä poiju | Grön boj | зелёный буй | Зелена бова |
| RY | piros úszó | baga ħamra | Rode boei | czerwona pława | Boia vermelha | geaman-durã roșie | červená bója | rdeča boja | punainen poiju | Röd boj | красный буй | Црвена бова |

**REASON CODE**

| EVENT | event | Случай | Suceso | událost | Begivenhed | Veranstaltung | Sündmus | Συμβάν | Evénement | Događaj | avvenimento | Pasākums | Įvykis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WORK | work | Работи (действия) | Obras | práce | Arbejder | Arbeiten | Töötamine | Εργασίες | Travaux | Radovi | lavori | Darbs | Darbai |
| DREDGE | dredging | Драгажни работи | Dragado | bagrování | Opmudring | Baggerarbeiten | Süvendamine | Βυθοκόρηση | Dragage | Iskapanje | dragaggio | Bagarēšanas darbi | Dugno gilinimas |
| EXERC | exercises | Упражнения | Ejercicios | cvičení | Øvelser | Übungen | Õppused | Ασκήσεις | exercices | Vježbe | esercitazioni | Vingrinājumi | Pratybos |
| HIGWAT | high water | Високи води | Nivel de agua elevado | vysoký vodní stav | Højvande | Hochwasser | Kõrgvesi | Υψηλή στάθμη υδάτων | Crue | Visok vodostaj | piena | Augsts ūdens līmenis | Aukštas vandens lygis |
| HIWAI | water level of cautious navigation | Водно ниво изискващо повишено внимание при корабоплаване | Nivel de agua para navegación prudente | vodní stav zvýšené opatrnosti plavby | Forsigtig sejlads pga. vandstanden | Marke I. | Ettevaatliku laevatamise veetase | Στάθμη υδάτων προσεκτικής ναυσιπλοΐας | Niveau d'eau nécessitant une navigation prudente | Vodostaj oprezne plovidbe | livello idrometrico di prudenza per la navigazione | Ūdens līmenis bīstams kuģošanai | Laivybai pavojingas vandens lygis |
| HIWAII | prohibitory water level | Водно ниво възпрепятстващо корабоплаването | Nivel de agua de prohibición | vodní stav, při kterém je zakázaná plavba | Forbud mod sejlads pga. vandstanden | Marke II oder Marke III | Laevatamiseks keelatud veetase | Απαγορευτική στάθμη υδάτων | Niveau d'eau d'interdiction | Vodostaj zabrane plovidbe | livello idrometrico proibitivo | Ūdens līmenis, kurā kuģošana aizliegta | Laivybą draudžiantis vandens lygis |
| LOWWAT | low water | Ниски води | Nivel de agua bajo | nízký vodní stav | Lavvande | Niedrigwasser | Madal vesi | Χαμηλή στάθμη υδάτων | Etiage | Nizak vodostaj | livello di magra | Zems ūdens līmenis | Žemas vandens lygis |
| SHALLO | siltation | Плитчина | Sedimentación | naplaveniny | Aflejringer | Versandung | Mudastumine | Σχηματισμός ιλύος | Atterissement | Pličina | accumulo di sabbia | Aizsērēšana | Sąnašos |
| CALAMI | calamity | Бедствие | Accidente | havárie | Nødsituation | Havarie | Õnnetus | Καταστροφή | Accident | Havarija | calamità | Negadījums | Avarija |
| LAUNCH | launching | Спускане на вода | Lanzamiento | spouštění na vodu | Søsætning | Stapellauf | Veeskamine | Καθέλκυση | Mise à l'eau | Porinuće | varo | Kuģa nolaišana ūdenī | Laivo nuleidimas į vandenį |
| DECLEV | lowering water level | Понижаване на водното ниво | Nivel de agua en descenso | pokles vodní hladiny | Vandstanden sænkes | Senken des Wasserspiegels | Veetaseme vähenemine | Μειούμενη στάθμη υδάτων | Abaissement du niveau de l'eau | Vodostaj u opadanju | calo del livello idrometrico | Ūdens līmeņa pazemināšana | Vandens lygio slūgimas |
| FLOMEA | flow measurement | Измерване на оттока | Medición de caudal | měření průtoku | Flowmåling | Strömungsmessung | Voolu mõõtmine | Μέτρηση ροής | Opération de mesure de débit | Mjerenje protoka | portata idrometrica | Straumes ātruma noteikšana | Tėkmės parametrų matavimas |
| BLDWRK | building work | Строителни работи | Obras de construcción | stavební práce | Anlægsarbejder | Bauarbeiten | Ehitustöö | Κατασκευαστικές εργασίες | Travaux de construction | Izgradnja | lavori di costruzione | Būvdarbi | Statybos |
| REPAIR | repair | Ремонтни работи | Reparación | opravy | Reparation | Reparaturarbeiten | Remont | Επισκευές | Travaux de réparation | Popravci | intervento di riparazione | Remonts | Remontas |
| INSPEC | inspection | Инспекция | Inspección | inspekce | Inspektion | Inspektion | Inspekteeri-mine | Επιθεώρηση | Inspection | Inspekcija | ispezione | Inspekcija | Apžiūra |
| FIRWRK | fireworks | Взривни работи | Fuegos artificiales | ohňostroj | Fyrværkeri | Feuerwerk | Ilutulestik | Πυροτεχνήματα | Feux d'artifice | Vatromet | fuochi d'artificio | Liesmu darbi | Fejerverkai |
| LIMITA | limitations | Ограничения | limitaciones | omezení | Begrænsninger | Einschränkungen | Piirangud | Περιορισμοί | restriction de la navigation | Ograničenja | limitazioni alla navigazione | Ierobežojumi | Apribojimai |
| CHGFWY | changes of the fairway | Изменение на фарватера | Cambios en vía navegable | změny plavební dráhy | Ændring af farvandet | Änderungen des Fahrwassers | Muudatused faarvaatris | Μεταβολές στον δίαυλο | modification du chenal navigable | Promjene u plovnom putu | modifiche del canale navigabile | Izmaiņas kuģu ceļā | Pasikeitimai farvateryje |
| CONSTR | constriction of fairway | Изграждане на воден път | Estrechamiento de vía navegable | zúžení vodní cesty | Indsnævring af vandvejen | Einengung des Fahrwassers | Faarvaatri kontriktsioon | Κατασκευή πλωτής οδού | rétrécissement du chenal navigable | Suženje plovnog puta | restrizione del canale navigabile | Ūdens ceļa sašaurinājums | Farvaterio susiaurėjimas |
| DIVING | diver under the water | Водолаз под водата | Presencia de submarinistas | práce pod vodou | Dykkere i arbejde | Taucher unter Wasser | Tuuker vee all | Υποβρύχιες εργασίες | plongeurs au travail | Ronilac pod vodom | sommozzatore in immersione | Ūdenslīdēju darbi | Vandenyje naras |
| SPECTR | special transport | Специализиран транспорт | Transporte especial | zvláštní přeprava | Særlig transport | Sondertransport | Erivedu | Ειδικές μεταφορές | transport spécial | Specijalni prijevoz | trasporto speciale | Īpašs transports | Specialus transportas |
| EXT | extensive sluicing | Активно изпускане на вода | Barrido extensivo | rozsáhlé vymílání | Omfattende slusedrift | extreme Dotierung | Laialdane lüüsikasutus | Εκτεταμένη εκκένωση υδατοφράτκη | Service étendu | Izrazito istjecanje | regolazione intensiva della portata idrometrica | Liela pārplūde | Gausus vandens nuleidimas |
| MIN | minimum sluicing | Минимално изпускане на вода | Barrido mínimo | minimální vymílání | Minimum slusedrift | minimale Dotierung | Minimaalne lüüsikasutus | Ελάχιστη εκκένωση υδατοφράκτη | Service minimum | Minimalno istjecanje | regolazione minima della portata idrometrica | Minimāla pārplūde | Minimalus vandens nuleidimas |
| SOUND | sounding works | Дълбочинно-измервателни работи | Obras de sondeo | měřenί plavební hloubky | Oplodning | Peilarbeiten | Loodimistööd | Εργασίες ηχοβολισμού | Travaux de sondage | Mjerenja dubine | lavori di scandaglio | Zondēšana | Zondavimo darbai |
| OTHER | others | Друго | Otros | jiné | Andet | andere | Muud | Λοιπά | Autres | Ostalo | diversi | Citi | Kita |
| INFSER | info service | Информационна служба (няма значение за безопасността на корабоплаването и не изисква планиране на рейса) | Servicio de información | Informační servis (netýká se bezpečnosti ani plánování plavby) | Informationstjeneste | Informationsservice | Teabeteenus (ei ole seotud ohutusega ega ole vajalik reisi korraldamisel) | Πληροφορίες (δεν έχει σχέση με την ασφάλεια και δεν χρειάζεται για τον προγραμματισμό του ταξιδίου) | Information (n'a pas d'impact sur la sécurité et n'est pas nécessaire au calcul d'itinéraire) | Informacijska usluga (ne odnosi se na sigurnost i nije potrebna za planiranje putovanja) | servizio informazioni (senza rilevanza ai fini della sicurezza e della pianificazione dell'itinerario) | Informācijas dienests (nav saistīts ar drošumu un nav vajadzīgs reisa plānošanai) | Informacija (nesusijusi su saugumu ir nebūtina planuojant reisą) |
| STRIKE | strike | Удар | Huelga | stávka | Strejke | Streik | Streik | Απεργία | Grève | Štrajk | sciopero | Streiks | Streikas |
| FLOMAT | floating material | Плаващи материали | Material flotante | plovoucí materiál | Flydende materiel | Treibgut | Ujuvmaterjal | Υλικό που επιπλέει | Embâcle | Plutajući predmeti | materiale flottante | Peldošs objekts | Plūduriuojantys daiktai |
| EXPLOS | explosives clearing operation | Взривни работи за разчистване | Operación de limpieza con explosivos | zneškodňování výbušnin | Rydning af sprængstoffer | Bombenräumung | Demineerimisoperatsioon | Επιχείριση άρσης ναρκοπεδίου | opération de déminage | Raščišćavanje eksplozivom | operazione di sminamento | Sprāgstvielu neitralizēšanas operācija | Sprogmenų šalinimo operacija |
| OBUNWA | obstruction under water | Подводно препятствие | Obstrucción bajo el agua | plavební překážka | Hindring under vandlinjen | Einschränkung unter Wasser | Veealune takistus | Υποβρύχια παρεμπόδιση | objet immergé | Prepreka ispod vode | ostruzione sommersa | Zemūdens šķērslis | Povandeninė kliūtis |
| FALMAT | falling material | Падащи материали | Material desprendido | padající materiál | Faldende materiel | herabfallende Gegenstände | Kukkuvad esemed | Πτώση αντικειμένων | chutes d’objets | Padajući predmeti s visine | caduta di materiale | Krītošs objekts | Krentantys daiktai |
| DAMMAR | damaged marks/signs | Повредена сигнализация/знаци | Marcas/señales estropeadas | poškozená signalizace | Beskadigede sømærker/skiltning | beschädigte Zeichen | Kahjustatud märgid/viidad | Κατεστραμμένα σημεία/σήματα | panneaux de signalisation endommagés | Oštećene oznake | segnaletica danneggiata | Bojātas zīmes/norādes | Pažeistos žymos / ženklai |
| HEARIS | health risk | Опасност за здравето | Riesgo para la salud | zdravotní riziko | Sundhedsrisiko | Gesundheitsgefahr | Terviseoht | Κίνδυνος για την υγεία | risques pour la santé | Opasnost za zdravlje | rischio per la salute | Veselības risks | Pavojus sveikatai |
| ICE | ice | Лед | Hielo | led | Is | Eis | Jää | Πάγος | glace | Led | ghiaccio | Ledus | Ledas |
| OBSTAC | obstacle | Препятствие | Obstáculo | překážka | Hindring | Schifffahrtshindernis | Takistus | Εμπόδιο | obstacle à la navigation | Prepreka | ostacolo alla navigazione | Šķērslis | Kliūtis |
| CHGMAR | change marks | Изменение в сигнализацията | Cambio de señalización | změna značení | Ændret signalering | Schifffahrtszeichen geändert | Muudatus-tähis | Αλλαγή σημείων | Signalisation modifée | Promjena navigacijske oznake | segnaletica modificata | Mainītas zīmes | Ženklų keitimas |
| HIGVOL | high voltage cable | Високо напрежение | Línea de alta tensión | vedení vysokého napětí | Højspændingskabler | Hochspannungsleitung | Kõrgepinge-juhtivus | Αγωγός υψηλής τάσης | Ligne haute tension | Visokonaponski kabel | alta tensione | Augstspriegums | Aukštos įtampos kabelis |
| ECDISU | Inland ECDIS update | Обновяване на ECDIS | Actualización ECDIS fluvial | aktualizace informací Inland ECDIS | Inland ECDIS update | Inland ECDIS Update | Uuendatud sisemaine ECDIS | Επικαιροποίηση ECDIS εσωτ. ναυσ. | Mise à jour des données Inland ECDIS | Ažuriranje sustava Inland ECDIS | aggiornamento ECDIS interno | Inland ECDIS informācijas atjaunošana | Inland ECDIS informacijos atnaujinimas |
| LOCRUL | local rules of traffic | Местни (локални) правила за движение | Normas locales de tráfico | místní úprava plavebních předpisů | Lokale trafikregler | lokal gültige Verkehrsvorschriften | Kohalikud liiklusees-kirjad | Τοπικοί κανόνες κυκλοφορίας | règlements particuliers de police | Lokalni prometni propisi | regole di traffico locali | Vietēji satiksmes noteikumi | Vietinės laivų eismo taisyklės |
| NEWOBJ | new object | Нов обект | Nuevo objeto | nový objekt | Nyt objekt | neues Objekt | Uus ese | Νέο αντικείμενο | Nouvel objet | Novi objekt | nuovo oggetto | Jauns objekts | Naujas objektas |
| MISECH | false radar echos | Грешно радарно ехо | Ecos radar falsos | falešná ozvěna | Falsk radarekko | Geisterechos | Radari vale kajasignaal | Εσφαλμένα σήματα ραντάρ | Faux échos radar | Pogrešan radarski odziv | rilevazioni radar distorte | Maldigs radara ehosignals | Klaidingi radaro rodmenys |
| VHFCOV | radio coverage | Радио покритие (обхват) | Cobertura de radio | rádiové pokrytí | Radiodækning | Funkabdeckung | Raadio leviala | Κάλυψη ασυρμάτου | Couverture radio | Radijska pokrivenost | copertura radio | Radiosignālu pārklājums | Radijo ryšio zona |
| REMOBJ | removal of object | Демонтиране на обект | Retirada de un objeto | odstranění objektu | Fjernelse af objekt | Bergungsarbeiten | Eseme eemaldamine | Απομάκρυνση αντικειμένου | enlèvement d'objet | Uklanjanje objekta | rimozione di oggetti | Objekta noņemšana | Objekto šalinimas |
| LEVRIS | rising water level | Растящо водно ниво | Nivel de agua en ascenso | stoupající vodní stav | Stigende vandstand | steigender Wasserstand | Veetaseme tõusmine | Αυξανόμενη στάθμη υδάτων | Eaux montantes | Vodostaj u porastu | livello idrometrico in aumento | Kāpjošs ūdens līmenis | Kylantis vandens lygis |
| SPCMAR | special marks | Специална сигнализация | Señalización especial | zvláštní signalizace | Særlig signalering | besondere Zeichen | Eritähised | Ειδικά σημεία | Signalisation spéciale | Posebne oznake | segnaletica speciale | Īpašas zīmes | Specialieji ženklai |
| WERMCO | weather conditions | Метеорологични условия | Condiciones meteorológicas | povětrnostní podmínky | Vejrforhold | Wetterbedingungen | Ilmastikuolud | Καιρικές συνθήκες | conditions météo | Vremenski uvjeti | condizioni meteorologiche | Laikapstākļi | Oro sąlygos |

**REASON CODE**

| EVENT | rendezvény | avveniment | Evenement | Impreza | Evento | eveniment | udalosť | prireditev | Tapahtumat | Evenemang | Мероприятие | Догађај |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WORK | munkálatok | xogħol | Werkzaamheden | Prace | Trabalhos | lucrări | práce | delo | Työt | Arbeten | Работы | Радови |
| DREDGE | kotrási munkálatok | tħammil | Baggeren | Pogłębianie | Dragagens | lucrări de dragaj | bagrovanie | poglabljanje dna | Ruoppaustyöt | Muddring | Землечерпательные работы | Багеровање |
| EXERC | gyakorlatok | eżerċizzji | Oefeningen | Ćwiczenia | Exercícios | exerciții | cvičenia | vaje | Harjoitukset | Övningar | Испытания | Вежбе |
| HIGWAT | magas vízállás | livell għoli tal-ilma | Hoogwater | Wysoki stan wody | Nível de cheia | ape mari | vysoký vodný stav | visok vodostaj | Korkea vesi | Högvatten | Высокая вода | Велика вода |
| HIWAI | kíméletes hajózási vízszint | livell tal-ilma li jeħtieġ navigazzjoni b’attenzjoni | Waterstand met beperkte scheepvaart | Stan wody wymagający ostrożnej żeglugi | Nível da água que obriga a navegação prudente | nivelul apei de avertizare pentru navigație | vodný stav pre opatrnú plavbu | vodostaj, ki zahteva previdno plovbo | varovaista liikkumista edellyttävä vedenkorkeus | Försiktig navigering p.g.a. vattennivån | Уровень опасный для судоходства | Водостај при којем је потреба опрезна пловидба |
| HIWAII | tilalmi vízszint | livell tal-ilma projbittiv | Waterstand met vaarverbod | Stan wody uniemożliwiający żeglugę | Nível da água que impossibilita a navegação | nivelul apei de interdicție | vodný stav pri ktorom je zakázaná plavba | vodostaj, ki ne dovoljuje plovbe | kiellon aiheuttava vedenkorkeus | Förbud p.g.a. vattennivån | Уровень запрещающий судоходство | Водостај при којем се забрањује пловидба |
| LOWWAT | alacsony vízállás | livell baxx tal-ilma | Laagwater | Niski stan wody | Nível de estiagem | ape mici | nízky vodný stav | nizek vodostaj | Matala vesi | Lågvatten | Низкая вода | Мала вода |
| SHALLO | gázlóképződés | sediment | Verondieping | Mielizna | Assoreamento | întinsură | naplaveniny | usedlina | Liettyminen | Slam-avsättning | Обмеление | Плићак |
| CALAMI | havaria/baleset | diżastru | Calamiteit | Wypadek | Acidente | calamitate | havária | nesreča | Onnettomuus | Olycka | Авария | Хаварија |
| LAUNCH | vízrebocsájtás | varar | Tewaterlating | Wodowanie | Lançamento à água | lansare la apă | spúšťanie na vodu | splavitev | Vesillelasku | Sjösättning | Спуск на воду | Поринуће |
| DECLEV | vízszint csökkentése | livell tal-ilma li qed jitbaxxa | Waterstandsverlaging | Spadek poziomu wody | Descida do nível da água | nivelul apei în scădere | klesajúca vodná hladina | nižanje vodostaja | Vedenkorkeuden laskeminen | Sjunkande vattennivå | Понижение уровня воды | Водостај у опадању |
| FLOMEA | áramlás mérése | kejl tal-fluss | Stroomsnelheidsmeting | Pomiar prądu | Caudal | operațiune de măsurare a debitului | meranie prietoku | merjenje pretoka | Virtauksen mittaaminen | Flödes-mätning | измерение скорости течения | Мерење протицаја |
| BLDWRK | építési munkálatok | xogħol ta’ bini | Bouwwerkzaamheden | Roboty budowlane | Obras | lucrări de construcții | stavebné práce | gradbena dela | Rakennustyöt | Byggnads-arbete | Строительство | Радови |
| REPAIR | javítási munkálatok | tiswija | Herstelwerkzaamheden | Prace remontowe | Reparações | lucrări de reparații | opravy | popravilo | Korjaustyöt | Reparations-arbete | Ремонтные работы | Поправка |
| INSPEC | szemle | spezzjoni | Inspectiewerkzaamheden | Inspekcja | Inspeção | inspecție | inšpekcia; prehliadka; kontrola | inšpekcijski pregled | Tarkastus | Inspektion | Инспекция | Инспекција |
| FIRWRK | tűzijáték | logħob tan-nar | Vuurwerk | Sztuczne ognie | Fogo de artifício | focuri de artificii | ohňostroj | ognjemet | Ilotulitus | Fyrverkerier | Взрывные работы | Ватромет |
| LIMITA | korlátozás | restrizzjonijiet | Beperkingen | Ograniczenia | Restrições | restricții | obmedzenia | omejitve | Rajoitukset | Begränsningar | Ограничения | Ограничења |
| CHGFWY | hajóútváltozás | bidliet tal-kanali navigabbli | Verandering van de vaarweg | Zmiany toru wodnego | Alterações no canal navegável | schimbări șenal navigabil | zmeny v plavebnej dráhe | spremembe na plovni poti | muutokset väylällä | Ändringar av farleden | изменение фарватера | Промене пловног пута |
| CONSTR | hajóútszűkület | restrizzjoni tal-kanal navigabbli | Beperking van de vaarweg | Zwężenie toru wodnego | Estreitamento da via navegável | îngustare cale navigabilă | zúženie vodnej cesty | zoženje plovne poti | vesiväylän kaventuminen | Smalare vattenväg | Сужение фарватера | Сужење пловног пута |
| DIVING | vízalatti munkák | bugħaddas taħt l-ilma | Duikwerkzaamheden | Nurek pod wodą | Presença de mergulhadores | scafandru în apă | potápač pod vodou | dela pod vodo | sukeltaja veden alla | Dykare i vattnet | Водолазные работы | Подводни радови |
| SPECTR | különleges szállítás | trasport speċjali | Bijzonder vervoer | Transport specjalny | Transporte especial | transport special | špeciálna preprava | posebni prevoz | erikoiskuljetus | Special-transport | специальная перевозка | Специјални транспорт |
| EXT | nagymértékű vízeresztés | kontroll estensiv tal-ilma | Uitgebreid schutbedrijf | Intensywne śluzowanie | Regime de descarga máximo | trafic de ecluză intens | rozsiahle dotovanie | ekstenzivno odtekanje | laajamittainen sulutus | Omfattande drift | значительный спуск воды | Значајно истицање |
| MIN | minimális vízeresztés | kontroll minimu tal-ilma | Minimaal schutbedrijf | Minimalne śluzowanie | Regime de descarga mínimo | trafic de ecluză redus | minimálne dotovanie | minimalno odtekanje | vähimmäissulutus | Minimidrift | минимальный спуск воды | Минимално истицање |
| SOUND | mélységmérési munka | xogħlijiet ta’ kejl tal-fond | Peilwerkzaamheden | Pomiary głębokości | Sondagens | lucrări de sondaj | sondovacie práce | merjenje globine | luotaustyöt | Lodnings-arbete | промерные работы | Мерења дубина |
| OTHER | egyéb | oħrajn | Overige | Inne | Outros | altele | Iné | drugo | muutokset väylällä | Annat | другое | Остало |
| INFSER | Tájékoztatás (nem biztonsági közlemény és útiterv készítéséhez nem szükséges) | servizz ta’ informazzjoni | Informatieservice | Serwis informacyjny (informacje niezwiązane z bezpieczeństwem i niewymagane do planowania rejsu) | Serviço de informações (sem relevância para a segurança e para a planificação de viagem) | mesaj informativ (nu se referă la siguranța traficului și nu este necesar pentru planificarea voiajelor) | Informačná služba (netýka sa bezpečnosti ani plánovania plavby) | informacijska služba | Tietopalvelu (ei ole olennainen turvallisuuden kannalta eikä tarpeen matkan suunnittelussa) | Informations-tjänst (inte säkerhets-relaterad och inte nödvändig för färdplanering) | Информационная служба (не значительна для безопасности и нет необходимости в ней для планирования рейса) | Услуга информисања (није релевантна за безбедност пловидбе и није потребна за планирање путовања) |
| STRIKE | sztrájk | strajk | Staking | Strajk | Greve | grevă | štrajk | stavka | Lakko | Strejk | Забастовка | Удар |
| FLOMAT | úszó anyag | materjal f'wiċċ l-ilma | Drijvend materiaal | Materiał pływający | Material flutuante | material plutitor | plávajúci materiál | plavajoči predmeti | Kelluva aines | Flytande föremål | Плавучий материал | Плутајући материјал |
| EXPLOS | robbanóanyag eltávolítás | operazzjoni ta’ tneħħija ta’ splussivi | Verwijderen van explosieven | Operacja usuwania materiałów wybuchowych | Operação de desminagem | explozive pentru degajare | zneškodňovanie výbušnín | odstranjevanje eksplozivov | Räjähteiden raivaaminen | Röjning av explosivt material | Разминирование | Операција разминирања |
| OBUNWA | víz alatti akadály | ostaklu taħt l-ilma | Belemmering onder water | Przeszkoda podwodna | Obstrução subaquática | obstacol subacvatic | prekážka pod vodou | zapora pod vodo | Vedenalainen este | Undervattenshinder | Препятствие под водой | Препрека под водом |
| FALMAT | lehulló anyagok | materjal qed jaqa’ | Vallend materiaal | Materiał spadający | Queda de materiais | material care cade | padajúci materiál | padajoči predmeti | Putoava aines | Fallande föremål | Падающий материал | Матаријал који пада |
| DAMMAR | sérült jelzés | sinjali bil-ħsara | Beschadigde markeringen/symbolen | Uszkodzone znaki/sygnały | Marcas/sinais danificados | semnale avariate | poškodené signálne znaky | poškodovane oznake/znaki | Vaurioituneet merimerkit | Skadade markeringar/signaler | Поврежденные знаки/огни | Оштећен знак |
| HEARIS | egészségügyi kockázat | riskju għas-saħħa | Gezondheidsrisico | Zagrożenie dla zdrowia | Risco para a saúde | risc de îmbolnăvire | zdravotné riziko | tveganje za zdravje | Terveysriski | Hälsorisk | Риск здоровью | Опасноист по здравље |
| ICE | jég | silġ | IJs | Lód | Gelo | gheață | ľad | led | Jää | Is | лед | Лед |
| OBSTAC | akadály | ostaklu | Obstakel | Przeszkoda | Obstáculo | obstacol | prekážka | ovira | Este | Hinder | Препятствие (помеха) | Препрека |
| CHGMAR | forgalmi jelek változtatása | bidla fis-sinjali | Gewijzigde markering | Zmiana oznakowania | Alteração da sinalização | semnalizare modificată | zmena značenia | sprememba oznak | Merkit muuttuneet | Ändrad märkning | Изменение СНО | Промена знака |
| HIGVOL | nagy feszültségű átfeszítés | kejbil b’voltaġġ għoli | Hoogspanningskabel | Linia wysokiego napięcia | Linha de alta tensão | linie de înaltă tensiune | vedenie vysokého napätia | visokonapetostni kabel | Korkeajännitejohto | Högspänningsledning | высоковольтный кабель | Кабл под високим напоном |
| ECDISU | Inland ECDIS frissítés | aġġornament tal-ECDIS Interna | Inland ECDIS-update | Aktualizacja Inland ECDIS | Atualização ECDIS-fluvial | actualizarea datelor ECDIS | aktualizácia Inland ECDIS | posodobitev celinskega ECDIS | Sisävesiliikenteen ECDIS:n päivitys | Uppdatering av inlands-ECDIS | Обновление информации для Inland ECDIS | Ажуриран Inland ECDIS |
| LOCRUL | helyi közlekedési rend (R) | regoli lokali tat-traffiku | Lokale verkeersregels | Miejscowe przepisy ruchu statków | Regras de tráfego locais | regulamente locale de trafic | lokálne pravidlá plavby | lokalna prometna pravila | paikalliset liikennöintisäännöt | Lokala trafikregler | Местные правила судоходства | Локална правила пловидбе |
| NEWOBJ | Új objektum | oġġett ġdid | Nieuw object | Nowy obiekt | Novo objeto | obiect nou | nový objekt | nov objekt | Uusi kohde | Nytt föremål | Новый объект | Нови објекат |
| MISECH | hamis radarvisszhangok | eki foloz tar-radar | Valse radarecho's | Fałszywe echa radarowe | Ecos radar falsos | ecou radar fals | falošná odozva | napačni odmevi radarja | Virheellisiä tutkakaikuja | Falska radarekon | Ложная радарная цель | Лажни радарски одраз |
| VHFCOV | rádiós lefedettség | kopertura tar-radju | Radiodekking | Pokrycie radiowe | Cobertura rádio | acoperire radio | rádiové pokrytie | pokritost radijskih zvez | Radion kuuluvuusalue | Radiotäckning | Покрытие радиосигналом | Покривеност радио сигналом |
| REMOBJ | mentési munkálatok | tneħħija ta’ oġġett | Verwijderen van object | Usuwanie objektu | Remoção de objetos | schimbarea obiectului | odstránenie objektu | odstranitev objekta | Kohteen poistaminen | Bärgning av föremål | Удаление объекта | Уклањање објекта |
| LEVRIS | emelkedő vízállás | livell tal-ilma qed jogħla | Waterstandsverhoging | Wzrost stanu wody | Subida do nível da água | creșterea nivelului apei | stúpajúca vodná hladina | višanje vodostaja | Vedenkorkeus nousee | Stigande vattennivå | Повышение уровня воды | Ниво воде у порасту |
| SPCMAR | speciális jelek | sinjali speċjali | Bijzondere markeringen | Znaki specjalne | Sinalização especial | semnalizare specială | špeciálne značenie | posebne oznake | Erikoismerkit | Särskilda markeringar | Специальные знаки | Посебне ознаке |
| WERMCO | időjárási viszonyok | kundizzjonijiet tat-temp | Weersomstandigheden | Warunki pogodowe | Condições meteorológicas | condiții meteorologice | poveternostné podmienky | vremenske razmere | Sääolosuhteet | Väderförhållanden | метеорологические условия | временски услови |

**REFERENCE CODE**

| NAP | NAP | NAP | NAP | NAP | Normal vandstand i Amsterdam | NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KP | channel level | Пегел на канала | Nivel local | kanálový vodočet | Kanalniveau | Kanal Pegel | kp | Στάθμη υδάτων καναλιού | Côte locale | Vodomjer u kanalu | livello canale | Kanāla ūdens līmeņrādis | Kanalo vandens lygis |
| FZP | FZP | FZP | Nivel de los canales frisones | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP |
| ADR | Adria | Адриатическа система | Mar Adriático | přes Adrii | Adria | über Adria | Adria | Αδριατική | Mer Adriatique | Razina Jadranskog mora | livello adriatico | Adrijas sistēma | Adrijos sistema |
| TAW | TAW/DNG | TAW/DNG | 2ª nivelación general/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG |
| PUL | Pulkovo 1942 | Пулково 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 |
| NGM | Ngm | Нгм | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm |
| ETRS | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 |
| POT | Potsdamer Datum | Координатна система Потсдам | Potsdamer Datum | Postupimské datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamas koordinātu sistēma | Potsdamo koordinačių sistema |
| LDC | low water level Danube Commission | Ниско водно ниво по Дунавската комисия | Comisión del Danubio, nivel bajo de agua | nízký plavební stav podle Dunajské komise | Lav vandstand defineret af Donau-kommissionen | RNW gemäß Donaukommission | Madala veetaseme Doonau komisjon | Χαμηλή στάθμη υδάτων, Επιτροπή Δούναβη | Commission du Danube, niveau bas des eaux | Niski plovidbeni vodostaj po Dunavskoj komisiji | livello di magra Commissione del Danubio | Zems ūdens līmenis, Donavas komisija | Žemas vandens lygis, Dunojaus komisija |
| HDC | high water level Danube Commission | Високо водно ниво по Дунавската комисия | Comisión del Danubio, nivel alto de agua | nejvyšší plavební vodní stav podle Dunajské komise | Høj vandstand defineret af Donau-kommissionen | HSW gemäß Donaukommission | Kõrge veetaseme Doonau komisjon | Υψηλή στάθμη υδάτων, Επιτροπή Δούναβη | Commission du Danube, niveau haut des eaux | Visoki plovidbeni vodostaj po Dunavskoj komisiji | livello di piena Commissione del Danubio | Augsts ūdens līmenis, Donavas komisija | Aukštas vandens lygis, Dunojaus komisija |
| ZPG | zero point of gauge | Нула на пегела | Punto de referencia de nivel | nulový bod vodočtu | Profilens nulpunkt | Pegelnullpunkt | Mõõtmiskoha nullpunkt | Μηδενικό σημείο μετρητή | point de référence de niveau | Nulta točka vodomjerne letve | zero idrometrico | Ūdens līmeņrāža nulles punkts | Nulinis vandens lygio rodmuo |
| GLW | equivalent low water level | Еквивалентно ниско водно ниво | Estiaje | ekvivalentní nízký vodní stav | Tilsvarende lav vandstand | Gleichwertiger Wasserstand (GLW) | Madala veetaseme ekvivalent | Ισοσύναμη χαμηλή στάθμη υδάτων | étiage | Ekvivalentni niski vodostaj | livello equivalente di magra | Minimālais ūdens līmenis | Žemo vandens lygio ekvivalentas |
| HSW | highest navigable water level | Най-високо корабоплавателно ниво | Nivel máximo navegable | nejvyšší plavební vodní stav | Højeste farbare vandstand | Höchster Schifffahrtswasserstand (HSW) | kõrgeim navigeeritav veetase | Υψηλότερη πλεύσιμη στάθμη υδάτων | Plus hautes eaux navigables | Maksimalni vodostaj dozvoljene plovidbe | massimo livello idrometrico navigabile | Augstākais kuģojamais ūdens līmenis | Aukščiausias laivybos vandens lygis |
| LNW | Low Navigable Water | Ниско корабоплавателно ниво | Nivel mínimo navegable | nízký plavební vodní stav (národní) | Lav farbar vandstand | RNW (national) | madal navigeeritav vesi | Χαμηλή πλεύσιμη στάθμη υδάτων | Plus basses eaux navigable | Niski vodostaj dozvoljene plovidbe | livello di magra navigabile | Zemākais kuģojamais ūdens līmenis | Žemas laivybos vandens lygis |
| HNW | High Navigable Water | Високо корабоплавателно ниво | Nivel alto navegable | nejvyšší plavební vodní stav (národní) | Høj farbar vandstand | HSW (national) | kõrge navigeeritav vesi | Υψηλή πλεύσιμη στάθμη υδάτων | Hautes eaux navigables | Visoki vodostaj dozvoljene plovidbe | livello di piena navigabile | Augsts kuģojamais ūdens līmenis | Aukštas laivybos vandens lygis |
| IGN | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 |
| WGS | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 |
| RN | normal level | Нормално ниво | Nivel normal | normální stav | Normalniveau | Normaler Pegel | normaaltase | Κανονική στάθμη υδάτων | Retenue normale | Normalna razina | livello idrometrico normale | Normāls ūdens līmenis | Normalus lygis |
| HBO | high water level of attention | Високо водно ниво преди наводнение | Atención por nivel alto de agua | vysoký vodní stav před vybřežením | Høj vandstand, der kræver forsigtighed | Hochwasser, das besondere Vorsicht erfordert | tähelepanu nõudev kõrge veetase | Υψηλή στάθμη υδάτων, απαιτείται προσοχή | cote d'attention | Visok vodostaj — stanje pripravnosti | livello di piena da sorvegliare | Ievērojami augsts ūdens līmenis | Pavojingai aukštas vandens lygis |

**REFERENCE CODE**

| NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KP | csatornavíz-szint | livell tal-kanal | Kanaalpeil | kp | Cota local | nivelul de referință local | prevádzková úroveň hladiny v kanáli | vodostaj v kanalu | kp | kp | Судоходный уровень канала | upozorenje od velike vode |
| FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP |
| ADR | az Adriai tenger szintje felett | Adria | Adriapeil | Adria | Adriático | Marea Adriatică | výškový systém ADRIA | nivo Jadranskega morja | Adria | Adria | Адриатическая система | Ниво Јадранског мора |
| TAW | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG |
| PUL | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Пулково 1942 | Пулково 1942 |
| NGM | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Нгм | Ngm |
| ETRS | ETRS89 | ETRS89 | Etrs89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 |
| POT | potsdami dátum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Координатная система Потсдам | Potsdamer датум |
| LDC | Dunabizottsági hajózási kisvízszint (LKHV) | livell baxx tal-ilma tal-Kummissjoni tad-Danubju | Laagwaterpeil Donaucommissie | niski stan wody wg Komisji Dunajskiej | Nível baixo da água, Comissão do Danúbio | nivelul apei minim — Comisia Dunării | hladina nízkej regulačnej a plavebnej vody podľa DK | nizek vodostaj po Donavski komisiji | Tonavan suojelukomission mukainen pieni vedenkorkeus | Lågvattennivå enligt Donau-kommissionen | Низкий уровень воды ДК | Ниски пловидбени ниво према Дунавској комисији |
| HDC | Dunabizottsági hajózási nagyvízszint (LNHV) | livell għoli tal-ilma tal-Kummissjoni tad-Danubju | Hoogwaterpeil Donaucommissie | wysoki stan wody wg Komisji Dunajskiej | Nível alto da água, Comissão do Danúbio | nivelul apei maxim — Comisia Dunării | hladina vysokej plavebnej vody podľa DK | visok vodostaj po Donavski komisiji | Tonavan suojelukomission mukainen suuri vedenkorkeus | Högvattennivå enligt Donau-kommissionen | Высокий уровень воды ДК | Високи пловидбени ниво према Дунавској комисији |
| ZPG | vízmérce nulla pontja | punt żero tal-kejl | Referentiepunt van de peilschaal | punkt zerowy wodowskazu | Ponto zero do fluviómetro | zero miră | nulový bod mernej stanice | ničelna točka vodomera | vedenkorkeusmittarin nollakohta | Vattenståndsmätarens nollpunkt | ноль уровня | ‘0’ водомера |
| GLW | egyenértékű kisvízszint | livell baxx tal-ilma ewkivalenti | Gelijkwaardige laagwaterstand | równoważny niski stan wody | Nível baixo equivalente da água | nivelul apei minim echivalent | ekvivalentná nízka vodná hladina | ekvivalent nizkega vodostaja | vastaava pieni vedenkorkeus | Ekvivalent lågvattennivå | Низкий уровень воды | Еквивалент малој води |
| HSW | legnagyobb hajózási vízszint (HNV) | l-ogħla livell tal-ilma navigabbli | Hoogste scheepvaartwaterstand | najwyższy stan wody dopuszczający żeglugę | Nível máximo navegável | cel mai mare nivel al apei pentru navigație | najvyššia plavebná hladina | najvišji vodostaj, pri katerem je mogoča plovba | suurin kulkukelpoinen vedenkorkeus | Högsta navigerbara vattennivå | Наивысший судоходный уровень | Највиши водостај за пловидбу |
| LNW | hajózási kisvízszint (HKV) | Ilma Navigabbli Baxx | Laagste scheepvaartwaterstand (nationaal) | niski stan wody dopuszczający żeglugę | Nível mínimo navegável | nivelul apei minim pentru navigație | nízka plavebná hladina | nizek vodostaj, pri katerem je mogoča plovba | Matala kulkukelpoinen vesi | Lågt navigerbart vatten | Минимальный судоходный уровень | Ниски пловидбени ниво |
| HNW | hajózási nagyvízszint (HNV) | Ilma Navigabbli Għoli | Hoogste scheepvaartwaterstand (nationaal) | wysoki stan wody dopuszczający żeglugę | Nível alto navegável | nivelul apei maxim pentru navigație | vysoká plavebná hladina | visok vodostaj, pri katerem je mogoča plovba | Korkea kulkukelpoinen vesi | Högt navigerbart vatten | максимальный судоходный уровень | Високи пловидбени ниво |
| IGN | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 |
| WGS | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 | SGM 84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS84 | WGS 84 |
| RN | szokásos szint | livell normali | Normaal peil | poziom normalny | Nível normal | nivelul apei normal | normálna úroveň | običajen vodostaj | normaali taso | Normal nivå | Нормальный уровень воды | Нормални ниво |
| HBO | LNHV-t meghaladó vízállás | livell għoli tal-ilma li jeħtieġ attenzjoni | Hoogwaterpeil, aandacht geboden | alarmowy stan wody | Nível alto da água que obriga a navegação atenta | cota de atenție | vysoká hladina — stav bdelosti | opozorilo glede visokega vodostaja | suuri vedenkorkeus, edellyttää erityistä huomiota | Högvattennivå som kräver uppmärksamhet | высокий уровень воды, угроза наводнения | upozorenje od velike vode |

**REGIME CODE**

| NO | normal | Нормално водно ниво | Normal | normální vodní stav | Normal vandstand | Regime: Normal Wasserstand | Tavaline | Κανονική | Hauteur d'eau normale | Režim: normalni vodostaj | normale | Normāls ūdens līmenis | Normalus vandens lygis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HI | high | Високи води | Alto | vysoký vodní stav | Højvande | Hochwasser | Kõrge | Υψηλή | Plus Hautes Eaux Navigables | Režim: visok vodostaj | livello idrometrico elevato | Augsts ūdens līmenis | Aukštas vandens lygis |
| II | prohibitory water level | Водно ниво възпрепятстващо корабоплаването | Nivel de agua de prohibición | vodní stav, při kterém je zakázaná plavba | Vandstand, hvor sejlads forbydes | Sperrung wegen Hochwasser | Keelatud veetase | Απαγορευτική στάθμη υδάτων | Niveau d'eau d'interdiction | Vodostaj zabrane plovidbe | livello idrometrico proibitivo | Ūdens līmenis, kurā kuģošana aizliegta | Laivybą draudžiantis vandens lygis |
| I | water level of cautious navigation | Водно ниво изискващо корабоплаване с повишено внимание | Nivel de agua para navegación prudente | vodní stav zvýšené opatrnosti plavby | Vandstand, hvor sejlads udføres med særlig agtpågivenhed | Marke I. | Ettevatliku laevatamise veetase | Στάθμη υδάτων προσεκτικής ναυσιπλοΐας | Niveau d'eau nécessitant une navigation prudente | Vodostaj oprezne plovidbe | livello idrometrico di prudenza per la navigazione | Ūdens līmenis bīstams kuģošanai | Laivybai pavojingas vandens lygis |
| NN | normal water level for navigation | Нормално водно ниво за корабоплаване | Nivel de agua normal para navegación | normální vodní stav pro plavbu | Normal vandstand for skibsfart | normaler Schifffahrtswasserstand | Laevatami-seks normaalne veetase | Κανονική στάθμη υδάτων ναυσιπλοΐας | Niveau Normal de Navigation | Vodostaj normalne plovidbe | livello idrometrico normale per la navigazione | Normāls ūdens līmenis kuģošanai | Laivybai tinkamas vandens lygis |
| LO | low water | Ниски води | Nivel de agua bajo | nízký vodní stav | Lavvande | Niedrigwasser | Madal vesi | Χαμηλή στάθμη υδάτων | Etiage | Nizak vodostaj | livello di magra | Zems ūdens līmenis | Žemas vandens lygis |

**REGIME CODE**

| NO | normál vízállás | normali | Normaal | normalny | Nível da água normal | nivelul normal | normálny vodný stav | normalen | Normaali | Normal | Нормальный уровень | Режим нормалног водостаја |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HI | magas vízállás | għoli | Hoogwaterregime | wysoki | Nível da água alto | nivelul maxim navigabil | vysoký vodný stav | visok | Suuri | Hög | Высокая вода (паводок) | Велика вода |
| II | tilalmi vízszint | livell tal-ilma projbittiv | Waterstand met vaarverbod | stan wody uniemożliwiający żeglugę | Nível da água que impossibilita a navegação | nivelul apei restrictiv pentru navigație | vodný stav, pri ktorom je zakázaná plavba | vodostaj, ki ne dovoljuje plovbe | kiellon aiheuttava vedenkorkeus | Förbud p.g.a. vattennivån | уровень воды, запрещающий судоходство | Водостај при коме се обуставља пловидба |
| I | kíméletes hajózási vízszint | livell tal-ilma li jeħtieġ navigazzjoni b’attenzjoni | Waterstand met beperkte scheepvaart | stan wody wymagający ostrożnej żeglugi | Nível da água que obriga a navegação prudente | nivelul apei de precauție pentru navigație | vodný stav pre opatrnú plavbu | vodostaj, ki zahteva previdno plovbo | varovaista liikkumista edellyttävä vedenkorkeus | Försiktig navigering p.g.a. vattennivån | уровень воды, опасный для судоходства | Водостај који захтева опрезну пловидбу |
| NN | normál hajózási vízszint | livell normali tal-ilma għan-navigazzjoni | Normaal waterpeil voor scheepvaart | normalny stan wody dla żeglugi | Nível da água normal para a navegação | nivelul apei normal pentru navigație | normálny vodný stav pre plavbu | normalen vodostaj za plovbo | normaali vedenkorkeus alusliikenteelle | Normal vattennivå för sjöfart | Нормальный уровень воды для судоходства | Нормални водостај за пловидбу |
| LO | alacsony vízállás | livell baxx tal-ilma | Laagwaterregime | niski stan wody | Nível de estiagem | ape mici | nízky vodný stav | nizek vodostaj | Matala vesi | Lågvatten | Низкая вода | Мала вода |

**REPORTING CODE**

| INF | information | Информация | Información | informace | Informationspunkt | Informationspunkt | Teave | Πληροφορίες | Point d'information | Informacijski | informazione | Informācijas punkts | Informavimas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADD | additional duty to report | Задължтелно допълнително известяване | Obligación adicional de notificación | dodatečná povinnost hlášení | Yderligere rapporteringspligt | zusätzliche Meldepflicht | Täiendav tollimaks teatada | Πρόσθετο καθήκον αναφοράς | Obligation complémentaire d'annonce | Dodatna obveza izvješćivanja | obbligo di ulteriore segnalazione | Papildu ziņošanas pienākums | Privalomas papildomas pranešimas |
| REG | regular duty to report | Обичаен режим за известяване | Obligación normal de notificación | normální povinnost hlášení | Normal rapporteringspligt | normale Meldepflicht | Tavatollimaks teatada | Κανονικό καθήκον αναφοράς | Obligation d'annonce normale | Redovna obveza izvješćivanja | regime normale di segnalazione | Pastāvīgas ziņošanas pienākums | Įprastas pranešimo režimas |

**REPORTING CODE**

| INF | információ | informazzjoni | Informatie | Punkt informacyjny | Informação | punct de informare | informácie | informacije | Tiedot | Information | Информация для сведения | Информација |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADD | kiegészítő bejelentkezési kötelezettség | dmir addizzjonali ta’ rappurtar | Extra meldplicht | Obowiązek dodatkowego meldowania | Obrigação adicional de comunicação | obligația suplimentară de a raporta | dodatočná povinnosť hlásenia | dodatna obveznost poročanja | Ylimääräinen raportointivelvollisuus | Extra rapporteringsskyldighet | Дополнительное извещение обязательно | Додатна обавеза извештавања |
| REG | bejelentkezési kötelezettség | dmir regolari ta’ rappurtar | Normale meldplicht | Obowiązek regularnego meldowania | Obrigação normal de comunicação | obligația de a raporta regulat | normálna povinnosť hlásenia | običajna obveznost poročanja | Säännöllinen raportointivelvollisuus | Regelbunden rapporteringskyldighet | Обычный режим извещения | Редовна обавеза извештавања |

**SUBJECT CODE**

| OBSTRU | Blockage | Препятствие | Obstrucción | uzávěra | Blokering | Sperre | Blokeerimine | Φραγμένο | Restriction | Prepreka | interruzione | Bloķēts | Blokavimas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PAROBS | Partial obstruction | Частично препятствие | Obstrucción parcial | částečná uzávěra | Delvis blokering | teilweise Sperre | Osaline takistus | Μερική παρεμπόδιση | Restriction partielle | Djelomična prepreka | ostruzione parziale | Daļēji bloķēts | Dalinis blokavimas |
| DELAY | Delay | Закъснение | Retraso | zpoždění | Forsinkelse | Verzögerung | Hilinemine | Καθυστέρηση | Délai | Kašnjenje | ritardo | Aizkavējums | Delsa |
| VESLEN | Vessel Length | Дължина на кораба | Eslora | délka plavidla | Fartøjets længde | Schiffslänge | Laeva pikkus | Μήκος σκάφους | Longueur du bateau | Dužina broda | lunghezza del natante | Kuģa garums | Laivo ilgis |
| VESHEI | Vessel air draught | Височина на кораба | Altura de la obra muerta | výška plavidla nad hladinou | Fartøjets højde over vandlinjen | Schiffshöhe | Laeva kõrgus veepinnast | Μέγιστο ύψος άνωθεν της ισάλου γραμμής | Tirant d'air du bateau | Visina najviše fiksne točke broda iznad vode | altezza del natante dal pelo dell'acqua | Kuģa virsūdens augstums | Laivo aukštis virš vandens |
| VESBRE | Vessel breadth | Ширина на кораба | Manga | šířka plavidla | Fartøjets bredde | Schiffsbreite | Laeva laius | Μέγιστο πλάτος σκάφους | Largeur du bateau | Širina broda | larghezza del natante | Kuģa platums | Laivo plotis |
| VESDRA | Vessel draught | Газене на кораба | Calado | ponor plavidla | Fartøjets dybgang | Schiffstiefgang | Laeva süvis | Βύθισμα σκάφους | Tirant d'eau du bateau | Gaz broda | pescaggio del natante | Kuģa iegrime | Laivo grimzlė |
| AVALEN | Available length | Допустима дължина | Eslora disponible | povolená délka | Disponibel længde | verfügbare Länge | Kasutatav pikkus | Διαθέσιμο μήκος | Longueur maximum | Raspoloživa duljina | lunghezza massima ammessa | Pieļaujamais garums | Leidžiamas ilgis |
| CLEHEI | Clearance height | Свободна височина | Gálibo vertical | podjezdná výška | Frigang i højden | Durchfahrtshöhe | Kuja kõrgus | Ελεύθερο ύψος διέλευσης | Tirant d'air maximum | Visina plovnog otvora | tirante d'aria | Pieļaujamais augstums | Leidžiamas aukštis |
| CLEWID | Clearance width | Свободна ширина | Gálibo horizontal | průjezdná šířka | Frigang, bredde | verfügbare Breite | Kuja laius | Ελεύθερο πλάτος διέλευσης | Largeur maximum | Širina plovnog otvora | larghezza massima della via navigabile | Pieļaujamais platums | Leidžiamas plotis |
| AVADEP | Available depth | Допустимо газене | Profundidad disponible | využitelná hloubka | Vanddybde | verfügbare Tiefe | Kasutatav sügavus | Διαθέσιμο πλάτος | Tirant d'eau maximum | Raspoloživa dubina | pescaggio massimo | Ūdens dziļums | Esamas gylis |
| NOMOOR | No mooring | Забранено швартоване | Prohibición de amarre | zákaz přistávání | Fortøjning forbudt | Festmacheverbot | Sildumine keelatud | Απαγόρευση αγκυροβολίας | Interdiction d'amarrage | Zabranjen vez | divieto di ormeggio | Pietauvošanās aizliegta | Draudžiama švartuotis |
| SERVIC | Limited service | Ограничено обслужване | Servicio limitado | provoz omezen | Begrænset betjening | Betrieb eingeschränkt | Piiratud teenindus | Περιορισμένη υπηρεσία | Exploitation limitée | Ograničena usluga | servizio limitato | Ierobežots pakalpojums | Ribotas aptarnavimas |
| NOSERV | No service | Няма обслужване | Interrupción del servicio | provoz zastaven | Ingen betjening | Betriebssperre | Ei teenindata | Καμία υπηρεσία | Manœuvre interrompue | Nema usluge | nessun servizio | Pakalpojums nav pieejams | Neaptarnaujama |
| SPEED | Speed | Допустима скорост | Límite de velocidad | nejvyšší rychlost | Hastighedsbegrænsning | Höchstgeschwindigkeit | Kiirus | Ταχύτητα | Limite de Vitesse | Ograničenje brzine | velocità | Ātruma ierobežojums | Ribojamas greitis |
| WAVWAS | No wash of waves | Забранено създаване на вълни | No crear oleaje | zákaz vytvářet vlnobití a sání | Undgå at lave efterdønninger | Sog und Wellenschlag vermeiden | Ei tekita voolu | Απαγόρευση πρόκλησης κυματισμών | Remous interdits | Zabranjeno pravljenje valova | divieto di moto ondoso | Neradīt viļņus | Nekelti bangų |
| PASSIN | No passing | Забранено преминаване | Prohibido el paso | zákaz potkávání | Passage er ikke tilladt | Begegnungsverbot | Läbimine keelatud | Απαγόρευση διέλευσης | Trématage interdit | Zabranjen prolaz | divieto di transito | Aizliegts šķērsot | Plaukti draudžiama |
| ANCHOR | No anchoring | Забранено хвърляне на котва | Prohibido fondear | zákaz kotvení | Opankring ikke tilladt | Ankerverbot | Ankrusse jäämine keelatud | Απαγόρευση αγκυροβολίας | Mouillage interdit | Zabranjeno sidrenje | divieto di ancoraggio | Noenkuroties aizliegts | Draudžiama nuleisti inkarą |
| OVRTAK | No overtaking | Забранено изпреварване | Prohibido adelantar | zákaz předjíždění | Overhaling ikke tilladt | Überholverbot | Möödasõit keelatud | Απαγόρευση προσπέρασης | Trématage interdit | Zabranjeno pretjecanje | divieto di sorpasso | Apdzīt aizliegts | Draudžiama lenkti |
| MINPWR | Minimum power | Минимална мощност | Potencia mínima | minimální výkon | Minimum kraft | Mindestantriebsleistung | Minimaalne võimsus | Ελάχιστη ισχύς | Puissance minimum | Minimalna snaga | potenza minima | Minimālā jauda | Mažiausia galia |
| DREDGE | Dredging | Драгажни работи | Dragado | bagrovací práce | Opmudring | Baggerarbeiten | Süvendus | Βυθοκόρηση | Dragage | Iskapanje | dragaggio | Bagarēšanas darbi | Dugno gilinimas |
| WORK | Work | Работи (действия) | Obras | práce | Arbejder | Arbeiten | Töötamine | Εργασίες | Travaux | Radovi | lavori | Darbs | Darbai |
| EVENT | Event | Случай | Suceso | událost | Begivenhed | Veranstaltung | Sündmus | Συμβάν | Evénement | Događaj | manifestazione | Pasākums | Įvykis |
| CHGMAR | Change marks | Изменение в знаците | Cambio de señalización | změna značení | Ændret signalering | Schifffahrtszeichen geändert | Muudatus-tähis | Αλλαγή σημείων | Signalisation modifée | Promjena navigacijske oznake | segnaletica modificata | Mainītas zīmes | Ženklų keitimas |
| CHGSER | Change service | Изменение в услугите | Cambio de servicio | změna provozu | Ændret betjening | Betrieb geändert | Vahetus-teenindus | Αλλαγή υπηρεσίας | manœuvre des ouvrages modifiée | Promjena usluge | regime modificato | Pakalpojums mainīts | Aptarnavimo pasikeitimai |
| SPCMAR | Special marks | Специална сигнализация | Señalización especial | zvláštní signalizace | Særlig signalering | besondere Zeichen | Eritähised | Ειδικά σημεία | Signalisation spéciale | Posebne oznake | segnaletica speciale | Īpašas zīmes | Specialieji ženklai |
| EXERC | Exercises | Упражнения | Ejercicios | cvičení | Øvelser | Übungen | Õppused | Ασκήσεις | exercices | Vježbe | esercitazioni | Vingrinājumi | Pratybos |
| LEADEP | Least depth sounded | Минимална дълбочина | Profundidad mínima medida | minimální změřená hloubka | Mindste loddede dybde | minimale Tiefe | Looditud väikseim sügavus | Μικρότερο μετρηθέν βάθος | Profondeur minimale | Minimalna dubina | profondità minima rilevata | Mazākais izmērītais dziļums | Mažiausias gylis |
| LEVDEC | Decreasing water level | Намаляващо водно ниво | Nivel de agua en descenso | klesající vodní stav | Faldende vandstand | fallender Wasserstand | Veetaseme alanemine | Μειούμενη στάθμη υδάτων | Décrue | Vodostaj u opadanju | livello idrometrico in diminuzione | Krītošs ūdens līmenis | Mažėjantis vandens lygis |
| LEVRIS | Rising water level | Растящо водно ниво | Nivel de agua en ascenso | stoupající vodní stav | Stigende vandstand | steigender Wasserstand | Veetaseme tõusmine | Αυξανόμενη στάθμη υδάτων | Eaux montantes | Vodostaj u porastu | livello idrometrico in aumento | Kāpjošs ūdens līmenis | Kylantis vandens lygis |
| ANNOUN | Announcement | Обява | Aviso | zpráva | Meddelelse | Nachricht | Teadaanne | Αγγελία | Annonce | Najava | annuncio | Paziņojums | Pranešimas |
| LIMITA | Limitations | Ограничение | Limitaciones | omezení | Begrænsninger | Einschränkungen | Piirangud | Περιορισμοί | Limitations | Ograničenja | limitazioni | Ierobežojumi | Apribojimai |
| CANCEL | Notice withdrawn | Анулирано известие | Anuncio anulado | zpráva byla zrušena | Efterretning trukket tilbage | Nachricht zurückgezogen | Kehtetu märguanne | Απόσυρση αγγελίας | Avis annulé | Povučena obavijest | segnalazione revocata | Paziņojums atcelts | Pranešimas atšauktas |
| MISECH | False radar echos | Грешно радарно ехо | Ecos radar falsos | falešná ozvěna | Falsk radarekko | Geisterechos | Radari vale kajasignaal | Εσφαλμένα σήματα ραντάρ | Faux échos radar | Pogrešan radarski odziv | rilevazioni radar distorte | Maldigs radara ehosignals | Klaidingi radaro rodmenys |
| ECDISU | Inland ECDIS update | Обновяване на ECDIS | Actualización ECDIS fluvial | aktualizace informací Inland ECDIS | Inland ECDIS update | Inland ECDIS Update | Uuendatud sisemaine ECDIS | Επικαιροποίηση ECDIS εσωτ. ναυσ. | Mise à jour des données Inland ECDIS | Ažuriranje sustava Inland ECDIS | aggiornamento ECDIS interno | Inland ECDIS informācijas atjaunošana | Inland ECDIS informacijos atnaujinimas |
| NEWOBJ | New object | Нов обект | Nuevo objeto | nový objekt | Nyt objekt | neues Objekt | Uus ese | Νέο αντικείμενο | Nouvel objet | Novi objekt | nuovo oggetto | Jauns objekts | Naujas objektas |
| WARNIN | Warning | Внимание | Alarma | varování | Advarsel | Warnung | Hoiatus | Προειδοποίηση | Avertissement | Upozorenje | allerta | Brīdinājums | Įspėjimas |
| CHWWY | Changes of the fairway | Промени във водния път | Cambio en la vía navegable | změna na vodní cestě | Ændring af farvandet | Änderungen des Fahrwassers | Veetee muutmine | Αλλαγή εντός πλωτής οδού | modification de la passe navigable | Promjene u plovnom putu | modifiche della via navigabile | Izmaiņas kuģu ceļā | Pasikeitimai farvateryje |
| CONWWY | Constriction of fairway | Строителни работи по водния път | Estrechamiento de vía navegable | zúžení vodní cesty | Indsnævring af vandvejen | Einengung des Fahrwassers | Veetee konstrikt-sioon | Κατασκευή πλωτής οδού | rétrécissement de la passe navigable | Suženje plovnog puta | strettoia | Ūdens ceļa sašaurinājums | Farvaterio susiaurėjimas |
| DIVER | Diver under the water | Водолазни работи | Presencia de submarinistas | práce pod vodou | Dykkere i vandet | Taucher unter Wasser | Tuuker vee all | Υποβρύχιες εργασίες | plongeurs au travail | Ronilac pod vodom | sommozzatore in immersione | Ūdenslīdēju darbi | Vandenyje naras |
| SPECTR | Special transport | Специализиран транспорт | Transporte especial | zvláštní přeprava | Særlig transport | Sondertransport | Erivedu | Ειδικές μεταφορές | transport spécial | Specijalni prijevoz | trasporto speciale | Īpašs transports | Specialus transportas |
| LOCRUL | Local rules of traffic | Местни (локални) правила за движение | Normas locales de tráfico | místní úprava plavebních předpisů | Lokale trafikregler | lokal gültige Verkehrsvorschriften | Kohalikud liiklusees-kirjad | Τοπικοί κανόνες κυκλοφορίας | règlements de navigation locaux | Lokalni prometni propisi | regole di traffico locali | Vietēji satiksmes noteikumi | Vietinės laivų eismo taisyklės |
| VHFCOV | Radio coverage | Радио покритие (обхват) | Cobertura de radio | rádiové pokrytí | Radiodækning | Funkabdeckung | Raadio leviala | Κάλυψη ασυρμάτου | Couverture radio | Radijska pokrivenost | copertura radio | Radiosignālu pārklājums | Radijo ryšio zona |
| HIGVOL | High voltage cable | Високо напрежение | Línea de alta tensión | vedení vysokého napětí | Højspændingskabler | Hochspannungsleitung | Kõrgepinge-juhtivus | Αγωγός υψηλής τάσης | Ligne haute tension | Visokonaponski kabel | alta tensione | Augstspriegums | Aukštos įtampos kabelis |
| TURNIN | No turning | Забранено извършване на поворот | Prohibido girar | zákaz provádět obrat | Vending ikke tilladt | Wendeverbot | Pööramine keelatud | Απαγόρευση στροφής | Interdiction de viver | Zabranjeno okretanje | divieto di manovra | Pagriezties aizliegts | Apsisukti draudžiama |
| CONBRE | Convoy breadth | Ширина на състава | Manga del convoy | šířka sestavy | Konvojbredde | Verbandsbreite | Konvoi laius | Πλάτος νηοπομπής | largeur du convoi | Širina sastava | larghezza del convoglio | Karavānas platums | Laivų vilkstinės plotis |
| CONLEN | Convoy lenght | Дължина на състава | Eslora del convoy | délka sestavy | Konvojlængde | Verbandslänge | Konvoi pikkus | Μήκος νηοπομπής | longueur du convoi | Duljina sastava | lunghezza del convoglio | Karavānas garums | Laivų vilkstinės ilgis |
| REMOBJ | Removal of object | Премахване на препятствие | Retirada de un objeto | odstranění objektu | Fjernelse af objekt | Bergungsarbeiten | Eseme eemaldamine | Απομάκρυνση αντικειμένου | enlèvement d'objet | Uklanjanje objekta | rimozione di oggetti | Objekta noņemšana | Objekto šalinimas |
| INFSER | Info service | Информационна служба | Servicio de información | Informační servis | Informationstjeneste | Informationsservice | Teabeteenus | Πληροφορίες | Service d'information | Informacijska usluga | servizio informazioni | Informācijas dienests | Informacija |

**SUBJECT CODE**

| OBSTRU | zárlat | Ostaklu | Stremming | Zamknięcie | Obstrução | Restricție | blokáda | zapora | Este | Blockering | Закрыто | Препрека |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PAROBS | részleges tilalom | Ostaklu parzjali | Gedeeltelijke stremming | Częściowe zamknięcie | Obstrução parcial | Restricție parțială | čiastočné prekážky | delna zapora | Osittainen este | Delvis obstruktion | Частично закрыто | Делимична препрека |
| DELAY | késedelem | Dewmien | Oponthoud | Opóźnienie | Demora | Întârziere | meškanie | zamuda | Viivästys | Försening | Задержка | Кашњење |
| VESLEN | hajó hossza | Tul tal-Bastiment | Scheepslengte | Długość statku | Comprimento (embarcação) | Lungimea navei | dĺžka plavidla | dolžina plovila | Aluksen pituus | Fartygslängd | Длина судна | Дужина пловила |
| VESHEI | hajó magassága | Għoli tal-bastiment | Scheepshoogte | Wysokość statku | Altura acima da linha de água (embarcação) | Înălțimea deasupra liniei de plutire | výška plavidla nad hladinou | prosta višina plovila | Aluksen suurin korkeus vedenpinnasta | Fartygets höjd över vattenytan | Высота судна | Максимална висина пловила над водом |
| VESBRE | hajó szélessége | Wisa’ tal-bastiment | Scheepsbreedte | Szerokość statku | Boca (embarcação) | Lățimea navei | šírka plavidla | širina plovila | Aluksen leveys | Fartygsbredd | Ширина судна | Ширина пловила |
| VESDRA | hajó merülése | Fundar meħtieġ għall-bastiment | Diepgang | Zanurzenie statku | Calado (embarcação) | Pescajul navei | ponor plavidla | ugrez plovila | Aluksen syväys | Fartygets djupgående | Осадка судна | Газ пловила |
| AVALEN | rendelkezésre álló hosszúság | Tul disponibbli | Doorvaartlengte | Długość użytkowa | Comprimento disponível | Lungimea admisă | dostupná dĺžka | razpoložljiva dolžina | Käytettävissä oleva pituus | Tillgänglig längd | Допустимая длина | Расположива дужина |
| CLEHEI | szabad űrszelvénymagasság | Fond ta’ spazju ħieles | Doorvaarthoogte | Wysokość w świetle | Altura livre | Gabaritul de înălțime | podjazdná výška | prosta višina prehoda | Alikulkukorkeus | Frihöjd | Допустимая высота | Слободна висина |
| CLEWID | hasznos szélesség | Wisa’ ta’ spazju ħieles | Doorvaartbreedte | Szerokość w świetle | Largura livre | Gabaritul de lățime | prejazdná šírka | prosta širina prehoda | Käytettävissä oleva leveys | Farledsbredd | Допустимая ширина | Слободна ширина |
| AVADEP | rendelkezésre álló vízmélység | Fond disponibbli | Beschikbare diepte | Głębokość użytkowa | Profundidade disponível | Adâncimea disponibilă | dostupná hĺbka | razpoložljiva globina | Käytettävissä oleva syväys | Tillgängligt djup | Существующая глубина | Расположива дубина |
| NOMOOR | veszteglési tilalom | Irmiġġ projbit | Afmeerverbod | Zakaz cumowania | Proibição de amarrar | Interdicția de a acosta | zákaz vyväzovania | prepovedan privez | Kiinnittyminen kielletty | Förtöjning förbjuden | Швартовка запрещена | Забрањено везивање |
| SERVIC | korlátozott üzem | Servizz limitat | Beperkte service | Usługa ograniczona | Serviço limitado | Manevră restricționată | obmedzená prevádzka | omejena storitev | Rajoitettu palvelu | Begränsad service | Ограниченое обслуживание | Ограничена услуга |
| NOSERV | üzemszünet | Servizz sospiż | Geen bediening | Usługa niedostępna | Interrupção do serviço | Întreruperea serviciului | zastavená prevádzka | ni storitve | Ei palvelua | Ingen service | Не обслуживаемое | Без услуге |
| SPEED | sebességkorlátozás | Veloċità | Snelheidsbeperking | Ograniczenie szybkości | Limite de velocidade | Limită de viteză | najvyššia povolená rýchlosť | hitrost | Nopeus | Hastighet | Ограничение скорости | Брзина |
| WAVWAS | hullámkeltést elkerülni | Tranja tal-mewġ projbita | Golfslag vermijden | Zakaz tworzenia fal | Não causar ondulação | Formarea valurilor interzisă | zákaz vlnobitia a sania | prepovedano povzročanje valov | Voimakkaan aallokon tuottaminen kielletty | Undvik svall | Берегись волны | Забрањено прављење таласа |
| PASSIN | találkozás tilos | Passaġġ projbit | Ontmoeten verboden | Zakaz wymijania | Proibição de passar | Traversarea interzisă | zákaz preplávania | prepovedan prehod | Ei läpikulkua | Passering förbjuden | Нет прохода | Забрањен пролаз |
| ANCHOR | horgonyozni tilos | Ankraġġ projbit | Ankeren verboden | Zakaz kotwiczenia | Proibição de ancorar | Ancorarea interzisă | zákaz kotvenia | prepovedano sidranje | Ei ankkuroitumista | Ankring förbjuden | Якорная стоянка запрещена | Забрањено сидрење |
| OVRTAK | előzni tilos | Projbit il-qbiż ta’ bastimenti oħra | Voorbijlopen verboden | Zakaz wyprzedzania | Proibição de cruzar ou ultrapassar | Depășirea interzisă | zákaz predchádzania | prepovedano prehitevanje | Ei ohittamista | Omkörning förbjuden | Обгон запрещен | Забрањено престизање |
| MINPWR | minimális teljesítmény | Potenza minima | Minimaal vermogen | Minimalna moc napędu | Potência mínima | Putere minimă | minimálny výkon | najmanjša moč | Vähimmäisteho | Minsta motoreffekt | минимальная мощность | Минимална снага |
| DREDGE | kotrási munkálatok | Tħammil | Baggerwerkzaamheden | Pogłębianie | Dragagens | Lucrări de dragaj | bagrovacie práce | poglabljanje dna | Ruoppaustyöt | Muddring | Встречное движение | Багеровање |
| WORK | munkálatok | Xogħol | Werkzaamheden | Prace | Trabalhos | Lucrări | práce | delo | Työt | Arbeten | Проводятся работы | Радови |
| EVENT | rendezvény | Avveniment | Evenement | Impreza | Evento | Eveniment | udalosť | prireditev | Tapahtumat | Evenemang | Мероприятие | Догађај |
| CHGMAR | forgalmi jelek változtatása | Bidla fis-sinjali | Gewijzigde markering | Zmiana oznakowania | Alteração da sinalização | Semnalizare modificată | zmena značenia | sprememba oznak | Merkit muuttuneet | Ändrad märkning | Изменение СНО | Промена знака |
| CHGSER | üzemidõ változtatása | Servizz modifikat | Gewijzigde bediening | Zmiana obsługi | Alteração do serviço | Manevre modificate | zmena prevádzky | sprememba storitve | Palvelu muuttunut | Förändrad drift | Изменение часов работы | Промена услуге |
| SPCMAR | speciális jelek | Sinjali speċjali | Bijzondere markeringen | Znaki specjalne | Sinalização especial | Semnalizare specială | špeciálne značenie | posebne oznake | Erikoismerkit | Särskilda markeringar | Специальные знаки | Посебне ознаке |
| EXERC | gyakorlatok | Eżerċizzji | Oefeningen | Ćwiczenia | Exercícios | Exerciții | cvičenia | vaje | Harjoitukset | Övningar | Испытания | Вежбе |
| LEADEP | minimális mélység | L-inqas fond imkejjel | Minst gepeilde diepte | Najmniejsza zmierzona głębokość | Profundidade mínima medida | Adâncimea minimă | najnižšia nameraná hĺbka | najmanjša izmerjena globina | Matalin luodattu syvyys | Minsta lodade djup | Минимальная глубина | Најмања измерена дубина |
| LEVDEC | csökkenő vízállás | Livell tal-ilma li qed jitbaxxa | Afnemend water | Spadek stanu wody | Descida do nível da água | Scăderea nivelului apei | klesajúca vodná hladina | nižanje vodostaja | Vedenkorkeus laskee | Sjunkande vattennivå | Снижение уровня воды | Водостај у опадању |
| LEVRIS | emelkedő vízállás | Livell tal-ilma li qed jogħla | Wassend water | Wzrost stanu wody | Subida do nível da água | Creșterea nivelului apei | stúpajúca vodná hladina | višanje vodostaja | Vedenkorkeus nousee | Stigande vattennivå | Повышение уровня воды | Водостај у порасту |
| ANNOUN | hirdetmény | Avviż | Aankondiging | Komunikat | Comunicado | Anunț | oznámenie | obvestilo | Ilmoitus | Meddelande | Объявление | Најава |
| LIMITA | korlátozás | Restrizzjonijiet | Beperkingen | Ograniczenia | Restrições | Limitări | obmedzenia | omejitve | Rajoitukset | begränsningar | Ограничение | Ограничење |
| CANCEL | hirdetmény visszavonva | Avviż annullat | Bericht ingetrokken | Komunikat odwołany | Aviso anulado | Mesaj anulat | správa bola zrušená | obvestilo preklicano | Ilmoitus peruutettu | Återkallad märkning | Отмена извещения | Повлачење издатог Саопштења |
| MISECH | hamis radarvisszhangok | Eki foloz tar-radar | Valse radarecho's | Fałszywe echa radarowe | Ecos radar falsos | Ecou radar fals | falošná odozva | napačni odmevi radarja | Virheellisiä tutkakaikuja | Falska radarekon | Ложная радарная цель | Лажни радарски одраз |
| ECDISU | Inland ECDIS frissítés | aġġornament tal-ECDIS Interna | Inland ECDIS-update | Aktualizacja Inland ECDIS | Atualização ECDIS-fluvial | actualizarea datelor ECDIS | aktualizácia Inland ECDIS | posodobitev celinskega ECDIS | Sisävesiliikenteen ECDIS:n päivitys | Uppdatering av inlands-ECDIS | Обновление информации для Inland ECDIS | Ажуриран Inland ECDIS |
| NEWOBJ | Új objektum | Oġġett ġdid | Nieuw object | Nowy obiekt | Novo objeto | Obiect nou | nový objekt | nov objekt | Uusi kohde | Nytt föremål | Новый объект | Нови објекат |
| WARNIN | figyelmeztetés | Twissija | Waarschuwing | Ostrzeżenie | Alerta | Avertisment | varovanie | opozorilo | Varoitus | Varning | Предупреждение | Упозорење |
| CHWWY | hajóútváltozás | Bidliet tal-kanal navigabbli | Verandering van de vaarweg | Zmiany toru wodnego | Alterações na via navegável | Modificări ale șenalului navigabil | zmeny na vodnej ceste | spremembe na plovni poti | vesiväylän muutos | Ändring av farleden | Изменение фарватера | Промене у пловном путу |
| CONWWY | hajóútszűkület | Restrizzjoni tal-kanal navigabbli | Beperking van de vaarweg | Zwężenie toru wodnego | Estreitamento da via navegável | Îngustarea șenalului navigabil | zúženie vodnej cesty | zoženje plovne poti | vesiväylän kaventuminen | Smalare farled | Сужение фарватера | Сужење пловног пута |
| DIVER | vízalatti munkák | Bugħaddas taħt l-ilma | Duikwerkzaamheden | Nurek pod wodą | Presença de mergulhadores | Scafandru în apă | práce pod vodou | dela pod vodo | sukeltaja veden alla | Dykare i vattnet | водолаз под водой | Ронилац под водом |
| SPECTR | különleges szállítás | Trasport speċjali | Bijzonder vervoer | Transport specjalny | Transporte especial | Transport special | špeciálna preprava | posebni prevoz | erikoiskuljetus | Specialtransport | Специальный транспорт | Специјални транспорт |
| LOCRUL | helyi közlekedési rend (R) | Regoli lokali tat-traffiku | Lokale verkeersregels | Miejscowe przepisy ruchu statków | Regras de tráfego locais | Regulamente locale de trafic | lokálne pravidlá plavby | lokalna prometna pravila | paikalliset liikennöintisäännöt | Lokala trafikregler | Местные правила судоходства | Локална правила пловидбе |
| VHFCOV | rádiós lefedettség | Kopertura tar-radju | Radiodekking | Pokrycie radiowe | Cobertura rádio | Acoperire radio | rádiové pokrytie | pokritost radijskih zvez | Radion kuuluvuusalue | Radiotäckning | Покрытие радиосигналом | Покривеност радио сигналом |
| HIGVOL | nagy feszültségű átfeszítés | Kejbil b’voltaġġ għoli | Hoogspanningskabel | Linia wysokiego napięcia | Linha de alta tensão | Linie de înaltă tensiune | vedenie vysokého napätia | visokonapetostni kabel | Korkeajännitejohto | Högspänningsledning | высоковольтный кабель | Кабл под високим напоном |
| TURNIN | megfordulni tilos | Dawran projbit | Draaien verboden | Zakaz zawracania | Proibição de inverter marcha | Întoarcerea interzisă | Zákaz vykonávania obratov | prepovedano obračanje | Kääntyminen kielletty | Vändning förbjuden | Поворот запрещен | Забрањено окретање |
| CONBRE | a kötelék szélessége | Wisa’ tal-konvoj | Breedte van de duwsleep | Szerokość zestawu | Largura do comboio | Lățimea convoiului | šírka zostavy | širina konvoja | kytkyeen leveys | Konvojbredd | Ширина состава судов | Ширина састава |
| CONLEN | a kötelék hossza | Tul tal-konvoj | Lengte van de duwsleep | Długość zestawu | Comprimento do comboio | Lungimea convoiului | dĺžka zostavy | dolžina konvoja | kytkyeen pituus | Konvojlängd | Длина состава судов | Дужина састава |
| REMOBJ | mentési munkálatok | Tneħħija ta’ oġġett | Verwijderen van object | Usuwanie objektu | Remoção de objeto | Schimbarea obiectului | odstránenie objektu | odstranitev objekta | Kohteen poistaminen | Bärgning av föremål | Удаление объекта | Уклањање објекта |
| INFSER | Tájékoztatás | Servizz ta’ informazzjoni | Informatieservice | Serwis informacyjny | Serviço de informações | Mesaj informativ | Informačná služba | informacijska služba | Tietopalvelu | Informationstjänst | Информационная служба | Инфо-сервис |

**TARGET GROUP CODE**

| ALL | all | Всички | Todos | všichni | Alle | alle | Kõik | Όλα | Tous les usagers | Sve vrste plovila | tutti | Visi | Visi |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CDG | vessels with dangerous goods | Търговски кораб превозващ опасни товари | Embarcaciones con mercancías peligrosas | plavidla určená pro přepravu nebezpečného nákladu | Fartøjer med farligt gods | Fahrzeuge mit gefährlichen Gütern | Ohtliku lastiga kaubalaev | Εμπορικά σκάφη με επικίνδυνο φορτίο | Transports de matières dangereuses | Komercijalno plovilo s opasnim teretom | navi mercantili con carichi pericolosi | Komerckuģi ar bīstamu kravu | Prekybos laivai su pavojingu kroviniu |
| COM | commercial vessels | Търговски кораб | Embarcaciones comerciales | plavidla pro přepravu nákladu | Handelsskibe | kommerzielle Fahrzeuge | Kauba-laevad | Εμπορικά σκάφη | Bateau de commerce | Komercijalno plovilo | navi mercantili | Komerckuģi | Prekybos laivai |
| PAX | passenger vessels | Пътнически кораб | Embarcaciones de pasajeros | plavidla pro přepravu cestujících | Passagerskibe | Fahrgastschiffe | Reisilaevad | Επιβατηγά σκάφη | Bateau à passagers | Putničko plovilo | navi passeggeri | Pasažieru kuģi | Keleiviniai laivai |
| PLE | pleasure crafts | Спортен или увеселителен кораб | Embarcaciones de recreo | sportovní plavidla | Fritidsfartøjer | Sportboote | Lõbusõidu-laev | Σκάφη αναψυχής | Bateau de plaisance | Plovilo za razonodu | natanti da diporto | Izpriecceļojumu kuģi | Pramoginiai laivai |
| CNV | convoys | Състав | Convoyes | sestavy | Konvojer | Verbände | Koosseis | Νηοπομπές | Convoi | Sastav | convogli | Karavānas | Vilkstinės |
| PUS | pushed convoys | Тласкан състав | Convoyes empujados | tlačné sestavy | Skubbekonvojer | Schubverbände | Tõugatav koosseis | Ωθούμενες νηοπομπές | convois poussés | Potiskivani sastav | convogli spinti | Karavānas ar stūmēju | Stumiamos vilkstinės |
| NNU | non navigating users | Потребители извън корабоплаването | Usuarios no navegantes | jiní než nautiční uživatelé | Brugere uden for skibsfart | andere als nautische Nutzer | muud kasutajad, v.a alused | Χρήση εκτός ναυσιπλοΐας | usagers non navigants | Korisnici koji ne plove | utilizzatori non in navigazione | Ar kuģošanu nesaistīti izmantotāji | Ne laivybos tikslais |
| LOA | loaded vessels | Натоварен кораб | Embarcaciones con carga | naložená plavidla | Lastede fartøjer | beladene Fahrzeuge | Laadungis laevad | Φορτωμένα σκάφη | bateaux chargés | Natovareno plovilo | navi cariche | Piekrauti kuģi | Laivai su kroviniu |
| SMA | small crafts | Малък кораб | Embarcaciones pequeñas | malá plavidla | Små fartøjer | Kleinfahrzeuge | Väikelaevad | Μικρά σκάφη | petites embarcations | Malo plovilo | piccoli natanti | Mazas tonnāžas peldlīdzekļi | Maži laivai |
| CND | convoys with dangerous goods | Състав превозващ опасен товар | Convoyes con mercancías peligrosas | sestava pro přepravu nebezpečného nákladu | Konvojer med farligt gods | Verbände mit gefährlichen Gütern | Ohtliku lastiga konvoid | Νηοπομπές με επικίνδυνα εμπορεύματα | convois de matières dangereuses | Sastav sa opasnim teretom | convogli con carichi pericolosi | Karavānas ar bīstamu kravu | Vilkstinės su pavojingu kroviniu |
| MOV | motorized vessels | Моторен кораб | Embarcaciones motorizadas | plavidla s vlastním strojním pohonem | Motordrevne fartøjer | Fahrzeuge mit Maschinenantrieb | Mootorlaevad | Μηχανοκίνητα σκάφη | bateaux motorisés | Plovilo s motorom | navi a motore | Motorizēti kuģi | Motoriniai laivai |
| NMV | non-motorized vessels | Немоторен кораб | Embarcaciones no motorizadas | plavidla bez vlastního strojního pohonu | Ikkemotordrevne fartøjer | Fahrzeuge ohne Maschinenantrieb | Mootorita laevad | Μη μηχανοκίνητα σκάφη | bateaux non motorisés | Plovilo bez motora | navi non a motore | Nemotorizēti kuģi | Nemotoriniai laivai |
| WOC | worksite crafts | Работни плаващи средства | Embarcaciones de obras | plavidla vykonávající práce na vodní cestě | Flydende arbejdsplatforme | Baufahrzeuge | Töölaevad | Σκάφη εργοταξίου | bateaux de service | Radno plovilo | navi cantiere | Darblaukuma peldlīdzekļi | Statybvietės plaukiojančios priemonės |

**TARGET GROUP CODE**

| ALL | mindenkire vonatkozó | kollha | Alle scheepvaart | Wszystkie jednostki | Todos os utentes | toți utilizatorii | všetci (používatelia) | vse | Kaikki | Alla | Все суда | Сви |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CDG | kereskedelmi hajó veszélyes áruval | bastimenti b’merkanzija perikoluża | Beroepsvaart gevaarlijke stoffen | Statki handlowe przewożące ładunki niebezpieczne | Embarcações de comércio com mercadorias perigosas | transport de materiale periculoase | plavidlá s nebezpečným tovarom | trgovska plovila z nevarnim blagom | Kauppa-alukset, joissa on vaarallisia aineita | Handelsfartyg med farlig last | Торговое судно с опасным грузом | Комерцијална пловила са опасним теретом |
| COM | kereskedelmi hajó | bastimenti kummerċjali | Beroepsvaart | Statki handlowe | Embarcações de comércio | navă comercială | obchodné lode | trgovska plovila | Kauppa-alukset | Handelsfartyg | Торговое судно | Комерцијално пловило |
| PAX | személyszállító hajó | bastimenti tal-passiġġieri | Passagiersschepen | Statki pasażerskie | Embarcações de passageiros | navă de pasageri | osobné lode | potniška plovila | Matkustaja-alukset | Passagerarfartyg | Пассажирское судно | Путничко пловило |
| PLE | kedvtelési célú hajó | opri tal-baħar għar-rikreazzjoni | Recreatievaart | Statki rekreacyjne | Embarcações de recreio | navă de agrement | rekreačné a športové plavidlá | plovila, namenjena za šport in rekreacijo | Huvialukset | Fritidsbåtar | Прогулочное судно | Спортско-рекреативно пловило |
| CNV | hajókötelék | konvojs | Samenstel | Zestawy | Comboios | convoi | zostavy | konvoji | Kytkyeet | Konvojer | Состав | Састави |
| PUS | tolt kötelékek | konvojs imbuttati | Duweenheid | Zestawy pchane | Comboios empurrados | convoi împins | tlačné zostavy | potisni konvoji | Työnnetyt kytkyeet | Påskjuten konvoj | Толкаемый состав | Потискивани састави |
| NNU | nem hajózási használók | utenti li ma jinnavigawx | Niet nautische gebruikers | Użytkownicy nieżeglujący | Utentes não navegantes | personal nenavigant | neplávajúci užívatelia | uporabniki, ki ne plujejo | muut käyttäjät kuin vesilläliikkujat | Andra än sjöfarande | для несудоходных целей | Корисници који не плове |
| LOA | berakott hajó | bastimenti mgħobbija | Beladen schepen | Statki załadowane | Embarcações carregadas | nava încărcată | naložené plavidlá | natovorjena plovila | Lastatut alukset | Lastade fartyg | Груженое судно | Натоварено пловило |
| SMA | kishajó | opri tal-baħar żgħar | Kleine vaartuigen | Mały statek | Pequenas embarcações | șalupă mică | malé plavidlá | mali plovni objekti | Pienet alukset | Småbåtar | Малое судно | Мало пловило |
| CND | veszélyes árut szállító kötelék | konvojs b’merkanzija perikoluża | Samenstel met gevaarlijke stoffen | Zestaw z ładunkiem niebezpiecznym | Comboios com mercadorias perigosas | convoi cu mărfuri periculoase | zostavy s nebezpečným tovarom | konvoji z nevarnim blagom | Kytkyeet, joissa vaarallisia aineita | Konvojer med farligt gods | Состав с опасными грузами | Састави са опасним теретом |
| MOV | motoros hajó | bastimenti b’mutur | Vaartuigen met motor | Statek o napędzie mechanicznym | Embarcações motorizadas | nave propulsate | plavidlá s vlastným strojným pohonom | motorizirana plovila | Moottoroidut alukset | Motordrivna fartyg | Моторные суда | Mоторизовано пловило |
| NMV | motor nélküli hajó | bastimenti li ma għandhomx mutur | Vaartuigen zonder motor | Statek bez napędu mechanicznego | Embarcações não-motorizadas | nave nepropulsate | plavidlá bez vlastného strojného pohonu | plovila brez motorja | Muut kuin moottoroidut alukset | Icke motordrivna fartyg | Безмоторные суда | Немоторизовано пловило |
| WOC | úszómunkagép | opri tal-baħar ta’ sit tax-xogħol | Schepen voor bouwwerkzaamheden | Statek roboczy | Embarcações de estaleiro | șalupa tehnică | plavidlá vykonávajúce práce na vodnej ceste | plovni objekti na delovni lokaciji | Työmaa-alukset | Arbetsfartyg | Технический флот | Пловни објекат на градилишту |

**TYPE CODE**

| RIV | river | Река | Río | řeka | Flod | Fluss | Jõgi | Ποταμός | Rivière | Rijeka | fiume | Upe | Upė |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CAN | canal | Канал | Canal | kanál | Kanal | Kanal | Kanal | Κανάλι | Canal | Kanal | canale | Kanāls | Kanalas |
| LAK | lake | Езеро | Lago | jezero | Sø | See | Järv | Λίμνη | Bassin | Jezero | lago | Ezers | Ežeras |
| FWY | fairway | Фарватер | Vía navegable | plavební dráha | Farvand | Fahrwasser | Faarvaater | Δίαυλος | Chenal | Plovni put | canale navigabile | Kuģu ceļš | Farvateris |
| LCK | lock | Бараж | Esclusa | plavební stupeň | Sluse | Schleuse | Lüüs | Υδατοφράκτης | Ecluse | Prevodnica | conca | Slūžas | Šliuzas |
| BRI | bridge | Мост | Puente | most | Bro | Brücke | Sild | Γέφυρα | Pont | Most | ponte | Tilts | Tiltas |
| RMP | ramp | Рампа | Rampa | rampa | Rampe | Rampe | Ramp | Πλατοφόρμα | Plan incliné | Rampa | rampa | Traps | Rampa |
| BAR | weir | Бент | Presa | jez | Overløbsdæmning | Wehr | Ülevoolupais | Φράγμα ποταμού | Barrage | Pregrada | sbarramento | Aizsprosts | Užtvanka |
| BNK | bank | Бряг | Margen | břeh | Bred | Ufer | Kallas | Όχθη | Berge | Obala | sponda | Krasts | Krantas |
| GAU | tide gauge | Водомерна станция | Mareógrafo | vodočet | Tidevandsmåler | Pegel | Tõusu ja mõõna mõõtur | Παλιρροιογράφος | Échelle/Marégraphe | Vodomjerna postaja | mareometro | Paisuma/ bēguma līmeņrādis | Mareografas |
| BUO | buoy | Буй | Boyas | bóje | Bøje | Boje | Poi | Σημαντήρας | Bouée | Plutača | boa | Boja | Plūduras |
| BEA | beacon | Фар | Balizas | maják | Fast sømærke | Bake | Paak | Υφαλοδείκτης | Balise | Svjetleći obalni znak | gavitello | Bāka | Švyturys |
| ANC | anchoring area | Котвена стоянка | Fondeadero | kotviště | Opankringsområde | Ankerplatz | Ankruplats | Περιοχή αγκυροβολίας | zone de stationnement | Sidrište | area di ancoraggio | Enkurvieta | Inkaravimosi vieta |
| BER | berth | Корабно място (кей) | Atracadero | vývaziště | Kajplads | Liegestelle | Kai | Αποβάθρα | point de stationnement | Pristanište | attracco | Pietauvošanas vieta | Prieplauka |
| MOO | mooring facility | Швартово устройство | Amarradero | vyvazovací zařízení | Fortøjningsanlæg | Festmacheeinrichtung | Sildumis-rajatis | Εγκατάσταση πρόσδεσης | Aménagement d'amarrage | Oprema za vezivanje | struttura di ormeggio | Pietauvošanas ierīce | Švartavimosi įrenginys |
| TER | terminal | Терминал | Terminal | překladiště | Terminal | Umschlagplatz | Terminal | Τερματικός σταθμός | Terminal | Terminal | terminal | Termināls | Terminalas |
| HAR | harbour | Пристанище | Puerto | přístav | Havn | Hafen | Sadam | Λιμάνι | Port | Luka | porto | Osta | Uostas |
| FDO | floating dock | Плаващ док | Muelle flotante | plovoucí dok | Flydedok | Schwimmdock | Ujuvdokk | Πλωτή αποβάθρα | Pontons | Plutajući dok | bacino galleggiante | Peldošais doks | Plūdrusis dokas |
| CAB | cable overhead | Далекопровод | Cable aéreo | vzdušné vedení kabelu | Luftledning | Überspannung | Elektriliin | Εναέριο καλώδιο | Câble suspendu (Chemin de câbles, lignes électriques) | Viseći dalekovod | cavo sospeso | Kabeļu pārvads | Oro linijos kabelis |
| FER | ferry | Ферибот | Transbordador | přívoz | Kabelfærge | Fähre | Parvlaev | Οχηματαγωγό | Bac | Skela | funivia | Prāmis | Keltas |
| PIP | pipeline | Тръбопровод | Conductos | potrubí | Rørledning | Pipeline | Torujuhe | Αγωγός | Oléoduc | Cjevovod | conduttura | Cauruļvads | Vamzdynas |
| PPO | pipeline overhead | Надземен тръбопровод | Conductos aéreos | nadzemní vedení potrubí | Rørbro | Rohrbrücke | Torustiku liin | Εναέριος αγωγός | Oléoduc aérien | Viseći cjevovod | conduttura sospesa | Cauruļvadu pārvads | Virš vandens iškeltas vamzdynas |
| HFA | harbour facility | Пристанищно оборудване | Instalación portuaria | přístavní zařízení | Havneanlæg | Hafeneinrichtung | Sadama rajatis | Λιμενική εγκατάσταση | Installation portuaire | Lučke građevine | installazione portuale | Ostas iekārta | Uosto įranga |
| HMO | harbour master's office | Капитан на пристанището | Capitanía de puerto | kancelář vedoucího přístavu | Havnekontor | Hafenmeisterbüro | Sadamakap-teni büroo | Λιμεναρχείο | Capitainerie | Kapetanija | capitaneria di porto | Ostas kapteiņa dienests | Uosto kapitono biuras |
| SHY | shipyard | Корабостроителница | Astillero | loděnice | Skibsværft | Werft | Laevatehas | Ναυπηγείο | Chantier naval | Brodogradilište | cantiere navale | Kuģu būvētava | Laivų statykla |
| REF | refuse dump | Пункт за събиране на отпадъци | Depósito de residuos | sběrna odpadu | Affaldsdeponi | Abfallsammelstelle | Prahikallur | Χώρος απόρριψης αποβλήτων | Station de collecte de déchets | Skladište otpadnog materijala | punto raccolta rifiuti | Atkritumu izgāztuve | Atliekų surinkimo aikštelė |
| MAR | notice mark | Информационно табло | Panel de señalización | plavební znak | Advarselsmærke | Schifffahrtszeichen | Teatise tähis | Προειδοποιητικό σημείο | Panneau de signalisation | Plovidbena oznaka | segnalazione | Informatīva zīme | Įspėjimo ženklas |
| LIG | light | Светещ знак | Alumbrado | světlo | Lys | Leuchtfeuer | Tuli | Φανός | Feux | Svjetlo | fanale | Gaisma | Šviesos |
| SIG | signal station | Сигнална станция | Estación de señalización | signální stanice | Signalstation | Signalstation | Märguande-punkt | Σηματοφορικός σταθμός | Station de signalisation | Signalna postaja | stazione di segnalamento | Signālstacija | Signalų postas |
| TUR | turning basin | Район за поворот | Cuenca de maniobra | obratiště | Vendebassin | Wendestelle | Pöörde eeldokk | Λεκάνη στροφής | Bassin de virage | Mjesto za okretanje | bacino di manovra | Pagriešanās vieta | Apsisukimo baseinas |
| CBR | canal bridge | Мост на канал | Puente canal | přemostění kanálu | Kanalbro | Kanalbrücke | Kanalisild | Γέφυρα καναλιού | Pont Canal | Most na kanalu | acquedotto | Kanāla tilts | Kanalo tiltas |
| TUN | tunnel | Тунел | Túnel | tunel | Tunnel | Tunnel | Tunnel | Σήραγγα | Tunnel | Tunel | tunnel | Tunelis | Tunelis |
| BCO | border control | Граничен контрол | Puesto fronterizo | hraniční kontrola | Grænsekontrol | Grenzstation | Piirikontroll | Συνοριακός έλεγχος | Poste de douane | Granična kontrola | controllo di frontiera | Robežkontrole | Pasienio kontrolė |
| REP | reporting point | Контролен пост | Puesto de notificación | místo hlášení | Rapporteringspunkt | Meldepunkt | Aruandlus-punkt | Σημείο αναφοράς | Poste de contrôle | Kontrolna točka | punto di controllo | Ziņošanas vieta | Kontrolės punktas |
| FLO | flood gate | Шлюз | Compuertas | ochranná vrata | Overløbslukke | Sperrtor | Tõusuvee-tõke | Θύρα υδροφράχτη | Porte de garde | Vrata prevodnice | paratoia | Slūžas | Dambos uždoris |
| SLI | ship lift | Корабен елеватор/подемник | Elevador de barcos | lodní výtah | Skibskran | Schiffshebewerk | Laevalift | Ανυψωτήρας πλοίων | ascenseur à bateaux | Dizalo za brod | ascensore per navi | Kuģu lifts | Laivų keltuvas |
| DUK | culvert | Водосток | Paso | propustek | Gennemløbsrør | Düker | Toruviik | Υδαταγωγός | caniveau | Odvodni kanal | tomba a sifone | Ūdensvadne | Pralaida |
| VTC | vessel traffic centre | Център за управление на корабоплаването | Centro de tráfico naval | centrum řízení plavby | Skibstrafikcenter | Verkehrszentrale | Laevaliikluskeskus | Κέντρο ρύθμισης της κυκλοφορίας των πλοίων | centre de gestion de trafic | Kontrolni centar | Centro di controllo del traffico navale | Kuģu satiksmes centrs | Laivų eismo centras |
| RES | reservoir | Резервоар | Embalse | nádrž | Reservoir | Stauhaltung | Hoidla | Δεξαμενή | bassin réservoir | Akumulacija | bacino | Rezervuārs | Tvenkinys |
| LKB | lock basin | Шлюзова камера | Esclusa con cabezas separadas | plavební komora | Kedelsluse | Schleusenkammer | Lüüsitiik | Θάλαμος δεξαμενής ανύψωσης | sas d’écluse | Bazen prevodnice | conca di navigazione | Slūžu baseins | Šliuzo baseinas |
| BRO | bridge opening | Плавателен отвор на мост | Apertura de puente | mostní pole | Oplukkelig bro | Brückendurchfahrtsöffnung | Sild avatud | Άνοιγμα γέφυρας | passe de pont | Otvor mosta | apertura del ponte | Tilta atvērums | Tilto anga |
| BNS | bunker/fuelling station | Място за бункероване | Tanque/Estación de suministro de combustible | tankovací stanice | bunker/tankstation | Bunkerstation | Punkerdus-/tankimisjaam | Αποθήκη καυσίμων/σταθμός τροφοδοσίας καυσίμων | poste de ravitaillement | Terminal za opskrbu gorivom | stazione di bunkeraggio / rifornimento | Tvertne/uzpildes stacija | Bunkeris / kuro pildymo punktas |

**TYPE CODE**

| RIV | folyó | xmara | Rivier | Rzeka | Rio | fluviu | rieka | reka | Joki | Flod | Река | Река |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CAN | csatorna | kanal | Kanaal | Kanał | Canal | canal | kanál | kanal | Kanava | Kanal | Канал | Канал |
| LAK | tó | lag | Meer | Jezioro | Lago | lac | jazero | jezero | Järvi | Sjö | Озеро | Језеро |
| FWY | hajóút | kanal navigabbli | Vaarweg | Tor wodny | Via navegável | șenal | plavebná dráha | plovna pot | Väylä | Farled | Фарватер | Пловни пут |
| LCK | zsilip | bieb tal-ilma magħluq | Sluis | Śluza | Eclusa | ecluză | plavebný stupeň | zapornica | Sulku | Sluss | Шлюз | Преводница |
| BRI | híd | pont | Brug | Most | Ponte | pod | most | most | Silta | Bro | Мост | Мост |
| RMP | rámpa | rampa | Helling | Pochylnia | Rampa | rampă | rampa | rampa | Ramppi | Ramp | Рампа | Рампа |
| BAR | gát | diga sommerġibbli | Stuw | Jaz | Barragem | baraj | hať | jez | Pato | Damm | Плотина | Устава |
| BNK | part | xatt | Oever | Brzeg | Margem | banc | breh | breg | Ranta | Bank | берег водоема | Обала (реке, канала, језера) |
| GAU | vízmérce | kejl il-marea | Peilschaal | Wodowskaz | Fluviómetro/marégrafo | miră de maree | vodomerná stanica | vodomerna postaja | Vuorovesimittari | Tidvattenmätare | водомерная станция, водомер | Водомерна станица |
| BUO | bója | baga | Boei | Boja | Boia | geamandură | bója | plovec | Poiju | Boj | Буй | Бова |
| BEA | parti (irány)jel | fanal | Baken | Stawa | Baliza | baliză | maják | svetilnik | Merimerkki | Signalboj | Маяк | Светлећи обалски знак |
| ANC | horgonyzó-hely | żona ta’ ankraġġ | Ankerplaats | Kotwicowisko | Ancoradouro | sector de ancorare | kotvisko | sidrišče | Ankkurointialue | Ankringsområde | Якорная стоянка | Сидриште |
| BER | kikötőhely | irmiġġ | Ligplaats | Miejsce postoju | Cais/fundeadouro | punct de ancorare | výväzisko | privez | Laituripaikka | Kaj | Причал | Пристајалиште |
| MOO | kikötőberendezés | faċilità ta’ rmiġġ | Afmeerfaciliteit | Cumowisko | Posto de amarração | posibilitate de acostare | vyväzovacie zariadenie | naprava za privez | Kiinnittymislaitteisto | Förtöjningsanläggning | Швартовое устройство | Опрема за извезивање |
| TER | rakodó | terminal | Terminal | Terminal | Terminal | terminal | terminál | terminal | Terminaali | Terminal | Терминал | Терминал |
| HAR | kikötő | port | Haven | Port | Porto | port | prístav | pristanišče | Satama | Hamn | Порт | Лука |
| FDO | úszódokk | baċir f’wiċċ l-ilma | Drijvend dok | Dok pływający | Doca flutuante | ponton | plávajúci dok | plavajoči dok | Uiva telakka | Flytdocka | плавучий док | Пловећи док |
| CAB | átfeszítés | kejbil fl-ajru | Overhangende kabel | Kabel napowietrzny | Cabo aéreo | cablu suspendat | vzdušné vedenie kábla | zračni daljnovod | Kaapeli yläpuolella | Luftledning | Подвесной кабель | Далековод |
| FER | komp | lanċa | Veerpont | Prom | Ferry | bac | prievozná loď (kompa) | trajekt | Lautta | Färja | Паром | Скела |
| PIP | csővezeték | pipeline | Pijpleiding | Rurociąg | Conduta | conducte | potrubie | cevovod | Putkijohto | Pipeline | Трубопровод | Цевовод |
| PPO | csőhíd | pipeline fl-ajru | Overhangende pijpleiding | Rurociąg napowietrzny | Conduta aérea | conducte suspendate | vzdušné vedenie potrubia | zračni cevovod | Putkijohto yläpuolella | Luftpipeline | Надземный трубопровод | Надземни цевовод |
| HFA | kikötői létesítmény | faċilità portwarja | Havenfaciliteit | Obiekt portowy | Instalação portuária | facilități portuare | prístavné zariadenia | pristaniška naprava | Satamalaitteisto | Hamnanläggning | Портовое оборудование | Лучка инфраструктура |
| HMO | kikötő kapitányság | kapitanerija | Havenkantoor | Kapitanat portu | Capitania do porto | căpitănie | Kapitanát | pristaniška kapitanija | Satamakonttori | Hamnkaptenens kontor | Капитания порта | Лучка капетанија |
| SHY | hajógyár | tarzna | Scheepswerf | Stocznia | Estaleiro naval | șantier naval | lodenica | ladjedelnica | Telakka | Varv | Судостроительный завод | Бродоградилиште |
| REF | hulladéklerakó | post għar-rimi ta’ skart | Afval afgiftepunt | Wysypisko śmieci | Instalação de recolha de resíduos | stație de colectare a deșeurilor | skládka odpadu | odlagališče odpadkov | Jäteasema | Sopinsamlingspunkt | отвал грунта | Складиште отпадних материја |
| MAR | hajózási jel(zés) | sinjal ta’ avviż | Verkeersteken | Znak informacyjny | Painel de sinalização | panou de semnalizare | plavebný znak | plovbna oznaka | Ilmoitusmerkki | Trafikmärke | Информационный знак | Пловидбени знак |
| LIG | fény | dawl | Licht | Światło | Luz | semnal luminos | svetlo | svetloba | Valo | Ljus | Огонь | Светло |
| SIG | jelzőállomás | stazzjon tas-sinjalar | Seinstation | Stacja sygnalizacyjna | Estação de sinalização | stație de semnalizare | signálna stanica | signalna postaja | Merkinantoasema | Signalstation | Сигнальная станция | Сигнална станица |
| TUR | fordítóhely | baċir għad-dawran | Zwaaikom | Obrotnica | Bacia de viragem | loc de rondou | obratisko | obračališče | Kääntöallas | Vändplats | разворотный бассейн | Базен за маневрисање |
| CBR | csatornahíd | pont fil-kanal | Aquaduct | Most kanałowy | Ponte-aqueduto | pod canal | akvadukt | most čez kanal | Kanavasilta | Kanalbro | Аквиадук | Мост на каналу |
| TUN | alagút | mina | Tunnel | Tunel | Túnel | tunel | tunel | predor | Tunneli | Tunnel | Туннель | Тунел |
| BCO | határállomás | kontroll fil-fruntieri | Grensstation | Kontrola graniczna | Posto fronteiriço | punct control trecere frontieră | hraničná kontrola | mejna kontrola | Rajatarkastus | Gränskontroll | Пограничный контроль | Гранична контрола |
| REP | jelentkezési pont | punt ta’ rappurtar | Meldpunt | Punkt meldunkowy | Ponto de notificação | punct raportare | miesto hlásenia | točka javljanja | Raportointipiste | Rapporteringspunkt | Точка оповещения | Пријавна тачка |
| FLO | zsilipkapu | xatba għall-għargħar | Keersluis | Śluza | Comporta | poartă pentru regularizare debit | protipovodňové vráta | drsna vrata | Sulkuportti | Dammlucka | Заградительные ворота шлюза | Устава за евакуацију поплавног таласа |
| SLI | hajólift | makkinarju għall-irfigħ tal-bastimenti | Scheepslift | Podnośnia statków | Elevador de navios | sincrolift nave | lodný výťah | ladijsko dvigalo | Laivahissi | Fartygshiss | Судоподъемник | Бродски лифт |
| DUK | búvár | kanal tad-drenaġġ | Duiker | Przepust | Aqueduto | scafandru | zhybka | kanal | Holvirumpu | Kulvert | Водопропуск | Одводни канал |
| VTC | forgalomirányító központ | ċentru tat-traffiku tal-bastimenti | Verkeersleidingcentrum | Centrum ruchu statków | Centro de tráfego de embarcações | centru de management al traficului | centrum riadenia plavby | prometno središče za plovila | Alusliikennekeskus | Center för fartygstrafik | Центр управления движением судов | Центар за управљање саобраћајем |
| RES | gyűjtő medence | ġibjun | Spaarbekken | Zbiornik | Albufeira | lac de acumulare | vodná nádrž | akumulacijsko jezero | Patoallas | Vattenmagasin | Водохранилище | Акумулација |
| LKB | zsilip várakozóhely | baċir ta’ bieb tal-ilma magħluq | Sluiskolk | Komora śluzy | Bacia de eclusa | bazinul ecluzei | plavebná komora | splavnica | Sulkukammio | Slusskammare | Шлюзовая камера | Комора преводнице |
| BRO | hídnyílás | ftuħ ta’ pont | Brugopening | Otwieranie mostu | Ponte a abrir | pod în deschidere | mostný otvor | prehod mostu | Avattu silta | Broöppning | Разводной мост | Мостовски отвор |
| BNS | üzemanyagtöltő állomás | stazzjon tal-karburant | Bunker-/tankstation | Bunkierka / Stacja tankowania | Posto de abastecimento | bunker/stație alimentare combustibil | zásobovacia/tankovacia stanica | tank/polnilnica goriva | Tankkausasema | Bunkrings-/tankstation | бункеровка/заправочная станция | Терминал за снадбевање бродова горивом |

**ICE ACCESSIBILITY CODE**

| A | navigation normal | Нормално корабоплаване | Navegación normal | normální plavební provoz | Normal skibsfart | Schifffahrt normal | Tavapärane navigatsioon | Κανονική ναυσιπλοΐα | Navigation normale | Normalna plovidba | navigazione normale | Normāla kuģošana | Įprasta laivyba |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | navigation not yet hindered | Корабоплаването все още е възможно | Navegación posible | plavba je ještě možná | Skibsfarten hindres endnu ikke | Schifffahrt wird noch nicht behindert | Navigatsioon ei ole veel takistatud | Ναυσιπλοΐα που δεν παρεμποδίζεται ακόμη | Navigation possible | Plovidba još uvijek moguća | navigazione non ancora ostacolata | Kuģošana vēl nav traucēta | Nekliudoma laivyba |
| F | low traffic | Слабо корабоплаване | Tráfico escaso | slabý plavební provoz | Lav trafiktæthed | wenig Schifffahrt | Vähene liiklus | Χαμηλός ρυθμός κυκλοφορίας | Trafic faible | Slab promet | scarso traffico | Neliela satiksmes intensitāte | Neintensyvus eismas |
| L | no navigation without breaking | Корабоплаване само след ледоразбивач | Navegación imposible sin rompehielos | nelze plout bez lámání ledu | Ingen skibsfart uden isbryder | keine Schifffahrt ohne Eisbrecher | Vaid katkestustega liiklus võimalik | Καμία ναυσιπλοΐα χωρίς θραύση των πάγων | navigation seulement derrière brise-glace | Nema plovidbe bez lomljenja leda | nessuna navigazione senza rompighiaccio | Kuģošana tikai ar ledus laušanu | Laivyba įmanoma tik naudojant ledlaužį |
| C | navigation possible for motorvessels with more than 0,74 kW (1 hp) per 2 tons | Корабоплаването е възможно само за кораби с мощност над 0,5 к.с. на тон | Navegación posible para embarcaciones motorizadas con más de 0,74 Kw (1cv) por 2 toneladas | plavba možná pro motorové lodě s výkonem od 0,74 kW (l ks) na 2 tuny | Skibsfart er mulig for motorbåde med mere end 0,74 Kw (1 HK) pr. 2 tons | Schifffahrt möglich für Motorschiffe ab 0,74 kW (1 PS) pro 2 Tonnen | Mootorlaevade (suurema võimsusega kui 0,74 Kw (1hp)/2 t) navigatsioon võimalik | Ναυσιπλοΐα δυνατή για μηχανοκίνητα σκάφη ισχύος άνω των 0,74 Kw (1 hp) ανά 2 κόρους | La navigation est possible pour automoteurs de plus de 0,74 Kw (1 ch) par 2 tonnes | Plovidba dozvoljena za plovila s motorom snage veće od 0,74 KW(1 ks)/2t | transito possibile per motonavi con potenza superiore a 0,74 kW (1 hp) per 2 tonnellate | Kuģošana iespējama motorkuģiem, kuru jauda ir lielāka nekā 0,74 Kw (1 ZS) uz 2 tonnām | Laivyba leidžiama motorlaiviams, kurių galia yra didesnė nei 0,74 kW (1 hp) 2 tonoms |
| D | navigation possible for motorvessels with more than 0,74 kW (1 hp) per ton | Корабоплаването е възможно само за кораби с мощност над 1 к.с. на тон | Navegación posible para embarcaciones motorizadas con más de 0,74 Kw (1cv) por tonelada | plavba možná pro motorové lodě s výkonem od 0,74 kW (l ks) na tunu | Skibsfart er mulig for motorbåde med mere end 0,74 Kw (1 HK) pr. ton | Schifffahrt möglich für Motorschiffe ab 0,74 kW (1 PS) pro Tonne | Mootorlaevade (suurema võimsusega kui 0,74 Kw (1hp)/1 t) navigatsioon võimalik | Ναυσιπλοΐα δυνατή για μηχανοκίνητα σκάφη ισχύος άνω των 0,74 Kw (1 hp) ανά κόρο | La navigation est possible pour automoteurs de plus de 0,74 Kw (1 ch) par tonne | Plovidba dozvoljena za plovila s motorom snage veće od 0,74 KW(1 ks)/t | transito possibile per motonavi con potenza superiore a 0,74 kW (1 hp) per tonnellata | Kuģošana iespējama motorkuģiem, kuru jauda ir lielāka nekā 0,74 Kw (1 ZS) uz tonnu | Laivyba leidžiama motorlaiviams, kurių galia yra didesnė nei 0,74 kW (1 hp) tonai |
| E | navigation possibilities remain constant | Възможностите за корабоплаване не са променени | Posibilidades de navegación estables | setrvalé plavební podmínky | Ingen ændring af de nuværende sejlmuligheder | heutige Fahrmöglichkeiten bleiben gleich | Navigatioonivõimalused konstantsed | Οι δυνατότητες ναυσιπλοΐας παραμένουν σταθερές | Les possibilités de navigation sont constantes | Uvjeti plovidbe ostaju isti | condizioni di transito costanti | Kuģošanas iespējas nemainās | Nepakitusios laivybos sąlygos |
| G | navigation possibilities may deteriorate rapidly | Възможно е рязко влошаване на условията за корабоплаване | Posibilidades de navegación que pueden deteriorarse rápidamente | plavební podmínky se mohou náhle zhoršit | Sejlmulighederne kan hurtigt forværres | Fahrmöglichkeit kann sich schnell verschlechtern | Navigatsioonivõimalused võivad kiiresti halveneda | Οι δυνατότητες ναυσιπλοΐας μπορούν να επιδεινωθούν ταχέως | Les possibilités de navigation peuvent se détériorer rapidement | Uvjeti plovidbe mogu se naglo pogoršati | navigabilità che può peggiorare rapidamente | Kuģošanas iespējas var strauji pasliktināties | Laivybos sąlygos gali greitai pablogėti |
| H | no navigation but no obstruction | Корабоплаването е преустановено, но няма препятствия | Navegación imposible pero sin obstrucciones | přerušení plavby bez plavebních překážek | Ingen skibsfart, men ingen hindring | keine Schifffahrt, aber keine Schifffahrtssperre | Navigatsiooni ei toimu, aga takistust ei ole | Καμία ναυσιπλοΐα αλλά ούτε και παρεμπόδιση | Interruption de navigation même sans obstacle | Nema plovidbe, nema prepreka | nessun transito anche senza ostruzione | Kuģošana nenotiek, bet kuģošanas aizliegums nepastāv | Laivyba neleidžiama, tačiau kliūčių nėra |
| M | navigation possible with the aid of ice breakers | Корабоплаването е възможно само с ледорезни приспособления | Navegación posible con asistencia de rompehielos | plavba je možná s pomocí ledoborce | Skibsfart mulig med støtte fra isbrydere | Schifffahrt mit Eisbrecher möglich | Navigatsioon võimalik jäämurdjate abiga | Ναυσιπλοΐα δυνατή με τη βοήθεια παγοθραυστικών | La navigation est possible à l'aide d'un brise-glace | Plovidba moguća uz upotrebu ledolomca | transito possibile con l'intervento dei rompighiaccio | Kuģošana iespējama ar ledlaužu palīdzību | Laivyba galima naudojant ledlaužį |
| K | navigation possible in convoy or towage | Корабоплаването е възможно в състав или с буксир | Navegación posible en convoy o remolque | plavba je možná ve skupině plavidel za sebou nebo ve vlečné sestavě | Skibsfart mulig i konvoj eller på slæb | Fahren im Konvoi oder Schlepp möglich | Navigatsioon võimalik kolonnis või pukseerides | Ναυσιπλοΐα δυνατή σε νηοπομπές ή με ρυμούλκιση | La navigation est possible en convois ou avec remorqueur | Plovidba moguća u sastavu ili u teglju | navigazione possibile in convoglio o in traino | Kuģošana iespējama karavānā vai, velkot tauvā | Laivyba galima vilkstine arba su vilkiku |
| T | navigation possibilities may improve rapidly | Възможно е рязко подобряване на условията за корабоплаване | Posibilidades de navegación que pueden mejorar rápidamente | plavební podmíky se mohou náhle zlepšit | Sejlmulighederne kan hurtigt forbedres | Fahrmöglichkeit kann sich schnell verbessern | Navigatsioonivõimalused võivad kiiresti paraneda | Οι δυνατότητες ναυσιπλοΐας μπορούν να βελτιωθούν ταχέως | Les possibilités de navigation peuvent s'améliorer rapidement | Uvjeti plovidbe se mogu naglo poboljšati | navigabilità che può migliorare rapidamente | Kuģošanas iespējas var strauji uzlaboties | Laivybos sąlygos gali greitai pagerėti |
| P | inland ports can hardly be reached | Речните пристанища са трудно достъпни | Puertos interiores casi inaccesibles | vnitrozemské přístavy jsou těžko dosažitelné | Indlandshavne svært tilgængelige | Innenhäfen kaum erreichbar | Siseveesadamad raskesti ligipääsetavad | Δύσκολη προσέγγιση των εσωτερικών λιμένων | L'arrivée aux ports intérieurs est très difficile | Riječne luke teško dostupne | porti fluviali difficilmente raggiungibili | Piekļuve iekšzemes ostām apgrūtināta | Vidaus uostai sunkiai pasiekiami |
| V | no navigation allowed | Преустановено корабоплаване | Navegación prohibida | zákaz plavby | Sejlads ikke tilladt | Fahrverbot | Navigatsioon keelatud | Δεν επιτρέπεται η ναυσιπλοΐα | Navigation interrompue | Plovidba nije dopuštena | nessun transito consentito | Kuģošana aizliegta | Laivyba draudžiama |
| X | navigation in convoys compulsory | Плаването в състав е задължително | Obligatorio navegar en convoy | přikázaná plavba plavidel ve skupině za sebou | Sejlads i konvoj er påbudt | Konvoifahrt verpflichtend | Navigatsioon kolonnis kohustuslik | Υποχρεωτική ναυσιπλοΐα σε νηοπομπές | Navigation en convois obligatoire | Obvezna plovidba u sastavima | obbligo di navigazione in convoglio | Obligāta kugošana karavānā | Privaloma laivyba vilkstine |

**ICE ACCESSIBILITY CODE**

| A | normális/szokásos hajózás | navigazzjoni normali | Scheepvaart normaal | żegluga normalna | Navegação normal | navigație normală | normálna plavba | normalna plovba | normaali alusliikenne | Normal sjöfart | Нормальные условия для судоходства | Нормална пловидба |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | hajózás még nem korlátozott | navigazzjoni għadha mhux imfixkla | Scheepvaart ondervindt nog geen hinder | żegluga jeszcze bez przeszkód | Navegação possível | navigație posibilă | plavba ešte nie je obmedzená | plovba je še vedno možna | alusliikenteessä ei vielä esteitä | Ännu obehindrad sjöfart | судоходство допустимо | Пловидба још увек могућа |
| F | jelentéktelen hajóforgalom | ftit li xejn traffiku | Scheepvaart gering | niskie natężenie żeglugi | Tráfego ligeiro | trafic scăzut | slabá premávka | malo prometa | vähäinen alusliikenne | Låg sjötrafik | низкий судопоток | Слаб саобраћај |
| L | jégtörõ nélkül hajózási tilalom | ebda navigazzjoni projbita mingħajr tkissir | Geen vaart indien niet wordt gebroken | żegluga tylko w asyście lodołamacza | Navegação impossível sem quebra-gelos | nu se navighează fără dispozitiv de spargere a gheții | zákaz plavby bez ľadoborca | plovba brez ledolomilca ni dovoljena | ei alusliikennettä ilman jäänmurtamista | Ingen sjöfart utan isbrytning | плавание только под проводкой ледокольных средств | Нема пловидбе без ломљења леда |
| C | hajózás csak géphajóknak: minimum 0,74 kW 2 tonnánkként | navigazzjoni possibbli għal bastimenti b’mutur ta’ potenza ogħla minn 0,74 kW (1 hp) għal kull 2 tunnellati | Vaart mogelijk voor motorschepen vanaf 0,74 kW (1 pk) per 2 ton | żegluga dozwolona dla jednostek z napędem silnikowym o mocy powyżej 0,74 kW (1 KM) na każde 2 tony masy | Navegação possível a embarcações motorizadas com mais de 0,74 kW (1cv) por 2 toneladas | navigația este posibilă pentru automotoare cu mai mult de 0,74 Kw (1 CP) per 2 tone | plavba možná pre motorové plavidlá s výkonom viac ako 0,74 kW (1 hp) na 2 t | plovba mogoča za motorna plovila z močjo večjo od 0,74 kW (1 KM) na 2 toni | alusliikenne mahdollista moottorialuksille, joiden teho on yli 0,74 Kw (1 hp) 2 tonnia kohden | Sjöfart möjlig med motorfartyg över 0,74 kW(1hp) per 2 ton | навигация только для самоходных судов с удельной мощностью более 1 лошадиной силы на 2 тонны | Пловидба дозвољена за самохотке (пловила са сопственим погоном) са више од 0,74 kW (1KS) по 2t |
| D | hajózás csak géphajóknak: minimum 0,74 kW tonnánkként | navigazzjoni possibbli għal bastimenti b’mutur ta’ potenza ogħla 0,74 kW (1 hp) għal kull tunnellata | Vaart mogelijk voor motorschepen vanaf 0,74 kW (1 pk) per 1 ton | żegluga dozwolona dla jednostek z napędem silnikowym o mocy powyżej 0,74 kW (1 KM) na tonę masy | Navegação possível a embarcações motorizadas com mais de 0,74 kW (1cv) por tonelada | navigația este posibilă pentru automotoare cu mai mult de 0,74 Kw (1 CP) per tonã | plavba možná pre motorové plavidlá s výkonom viac ako 0,74 kW (1 hp) / t | plovba mogoča za motorna plovila z močjo večjo od 0,74 kW (1 KM) na tono | alusliikenne mahdollista moottorialuksille, joiden teho on yli 0,74 Kw (1 hp) tonnia kohden | Sjöfart möjlig med motorfartyg över 0,74 kW(1hp) per ton | навигация только для самоходных судов с удельной мощностью более 1 лошадиной силы на 1 тонну | Пловидба дозвољена за самохотке (пловила са сопственим погоном) са више од 0,74 kW (1KS) по 1t |
| E | hajózási feltételek állandósultak | il-possibbiltajiet ta’ navigazzjoni jibqgħu kostanti | Huidige vaarmogelijkheid blijft hetzelfde | warunki żeglugi bez zmian | Possibilidades de navegação estáveis | posibilitățile de navigație rămân constante | súčasné plavebné podmienky zostávajú rovnaké | možnost plovbe ostaja nespremenjena | alusliikennemahdollisuudet pysyvät ennallaan | Farbarhet förblir oförändrad | навигационные условия без изменений | Услови пловидбе остају исти |
| G | a hajózási lehetõségek gyorsan változhatnak | il-possibbiltajiet ta’ navigazzjoni jistgħu jiddeterjoraw rapidament | Vaarmogelijkheid kan snel verslechteren | możliwość gwałtownego pogorszenia warunków żeglugi | Possibilidades de navegação podem deteriorar-se rapidamente | posibilitățile de navigație se pot deteriora rapid | plavebné podmienky sa môžu rýchlo zhoršiť | možnost plovbe se lahko hitro poslabša | alusliikennemahdollisuudet voivat huonontua nopeasti | Farbarheten kan minska snabbt | возможно резкое ухудшение условий плавания | Услови пловидбе се могу нагло погоршати |
| H | hajózás akadálymentesség ellenére nincs | ebda navigazzjoni iżda ebda ostaklu | Geen vaart, maar niet gestremd | żegluga przerwana mimo braku zakazu żeglugi | Navegação impossível, mas não há obstruções | nu se navighează dar nu sunt obstrucții | zastavená plavba, bez plavebnej prekážky | plovba ni dovoljena, vendar ni ovir | ei alusliikennettä, vaikkei estettä | Ingen sjöfart, men ingen blockering | судоходства нет, но движение разрешено | Нема пловидбе, нема препрека |
| M | hajózás jégtörõvel lehetséges | navigazzjoni possibbli bit-tkissir tas-silġ | Scheepvaart met ijsbrekers mogelijk | możliwość żeglugi w asyście lodołamaczy | Navegação possível com a assistência de quebra-gelos | navigația este posibilă cu ajutorul spărgătoarelor de gheață | plavba možná s pomocou ľadoborca | plovba mogoča s pomočjo ledolomilca | alusliikenne mahdollista jäänmurtajien avulla | Sjöfart möjlig med hjälp av isbrytare | плавание под проводкой ледокольных средств разрешено | Пловидба могућа уз употребу ледоломца |
| K | hajózás kötelékben vagy vontatva lehetséges | navigazzjoni possibbli f’konvoj jew permezz ta’ rmonkar | Varen in konvooi of sleep mogelijk | możliwość żeglugi w konwojach lub za holownikiem | Navegação possível em comboio ou a reboque | navigația este posibilă în convoi sau remorcat | plavba možná v zostave alebo vo vleku | plovba mogoča v konvoju ali z vlečenjem | alusliikenne mahdollista kytkyeessä tai hinauksessa | Sjöfart möjlig i konvoj eller med bogsering | движение в составах или с буксирами | Пловидба могућа за потискиване или тегљене саставе |
| T | hajózási lehetõségek gyorsan javulhatnak | il-possibbiltajiet ta’ navigazzjoni jistgħu jitjiebu rapidament | Vaarmogelijkheid kan snel verbeteren | możliwość szybkiej poprawy warunków żeglugi | Possibilidades de navegação podem melhorar rapidamente | posibilitățile de navigație se pot ameliora rapid | plavebné podmienky sa môžu rýchlo zlepšiť | možnost plovbe se lahko hitro izboljša | alusliikennemahdollisuudet voivat parantua nopeasti | Farbarheten kan öka snabbt | возможно резкое улучшение условий плавания | Услови пловидбе се могу нагло побољшати |
| P | belvízi kikötõk alig elérhetõk | diffiċli jintlaħqu l-portijiet interni | Binnenhavens nauwelijks bereikbaar | ograniczone możliwości dotarcia do portów śródlądowych | Portos interiores quase inacessíveis | accesul în porturile interioare poate fi foarte dificil | vnútrozemské prístavy sú ťažko dosiahnuteľné | rečna pristanišča so težko dostopna | vaikea päästä sisävesisatamiin | Inlandshamnar mycket svåråtkomliga | доступ к внутренним портам сильно затруднён | Речне луке тешко доступне |
| V | hajózási tilalom | navigazzjoni projbita | Vaarverbod | zakaz żeglugi | Navegação proibida | navigația nu este permisă | zákaz plavby | plovba prepovedana | alusliikenne ei ole sallittua | Ingen sjöfart tillåten | навигация запрещена | Пловидба није дозвољена |
| X | hajózás csak kötelékben engedélyezett | in-navigazzjoni f’konvojs hija obbligatorja | Verplichte konvooivaart | obowiązek żeglugi w konwojach | Obrigatório navegar em comboio | navigația în convoaie este obligatorie | povinná plavba v zostave | obvezna plovba v konvojih | alusliikenne kytkyeissä pakollista | Obligatorisk konvojgång | движение только в составах | Обавезна пловидба у саставима |

**ICE CLASSIFICATION CODE**

| A | navigable | Свободно корабоплаване | Navegable | splavný | Uhindret sejlads | gut befahrbar | Navigeeritav | Πλεύσιμος | navigable | Plovno | navigabile | kuģojams | Laivyba be kliūčių |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | fairly navigable | Умерено корабоплаване | Razonablemente navegable | dobře splavný | Næsten uhindret sejlads | ziemlich gut befahrbar | Keskmiselt navigeeritav | Πλεύσιμος σε μικρό βαθμό | raisonnablement navigable | Pretežno plovno | abbastanza navigabile | diezgan labi kuģojams | Laivyba beveik be kliūčių |
| C | navigable with difficulty | Затруднено корабоплаване | Navegación difícil | obtížně splatný | Sejlads vanskelig | schwer befahrbar | Raskustega navigeeritav | Πλεύσιμος με δυσκολία | navigation pénible | Plovno uz teškoće | navigabile con difficoltà | grūti kuģojams | Sunki laivyba |
| D | navigable only with great difficulty | Силно затруднено корабоплаване | Navegación muy difícil | velmi obtížně splavný | Sejlads meget vanskelig | sehr Schwer befahrbar | Üksnes suurte raskustega navigeeritav | Πλεύσιμος μόνο με μεγάλη δυσκολία | navigation très pénible | Plovno uz velike teškoće | navigabile solo con grande difficoltà | ļoti grūti kuģojams | Laivyba labai sunki |
| E | no navigation allowed | Преустановено корабоплаване | Navegación prohibida | zákaz plavby | Sejlads ikke tilladt | Fahrverbot | Navigatsioon keelatud | Δεν επιτρέπεται καθόλου η ναυσιπλοΐα | navigation interrompue | Plovidba nije dopuštena | nessuna navigazione consentita | kuģošana aizliegta | Laivyba draudžiama |

**ICE CLASSIFICATION CODE**

| A | hajózható | navigabbli | Goed bevaarbaar | żeglowny | Navegável | navigabil | splavný | plovno | Kulkukelpoinen | Farbar | беспрепятственное судоходство | Пловно |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | teljes mértékben hajózható | pjuttost navigabbli | Vrij goed bevaarbaar | dość żeglowny | Razoavelmente navegável | navigabil în condiții acceptabile | pomerne dobre splavný | precej dobro plovno | melko kulkukelpoinen | Relativt farbar | достаточно беспрепятственное судоходство | Релативно пловно |
| C | nehezen hajózható | navigabbli b’xi diffikultajiet | Moeilijk bevaarbaar | żeglowny z trudnościami | Navegação difícil | navigabil cu dificultate | splavný s ťažkosťami | težko plovno | hankalasti kulkukelpoinen | Svårframkomlig | затруднённое судоходство | Пловно уз потешкоће |
| D | nagyon nehezen hajózható | navigabbli biss b’ħafna diffikultà | Zeer moeilijk bevaarbaar | żeglowny ale z dużymi trudnościami | Navegação muito difícil | navigabil numai cu mare dificultate | splavný len s veľkými ťažkosťami | zelo težko plovno | erittäin hankalasti kulkukelpoinen | Mycket svårframkomlig | сильно затруднённое судоходство | Пловно уз велике потешкоће |
| E | hajózási tilalom | navigazzjoni projbita | Vaarverbod | zakaz żeglugi | Navegação proibida | navigația nu este permisă | zákaz plavby | plovba prepovedana | alusliikenne ei ole sallittua | Ingen sjöfart tillåten | судоходство запрещено | Пловидба није дозвољена |

**ICE CONDITION CODE**

| A | — | clear water | Чиста вода | Aguas normales | volná voda | Isfrit farvand | offenes Wasser | selge vesi | Ύδατα άνευ πάγου | Eaux normales | Vodni put bez leda | acque normali | brīvs ūdens | Ledo nėra |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 0 — 4 cm | light spread floating ice | Разпръснат плаващ лед | Hielo flotante ligero disperso | ledová tříšť | Let spredt drivis | Treibeis | kergelt leviv triivjää | Ελαφρά διασκορπισμένα τεμάχια επιπλέοντος πάγου | glaces légères dispersées | Slabo formiran tanak plutajući led | leggero ghiaccio galleggiante sparso | izklaidu peldošs plāns ledus | Plonas pasklidęs plūduriuojantis ledas |
| C | 0 — 4 cm | light floating ice | Рядък плаващ лед | Hielo flotante ligero | slabá ledová tříšť | Let drivis | leichtes Treibeis | kerge triivjää | Ελαφρά τεμάχια επιπλέοντος πάγου | glaces légères flottantes | Tanak plutajući led | ghiaccio leggero galleggiante | plāns peldošs ledus | Plonas plūduriuojantis ledas |
| D | 0 — 4 cm | light solid ice | Слабо заледяване | Hielo sólido ligero | slabý led | Tynd fast is | leichtes Eis | kerge tahke jää | Ελαφρά τεμάχια συμπαγούς πάγου | glace légère | Tanak sloj leda | leggero ghiaccio solido | plāna ledus kārta | Plonas ištisinis ledas |
| E | 4 — 8 cm | medium spread floating ice to 40 % covered | Средно разреден плаващ лед (до 40 % покритие) | Hielo flotante disperso medio que cubre hasta un 40 % | středně silná rozpýlená ledová tříšť, pokrytí do 40 % | Middelsvær drivis op til 40 % dækket | mittelschweres zerstreutes Treibeis, bis 40 % eisbedeckt | keskmiselt leviv triivjää kuni 40 % kattuvusega | Μέσου πάχους διασκορπισμένα τεμάχια επιπλέοντος πάγου που καλύπτουν επιφάνεια 40 % | glaces moyennes dispersées couvrant 40 % | Srednje formiran plutajući led, pokrivenost do 40 % | ghiaccio sparso galleggiante di spessore medio con copertura fino al 40 % | vidēji biezs izklaidu peldošs ledus klāj līdz 40 % ūdens virsmas | Vidutinio storio pasklidęs plūduriuojantis ledas (dengia iki 40 % paviršiaus) |
| F | 4 — 8 cm | medium spread floating ice 40 to 75 % covered | Средно разреден плаващ лед (40 %-70 % покритие) | Hielo flotante disperso medio que cubre entre un 40 % y un 75 % | středně silně rozptýlená ledová tříšť, pokrytí od 40 % do 75 % | Middelsvær drivis 40-75 % dækket | mittelschweres zerstreutes Treibeis, 40 bis 75 % eisbedeckt | keskmiselt leviv triivjää kattuvusega 40 % kuni 75 % | Μέσου πάχους διασκορπισμένα τεμάχια επιπλέοντος πάγου που καλύπτουν επιφάνεια 40 % έως 75 % | glaces moyennes flottantes dispersées couvrant 40 à 75 % | Srednje formiran plutajući led, pokrivenost od 40 do 75 % | ghiaccio sparso galleggiante di spessore medio con copertura compresa tra 40 % e 75 % | vidēji biezs izklaidu peldošs ledus klāj 40 līdz 75 % ūdens virsmas | Vidutinio storio plūduriuojantis ledas (dengia 40–75 % paviršiaus) |
| G | 4 — 8 cm | medium floating ice more than 75 % in sludge or lead | Плаващ лед със средна дебелина покриващ над 75 % | Hielo flotante medio que cubre más del 75 % del canal | středně silně rozptýlená ledová tříšť, pokrytí vice než 75 % | Middelsvær drivis mere end 75 % dækket | mittelschweres Treibeis, mehr als 75 % der Rinne eisbedeckt | keskmiselt leviv triivjää, rohkem kui 75 % jääpankade või jäävallidena | Μέσου πάχους τεμάχια επιπλέοντος πάγου που καλύπτουν επιφάνεια άνω του 75 % του διαύλου | glaces moyennes flottantes dispersées couvrant plus de 75 % du chenal | Srednje formiran plutajući led, pokrivenost veća od 75 % | ghiaccio galleggiante di spessore medio costituito per più del 75 % da frammenti o canale ricoperto da frammenti | vidēji biezs peldošs ledus, vairāk nekā 75 % ūdens virsmas klāta vižņiem | Vidutinio storio plūduriuojantis ledas (daugiau kaip 75 % sudaro ižas) arba vandens tarpas tarp ledų |
| H | 4 — 8 cm | medium vast ice | Средно дебел твърд лед | Hielo compacto medio | středně silně pevný led | Middelsvær fast is | mittelschweres festes Eis | keskmine rüsijää | Μέσου πάχους εκτεταμένος πάγος | glace moyenne | Srednje velika santa leda | ghiaccio di spessore medio fisso | vidēji biezs blīvs ledus | Vidutinio storio ištisinis ledas |
| K | 8 — 12 cm | heavy spread floating ice to 40 % covered | Дебел плаващ лед (до 40 % покритие) | Hielo flotante pesado disperso que cubre hasta un 40 % | silná rozptýlená ledová tříšť, pokrytí do 40 % | Svær drivis op til 40 % dækket | schweres zerstreutes Treibeis, bis 40 % eisbedeckt | mitteleviv triivjää kuni 40 % kattuvusega | Βαρέα διασκορπισμένα τεμάχια επιπλέοντος πάγου σε έκταση 40 % | glaces lourdes flottantes dispersées couvrant jusqu'à 40 % | Dobro formiran plutajući led, pokrivenost do 40 % | ghiaccio spesso galleggiante con copertura fino al 40 % | biezs izklaidu peldošs ledus klāj līdz 40 % ūdens virsmas | Storas pasklidęs plūduriuojantis ledas (dengia iki 40 % paviršiaus) |
| L | 8 — 12 cm | heavy spread floating ice 40 to 75 % covered | Дебел плаващ лед (40 %-70 % покритие) | Hielo flotante pesado disperso que cubre entre un 40 % y un 75 % | silná rozptýlená ledová tříšť, pokrytí od 40 % do 75 % | Svær drivis 40-75 % dækket | schweres zerstreutes Treibeis, 40 bis 75 % eisbedeckt | mitteleviv triivjää kattuvusega 40 % kuni 75 % | Βαρέα διασκορπισμένα τεμάχια επιπλέοντος πάγου σε έκταση από 40 % έως 75 % | glaces lourdes flottantes dispersées couvrant 40 à 75 % | Dobro formiran plutajući led, pokrivenost od 40 do 75 % | ghiaccio spesso galleggiante con copertura compresa tra il 40 % e il 75 % | biezs izklaidu peldošs ledus klāj 40 līdz 75 % ūdens virsmas | Storas pasklidęs plūduriuojantis ledas (dengia 40–75 % paviršiaus) |
| M | 8 — 12 cm | heavy dense floating ice with more than 75 % chance on coagulation | Дебел плътен лед с вероятност за заледяване над 75 % | Hielo flotante pesado denso con más del 75 % de posibilidades de cuajar | těžká stlačená ledová tříšť s více než 75 % možnosti koagulace | Svær og pakket drivis mere end 75 % dækket; risiko for fastfrysning | schweres zusammengepferchtes Treibeis mit mehr als 75 %, Gefahr für Dammbildung | paks tihe triivjää jäätumusega rohkem kui 75 % | Βαρέα τεμάχια επιπλέοντος πάγου με πιθανότητες πήξης άνω του 75 % | glaces lourdes flottantes dispersées couvrant plus de 75 % et chance de coagulation | Debele sante leda, 75 % mogućnost zaleđivanja | ghiaccio spesso galleggiante con più del 75 % di probabilità di addensamento | ļoti blīvs peldošs ledus, sablīvējumu veidošanās iespēja — vairāk nekā 75 % | Storas tankus plūduriuojantis ledas, koaguliacijos tikimybė didesnė nei 75 % |
| P | 8 — 12 cm | heavy floating ice with more than 75 % in sludge or lead currently broken sludge | Дебел плътен лед покриващ над 75 % или току що разбит лед | Hielo flotante pesado que cubre más del 75 % del canal recientemente abierto | těžká ledová tříšť, pokrytí více než 75 %, plavební dráha dnes prolomena | Svær drivis mere end 75 % dækket; sejlrende er brudt for nylig | schweres Treibeis mehr als 75 % der Rinne eisbedeckt, Rinne heute gebrochen | paks triivjää rohkem kui 75 % jääpankadena või ajuti murduvate jäävallidena | Βαρέα τεμάχια προσφάτως θραυσθέντος επιπλέοντος πάγου σε επιφάνεια άνω του 75 % του διαύλου | glaces lourdes flottantes couvrant plus de 75 % du chenal, chenal brisé recemment | Debele sante leda, s više od 75 % leda u komadu ili trenutno polomljenih komada | ghiaccio spesso galleggiante costituito per più del 75 % da frammenti o canale attualmente coperto da ghiaccio frammentato | biezs peldošs ledus ar vairāk nekā 75 % vižņu, kuri nesen salūzuši | Storas plūduriuojantis ledas (daugiau kaip 75 % sudaro ižas) arba šiuo metu tarp ledų pralaužtas vandens tarpas |
| R | 8 — 12 cm | heavy vast ice | Дебел твърд лед | Hielo compacto pesado | těžký pevný led | Svær fast is | schweres festes Eis | paks rüsijää | Βαρέα τεμάχια εκτεταμένου πάγου | glace solide épaisse | Teška velika santa leda | ghiaccio spesso ed esteso | biezs blīvs ledus | Storas ištisinis ledas |
| S | \> 12 cm | very heavy floating ice en solid ice nearly 100 % covered | Много дебел плаващ твърд лед покриващ почти 100 % | Hielo flotante muy pesado y sólido que cubre casi el 100 % | velmi těžká ledová tříšť a ledové kry, téměř 100 % pokryto ledem | Meget svær drivis og fast is næsten 100 % dækket | sehr schweres Treibeis und Packeis, fast 100 % eisbedeckt | väga paks triivjää tahke jääna peaagu 100 % kattuvusega | Πολύ βαρέα τεμάχια συμπαγούς επιπλέοντος πάγου σε έκταση σχεδόν 100 % | glaces flottantes trés lourdes et banquise couvrant presque 100 % | Vrlo debele sante i tvrdi led sa skoro 100 % pokrivenosti | ghiaccio galleggiante molto spesso e solido con copertura quasi del 100 % | ļoti biezs peldošs ledus un ledus kārta klāj gandrīz 100 % ūdens virsmas | Labai storas plūduriuojantis ledas ir ištisinis ledas dengia beveik 100 % paviršiaus |
| U | \> 40 cm | ice dam or drifting ice | Ледени прегради или струпвания | Barrera de hielo o hielo a la deriva | ledová bariéra nebo nahromadění ledu | Isdæmning eller isspærring | Eisdamm oder Eisstau | rüsijäävallid või rüsijää | Φράγμα πάγου ή παρασυρόμενος πάγος | barrage de glace ou débâcle | Ledena prepreka ili plutajući led | barriera di ghiaccio o ghiaccio alla deriva | ledus aizsprosts vai dreifējošs ledus | Ledo lyčių sangrūda arba dreifuojantis ledas |
| O | — | disappearing (pap)ice, no longer obstructing | Топящ се лед, няма препятствия | Hielo a punto de fundirse que ya no constituye un obstáculo | tenký měkký led, který již nepřekáží | Smelteis, ingen hindring længere | Pappeis, nicht länger behinderlich | kaduv jää, enam mitte takistav | Εξαφανιζόμενος πάγος που δεν προκαλεί πλέον εμπόδια | glaces fondantes, aucune gêne | Otapanje leda, nema prepreka | ghiaccio in fase di scioglimento, nessuna ostruzione | izzūdošs ledus, vairs nekavē kuģošanu | Tirpstantis, laivybai kliūčių nesudarantis ledas |
| V | — | navigation interrupted | Корабоплаването е преустановено | Navegación interrumpida | zákaz plavby | Skibsfarten er indstillet | Fahrverbot | navigeerimine katkestatud | Διακοπή ναυσιπλοΐας | navigation interrompue | Zabrana plovidbe | navigazione interrotta | kuģošana pārtraukta | Laivyba nutraukta |

**ICE CONDITION CODE**

| A | — | jégmentes víz | ilma nadif | Open water | woda otwarta | Água livre | fără gheață | voľná voda | brez ledu | avovesi | Öppet vatten | чистая вода | Водни пут без леда |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 0 — 4 cm | vékony szórványos jégtáblák | ftit silġ mifrux f’wiċċ l-ilma | Licht verspreid drijfijs | rozproszona, cienka kra lodowa | Gelo flutuante ligeiro disperso | gheață subțire plutitoare dispersată | ľadová triešť | plavajoči led | ohutta rikkonaista ajojäätä | Lätt spridd drivis | малоразреженный плавучий лёд | Слабо формиран танки плутајући лед |
| C | 0 — 4 cm | vékony jégtáblák | ftit silġ f’wiċċ l-ilma | Licht drijfijs | cienka kra lodowa | Gelo flutuante ligeiro | gheață subțire plutitoare | slabá ľadová triešť | tanek plavajoči led | ohutta ajojäätä | Lätt drivis | редкий плавучий лёд | Танак плутајући лед |
| D | 0 — 4 cm | könnyû beállt jég | ftit silġ solidu | Licht vast ijs | cienka pokrywa lodowa | Gelo compacto ligeiro | gheață subțire | slabý ľad | tanek trdni led | ohutta kiintojäätä | Lätt fastis | малосплочённый лёд | Танак слој леда |
| E | 4 — 8 cm | közepes szórványos jégtáblák 40 %-ig jégfedettségig | ammont medju ta’ silġ mifrux f’wiċċ l-ilma sa kopertura ta’ 40 % | Middelzwaar verspreid drijfijs tot 40 % bedekt | rozproszona kra lodowa średniej grubości, pokrycie do 40 % | Gelo flutuante médio disperso, cobrindo até 40 % | gheață mijlocie plutitoare dispersată acoperind 40 % | stredne silná rozptýlená ľadová triešť, pokrytie do 40 % | srednje debel plavajoči led, pokritost do 40 % | keskiraskasta rikkonaista ajojäätä, enintään peittävyys 40 % | Medelstor spridd drivis, 40 % istäcke | плавучий лёд средней разреженности (до 40 %) | Средње формиран плутајући лед, покривеност до 40 % |
| F | 4 — 8 cm | közepes szórványos jégtáblák 40 %-70 % közötti jégfedettséggel | ammont medju ta’ silġ mifrux f’wiċċ l-ilma b’kopertura ta’ bejn 40 % u 75 % | Middelzwaar verspreid drijfijs 40 tot 75 % bedekt | rozproszona kra lodowa średniej grubości, pokrycie 40 do 75 % | Gelo flutuante médio disperso, cobrindo 40 % a 75 % | gheață mijlocie plutitoare dispersată acoperind 40 % până la 75 % | stredne silná rozptýlená ľadová triešť, pokrytie od 40 % do 75 % | srednje debel plavajoči led, pokritost od 40 do 75 % | keskiraskasta rikkonaista ajojäätä, peittävyys 40–75 % | Medelstor spridd drivis, 40-75 % istäcke | плавучий лёд средней разреженности (40 % — 70 %) | Средње формиран плутајући лед, покривеност 40 do 75 % |
| G | 4 — 8 cm | közepes jégtáblák több mint 75 %-ban kásajégként vagy jégmentes sávokban | ammont medju ta’ silġ f’wiċċ l-ilma b’aktar minn 75 % minnu ħama jew ftuħ fis-silġ | Middelzwaar drijfijs met meer dan 75 % in geul of slop | kra lodowa średniej grubości, pokrycie powyżej 75 % kanału | Gelo flutuante médio, cobrindo mais de 75 % da esteira | gheață mijlocie plutitoare dispersată acoperind peste 75 % din șenal | stredne silná rozptýlená ľadová triešť, pokrytie viac ako 75 % | srednje debel plavajoči led, pokritost večja od 75 % | keskiraskasta ajojäätä, peittävyys yli 40–75 % väylästä | Medelstor spridd drivis, över 75 % av farrännan istäckt | плавучий лёд средней разреженности (больше 75 % ледового канала покрыто ледяной кашей) | Средње формиран плутајући лед, покривеност већа од 75 % |
| H | 4 — 8 cm | közepes beállt jég | silġ vast medju | Middelzwaar vast ijs | pokrywa lodowa średniej grubości | Gelo compacto médio | gheață mijlocie | stredne pevný ľad | srednje debel trdni led | keskiraskasta jäätä | Medeltjock fastis | лёд средней сплочённости | Средње велика санта леда |
| K | 8 — 12 cm | vastag szórványos jégtáblák 40 %-os jégfedettségig | ħafna silġ mifrux f’wiċċ l-ilma sa kopertura ta’ 40 % | Zwaar verspreid drijfijs tot 40 % bedekt | rozproszona, gruba kra lodowa, pokrycie do 40 % | Gelo flutuante pesado disperso, cobrindo até 40 % | gheață groasă plutitoare dispersată acoperind până la 40 % | silná a rozptýlená ľadová triešť, pokrytie do 40 % | debel plavajoči led, pokritost do 40 % | raskasta rikkonaista ajojäätä, peittävyys enintään 40 % | Tjock, spridd drivis, upp till 40 % istäcke | тяжелый разреженный плавучий лёд (до 40 %) | Добро формиран плутајући лед, покривенотс до 40 % |
| L | 8 — 12 cm | vastag jégtáblák 40 %-70 % közötti jégfedettséggel | ħafna silġ mifrux f’wiċċ l-ilma b’kopertura ta’ bejn 40 % u 75 % | Zwaar verspreid drijfijs 40 tot 75 % bedekt | rozproszona, gruba kra lodowa, pokrycie 40 do 75 % | Gelo flutuante pesado disperso, cobrindo 40 % a 75 % | gheață groasă plutitoare dispersată acoperind 40 % până la 75 % | silná a rozptýlená ľadová triešť, pokrytie od 40 % do 75 % | debel plavajoči led, pokritost od 40 do 75 % | raskasta rikkonaista ajojäätä, peittävyys 40–75 % | Tjock, spridd drivis, 40-75 % istäcke | тяжелый разреженный плавучий лёд (40 % — 75 %) | Добро формиран плутајући лед, покривеност 40 do 75 % |
| M | 8 — 12 cm | vastag jégtáblák több mint 75 %-os, torlaszképződés veszély | ħafna silġ dens f’wiċċ l-ilma b’ċans ta’ aktar minn75 % li jagħqad | Zwaar opeengepakt drijfijs met meer dan 75 % kans op propvorming | gęsta, gruba kra lodowa, pokrycie powyżej 75 %, możliwość koagulacji | Gelo flutuante pesado denso, com probabilidade de concreção superior a 75 % | gheață groasă plutitoare dispersată acoperind mai mult de 75 % și șanse de îngheț | hustá ľadová triešť s viac ako 75 % možnosťou koagulácie | debel plavajoči led, pokritost večja od 75 %, možnost sesedanja | raskasta tiheää ajojäätä, peittävyys yli 75 %, hyytymisvaara | Tätt sammanpackad drivis, över 75 % risk för stampisvall | очень сплочённый лёд, более 75 %-ая вероятность образования заторов | Плутајући лед велике густине, са 75 % шансе за коагулацију |
| P | 8 — 12 cm | vastag jégtáblák több mint 75 %-os fedettség, ma tört hajózócsatornával | ħafna silġ f’wiċċ l-ilma b’aktar minn 75 % minnu ħama jew ftuħ fis-silġ magħmul minn ħama attwalment imkissra | Zwaar drijfijs met meer dan 75 % in geul of slop, heden gebroken geul | gruba kra lodowa, pokrycie powyżej 75 % kanału, świeżo przełamany kanał | Gelo flutuante pesado cobrindo mais de 75 % da esteira, passagem aberta recentemente | gheață groasă plutitoare dispersată acoperind peste 75 % din șenal, șenal spart recent | silná a rozptýlená ľadová triešť, pokrytie viac ako 75 % plavebnej dráhy, dnes rozbitá ryha | debel plavajoči led, pokritost večja od 75 %, trenutno razbit | raskasta ajojäätä, peittävyys yli 75 % väylästä, joka on äskettäin murrettu | Tjock drivis, över 75 % av farrännan täckt, rännan bruten i dag | тяжелый плавучий лёд, более 75 %, в настоящий момент судоходство затруднено из-за ледяной каши в ледовом канале | Тешки плутајући лед са више од 75 % леда у комаду или тренутно поломљених комада |
| R | 8 — 12 cm | vastag beállt jég | silġ vast qawwi | Zwaar vast ijs | gruba pokrywa lodowa | Gelo compacto pesado | gheață groasă solidă | silne pevný ľad | debel trdni led | raskasta jäätä | Tjock fastis | очень сплочённый лёд | Тешка велика санта леда |
| S | \> 12 cm | nagyon vastag úszó és parti jég közel 100 %-os jégfedettséggel | silġ qawwi ħafna f’wiċċ l-ilma u silġ solidu b’kopertura ta’ kważi 100 % | Zeer zwaar drijfijs en pakijs bijna 100 % bedekt | bardzo gruba kra lodowa i pokrywa lodowa, pokrycie niemal 100 % | Gelo flutuante e gelo compacto ultrapesados, cobrindo quase 100 % | banchize plutitoare groase acoperind aproape 100 % | veľmi pevná ľadová triešť a ľadovce, pokrytie takmer 100 % | zelo debel plavajoči led in trdni led, pokritost skoraj 100 % | erittäin raskasta ajojäätä ja kiintojäätä, peittävyys lähes 100 % | Mycket tjock drivis och fastis med nästan 100 % istäcke | очень тяжёлый плавучий и сплошной лёд (почти 100 %) | Веома тежак плутајући лед са чврстим ледом, покривеност скоро 100 % |
| U | \> 40 cm | jégtorlasz vagy sodródó jég | diga tas-silġ jew silġ jinġarr mal-kurrent | IJsdam of kruiend ijs | bariera lodowa lub zator lodowy | Barreira de gelo ou gelo à deriva | pod de gheață sau gheață plutitoare | ľadová bariéra alebo nahromadenie ľadu | ledena ovira ali naplavine | jääpato tai ajojäätä | Stampisvall eller drivis | ледяной затор или скопление дрейфующего льда | Ледена преграда или лед у покрету |
| O | — | elolvadó (kásás) jég, akadályozás megszűnt | silġ (artab) li qed jinħall u li ma għadux jostakola | Verdwijnend (pap)ijs, niet meer hinderlijk | zanikający lód (papka), nie przeszkadzający w żegludze | Gelo em fusão, já não causa obstrução | ghețari topiți, nici unul periculos | strácajúci sa tenký ľad, žiadne prekážky | taljenje ledu, brez ovir | sulavaa jäätä, ei enää esteenä | Upplöst issörja, ingen blockering | разрушающийся лёд с проталинами, беспрепятственное судоходство | Отапање леда, нема препрека |
| V | — | hajózási szünetel | navigazzjoni interrotta | Scheepvaart onderbroken | zakaz żeglugi | Navegação suspensa | navigație întreruptă | zákaz plavby | prepoved plovbe | alusliikenne keskeytetty | Sjöfart förbjuden | судоходство остановлено | Забрана пловидбе |

**ICE SITUATION CODE**

| NOL | no limitation | Без ограничение | Sin limitación | bez omezení | Ingen begrænsninger | keine Behinderung | piirangut ei ole | Κανένας περιορισμός | pas de limitation | Nema ograničenja | nessuna limitazione | bez ierobežojumiem | Apribojimų nėra |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LIM | limitation | Ограничение | Limitación | omezení | Begrænset | Behinderung | piirang | Περιορισμός | limitation | Ograničenje | limitazione | ierobežojums | Apribojimai |
| NON | no navigation allowed | Преустановено корабоплаване | Navegación prohibida | zákaz plavby | Sejlads ikke tilladt | gesperrt | navigatsioon keelatud | Δεν επιτρέπεται καμία ναυσιπλοΐα | navigation interdite | Plovidba nije dopuštena | nessuna navigazione consentita | kuģošana aizliegta | Laivyba draudžiama |

**ICE SITUATION CODE**

| NOL | nincs korlátozás | ebda restrizzjoni | Geen beperking | brak ograniczeń | Sem restrições | fără restricții | bez obmedzenia | brez omejitve | ei rajoitusta | Ingen begränsning | без ограничений | Без ограничења |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LIM | korlátozás | restrizzjoni | Beperking | ograniczenie | Restrições | cu restricții | obmedzenie | omejitev | rajoitus | Begränsad trafk | ограниченно | Ограничење |
| NON | hajózás nem megengedett | navigazzjoni projbita | Vaarverbod | zakaz żeglugi | Navegação proibida | navigația nu este permisă | zákaz plavby | plovba prepovedana | alusliikenne ei ole sallittua | Ingen sjöfart tillåten | навигация запрещена | Пловидба није дозвољена |

**WEATHER CLASS CODE**

| CLR | clear | Ясно | Despejado | jasno | Klart | klar | selge | Αίθριος καιρός | clair | Vedro | sereno | skaidrs | giedra |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CLDY | cloudy | Облачно | Nublado | oblačno | Skyet | bewölkt | pilvitus | Νεφώσεις | nuageux | Oblačno | nuvoloso | mākoņains | debesuota |
| OCST | overcast | Заоблачено | Cubierto | zataženo | Overskyet | bedeckt | lauspilvitus | Πλήρως νεφοσκεπής ουρανός | couvert | Jača naoblaka | coperto | apmācies | apsiniaukę |
| DZZL | drizzle | Ръмеж | Llovizna | mrholení | Støvregn | Nieselregen | uduvihm | Ψεκάδες βροχής | bruine | Rosa | pioviggine | smalks lietus | dulksna |
| RAIN | rain | Дъжд | Lluvia | déšť | Regn | Regen | vihm | Βροχή | pluie | Kiša | pioggia | lietus | lietus |
| LRAIN | light rain | Лек дъжд | Lluvia ligera | slabý déšť | Let regn | leichter Regen | kerge vihm | Ασθενής βροχή | légère pluie | Slaba kiša | pioggia debole | viegls lietus | silpnas lietus |
| ORAIN | occasional rain | Откъслечни превалявания | Lluvia ocasional | občasný déšť | Lejlighedsvis regn | gelegentlich Regen | hoovihm | Σποραδική βροχή | pluie intermittente | Povremena kiša | piogge occasionali | neregulārs lietus | nepastovus lietus |
| HRAIN | heavy rain | Силен дъжд | Lluvia intensa | silný déšť | Kraftig regn | schwerer Regen | paduvihm | Έντονη βροχόπτωση | forte pluie | Jaka kiša | forti piogge | spēcīgs lietus | smarkus lietus |
| SLEET | sleet | Лапавица | Aguanieve | déšť se sněhem | Tøsne | Graupel | lörts | Χιονόνερο | neige fondue | Susnježica | nevischio | slapjdraņķis | šlapdriba |
| SNOW | snow | Сняг | Nieve | sněžení | Sne | Schneefall | lumi | Χιόνι | neige | Snježne oborine | neve | sniegs | snygis |
| SNFALL | heavy snow fall | Силен снеговалеж | Nieve intensa | silné sněžení | Kraftigt snefald | schwerer Schneefall | tugev lumesadu | Έντονη χιονόπτωση | neige dense | Jake snježne oborine | pesanti nevicate | spēcīgs sniegs | stiprus snygis |
| HAIL | hail | Град | Granizo | krupobití | Hagl | Hagel | rahe | Χαλάζι | grêle | Tuča | grandine | krusa | kruša |
| SHWRS | showers | Преваляване | Chubasco | přeháňky | Byer | Schauer | sajuhood | Όμβρος | averses | Pljusak | rovesci | lietusgāzes | liūtys |
| THSTRM | thunderstorm | Гръмотевична буря | Tormenta eléctrica | bouřka | Tordenvejr | Gewitter | äike | Καταιγίδα | orage | Olujno nevrijeme | temporale | pērkona negaiss | perkūnija |
| HAZY | hazy | Замъглено | Bruma | zamlženo | Diset | diesig | somp | Υγρή αχλύς | brume | Maglovito | cielo velato | dūmaka | migla |
| FOG | fog | Мъгла | Niebla | mlha | Tåge | Nebel | udu | Ομίχλη | brouillard | Magla | nebbia | migla | rūkas |
| FOGPAT | fog patches | Мъгливи участъци | Zonas de niebla | lokální mlha | Pletvis tåge | Nebelbänke | udulaigud | Ομίχλη κατά τόπους | bancs de brouillard | Mjestimična magla | banchi di nebbia | miglas joslas | vietomis rūkas |
| GALE | gale | Силен вятър | Temporal | vichřice | Hård kuling | stürmischer Wind | raju | Θυελλώδης άνεμος | grand vent | Udari vjetra | burrasca | vētrains | audra |
| STRM | storm | Буря | Tormenta | bouře | Storm | Sturm | torm | Θύελλα | tempête | Oluja | tempesta | stipra vētra | štormas |
| HURRC | hurricane | Ураган | Huracán | hurikán | Orkan | Orkan | orkaan | Κυκλώνας | ouragan | Orkan | uragano | orkāns | uraganas |
| FZRA | freezing rain (black ice) | Суграшица | Lluvia escarchada (hielo glaseado) | mrznoucí déšť | Isslag | gefrierender Regen | allajahtunud vihm (must jää) | Βροχή με παγοκρυστάλλους (υαλόπαγος) | pluie verglaçante | Ledena kiša | vetrone | atkala (melnais ledus) | lijundra (apšalas) |

**WEATHER CLASS CODE**

| CLR | tiszta | ċar | Helder | bezchmurnie | Céu limpo | senin | bezoblačno (jasno) | jasno | selkeää | Klart | ясно | Ведро |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CLDY | felhős | imsaħħab | Bewolkt | pochmurnie | Céu nublado | noros | oblačno | pretežno oblačno | enimmäkseen pilvistä | Molnigt | облачно | Облачно |
| OCST | borult | mgħajjeb bis-sħab | Betrokken | zachmurzenie | Céu encoberto | acoperit | zamračené | oblačno | pilvistä | Mulet | пасмурно | Наоблачење |
| DZZL | szitáló eső | irxiex | Motregen | mżawka | Chuvisco | burniță | mrholenie | pršenje | tihkusadetta | Duggregn | изморозь | Роса |
| RAIN | eső | xita | Regen | deszcz | Chuva | ploaie | dážď | dež | sadetta | Regn | дождь | Киша |
| LRAIN | gyenge eső | xita ħafifa | Lichte regen | lekki deszcz | Chuva fraca | ploaie ușoară | slabý dážď | rahel dež | heikkoa vesisadetta | Lätt regn | слабый дождь | Слаба киша |
| ORAIN | szórványos eső | kultant xita | Verspreide regen | sporadyczny deszcz | Chuvas ocasionais | ploaie ocazională | občasný dážď | občasen dež | ajoittaista vesisadetta | Tidvis regn | возможен дождь | Повремена киша |
| HRAIN | heves eső | xita qalila | Zware regenval | ulewa | Chuva forte | averse de ploaie | silný dážď | močan dež | voimakasta vesisadetta | Kraftigt regn | сильный дождь | Јака киша |
| SLEET | hódara | taħlita ta’ xita u silġ | Natte sneeuw | deszcz ze śniegiem | Neve molhada | lapoviță | dážď so snehom | leden dež | räntäsadetta | Snöblandat regn | дождь со снегом | Суснежица |
| SNOW | hó | borra | Sneeuw | śnieg | Neve | ninsoare | sneh (sneženie) | sneg | lumisadetta | Snö | снег | Снег |
| SNFALL | erős hóesés | borra qalila | Zware sneeuwval | intensywny opad śniegu | Forte nevão | averse de ninsoare | silné sneženie | močno sneženje | runsasta lumisadetta | Kraftigt snöfall | сильный снегопад | Јаке снежне падавине |
| HAIL | jégeső | xita balal | Hagel | grad | Granizo | grindină | krupobitie | toča | rakeita | Hagel | град | Град |
| SHWRS | zápor | ħalbiet tax-xita | Buien | przelotny opad śniegu | Aguaceiros | averse | prehánky | plohe | sadekuuroja | Regnskurar | ливни | Пљусак |
| THSTRM | zivatar | maltempata bir-ragħad | Onweer | burza (z piorunami) | Trovoada | vijelie | silná búrka | nevihta | raju ukonilma | Åskväder | гроза | Олујно невреме |
| HAZY | párás | imċajpar | Nevelig | mglisto | Bruma | negură | hmlisto | megličasto | auerta | Disigt | дымка | Магловито |
| FOG | köd | ċpar | Mist | mgła | Nevoeiro | ceață | hmla | megla | sumua | Dimma | туман | Магла |
| FOGPAT | ködfoltok | irqajja’ mċajprin | Mistbanken | lokalne zamglenie | Banco de nevoeiro | ceață în valuri | občasná hmla | zaplate megle | paikoitellen sumua | Dimbankar | туман местами | Местимична магла |
| GALE | viharos szél | burraxka | Harde wind | wichura | Vento muito forte | vânt puternic | víchrica | viharni veter | kovaa tuulta | Hård vind | штормовой ветер | Јак ветар |
| STRM | vihar | maltempata | Storm | burza | Tempestade | furtună | búrka | močan vihar | myrskyä | Storm | шторм | Олуја |
| HURRC | orkán | uragan | Orkaan | huragan | Furacão | tornadă | hurikán | orkan | hirmumyrskyä | Orkan | ураган | Оркан |
| FZRA | fagyos eső | xita ffriżata (“black ice”) | IJsregen (zwart ijs) | marznący deszcz | Chuva gelada (geada transparente) | polei | mrznúci dážď | žled (poledica) | jäätävää sadetta (mustaa jäätä) | Underkylt regn | гололед | Ледена киша |

**WEATHER ITEM CODE**

| WI | wind | Вятър | Viento | vítr | Vind | Wind | tuul | Άνεμος | vent | Vjetar | vento | vējš | vėjas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WA | waves | Вълнение | Oleaje | vlny | Bølger | Wellen | lained | Κύματα | remous | Valovi | moto ondoso | viļņi | bangos |
| FG | visibility | Видимост | Visibilidad | dohlednost | Sigtbarhed | Sicht | nähtavus | Ορατότητα | visibilité | Vidljivost | visibilità | redzamība | matomumas |
| RN | rain | Дъжд | Lluvia | déšť | Regn | Regen | vihm | Βροχή | pluie | Kiša | pioggia | lietus | lietus |
| SN | snow | Сняг | Nieve | sníh (sněžení) | Sne | Schnee | lumi | Χιόνι | neige | Snijeg | neve | sniegs | snygis |
| AT | air temperature | Температура на въздуха | Temperatura del aire | teplota vzduchu | Lufttemperatur | Lufttemperatur | õhutemperatuur | Θερμοκρασία αέρα | température de l'air | Temperatura zraka | temperatura dell'aria | gaisa temperatūra | oro temperatūra |
| WT | water temperature | Температура на водата | Temperatura del agua | teplota vody | Vandtemperatur | Wassertemperatur | veetemperatuur | Θερμοκρασία νερού | température de l'eau | Temperatura vode | temperatura dell'acqua | ūdens temperatūra | vandens temperatūra |

**WEATHER ITEM CODE**

| WI | szél | riħ | Wind | wiatr | Vento | vânt | vietor | veter | tuuli | Vind | ветер | Ветар |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WA | hullámok | mewġ | Golven | fale | Ondas | valuri | vlny | valovi | aallokko | Vågor | высота волн | Таласи |
| FG | látótávolság | viżibbiltà | Zicht | mgła | Visibilidade | vizibilitate | viditeľnosť | vidljivost | näkyvyys | Sikt | видимость | видљивост |
| RN | eső | xita | Regen | deszcz | Chuva | ploaie | dážď | dež | sade | Regn | дождь | Киша |
| SN | hó | borra | Sneeuw | śnieg | Neve | zăpadă | sneženie | sneg | lumi | Snö | снег | Снег |
| AT | léghőmérséklet | temperatura tal-arja | Luchttemperatuur | temperatura powietrza | Temperatura do ar | temperatura aerului | teplota vzduchu | temperatura zraka | ilman lämpötila | Lufttemperatur | температура воздуха | Температура ваздуха |
| WT | vízhőmérséklet | temperatura tal-ilma | Watertemperatuur | temperatura wody | Temperatura da água | temperatura apei | teplota vody | temperatura vode | veden lämpötila | Vattentemperatur | температура воды | Температура воде |

**WEATHER CATEGORY CODE**

| 0 | calm | безветрие | Calma | bezvětří | Roligt | Windstille | tuulevaikus | Νηνεμία | calme | Mirno | calma | bezvējš | štilis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | light air | тих вятър | Ventolina | vánek | Let vind | leichter Zug | vaikne tuul | Ασθενής άνεμος | courant d'air | Lahor | bava di vento | vēja vēsma | tylus vėjelis |
| 2 | light breeze | лек ветрец | Brisa muy débil | slabý vítr | Let brise | leichte Briese | kerge tuul | Ελαφρά αύρα | brise légère | Povjetarac | brezza leggera | viegls vējš | lengvas vėjas |
| 3 | gentle breeze | лек вятър | Brisa débil | mírný vítr | Blid brise | schwache Briese | nõrk tuul | Ασθενής αύρα | brise douce | Slab vjetar | brezza | lēns vējš | silpnas vėjas |
| 4 | moderate breeze | умерен вятър | Brisa moderada | dosti čerstvý vítr | Moderat brise | mäßige Briese | mõõdukas tuul | Μέτρια αύρα | brise modérée | Umjeren vjetar | brezza vivace | mērens vējš | vidutinis vėjas |
| 5 | fresh breeze | разхлаждащ вятър | Brisa fresca | čerstvý vítr | Frisk brise | frische Briese | kaunis tugev tuul | Δροσερή αύρα | brise fraîche | Umjereno jak vjetar | brezza tesa | mēreni stiprs vējš | gaivus vėjas |
| 6 | strong breeze | силен вятър | Brisa fuerte | silný vítr | Kraftig brise | starker Wind | tugev tuul | Ισχυρή αύρα | vent fort | Jak vjetar | vento fresco | stiprs vējš | stiprus vėjas |
| 7 | near gale | доста силен вятър | Viento fuerte | mírný vichr (prudký vítr) | Tæt på hård kuling | steifer Wind | vali tuul | Σχεδόν θυελλώδης άνεμος | tempête modérée | Snažan vjetar | vento forte | ļoti stiprs vējš | beveik audra |
| 8 | gale | много силен вятър | Temporal | bouřlivý vítr | Hård kuling | stürmischer Wind | väga vali tuul | Θυελλώδης άνεμος | tempête fraîche | Olujni vjetar | burrasca moderata | vētrains | audra |
| 9 | strong gale | силен вихър | Gran temporal | vichřice | Hård kuling | Sturm | rajutuul | Ισχυρός θυελλώδης άνεμος | tempête forte | Jak olujni vjetar | burrasca forte | vētra | stipri audra |
| 10 | storm | много силен вихър | Tormenta | silná vichřice | Storm | schwerer Sturm | torm | Θύελλα | tempête | Orkanski vjetar | tempesta | stipra vētra | štormas |
| 11 | violent storm | стихийна буря | Borrasca | mohutná vichřice | Meget kraftig storm | orkanartiger Sturm | tugev torm | Σφοδρή θύελλα | orage | Jak orkanski vjetar | fortunale | ļoti stipra vētra | stiprus štormas |
| 12 | hurricane | ураган | Huracán | orkán | Orkan | Orkan | orkaan | Κυκλώνας | ouragan | Orkan | uragano | orkāns | uraganas |
| 13 | thick fog | много гъста мъгла | Niebla espesa | velmi hustá mlha | Tyk tåge | dichter Nebel | tihe udu | Πυκνή ομίχλη | brouillard épais | Izrazito gusta magla | nebbia fitta | spēcīga migla | tirštas rūkas |
| 14 | dense fog | гъста мъгла | Niebla densa | hustá mlha | Tæt tåge | dichter Nebel | väga tihe udu | Πυκνή ομίχλη | brouillard dense | Gusta magla | nebbia densa | bieza migla | stiprus rūkas |
| 15 | moderate fog | умерена мъгла | Niebla moderada | mírná mlha | Moderat tåge | mäßiger Nebel | mõõdukas udu | Μέτρια ομίχλη | brouillard modéré | Umjerena magla | nebbia moderata | mērena migla | vidutinis rūkas |
| 16 | fog | слаба мъгла | Niebla | mlha | Tåge | Nebel | udu | Ομίχλη | brouillard | Magla | nebbia | migla | rūkas |
| 17 | mist | мъгла от изпарение | Neblina | kouřmo | Dis | Nebel | hägu | Υγρά αχλύς | brouillard léger | Sumaglica | nebbia leggera | viegla migla | migla |
| 18 | haze | замъглено | Bruma | zákal | Tågedis | Dunst | somp | Ξηρά αχλύς | brume | Izmaglica | foschia | dūmaka | rūkana |
| 19 | light haze | леко замъглено | Bruma ligera | slabý zákal | Let tågedis | leichter Dunst | kerge somp | Ελαφρά ξηρά αχλύς | brume légère | Blaga izmaglica | foschia leggera | viegla dūmaka | lengva rūkana |
| 20 | clear | чисто | Despejado | průzračný vzduch | Klart | klar | selge | Αίθριος καιρός | clair | Vedro | sereno | skaidrs | giedra |
| 21 | very clear | много чисто | Muy despejado | velmi průzračný vzduch | Meget klart | sehr klar | väga selge | Πολύ αίθριος καιρός | très clair | Vrlo vedro | molto sereno | ļoti skaidrs | labai giedra |
| 22 | no fog | липса на мъгла | Sin niebla | bez mlhy | Ingen tåge | kein Nebel | udutu | Απουσία ομίχλης | pas de brouillard | Bez magle | assenza di nebbia | nav miglas | rūko nėra |

**WEATHER CATEGORY CODE**

| 0 | szélcsend | kalm | Stil | cisza | Calmo | calm | bezvetrie | brezvetrje | tyyntä | Lugnt | штиль (безветрие) | тихо |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | gyenge szellő, fuvallat | arja ħafifa | Flauw en stil | powiew | Aragem | vânt perceptibil | vánok | sapica | pientä tuulenvirettä | Svag vind | тихий ветер | лахор |
| 2 | enyhe szél | żiffa ħafifa | Flauwe koelte | słaby wiatr | Brisa ligeira | briză ușoară | slabý vietor | vetrič | heikkoa tuulta | Svag vind | легкий ветер | поветарац |
| 3 | gyenge szél | żiffa ħelwa | Lichte koelte | łagodny wiatr | Pequena brisa | briză slabă | mierny vietor | šibek veter | kohtalaista tuulta | Måttlig vind | слабый ветер | слаб ветар |
| 4 | mérsékelt szél | żiffa moderata | Matige koelte | umiarkowany wiatr | Brisa moderada | briză moderată | dosť čerstvý vietor | zmeren veter | navakkaa tuulta | Måttlig vind | умеренный ветер | умерен ветар |
| 5 | élénk szél | żiffa friska | Frisse bries | dość silny wiatr | Brisa fresca | briză semnificativă | čerstvý vietor | zmerno močan veter | kovaa tuulta | Frisk vind | свежий ветер | умерено јак ветар |
| 6 | erős szél | żiffa qawwija | Stijve bries | silny wiatr | Vento fresco | briză puternică | silný vietor | močan veter | myrskyä | Frisk vind | сильный ветер | јак ветар |
| 7 | viharos szél | kważi burraxka | Harde wind | bardzo silny wiatr | Vento forte | vânt puternic | prudký vietor | zelo močan veter | navakkaa tuulta (near gale) | Hård vind | крепкий ветер | бура |
| 8 | élénk viharos szél, vihar | burraxka | Stormachtig | sztorm/ wicher | Vento muito forte | vânt foarte puternic | búrlivý vietor | viharni veter | kovaa tuulta (gale) | Hård vind | очень крепкий ветер | средња бура |
| 9 | heves vihar | burraxka qalila | Storm | silny sztorm | Vento tempestuoso | furtună | víchrica | vihar | erittäin kovaa tuulta (strong gale) | Mycket hård vind | шторм | јака бура |
| 10 | dühöngő vihar, szélvész | maltempata | Zware storm | bardzo silny sztorm | Tempestade | furtună puternică | silná víchrica | močan vihar | myrskyä (storm) | Storm | сильный шторм | жестока бура |
| 11 | heves szélvész | maltempata qalila | Zeer zware storm | gwałtowny sztorm | Tempestade violenta | furtună violentă | mohutná víchrica | orkanski veter | ankaraa myrskyä (violent storm) | Svår storm | жестокий шторм | жестока олуја |
| 12 | orkán | uragan | Orkaan | huragan | Furacão | uragan | orkán | orkan | hirmumyrskyä (hurricane) | Orkan | ураган | ураган |
| 13 | sürű köd | ċpar oħxon | Zeer dichte mist | gęsta mgła | Nevoeiro cerrado | ceață groasă | veľmi silná hmla | zelo gosta megla | hyvin sakeaa sumua | Tjocka | сильный туман | веома густа магла |
| 14 | tartós köd, 6 órát meghaladja | ċpar dens | Dichte mist | bardzo gęsta mgła | Nevoeiro denso | ceață densă | silná hmla | gosta megla | sakeaa sumua | Tät dimma | плотный (густой) туман | густа магла |
| 15 | enyhe köd | ċpar moderat | Matige mist | lekka mgła | Nevoeiro moderado | ceață moderată | mierna hmla | zmerna megla | kohtalaista sumua | Måttlig dimma | умеренный туман | умерена магла |
| 16 | köd | ċpar | Mist (zichtbaarheid < 1000 m) | mgła | Nevoeiro | ceață | hmla | megla | heikkoa sumua | Dimma | туман | магла |
| 17 | párásság | raxx | Mist (zichtbaarheid > 1000 m) | mgiełka | Neblina | pâclă | dymno | meglica | utua | Lätt dimma | дымка | измаглица |
| 18 | homály | imċajpar | Nevel | przymglenie | Bruma | negură | zákal | suha motnost | auerta | Dis | мгла | сумаглица |
| 19 | száraz légköri homály | ftit imċajpar | Lichte nevel | lekkie przymglenie | Bruma ligeira | ceață subțire | slabý zákal | rahla suha motnost | kevyttä auerta | Lätt dis | легкая мгла | блага сумаглица |
| 20 | tiszta | ċar | Helder | przejrzyście | Limpo | senin | jasno | jasno | selkeää | Klart | ясно | ведро |
| 21 | teljes látás | ċar ħafna | Zeer helder | bardzo przejrzyście | Muito limpo | foarte senin | veľmi jasno | zelo jasno | hyvin selkeää | Helt klart | очень ясно | веома ведро |
| 22 | ködmentes | ebda ċpar | Geen mist | brak mgły | Sem nevoeiro | fără ceață | bez hmly | brez megle | ei sumua | Ingen dimma | нет тумана | без магле |

**WEATHER DIRECTION CODE**

| N | north | Северно | Norte | severně | Nord | Nord | põhi | Βόρεια | Nord | Sjeverno | nord | Uz ziemeļiem | šiaurė |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NE | north-east | Североизточно | Noreste | severo-východně | Nordøst | Nord-Ost | kirre | Βορειοανατολικά | Nord-est | Sjeveroistočno | nord-est | Uz ziemeļaustrumiem | šiaurės rytai |
| E | east | Източно | Este | východně | Øst | Ost | ida | Ανατολικά | Est | Istočno | est | Uz austrumiem | rytai |
| SE | south-east | Югоизточно | Sureste | jiho-východně | Sydøst | Süd-Ost | kagu | Νοτιοανατολικά | Sud-est | Jugoistočno | sud-est | Uz dienvidaustrumiem | pietryčiai |
| S | south | Южно | Sur | jižně | Syd | Süd | lõuna | Νότια | Sud | Južno | sud | Uz dienvidiem | pietūs |
| SW | south-west | Югозападно | Suroeste | jiho-západně | Sydvest | Süd-West | edel | Νοτιοδυτικά | Sud-ouest | Jugozapadno | sud-ovest | Uz dienvidrietumiem | pietvakariai |
| W | west | Западно | Oeste | západně | Vest | West | lääs | Δυτικά | Ouest | Zapadno | ovest | Uz rietumiem | vakarai |
| NW | north-west | Северозападно | Noroeste | severo-západně | Nordvest | Nord-West | loe | Βορειοδυτικά | Nord-ouest | Sjeverozapadno | nord-ovest | UZ ziemeļrietumiem | šiaurės vakarai |
| WRB | variable | Променлив | Variable | proměnlivě | Variabel | veränderlich | muutlik | Μεταβλητός | variable | Promjenjivo | variabile | Mainīgi | nepastovi |

**WEATHER DIRECTION CODE**

| N | észak | it-Tramuntana | Noord | północ | Norte | nord | severne | severni | Pohjoinen | Nord | северный | Север |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NE | észak-kelet | il-Grigal | Noordoost | północny wschód | Nordeste | nord-est | severo-východne | severovzhodni | Koillinen | Nordost | северо-восточный | Североисток |
| E | kelet | il-Lvant | Oost | wschód | Leste | est | východne | vzhodni | Itä | Öst | восточный | Исток |
| SE | dél-kelet | ix-Xlokk | Zuidoost | południowy wschód | Sudeste | sud-est | juho-východne | jugovzhodni | Kaakko | Sydost | юго-восточный | Југоисток |
| S | dél | in-Nofsinhar | Zuid | południe | Sul | sud | južne | južni | Etelä | Syd | южный | Југ |
| SW | dél-nyugat | il-Lbiċ | Zuidwest | południowy zachód | Sudoeste | sud-vest | juho-západne | jugozahodni | Lounas | Sydväst | юго-западный | Југозапад |
| W | nyugat | il-Punent | West | zachód | Oeste | vest | západne | zahodni | Länsi | Väst | западный | Запад |
| NW | észak-nyugat | il-Majjistral | Noordwest | północny zachód | Noroeste | nord-vest | severo-západne | severozahodni | Luode | Nordväst | северо-западный | Северозапад |
| WRB | változó | varjabbli | Veranderlijk | zmienny | Variável | variabil | premenlivo | spremenljiv | vaihtelee | Växlande | Переменный | променљив |

**GUI LABELS**

| area | area | Район | Área | Oblast | Område | Gebiet | piirkond | Ζώνη | zone | Područje | area | Apgabals | sritis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| button_back | Back | Назад | Retroceder | Zpět | Tilbage | Zurück | Tagasi | Επιστροφή | Retour | Natrag | indietro | Atpakaļ | Atgal |
| button_cancel | Cancel | Отказ | Cancelar | Zrušit | Annullér | Abbrechen | Katkesta | Ακύρωση | Annuler | Odustani | annulla | Atcelt | Atšaukti |
| button_new_search | New search | Ново търсене | Nueva búsqueda | Nové hledání | Ny søgning | Neue Suche | Uus otsing | Νέα έρευνα | nouvelle recherche | Nova pretraga | nuova ricerca | Jauns meklēšanas vaicājums | Nauja paieška |
| button_register | Register | Регистриране | Registrarse | Registrovat | Registrér | Registrieren | Registreeri | Εγγραφή | S'enregistrer | Registracija | registrare | Reģistrēt | Registruotis |
| button_save | Save | Запазване | Guardar | Uložit | Gem | Speichern | Salvesta | Αποθήκευση | Sauvegarder | Spremi | salvare | Saglabāt | Išsaugoti |
| button_search | Search | Търсене | Buscar | Hledat | Søg | Suchen | Otsi | Αναζήτηση | Rechercher | Traži | ricerca | Meklēt | Paieška |
| button_view | View | Преглед | Visualizar | Zobrazit | Vis | Anzeigen | Vaata | Προβολή | Voir | Pregled | visualizzare | Skatīt | Rodyti |
| email_address | E-mail address | Адрес на ел. поща | Correo electrónico | E-mailová adresa | E-mailadresse | E-Mail Adresse | E-posti aadress | Διεύθυνση ηλεκτρονικού ταχυδρομείου | Adresse email | Adresa e-pošte | indirizzo e-mail | E-pasta adrese | E. pašto adresas |
| email_service | e-mail service | E-mail услуга | Servicio de correo electrónico | E-mailová služba | E-mailtjeneste | E-Mail Service | E-posti teenus | Υπηρεσία ηλεκτρονικού ταχυδρομείου | Service email | Usluga elektronske pošte | servizio e-mail | E-pasta pakalpojums | e. pašto paslauga |
| email_service_register | Registration e-mail service | Регистриране за E-mail услуга | Registrarse servicio de correo electrónico | Registrace e-mailové služby | Registrering af E-mailtjeneste | Registrierung E-Mail-Service | Registreerimise e-posti teenus | Εγγραφή σε υπηρεσία ηλεκτρονικού ταχυδρομείου | Enregistrement service email | Registracija usluge elektronske pošte | registrare servizio e-mail | Reģistrācijas e-pasta pakalpojums | Registracijos e. pašto paslauga |
| error_validation | Validation error: | Грешка при валидиране | Error de validación: | Chyba ověření: | Validation error: | Fehler bei der Validierung: | Valideerimise viga: | Σφάλμα επικύρωσης | Erreur de validation: | Pogreška pri provjeri valjanosti: | errore di convalida: | Validācijas kļūda: | Atlikus patikrą aptikta klaida: |
| format_code | Code | Кодов формат | Código | Kód | Kode | Code | Kood | Κωδικός | Code | Kod | codice | Kods | Kodas |
| format_pdf | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF |
| format_select | Select format | Избиране на формат | Seleccionar formato | Vyberte formát | Vælg format | Format wählen | Vali vorming | Επιλογή μορφοτύπου | Sélectionner le format | Odaberite format | seleziona formato | Atlasīt formātu | Pasirinkti formatą |
| format_text | Full text | Пълен текст | Texto íntegro | Textová zpráva | Fuld tekst | Volltext | Terviktekst | Πλήρες κείμενο | Message intégral | Puni tekst | full-text | Pilns teksts | Visas tekstas |
| format_xml | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML |
| gauge | gauge | Водомерна станция | Gálibo | Vodočet | Profil | Pegel | Mõõtur | Αισθητήρας | capteur | Vodomjerna postaja | misuratore | Mērinstruments | Vandens lygio matavimo punktas |
| ID | ID | Идентификация | ID | ID | ID | ID | ID | ID | ID | ID | ID | ID | ID |
| km_from | River km from | Речен км. от | Km de río desde | Říční km od | Flod km fra | Stromkilometer von | Jõe km alates | Χιλιόμετρα από | Kilomètres depuis | Riječni km od | km di fiume da | Upes km no | Upės km nuo |
| km_to | River km to | Речен км. до | Km de río hasta | Říční km do | Flod km til | Stromkilometer bis | Jõe km kuni | Χιλιόμετρα έως | Kilomètres jusqu'a | Riječni km do | km di fiume fino a | Upes km līdz | Upės km iki |
| language | Language | Език | Lengua | Jazyk | Sprog | Sprache | Keel | Γλώσσα | Langue | Jezik | lingua | Valoda | Kalba |
| language_select | English | Български | Inglés | Česky | Engelsk | Deutsch | Eesti | Ελληνική | Français | Hrvatski | italiano | Angļu | Anglų |
| message_search | Search notices | Търсене на съобщения | Buscar avisos | Vyhledat zprávy | Søgemeddelelser | Nachrichtenabfrage | Otsi teadetest | Αναζήτηση ανακοίνωσης | Chercher avis | Pretraži obavijesti | ricerca avvisi | Meklēt paziņojumus | Pranešimų paieška |
| message_type | Message type | Тип на съобщението | Tipo de mensaje | Typ zprávy | Meddelelsestype | Nachrichtentyp | Teate liik | Τύπος μηνύματος | Type de message | Vrsta poruke | tipo di messaggio | Ziņojuma veids | Pranešimo tipas |
| nts | Notices to skippers | Известие до корабните водачи | Avisos a los navegantes | Zprávy vůdcům plavidel | Efterretninger for skippere | Nachrichten für die Binnenschifffahrt | Kipritele edastatavad teated | Ανακοινώσεις προς πλοιάρχους | Avis à la batellerie | Priopćenja brodarstvu | avvisi ai naviganti | Paziņojumi kapteiņiem | Pranešimai kapitonams |
| password | Password | Парола | Contraseña | Heslo | Adgangskode | Passwort | Salasõna | Κωδικός πρόσβασης | Mot de passe | Lozinka | password | Parole | Slaptažodis |
| password_repeat | Repeat password | Повторете паролата | Repetir contraseña | Zopakovat heslo | Gentag adgangskode | Passwort wiederholen | Korda salasõna | Επανάληψη κωδικού πρόσβασης | Répéter mot de passe. | Potvrda lozinke | ripeti password | Parole vēlreiz | Pakartokite slaptažodį |
| title | Title | Заглавие | Título | Název | Titel | Titel | Tiitel | Τίτλος | Titre | Naslov | titolo | Nosaukums | Pavadinimas |
| user_account_management | Manage user account | Управление на акаунта | Gestionar cuenta de usuario | Spravovat uživatelský účet | Forvaltning af brugerkonto | Benutzerkonto verwalten | Kasutajakonto haldamine | Διαχείριση λογαριασμού χρήστη | Gérer votre compte | Upravljanje korisničkim računom | gestisci account utente | Pārvaldīt lietotāja kontu | Tvarkyti vartotojo paskyrą |
| valid_from | Valid from | Валиден от | Válido desde | Platné od | Gyldig fra | Gültig von | Kehtiv alates | Ισχύει από | Valide à partir de | Važeće od | valido da | Derīgs no | Galioja nuo |
| valid_till | Valid till | Валиден до | Válido hasta | Platné do | Gyldig til | Gültig bis | Kehtiv kuni | Ισχύει έως | Valide jusqu'à | Važeće do | valido fino a | Derīgs līdz | Galioja iki |
| waterway | Waterway | Воден път | Vía navegable | Vodní cesta | Vandvej | Wasserstraße | Veetee | Πλωτή οδός | Voie d’eau | Vodni put | via navigabile | Ūdensceļš | Vandens kelias |
| Waterway_section | Waterway section | Участък от водния път | Tramo de vía navegable | Úsek vodní cesty | Vandvejsstrækning | Wasserstraßenabschnitt | Veetee osa | Τμήμα πλωτής οδού | Section de voie d'eau | Dionica vodnog puta | sezione di via navigabile | Ūdensceļa posms | Vandens kelio ruožas |

**GUI LABELS**

| area | terület | żona | Gebied | obszar | Superfície | zonă | Oblasť | območje | alue | Område | Область | Област |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| button_back | Vissza | Lura | Terug | Cofnij | Recuar | Înapoi | Späť | nazaj | takaisin | Tillbaka | Назад | Назад |
| button_cancel | Mégsem | Ikkanċella | Annuleren | Anuluj | Cancelar | Anulează | Zrušiť | prekliči | peruuta | Avbryt | Отменить | Откажи |
| button_new_search | Új keresés | Tfittxija ġdida | Nieuwe zoekopdracht | Nowe wyszukiwanie | Nova pesquisa | Căutare nouă | Nové hľadanie | novo iskanje | uusi haku | Ny sökning | Новый поиск | Нова претрага |
| button_register | Regisztráció | Irreġistra | Registreren | Zarejestruj | Registar | Înregistrare | Registrovať | registracija | Rekisteröidy | Registrera | Регистрация | Регистрација |
| button_save | Mentés | Issejvja | Opslaan | Zapisz | Guardar | Salvează | Uložiť | shrani | Tallenna | Spara | Сохранить | Снимити |
| button_search | Keresés | Fittex | Zoeken | Szukaj | Pesquisar | Căutare | Vyhľadať | iskanje | Hae | Sök | Поиск | Претрага |
| button_view | Megtekint | Ara | Bekijken | Pokaż | Visualizar | Vizualizare | Zobraziť | pogled | Katso | Visa | Просмотр | Преглед |
| email_address | Email cím | Indirizz tal-posta elettronika | E-mailadres | Adres e-mail | Endereço eletrónico | Adresa de e-mail | E-mailová adresa | e-poštni naslov | sähköpostiosoite | e-postadress | Адрес электронной почты | Електронска адреса |
| email_service | Email szolgáltatás | servizz tal-posta elettronika | E-maildienst | Usługa e-mail | Correio eletrónico | Serviciu e-mail | E-mailová služba | e-poštna storitev | sähköpostipalvelu | e-posttjänst | услуга электронной почты | Услуга електронске поште |
| email_service_register | Regisztráció az email-küldő szolgáltatásra | Reġistrazzjoni tas-servizz tal-posta elettronika | Registreren e-maildienst | Rejstracja do usługi e-mail | Registo correio eletrónico | Înregistrare pentru serviciu e-mail | Registrácia pre e-mailovú službu | storitev za registracijo e-poštnega naslova | Rekisteröidy sähköpostipalveluun | Registrering, e-posttjänst | Регистрация услуг электронной почты | Регистрација сервиса електронске поште |
| error_validation | Érvényesítési hiba | Żball fil-validazzjoni: | Validatiefout | Błąd walidacji | Erro de validação: | Eroare de validare: | Chyba validácie: | napaka pri potrjevanju | Validointivirhe: | Valideringsfel: | Ошибка валидации: | Грешка у провери: |
| format_code | Kód | Kodiċi | Code | Kod | Código | Cod | Kód | koda | Koodi | Kod | Код | Код |
| format_pdf | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF |
| format_select | Válasszon formátumot | Agħżel il-format | Formaat kiezen | Wybierz format | Selecionar formato | Selectați formatul | Vyberte formát | izberi format | Valitse formaatti | Välj format | Выберите формат | Изабери формат |
| format_text | Teljes szöveg | Test sħiħ | Volle tekst | Pełny tekst | Texto integral | Mesaj text integral | Textová správa | celotno besedilo | Kokoteksti | Fulltext | Полный текст сообщения | Цео текст |
| format_xml | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML |
| gauge | mérce | kejl | Gauge | Wodowskaz | Gabarito | miră | Vodomerná stanica | merilnik | Vedenkorkeusmittari | Vattenståndsmätare | Водомерный пост | Водомерна станица |
| ID | Azonosító | ID | ID | ID | ID | ID | ID | ID | ID | ID | ID | ID |
| km_from | Folyó-km-tól | Km tax-xmara minn | Rivier-km vanaf | km rzeki od | Km do rio a partir de | De la kilometrul | Riečny km od | rečni km od | Jokikilometrejä lähtöpaikasta | Från flodkilometer | От км | Речни километар од |
| km_to | Folyó km-ig | Km tax-xmara sa | Rivier-km tot | km rzeki od | Km do rio até | Până la kilometrul | Riečny km do | rečni km do | Jokikilometrejä kohteeseen | Till flodkilometer | До км | Речни километар до |
| language | Nyelv | Lingwa | Taal | Język | Língua | Limba | Jazyk | jezik | Kieli | Språk | язык | Језик |
| language_select | Magyar | Ingliż | Nederlands | polski | Inglês | Română | Slovensky | slovenščina | suomi | Svenska | Русский | српски |
| message_search | Hírlevelek keresése | Fittex avviżi | Berichten zoeken | Szukaj komunikatu | Pesquisar avisos | Caută avize | Vyhľadať správy | išči obvestila | Viestihaku | Sök meddelanden | Поиск извещения | Претрага Саопштења |
| message_type | Üzenettípus | Tip ta’ messaġġ | Berichttype | Typ wiadomości | Tipo de mensagem | Tip de mesaj | Typ správy | vrsta sporočila | Viestin laji | Typ av meddelande | Тип сообщения | Тип поруке |
| nts | Hajósoknak szóló információk | Avviżi lill-Kaptani | Berichten aan de scheepvaart | Komunikaty dla kapitanów | Avisos à navegação | Aviz către navigatori | Správy pre veliteľov lodí | obvestila kapitanom | Ilmoitukset kapteenille | Meddelanden till befälhavare | Извещения судоводителям | Саопштење бродарству |
| password | Jelszó | Password | Wachtwoord | Hasło | Senha | Parola | Heslo | geslo | Salasana | Lösenord | Пароль | Лозинка |
| password_repeat | Jelszó újra | Irripeti l-password | Wachtwoord herhalen | Powtórz hasło | Repetir senha | Reintroduceți parola | Zopakovať heslo | ponovno vpiši geslo | Toista salasana | Upprepa lösenord | Пожалуйста, повторите пароль. | Поновите лозинку |
| title | Cím | Titlu | Titel | Tytuł | Título | Titlu | Názov | naslov | Nimi | Titel | Название | Назив |
| user_account_management | Felhasználói számla kezelése | Immaniġġja l-kont tal-utent | Gebruikersaccount beheren | Zrządzaj kontem użytkownika | Gerir conta utilizador | Setează cont | Spravovať účet | upravljanje uporabniškega računa | Hallinnoi käyttäjätiliä | Hantera användarkonto | Управление аккаунтом | Управљање корисничким налогом |
| valid_from | Érvényesség kezdete | Validu minn | Geldig vanaf | Ważne od | Válido de | Valabil din | Platné od | veljavno od | Voimassa … alkaen | Giltigt från och med | Действует с | Важи од |
| valid_till | Érvényesség lejárata | Validu sa | Geldig tot | Ważne do | Válido até | Valabil până la | Platné do | veljavno do | Voimassa … asti | Giltigt till och med | действительна до | Важи до |
| waterway | Víziút | Passaġġ fuq l-ilma | Waterweg | Droga wodna | Via navegável | Numele căii navigabile | Vodná cesta | vodna pot | Vesiväylä | Vattenväg | Водный путь | Водни пут |
| Waterway_section | Víziút szakasz | Sezzjoni ta’ passaġġ fuq l-ilma | Waterwegsectie | Odcinek drogi wodnej | Troço via navegável | Secțiunea căii navigabile | Úsek vodnej cesty | odsek vodne poti | Vesiväylän osa | Avsnitt av vattenväg | Участок водного пути | Део водног пута |

(

) Regulamento (CE) n.º 414/2007 da Comissão, de 13 de março de 2007, relativo às directrizes técnicas para a planificação, introdução e operação dos serviços de informação fluvial referidas no artigo 5.º da Diretiva 2005/44/CE do Parlamento Europeu e do Conselho relativa a serviços de informação fluvial (RIS) harmonizados nas vias navegáveis interiores da Comunidade (JO L 105 de 23.4.2007, p. 1).

(

) Regulamento (CE) n.º 415/2007 da Comissão, de 13 de março de 2007, relativo às especificações técnicas dos sistemas de localização e seguimento de embarcações a que se refere o artigo 5.º da Diretiva 2005/44/CE do Parlamento Europeu e do Conselho relativa a serviços de informação fluvial (RIS) harmonizados nas vias navegáveis interiores da Comunidade (JO L 105 de 23.4.2007, p. 35).

(

) Os códigos ONU de país são definidos em conformidade com o ponto 2.4.2.12 do anexo do Regulamento (UE) n.º 164/2010 da Comissão (JO L 57 de 6.3.2010, p. 1) e são idênticos ao código alfabético de duas letras da norma ISO 3166-1.

(

) Descrição citada do sítio Web da WS-I: http://www.ws-i.org
