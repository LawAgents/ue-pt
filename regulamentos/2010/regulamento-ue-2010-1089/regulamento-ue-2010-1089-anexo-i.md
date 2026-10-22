---
id: "regulamento-ue-2010-1089-anexo-i"
celex: "32010R1089"
title: "Regulamento (UE) n. ° 1089/2010 da Comissão, de 23 de Novembro de 2010 , que estabelece as disposições de execução da Directiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Anexo I"
type: "Regulamento"
number: "1089/2010"
year: 2010
date: 2010-11-23
status: "em vigor"
text_version: "consolidado"
last_amended: 2023-11-19
consolidated_celex: "02010R1089-20231119"
source: "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:02010R1089-20231119"
eli: "http://data.europa.eu/eli/reg/2010/1089/oj"
retrieved: 2026-10-21
legal_notice: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
part_of: "regulamento-ue-2010-1089"
part: "Anexo I"
---

# Regulamento (UE) n. ° 1089/2010 da Comissão, de 23 de Novembro de 2010 , que estabelece as disposições de execução da Directiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Anexo I

## Anexo I

**Tipos Comuns, Definições e Requisitos**

**1. TIPOS DEFINIDOS EM NORMAS EUROPEIAS E INTERNACIONAIS**

Os seguintes tipos comuns, utilizados em atributos ou associações de tipos de objetos geográficos ou de tipos de dados, são definidos do seguinte modo:

(1) Para os tipos «Any», «Angle», «Area», «Boolean», «CharacterString», «Date», «DateTime», «Decimal», «Distance», «Integer», «Length», «Measure», «Number», «Probability», «Real», «RecordType», «Sign», «UnitOfMeasure», «Velocity» e «Volume», são aplicáveis as definições estabelecidas na norma ISO/TS 19103:2005.

(2) Para os tipos «DirectPosition», «GM_Boundary», «GM_Curve», «GM_MultiCurve», «GM_MultiSurface», «GM_Object», «GM_Point», «GM_Position», «GM_Primitive», «GM_Solid», «GM_Surface» e «GM_Tin»“, são aplicáveis as definições estabelecidas na norma EN ISO 19107:2005.

(3) Para os tipos «TM_Duration», «TM_GeometricPrimitive», «TM_Instant», «TM_Object», «TM_Period» e «TM_Position», são aplicáveis as definições estabelecidas na norma EN ISO 19108:2005/AC:2008.

(4) Para o tipo «GF_PropertyType», são aplicáveis as definições estabelecidas na norma EN ISO 19109:2006.

(5) Para os tipos «CI_Citation», «CI_Date», «CI_RoleCode», «EX_Extent», «EX_VerticalExtent», «MD_Distributor», «MD_Resolution» e «URL», são aplicáveis as definições estabelecidas na norma EN ISO 19115:2005/AC:2008.

(6) Para o tipo «CV_SequenceRule», são aplicáveis as definições estabelecidas na norma EN ISO 19123:2007.

(7) Para o tipo «AbstractFeature», são aplicáveis as definições estabelecidas na norma EN ISO 19136:2009.

(8) Para os tipos «LocalisedCharacterString», «PT_FreeText» e «URI» são aplicáveis as definições estabelecidas na norma CEN ISO/TS 19139:2009.

(9) Para o tipo «LC_LandCoverClassificationSystem», são aplicáveis as definições estabelecidas na norma ISO 19144-2:2012.

(10) Para os tipos «GFI_Feature», «Location», «NamedValue», «OM_Observation», «OM_Process», «SamplingCoverageObservation», «SF_SamplingCurve», «SF_SamplingPoint», «SF_SamplingSolid», «SF_SamplingSurface» e «SF_SpatialSamplingFeature», são aplicáveis as definições estabelecidas na norma ISO 19156:2011.

(11) Para os tipos «Category», «Quantity», «QuantityRange» e «Time», são aplicáveis as definições estabelecidas em Robin, Alexandre (ed.), OGC®SWE Common Data Model Encoding Standard, version 2.0.0, Open Geospatial Consortium, 2011.

(12) Para os tipos «TimeValuePair» e «Timeseries», são aplicáveis as definições estabelecidas em Taylor, Peter (ed.), OGC® WaterML 2.0: Part 1 — Timeseries, version 2.0.0, Open Geospatial Consortium, 2012.

(13) Para os tipos «CGI_LinearOrientation» e «CGI_PlanarOrientation», são aplicáveis as definições estabelecidas em CGI Interoperability Working Group, Geoscience Markup Language (GeoSciML), version 3.0.0, Commission for the Management and Application of Geoscience Information (CGI) of the International Union of Geological Sciences, 2011.

**2. TIPOS DE DADOS COMUNS**

**2.1. Identificador (Identifier)**

Identificador de objecto externo único publicado pela entidade responsável, que pode ser utilizado por aplicações externas para referenciar o objecto geográfico.

**Atributos do tipo de dados «Identifier»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| localId | Identificador local, atribuído pelo fornecedor de dados. O identificador local é único no espaço de nomes, ou seja nenhum outro objecto geográfico tem o mesmo identificador único. | CharacterString |  |
| namespace | Espaço de nomes que identifica de forma única a fonte de dados do objecto geográfico. | CharacterString |  |
| versionId | Identificador da versão específica do objecto geográfico, com um comprimento máximo de 25 caracteres. Se a especificação de um tipo de objecto geográfico com um identificador de objecto externo incluir a informação do ciclo de vida, o identificador da versão é utilizado para distinguir as diferentes versões de um objecto geográfico. No conjunto de todas as versões de um objecto geográfico, o identificador da versão é único. | CharacterString | voidable |

—————

**2.2. Parte relacionada (RelatedParty)**

Uma organização ou pessoa com uma função relacionada com um recurso.

**Atributos do tipo de dados «RelatedParty»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| individualName | Nome da pessoa relacionada. | PT_FreeText | voidable |
| organisationName | Nome da organização relacionada. | PT_FreeText | voidable |
| positionName | Posição da parte em relação a um recurso, como, por exemplo, chefe de departamento. | PT_FreeText | voidable |
| contact | Referências de contacto da parte relacionada. | Contact | voidable |
| role | Funções da parte em relação a um recurso, como, por exemplo, detentor. | PartyRoleValue | voidable |

