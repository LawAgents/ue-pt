---
id: "regulamento-ue-2013-1253-considerandos-a-anexo-i"
celex: "32013R1253"
title: "Regulamento (UE) n. ° 1253/2013 da Comissão, de 21 de outubro de 2013 , que altera o Regulamento (UE) n. ° 1089/2010 que estabelece as disposições de execução da Diretiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Considerandos a Anexo I"
type: "Regulamento"
number: "1253/2013"
year: 2013
date: 2013-10-21
status: "em vigor"
text_version: "original sem consolidação"
source: "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32013R1253"
eli: "http://data.europa.eu/eli/reg/2013/1253/oj"
retrieved: 2026-10-21
legal_notice: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
part_of: "regulamento-ue-2013-1253"
part: "Considerandos a Anexo I"
---

# Regulamento (UE) n. ° 1253/2013 da Comissão, de 21 de outubro de 2013 , que altera o Regulamento (UE) n. ° 1089/2010 que estabelece as disposições de execução da Diretiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Considerandos a Anexo I

## Considerandos

A COMISSÃO EUROPEIA,

Tendo em conta o Tratado sobre o Funcionamento da União Europeia,

Tendo em conta a Diretiva 2007/2/CE do Parlamento Europeu e do Conselho, de 14 de março de 2007, que estabelece uma infraestrutura de informação geográfica na Comunidade Europeia (INSPIRE) (1), nomeadamente, o artigo 7.º, n.º 1,

Considerando o seguinte:

(1) O Regulamento (UE) n.º 1089/2010 da Comissão, de 23 de novembro de 2010, que estabelece as disposições de execução da Diretiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos (2), define as modalidades técnicas da interoperabilidade dos conjuntos de dados geográficos relacionadas com as categorias temáticas de dados geográficos constantes do anexo I da Diretiva 2007/2/CE

(2) A fim de assegurar a plena interoperabilidade dos conjuntos de dados geográficos, convém estabelecer as disposições técnicas relativas à interoperabilidade dos conjuntos de dados geográficos relacionados com as categorias temáticas de dados geográficos constantes dos anexos II e III da Diretiva 2007/2/CE.

(3) A fim de assegurar a coerência global dos aspetos técnicos no que diz respeito à interoperabilidade dos conjuntos de dados geográficos constantes do presente regulamento, devem ser alteradas as atuais disposições técnicas em matéria de interoperabilidade dos conjuntos de dados geográficos relacionadas com as categorias temáticas de dados geográficos constantes do anexo I da Diretiva 2007/2/CE.

(4) Em primeiro lugar, os requisitos relativos às listas de códigos devem ser alterados a fim de permitir uma abordagem flexível no que diz respeito à descrição dos valores das listas de códigos a diferentes níveis de detalhe e de estabelecer as disposições técnicas para a partilha de listas de códigos alargadas.

(5) Em segundo lugar, a restrição das propriedades geográficas no esquema geográfico «Simple Feature» («Simple Feature spatial schema») deve ser aplicada de forma mais flexível, a fim de permitir também a disponibilização de dados 2.5D.

(6) Em terceiro lugar, deve ser introduzido um elemento adicional de metadados a fim de permitir a identificação do tipo de representação espacial («spatial representation type») utilizado para um conjunto de dados.

(7) Em quarto lugar, a categoria temática de dados geográficos «Sistemas de Quadrículas Geográficas» deve ser alargada a fim de comportar uma quadrícula multirresoluções baseada em coordenadas geográficas.

(8) Em quinto lugar, a categoria temática de dados geográficos «Unidades Administrativas» deve ser alargada a fim de descrever unidades administrativas marítimas.

(9) Em sexto lugar, a fim de evitar sobreposições com tipos de objetos geográficos especificados em categorias temáticas de dados geográficos constantes dos anexos II e III da Diretiva 2007/2/CE, devem ser suprimidos alguns tipos candidatos das categorias temáticas de dados geográficos «Unidades Administrativas» e «Hidrografia».

(10) O Regulamento (UE) n.º 1089/2010 deve, por conseguinte, ser alterado em conformidade.

(11) As medidas previstas no presente regulamento estão em conformidade com o parecer do comité instituído pelo artigo 22.º da Diretiva 2007/2/CE,

ADOTOU O PRESENTE REGULAMENTO:

## Artigo 1.º

O Regulamento (UE) n.º 1089/2010 é alterado do seguinte modo:

(1) O artigo 2.º é alterado do seguinte modo:

(a) A parte introdutória passa a ter a seguinte redação:

«Para efeitos do presente regulamento, são aplicáveis as definições seguintes, bem como as definições específicas de temas constantes dos anexos:»

(b) O ponto 4 é suprimido;

(c) No ponto 6, «a norma ISO 19103» é substituída por «a norma ISO/TS 19103:2005»;

(d) No ponto 9, «a norma EN ISO 19135» é substituída por «a norma EN ISO 19135:2007»;

(e) No ponto 11, «a norma EN ISO 19128» é substituída por «a norma EN ISO 19128:2008»;

(f) No ponto 13, «a norma EN ISO 19115» é substituída por «a norma EN ISO 19115:2005/AC:2008»;

(g) No ponto 15, «a norma EN ISO 19135» é substituída por «a norma EN ISO 19135:2007»;

(h) No ponto 18, «a norma ISO 19103» é substituída por «a norma ISO/TS 19103:2005»;

(i) São aditados os seguintes pontos 21 a 30:

«21. «Propriedade»(property)

: um atributo ou associação;

22. «Tipo de união»(union type)

: um tipo que consiste numa, e apenas numa, de várias alternativas (enumeradas como atributos membros), em conformidade com a norma ISO/TS 19103:2005;

23. «Classe de associação»(association class)

: um tipo que define propriedades adicionais numa relação entre dois outros tipos;

24. «Cobertura»(coverage)

: um objeto geográfico que atua como uma função para fornecer valores da sua gama para qualquer posição direta dentro do seu domínio espacial, temporal ou espaciotemporal, em conformidade com a norma ISO 19123:2007;

25. «Domínio»(domain)

: um conjunto bem definido, em conformidade com a norma ISO/TS 19103:2005;

26. «Gama»(range)

: um conjunto de valores de atributos de características (features) associado por uma função com os elementos do domínio de uma cobertura, em conformidade com a norma EN ISO 19123:2007;

27. «Quadrícula retificada»(rectified grid)

: uma quadrícula em que existe uma transformação afim entre as coordenadas da quadrícula e as coordenadas de um sistema de referência de coordenadas, em conformidade com a norma EN ISO 19123:2007;

28. «Quadrícula referenciável»(referenceable grid)

: uma quadrícula associada a uma transformação que pode ser utilizada para converter valores de coordenadas de quadrículas em valores de coordenadas referenciadas a um sistema de referência de coordenadas externo, em conformidade com a norma EN ISO 19123:2007;

29. «Tesselação»(tessellation)

: a partição de um espaço num conjunto de subespaços contíguos com a mesma dimensão do espaço particionado; Uma tecelagem num espaço 2D consiste num conjunto de polígonos não sobrepostos que cobrem totalmente uma região de interesse;