**Restrições do tipo de dados «RelatedParty»**

Deve ser fornecido, pelo menos, o nome da pessoa, organização ou cargo.

**2.3. Contacto (Contact)**

Os canais de comunicação através dos quais é possível aceder a uma pessoa ou a algo.

**Atributos do tipo de dados «Contact»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| address | Um endereço fornecido sob a forma de texto livre. | AddressRepresentation | voidable |
| contactInstructions | Instruções suplementares sobre como e quando contactar uma pessoa ou organização. | PT_FreeText | voidable |
| electronicMailAddress | Um endereço de correio eletrónico da organização ou da pessoa. | CharacterString | voidable |
| hoursOfService | Os períodos de tempo em que a organização ou a pessoa pode ser contactada. | PT_FreeText | voidable |
| telephoneFacsimile | Número de fax da organização ou da pessoa. | CharacterString | voidable |
| telephoneVoice | Número de telefone da organização ou da pessoa. | CharacterString | voidable |
| website | Páginas disponibilizadas na Internet pela organização ou pela pessoa. | URL | voidable |

**2.4. Citação do documento (DocumentCitation)**

Citação para fins de referenciação de um documento de forma inequívoca.

**Atributos do tipo de dados «DocumentCitation»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| name | Nome do documento. | CharacterString |  |
| shortName | Nome abreviado ou título alternativo do documento. | CharacterString | voidable |
| date | Data de criação, publicação ou revisão do documento. | CI_Date | voidable |
| link | Ligação a uma versão em linha do documento | URL | voidable |
| specificReference | Referência a uma parte específica do documento | CharacterString | voidable |

**2.5. Citação da legislação (LegislationCitation)**

Citação para fins de referenciação inequívoca de um ato jurídico ou de uma parte específica de um ato jurídico.

Este tipo é um subtipo de «DocumentCitation».

**Atributos do tipo de dados «LegislationCitation»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| identificationNumber | Código utilizado para identificar o instrumento legislativo | CharacterString |  |
| officialDocumentNumber | Número do documento oficial utilizado para identificar de forma única o instrumento legislativo. | CharacterString |  |
| dateEnteredIntoForce | Data em que o instrumento legislativo entrou em vigor. | TM_Position |  |
| dateRepealed | Data em que o instrumento legislativo foi revogado. | TM_Position |  |
| level | O nível a que é adotado o instrumento legislativo. | LegislationLevelValue |  |
| journalCitation | Citação do jornal oficial em que está publicada a legislação. | OfficialJournalInformation |  |

**Restrições do tipo de dados «LegislationCitation»**

Se o atributo de ligação estiver vazio («void»), deve ser fornecida a citação do jornal oficial.

**2.6. Informação do Jornal Oficial (OfficialJournalInformation)**

Citação integral da localização do instrumento legislativo no jornal oficial.

**Atributos do tipo de dados «OfficialJournalInformation»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| officialJournalIdentification | Referência do jornal oficial em que foi publicado o instrumento legislativo. Esta referência deve ser constituída por três partes: <br> — Título do jornal oficial <br> — Volume e/ou número de série do jornal oficial <br> — Número da(s) página(s) | CharacterString |  |
| ISSN | O Número Internacional Normalizado das Publicações em Série (ISSN) é um número com oito dígitos que identifica a publicação periódica em que o instrumento legislativo foi publicado. | CharacterString |  |
| ISBN | O Número Internacional Normalizado do Livro (ISBN) é um número com nove dígitos que identifica de forma única o livro em que foi publicado o instrumento legislativo. | CharacterString |  |
| linkToJournal | Ligação a uma versão em linha do jornal oficial | URL |  |

**2.7. Identificador temático (ThematicIdentifier)**

Identificador temático para identificar de forma única o objeto geográfico.

**Atributos do tipo de dados «ThematicIdentifier»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| identifier | Identificador único utilizado para identificar o objeto geográfico no sistema de identificação especificado. | CharacterString |  |
| identifierScheme | Identificador que define o sistema utilizado para atribuir o identificador. | CharacterString |  |

—————

**4. LISTAS DE CÓDIGOS COMUNS**

**4.1. Posição vertical (VerticalPositionValue)**

A posição vertical relativa de um objeto geográfico.

**4.2. Estado da instalação (ConditionOfFacilityValue)**

O estado de uma instalação no que diz respeito à sua completude e utilização.

**4.3. Código do país (CountryCode)**

O código do país conforme definido no Código de Redação Interinstitucional publicado pelo Serviço das Publicações da União Europeia.

**4.4. Nível de legislação (LegislationLevelValue)**

O nível a que um ato jurídico ou convenção foi adotado.

**4.5. Função da parte (PartyRoleValue)**

Funções das partes relacionadas com um recurso ou responsáveis por esse recurso.

Os valores para esta lista de códigos incluem os valores constantes das listas de códigos seguintes ou de outras listas de códigos especificadas pelos fornecedores do dados.

— Código da função (CI_RoleCode): Funções desempenhadas por uma parte responsável.

— Função de uma parte relacionada (RelatedPartyRoleValue): Classificação das funções das partes relacionadas.

**4.6. Nomes padronizados de previsões e fenómenos climáticos (CFStandardNamesValue)**

Definições de fenómenos observados em meteorologia e oceanografia.

**4.7. Sexo (GenderValue)**

O sexo de uma pessoa ou grupo de pessoas.

**5. GENERIC NETWORK MODEL**

**5.1. Tipos de objectos geográficos**

**5.1.1. Referência cruzada (CrossReference)**

Representa uma referência entre dois elementos na mesma rede.

**Associações do tipo de objecto geográfico «CrossReference»**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| element | Os elementos que são objecto de uma referência cruzada. | NetworkElement |  |

**5.1.2. Segmento generalizado (GeneralisedLink)**

Tipo de base abstracto que representa um elemento linear da rede que pode ser utilizado como alvo na referenciação linear.

Este tipo é um subtipo de «NetworkElement».

Este tipo é abstracto.

**5.1.3. Cruzamento em níveis distintos (GradeSeparatedCrossing)**

Indicador de qual ou quais de dois ou mais elementos de intersecção se encontra(m) num nível superior e num nível inferior, a utilizar se as coordenadas de altitude não estiverem presentes ou não forem fiáveis.

Este tipo é um subtipo de «NetworkElement».

**Associações do tipo de objecto geográfico «GradeSeparatedCrossing»**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| element | Sequência de segmentos de cruzamento. A ordem em que são referidas reflecte a sua altitude; o primeiro segmento é o segmento a mais baixa altitude. | Link |  |

**5.1.4. Segmento (Link)**

Elemento curvilíneo da rede que liga duas posições e representa um trajecto homogéneo na rede. As posições ligadas podem ser representadas como nós.

Este tipo é um subtipo de «GeneralisedLink».

Este tipo é abstracto.

**Atributos do tipo de objecto geográfico «Link»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| centrelineGeometry | Geometria que representa o eixo do segmento. | GM_Curve |  |
| fictitious | Indicador de que a geometria do eixo do segmento é uma linha recta sem pontos de controlo intermédios – a não ser que a linha recta represente adequadamente a geografia na resolução do conjunto de dados. | Boolean |  |

**Associações do tipo de objecto geográfico «Link»**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| endNode | Nó final opcional para este segmento. O nó final pode ser a mesma instância do nó de início. | Node |  |
| startNode | Nó de início opcional para este segmento. | Node |  |

**5.1.5. Sequência de segmentos (LinkSequence)**

Um elemento da rede que representa um trajecto contínuo na rede sem quaisquer ramificações. O elemento tem um início e um fim definidos e cada posição na sequência de segmentos é identificável com um parâmetro único, como o comprimento.

Este tipo é um subtipo de «GeneralisedLink».

Este tipo é abstracto.

**Atributos do tipo de objecto geográfico «LinkSequence»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| link | Colecção ordenada de segmentos direccionados que constituem a sequência de segmentos. | DirectedLink |  |

**5.1.6. Conjunto de segmentos (LinkSet)**

Uma colecção de sequências de segmentos e/ou de segmentos individuais que tem uma função ou significado específico numa rede.

Este tipo é um subtipo de «NetworkElement».

Este tipo é abstracto.

**Associações do tipo de objecto geográfico «LinkSet»**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| link | Conjunto de segmentos e de sequências de segmentos que constituem o conjunto de segmentos. | GeneralisedLink |  |

**5.1.7. Rede (Network)**

Uma rede é uma colecção de elementos de rede.

**Atributos do tipo de objecto geográfico «Network»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geographicalName | Topónimo da rede em causa. | GeographicalName | voidable |

**Associações do tipo de objecto geográfico «Network»**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| elements | A colecção de elementos que constitui a rede. | NetworkElement |  |

**5.1.8. Área da rede (NetworkArea)**

Um elemento bidimensional numa rede.

Este tipo é um subtipo de «NetworkElement».

Este tipo é abstracto.

**Atributos do tipo de objecto geográfico «NetworkArea»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Representa as propriedades geométricas da área. | GM_Surface |  |

**5.1.9. Conexão de rede (NetworkConnection)**

Representa uma conexão lógica entre dois ou mais elementos de rede em diferentes redes.

Este tipo é um subtipo de «NetworkElement».

Atributos do tipo de objecto geográfico «NetworkConnection»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| type | Categorização da conexão de rede. | ConnectionTypeValue | voidable |

Associações do tipo de objecto geográfico «NetworkConnection»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| element | Elementos de rede em diferentes redes. | NetworkElement |  |

Restrições do tipo de objecto geográfico «NetworkConnection»

Todos os elementos têm de estar em redes diferentes.

**5.1.10. Elemento de rede (NetworkElement)**

Tipo de base abstracto que representa um elemento numa rede. Todos os elementos de uma rede desempenham alguma função que é de interesse na rede.

Este tipo é abstracto.

**Atributos do tipo de objecto geográfico «NetworkElement»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifespanVersion | Data e hora em que esta versão do objecto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objecto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| inspireId | Identificador de objecto externo do objecto geográfico. | Identifier |  |

**Associações do tipo de objecto geográfico «NetworkElement»**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| inNetwork | As redes de que um elemento de rede faz parte. | Network | voidable |

**5.1.11. Propriedade da rede (NetworkProperty)**

Tipo de base abstracto que representa fenómenos localizados num elemento da rede ou ao longo deste. Este tipo de base apresenta propriedades gerais para associar os fenómenos relacionados com a rede (propriedades da rede) aos elementos da rede.

Este tipo é abstracto.

**Atributos do tipo de objecto geográfico «NetworkProperty»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifespanVersion | Data e hora em que esta versão do objecto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objecto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| inspireId | Identificador de objecto externo do objecto geográfico. | Identifier |  |
| networkRef | Referência geográfica da propriedade relacionada com a rede. | NetworkReference | voidable |

**5.1.12. Nó (Node)**

Representa uma posição significativa na rede que ocorre sempre no início ou no final de um segmento.

Este tipo é um subtipo de «NetworkElement».

Este tipo é abstracto.

**Atributos do tipo de objecto geográfico «Node»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Localização do nó. | GM_Point |  |

**Associações do tipo de objecto geográfico «Node»**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| spokeEnd | Segmentos que entram no nó. | Link | voidable |
| spokeStart | Segmentos que saem do nó. | Link | voidable |

**5.2. Tipos de dados**

**5.2.1. Segmento direccionado (DirectedLink)**

Um segmento, tanto na sua direcção positiva como negativa.

**Atributos do tipo de dados «DirectedLink»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| direction | Indica se o segmento direccionado concorda (positiva) ou não (negativa) com a direcção positiva do segmento. | Sign |  |

**Associações do tipo de dados «DirectedLink»**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| link | O segmento. | Link |  |