30. «Valor mais restrito»(narrower value)

: um valor que tem uma relação hierárquica com um valor-mãe mais geral.»

(2) O artigo 4.º é alterado do seguinte modo:

(a) O n.º 1 passa a ter a seguinte redação:

«1. Para o intercâmbio e classificação de objetos geográficos a partir de conjuntos de dados que satisfazem as condições estabelecidas no artigo 4.º da Diretiva 2007/2/CE, os Estados-Membros devem utilizar os tipos de objetos geográficos e os tipos de dados associados, as enumerações e as listas de códigos definidos nos anexos II, III e IV no que diz respeito às categorias temáticas com que os conjuntos de dados estão relacionados.»

(b) Todas as referências a «no anexo II» nos n.ºs 2 e 3 são substituídas por referências a «nos anexos».

(c) No n.º 3, o segundo período passa a ter a seguinte redação: «Os valores das enumerações e das listas de códigos são identificados de forma única por códigos mnemónicos linguisticamente neutros para computadores. Os valores podem também incluir um nome específico de uma língua a utilizar para fins de interação humana.»

(3) No artigo 5.º, o n.º 4 é suprimido.

(4) O artigo 6.º passa a ter a seguinte redação:

«Artigo 6.º

Listas de códigos e enumerações

1. As listas de códigos devem ser de um dos seguintes tipos, conforme indicado nos anexos:

(a) Listas de códigos cujos valores autorizados incluem apenas os valores especificados no presente regulamento;

(b) Listas de códigos cujos valores autorizados incluem os valores especificados no presente regulamento e valores mais restritos definidos pelos fornecedores de dados;

(c) Listas de códigos cujos valores autorizados incluem os valores especificados no presente regulamento e valores adicionais a qualquer nível definidos pelos fornecedores de dados;

(d) Listas de códigos cujos valores autorizados incluem quaisquer valores definidos pelos fornecedores de dados.

Para fins do disposto nas alíneas b), c) e d), para além dos valores autorizados, os fornecedores de dados podem utilizar os valores especificados no Documento de Orientação Técnica INSPIRE (INSPIRE Technical Guide) relevante disponível no sítio Web INSPIRE do Centro Comum de Investigação.

2. As listas de códigos podem ser hierárquicas. Os valores das listas de códigos hierárquicas podem ter um valor-mãe mais geral. Quando os valores válidos de uma lista de códigos hierárquica são especificados num quadro do presente regulamento, os valores-mãe são enumerados na última coluna.

3. Quando, relativamente a um atributo cujo tipo é uma lista de códigos conforme referido no n.º 1, alíneas b), c) ou d), um fornecedor de dados apresentar um valor que não está especificado no presente regulamento, esse valor e a sua definição devem ser disponibilizados num registo.

4. Os atributos ou associações de tipos de objetos geográficos ou de tipos de dados cujo tipo é uma lista de códigos apenas podem assumir valores que estejam autorizados de acordo com a especificação da lista de códigos.

5. Os atributos ou as associações de tipos de objetos geográficos ou de tipos de dados que tenham um tipo de enumeração apenas podem assumir valores das listas especificadas para o tipo de enumeração.»

(5) No artigo 8.º, n.º 2, e no artigo 11.º, n.º 1, as referências «no anexo II», são substituídas por referências «nos anexos».

(6) O artigo 12.º é alterado do seguinte modo:

(a) O n.º 1 passa a ter a seguinte redação:

«1. O domínio de valores das propriedades geográficas definidas no presente regulamento deve limitar-se ao esquema geográfico «Simple Feature» conforme definido em Herring, John R. (ed.), OpenGIS® Implementation Standard for Geographic information – Simple feature access – Part 1: Common architecture, version 1.2.1, Open Geospatial Consortium, 2011, salvo quando indicação em contrário para um determinado tipo ou categoria temática de dados geográficos.»

(b) O n.º 2 é alterado do seguinte modo:

O termo «unidades SI» é substituído por «unidades SI ou unidades não-SI aceites para utilização com o Sistema Internacional de Unidades».

(7) Ao artigo 13.º é aditado o seguinte n.º 6:

«6. Tipo de representação espacial: o método a utilizar para representar espacialmente a informação geográfica.»

(8) O artigo 14.º é alterado do seguinte modo:

(a) O n.º 2, alínea b), passa a ter a seguinte redação:

«(b) O tipo ou tipos de objetos geográficos, ou um subconjunto destes, que constituem o conteúdo da camada.»

(b) É aditado o seguinte n.º 3:

«3. Podem ser definidas várias camadas em relação a tipos de objetos geográficos cujos objetos podem ser classificados mais pormenorizadamente utilizando um atributo com um valor na lista de códigos. Cada uma destas camadas deve incluir os objetos geográficos correspondentes a um valor específico da lista de códigos. Na definição desses conjuntos de camadas nos anexos II, III e IV, devem ser cumpridos todos os seguintes requisitos:

a) O espaço reservado a <Valor de lista de códigos> deve representar os valores da lista de códigos relevante, com o primeiro caráter em maiúsculas.

b) O espaço reservado a <nome legível para as pessoas> deve representar o nome legível para as pessoas dos valores da lista de códigos;

c) O tipo de objeto geográfico deve incluir o atributo e a lista de códigos relevantes, entre parênteses;

d) Deve ser apresentado um exemplo de uma camada.»

(9) O anexo I é alterado em conformidade com o estabelecido no anexo I do presente regulamento.

(10) O anexo II é alterado em conformidade com o estabelecido no anexo II do presente regulamento.

(11) É aditado o anexo III, cujo texto figura no anexo III do presente regulamento.

(12) É aditado o anexo IV, cujo texto figura no anexo IV do presente regulamento.

## Artigo 2.º

O presente regulamento entra em vigor no [vigésimo] dia seguinte ao da sua publicação no Jornal Oficial da União Europeia.

## Assinatura

O presente regulamento é obrigatório em todos os seus elementos e diretamente aplicável nos Estados-Membros de acordo com o estabelecido nos Tratados.

Feito em Bruxelas, em 21 de outubro de 2013.

Pela Comissão

O Presidente

José Manuel BARROSO

(1)

JO L 108 de 25.4.2007, p. 1.

(2)

JO L 323 de 8.12.2010, p. 11

## Anexo I

O anexo I do Regulamento (UE) n.º 1089/2010 é alterado do seguinte modo:

(1) O título passa a ter a seguinte redação: «Tipos Comuns, Definições e Requisitos».

(2) Em todo o texto, e salvo disposição em contrário no presente anexo, todas as ocorrências do período «Esta lista de códigos não pode ser alargada pelos Estados-Membros.» são substituídas por «Os valores autorizados para esta lista de códigos compreendem apenas os valores estabelecidos no quadro infra.»

(3) Em todo o texto, nos títulos de todos os quadros que especificam valores de listas de códigos, o texto «Valores autorizados para a lista de códigos» é substituído por «Valores para a lista de códigos».