**5.2.2. Referência do segmento (LinkReference)**

Uma referência de rede a um elemento linear de rede.

Este tipo é um subtipo de «NetworkReference».

Atributos do tipo de dados «LinkReference»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| applicableDirection | Direcções do segmento generalizado a que se aplica a referência. Nos casos em que uma propriedade não se aplica a uma direcção ao longo de um segmento, mas representa um fenómeno ao longo de um segmento, «inDirection» refere-se ao lado direito na direcção do segmento. | LinkDirectionValue | voidable |

Restrições do tipo de dados «LinkReference»

Os alvos de referências lineares devem ser elementos lineares de rede. Ou seja, se for utilizada a referenciação linear ou se a direcção for relevante, o alvo da referência de rede deve ser um segmento ou uma sequência de segmentos.

**5.2.3. Referência de rede (NetworkReference)**

Uma referência a um elemento da rede.

**Associações do tipo de dados «NetworkReference»**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| element | Elemento de rede referenciado. | NetworkElement |  |

**5.2.4. Referência linear simples (SimpleLinearReference)**

Uma referência de rede que está limitada a uma parte de um elemento linear de rede. Essa parte é a parte do elemento de rede entre «fromPosition» e «toPosition».

Este tipo é um subtipo de «LinkReference».

**Atributos do tipo de dados «SimpleLinearReference»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| fromPosition | Posição de início do elemento linear, expressa como a distância desde o início do elemento linear de rede ao longo da sua geometria curva. | Length |  |
| offset | Desvio da geometria do eixo do segmento generalizado, quando aplicável; um desvio positivo é um desvio para a direita na direcção do segmento, um desvio negativo é um desvio para a esquerda. | Length | voidable |
| toPosition | Posição de fim do elemento linear, expressa como a distância desde o início do elemento linear de rede ao longo da sua geometria curva. | Length |  |

**5.2.5. Referência de ponto simples (SimplePointReference)**

Uma referência de rede que está limitada a um ponto num elemento linear de rede. O ponto é a localização no elemento da rede na posição «atPosition» ao longo da rede.

Este tipo é um subtipo de «LinkReference».

**Atributos do tipo de dados «SimplePointReference»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| atPosition | Posição do ponto, expressa como a distância desde o início do elemento linear de rede ao longo da sua geometria curva. | Length |  |
| offset | Desvio da geometria do eixo do segmento generalizado, quando aplicável; um desvio positivo é um desvio para a direita na direcção do segmento, um desvio negativo é um desvio para a esquerda. | Length | voidable |

**5.3. Listas de códigos**

**5.3.1. Tipo de conexão (ConnectionTypeValue)**

Tipos de conexões entre redes diferentes.

**5.3.2. Direção do segmento (LinkDirectionValue)**

Lista de valores para as direções em relação a um segmento.

**6. MODELO DE COBERTURA (COVERAGE MODEL)**

O modelo de cobertura INSPIRE consiste nos seguintes pacotes:

— Coberturas (Base) (Coverages (Base))

— Coberturas (Domínio e gama) (Coverages (Domain And Range))

**6.1. Coberturas (Base)**

**6.1.1. Tipos de objetos geográficos**

O pacote «Coberturas (Base)» contém o tipo de objeto geográfico «Cobertura».

6.1.1.1. Cobertura (Coverage)

Objeto geográfico que atua como uma função para fornecer valores da sua gama para qualquer posição direta dentro do seu domínio espacial, temporal ou espaciotemporal.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «Coverage»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| metadata | Metadados específicos da aplicação da cobertura. | Any |  |
| rangeType | Descrição da estrutura dos valores da gama. | RecordType |  |

**6.2. Coberturas (Domínio e gama)**

**6.2.1. Tipos de objetos geográficos**

O pacote «Coberturas (Domínio e Gama)» contém os seguintes tipos de objetos geográficos:

— Cobertura (Representação de domínio e gama) (Coverage (Domain And Range Representation))

— Cobertura de quadrícula retificada (Rectified Grid Coverage)

— Cobertura de quadrícula referenciável (Referenceable Grid Coverage)

6.2.1.1. Cobertura (Representação por domínio e gama) (CoverageByDomainAndRange)

Cobertura que fornece o domínio e a gama como propriedades separadas.

Este tipo é um subtipo de «Coverage».

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «CoverageByDomainAndRange»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| coverageFunction | Descrição do modo como podem ser obtidos os valores da gama em localizações no domínio de cobertura. | CoverageFunction |  |
| domainSet | Configuração do domínio da cobertura descrita em termos de coordenadas. | Any |  |
| rangeSet | Conjunto de valores associados por uma função aos elementos do domínio da cobertura. | Any |  |

Restrições do tipo de objeto geográfico «CoverageByDomainAndRange»

A função de quadrícula só é válida para domínios que são quadrículas.

6.2.1.2. Cobertura de quadrícula retificada (RectifiedGridCoverage)

Cobertura cujo domínio consiste numa quadrícula retificada.

Este tipo é um subtipo de «CoverageByDomainAndRange».

Restrições do tipo de objeto geográfico «RectifiedGridCoverage»

O domínio deve ser uma quadrícula retificada.

Os pontos da quadrícula de uma «RectifiedGridCoverage» devem coincidir com os centros das células das quadrículas geográficas definidas no ponto 2.2 do anexo II a qualquer nível de resolução.

6.2.1.3. Cobertura de quadrícula referenciável (ReferenceableGridCoverage)

Cobertura cujo domínio consiste numa quadrícula referenciável.

Este tipo é um subtipo de «CoverageByDomainAndRange».

Restrições do tipo de objeto geográfico «ReferenceableGridCoverage»

O domínio deve ser uma quadrícula referenciável.

**6.2.2. Tipos de dados**

6.2.2.1. Função de cobertura (CoverageFunction)

Descrição do modo como podem ser obtidos os valores da gama em localizações no domínio de cobertura.

Este tipo é um tipo de união.

Atributos do tipo de união «CoverageFunction»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| ruleDefinition | Uma descrição formal ou informal da função de cobertura como texto. | CharacterString |  |
| ruleReference | Uma descrição formal ou informal da função de cobertura como referência. | URI |  |
| gridFunction | Regra cartográfica para geometrias de quadrículas. | GridFunction |  |

6.2.2.2. Função da quadrícula (GridFunction)

Uma regra cartográfica explícita para geometrias de quadrículas.

Atributos do tipo de dados «GridFunction»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| sequenceRule | Descrição do modo como os pontos das quadrículas estão ordenados para associação aos elementos dos valores no conjunto de gamas de valores da cobertura. | CV_SequenceRule |  |
| startPoint | O ponto da quadrícula a associar ao primeiro registo no conjunto de gamas de valores da cobertura. | Integer |  |

**7. Modelo das observações (Observations Model)**

O modelo de observações INSPIRE consiste nos seguintes pacotes:

— Referências da observação (Observation References)

— Processos (Processes)

— Propriedades observáveis (Observable Properties)

— Observações especializadas (Specialised Observations)

**7.1. Referências da observação**

**7.1.1. Tipos de objetos geográficos**

O pacote «Referências da Observação» contém o tipo de objeto geográfico Conjunto de Observações».

7.1.1.1 Conjunto de observações (ObservationSet)

Liga um conjunto de observações.

Atributos do tipo de objeto geográfico «ObservationSet»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| extent | Informação sobre a extensão geográfica e temporal. | EX_Extent |  |

Associações do tipo de objeto geográfico «ObservationSet»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| member | Um membro do «ObservationSet». | OM_Observation |  |

**7.2. Processos**

**7.2.1. Tipos de objetos geográficos**

O pacote «Processos» contém o tipo de objeto geográfico «Process».

7.2.1.1. Processo (Process)

Descrição de um processo de observação.

Este tipo é um subtipo de «OM_Process».

Atributos do tipo de objeto geográfico «Process»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier | voidable |
| name | Nome do processo. | CharacterString | voidable |
| type | Tipo de processo. | CharacterString | voidable |
| documentation | Mais informações em linha/fora de linha (online/offline) associadas ao processo. | DocumentCitation | voidable |
| processParameter | Parâmetro que controla a aplicação do processo e, consequentemente, o seu resultado. | ProcessParameter | voidable |
| responsibleParty | Pessoa ou organização relacionada com o processo. | RelatedParty | voidable |

**7.2.2. Tipos de dados**

7.2.2.1. Parâmetro do processo (ProcessParameter)

Descrição de um determinado parâmetro

Atributos do tipo de dados «ProcessParameter»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| name | Nome do parâmetro do processo. | ProcessParameterNameValue |  |
| description | Descrição do parâmetro do processo. | CharacterString |  |

**7.2.3. Listas de códigos**

7.2.3.1. Nome do parâmetro do processo (ProcessParameterNameValue)

Uma lista de códigos dos nomes dos parâmetros do processo.

**7.3. Propriedades observáveis**

**7.3.1. Tipos de dados**

7.3.1.1. Restrição (Constraint)

Uma restrição sobre uma propriedade, por exemplo, comprimento de onda = 200 nm.

Atributos do tipo de dados «Constraint»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| constrainedProperty | A propriedade sujeita a restrição, por exemplo, «colour» se a restrição for «colour = blue». | PhenomenonTypeValue |  |
| label | Uma título legível para as pessoas relativo à restrição no seu conjunto. | CharacterString |  |

7.3.1.2. Restrição da categoria (CategoryConstraint)

Uma restrição baseada numa categoria de qualificação. Por exemplo, «colour = red».

Este tipo é um subtipo de «Constraint».

Atributos do tipo de dados «CategoryConstraint»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| comparison | Um operador de comparação. No caso de uma restrição de categoria deve ser «equalTo» ou «notEqualTo». | ComparisonOperatorValue |  |
| value | O valor da propriedade sujeita a restrição, por exemplo «blue» (se a propriedade sujeita a restrição for a cor). | CharacterString |  |

7.3.1.3. Restrição da gama (RangeConstraint)

Uma restrição da gama numérica sobre alguma propriedade, por exemplo, comprimento de onda ≥ 300 nm e comprimento de onda ≤ 600 nm.

Este tipo é um subtipo de «Constraint».

Atributos do tipo de dados «RangeConstraint»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| value | A gama numérica de valores da propriedade sujeita a restrição. | RangeBounds |  |
| uom | Unidades de medida utilizadas na restrição. | UnitOfMeasure |  |

7.3.1.4. Limites da gama (RangeBounds)

Os valores-limite de início e fim de uma gama numérica (por exemplo, início ≥ 50, fim ≤ 99).

Atributos do tipo de dados «RangeBounds»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| startComparison | O comparador utilizado para o limite inferior da gama de valores (por exemplo, «greaterThanOrEqualTo»). | ComparisonOperatorValue |  |
| rangeStart | O limite inferior da gama de valores. | Real |  |
| endComparison | O comparador utilizado para o limite superior da gama de valores (por exemplo, «lessThan»). | ComparisonOperatorValue |  |
| rangeEnd | O limite superior da gama de valores. | Real |  |

7.3.1.5. Restrição escalar (ScalarConstraint)

Uma restrição numérica escalar relativa a uma propriedade, por exemplo, «comprimento ≥ 1 m».

Este tipo é um subtipo de «Constraint».

Atributos do tipo de dados «ScalarConstraint»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| value | O valor numérico da propriedade sujeita a restrição. | Real |  |
| comparison | O comparador a utilizar na restrição, por exemplo, «greaterThan» | ComparisonOperatorValue |  |
| uom | Unidades de medida utilizadas na restrição. | UnitOfMeasure |  |

7.3.1.6. Outra restrição (OtherConstraint)

Uma restrição que não é modelizada de uma forma estruturada, mas que pode ser descrita utilizando o atributo «description» de texto livre.

Este tipo é um subtipo de «Constraint».

Atributos do tipo de dados «OtherConstraint»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| description | Uma descrição da restrição. | CharacterString |  |

7.3.1.7. Medida estatística (StatisticalMeasure)