(4) A secção 1 passa a ter a seguinte redação:

\**«1. TIPOS DEFINIDOS EM NORMAS EUROPEIAS E INTERNACIONAIS**

Os seguintes tipos comuns, utilizados em atributos ou associações de tipos de objetos geográficos ou de tipos de dados, são definidos do seguinte modo:

(1) Para os tipos “Any”, “Angle”, “Area”, “Boolean”, “CharacterString”, “Date”, “DateTime”, “Decimal”, “Distance”, “Integer”, “Length”, “Measure”, “Number”, “Probability”, “Real”, “RecordType”, “Sign”, “UnitOfMeasure”, “Velocity” e “Volume”, são aplicáveis as definições estabelecidas na norma ISO/TS 19103:2005.

(2) Para os tipos “DirectPosition”, “GM_Boundary”, “GM_Curve”, “GM_MultiCurve”, “GM_MultiSurface”, “GM_Object”, “GM_Point”, “GM_Primitive”, “GM_Solid”, “GM_Surface” e “GM_Tin”, são aplicáveis as definições estabelecidas na norma EN ISO 19107:2005.

(3) Para os tipos “TM_Duration”, “TM_GeometricPrimitive”, “TM_Instant”, “TM_Object”, “TM_Period” e “TM_Position”, são aplicáveis as definições estabelecidas na norma EN ISO 19108:2005/AC:2008.

(4) Para o tipo “GF_PropertyType”, são aplicáveis as definições estabelecidas na norma EN ISO 19109:2006.

(5) Para os tipos “CI_Citation”, “CI_Date”, “CI_RoleCode”, “EX_Extent”, “EX_VerticalExtent”, “MD_Distributor”, “MD_Resolution” e “URL”, são aplicáveis as definições estabelecidas na norma EN ISO 19115:2005/AC:2008.

(6) Para o tipo “CV_SequenceRule”, são aplicáveis as definições estabelecidas na norma EN ISO 19123:2007.

(7) Para os tipos “AbstractFeature”, “Quantity” e “Sign”, são aplicáveis as definições estabelecidas na norma EN ISO 19136:2009.

(8) Para os tipos “LocalisedCharacterString”, “PT_FreeText” e “URI”, são aplicáveis as definições estabelecidas na norma CEN ISO/TS 19139:2009.

(9) Para o tipo “LC_LandCoverClassificationSystem”, são aplicáveis as definições estabelecidas na norma ISO 19144-2:2012.

(10) Para os tipos “GFI_Feature”, “Location”, “NamedValue”, “OM_Observation”, “OM_Process”, “SamplingCoverageObservation”, “SF_SamplingCurve”, “SF_SamplingPoint”, “SF_SamplingSolid”, “SF_SamplingSurface” e “SF_SpatialSamplingFeature”, são aplicáveis as definições estabelecidas na norma ISO 19156:2011.

(11) Para os tipos “Category”, “Quantity”, “QuantityRange” e “Time”, são aplicáveis as definições estabelecidas em Robin, Alexandre (ed.), OGC®SWE Common Data Model Encoding Standard, version 2.0.0, Open Geospatial Consortium, 2011.

(12) Para os tipos “TimeValuePair” e “Timeseries”, são aplicáveis as definições estabelecidas em Taylor, Peter (ed.), OGC® WaterML 2.0: Part 1 – Timeseries, v2.0.0, Open Geospatial Consortium, 2012.

(13) Para os tipos “CGI_LinearOrientation” e “CGI_PlanarOrientation”, são aplicáveis as definições estabelecidas em CGI Interoperability Working Group, Geoscience Markup Language (GeoSciML), version 3.0.0, Commission for the Management and Application of Geoscience Information (CGI) of the International Union of Geological Sciences, 2011.»

(5) A Secção 2 é alterada do seguinte modo:

(a) No ponto 2.1, são suprimidas as seguintes restrições:

\**« Restrições do tipo de dados “Identificador”**

Nos atributos “localId” e “namespace”, apenas será utilizado o seguinte conjunto de carateres: {“A” …“Z”, “a”…“z”, “0”…“9”, “_”, “.”, “-”}, ou seja, apenas são autorizados caracteres do alfabeto latino, dígitos, traços inferiores (_), pontos e hífenes.».

(b) São aditados os seguintes pontos 2.2 a 2.7:

\**«2.2 Parte relacionada (RelatedParty)**

Uma organização ou pessoa com uma função relacionada com um recurso.

\**Atributos do tipo de dados “RelatedParty”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| individualName | Nome da pessoa relacionada. | PT_FreeText | voidable |
| organisationName | Nome da organização relacionada. | PT_FreeText | voidable |
| positionName | Posição da parte em relação a um recurso, como, por exemplo, chefe de departamento. | PT_FreeText | voidable |
| contact | Referências de contacto da parte relacionada. | Contact | voidable |
| role | Funções da parte em relação a um recurso, como, por exemplo, detentor. | PartyRoleValue | voidable |

\**Restrições do tipo de dados “RelatedParty”**

Deve ser fornecido, pelo menos, o nome da pessoa, organização ou cargo.

\**2.3 Contacto (Contact)**

Os canais de comunicação através dos quais é possível aceder a uma pessoa ou a algo.

\**Atributos do tipo de dados “Contact”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| address | Um endereço fornecido sob a forma de texto livre. | AddressRepresentation | voidable |
| contactInstructions | Instruções suplementares sobre como e quando contactar uma pessoa ou organização. | PT_FreeText | voidable |
| electronicMailAddress | Um endereço de correio eletrónico da organização ou da pessoa. | CharacterString | voidable |
| hoursOfService | Os períodos de tempo em que a organização ou a pessoa pode ser contactada. | PT_FreeText | voidable |
| telephoneFacsimile | Número de fax da organização ou da pessoa. | CharacterString | voidable |
| telephoneVoice | Número de telefone da organização ou da pessoa. | CharacterString | voidable |
| website | Páginas disponibilizadas na Internet pela organização ou pela pessoa. | URL | voidable |

\**2.4 Citação do documento (DocumentCitation)**

Citação para fins de referenciação de um documento de forma inequívoca.

\**Atributos do tipo de dados “DocumentCitation”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| name | Nome do documento. | CharacterString |  |
| shortName | Nome abreviado ou título alternativo do documento. | CharacterString | voidable |
| date | Data de criação, publicação ou revisão do documento. | CI_Date | voidable |
| link | Ligação a uma versão em linha do documento | URL | voidable |
| specificReference | Referência a uma parte específica do documento | CharacterString | voidable |

\**2.5 Citação da legislação (LegislationCitation)**

Citação para fins de referenciação inequívoca de um ato jurídico ou de uma parte específica de um ato jurídico.

Este tipo é um subtipo de “DocumentCitation”.