Uma descrição de uma medida estatística, por exemplo, «daily maximum» (máximo diário).

Atributos do tipo de dados «StatisticalMeasure»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| label | Um título legível para as pessoas relativo à medida estatística. | CharacterString |  |
| statisticalFunction | Uma função estatística, por exemplo, média. | StatisticalFunctionTypeValue |  |
| aggregationTimePeriod | Uma gama temporal em que é calculada uma estatística, por exemplo, um dia, uma hora. | TM_Duration |  |
| aggregationLength | Uma gama espacial unidimensional na qual é calculada uma estatística, por exemplo, 1 metro. | Length |  |
| aggregationArea | Um gama espacial bidimensional na qual é calculada uma estatística, por exemplo, 1 metro quadrado. | Area |  |
| aggregationVolume | Uma gama espacial tridimensional na qual é calculada uma estatística, por exemplo, 1 metro cúbico. | Volume |  |
| otherAggregation | Qualquer outro tipo de agregação. | Any |  |

Associações do tipo de dados «StatisticalMeasure»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| derivedFrom | Uma medida estatística pode ser derivada de outra, por exemplo, as temperaturas máximas mensais podem ser derivadas das temperaturas médias diárias. | StatisticalMeasure |  |

7.3.1.8. Propriedade observável abstrata (AbstractObservableProperty)

Uma classe abstrata que representa uma propriedade (ou fenómeno) observável.

Este tipo é abstrato.

**Atributos do tipo de dados «AbstractObservableProperty»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| label | Um título legível para as pessoas relativo à propriedade observável. | CharacterString |  |

7.3.1.9. Propriedade observável composta (CompositeObservableProperty)

Uma composição de múltiplas propriedades observáveis.

Este tipo é um subtipo de «AbstractObservableProperty».

**Atributos do tipo de dados «CompositeObservableProperty»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| count | Número de componentes desta composição. | Integer |  |

**Associações do tipo de dados «CompositeObservableProperty»**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| component | Propriedades observáveis que, em conjunto, compõem a mesma propriedade observável, por exemplo, ventos U e V. | AbstractObservableProperty |  |

7.3.1.10. Propriedade observável (ObservableProperty)

Representa uma única propriedade observável, por exemplo «temperatura».

Este tipo é um subtipo de «AbstractObservableProperty».

**Atributos do tipo de dados «ObservableProperty»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| basePhenomenon | O fenómeno em que se baseia a descrição da propriedade observável. | PhenomenonTypeValue |  |
| uom | A unidade de medida. | UnitOfMeasure |  |

**Associações do tipo de dados «ObservableProperty»**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| restriction | Uma restrição aplicada à propriedade observável. | Constraint |  |
| statisticalMeasure | Medida estatística aplicada à propriedade observável, por exemplo «temperatura média diária». | StatisticalMeasure |  |

—————

**7.3.3. Listas de códigos**

7.3.3.1 Tipo de fenómeno (PhenomenonTypeValue)

Uma lista de códigos de fenómenos (por exemplo temperatura, velocidade do vento).

Esta lista de códigos inclui os valores constantes das listas de códigos seguintes ou de outras listas de códigos definidas pelos fornecedores dos dados:

— Nomes padronizados de previsões e fenómenos climáticos (CFStandardNamesValue): Definições de fenómenos observados em meteorologia e oceanografia, conforme especificado no ponto 4.5 do presente anexo.

— Nome do parâmetro do elemento do perfil (ProfileElementParameterNameValue): Propriedades que podem ser observadas para caracterizar o elemento do perfil, conforme especificado no ponto 3.3.8 do anexo IV.

— Nome do parâmetro do objeto derivado do solo (SoilDerivedObjectParameterNameValue): Propriedades relacionadas com o solo que podem ser derivadas de dados sobre o solo e de outros dados, conforme especificado no ponto 3.3.9 do anexo IV.

— Nome do parâmetro do perfil do solo (SoilProfileParameterNameValue): Propriedades que podem ser observadas para caracterizar o perfil do solo, conforme especificado no ponto 3.3.12 do anexo IV.

— Nome do parâmetro do sítio no solo (SoilSiteParameterNameValue): Propriedades que podem ser observadas para caracterizar o sítio no solo, conforme especificado no ponto 3.3.13 do anexo IV.

— Componente de referência da qualidade do ar da UE (EU_AirQualityReferenceComponentValue): Definições de fenómenos relativos à qualidade do ar no contexto da comunicação de informações ao abrigo da legislação da União, conforme especificado no ponto 13.2.1.1 do anexo IV.

— Quadro 4.2 de Códigos e Marcadores do formato GRIB da Organização Meteorológica Mundial (GRIB_CodeTable4_2Value): Definições de fenómenos observados em meteorologia, conforme especificado no ponto 13.2.1.2 do anexo IV.

— Utilização do parâmetro BODC P01 (BODC_P01ParameterUsageValue): Definições de fenómenos observados em oceanografia, conforme especificado no ponto 14.2.1.1 do anexo IV.

7.3.3.2. Tipo de função estatística (StatisticalFunctionTypeValue)

Uma lista de códigos de funções estatísticas (por exemplo, máximo, mínimo, média).

7.3.3.3 Operador de comparação (ComparisonOperatorValue)

Uma lista de códigos de operadores de comparação (por exemplo maior do que, menor do que, igual a).

**7.4. Observações especializadas**

**7.4.1. Tipos de objetos geográficos**

O pacote «Observações Especializadas» contém os seguintes tipos de objetos geográficos:

— Observação de quadrícula

— Observação de séries de quadrículas

— Observação de pontos

— Coleção de observações de pontos

— Observação multipontos

— Observação de séries temporais de pontos

— Observação do perfil

— Observação da trajetória

7.4.1.1. Observação de quadrículas (GridObservation)

Observação que representa um campo em quadrículas num único instante temporal.

Este tipo é um subtipo de «SamplingCoverageObservation».

Restrições do tipo de objeto geográfico «GridObservation»

A «featureOfInterest» deve ser um «SF_SamplingSolid» ou «SF_SamplingSurface».