\**Atributos do tipo de dados “LegislationCitation”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| identificationNumber | Código utilizado para identificar o instrumento legislativo | CharacterString |  |
| officialDocumentNumber | Número do documento oficial utilizado para identificar de forma única o instrumento legislativo. | CharacterString |  |
| dateEnteredIntoForce | Data em que o instrumento legislativo entrou em vigor. | TM_Position |  |
| dateRepealed | Data em que o instrumento legislativo foi revogado. | TM_Position |  |
| level | O nível a que é adotado o instrumento legislativo. | LegislationLevelValue |  |
| journalCitation | Citação do jornal oficial em que está publicada a legislação. | OfficialJournalInformation |  |

\**Restrições do tipo de dados “LegislationCitation”**

Se o atributo de ligação estiver vazio (“void”), deve ser fornecida a citação do jornal oficial.

\**2.6 Informação do Jornal Oficial (OfficialJournalInformation)**

Citação integral da localização do instrumento legislativo no jornal oficial.

\**Atributos do tipo de dados “OfficialJournalInformation”**

<table> <tbody> <tr> <td>Atributo</td> <td>Definição</td> <td>Tipo</td> <td>Voidability</td> </tr> <tr> <td>officialJournalIdentification</td> <td>Referência do jornal oficial em que foi publicado o instrumento legislativo. Esta referência deve ser constituída por três partes: <table> <tbody> <tr> <td>—</td> <td>Título do jornal oficial</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>Volume e/ou número de série do jornal oficial</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>Número da(s) página(s)</td> </tr> </tbody> </table></td> <td>CharacterString</td> <td></td> </tr> <tr> <td>ISSN</td> <td>O Número Internacional Normalizado das Publicações em Série (ISSN) é um número com oito dígitos que identifica a publicação periódica em que o instrumento legislativo foi publicado.</td> <td>CharacterString</td> <td></td> </tr> <tr> <td>ISBN</td> <td>O Número Internacional Normalizado do Livro (ISBN) é um número com nove dígitos que identifica de forma única o livro em que foi publicado o instrumento legislativo.</td> <td>CharacterString</td> <td></td> </tr> <tr> <td>linkToJournal</td> <td>Ligação a uma versão em linha do jornal oficial</td> <td>URL</td> <td></td> </tr> </tbody> </table>

\**2.7 Identificador temático (ThematicIdentifier)**

Identificador temático para identificar de forma única o objeto geográfico.

\**Atributos do tipo de dados “ThematicIdentifier”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| identifier | Identificador único utilizado para identificar o objeto geográfico no sistema de identificação especificado. | CharacterString |  |
| identifierScheme | Identificador que define o sistema utilizado para atribuir o identificador. | CharacterString» |  |

(6) A secção 4 é alterada do seguinte modo:

(a) O ponto 4.1 passa a ter a seguinte redação:

\**«4.1 Estado da instalação (ConditionOfFacilityValue)**

O estado de uma instalação no que diz respeito à sua completude e utilização.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores mais restritos definidos pelos fornecedores de dados.

\**Valores para a lista de códigos “ConditionOfFacilityValue”**

| Valor | Nome | Definição |
|---|---|---|
| functional | funcional | A instalação está funcional. |
| projected | projetado | A instalação encontra-se em fase de projeto. Os trabalhos de construção ainda não tiveram início. |
| underConstruction | em construção | A instalação encontra-se em fase de construção e ainda não está funcional. Este valor aplica-se unicamente à construção inicial da instalação e não a trabalhos de manutenção. |
| disused | em desuso | A instalação já não é utilizada, mas não está a ser ou não foi desmantelada. |
| decommissioned | desmantelado | A instalação já não é utilizada e foi ou está a ser desmantelada.» |

(b) No ponto 4.2 «Código de país (CountryCode)», é suprimido o período «Esta lista de códigos não deve ser alargada pelos Estados-Membros.»

(c) São aditados os seguintes pontos 4.3 a 4.6:

\**«4.3 Nível de legislação (LegislationLevelValue)**

O nível a que um ato jurídico ou convenção foi adotado.

Os valores autorizados para esta lista de códigos incluem eventuais valores definidos pelos fornecedores de dados.

Os fornecedores de dados podem utilizar os valores especificados no Documento de Orientação Técnica INSPIRE sobre o Modelo Concetual Genérico INSPIRE (“

INSPIRE Generic Conceptual Model

”).

\**4.4 Função da parte (PartyRoleValue)**

Funções das partes relacionadas com um recurso ou responsáveis por esse recurso.

Os valores autorizados para esta lista de códigos incluem os valores constantes das listas de códigos seguintes ou de outras listas de códigos especificadas pelos fornecedores de dados:

— Código da função (CI_RoleCode): Funções desempenhadas por uma parte responsável, conforme especificado na norma EN ISO 19115:2005/AC:2008.

— Função de uma parte relacionada (RelatedPartyRoleValue): Classificação das funções das partes relacionadas, conforme indicado no quadro.

\**Valores para a lista de códigos “RelatedPartyRoleValue”**

| Valor | Nome | Definição |
|---|---|---|
| authority | autoridade | Uma parte legalmente mandatada para supervisionar um recurso e/ou as partes relacionadas com um recurso. |
| operator | operador | Uma parte que explora um recurso. |
| owner | detentor | Uma parte que possui um recurso, ou seja, à qual um recurso pertence de um ponto de vista jurídico. |

\**4.5 Nomes padronizados de previsões e fenómenos climáticos (CFStandardNamesValue)**

Definições de fenómenos observados em meteorologia e oceanografia.

Os valores autorizados para esta lista de códigos incluem eventuais valores definidos pelos fornecedores de dados.

Os fornecedores de dados podem utilizar os valores especificados no Documento de Orientação Técnica INSPIRE sobre o Modelo Concetual Genérico INSPIRE.

\**4.6 Sexo (GenderValue)**

O sexo de uma pessoa ou grupo de pessoas.

Os valores autorizados para esta lista de códigos incluem apenas os valores especificados no quadro infra.

\**Valores para a lista de códigos “GenderValue”**

| Valor | Nome | Definição |
|---|---|---|
| female | sexo feminino | Uma pessoa ou um grupo de pessoas do sexo feminino. |
| male | sexo masculino | Uma pessoa ou um grupo de pessoas do sexo masculino. |
| unknown | desconhecido | Uma pessoa ou um grupo de pessoas de sexo desconhecido.» |

(7) A seguir à secção 5, são aditadas as secções 6, 7 e 8:

\**«6. MODELO DE COBERTURA (COVERAGE MODEL)**

O modelo de cobertura INSPIRE consiste nos seguintes pacotes:

— Coberturas (Base) (Coverages (Base))

— Coberturas (Domínio e gama) (Coverages (Domain And Range))

\**6.1. Coberturas (Base)**

\**6.1.1. Tipos de objetos geográficos**

O pacote “Coberturas (Base)” contém o tipo de objeto geográfico “Cobertura”.

\**6.1.1.1. Cobertura (Coverage)**

Objeto geográfico que atua como uma função para fornecer valores da sua gama para qualquer posição direta dentro do seu domínio espacial, temporal ou espaciotemporal.

Este tipo é abstrato.

\**Atributos do tipo de objeto geográfico “Coverage”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| metadata | Metadados específicos da aplicação da cobertura. | Any |  |
| rangeType | Descrição da estrutura dos valores da gama. | RecordType |  |