O «phenomenonTime» deve ser um «TM_Instant».

O «result» deve ser uma «RectifiedGridCoverage» ou «RefererencableGridCoverage».

7.4.1.2. Observação de séries de quadrículas (GridSeriesObservation)

Observação que representa um campo em quadrículas em evolução numa sucessão de instantes temporais.

Este tipo é um subtipo de «SamplingCoverageObservation».

Restrições do tipo de objeto geográfico «GridSeriesObservation»

A «featureOfInterest» deve ser um «SF_SamplingSolid».

O «phenomenonTime» deve ser um «TM_Period».

O «result» deve ser uma «RectifiedGridCoverage» ou «ReferenceableGridCoverage».

7.4.1.3 Observação de pontos (PointObservation)

Observação que representa uma medição de uma propriedade num único ponto no tempo e no espaço.

Este tipo é um subtipo de «SamplingCoverageObservation».

Restrições do tipo de objeto geográfico «PointObservation»

A «featureOfInterest» deve ser um «SF_SamplingPoint».

O «phenomenonTime» deve ser um «TM_Instant».

7.4.1.4. Coleção de observações de pontos (PointObservationCollection)

Uma coleção de observações de pontos.

Este tipo é um subtipo de «ObservationSet».

Restrições do tipo de objeto geográfico «PointObservationCollection»

Cada membro deve uma «PointObservation».

7.4.1.5. Observação multipontos (MultiPointObservation)

Observação que representa um conjunto de medições todas elas efetuadas exatamente ao mesmo tempo mas em diferentes locais.

Este tipo é um subtipo de «SamplingCoverageObservation».

Restrições do tipo de objeto geográfico «MultiPointObservation»

A «featureOfInterest» dever ser uma «SF_SamplingCurve», «SF_SamplingSurface» ou «SF_SamplingSolid».

O «phenomenonTime» deve ser um «TM_Instant».

O «result» deve ser uma «MultiPointCoverage».

7.4.1.6. Observação de séries temporais de pontos (PointTimeSeriesObservation)

Observação que representa uma série temporal de medições de pontos de uma propriedade num local fixo no espaço.

Este tipo é um subtipo de «SamplingCoverageObservation».

Restrições do tipo de objeto geográfico «PointTimeSeriesObservation»

A «featureOfInterest» deve ser um «SF_SamplingPoint».

O «phenomenonTime» deve ser um «TM_Period».

O «result» deve ser uma «Timeseries».

7.4.1.7. Observação do perfil (ProfileObservation)

Observação que representa a medição de uma propriedade ao longo de um perfil vertical no espaço num único instante temporal.

Este tipo é um subtipo de «SamplingCoverageObservation».

Restrições do tipo de objeto geográfico «ProfileObservation»

A «featureOfInterest» deve ser uma «SF_SamplingCurve»

O «phenomenonTime» deve ser um «TM_Instant».

O «result» deve ser uma «ReferenceableGridCoverage» ou «RectifiedGridCoverage».

O domínio espacial do resultado deve conter um eixo que deve ser vertical.

7.4.1.8. Observação da trajetória (TrajectoryObservation)

Observação que representa a medição de uma propriedade ao longo de uma curva sinuosa no tempo e no espaço.

Este tipo é um subtipo de «SamplingCoverageObservation».

Restrições do tipo de objeto geográfico «TrajectoryObservation»

O «phenomenonTime» deve ser um «TM_Period».

O «result» deve ser uma «Timeseries».

Cada ponto no «result» deve ser uma «TimeLocationValueTriple».

A «featureOfInterest» deve ser uma «SF_Sampling Curve».

**7.4.2. Tipos de dados**

7.4.2.1. Tríade de tempo, local e valor (TimeLocationValueTriple)

Um conjunto triplo de tempo, local e valor (medição). Por exemplo, num ponto ao longo de uma trajetória.

Este tipo é um subtipo de «TimeValuePair».

Atributos do tipo de dados «TimeLocationValueTriple»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| location | Localização geográfica em que o valor é válido. | GM_Position |  |

**7.5. Requisitos para observações**

Quando o tipo «OM_Observation», ou qualquer subtipo deste, é utilizado para disponibilizar dados, são aplicáveis os seguintes requisitos:

(1) O tipo «Process» deve ser utilizado para indicar o procedimento utilizado numa «OM_Observation».

(2) Quando é feita referência a uma «EnvironmentalMonitoringFacility» a partir de uma «OM_Observation», deve ser fornecido um atributo «parameter», cujo atributo «name» é «relatedMonitoringFeature» e cujo atributo «value» é do tipo «AbstractMonitoringFeature».

(3) Para todas as codificações utilizadas para a totalidade ou parte de um resultado «OM_Observation», deve estar disponível uma Interface de Programação de Aplicações (Application Programming Interface - API) para ler o ficheiro codificado. A referida API deve ser capaz de expor a informação necessária para realizar objetos geográficos INSPIRE.

(4) Se estiver presente o atributo «processParameter» na propriedade «procedure» de um objeto de «OM_Observation», o seu valor (um nome) deve ser incluído no atributo «parameter» do objeto «OM_Observation».

**8. MODELO DE COMPLEXO DE ATIVIDADES**

O modelo de complexo de atividades INSPIRE contém o pacote «Complexo de Atividades» (Activity Complex).

**8.1. Complexo de atividades**

**8.1.1. Tipos de objetos geográficos**

O pacote «Complexo de Atividades» contém o tipo de objeto geográfico «Complexo de Atividades».

8.1.1.1. Complexo de atividades (ActivityComplex)

Uma unidade única, tanto do ponto de vista técnico como económico, sob o controlo da gestão de uma entidade jurídica (operador), abrangendo atividades como as enumeradas na Classificação NACE do Eurostat estabelecida pelo Regulamento (CE) n.º 1893/2006 do Parlamento Europeu e do Conselho (

5

). O «Complexo de Atividades» deve representar a totalidade da área, na mesma ou em diferentes localizações geográficas, gerida pelo mesmo operador, incluindo todas as infraestruturas, equipamentos e materiais.

Atributos do tipo de objeto geográfico «ActivityComplex»

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

**8.1.2. Tipos de dados**

8.1.2.1. Função (Function)

A função de algo expressa como uma atividade e informação opcional de entrada e/ou saída.

Atributos do tipo de dados «Function»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| activity | Descrição categorizada de um conjunto individual ou organizado de processos tecnicamente relacionados que são executados por uma unidade económica, privada ou pública, com ou sem fins lucrativos. | EconomicActivityValue |  |
| input | Qualquer material classificado ou registado que entra numa unidade técnica e económica de acordo com a sua função. | InputOutputValue | voidable |
| output | Qualquer material classificado ou registado que sai de uma unidade técnica e económica de acordo com a sua função. | InputOutputValue | voidable |
| description | Uma descrição mais detalhada da função. | PT_FreeText | voidable |

8.1.2.2. Capacidade (Capacity)

A quantificação de um capacidade real ou potencial para desenvolver uma atividade, que geralmente não se altera, não se altera frequentemente ou não se altera de modo significativo.

Atributos do tipo de dados «Capacity»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| activity | Descrição categorizada de um conjunto individual ou organizado de processos tecnicamente relacionados que são executados por uma unidade económica, privada ou pública, com ou sem fins lucrativos. | EconomicActivityValue |  |
| input | Informação mensurável sobre qualquer material classificado ou registado que entra numa unidade técnica e económica de acordo com a sua função. | InputOutputAmount |  |
| output | Informação mensurável sobre qualquer material classificado ou registado que sai de uma unidade técnica e económica de acordo com a sua função. | InputOutputAmount |  |
| time | Período de tempo a que se refere a capacidade especificada, como 1 ano para uma capacidade anual. | TM_Duration |  |
| description | Uma descrição da capacidade. | PT_FreeText | voidable |

8.1.2.3. Quantidade de entradas ou saídas (InputOutputAmount)

Tipo e, quando disponível, quantidade mensurável de um material classificado ou registado que entra ou sai de uma unidade técnica e económica.

Atributos do tipo de dados «InputOutputAmount»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inputOutput | Material classificado ou registado que entra ou sai de uma unidade técnica e económica de acordo com a sua função. | InputOutputValue |  |
| amount | Quantidade (como um volume ou massa) do material classificado ou registado que entra ou sai de uma unidade técnica e económica. | Measure | voidable |

8.1.2.4. Permissão (Permission)

Decisão oficial (consentimento formal) que concede autorização para operar a totalidade ou parte de um «Complexo de Atividades», sujeita a determinadas condições que garantem que as instalações ou partes das instalações situadas no mesmo sítio e operadas pelo mesmo operador cumprem os requisitos estabelecidos por uma autoridade competente. Uma permissão pode abranger uma ou mais funções e fixar parâmetros de capacidade. O termo poderia ser alargado a outros tipos de certificados ou documentos de especial relevância em função do âmbito de aplicação (por exemplo, ISO, EMAS, normas nacionais de qualidade, etc.).

Atributos do tipo de dados «Permission»

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

8.1.2.5. Descrição do complexo de atividades (ActivityComplexDescription)

Informação adicional sobre um complexo de atividades, incluindo a sua descrição, endereço, dados de contacto e partes relacionadas.

Atributos do tipo de objeto geográfico «ActivityComplexDescription»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| description | Uma definição complementar de «Complexo de Atividades» e suas características. | PT_FreeText | voidable |
| address | Um endereço para o complexo de atividades, ou seja, um endereço onde se realizam as atividades. | AddressRepresentation | voidable |
| contact | Informação de contacto para o complexo de atividades. | Contact | voidable |
| relatedParty | Informação de partes relacionadas com o «Complexo de Atividades». Está aberta a muitas funções diferentes, como detentores de dados, operadores ou autoridades competentes. | RelatedParty | voidable |

**8.1.3. Listas de códigos**

8.1.3.1. Atividade económica (EconomicActivityValue)

Classificação das atividades económicas.

Os valores autorizados para esta lista de códigos incluem os valores constantes das listas de códigos seguintes ou de outras listas de códigos especificadas pelos fornecedores de dados:

— Classificação das Atividades Económicas da UE (EconomicActivityNACEValue): Atividades económicas de acordo com os valores da Classificação NACE do Eurostat, tal como estabelecidas no Regulamento (CE) n.º 1893/2006 do Parlamento Europeu e do Conselho (

6

).

— Classificação da UE de estatísticas das atividades económicas no setor dos resíduos (EconomicActivityWasteStatisticsValue): Classificação das atividades económicas de acordo com o anexo I, Secção 8, do Regulamento (CE) n.º 2150/2002 (

7

)

— Classificação da UE relativa à Eliminação e Valorização de Resíduos (WasteRecoveryDisposalValue): Classificação das operações de valorização e eliminação de resíduos de acordo com os anexos I e II da Diretiva 2008/98/CE do Parlamento Europeu e do Conselho (

8

).

8.1.3.2. Entradas ou saídas (InputOutputValue)

Classificação das entradas ou saídas.

Os valores autorizados para esta lista de códigos incluem os valores constantes das listas de códigos seguintes ou de outras listas de códigos especificadas pelos fornecedores de dados.

— Classificação de Produtos da UE (ProductCPAValue): Classificação de Produtos por Atividade Económica de acordo com o Regulamento (CE) n.º 451/2008 do Parlamento Europeu e do Conselho (

9

).

— Classificação de Resíduos da UE (WasteValue): Classificação dos Resíduos de acordo com a Decisão 2000/532/CE (

10

).

**8.2. Requisitos para «Complexos de Atividades»**

Se um fornecedor de dados utilizar um subtipo de «ActivityComplex» para disponibilizar informações sobre o estatuto, a capacidade física, as permissões e/ou informações adicionais, devem ser utilizadas as listas de códigos e os tipos de dados relevantes («ConditionOfFacilityValue», «Capacity», «Permission», «ActivityComplexDescription») incluídos no pacote «Complexo de Atividades».