\**6.2. Coberturas (Domínio e gama)**

\**6.2.1. Tipos de objetos geográficos**

O pacote “Coberturas (Domínio e Gama)” contém os seguintes tipos de objetos geográficos:

— Cobertura (Representação de domínio e gama) (Coverage (Domain And Range Representation))

— Cobertura de quadrícula retificada (Rectified Grid Coverage)

— Cobertura de quadrícula referenciável (Referenceable Grid Coverage)

\**6.2.1.1. Cobertura (Representação por domínio e gama) (CoverageByDomainAndRange)**

Cobertura que fornece o domínio e a gama como propriedades separadas.

Este tipo é um subtipo de “Coverage”.

Este tipo é abstrato.

\**Atributos do tipo de objeto geográfico “CoverageByDomainAndRange”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| coverageFunction | Descrição do modo como podem ser obtidos os valores da gama em localizações no domínio de cobertura. | CoverageFunction |  |
| domainSet | Configuração do domínio da cobertura descrita em termos de coordenadas. | Any |  |
| rangeSet | Conjunto de valores associados por uma função aos elementos do domínio da cobertura. | Any |  |

\**Restrições do tipo de objeto geográfico “CoverageByDomainAndRange”**

A função de quadrícula só é válida para domínios que são quadrículas.

\**6.2.1.2. Cobertura de quadrícula retificada (RectifiedGridCoverage)**

Cobertura cujo domínio consiste numa quadrícula retificada.

Este tipo é um subtipo de “CoverageByDomainAndRange”.

\**Restrições do tipo de objeto geográfico “RectifiedGridCoverage”**

O domínio deve ser uma quadrícula retificada.

Os pontos da quadrícula de uma “RectifiedGridCoverage” devem coincidir com os centros das células das quadrículas geográficas definidas no ponto 2.2 do anexo II a qualquer nível de resolução.

\**6.2.1.3. Cobertura de quadrícula referenciável (ReferenceableGridCoverage)**

Cobertura cujo domínio consiste numa quadrícula referenciável.

Este tipo é um subtipo de “CoverageByDomainAndRange”.

\**Restrições do tipo de objeto geográfico “ReferenceableGridCoverage”**

O domínio deve ser uma quadrícula referenciável.

\**6.2.2. Tipos de dados**

\**6.2.2.1. Função de cobertura (CoverageFunction)**

Descrição do modo como podem ser obtidos os valores da gama em localizações no domínio de cobertura.

Este tipo é um tipo de união.

\**Atributos do tipo de união “CoverageFunction”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| ruleDefinition | Uma descrição formal ou informal da função de cobertura como texto. | CharacterString |  |
| ruleReference | Uma descrição formal ou informal da função de cobertura como referência. | URI |  |
| gridFunction | Regra cartográfica para geometrias de quadrículas. | GridFunction |  |

\**6.2.2.2. Função da quadrícula (GridFunction)**

Uma regra cartográfica explícita para geometrias de quadrículas.

\**Atributos do tipo de dados “GridFunction”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| sequenceRule | Descrição do modo como os pontos das quadrículas estão ordenados para associação aos elementos dos valores no conjunto de gamas de valores da cobertura. | CV_SequenceRule |  |
| startPoint | O ponto da quadrícula a associar ao primeiro registo no conjunto de gamas de valores da cobertura. | Integer |  |

\**7. Modelo das observações (Observations Model)**

O modelo de observações INSPIRE consiste nos seguintes pacotes:

— Referências da observação (Observation References)

— Processos (Processes)

— Propriedades observáveis (Observable Properties)

— Observações especializadas (Specialised Observations)

\**7.1. Referências da observação**

\**7.1.1. Tipos de objetos geográficos**

O pacote “Referências da Observação” contém o tipo de objeto geográfico Conjunto de Observações».

\**7.1.1.1 Conjunto de observações (ObservationSet)**

Liga um conjunto de observações.

\**Atributos do tipo de objeto geográfico “ObservationSet”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| extent | Informação sobre a extensão geográfica e temporal. | EX_Extent |  |

\**Associações do tipo de objeto geográfico “ObservationSet”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| member | Um membro do “ObservationSet”. | OM_Observation |  |

\**7.2. Processos**

\**7.2.1. Tipos de objetos geográficos**

O pacote “Processos” contém o tipo de objeto geográfico “Process”.

\**7.2.1.1. Processo (Process)**

Descrição de um processo de observação.

Este tipo é um subtipo de “OM_Process”.

\**Atributos do tipo de objeto geográfico “Process”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier | voidable |
| name | Nome do processo. | CharacterString | voidable |
| type | Tipo de processo. | CharacterString | voidable |
| documentation | Mais informações em linha/fora de linha (online/offline) associadas ao processo. | DocumentCitation | voidable |
| processParameter | Parâmetro que controla a aplicação do processo e, consequentemente, o seu resultado. | ProcessParameter | voidable |
| responsibleParty | Pessoa ou organização relacionada com o processo. | RelatedParty | voidable |

\**7.2.2. Tipos de dados**

\**7.2.2.1. Parâmetro do processo (ProcessParameter)**

Descrição de um determinado parâmetro

\**Atributos do tipo de dados “ProcessParameter”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| name | Nome do parâmetro do processo. | ProcessParameterNameValue |  |
| description | Descrição do parâmetro do processo. | CharacterString |  |

\**7.2.3. Listas de códigos**

\**7.2.3.1. Nome do parâmetro do processo (ProcessParameterNameValue)**

Um lista de códigos dos nomes dos parâmetros do processo.

Os valores autorizados para esta lista de códigos incluem eventuais valores definidos pelos fornecedores de dados.

\**7.3. Propriedades observáveis**

\**7.3.1. Tipos de dados**

\**7.3.1.1. Restrição (Constraint)**

Uma restrição sobre uma propriedade, por exemplo, comprimento de onda = 200 nm.

\**Atributos do tipo de dados “Constraint”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| constrainedProperty | A propriedade sujeita a restrição, por exemplo, “colour” se a restrição for “colour = blue”. | PhenomenonTypeValue |  |
| label | Uma título legível para as pessoas relativo à restrição no seu conjunto. | CharacterString |  |

\**7.3.1.2. Restrição da categoria (CategoryConstraint)**

Uma restrição baseada numa categoria de qualificação. Por exemplo, “colour = red”.

Este tipo é um subtipo de “Constraint”.

\**Atributos do tipo de dados “CategoryConstraint”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| comparison | Um operador de comparação. No caso de uma restrição de categoria deve ser “equalTo” ou “notEqualTo”. | ComparisonOperatorValue |  |
| value | O valor da propriedade sujeita a restrição, por exemplo “blue” (se a propriedade sujeita a restrição for a cor). | CharacterString |  |

\**7.3.1.3. Restrição da gama (RangeConstraint)**

Uma restrição da gama numérica sobre alguma propriedade, por exemplo, comprimento de onda ≥ 300 nm e comprimento de onda ≤ 600 nm.

Este tipo é um subtipo de “Constraint”.

\**Atributos do tipo de dados “RangeConstraint”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| value | A gama numérica de valores da propriedade sujeita a restrição. | RangeBounds |  |
| uom | Unidades de medida utilizadas na restrição. | UnitOfMeasure |  |

\**7.3.1.4. Limites da gama (RangeBounds)**

Os valores-limite de início e fim de uma gama numérica (por exemplo, início ≥ 50, fim ≤ 99).

\**Atributos do tipo de dados “RangeBounds”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| startComparison | O comparador utilizado para o limite inferior da gama de valores (por exemplo, “greaterThanOrEqualTo”). | ComparisonOperatorValue |  |
| rangeStart | O limite inferior da gama de valores. | Real |  |
| endComparison | O comparador utilizado para o limite superior da gama de valores (por exemplo, “lessThan”). | ComparisonOperatorValue |  |
| rangeEnd | O limite superior da gama de valores. | Real |  |

\**7.3.1.5. Restrição escalar (ScalarConstraint)**

Uma restrição numérica escalar relativa a uma propriedade, por exemplo, “comprimento ≥ 1 m”.

Este tipo é um subtipo de “Constraint”.

\**Atributos do tipo de dados “ScalarConstraint”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| value | O valor numérico da propriedade sujeita a restrição. | Real |  |
| comparison | O comparador a utilizar na restrição, por exemplo, “greaterThan” | ComparisonOperatorValue |  |
| uom | Unidades de medida utilizadas na restrição. | UnitOfMeasure |  |

\**7.3.1.6. Outra restrição (OtherConstraint)**

Uma restrição que não é modelizada de uma forma estruturada, mas que pode ser descrita utilizando o atributo “description” de texto livre.

Este tipo é um subtipo de “Constraint”.

\**Atributos do tipo de dados “OtherConstraint”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| description | Uma descrição da restrição. | CharacterString |  |

\**7.3.1.7. Medida estatística (StatisticalMeasure)**

Uma descrição de uma medida estatística, por exemplo, “daily maximum” (máximo diário).

\**Atributos do tipo de dados “StatisticalMeasure”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| label | Um título legível para as pessoas relativo à medida estatística. | CharacterString |  |
| statisticalFunction | Uma função estatística, por exemplo, média. | StatisticalFunctionTypeValue |  |
| aggregationTimePeriod | Uma gama temporal em que é calculada uma estatística, por exemplo, um dia, uma hora. | TM_Duration |  |
| aggregationLength | Uma gama espacial unidimensional na qual é calculada uma estatística, por exemplo, 1 metro. | Length |  |
| aggregationArea | Um gama espacial bidimensional na qual é calculada uma estatística, por exemplo, 1 metro quadrado. | Area |  |
| aggregationVolume | Uma gama espacial tridimensional na qual é calculada uma estatística, por exemplo, 1 metro cúbico. | Volume |  |
| otherAggregation | Qualquer outro tipo de agregação. | Any |  |

\**Associações do tipo de dados “StatisticalMeasure”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| derivedFrom | Uma medida estatística pode ser derivada de outra, por exemplo, as temperaturas máximas mensais podem ser derivadas das temperaturas médias diárias. | StatisticalMeasure |  |

\**7.3.2. Enumerações**

\**7.3.2.1. Operador de comparação (ComparisonOperatorValue)**

Uma enumeração de operadores de comparação (por exemplo, superior a)

\**Valores para a enumeração “ComparisonOperatorValue”**

| Valor | Definição |
|---|---|
| equalTo | exatamente igual a |
| notEqualTo | não exatamente igual a |
| lessThan | inferior a |
| greaterThan | superior a |
| lessThanOrEqualTo | inferior a ou exatamente igual a |
| greaterThanOrEqualTo | superior a ou exatamente igual a |

\**7.3.3. Listas de códigos**

\**7.3.3.1. Tipo de fenómeno (PhenomenonTypeValue)**

Uma lista de códigos de fenómenos (por exemplo, temperatura, velocidade do vento).

Os valores autorizados para esta lista de códigos incluem os valores constantes das listas de códigos seguintes ou de outras listas de códigos definidas pelos fornecedores de dados:

— Nomes padronizados de previsões e fenómenos climáticos (CFStandardNamesValue) Definições de fenómenos observados em meteorologia e oceanografia, conforme especificado no ponto 4.5 do presente anexo.

— Nome do parâmetro do elemento do perfil (ProfileElementParameterNameValue) Propriedades que podem ser observadas para caracterizar o elemento do perfil, conforme especificado no ponto 0 do anexo IV.

— Nome do parâmetro do objeto derivado do solo (SoilDerivedObjectParameterNameValue): Propriedades relacionadas com o solo que podem ser derivadas de dados sobre o solo e de outros dados, conforme especificado no ponto 0 do anexo IV.

— Nome do parâmetro do perfil do solo (SoilProfileParameterNameValue): Propriedades que podem ser observadas para caracterizar o perfil do solo, conforme especificado no ponto 0 do anexo IV.

— Nome do parâmetro do sítio no solo (SoilSiteParameterNameValue): Propriedades que podem ser observadas para caracterizar o sítio no solo, conforme especificado no ponto 0 do anexo IV.

— Componente de referência da qualidade do ar da UE (EU_AirQualityReferenceComponentValue): Definições de fenómenos relativos à qualidade do ar no contexto da comunicação de informações ao abrigo da legislação da União, conforme especificado no ponto 0 do anexo IV.

— WMO GRIB Code and Flags Table 4.2 da Organização Meteorológica Mundial (GRIB_CodeTable4_2Value): Definições de fenómenos observados em meteorologia, conforme especificado no ponto 0 do anexo IV.

— Utilização do parâmetro BODC P01 (BODC_P01ParameterUsageValue): Definições de fenómenos observados em oceanografia, conforme especificado no ponto 0 do anexo IV.

\**7.3.3.2. Tipo de função estatística (StatisticalFunctionTypeValue)**

Uma lista de códigos de funções estatísticas (por exemplo, máximo, mínimo, média).

Os valores autorizados para esta lista de códigos incluem eventuais valores definidos pelos fornecedores de dados.

\**7.4. Observações especializadas**

\**7.4.1. Tipos de objetos geográficos**

O pacote “Observações Especializadas” contém os seguintes tipos de objetos geográficos:

— Observação de quadrícula

— Observação de séries de quadrículas

— Observação de pontos

— Coleção de observações de pontos

— Observação multipontos

— Observação de séries temporais de pontos

— Observação do perfil

— Observação da trajetória

\**7.4.1.1. Observação de quadrículas (GridObservation)**

Observação que representa um campo em quadrículas num único instante temporal.

Este tipo é um subtipo de “SamplingCoverageObservation”.

\**Restrições do tipo de objeto geográfico “GridObservation”**

A “featureOfInterest” deve ser um “SF_SamplingSolid” ou “SF_SamplingSurface”.

O “phenomenonTime” deve ser um “TM_Instant”.

O “result” deve ser uma “RectifiedGridCoverage” ou “RefererencableGridCoverage”.

\**7.4.1.2. Observação de séries de quadrículas (GridSeriesObservation)**

Observação que representa um campo em quadrículas em evolução numa sucessão de instantes temporais.

Este tipo é um subtipo de “SamplingCoverageObservation”.

\**Restrições do tipo de objeto geográfico “GridSeriesObservation”**

A “featureOfInterest” deve ser um “SF_SamplingSolid”.

O “phenomenonTime” deve ser um “TM_Period”.

O “result” deve ser uma “RectifiedGridCoverage” ou “ReferenceableGridCoverage”.

\**7.4.1.3 Observação de pontos (PointObservation)**

Observação que representa uma medição de uma propriedade num único ponto no tempo e no espaço.

Este tipo é um subtipo de “SamplingCoverageObservation”.

\**Restrições do tipo de objeto geográfico “PointObservation”**

A “featureOfInterest” deve ser um “SF_SamplingPoint”.

O “phenomenonTime” deve ser um “TM_Instant”.

\**7.4.1.4. Coleção de observações de pontos (PointObservationCollection)**

Uma coleção de observações de pontos.

Este tipo é um subtipo de “ObservationSet”.

\**Restrições do tipo de objeto geográfico “PointObservationCollection”**

Cada membro deve uma “PointObservation”.

\**7.4.1.5. Observação multipontos (MultiPointObservation)**

Observação que representa um conjunto de medições todas elas efetuadas exatamente ao mesmo tempo mas em diferentes locais.

Este tipo é um subtipo de “SamplingCoverageObservation”.

\**Restrições do tipo de objeto geográfico “MultiPointObservation”**

A “featureOfInterest” dever ser uma “SF_SamplingCurve”, “SF_SamplingSurface” ou “SF_SamplingSolid”.

O “phenomenonTime” deve ser um “TM_Instant”.

O “result” deve ser uma “MultiPointCoverage”.

\**7.4.1.6. Observação de séries temporais de pontos (PointTimeSeriesObservation)**

Observação que representa uma série temporal de medições de pontos de uma propriedade num local fixo no espaço.

Este tipo é um subtipo de “SamplingCoverageObservation”.

\**Restrições do tipo de objeto geográfico “PointTimeSeriesObservation”**

A “featureOfInterest” deve ser um “SF_SamplingPoint”.

O “phenomenonTime” deve ser um “TM_Period”.

O “result” deve ser uma “Timeseries”.

\**7.4.1.7. Observação do perfil (ProfileObservation)**

Observação que representa a medição de uma propriedade ao longo de um perfil vertical no espaço num único instante temporal.

Este tipo é um subtipo de “SamplingCoverageObservation”.

\**Restrições do tipo de objeto geográfico “ProfileObservation”**

A “featureOfInterest” deve ser uma “SF_SamplingCurve”

O “phenomenonTime” deve ser um “TM_Instant”.

O “result” deve ser uma “ReferenceableGridCoverage” ou “RectifiedGridCoverage”.

O domínio espacial do resultado deve conter um eixo que deve ser vertical.

\**7.4.1.8. Observação da trajetória (TrajectoryObservation)**

Observação que representa a medição de uma propriedade ao longo de uma curva sinuosa no tempo e no espaço.

Este tipo é um subtipo de “SamplingCoverageObservation”.

\**Restrições do tipo de objeto geográfico “TrajectoryObservation”**

O “phenomenonTime” deve ser um “TM_Period”.

O “result” deve ser uma “Timeseries”.

Cada ponto no “result” deve ser uma “TimeLocationValueTriple”.

A “featureOfInterest” deve ser uma “SF_Sampling Curve”.

\**7.4.2. Tipos de dados**

\**7.4.2.1. Tríade de tempo, local e valor (TimeLocationValueTriple)**

Um conjunto triplo de tempo, local e valor (medição). Por exemplo, num ponto ao longo de uma trajetória.

Este tipo é um subtipo de “TimeValuePair”.

\**Atributos do tipo de dados “TimeLocationValueTriple”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| location | Localização geográfica em que o valor é válido. | GM_Position |  |

\**7.5. Requisitos para observações**

Quando o tipo “OM_Observation”, ou qualquer subtipo deste, é utilizado para disponibilizar dados, são aplicáveis os seguintes requisitos:

(1) O tipo “Process” deve ser utilizado para indicar o procedimento utilizado numa “OM_Observation”.

(2) Quando é feita referência a uma “EnvironmentalMonitoringFacility” a partir de uma “OM_Observation”, deve ser fornecido um atributo “parameter”, cujo atributo “name” é “relatedMonitoringFeature” e cujo atributo “value” é do tipo “AbstractMonitoringFeature”.

(3) Para todas as codificações utilizadas para a totalidade ou parte de um resultado “OM_Observation”, deve estar disponível uma Interface de Programação de Aplicações (Application Programming Interface - API) para ler o ficheiro codificado. A referida API deve ser capaz de expor a informação necessária para realizar objetos geográficos INSPIRE.

(4) Se estiver presente o atributo “processParameter” na propriedade “procedure” de um objeto de “OM_Observation”, o seu valor (um nome) deve ser incluído no atributo “parameter” do objeto “OM_Observation”.

\**8. MODELO DE COMPLEXO DE ATIVIDADES**

O modelo de complexo de atividades INSPIRE contém o pacote “Complexo de Atividades” (Activity Complex).

\**8.1. Complexo de atividades**

\**8.1.1. Tipos de objetos geográficos**

O pacote “Complexo de Atividades” contém o tipo de objeto geográfico “Complexo de Atividades”.

\**8.1.1.1. Complexo de atividades (ActivityComplex)**

Uma unidade única, tanto do ponto de vista técnico como económico, sob o controlo da gestão de uma entidade jurídica (operador), abrangendo atividades como as enumeradas na Classificação NACE do Eurostat estabelecida pelo Regulamento (CE) n.º 1893/2006 do Parlamento Europeu e do Conselho (1). O “Complexo de Atividades” deve representar a totalidade da área, na mesma ou em diferentes localizações geográficas, gerida pelo mesmo operador, incluindo todas as infraestruturas, equipamentos e materiais.

\**Atributos do tipo de objeto geográfico “ActivityComplex”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| thematicId | Identificador temático do complexo de atividades. | ThematicIdentifier |  |
| geometry | A geometria utilizada para definir a extensão ou posição do complexo de atividades. | GM_Object |  |
| function | Atividades realizadas pelo complexo de atividades. A função é descrita pela atividade e potencialmente complementada com informações sobre as entradas (inputs) e saídas (outputs) que daí resultam. | Function |  |
| name | Nome descritivo do complexo de atividades. | CharacterString | voidable |
| validFrom | O momento em que o complexo de atividades começou a existir no mundo real. | DateTime | voidable |
| validTo | O momento em que o complexo de atividades deixou de existir no mundo real. | DateTime | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

\**8.1.2. Tipos de dados**

\**8.1.2.1. Função (Function)**

A função de algo expressa como uma atividade e informação opcional de entrada e/ou saída.

\**Atributos do tipo de dados “Function”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| activity | Descrição categorizada de um conjunto individual ou organizado de processos tecnicamente relacionados que são executados por uma unidade económica, privada ou pública, com ou sem fins lucrativos. | EconomicActivityValue |  |
| input | Qualquer material classificado ou registado que entra numa unidade técnica e económica de acordo com a sua função. | InputOutputValue | voidable |
| output | Qualquer material classificado ou registado que sai de uma unidade técnica e económica de acordo com a sua função. | InputOutputValue | voidable |
| description | Uma descrição mais detalhada da função. | PT_FreeText | voidable |

\**8.1.2.2. Capacidade (Capacity)**

A quantificação de um capacidade real ou potencial para desenvolver uma atividade, que geralmente não se altera, não se altera frequentemente ou não se altera de modo significativo.

\**Atributos do tipo de dados “Capacity”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| activity | Descrição categorizada de um conjunto individual ou organizado de processos tecnicamente relacionados que são executados por uma unidade económica, privada ou pública, com ou sem fins lucrativos. | EconomicActivityValue |  |
| input | Informação mensurável sobre qualquer material classificado ou registado que entra numa unidade técnica e económica de acordo com a sua função. | InputOutputAmount |  |
| output | Informação mensurável sobre qualquer material classificado ou registado que sai de uma unidade técnica e económica de acordo com a sua função. | InputOutputAmount |  |
| time | Período de tempo a que se refere a capacidade especificada, como 1 ano para uma capacidade anual. | TM_Duration |  |
| description | Uma descrição da capacidade. | PT_FreeText | voidable |

\**8.1.2.3. Quantidade de entradas ou saídas (InputOutputAmount)**

Tipo e, quando disponível, quantidade mensurável de um material classificado ou registado que entra ou sai de uma unidade técnica e económica.

\**Atributos do tipo de dados “InputOutputAmount”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inputOutput | Material classificado ou registado que entra ou sai de uma unidade técnica e económica de acordo com a sua função. | InputOutputValue |  |
| amount | Quantidade (como um volume ou massa) do material classificado ou registado que entra ou sai de uma unidade técnica e económica. | Measure | voidable |

\**8.1.2.4. Permissão (Permission)**

Decisão oficial (consentimento formal) que concede autorização para operar a totalidade ou parte de um “Complexo de Atividades”, sujeita a determinadas condições que garantem que as instalações ou partes das instalações situadas no mesmo sítio e operadas pelo mesmo operador cumprem os requisitos estabelecidos por uma autoridade competente. Uma permissão pode abranger uma ou mais funções e fixar parâmetros de capacidade. O termo poderia ser alargado a outros tipos de certificados ou documentos de especial relevância em função do âmbito de aplicação (por exemplo, ISO, EMAS, normas nacionais de qualidade, etc.).

\**Atributos do tipo de dados “Permission”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| id | Referência que identifica a permissão. | ThematicIdentifier |  |
| relatedParty | Partes relacionadas com a permissão concedida ao complexo de atividades aberto a numerosas funções diferentes, nomeadamente autoridades competentes ou empresas | RelatedParty | voidable |
| decisionDate | Referência temporal que complementa a definição da permissão. | DateTime | voidable |
| dateFrom | Uma data a partir da qual a permissão é aplicável e válida. | DateTime | voidable |
| dateTo | Uma data até à qual a permissão é aplicável e válida. | DateTime | voidable |
| description | Uma descrição da permissão. | PT_FreeText | voidable |
| permittedFunction | Função ou funções para as quais é concedida a permissão. | Function | voidable |
| permittedCapacity | Quantidades máximas de entradas e/ou saídas da atividade, em conformidade com a permissão. | Capacity | voidable |

\**8.1.2.5. Descrição do complexo de atividades (ActivityComplexDescription)**

Informação adicional sobre um complexo de atividades, incluindo a sua descrição, endereço, dados de contacto e partes relacionadas.

\**Atributos do tipo de objeto geográfico “ActivityComplexDescription”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| description | Uma definição complementar de “Complexo de Atividades” e suas características. | PT_FreeText | voidable |
| address | Um endereço para o complexo de atividades, ou seja, um endereço onde se realizam as atividades. | AddressRepresentation | voidable |
| contact | Informação de contacto para o complexo de atividades. | Contact | voidable |
| relatedParty | Informação de partes relacionadas com o “Complexo de Atividades”. Está aberta a muitas funções diferentes, como detentores de dados, operadores ou autoridades competentes. | RelatedParty | voidable |

\**8.1.3. Listas de códigos**

\**8.1.3.1. Atividade económica (EconomicActivityValue)**

Classificação das atividades económicas.

Os valores autorizados para esta lista de códigos incluem os valores constantes das listas de códigos seguintes ou de outras listas de códigos especificadas pelos fornecedores de dados:

— Classificação das Atividades Económicas da UE (EconomicActivityNACEValue): Atividades económicas de acordo com os valores da Classificação NACE do Eurostat, tal como estabelecidas no Regulamento (CE) n.º 1893/2006 do Parlamento Europeu e do Conselho (2).

— Classificação da UE de estatísticas das atividades económicas no setor dos resíduos (EconomicActivityWasteStatisticsValue): Classificação das atividades económicas de acordo com o anexo I, Secção 8, do Regulamento (CE) n.º 2150/2002 (3)

— Classificação da UE relativa à Eliminação e Valorização de Resíduos (WasteRecoveryDisposalValue): Classificação das operações de valorização e eliminação de resíduos de acordo com os anexos I e II da Diretiva 2008/98/CE do Parlamento Europeu e do Conselho (4).

\**8.1.3.2. Entradas ou saídas (InputOutputValue)**

Classificação das entradas ou saídas.

Os valores autorizados para esta lista de códigos incluem os valores constantes das listas de códigos seguintes ou de outras listas de códigos especificadas pelos fornecedores de dados.

— Classificação de Produtos da UE (ProductCPAValue): Classificação de Produtos por Atividade Económica de acordo com o Regulamento (CE) n.º 451/2008 do Parlamento Europeu e do Conselho (5).

— Classificação de Resíduos da UE (WasteValue): Classificação dos Resíduos de acordo com a Decisão 2000/532/CE (6).

\**8.2. Requisitos para “Complexos de Atividades”**

Se um fornecedor de dados utilizar um subtipo de “ActivityComplex” para disponibilizar informações sobre o estatuto, a capacidade física, as permissões e/ou informações adicionais, devem ser utilizadas as listas de códigos e os tipos de dados relevantes (“ConditionOfFacilityValue”, “Capacity”, “Permission”, “ActivityComplexDescription”) incluídos no pacote “Complexo de Atividades”.»

(1)

JO L 393 de 30.12.2006, p. 1.

(2)

JO L 393 de 30.12.2006, p. 1.

(3)

JO L 332 de 9.12.2002, p. 1.

(4)

JO L 312 de 22.11.2008, p. 3.

(5)

JO L 145 de 4.6.2008, p. 65.

(6)

JO L 226 de 6.9.2000, p. 3.
