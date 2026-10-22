---
id: "regulamento-ue-2013-1253-anexo-iii"
celex: "32013R1253"
title: "Regulamento (UE) n. ° 1253/2013 da Comissão, de 21 de outubro de 2013 , que altera o Regulamento (UE) n. ° 1089/2010 que estabelece as disposições de execução da Diretiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Anexo III"
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
part: "Anexo III"
---

# Regulamento (UE) n. ° 1253/2013 da Comissão, de 21 de outubro de 2013 , que altera o Regulamento (UE) n. ° 1089/2010 que estabelece as disposições de execução da Diretiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Anexo III

## Anexo III

É aditado o seguinte anexo III ao Regulamento (CE) n.º 1089/2010:

«ANEXO III

**Requisitos relativos a categorias temáticas de dados geográficos enumeradas no anexo II da Diretiva 2007/2/CE**

**1. ALTITUDE (ELEVATION)**

**1.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) “Modelo Numérico Altimétrico” (Digital Elevation Model - DEM): Modelo Numérico Topográfico (DSM) ou Modelo Digital do Terreno (DTM).

(2) “Modelo Numérico Topográfico” (Digital Surface Model - DSM): uma superfície que descreve a forma tridimensional da superfície terrestre, incluindo todos elementos estáticos sobre esta. Os fenómenos temporários não fazem parte da superfície, mas, devido às dificuldades técnicas de eliminação desses fenómenos, alguns desses elementos podem também estar presentes na superfície.

(3) “Modelo Digital do Terreno” (Digital Terrain Model - DTM): uma superfície que descreve a forma tridimensional da superfície terrestre nua, excluindo tanto quanto possível outros elementos sobre esta.

(4) “Altitude”(elevation)

: uma propriedade dimensional de um objeto geográfico delimitada na vertical que consiste numa medição absoluta referenciada a uma superfície bem definida que é normalmente tomada como origem.

(5) “Altura”(height)

: uma propriedade altimétrica medida ao longo de uma linha de fio de prumo num sentido oposto ao do campo de gravidade da Terra (para cima).

(6) “Profundidade”(depth)

: uma propriedade altimétrica medida ao longo de uma linha de fio de prumo num sentido coincidente com o do campo de gravidade da Terra (para baixo).

**1.2. Estrutura da categoria temática de dados geográficos “Altitude”**

Os tipos especificados para a categoria temática de dados geográficos “Altitude” estão estruturados nos seguintes pacotes:

— Altitude - Tipos de base (Elevation – Base Types)

— Altitude - Cobertura matricial (Elevation – Grid Coverage)

— Altitude - Elementos vetoriais (Elevation – Vector Elements)

— Altitude - TIN (Elevation – TIN)

Devem ser disponibilizados conjuntos de dados geográficos que descrevam a morfologia da altimetria terrestre utilizando, pelo menos, os tipos de objetos geográficos incluídos no pacote “Altitude - Cobertura Matricial”.

Devem ser disponibilizados conjuntos de dados geográficos que descrevam a morfologia da batimetria terrestre utilizando, pelo menos, os tipos de objetos geográficos incluídos no pacote “Altitude - Cobertura Matricial” ou no pacote “Altitude - Elementos Vetoriais”.

**1.3. Altitude - Tipos de base**

**1.3.1. Enumerações**

**1.3.1.1. Tipo de propriedade altimétrica (ElevationPropertyTypeValue)**

Tipo de enumeração que determina a propriedade altimétrica que foi medida ou calculada.

**Valores para a enumeração “ElevationPropertyTypeValue”**

| Valor | Definição |
|---|---|
| Height | Propriedade altimétrica medida ao longo de uma linha de fio de prumo num sentido oposto ao do campo de gravidade da Terra (para cima). |
| Depth | Propriedade altimétrica medida ao longo de uma linha de fio de prumo num sentido coincidente com o do campo de gravidade da Terra (para baixo). |

**1.3.1.2. Tipo de superfície (SurfaceTypeValue)**

Tipo de enumeração que determina a superfície altimétrica no que diz respeito à sua relativa similitude com a superfície nua da Terra.

**Valores para a enumeração “SurfaceTypeValue”**

| Valor | Definição |
|---|---|
| DTM | Modelo Digital do Terreno. |
| DSM | Modelo Numérico Topográfico. |

**1.4. Altitude - Cobertura matricial**

**1.4.1. Tipos de objetos geográficos**

O pacote “Altitude - Cobertura Matricial” contém o tipo de objeto geográfico “Altitude - Cobertura Matricial”.

**1.4.1.1. Cobertura altimétrica matricial (ElevationGridCoverage)**

Cobertura contínua que utiliza uma tesselação sistemática baseada numa quadrícula quadrilateral retificada regular para cobrir o seu domínio, quando o valor da propriedade altimétrica é geralmente conhecido para cada uma das cotas que formam este domínio.

Este tipo é um subtipo de “RectifiedGridCoverage”.

**Atributos do tipo de objeto geográfico “ElevationGridCoverage”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| domainExtent | Extensão do domínio espaciotemporal da cobertura. | EX_Extent |  |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| propertyType | Atributo que determina a propriedade altimétrica representada pela cobertura altimétrica matricial. | ElevationPropertyTypeValue |  |
| surfaceType | Atributo que indica o tipo de superfície altimétrica que a cobertura descreve em relação à superfície nua da Terra. | SurfaceTypeValue |  |

**Associações do tipo de objeto geográfico “ElevationGridCoverage”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| contributingElevationGridCoverage | Referência às coberturas altimétricas matriciais que compõem uma cobertura altimétrica matricial agregada. <br> A associação tem propriedades adicionais conforme definido na classe de associação “ElevationGridCoverageAggregation”. | ElevationGridCoverage |  |

**Restrições do tipo de objeto geográfico “ElevationGridCoverage”**

A dimensão da quadrícula deve ser sempre 2 para uma cobertura altimétrica matricial.

O atributo “domainExtent” deve estar preenchido, pelo menos, com um subtipo de “EX_GeographicExtent”.

Deve ser fornecido o sistema de referência de coordenadas utilizado para referenciar a quadrícula.

Todas as instâncias de “ElevationGridCoverage”, a que se refere uma instância de “ElevationGridCoverage” agregada, devem partilhar a mesma orientação de eixos da quadrícula e o mesmo espaçamento de quadrículas em cada direção.

A origem da quadrícula deve ser descrita em duas dimensões.

Os valores no conjunto da gama de valores devem ser descritos pelo tipo “Float”.

**1.4.2. Tipos de dados**

**1.4.2.1. Agregação da cobertura altimétrica matricial (ElevationGridCoverageAggregation)**

Características geométricas da agregação da cobertura altimétrica matricial.

Este tipo é uma classe de associação.

**Atributos do tipo de dados “ElevationGridCoverageAggregation”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| contributingFootprint | Representação geométrica que delimita a área geográfica da cobertura altimétrica matricial que contribui para a cobertura altimétrica matricial agregada. | GM_MultiSurface |  |

**1.5. Altitude - Elementos vetoriais**

**1.5.1. Tipos de objetos geográficos**

O pacote “Altitude - Elementos Vetoriais” contém os seguintes tipos de objetos geográficos:

— Objeto altimétrico vetorial

— Cota altimétrica

— Curva de nível

— Linha de rutura

— Área vazia

— Área isolada

**1.5.1.1. Objeto altimétrico vetorial (ElevationVectorObject)**

Objeto geográfico altimétrico que faz parte de um conjunto de dados vetoriais e que participa na descrição da propriedade altimétrica de uma superfície no mundo real. Consiste numa base de identificação de todos os objetos vetoriais que podem ser incluídos como parte de um conjunto de dados altimétricos.

Este tipo é abstrato.

**Atributos do tipo de objeto geográfico “ElevationVectorObject”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| localDepthDatum | Identificação de um sistema local de referência de coordenadas verticais não incluído num registo, que é utilizado para referir medições de profundidade. | ChartDatum |  |
| propertyType | Atributo que classifica o objeto altimétrico vetorial como um objeto geográfico altimétrico ou batimétrico. Determina a propriedade altimétrica representada pelo objeto. | ElevationPropertyTypeValue |  |

**1.5.1.2. Cota altimétrica (SpotElevation)**

Objeto geográfico com representação pontual que descreve a altitude de uma superfície terrestre num local específico. Fornece um valor único de propriedade altimétrica.

Este tipo é um subtipo de “ElevationVectorObject”.

**Atributos do tipo de objeto geográfico “SpotElevation”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| classification | Classe da cota altimétrica de acordo com a Especificação LAS da Sociedade Americana de Fotogrametria e Teledeteção (American Society for Photogrammetry and Remote Sensing - ASPRS). | SpotElevationClassValue | voidable |
| geographicalName | Topónimo que é utilizado para identificar uma determinada localização de uma superfície terrestre ou imersa no mundo real, que é representado pelo objeto geográfico de cota altimétrica. | GeographicalName | voidable |
| geometry | Representa as propriedades geométricas do objeto geográfico. | GM_Point |  |
| propertyValue | Valor da propriedade altimétrica do objeto geográfico referido a um determinado sistema de referência de coordenadas verticais. | DirectPosition |  |
| spotElevationType | O tipo da cota altimétrica. | SpotElevationTypeValue | voidable |

**Restrições do tipo de objeto geográfico “SpotElevation”**

A dimensão da coordenada do valor da propriedade deve ser 1.

O valor da propriedade deve ser expresso por referência a um sistema de referência de coordenadas verticais.

**1.5.1.3. Curva de nível (ContourLine)**

Objeto geográfico linear composto por um conjunto de localizações adjacentes caracterizadas por terem o mesmo valor de propriedade altimétrica. Descreve, juntamente com outras curvas de nível presentes na área, a morfologia local da superfície terrestre.

Este tipo é um subtipo de “ElevationVectorObject”.

**Atributos do tipo de objeto geográfico “ContourLine”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| contourLineType | Tipo de curva de nível no que diz respeito ao intervalo da curva de nível normal vertical (caso exista). | ContourLineTypeValue | voidable |
| downRight | Propriedade que indica que o objeto geográfico de curva de nível está digitalizado de um modo que a altura da superfície altimétrica é inferior no lado direito da curva. | Boolean | voidable |
| geometry | Representa as propriedades geométricas do objeto geográfico. | GM_Curve |  |
| propertyValue | Valor da propriedade altimétrica do objeto geográfico referenciado a um determinado sistema de referência de coordenadas verticais. | DirectPosition |  |

**Restrições do tipo de objeto geográfico “ContourLine”**

A dimensão da coordenada do valor da propriedade deve ser 1.

O valor da propriedade deve ser expresso por referência a um sistema de referência de coordenadas verticais.

**1.5.1.4. Linha de rutura (BreakLine)**

Uma linha crítica que descreve a forma de uma superfície altimétrica e indica uma descontinuidade no declive da superfície (ou seja, uma alteração abrupta da sua inclinação). Os triângulos incluídos num modelo TIN não devem nunca atravessá-la.

Este tipo é um subtipo de “ElevationVectorObject”.

**Atributos do tipo de objeto geográfico “BreakLine”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| breakLineType | Tipo de linha de rutura relativamente à característica natural ou artificial do mundo real que representa, ou à função específica que tem no cálculo de um Modelo Numérico Altimétrico (DEM). | BreakLineTypeValue |  |
| geometry | Representa as propriedades geométricas do objeto geográfico. | GM_Curve |  |
| manMadeBreak | Linha que representa uma descontinuidade altimétrica devida a uma construção artificial presente no terreno. | Boolean | voidable |

**1.5.1.5. Área vazia (VoidArea)**

Área da superfície terrestre em que o modelo altimétrico é desconhecido devido à falta de dados de entrada. Esta área deve ser excluída de um modelo DEM.

Este tipo é um subtipo de “ElevationVectorObject”.

**Atributos do tipo de objeto geográfico “VoidArea”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Representa as propriedades geométricas do objeto geográfico. | GM_Surface |  |

**1.5.1.6. Área isolada (IsolatedArea)**

Delimitação de uma área da superfície terrestre em que existe uma parte isolada do modelo altimétrico. As suas áreas circundantes exteriores não têm informação altimétrica.

Este tipo é um subtipo de “ElevationVectorObject”.

**Atributos do tipo de objeto geográfico “IsolatedArea”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Representa as propriedades geométricas do objeto geográfico. | GM_Surface |  |

**1.5.2. Tipos de dados**

**1.5.2.1. Datum cartográfico (ChartDatum)**

Sistema local de referência de coordenadas verticais que é utilizado para referir e representar as medições de profundidade como valores de propriedades.

**Atributos do tipo de dados “ChartDatum”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| datumWaterLevel | Nível da água que determina a origem das medições da profundidade para o datum cartográfico. | WaterLevelValue |  |
| offset | Diferença relativa entre a altura de cada ponto de referência e a altura do nível da água que determina o datum cartográfico. | Measure |  |
| referencePoint | Posição(ões) geográfica(s) de: - Caso A: um ponto único que é utilizado para referir os valores de profundidade no âmbito geográfico do datum cartográfico. - Caso B: um conjunto de pontos em que são efetuadas medições do nível da água para determinar o nível da água do datum cartográfico. | GM_Point |  |
| scope | Âmbito geográfico em que o datum de profundidade local é na prática utilizado. | EX_Extent |  |

**1.5.3. Enumerações**

**1.5.3.1. Tipo de curvas de nível (ContourLineTypeValue)**

Lista de categorias possíveis de curvas de nível baseadas no parâmetro equidistância do conjunto de dados.

**Valores para a enumeração “ContourLineTypeValue”**

| Valor | Definição |
|---|---|
| master | Nível numa distância vertical que é múltiplo do parâmetro equidistância (correspondendo a um determinado múltiplo do intervalo do nível vertical normal) associado à escala nominal. |
| ordinary | Nível no parâmetro de equidistância (correspondendo ao intervalo do nível vertical normal) associado à escala nominal, e que não é um nível principal (master). |
| auxiliary | Um nível suplementar – não correspondente ao intervalo do nível vertical normal – estimado ou interpolado a partir de níveis circundantes, utilizado em áreas em que a informação altimétrica é insuficiente para fins de cartografia altimétrica ou para controlar a criação de um modelo numérico altimétrico. |

**1.5.4. Listas de códigos**

**1.5.4.1. Tipo de linha de rutura (BreakLineTypeValue)**

Lista de possíveis valores do tipo para linhas de rutura com base nas características físicas da linha de rutura [na superfície altimétrica].

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores mais restritos definidos pelos fornecedores de dados.

**Valores para a lista de códigos “BreakLineTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| bottomOfSlope | base do declive | Linha de rutura que representa o limite inferior de uma área que tem um declive constante na superfície do terreno, variando geralmente entre aproximadamente 2° e 40°. |
| changeInSlope | alteração no declive | Linha de rutura que representa uma coleção de pontos adjacentes em que o terreno apresenta uma alteração abrupta do declive. |
| flatAreaBoundary | limite de área plana | Linha de rutura que delimita uma parte isolada do território em que o modelo altimétrico tem de ser mantido ao mesmo valor altimétrico. |
| formLine | linha de forma | Linha de rutura que representa uma orientação local em que a superfície altimétrica objeto de descrição apresenta o maior declive. |
| topOfSlope | topo do declive | Linha de rutura que representa o limite superior de uma área que tem um declive constante na superfície do terreno, variando em regra entre aproximadamente 2° e 40°. |

**1.5.4.2. Classificação da cota altimétrica (SpotElevationClassValue)**

Valores possíveis de classificação das cotas altimétricas baseados na especificação LAS elaborada pela Sociedade Americana de Fotogrametria e Teledeteção (ASPRS).

Os valores autorizados para esta lista de códigos incluem eventuais valores definidos pelos fornecedores de dados.

Os fornecedores de dados podem utilizar os valores especificados no Documento de Orientação Técnica INSPIRE sobre Altitude.

**1.5.4.3 Tipo de cota altimétrica (SpotElevationTypeValue)**

Valores possíveis para pontos da cota altimétrica que descrevem uma singularidade da superfície.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores mais restritos definidos pelos fornecedores de dados.

**Valores para a lista de códigos “SpotElevationTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| depression | depressão | Ponto que representa uma parte do relevo da superfície do terreno ou da superfície do fundo da massa de água com uma altimetria inferior em relação aos seus pontos circundantes. |
| formSpot | ponto de forma | Cota altimétrica suplementar, estimada ou interpolada a partir de cotas circundantes, em áreas em que existem poucas curvas de nível ou outra informação altimétrica. |
| generic | genérico | Objeto geográfico de cota altimétrica que não preenche a descrição de qualquer dos outros valores na atual lista de códigos. |
| pass | colo | Ponto mais baixo de uma depressão numa cordilheira, geralmente aberto ao longo da linha da crista, que permite a passagem de uma vertente para outra. |
| summit | cume | Ponto mais elevado de uma proeminência no relevo de uma superfície terrestre ou na superfície do fundo de uma massa de água. |

**1.6. Altitude - TIN**

**1.6.1. Tipos de objetos geográficos**

O pacote “Altitude – TIN” contém o tipo de objeto geográfico “TIN Altimétrica”.

**1.6.1.1. TIN altimétrica (ElevationTIN)**

Coleção de objetos geográficos altimétricos que formam uma determinada tesselação do espaço com base numa “

Triangulated Irregular Network

” (TIN) (rede irregular de triângulos) de acordo com a geometria “GM_Tin” definida na norma ISO 19107:2003). Os seus componentes são um conjunto de pontos de controlo cujos valores da propriedade altimétrica são conhecidos e um conjunto de linhas de rutura e de linhas de paragem.

**Atributos do tipo de objeto geográfico “ElevationTIN”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| geometries | Representa a coleção de propriedades geométricas do objeto geográfico TIN altimétrica. | GM_Tin |  |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| propertyType | Atributo que determina a propriedade altimétrica representada pela TIN altimétrica. | ElevationPropertyTypeValue |  |
| surfaceType | Atributo que indica o tipo de superfície altimétrica que a TIN altimétrica descreve em relação à superfície nua da Terra. | SurfaceTypeValue |  |

**1.7. Requisitos específicos de categorias temáticas**

**1.7.1. Requisitos aplicáveis aos identificadores de objetos externos**

|  | (1) | Se os dados altimétricos forem atualizados com base em novos dados-fonte, deve ser atribuído aos objetos atualizados um novo identificador de objeto externo. |
|---|---|---|

**1.7.2. Requisitos para as coberturas altimétricas matriciais**

<table> <tbody> <tr> <td></td> <td>(1)</td> <td>Em derrogação ao requisito estabelecido no ponto 2.2 do anexo II, qualquer quadrícula compatível com um dos seguintes sistemas de referência de coordenadas pode ser utilizada para a disponibilização de dados altimétricos matriciais: <table> <tbody> <tr> <td>—</td> <td>coordenadas geodésicas bidimensionais (latitude e longitude) baseadas num datum especificado no ponto 1.2. do anexo II e que utilizam os parâmetros da elipsoide do GRS80;</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>coordenadas planas utilizando o sistema de referência de coordenadas de projeção cónica conforme de Lambert do ETRS89;</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>coordenadas planas utilizando o sistema de referência de coordenadas de projeção transversa de Mercator do ETRS89;</td> </tr> </tbody> </table> Não deve ser utilizada a quadrícula referida no ponto 2.2.1 do anexo II.</td> </tr> </tbody> </table>

|  | (2) | O atributo “domainExtent” de cada instância de <br> “ElevationGridCoverage” <br> deve ser preenchido, pelo menos, com um subtipo do tipo <br> “EX_GeographicExtent” <br> . |
|---|---|---|

|  | (3) | Os valores da propriedade altimétrica incluídos no conjunto de gamas de valores de uma única “ElevationGridCoverage” devem ser referenciados a um único sistema de referência de coordenadas verticais. |
|---|---|---|

|  | (4) | Todas as instâncias de “ElevationGridCoverage”, a que se refere uma instância de “ElevationGridCoverage” agregada, devem ser coerentes. Isto significa que devem ter o mesmo tipo de gama de valores, sistema de referência de coordenadas e resolução. Devem também suportar o alinhamento de quadrículas, ou seja os pontos da quadrícula numa instância de “ElevationGridCoverage” devem estar alinhados com os pontos da quadrícula de outras instâncias de “ElevationGridCoverage”, de modo a que as células das quadrículas não se sobreponham parcialmente. |
|---|---|---|

|  | (5) | As “pegadas” (footprints) de quaisquer duas instâncias de “ElevationGridCoverage” a que se refere a mesma instância de “ElevationGridCoverage” agregada devem ser adjacentes ou não adjacentes. |
|---|---|---|

|  | (6) | \A união das “pegadas” das instâncias de “ElevationGridCoverage” a que se refere a mesma instância de “ElevationGridCoverage” agregada determina a extensão geográfica (“domainExtent”) da instância da “ElevationGridCoverage” agregada. |
|---|---|---|

|  | (7) | O pacote “ElevationGridCoverage” deve ser limitado a geometrias bidimensionais. |
|---|---|---|

<table> <tbody> <tr> <td></td> <td>(8)</td> <td>Deve ser fornecida informação sobre as datas de aquisição dos dados contidos nas coberturas altimétricas matriciais em, pelo menos, uma das seguintes formas: <table> <tbody> <tr> <td>(a)</td> <td>Fornecendo o elemento de metadados de referência temporal para cada objeto geográfico através do atributo de metadados do tipo de objeto geográfico “ElevationGridCoverage”;</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(b)</td> <td>Fornecendo o elemento de metadados de referência temporal estabelecido no Regulamento (CE) n.º 1205/2008 como uma extensão temporal.</td> </tr> </tbody> </table></td> </tr> </tbody> </table>

**1.7.3. Requisitos aplicáveis aos dados altimétricos vetoriais**

|  | (1) | Quando os conjuntos de dados altimétricos vetoriais são fornecidos utilizando geometrias 2-D, a componente vertical (terceira dimensão) deve ser fornecida como valores da propriedade altimétrica no atributo “propertyValue”. |
|---|---|---|

|  | (2) | Quando os conjuntos de dados altimétricos vetoriais são fornecidos utilizando geometrias 2.5-D, os valores da propriedade altimétrica só devem ser incluídos na terceira coordenada (Z) dessas geometrias. |
|---|---|---|

**1.7.4. Requisitos aplicáveis a TIN altimétricas**

|  | (1) | Os valores de propriedade incluídos numa única instância do tipo de objeto geográfico “ElevationTIN” (modelo TIN) devem ser referenciados a um único sistema de referência de coordenadas verticais. |
|---|---|---|

|  | (2) | Os triângulos que intersetam uma linha de paragem devem ser eliminados de uma superfície TIN, deixando buracos na superfície. Se a coincidência ocorrer em triângulos limitadores de superfícies, o resultado deve ser uma alteração do limite da superfície. |
|---|---|---|

|  | (3) | Os objetos geográficos vetoriais fornecidos como componentes de uma coleção TIN devem cumprir as regras genéricas de coerência estabelecidas para objetos vetoriais. |
|---|---|---|

**1.7.5. Requisitos aplicáveis a sistemas de referência**

|  | (1) | Para a medição da profundidade do fundo do mar quando se verifica uma apreciável amplitude de marés (águas de maré), deve ser utilizada a maré astronómica mais baixa (Lowest Astronomical Tide - LAT) como superfície de referência. |
|---|---|---|

|  | (2) | Para a medição da profundidade do fundo do mar nas zonas marinhas sem uma amplitude de marés apreciável, em oceanos abertos e em águas com uma profundidade superior a 200 metros, a profundidade do fundo do mar deve ser referenciada ao nível médio do mar (Mean Sea Level - MSL), ou a um nível de referência bem definido próximo do MSL. |
|---|---|---|

|  | (3) | A altitude do nível de referência a que a profundidade do fundo de uma massa de água interior é medida deve ser referenciada a um sistema de referência vertical relacionado com a gravidade. Esse sistema deve ser o Sistema Europeu de Referência Vertical (European Vertical Reference System - EVRS) no que diz respeito às áreas no âmbito geográfico do EVRS, ou o sistema de referência vertical relacionado com a gravidade identificado pelo Estado-Membro fora do âmbito do EVRS. |
|---|---|---|

|  | (4) | Quando fornecem um modelo altimétrico integrado terra-mar, deve ser modelada apenas uma propriedade altimétrica (a altura ou a profundidade), e os seus valores devem ser referenciados a um único sistema de referência de coordenadas verticais. |
|---|---|---|

**1.7.6. Requisitos aplicáveis à qualidade e coerência dos dados**

|  | (1) | Se forem utilizadas medições diferentes das medições ISO referentes à qualidade dos dados para avaliar um conjunto de dados altimétricos, o elemento de metadados “Histórico” deve incluir informações sobre essas medições e, se possível, uma referência a um recurso em linha em que estejam disponíveis mais informações. |
|---|---|---|

|  | (2) | Os objetos geográficos de curvas de nível ligadas devem ter o mesmo valor altimétrico quando estão referenciados ao mesmo sistema de referência de coordenadas verticais. |
|---|---|---|

|  | (3) | Quando os valores altimétricos de objetos geográficos de linha de rutura são fornecidos como terceiras coordenadas (Z), o ponto de intersecção de dois objetos geográficos de linha de rutura devem ter o mesmo valor altimétrico. |
|---|---|---|

|  | (4) | Quando um objeto geográfico de curvas de nível e um objeto geográfico de linha de rutura fornecidos no mesmo sistema de referência de coordenadas verticais se intersetam, o ponto de intersecção deve ter o mesmo valor altimétrico (se os valores altimétricos dos objetos geográficos da linha de rutura forem fornecido pela terceira coordenada (Z)). |
|---|---|---|

|  | (5) | Os objetos geográficos de curvas de nível que têm diferentes valores altimétricos não devem intersectar-se nem tocar-se quando são referenciados ao mesmo sistema de referência de coordenadas verticais. |
|---|---|---|

|  | (6) | O limite de um objeto geográfico de área isolada não deve tocar no limite externo de um objeto geográfico de área vazia quando esses objetos são referenciados ao mesmo sistema de referência de coordenadas verticais. |
|---|---|---|

**1.8. Camadas**

**Camadas para a categoria temática de dados geográficos “Altitude”**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| EL.BreakLine | Linha de rutura | BreakLine |
| EL.ContourLine | Curva de nível | ContourLine |
| EL.IsolatedArea | Área isolada | IsolatedArea |
| EL.SpotElevation | Cota altimétrica | SpotElevation |
| EL.VoidArea | Área vazia | VoidArea |
| EL.ElevationGridCoverage | Cobertura altimétrica matricial | ElevationGridCoverage |
| EL.ElevationTIN | TIN altimétrica | ElevationTIN |

**2. OCUPAÇÃO DO SOLO (LAND COVER)**

**2.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) “Sistema de classificação”(classification system)

: um sistema para a atribuição de objetos a classes, em conformidade com a norma ISO 19144-1:2012;

(2) “Cobertura discreta”(discrete coverage)

: uma cobertura que fornece os mesmos valores do atributo de entidade para cada posição direta em qualquer objeto geográfico, objeto temporal ou objeto espaciotemporal simples no seu domínio, em conformidade com a norma EN ISO 19123:2007;

(3) “Objeto de ocupação do solo”(land cover object)

: um objeto geográfico (ponto, pixel ou polígono) em que foi observada a ocupação do solo;

(4) “Legenda”(legend)

: a aplicação de uma classificação numa área específica utilizando uma escala cartográfica definida e um conjunto de dados específico;

(5) “Unidade cartográfica mínima”(minimal mapping unit)

: a menor área de um polígono cuja representação é permitida num determinado conjunto de dados da ocupação do solo;

(6) “Situação”(situation)

: o estado de um determinado objeto de ocupação do solo num determinado momento.

**2.2. Estrutura da categoria temática de dados geográficos “Ocupação do Solo”**

Os tipos especificados para a categoria temática de dados geográficos “Ocupação do Solo” estão estruturados nos seguintes pacotes:

— Nomenclatura da ocupação do solo (Land Cover Nomenclature)

— Vetor de ocupação do solo (Land Cover Vector)

— Raster de ocupação do solo (Land Cover Raster)

**2.3. Nomenclatura da ocupação do solo**

**2.3.1. Tipos de dados**

**2.3.1.1. Nomenclatura da ocupação do solo (LandCoverNomenclature)**

Informação sobre nomenclaturas de referência de ocupação do solo nacionais, institucionais ou locais.

**Atributos do tipo de dados “LandCoverNomenclature”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| responsibleParty | Parte responsável pelo desenvolvimento e/ou manutenção da nomenclatura. | RelatedParty |  |
| externalDescription | Documento que descreve a nomenclatura utilizada neste conjunto de dados. | DocumentCitation | voidable |
| embeddedDescription | Uma codificação incorporada do sistema de classificação de acordo com a norma ISO 19144-2. | LC_LandCoverClassificationSystem | voidable |
| nomenclatureCodeList | Um URI http que aponta para a lista de códigos apensa à nomenclatura utilizada. | URI |  |

**Restrições do tipo de dados “LandCoverNomenclature”**

Deve ser fornecida a descrição incorporada ou a descrição externa.

**2.3.2. Listas de códigos**

**2.3.2.1. Classe de ocupação do solo (LandCoverClassValue)**

Classificação ou lista de códigos de ocupação do solo.

Os valores autorizados para esta lista de códigos incluem eventuais valores definidos pelos fornecedores de dados.

Os fornecedores de dados podem utilizar os valores e os códigos do tipo número inteiro (a utilizar para representar classes específicas de ocupação do solo na gama dos objetos “LandCoverGridCoverage”) especificados para a lista de códigos “Componente Pura de Ocupação do Solo” (“PureLandCoverComponentValue”) no Documento de Orientação Técnica INSPIRE sobre Ocupação do Solo.

**2.4. Vetor de ocupação do solo**

**2.4.1. Tipos de objetos geográficos**

O pacote “Vetor de Ocupação do Solo” contém os seguintes tipos de objetos geográficos:

— Conjunto de dados de ocupação do solo

— Unidade de ocupação do solo

**2.4.1.1. Conjunto de dados de ocupação do solo (LandCoverDataset)**

Uma representação vetorial para dados de Ocupação do Solo.

**Atributos do tipo de objeto geográfico “LandCoverDataset”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| name | Nome do conjunto de dados Ocupação do Solo. | CharacterString |  |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| extent | Contém a extensão do conjunto de dados. | EX_Extent |  |
| nomenclatureDocumentation | Informação sobre a nomenclatura utilizada neste conjunto de dados. | LandCoverNomenclature |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | Momento em que o fenómeno começou a existir no mundo real. | DateTime | voidable |
| validTo | Momento em que o fenómeno deixou de existir no mundo real. | DateTime | voidable |

**Associações do tipo de objeto geográfico “LandCoverDataset”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| member | Unidade de ocupação do solo que faz parte do conjunto de dados. | LandCoverUnit |  |

**2.4.1.2. Unidade de ocupação do solo (LandCoverUnit)**

Um elemento individual do conjunto de dados Ocupação do Solo representado por um ponto ou uma superfície.

**Atributos do tipo de objeto geográfico “LandCoverUnit”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| geometry | Representação espacial dos dados Ocupação do Solo. | GM_Object |  |
| landCoverObservation | Informações sobre a ocupação do solo num local e momento específicos. | LandCoverObservation |  |

**Restrições do tipo de objeto geográfico “LandCoverUnit”**

As geometrias devem ser pontos ou superfícies.

**2.4.2. Tipos de dados**

**2.4.2.1. Observação da ocupação do solo (LandCoverObservation)**

Informações sobre a Ocupação do Solo num local e momento específicos.

**Atributos do tipo de dados “LandCoverObservation”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| class | Atribuição de uma classe de ocupação do solo a uma unidade de ocupação do solo mediante um identificador de código de classificação. | LandCoverClassValue |  |
| observationDate | Data de observação associada a uma observação. | DateTime | voidable |
| mosaic | Lista de valores de classificação que descreve detalhadamente uma unidade de ocupação do solo, associada a percentagens. | LandCoverValue | voidable |

**Restrições do tipo de objeto geográfico “LandCoverObservation”**

A soma de todos os atributos “coveredPercentage” associados a cada “LandCoverObservation” deve ser inferior ou igual a 100.

**2.4.2.2. Ocupação do solo (LandCoverValue)**

Classe genérica subjacente ao valor e percentagem de Ocupação do Solo.

**Atributos do tipo de dados “LandCoverValue”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| class | Atribuição de um objeto geográfico de ocupação do solo a uma classe de ocupação do solo mediante um identificador de código de classificação. | LandCoverClassValue |  |
| coveredPercentage | Fração da “LandCoverUnit” a que diz respeito o valor de classificação. | Integer | voidable |

**2.5. Raster de ocupação do solo**

**2.5.1. Tipos de objetos geográficos**

O pacote “

Raster de Ocupação do Solo” contém o tipo de objeto geográfico Cobertura Matricial da Ocupação do Solo.

**2.5.1.1. Cobertura matricial da ocupação do solo (LandCoverGridCoverage)**

Uma representação rasterizada para dados de Ocupação do Solo.

Este tipo é um subtipo de “RectifiedGridCoverage”.

**Atributos do tipo de objeto geográfico “LandCoverGridCoverage”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| name | Nome da cobertura de Ocupação do Solo. | CharacterString |  |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| extent | Contém a extensão do conjunto de dados. | EX_Extent |  |
| nomenclatureDocumentation | Informação sobre a nomenclatura utilizada nesta cobertura. | LandCoverNomenclature |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | Momento em que o fenómeno começou a existir no mundo real. | DateTime | voidable |
| validTo | Momento em que o fenómeno deixou de existir no mundo real. | DateTime | voidable |

**Restrições do tipo de objeto geográfico “LandCoverGridCoverage”**

Os valores no conjunto da gama de valores estão restringidos a um número inteiro.

**2.6. Requisitos específicos de categorias temáticas**

Se é fornecido um atributo “onlineDescription” para um tipo de dados “LandCoverNomenclature”, a descrição em linha referenciada deve definir, para cada classe, pelo menos um código, um nome, uma definição e um valor RGB a utilizar para fins de representação. Se a descrição em linha descreve a nomenclatura para um objeto “LandCoverGridCoverage”, deve também ser fornecido um código de quadrícula do tipo número inteiro (“Integer”) para cada classe. Este código deve ser utilizado na gama de valores da “LandCoverGridCoverage” a fim de representar a classe correspondente.

**2.7. Camadas**

**Camadas para a categoria temática de dados geográficos “Ocupação do Solo”**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| LC.LandCoverPoints | Pontos de ocupação do solo | LandCoverUnit |
| LC.LandCoverSurfaces | Superfícies de ocupação do solo | LandCoverUnit |
| LC.LandCoverRaster | Raster de ocupação do solo | LandCoverGridCoverage |

**3. ORTOIMAGENS (ORTHOIMAGERY)**

**3.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) “Mosaico”(mosaic)

: uma imagem composta por uma fusão de múltiplas fotografias ou imagens adjacentes ou em sobreposição.

(2) “Agregação de ortoimagens”(orthoimage aggregation)

: uma combinação de subconjuntos provenientes de várias coberturas homogéneas de ortoimagens que formam uma nova cobertura de ortoimagens.

(3) “Raster”: um padrão normalmente retangular de linhas de varrimento paralelas que formam, ou correspondem a, uma visualização num tubo de raios catódicos, em conformidade com a norma EN ISO 19123:2007.

**3.2. Tipos de objetos geográficos**

São especificados os seguintes tipos de objetos geográficos para a categoria temática de dados geográficos “Ortoimagens”:

— Cobertura de ortoimagens

— Elemento de mosaico

— Elemento de mosaico único

— Elemento de mosaico agregado

**3.2.1. Cobertura de ortoimagens (OrthoimageCoverage)**

Imagem rasterizada da superfície da Terra que foi geometricamente corrigida (“ortorretificada”) a fim de eliminar a distorção causada por diferenças na altimetria e inclinação do sensor e, opcionalmente, pela ótica do sensor.

Este tipo é um subtipo de “RectifiedGridCoverage”.

**Atributos do tipo de objeto geográfico “OrthoimageCoverage”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| domainExtent | Extensão do domínio espaciotemporal da cobertura. | EX_Extent |  |
| footprint | Área geográfica que encerra os dados válidos da cobertura de ortoimagens. | GM_MultiSurface | voidable |
| interpolationType | Método matemático que deve ser utilizado para avaliar uma cobertura contínua, ou seja, determinar os valores da cobertura em qualquer posição direta dentro do domínio da cobertura. | InterpolationMethodValue |  |
| name | Nome em texto livre da cobertura de ortoimagens. | CharacterString | voidable |
| phenomenonTime | Descrição da extensão da aquisição/observação no tempo. | TM_Period | voidable |
| beginLifespanVersion | Posição temporal em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | TM_Position | voidable |
| endLifespanVersion | Posição temporal em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | TM_Position | voidable |

**Associações do tipo de objeto geográfico “OrthoimageCoverage”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| contributingOrthoimageCoverage | Referência às coberturas de ortoimagens que compõem uma cobertura de ortoimagens agregadas. <br> A associação tem propriedades adicionais conforme definido na classe de associação “OrthoimageAggregation”. | OrthoimageCoverage |  |
| mosaicElement | Representação espacial do momento de aquisição de uma cobertura de ortoimagens em mosaico. | MosaicElement | voidable |

**Restrições do tipo de objeto geográfico “OrthoimageCoverage”**

O momento de aquisição da cobertura de ortoimagens deve ser fornecido através do atributo “phenomenonTime” ou da associação “mosaicElement”.

A dimensão da quadrícula utilizada deve ser sempre 2.

O atributo “domainExtent” deve estar preenchido, pelo menos, com um subtipo de “EX_GeographicExtent”.

Deve ser fornecido o sistema de referência de coordenadas utilizado para referenciar a quadrícula.

Todas as instâncias de “OrthoimageCoverage”, a que se refere uma instância de “OrthoimageCoverage” agregada, devem partilhar a mesma orientação dos eixos da quadrícula e o mesmo espaçamento de quadrículas em cada direção.

A origem da quadrícula deve ser descrita em duas dimensões.

Os valores no conjunto da gama de valores devem ser descritos pelo tipo “Integer”.

**3.2.2. Elemento de mosaico (MosaicElement)**

Tipo abstrato que identifica tanto a área contribuinte como o tempo de aquisição de uma ou várias imagens de entrada utilizadas para gerar uma cobertura de ortoimagens em mosaico.

Este tipo é abstrato.

**Atributos do tipo de objeto geográfico “MosaicElement”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| geometry | Representação geométrica que delimita espacialmente a data e a hora de aquisição das várias imagens de entrada que contribuem para o mosaico final. | GM_MultiSurface |  |
| phenomenonTime | Descrição da extensão da aquisição/observação no tempo da(s) imagem(ns) de entrada. | TM_Period |  |

**3.2.3. Elemento de mosaico único (SingleMosaicElement)**

Elemento de mosaico relativo a uma única imagem de entrada.

Este tipo é um subtipo de “MosaicElement”.

**Atributos do tipo de objeto geográfico “SingleMosaicElement”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| imageSourceReference | Referência à imagem de entrada. | CharacterString | voidable |

**3.2.4. Elemento de mosaico agregado (AggregatedMosaicElement)**

Elemento de mosaico relacionado com várias imagens de entrada que partilham o mesmo momento de aquisição a um determinado nível de definição (por exemplo, dia, mês).

Este tipo é um subtipo de “MosaicElement”.

**3.3. Tipos de dados**

**3.3.1. Agregação de ortoimagens (OrthoimageAggregation)**

Características geométricas da agregação de ortoimagens.

Este tipo é uma classe de associação.

**Atributos do tipo de dados “OrthoimageAggregation”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| contributingFootprint | Representação geométrica que delimita a área geográfica de uma cobertura de ortoimagens que contribui para a cobertura de ortoimagens agregadas. | GM_MultiSurface |  |

**3.4. Listas de códigos**

**3.4.1. Método de interpolação (InterpolationMethodValue)**

Lista dos códigos que identificam os métodos de interpolação que podem ser utilizados para avaliar as coberturas de ortoimagens.

Os valores autorizados para esta lista de códigos compreendem apenas os valores estabelecidos no quadro infra.

**Valores para a lista de códigos “InterpolationTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| nearestNeighbour | vizinho mais próximo | Interpolação ao vizinho mais próximo |
| bilinear | bilinear | Interpolação bilinear |
| biquadratic | biquadrática | Interpolação biquadrática |
| bicubic | bicúbica | Interpolação bicúbica |

**3.5 Requisitos específicos de categorias temáticas**

**3.5.1. Requisitos aplicáveis a identificadores de objetos externos**

|  | (1) | Se uma ortoimagem for atualizada com base em novos dados-fonte, deve ser atribuído aos objetos atualizados um novo identificador de objeto externo. |
|---|---|---|

**3.5.2. Requisitos aplicáveis a coberturas de ortoimagens**

<table> <tbody> <tr> <td></td> <td>(1)</td> <td>Em derrogação ao requisito estabelecido no ponto 2.2 do anexo II, pode ser utilizada qualquer quadrícula compatível com um dos seguintes sistemas de referência de coordenadas para a disponibilização de dados matriciais de ortoimagens: <table> <tbody> <tr> <td>—</td> <td>coordenadas geodésicas bidimensionais (latitude e longitude) baseadas num datum especificado no ponto 1.2. do anexo II e nos parâmetros da elipsoide do GRS80;</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>coordenadas planas baseadas no sistema de referência de coordenadas de projeção cónica conforme de Lambert do ETRS89;</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>coordenadas planas baseadas no sistema de referência de coordenadas de projeção transversa de Mercator do ETRS89;</td> </tr> </tbody> </table> Não deve ser utilizada a quadrícula referida no ponto 2.2.1 do anexo II.</td> </tr> </tbody> </table>

|  | (2) | A “pegada” de uma instância de “OrthoimageCoverage” deve ser espacialmente incluída na sua extensão geográfica que é descrita com a propriedade “domainExtent”. |
|---|---|---|

|  | (3) | O tipo de valor da propriedade de metadados representado pelo tipo de objeto geográfico “OrthoimageCoverage” deve ser definido como “OM_Observation” quando se utiliza o modelo de metadados “Observation and Measurement” definido na norma ISO 19156:2011. |
|---|---|---|

|  | (4) | Todas as instâncias de “OrthoimageCoverage”, a que se refere uma instância de “OrthoimageCoverage” agregada, devem ser coerentes. Isto significa que devem partilhar o mesmo tipo de gama de valores, sistema de referência de coordenadas e resolução. Devem também suportar o alinhamento de quadrículas, ou seja os pontos da quadrícula numa instância de “OrthoimageCoverage” devem estar alinhados com os pontos da quadrícula das outras instâncias de “OrthoimageCoverage”, para que as células da quadrícula não se sobreponham parcialmente. |
|---|---|---|

|  | (5) | A “pegada” de uma instância de “OrthoimageCoverage” referenciada por uma instância de “OrthoimageCoverage” agregada deve ser espacialmente incluída na sua própria pegada. |
|---|---|---|

|  | (6) | As “pegadas” de quaisquer duas instâncias de “OrthoimageCoverage” referenciadas pela mesma instância de “OrthoimageCoverage” agregada devem ser adjacentes ou não adjacentes. |
|---|---|---|

|  | (7) | A união das pegadas das instâncias de “OrthoimageCoverage” referenciadas pela mesma instância de “OrthoimageCoverage” agregada deve determinar a “pegada” da instância de “OrthoimageCoverage” agregada. |
|---|---|---|

**3.5.3. Requisitos aplicáveis a elementos de mosaico**

|  | (1) | Todos os elementos de mosaico relacionados com uma instância de “OrthoimageCoverage” devem ser do mesmo tipo, ou seja, “SingleMosaicElement” ou “AggregatedMosaicElement”. |
|---|---|---|

|  | (2) | As geometrias que delimitam quaisquer duas instâncias de “MosaicElement” relacionadas com a mesma instância de “OrthoimageCoverage” devem ser adjacente ou não adjacentes. |
|---|---|---|

|  | (3) | A união das geometrias que delimitam todas as instâncias do “MosaicElement” relacionadas com a mesma instância de “OrthoimageCoverage” deve incluir a sua “pegada” e estar contida na sua extensão de domínio geográfico. |
|---|---|---|

**3.5.4. Requisitos aplicáveis a sistemas de referência**

|  | (1) | Os dados relacionados com a categoria temática de dados geográficos “Ortoimagens” devem ser limitados a geometrias bidimensionais. |
|---|---|---|

|  | (2) | Serão utilizados apenas sistemas de referência de coordenadas bidimensionais para representar conjuntos de dados de ortoimagens INSPIRE. |
|---|---|---|

**3.5.5. Requisitos aplicáveis à qualidade dos dados**

|  | (1) | As medidas “erro médio quadrático em X” (root mean square error in X - RMSE-x) e “erro médio quadrático em Y” (root mean square error in Y - RMSE-Y) devem ser fornecidas em conjunto quando utilizadas para avaliar a posição dos dados matriciais presentes nos dados de ortoimagens. |
|---|---|---|

**3.6. Camadas**

**Camadas para a categoria temática de dados geográficos “Ortoimagens”**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| OI.OrthoimageCoverage | cobertura de ortoimagens | OrthoimageCoverage |
| OI.MosaicElement | elemento de mosaico | MosaicElement |

**4. GEOLOGIA**

**4.1. Estrutura da categoria temática de dados geográficos “Geologia”**

Os tipos especificados para a categoria temática de dados geográficos “Geologia” estão estruturados nos seguintes pacotes:

— Geologia (Geology)

— Geofísica (Geophysics)

— Hidrogeologia (Hydrogeology)

**4.2. Geologia**

**4.2.1. Tipos de objetos geográficos**

O pacote “Geologia” contém os seguintes tipos de objetos geográficos:

— Característica geomorfológica antropogénica

— Furo

— Dobra

— Coleção geológica

— Evento geológico

— Característica geológica

— Estrutura geológica

— Unidade geológica

— Característica geomorfológica

— Característica cartográfica

— Intervalo cartográfico

— Característica geomorfológica natural

— Estrutura de deslocamento de corte

**4.2.1.1. Característica geomorfológica antropogénica (AnthropogenicGeomorphologicFeature)**

Uma característica geomorfológica (ou seja, configuração do terreno) que foi criada pela atividade humana.

Este tipo é um subtipo de “GeomorphologicFeature”.

**Atributos do tipo de objeto geográfico “AnthropogenicGeomorphologicFeature”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| anthropogenicGeomorphologicFeatureType | Termos utilizados para descrever o tipo de uma característica geomorfológica. | AnthropogenicGeomorphologicFeatureTypeValue |  |

**4.2.1.2. Furo (Borehole)**

Furo é o termo genérico para designar qualquer perfuração de pequena largura no solo.

**Atributos do tipo de objeto geográfico “Borehole”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| boreholeLength | Comprimento do furo. | Quantity | voidable |
| elevation | Altura acima do datum do emboquilhamento do furo. | DirectPosition | voidable |
| location | Localização do emboquilhamento do furo. | GM_Point |  |
| purpose | Objetivo da realização do furo. | BoreholePurposeValue | voidable |
| downholeGeometry | Geometria do fundo do furo | GM_Curve | voidable |

**Associações do tipo de objeto geográfico “Borehole”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| logElement | Instâncias de “MappedFeature” 1-D que são intervalos registados (interpretados) dentro de um furo. | MappedInterval | voidable |

**4.2.1.3. Dobra (Fold)**

Uma ou mais camadas, superfícies ou linhas sistematicamente curvas numa massa rochosa.

Este tipo é um subtipo de “GeologicStructure”.

**Atributos do tipo de objeto geográfico “Fold”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| profileType | Tipo da dobra. | FoldProfileTypeValue | voidable |

**4.2.1.4. Coleção geológica (GeologicCollection)**

Uma coleção de objetos geológicos ou geofísicos.

**Atributos do tipo de objeto geográfico “GeologicCollection”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| name | Nome da coleção. | CharacterString |  |
| collectionType | Tipo da coleção. | CollectionTypeValue |  |
| reference | Referência à coleção. | DocumentCitation | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

**Associações do tipo de objeto geográfico “GeologicCollection”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| geophObjectSet | Um membro de “GeophObjectSet” da coleção geológica. | GeophObjectSet | voidable |
| geophObjectMember | Um “GeophObjectMember” da coleção geológica. | GeophObject | voidable |
| boreholeMember | Um membro de “Borehole” de uma coleção geológica. | Borehole | voidable |
| mapMember | Um membro de “MappedFeature” de uma coleção geológica. | MappedFeature | voidable |

**4.2.1.5. Evento geológico (GeologicEvent)**

Um evento identificável durante o qual um ou mais processos geológicos alteram entidades geológicas.

**Atributos do tipo de objeto geográfico “GeologicEvent”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| name | Nome do evento geológico. | CharacterString | voidable |
| eventEnvironment | Contexto físico em que o evento geológico ocorre. | EventEnvironmentValue | voidable |
| eventProcess | O ou os processos que ocorreram durante o evento geológico. | EventProcessValue | voidable |
| olderNamedAge | Limite mais antigo da idade do evento geológico. | GeochronologicEraValue | voidable |
| youngerNamedAge | Limite mais recente da idade do evento geológico. | GeochronologicEraValue | voidable |

**4.2.1.6. Característica geológica (GeologicFeature)**

Uma característica geológica conceptual que se supõe existir de forma coerente no mundo.

Este tipo é abstrato.

**Atributos do tipo de objeto geográfico “GeologicFeature”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| name | Nome da característica geológica. | CharacterString | voidable |

**Associações do tipo de objeto geográfico “GeologicFeature”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| themeClass | Classificação temática da característica geológica. | ThematicClass | voidable |
| geologicHistory | Associação que relaciona um ou mais eventos geológicos com uma característica geológica para descrever a sua idade ou história geológica. | GeologicEvent | voidable |

**4.2.1.7. Estrutura geológica (GeologicStructure)**

Uma configuração de matéria na Terra baseada na falta de homogeneidade, no padrão ou na fratura passível de descrição num material terrestre.

Este tipo é um subtipo de “GeologicFeature”.

Este tipo é abstrato.

**4.2.1.8. Unidade geológica (GeologicUnit)**

Um volume de rocha com características distintas.

Este tipo é um subtipo de “GeologicFeature”.

**Atributos do tipo de objeto geográfico “GeologicUnit”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geologicUnitType | Tipo da unidade geológica. | GeologicUnitTypeValue |  |

**Associações do tipo de objeto geográfico “GeologicUnit”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| composition | Descreve a composição da unidade geológica. | CompositionPart | voidable |

**4.2.1.9. Característica geomorfológica (GeomorphologicFeature)**

Um tipo de objeto geográfico abstrato que descreve a forma e a natureza da superfície terrestre da Terra (ou seja, uma configuração do terreno).

Este tipo é um subtipo de “GeologicFeature”.

Este tipo é abstrato.

**4.2.1.10. Característica cartográfica (MappedFeature)**

Uma representação espacial de uma “GeologicFeature”

**Atributos do tipo de objeto geográfico “MappedFeature”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| shape | Geometria da característica cartográfica. | GM_Object |  |
| mappingFrame | Superfície sobre a qual a característica cartográfica está projetada. | MappingFrameValue |  |

**Associações do tipo de objeto geográfico “MappedFeature”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| specification | Associação descritiva que liga a característica cartográfica a uma noção de característica geológica. | GeologicFeature |  |

**4.2.1.11. Intervalo cartográfico (MappedInterval)**

Um tipo especial de característica cartográfica cuja forma é um intervalo 1-D e que utiliza o sistema de referência geográfica do furo que a contém.

Este tipo é um subtipo de “MappedFeature”.

**4.2.1.12. Característica geomorfológica natural (NaturalGeomorphologicFeature)**

Característica geomorfológica (ou seja, configuração do terreno) que foi gerada pelos processos naturais da Terra.

Este tipo é um subtipo de “GeomorphologicFeature”.

**Atributos do tipo de objeto geográfico “NaturalGeomorphologicFeature”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| naturalGeomorphologicFeatureType | Tipo da característica geomorfológica natural. | NaturalGeomorphologicFeatureTypeValue |  |
| activity | Nível de atividade da característica geomorfológica natural. | GeomorphologicActivityValue | voidable |

**4.2.1.13. Estrutura de deslocamento de corte (ShearDisplacementStructure)**

Estruturas de estilo friável a dúctil ao longo das quais ocorreram deslocamentos.

Este tipo é um subtipo de “GeologicStructure”.

**Atributos do tipo de objeto geográfico “ShearDisplacementStructure”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| faultType | Refere-se a um vocabulário de termos que descrevem o tipo de estrutura de deslocamento de corte. | FaultTypeValue |  |

**4.2.2. Tipos de dados**

**4.2.2.1. Parte da composição (CompositionPart)**

A composição de uma unidade geológica em termos de constituintes litológicos.

**Atributos do tipo de dados “CompositionPart”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| material | Material que compõe uma parte ou a totalidade da unidade geológica. | LithologyValue |  |
| proportion | Quantidade que especifica a fração da unidade geológica composta pelo material. | QuantityRange | voidable |
| role | Relação da parte da composição com a composição da unidade geológica no seu todo. | CompositionPartRoleValue |  |

**4.2.2.2. Classe temática (ThematicClass)**

Um classificador temático genérico para permitir a reclassificação de Características Geológicas com classes definidas pelos utilizadores adequadas para mapas temáticos.

**Atributos do tipo de dados “ThematicClass”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| themeClass | Valor da classe temática. | ThematicClassValue |  |
| themeClassification | Classificação utilizada. | ThematicClassificationValue |  |

**4.2.3. Listas de códigos**

**4.2.3.1. Tipo de característica geomorfológica antropogénica (AnthropogenicGeomorphologicFeatureTypeValue)**

Tipos de características geomorfológicas antropogénicas.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “AnthropogenicGeomorphologicFeatureTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| artificialCollapsedDepression | depressão artificial colapsada | Bacia colapsada, normalmente uma depressão fechada, que é o resultado direto do afundamento da superfície associado à exploração mineira subterrânea ou em túnel. |
| artificialDrainage | drenagem artificial | Rede construída pelo homem principalmente para baixar ou controlar o lençol freático local. |
| artificialLevee | dique artificial | Aterro artificial construído ao longo da margem de um curso de água ou de um braço do mar para proteger as terras contra inundações ou para confinar o caudal no seu canal. |
| dredgedChannel | canal dragado | Área de águas profundas aproximadamente linear formada por uma operação de dragagem para fins de navegação |
| dump | descarga | Área com acumulações ou pilhas lisas ou irregulares de resíduos de rochas, material terroso ou detritos gerais que é incapaz, sem uma profunda recuperação, de abrigar plantas. |
| fill | terras de preenchimento | Depósitos construídos pelo homem constituídos por materiais de terras naturais e/ou resíduos utilizados para aterrar uma depressão, alargar a extensão das margens para dentro de uma massa de água ou construir barragens. |
| impactCraterAnthropogenic | cratera de impacto (antropogénica) | Depressão geralmente circular ou elíptica formada pelo impacto a hipervelocidade de um projétil experimental ou explosivo em material terroso ou rochoso. |
| landfillSite | sítio de aterro | Instalação de eliminação de resíduos utilizada para a deposição controlada de resíduos acima ou abaixo da superfície. |
| levelledLand | terreno nivelado | Área de terreno, geralmente um campo, que foi mecanicamente aplanado ou alisado para facilitar práticas de gestão, como a rega por alagamento. |
| openpitMine | mina a céu aberto | Depressão relativamente vasta resultante da escavação de material e da redistribuição das terras de cobertura associada a operações de exploração mineira à superfície. |
| pit | poço | Depressão, vala ou poço escavado para extrair gravilha, areia ou outros materiais para fins de construção de estradas ou outros; um tipo de escavação de empréstimo de terras. |
| quarry | pedreira | Áreas de escavação, a céu aberto, geralmente para a extração de pedra. |
| reclaimedLand | terreno recuperado | Área de terreno composta por materiais terrosos de enchimento que foram colocados e modelados de forma a se aproximarem dos contornos naturais do terreno, geralmente em consequência de ações de valorização dos solos após operações mineiras. Ou área de terreno, normalmente submersa no seu estado natural, que tem sido protegida por estruturas artificiais e drenada para fins agrícolas ou outros. |
| reservoirLake | lago reservatório | Massa de águas interiores permanentemente paradas, geralmente de água doce, que ocupa uma depressão na superfície da Terra fechada por uma barragem. |
| spoilBank | desentulho | Banco, monte ou outra acumulação artificial de detritos rochosos e depósitos de descarga de terras retiradas de valas, minas a céu aberto ou outros trabalhos de escavação. |
| subsidenceAreaAnthropogenic | área de subsidência (antropogénica) | Área sujeita a um processo da aluimento induzido por atividades antropogénicas, por exemplo, a exploração mineira de subsuperfície, a escavação de túneis e a extração de hidrocarbonetos ou águas subterrâneas. |

**4.2.3.2. Finalidade do furo (BoreholePurposeValue)**

Fins para os quais foi feito o furo.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

Esta lista de códigos é hierárquica.

**Valores para a lista de códigos “BoreholePurposeValue”**

<table> <tbody> <tr> <td>Valor</td> <td>Nome</td> <td>Definição</td> <td>Parent</td> </tr> <tr> <td>geologicalSurvey</td> <td>levantamento geológico</td> <td>Exame global das entidades geológicas de uma área.</td> <td></td> </tr> <tr> <td>explorationExploitationRawMaterial</td> <td>prospeção e exploração de matérias-primas</td> <td>Descoberta e identificação de recursos minerais, incluindo a avaliação da sua importância e a avaliação dos seu potencial económico.</td> <td></td> </tr> <tr> <td>explorationExploitationEnergyResources</td> <td>prospeção e exploração de recursos energéticos</td> <td>Exame da subsuperfície quanto à existência de recursos energéticos fósseis e planeamento da sua extração.</td> <td></td> </tr> <tr> <td>hydrocarbonProduction</td> <td>produção de hidrocarbonetos</td> <td>Produção de óleo de petróleo e/ou gás</td> <td>explorationExploitationRawMaterial</td> </tr> <tr> <td>hydrocarbonExploration</td> <td>prospeção de hidrocarbonetos</td> <td>Prospeção numa área não comprovada a fim de proceder a ensaios para um novo campo, uma nova jazida, um reservatório com maior profundidade ou um reservatório com menor profundidade.</td> <td>explorationExploitationRawMaterial</td> </tr> <tr> <td>hydrocarbonAppraisal</td> <td>apreciação de hidrocarbonetos</td> <td>Avaliação das características de uma acumulação comprovada de hidrocarbonetos.</td> <td>explorationExploitationRawMaterial</td> </tr> <tr> <td>geothermalEnergy</td> <td>energia geotérmica, permutadores de calor geotérmicos</td> <td>Prospeção relacionada com a utilização de recursos de energia geotérmica e conceção de bombas de calor geotérmicas.</td> <td>explorationExploitationRawMaterial</td> </tr> <tr> <td>heatStorage</td> <td>armazenamento de calor</td> <td>Poço para permitir a utilização do subsolo para o armazenamento de calor.</td> <td>geothermalEnergy</td> </tr> <tr> <td>mineralExplorationExtraction</td> <td>prospeção e extração mineira</td> <td>Poço perfurado para fins de localização e/ou extração de recursos minerais a partir da subsuperfície, geralmente através da injeção e/ou extração de fluidos que contêm minerais.</td> <td>explorationExploitationRawMaterial</td> </tr> <tr> <td>explorationExploitationNonmetallicMineralDepo MineralDepositGroupValue sits</td> <td>prospeção e exploração de depósitos minerais não metálicos</td> <td>Prospeção no que diz respeito à disponibilidade e planeamento da escavação de depósitos de minerais não metálicos principalmente para as indústrias de construção, pedras para a construção, cimentos, cerâmica ou vidro.</td> <td>explorationExploitationRawMaterial</td> </tr> <tr> <td>disposal</td> <td>eliminação</td> <td>Poço, frequentemente um poço de petróleo ou de gás esgotado, no qual podem ser injetados fluidos de resíduos com vista à sua eliminação em condições de segurança.</td> <td></td> </tr> <tr> <td>explorationNaturalUndergroundStorage</td> <td>prospeção de espaço subterrâneo natural para armazenamento</td> <td>Exame da capacidade da subsuperfície para armazenar vários materiais.</td> <td></td> </tr> <tr> <td>waterSupply</td> <td>abastecimento de água</td> <td>Abastecimento de água em geral.</td> <td></td> </tr> <tr> <td>drinkingWaterSupply</td> <td>abastecimento de água potável</td> <td>Construção de poços de água potável.</td> <td>waterSupply</td> </tr> <tr> <td>industrialWaterSupply</td> <td>abastecimento de águas industriais</td> <td>Construção de poços para o abastecimento de água para fins industriais.</td> <td>waterSupply</td> </tr> <tr> <td>aquaculture</td> <td>aquacultura</td> <td>Para abastecimento de água para fins aquícolas.</td> <td>waterSupply</td> </tr> <tr> <td>irrigation</td> <td>irrigação</td> <td>Construção de poços para fins de irrigação.</td> <td>waterSupply</td> </tr> <tr> <td>emergencyWaterSupply</td> <td>abastecimento de água de emergência</td> <td>Construção de poços para abastecimento de água de emergência.</td> <td>waterSupply</td> </tr> <tr> <td>contingencyWaterSupply</td> <td>abastecimento de água para contingências</td> <td>Abastecimento de águas de reserva em caso de deficiência das águas.</td> <td>waterSupply</td> </tr> <tr> <td>geophysicalSurvey</td> <td>levantamento geofísico</td> <td>Exame das propriedades geofísicas da subsuperfície.</td> <td></td> </tr> <tr> <td>shotHole</td> <td>furo para tiro</td> <td>Em ligação com sondagens sísmicas, são carregados explosivos em furos para tiro.</td> <td>geophysicalSurvey</td> </tr> <tr> <td>flowingShot</td> <td>furo artesiano</td> <td>Furo aberto para fins sísmicos que penetra numa fonte de água subterrânea com pressão suficiente para provocar um “transbordamento” de água no furo.</td> <td>shotHole</td> </tr> <tr> <td>hydrogeologicalSurvey</td> <td>levantamento hidrogeológico, gestão da água</td> <td>Exame do débito das águas subterrâneas, das propriedades químicas das águas subterrâneas e do transporte de partículas, solutos e energia, bem como gestão da utilização sustentável dos recursos hídricos subterrâneos.</td> <td></td> </tr> <tr> <td>geotechnicalSurvey</td> <td>levantamento geotécnico, caracterização do local de construção</td> <td>Estudos geotécnicos executados para obter informações sobre as propriedades físicas e mecânicas do solo e das rochas circundantes a fim de projetar os trabalhos de terraplenagem e fundações para as estruturas previstas e para a reparação de danos a terraplanagens e estruturas causados por condições da subsuperfície.</td> <td></td> </tr> <tr> <td>geochemicalSurvey</td> <td>análises e levantamentos geoquímicos</td> <td>Exame das propriedades químicas da formação rochosa e/ou dos fluidos que nela circulam.</td> <td></td> </tr> <tr> <td>pedologicalSurvey</td> <td>levantamento pedológico</td> <td>Estudo para caracterizar os tipos de solos.</td> <td></td> </tr> <tr> <td>environmentalMonitoring</td> <td>monitorização do ambiente</td> <td>Monitorização da química e do nível das águas subterrâneas.</td> <td></td> </tr> <tr> <td>pollutionMonitoring</td> <td>monitorização da poluição</td> <td>Monitorização de sítios de poluição conhecidos.</td> <td>environmentalMonitoring</td> </tr> <tr> <td>waterQualityMonitoring</td> <td>monitorização da qualidade da água</td> <td>Monitorização para avaliar a natureza e a distribuição de poluentes e contaminantes nas águas subterrâneas; a natureza e a distribuição de constituintes químicos de ocorrência natural; as condições hidrológicas à subsuperfície e as propriedades hidráulicas dos estratos na medida em que estejam relacionadas com a circulação de poluentes e contaminantes.</td> <td>environmentalMonitoring</td> </tr> <tr> <td>groundwaterLevelMonitoring</td> <td>monitorização do nível das águas subterrâneas</td> <td>Construção de um indicador de nível para registar as alterações do nível das águas subterrâneas.</td> <td>environmentalMonitoring</td> </tr> <tr> <td>dewatering</td> <td>secagem</td> <td>Secagem é a eliminação da água do solo ou de materiais sólidos por meio de classificação por via húmida, centrifugação, filtração ou processos similares de separação sólidos-líquidos. Remoção ou drenagem de água do leito de um rio, de um local de construção, ensecadeira, ou poço de mina, por bombagem ou evaporação.</td> <td></td> </tr> <tr> <td>mitigation</td> <td>mitigação</td> <td>Descida do nível das águas subterrâneas para evitar que o lençol freático atinja sítios poluídos.</td> <td>dewatering</td> </tr> <tr> <td>remediation</td> <td>reabilitação</td> <td>Reabilitação em geral. A eliminação da poluição ou de contaminantes das águas subterrâneas, do solo e de outras rochas</td> <td></td> </tr> <tr> <td>thermalCleaning</td> <td>aspersão, depuração térmica</td> <td>Um tipo de reabilitação. Depuração in situ do solo utilizando calor ou vapor de água.</td> <td>remediation</td> </tr> <tr> <td>recharge</td> <td>recarga</td> <td><table> <tbody> <tr> <td>a)</td> <td>Poços de recarga de aquíferos: Utilizados para recarregar aquíferos esgotados injetando água a partir de uma variedade de fontes, como lagos, cursos de água, instalações de tratamento de águas residuais urbanas, outros aquíferos, etc.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>b)</td> <td>Poços de barreira à intrusão de água salina: Utilizados para injetar água em aquíferos de água doce a fim de evitar a intrusão de água salgada em aquíferos de água doce.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>c)</td> <td>Poços de controlo da subsidência: Utilizados para injetar fluidos numa zona não produtora de petróleo ou de gás a fim de reduzir ou eliminar a subsidência associada ao excesso de extração de água doce.</td> </tr> </tbody> </table></td> <td></td> </tr> </tbody> </table>

**4.2.3.3. Tipo de coleção (CollectionTypeValue)**

Tipos de coleções de objetos geológicos e geofísicos

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “CollectionTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| boreholeCollection | coleção de furos | Coleção de furos |
| geologicalModel | modelo geológico | Coleção de objetos para um modelo geográfico geológico 3D |
| geologicalMap | carta geológica | Coleção de características para uma carta geológica que descreve unidades geológicas, estruturas, características geomorfológicas, etc. |
| geophysicalObjectCollection | coleção de objetos geofísicos | Coleção de objetos geofísicos |

**4.2.3.4. Função da parte da composição (CompositionPartRoleValue)**

As funções que uma parte da composição desempenha numa unidade geológica.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

Esta lista de códigos é hierárquica.

**Valores para a lista de códigos “CompositionPartRoleValue”**

| Valor | Nome | Definição | Parent |
|---|---|---|---|
| onlyPart | única parte | Toda a unidade descrita é composta por uma única parte ou constituinte. |  |
| partOf | parte de | A função da parte da unidade geológica não é conhecida de forma mais detalhada. |  |
| facies | fácies | Representa uma massa de rocha específica que é uma variante lateral de uma unidade litostratigráfica ou uma variante de uma unidade litodémica. | partOf |
| inclusion | inclusão | A parte constituinte da unidade geológica está presente como massas geralmente com limites bem definidos encerradas dentro de uma matriz de outro material. | partOf |
| lithosome | litosoma | Tipo de massa de rochas com múltiplas ocorrências numa única unidade geológica. Massa de rocha de caráter uniforme, caracterizada pela geometria, composição e estrutura interna. | partOf |
| stratigraphicPart | parte estratigráfica | Parte da unidade geológica que ocupa uma posição estratigráfica específica dentro de uma unidade geográfica. | partOf |
| unspecifiedPartRole | função da parte não especificada | Parte de unidade geológica com uma função não especificada. | partOf |

**4.2.3.5. Ambiente do evento (EventEnvironmentValue)**

Termos para os ambientes geológicos no âmbito dos quais ocorrem eventos geológicos.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

Os fornecedores de dados podem também utilizar os valores mais restritos especificados para esta lista de códigos no Documento de Orientação Técnica INSPIRE sobre Geologia.

**Valores para a lista de códigos “EventEnvironmentValue”**

| Valor | Nome | Definição |
|---|---|---|
| earthInteriorSetting | condições no interior da Terra | Ambientes geológicos dentro da massa sólida da Terra. |
| earthSurfaceSetting | condições na superfície da Terra | Ambientes geológicos sobre a superfície da Terra sólida. |
| extraTerrestrialSetting | condições extraterrestres | Material com origem fora da Terra ou da sua atmosfera. |
| tectonicallyDefinedSetting | condições definidas de forma tectónica | Condições definidas por relações com placas tectónicas à superfície ou no interior da Terra. |

**4.2.3.6. Processo do evento (EventProcessValue)**

Termos que especificam o processo ou processos que ocorreram durante um evento.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

Os fornecedores de dados podem também utilizar os valores mais restritos especificados para esta lista de códigos no Documento de Orientação Técnica INSPIRE sobre Geologia.

**Valores para a lista de códigos “EventProcessValue”**

| Valor | Nome | Definição |
|---|---|---|
| bolideImpact | impacto de bólide | O impacto de um corpo extraterrestre na superfície da Terra. |
| deepWaterOxygenDepletion | Depleção do oxigénio nas águas profundas | Processo de remoção de oxigénio da parte profunda de uma massa de água. |
| deformation | deformação | Movimento de massas rochosas por deslocação em zonas de falha ou cisalhamento, ou alteração na forma de uma massa de material terrestre. |
| diageneticProcess | processo diagenético | Qualquer processo químico, físico ou biológico que afeta um material terrestre sedimentar após deposição inicial, e durante ou após litificação, com exclusão da meteorização e metamorfismo. |
| extinction | extinção | Processo de desaparecimento de uma espécie ou de um táxon superior, de modo a já não existir em lugar algum nem em registos fósseis subsequentes. |
| geomagneticProcess | processo geomagnético | Processo que resulta na alteração do campo magnético da Terra. |
| humanActivity | atividade humana | Processos de modificação da terra realizados pelo homem para produzir características geológicas. |
| magmaticProcess | processo magmático | Processo que envolve rochas em fusão (magma). |
| metamorphicProcess | processo metamórfico | Ajustamento mineralógico, químico e estrutural de rochas sólidas a condições físicas e químicas que diferem das condições em que as rochas em causa tiveram origem e que estão, em geral, a ser impostas em profundidade, abaixo das zonas de superfície de meteorização e cementação. |
| seaLevelChange | alteração do nível do mar | Processo de alteração do nível médio do mar relativamente a um datum. |
| sedimentaryProcess | processo sedimentar | Fenómeno que altera a distribuição ou propriedades físicas de sedimentos à superfície ou próximo da superfície da Terra. |
| speciation | especiação | Processo que resulta no aparecimento de novas espécies. |
| tectonicProcess | processo tectónico | Processos relacionados com a interação entre - ou a deformação de - placas rígidas que formam a crosta terrestre. |
| weathering | meteorização | Processo ou grupo de processos através dos quais os materiais terrosos expostos aos agentes atmosféricos à superfície ou perto da superfície da Terra sofrem alterações ao nível da cor, textura, composição, consistência ou forma, com pouco ou nenhum transporte do material solto ou alterado. Estes processos incluem tipicamente oxidação, hidratação e lixiviação de constituintes solúveis. |

**4.2.3.7. Tipo de falha (faulttypevalue)**

Termos utilizados para descrever o tipo de estrutura de deslocamento de corte.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

Os fornecedores de dados podem também utilizar os valores mais restritos especificados para esta lista de códigos no Documento de Orientação Técnica INSPIRE sobre Geologia.

Esta lista de códigos é hierárquica.

**Valores para a lista de códigos “FaultTypeValue”**

| Valor | Nome | Definição | Parent |
|---|---|---|---|
| fault | falha | Superfície discreta, ou zona de superfícies discretas, com alguma espessura que separa dois blocos de rocha e ao longo da qual uma massa deslizou sobre a outra. |  |
| extractionFault | falha convergente | Falha cujos blocos se aproximaram substancialmente entre si na direção perpendicular à falha. | fault |
| highAngleFault | falha de grande ângulo | Falha que mergulha, pelo menos, 45 graus em mais de metade da sua extensão conhecida, para a qual não é explicitamente especificado deslizamento ou separação. | fault |
| lowAngleFault | falha de pequeno ângulo | Falha que mergulha menos de 45 graus ao longo de mais de metade da extensão conhecida da falha. | fault |
| obliqueSlipFault | falha oblíqua | Falha com um vetor de deslizamento com relações entre 10 para 1 e 1 para 10 das componentes paralelas à direção e inclinação, pelo menos, num local ao longo do traçado cartografado da falha. | fault |
| reverseFault | falha inversa | Falha em que o vetor de deslizamento tem componente paralela à inclinação mais de 10 vezes superior à componente paralela à direção em, pelo menos, um local ao longo do traçado cartografado da falha, e a falha mergulha consistentemente no mesmo sentido com o teto deslocado para cima relativamente ao muro ao longo de, pelo menos, metade do traçado cartografado da falha. | fault |
| scissorFault | falha rotacional | Falha em que se verifica um rejeito ou separação cada vez maior ao longo da direção da falha a partir de um ponto inicial de rejeito nulo, com sinal oposto do rejeito em sentidos opostos. | fault |
| strikeSlipFault | falha deslizante | Falha com um vetor de deslizamento em que a componente paralela à direção é mais de 10 vezes superior à componente paralela à inclinação em, pelo menos, um local ao longo do traçado cartografado da falha. | fault |

**4.2.3.8. Tipo de perfil da dobra (FoldProfileTypeValue)**

Termos que especificam o tipo de dobra.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “FoldProfileTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| anticline | anticlinal | Dobra, geralmente convexa para cima, cujo núcleo contém rochas mais antigas do ponto de vista estratigráfico. |
| antiform | antiforma | Qualquer dobra convexa para cima, côncava para baixo. |
| syncline | sinclinal | Dobra cujo núcleo contém as rochas mais recentes do ponto de vista estratigráfico; é geralmente uma dobra côncava para cima. |
| synform | sinforma | Qualquer dobra cujos flancos se fecham para baixo. |

**4.2.3.9. Período geocronológico (GeochronologicEraValue)**

Termos que especificam unidades geológicas temporais reconhecidas.

Os valores autorizados para esta lista de códigos incluem os valores constantes em Cohen, K.M., Finney, S. & Gibbard, P.L., International Chronostratigraphic Chart, August 2012, International Commission on Stratigraphy of the International Union of Geological Sciences, 2012 e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

Os fornecedores de dados podem utilizar os valores adicionais para rochas pré-câmbricas e unidades do Quaternáro especificados no Documento de Orientação Técnica INSPIRE sobre Geologia.

**4.2.3.10. Tipo de unidade geológica (GeologicUnitTypeValue)**

Termos que descrevem o tipo de unidade geológica.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

Esta lista de códigos é hierárquica.

**Valores para a lista de códigos “GeologicUnitTypeValue”**

| Valor | Nome | Definição | Parent |
|---|---|---|---|
| geologicUnit | unidade geológica | Tipo de unidade geológica que é desconhecido, não especificado, irrelevante, ou qualquer tipo não incluído no vocabulário. |  |
| allostratigraphicUnit | unidade aloestratigráfica | Unidade geológica definida por superfícies delimitadoras. Não necessariamente estratificada. | geologicUnit |
| alterationUnit | unidade de alteração | Unidade geológica definida pelo processo de alteração. | geologicUnit |
| biostratigraphicUnit | unidade bioestratigráfica | Unidade geológica definida com base no conteúdo fóssil. | geologicUnit |
| chronostratigraphicUnit | unidade cronoestratigráfica | Unidade geológica que inclui todas as rochas formadas durante um intervalo específico de tempo geológico | geologicUnit |
| geophysicalUnit | unidade geofísica | Unidade geológica definida pelas suas características geofísicas. | geologicUnit |
| magnetostratigraphicUnit | unidade magnetoestratigráfica | Unidade geológica definida pelas suas características magnéticas. | geophysicalUnit |
| lithogeneticUnit | unidade litogenética | Unidade geológica definida por génese. A génese manifesta-se por propriedades do material, mas o material não é a propriedade definidora. | geologicUnit |
| artificialGround | solo artificial | Unidade geológica definida por génese que envolve ação humana direta para a deposição ou modificação do material. | lithogeneticUnit |
| excavationUnit | unidade de escavação | Unidade geológica definida por génese antropogénica que envolve escavação. | lithogeneticUnit |
| massMovementUnit | unidade de movimento de massas | Unidade geológica produzida por deslocação gravítica descendente de material e caracterizada pelo tipo de movimento que deu origem ao depósito e pela forma como os tipos de cada um dos movimentos presentes no depósito estão relacionados no tempo e no espaço. | lithogeneticUnit |
| lithologicUnit | unidade litológica | Unidade geológica definida por litologia independentemente das relações com outras unidades. | geologicUnit |
| lithostratigraphicUnit | unidade litoestratigráfica | Unidade geológica definida com base em propriedades litológicas observáveis e distintivas ou numa combinação de propriedades litológicas e relações estratigráficas. | geologicUnit |
| lithodemicUnit | unidade litodémica | unidade litoestratigráfica sem estratificação | lithostratigraphicUnit |
| lithotectonicUnit | unidade litotectónica | Unidade geológica definida com base em características estruturais ou de deformação, relações mútuas, origem ou evolução histórica. O material contido pode ser ígneo, sedimentar ou metamórfico. | geologicUnit |
| deformationUnit | unidade de deformação | Unidade litotectónica definida pelo estilo de deformação ou pela estrutura geológica característica observável no afloramento. | lithotectonicUnit |
| pedostratigraphicUnit | unidade pedoestratigráfica | Unidade geológica que representa um horizonte pedológico único numa sequência de estratos (consolidados ou não consolidados). | geologicUnit |
| polarityChronostratigraphicUnit | unidade de polaridade cronoestratigráfica | Unidade geológica definida pelo registo primário de polaridade magnética imposto quando a rocha foi depositada ou cristalizada durante um intervalo específico de tempo geológico. | geologicUnit |

**4.2.3.11. Atividade geomorfológica (GeomorphologicActivityValue)**

Termos que indicam o nível de atividade de uma característica geomorfológica.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “GeomorphologicActivityValue”**

| Valor | Nome | Definição |
|---|---|---|
| active | ativo | Processo geomorfológico que está atualmente em ação, ou que foi reativado há um período de tempo convencionalmente curto. |
| dormant | dormente | Processo geomorfológico que não apresentou sinais de atividade desde um período de tempo convencionalmente curto e que poderia ser reativado pelas suas causas originais ou desencadeado por causas induzidas, como as atividades antropogénicas. |
| reactivated | reativado | Um processo geomorfológico reativado é um processo geomorfológico ativo que esteve dormente. |
| stabilised | estabilizado | Um processo geomorfológico estabilizado é um processo inativo que tem sido protegido das suas causas originais por medidas corretivas. |
| inactive | inativo | Processo geomorfológico relicto ou fóssil. |

**4.2.3.12. Litologia (LithologyValue)**

Termos que descrevem a litologia.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

Os fornecedores de dados podem também utilizar os valores mais restritos especificados para esta lista de códigos no Documento de Orientação Técnica INSPIRE sobre Geologia.

Esta lista de códigos é hierárquica.

**Valores para a lista de códigos “LithologyValue”**

| Valor | Nome | Definição | Parent |
|---|---|---|---|
| compoundMaterial | material composto | Um material terrestre composto por uma agregação de partículas de material terrestre, incluindo possivelmente outros materiais compostos. |  |
| anthropogenicMaterial | material antropogénico | Material que se sabe ser de origem artificial (relacionada com a atividade humana); informação insuficiente para uma classificação mais detalhada. | compoundMaterial |
| anthropogenicConsolidatedMaterial | material consolidado antropogénico | Material consolidado que se sabe ser de origem artificial (relacionada com a atividade humana). | anthropogenicMaterial |
| anthropogenicUnconsolidatedMaterial | material não consolidado antropogénico | Material não consolidado que se sabe ser de origem artificial (relacionada com a atividade humana). | anthropogenicMaterial |
| breccia | brecha | Material granuloso composto por fragmentos angulares de rochas fraturadas; os fragmentos têm normalmente arestas vivas e cantos não desgastados. | compoundMaterial |
| compositeGenesisMaterial | material de génese compósita | Material em estado de consolidação não especificado formado por modificação geológica de materiais preexistentes fora do âmbito dos processos ígneos e sedimentares. | compoundMaterial |
| compositeGenesisRock | rocha de génese compósita | Rocha formada por modificação geológica de rochas preexistentes fora do âmbito de processos ígneos e sedimentares. | compositeGenesisMaterial |
| faultRelatedMaterial | material relacionado com uma falha | Material formado em resultado de uma falha friável, composto de uma matriz superior a 10 %; a matriz é material de granulação fina gerado por uma redução da sua granulometria de origem tectónica. | compositeGenesisMaterial |
| impactGeneratedMaterial | material gerado por impacto | Material com características indicativas de metamorfismo de choque, como sejam características de deformação planar microscópica com grãos ou cones de estilhaçamento, interpretados como sendo o resultado do impacto de um bólide extraterrestre. Inclui brechas e rochas fundidas. | compositeGenesisMaterial |
| materialFormedInSurficialEnvironment | material formado num ambiente à superfície | Material que é o produto de processos de meteorização em rochas ou depósitos preexistente, análogo a rochas hidrotermais ou metassomáticas, mas formado à temperatura e pressão ambientes da superfície da Terra. | compositeGenesisMaterial |
| rock | rocha | Agregado consolidado de um ou mais materiais terrestres, ou uma massa de material mineral indiferenciada ou de material orgânico sólido. | compoundMaterial |
| aphanite | rocha afanítica | Rocha com granulação demasiado fina para ser classificada de forma mais detalhada. | rock |
| sedimentaryRock | rocha sedimentar | Rocha formada por acumulação e cementação de materiais sólidos fragmentários depositados pelo ar, água ou gelo, ou em resultado de outros agentes naturais, como a precipitação a partir de uma solução, a acumulação de matéria orgânica, ou processos biogénicos, incluindo secreção por organismos. | rock |
| tuffite | tufo | Rocha constituída por mais de 50 % de partículas de origem piroclástica ou epiclástica indeterminada e menos de 75 % de partículas de origem claramente piroclástica. | rock |
| sedimentaryMaterial | material sedimentar | Material formado por acumulação de material fragmentário sólido depositado por ar, água ou gelo, ou material acumulado devido a outros agentes naturais, como precipitação química a partir de uma solução ou secreção por organismos. | compoundMaterial |
| carbonateSedimentaryMaterial | material sedimentar carbonatado | Material sedimentar em que, pelo menos, 50 % dos constituintes primários e/ou recristalizados são composto por um (ou mais) dos minerais carbonatados como a calcite, aragonite e dolomite, em partículas de origem intrabacia. | sedimentaryMaterial |
| chemicalSedimentaryMaterial | material sedimentar químico | Material sedimentar que é constituído por, pelo menos, 50 % de material produzido por processos químicos inorgânicos dentro da bacia de deposição. Inclui classes de sedimentos inorgânicos, siliciosos, carbonatados, evaporíticos, ricos em ferro e fosfatados. | sedimentaryMaterial |
| clasticSedimentaryMaterial | material sedimentar clástico | Material sedimentar num estado de consolidação não especificado em que, pelo menos, 50 % das partículas constituintes foram derivadas por erosão, meteorização ou perda de massa de materiais terrosos preexistentes e transportados para o local de deposição por agentes mecânicos como a água, o vento, o gelo e a gravidade. | sedimentaryMaterial |
| nonClasticSiliceousSedimentaryMaterial | material sedimentar silicioso não clástico | Material sedimentar que é constituído por, pelo menos, 50 % de material mineral silicatado, depositado diretamente por processos químicos ou biológicos na superfície de deposição, ou por partículas formadas por processos químicos ou biológicos na bacia de deposição. | sedimentaryMaterial |
| organicRichSedimentaryMaterial | material sedimentar rico em matéria orgânica | Material sedimentar em que 50 % ou mais do material sedimentar primário é constituído por carbono orgânico. | sedimentaryMaterial |
| igneousMaterial | material ígneo | Material terrestre formado em resultado de processos ígneos, por exemplo intrusão e arrefecimento de magma na crosta, erupção vulcânica. | compoundMaterial |
| fragmentalIgneousMaterial | material ígneo fragmentário | Material ígneo em estado de consolidação não especificado em que mais de 75 por cento da rocha consiste em fragmentos produzidos em resultado do processo ígneo de formação de rochas. | igneousMaterial |
| acidicIgneousMaterial | material ígneo ácido | Material ígneo com mais de 63 % de SiO2. | igneousMaterial |
| basicIgneousMaterial | Material ígneo básico | Material ígneo com 45 a 52 por cento de SiO2. | igneousMaterial |
| igneousRock | rocha ígnea | Rocha formada em resultado de processos ígneos, por exemplo, intrusão e arrefecimento de magma na crosta ou erupção vulcânica. | igneousMaterial |
| intermediateCompositionIgneousMaterial | material ígneo de composição intermédia | Material ígneo com 52 a 63 por cento de SiO2. | igneousMaterial |
| unconsolidatedMaterial | material não consolidado | “Compoundmaterial” composto por uma agregação de partículas que não aderem entre si de forma suficientemente forte para que o agregado possa ser considerado um sólido de pleno direito. | compoundMaterial |
| naturalUnconsolidatedMaterial | material não consolidado natural | Material não consolidado que se sabe ser de origem natural, ou seja, não de origem humana. | unconsolidatedMaterial |
| sediment | sedimento | Material não consolidado constituído por uma agregação de partículas transportadas ou depositadas por ar, água ou gelo, ou que se acumularam pela ação de outros agentes naturais, como a precipitação química, e que forma camadas na superfície da Terra. | naturalUnconsolidatedMaterial |

**4.2.3.13. Quadro cartográfico (MappingFrameValue)**

Termos que indicam a superfície sobre a qual é projetada a “MappedFeature”.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “MappingFrameValue”**

| Valor | Nome | Definição |
|---|---|---|
| baseOfQuaternary | base do Quaternário | Base do material sedimentar predominantemente não consolidado do período quaternário. |
| surfaceGeology | geologia de superfície | Substrato rochoso e depósitos superficiais que seriam visíveis se o solo que os recobre fosse removido ou que estão expostos na superfície topográfica. |
| topOfBasement | topo do soco rochoso | Superfície na crosta da Terra abaixo dos depósitos sedimentares ou vulcânicos, ou unidade rochosa transportada por um processo tectónico. |
| topOfBedrock | Topo do substrato rochoso | Superfície superior normalmente de rocha firme que pode aflorar na superfície topográfica ou estar coberta por depósitos não consolidados. |

**4.2.3.14. Tipo de característica geomorfológica natural (NaturalGeomorphologicFeatureTypeValue)**

Termos que descrevem o tipo de característica geomorfológica natural.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “NaturalGeomorphologicFeatureTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| naturalGeomorphologicFeature | característica geomorfológica natural | Característica geomorfológica produzida pela dinâmica natural. |
| drainagePattern | padrão de drenagem | Configuração ou disposição dos cursos de água numa área, incluindo ravinamento ou áreas de escoamento canalizado de primeira ordem, afluentes de ordem superior e cursos de água principais. |
| constructionalFeature | característica construtiva | Sítio de uma configuração do terreno que deve a sua origem, forma, posição ou caráter geral a processos de deposição (agradação), tais como a acumulação de sedimentos |
| destructionalFeature | característica destrutiva | Sítio de uma configuração do terreno que deve a sua origem, forma, posição ou caráter geral à remoção de material por processos de erosão e meteorização (degradação) resultantes do desgaste ou desagregação da superfície do terreno. |
| degradationFeature | característica de degradação | Característica geomorfológica resultante do desgaste ou desagregação, e da redução ou abaixamento geral, da superfície terrestre por processos naturais de meteorização e erosão, podendo-se inferir os processos de transporte de sedimentos. |
| relic | relíquia | Configuração do terreno que sobreviveu a degradação ou desintegração, ou que foi abandonada após o desaparecimento da maior parte da sua substância, como seja uma ilha remanescente. |
| exhumedFeature | característica exumada | Configurações do terreno, superfícies geomorfológicas ou paleossolos anteriormente soterrados que foram reexpostos pela erosão do manto que os cobria. |
| buriedFeature | característica soterrada | Configurações do terreno, superfícies geomorfológicas ou paleossolos cobertos por sedimentos mais recentes. |
| pediment | pedimento | Superfície erodida em declive suave gerada no sopé da encosta de um monte ou de uma montanha em recuo, geralmente com um perfil ligeiramente côncavo para cima, que atravessa estratos de rocha ou sedimentos que se estendem por debaixo das terras altas adjacentes. |
| erosional | características de erosão | Superfície terrestre moldada pela ação da erosão, especialmente por águas correntes. |
| hill | colina | Termo genérico que designa uma elevação do terreno de, pelo menos, 30 metros e de menos de 300 metros acima das terras baixas circundantes, geralmente com uma área nominal do cume relativa às encostas limítrofes, um perfil bem definido e arredondado e encostas com uma inclinação geralmente superior a 15 por cento. |
| interfluve | interflúvio | Componente geomorfológica das colinas que consiste no nível mais elevado comparativamente ou da área em ligeiro declive de uma colina; os flancos de encostas de colinas que sofrem a ação da erosão podem estreitar as zonas ou fundir-se resultando numa forma fortemente convexa. |
| crest | cumeada | Componente geomorfológica de colinas constituída por encostas convexas (perpendiculares à curva de nível) que formam a área superior estreita e aproximadamente linear de uma colina, crista ou outras terras altas em que os flancos convergiram a ponto de pouco ou nada restar do cume; dominada por processos de erosão, erosão aquática das encostas e processos de movimentos de massas e sedimentos. |
| headSlope | talude de cabeceira | Componente geomorfológica das colinas que consiste numa área lateralmente côncava de uma colina, especialmente à entrada de uma via de drenagem, que resulta em fluxos de escoamento superficial convergentes. |
| sideSlope | talude lateral | Componente geomorfológica das colinas constituída por uma área lateralmente plana de uma encosta, que resulta em fluxos de escoamento superficial predominantemente paralelos. As curvas de nível formam geralmente linhas retas. |
| noseSlope | talude de tergo | Componente geomorfológica das colinas constituída por uma projeção terminal (área lateralmente convexa) de uma colina, que resulta num escoamento superficial predominantemente divergente. As curvas de nível formam geralmente curvas convexas. |
| freeFace | face livre | Componente geomorfológica das colinas e montanhas constituída por um afloramento de rocha nua que solta fragmentos de rocha e outros sedimentos para a vertente coluvial imediatamente abaixo, e sendo geralmente mais inclinada que o ângulo do talude; observada mais frequentemente em posições nos contrafortes e em partes mais recuadas dos taludes, pode compreender a totalidade ou parte de um talude de tergo ou de um talude lateral. |
| baseSlope | pé do talude | Componente geomorfológica das colinas que consiste na encosta de côncava a linear (perpendicular à curva de nível) que, independentemente da forma lateral, é uma área que forma uma aba no sopé de uma colina dominada por processos coluviais e de erosão aquática e sedimentos. |
| mountain | montanha | Termo genérico que designa uma elevação do terreno a mais de 300 metros acima das terras baixas circundantes, geralmente com uma área nominal do cume relativa às encostas limítrofes e geralmente com vertentes com uma forte inclinação (superior a 25 %) com ou sem uma quantidade considerável de rocha nua exposta. |
| mountaintop | cume de montanha | Componente geomorfológica das montanhas que consiste na área mais elevada e comparativamente plana ou com uma inclinação suave, caracterizada por encostas relativamente pequenas e simples compostas por rocha nua, resíduos ou sedimentos coluviais transportados a curta distância. |
| mountainslope | talude de montanha | Parte de uma montanha entre o cume e o sopé. |
| mountainflank | flanco de montanha | Componente geomorfológica das montanhas caracterizada por longas e complexas partes recuadas dos taludes com uma inclinação comparativamente acentuada e composta por mantos de sedimentos coluviais, afloramentos rochosos ou bancos estruturais altamente diversos. |
| mountainbase | sopé da montanha | Componente geomorfológica das montanhas que consiste na aba ou cunha coluvial de forte a ligeiramente côncava na base das encostas da montanha. |
| depression | depressão | Qualquer parte da superfície da Terra relativamente cavada e especialmente uma área de terras baixas rodeadas por terreno mais elevado. |
| plain | planície | Qualquer área plana, de grande ou pequena dimensão, a uma baixa altitude; especificamente uma região extensa de terreno comparativamente liso e plano ou ligeiramente ondulante, que tem poucas ou nenhumas irregularidades superficiais proeminentes, mas que tem por vezes um declive considerável, e geralmente a baixa altitude relativamente às áreas circundantes. |
| tectonicStructural | características tectónicas e estruturais | Configurações do terreno e paisagens geomorfológicas relacionadas com estruturas de substratos rochosos regionais ou locais ou movimentos da crosta; e configurações do terreno e paisagens geomorfológicas relacionadas predominantemente com a erosão pela água, mas excluindo caudais permanentes com escoamento canalizado (ou seja, fluviais ou fluvioglaciares), ou erosão eólica. |
| volcanic | características vulcânicas | Configurações do terreno e paisagens geomorfológicas relacionadas com os processos a grande profundidade (ígneos) através dos quais o magma e gases associados penetram na crosta, emergem à superfície da Terra e são lançados na atmosfera. |
| hydrothermal | características hidrotermais | Configurações do terreno e paisagens geomorfológicas relacionadas com processos hidrotermais. |
| erosionSurface | superfície de erosão | Configurações do terreno e paisagens geomorfológicas relacionadas predominantemente com a erosão pela água, mas excluindo os caudais permanentes com escoamento canalizado (ou seja, fluviais ou fluvioglaciares), ou erosão eólica. |
| slopeGravitational | características de declives gravitacionais | Configurações do terreno e paisagens geomorfológicas relacionadas com ambientes em talude; configurações do terreno e paisagens geomorfológicas desenvolvidas sob a ação da força gravitacional. |
| nivalPeriglacialPermafrost | características nivais, periglaciais e de pergelissolo | Configurações do terreno e paisagens geomorfológicas relacionadas com ambientes climáticos frios, com neve e não glaciares; configurações do terreno e paisagens geomorfológicas que ocorrem na proximidade de glaciares e lençóis de gelo; configurações do terreno e paisagens geomorfológicas relativas ao terreno, solo ou rocha que se mantêm a uma temperatura igual ou inferior a 0° C durante, pelo menos, dois anos. |
| glacial | características glaciares, glaciofluviais, glaciolacustres e glaciomarinhas | Configurações do terreno e paisagens geomorfológicas relacionadas com ambientes glaciares, glaciofluviais, glaciolacustres e glaciomarinhos. |
| eolian | características eólicas | Configurações do terreno e paisagens geomorfológicas relacionadas com ambientes dominados pela ação do vento. |
| marineLittoralCoastalWetland | características de zonas húmidas marinhas, litorais e costeiras | Configurações do terreno e paisagens geomorfológicas relacionadas com a dinâmica das marés ou das ondas desenvolvidas em ambientes de zonas marinhas, marinhas de baixa profundidade, quase-litorais e litorais, e as relacionadas com zonas húmidas com vegetação e/ou de pouca profundidade. |
| karstChemicalWeathering | características de meteorização cársica e química | Configurações do terreno e paisagens geomorfológicas dominadas pela dissolução de minerais, e frequentemente, drenagem da subsuperfície. |
| alluvialFluvial | características aluviais e fluviais | Configurações do terreno e paisagens geomorfológicas predominantemente relacionadas com caudais concentrados (escoamento canalizado). |
| lacustrine | características lacustres | Configurações do terreno e paisagens geomorfológicas relacionadas com massas de águas interiores permanentes (lagos). |
| impact | características de impacto | Configurações do terreno e paisagens geomorfológicas relacionadas com o impacto de material de origem extraterrestre na superfície da Terra. |

**4.2.3.15. Classe temática (ThematicClassValue)**

Valores para a classificação temática das características geológicas.

Os valores autorizados para esta lista de códigos incluem eventuais valores definidos pelos fornecedores de dados.

**4.2.3.16. Classificação temática (ThematicClassificationValue)**

Lista de classificações temáticas para características geológicas.

Os valores autorizados para esta lista de códigos incluem eventuais valores definidos pelos fornecedores de dados.

**4.3. Geofísica**

**4.3.1. Tipos de objetos geográficos**

O pacote “Geofísica” contém os seguintes tipos de objetos geográficos:

— Campanha

— Medição geofísica

— Objeto geofísico

— Conjunto de objetos geofísicos

— Perfil geofísico

— Estação geofísica

— Faixa geofísica

— Geophysical Measurement

**4.3.1.1. Campanha (Campaign)**

Atividade geofísica que decorre durante um período de tempo limitado e numa área limitada para produzir medições geofísicas similares e processar os resultados ou modelos.

Este tipo é um subtipo de “GeophObjectSet”.

**Atributos do tipo de objeto geográfico “Campaign”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| campaignType | Tipo de atividade para a produção de dados. | CampaignTypeValue |  |
| surveyType | Tipo de levantamento geofísico. | SurveyTypeValue |  |
| client | Parte para a qual foram criados os dados. | RelatedParty | voidable |
| contractor | Parte através da qual os dados foram criados. | RelatedParty | voidable |

**Restrições do tipo de objeto geográfico “Campaign”**

O atributo da forma deve ser do tipo “GM_Surface”.

**4.3.1.2. Objeto geofísico (GeophObject)**

Uma classe genérica para objetos geofísicos.

Este tipo é um subtipo de “SF_SpatialSamplingFeature”.

Este tipo é abstrato.

**Atributos do tipo de objeto geográfico “GeophObject”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| citation | Citação de documentação geofísica. | DocumentCitation |  |
| projectedGeometry | Projeção 2D da característica na superfície do solo (como um ponto, curva ou polígono delimitador representativo) a utilizar por um serviço de visualização INSPIRE para visualizar a localização do objeto geográfico numa carta. | GM_Object |  |
| verticalExtent | Extensão vertical da gama de interesse. | EX_VerticalExtent | voidable |
| distributionInfo | Metadados de distribuição. | MD_Distributor | voidable |
| largerWork | Identificador de um maior conjunto de dados de trabalho, geralmente uma campanha ou projeto. | Identifier | voidable |

**Restrições do tipo de objeto geográfico “GeophObject”**

O atributo de “projectedGeometry” deve ser do tipo “GM_Point”, “GM_Curve” ou “GM_Surface”.

**4.3.1.3. Medição geofísica (GeophMeasurement)**

Um tipo genérico de objeto geográfico para medições geofísicas.

Este tipo é um subtipo de “GeophObject”.

Este tipo é abstrato.

**Atributos do tipo de objeto geográfico “GeophMeasurement”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| relatedModel | Identificador do modelo geofísico que foi criado a partir da medição. | Identifier | voidable |
| platformType | Plataforma a partir da qual foi efetuada a medição. | PlatformTypeValue |  |
| relatedNetwork | Nome de uma rede de observação nacional ou internacional a que pertence a instalação, ou à qual são comunicados os dados das medições. | NetworkNameValue | voidable |

**4.3.1.4. Conjunto de objetos geofísicos (GeophObjectSet)**

Uma classe genérica para coleções de objetos geofísicos.

Este tipo é um subtipo de “SF_SpatialSamplingFeature”.

**Atributos do tipo de objeto geográfico “GeophObjectSet”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| citation | Citação de documentação geofísica. | DocumentCitation |  |
| verticalExtent | Extensão vertical da gama de interesse. | EX_VerticalExtent | voidable |
| distributionInfo | Metadados de distribuição. | MD_Distributor | voidable |
| projectedGeometry | Projeção 2D da característica na superfície do solo (como um ponto, curva ou polígono delimitador representativo) a utilizar por um serviço de visualização INSPIRE para visualizar a localização do objeto geográfico numa carta. | GM_Object |  |
| largerWork | Identificador de um maior conjunto de dados de trabalho. | Identifier | voidable |

**Restrições do tipo de objeto geográfico “GeophObjectSet”**

O atributo de “projectedGeometry” deve ser do tipo “GM_Point”, “GM_Curve” ou “GM_Surface”.

**4.3.1.5. Perfil geofísico (GeophProfile)**

Uma medição geofísica referenciada espacialmente a uma curva.

Este tipo é um subtipo de “GeophMeasurement”.

**Atributos do tipo de objeto geográfico “GeophProfile”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| profileType | Tipo de perfil geofísico. | ProfileTypeValue |  |

**Restrições do tipo de objeto geográfico “GeophProfile”**

O atributo da forma deve ser do tipo “GM_Curve”.

**4.3.1.6. Estação geofísica (GeophStation)**

Medição geofísica referenciada geograficamente a um ponto único.

Este tipo é um subtipo de “GeophMeasurement”.

**Atributos do tipo de objeto geográfico “GeophStation”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| stationType | Tipo de estação geofísica. | StationTypeValue |  |
| stationRank | As estações geofísicas podem fazer parte de um sistema hierárquico. A ordenação é proporcional à importância da estação. | StationRankValue | voidable |

**Restrições do tipo de objeto geográfico “GeophStation”**

O atributo da forma deve ser do tipo “GM_Point”.

**4.3.1.7. Faixa geofísica (GeophSwath)**

Uma medição geofísica espacialmente referenciada a uma superfície.

Este tipo é um subtipo de “GeophMeasurement”.

**Atributos do tipo de objeto geográfico “GeophSwath”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| swathType | Tipo de faixa geofísica. | SwathTypeValue |  |

**Restrições do tipo de objeto geográfico “GeophSwath”**

O atributo da forma deve ser do tipo “GM_Surface”.

**4.3.2. Listas de códigos**

**4.3.2.1. Tipo de campanha (CampaignTypeValue)**

Um tipo de campanha geofísica.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “CampaignTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| measurement | medição | Campanha de aquisição de dados no terreno. |

**4.3.2.2. Nome da rede (NetworkNameValue)**

Um nome da rede geofísica.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “NetworkNameValue”**

| Valor | Nome | Definição |
|---|---|---|
| GSN | GSN | Global Seismographic Network |
| IMS | IMS | IMS Seismological network |
| INTERMAGNET | INTERMAGNET | International Real-time Magnetic Observatory Network |
| UEGN | UEGN | Unified European Gravity Network |
| WDC | WDC | World Data Center |

**4.3.2.3. Tipo de plataforma (PlatformTypeValue)**

Uma plataforma na qual foi efetuada a aquisição de dados.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “PlatformTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| ground | solo | Medição efetuada no solo. |
| landVehicle | veículo terrestre | Medição efetuada a partir de um veículo terrestre. |
| fixedWingAirplane | aeronave de asa fixa | Medição efetuada a partir de uma aeronave de asa fixa. |
| helicopter | helicóptero | Medição efetuada a partir de um helicóptero. |
| seafloor | fundo marinho | Medição efetuada a partir dos fundos marinhos. |
| researchVessel | navio de investigação | Medição efetuada a partir de um navio. |
| satellite | satélite | Medição efetuada a partir de um satélite. |

**4.3.2.4. Tipo de perfil (ProfileTypeValue)**

Tipo de perfil geofísico.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “ProfileTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| boreholeLogging | estudo do furo | Medição geofísica efetuada ao longo do eixo de um furo de exploração com um dispositivo especial de diagrafia. |
| multielectrodeDCProfile | perfil multielétrodos CC | Medição da resistividade CC e/ou capacidade de carga (IP) efetuada ao longo de um perfil com um maior conjunto de elétrodos. Também conhecida por tomografia de resistividade 2D. |
| seismicLine | linha sísmica | Medição geofísica utilizada para registar a resposta acústica de fontes sísmicas ao longo de uma linha a fim de definir as propriedades sísmicas num corte transversal da Terra. |

**4.3.2.5. Posição da estação na classificação (StationRankValue)**

A posição hierárquica da estação geofísica na classificação.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “StationRankValue”**

| Valor | Nome | Definição |
|---|---|---|
| observatory | observatório | Instalação de monitorização permanente com um calendário de observação contínua. |
| secularStation | estação secular | Estação de base para registar variações a longo prazo do campo físico observado. |
| 1stOrderBase | base de 1ª ordem | Estação de base de precisão máxima mantida por uma autoridade. É utilizada por observadores terceiros para ligar medições relativas à rede absoluta. |
| 2ndOrderBase | base de 2ª ordem | Estação de base de alta precisão de menor importância mantida por uma autoridade. É utilizada por observadores terceiros para ligar medições relativas à rede absoluta. |

**4.3.2.6. Tipo de estação (StationTypeValue)**

Um tipo de estação “geophysical”.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “StationTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| gravityStation | estação gravimétrica | Estação geofísica para observar o campo gravitacional. |
| magneticStation | estação magnética | Estação geofísica para observar o campo magnético. |
| seismologicalStation | estação sismológica | Estação geofísica para observar eventos sismológicos com vibrações fortes (terramoto) ou ruído ambiente. |
| verticalElectricSounding | sondagem elétrica vertical | Estação geofísica para medir as alterações da resistividade elétrica subterrânea e/ou da capacidade de carga (IP) em profundidade utilizando 4 elétrodos (AMNB) e corrente contínua. Atividade também conhecida como “VES”. |
| magnetotelluricSounding | sondagem magnetotelúrica | Estação geofísica para medir as alterações da resistividade elétrica subterrânea utilizando variações do campo eletromagnético natural. Também conhecida por “MT sounding”. |

**4.3.2.7. Tipo de levantamento (SurveyTypeValue)**

Um tipo de levantamento ou conjunto de dados geofísicos.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “SurveyTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| airborneGeophysicalSurvey | Levantamento geofísico aéreo | Campanha de medições geofísicas aéreas. |
| groundGravitySurvey | levantamento gravimétrico no solo | Campanha de medições da gravidade no solo. |
| groundMagneticSurvey | levantamento magnético no solo | Campanha de medições magnéticas no solo. |
| 3DResistivitySurvey | levantamento da resistividade 3D | Campanha de medições multielétrodos em corrente contínua em 3D. |
| seismologicalSurvey | levantamento sismológico | Campanha de medições sismológicas. |

**4.3.2.8. Tipo de faixa (SwathTypeValue)**

Um tipo de faixa geofísica.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “SwathTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| 3DSeismics | sísmica 3D | Medição geofísica utilizada para registar a resposta acústica de fontes sísmicas numa área a fim de definir a distribuição de propriedades sísmicas 3D num volume da Terra. |

**4.4. Hidrogeologia (Hydrogeology)**

**4.4.1. Tipos de objetos geográficos**

O pacote “Hidrogeologia” contém os seguintes tipos de objetos geográficos:

— Poço em atividade

— Aquiclude

— Aquífero

— Sistema aquífero

— Aquitardo

— Massa de água subterrânea

— Objeto hidrogeológico

— Objeto hidrogeológico artificial

— Objeto hidrogeológico natural

— Unidade hidrogeológica

**4.4.1.1. Poço em atividade (ActiveWell)**

Um poço que influencia os recursos freáticos do aquífero.

Este tipo é um subtipo de “HydrogeologicalObjectManMade”.

**Atributos do tipo de objeto geográfico “ActiveWell”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| activityType | Tipo de atividade do poço. | ActiveWellTypeValue |  |

**Associações do tipo de objeto geográfico “ActiveWell”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| groundWaterBody | “GroundWaterBody” do qual o “ActiveWell” extrai os recursos fréaticos. | GroundWaterBody | voidable |
| environmentalMonitoringFacility | “Environmentalmonitoringfacility” conexa. | EnvironmentalMonitoringFacility | voidable |
| borehole | “Borehole” em que o “ActiveWell” está baseado. | Borehole | voidable |

**4.4.1.2. Aquiclude (Aquiclude)**

Uma massa impermeável de rocha ou estrato de sedimentos que funciona como uma barreira ao escoamento de águas subterrâneas.

Este tipo é um subtipo de “HydrogeologicalUnit”.

**4.4.1.3. Aquífero (Aquifer)**

Uma camada subterrânea húmida de rocha permeável com aquífero ou materiais não consolidados (gravilha, areia, limo ou argila) a partir da qual podem ser utilmente extraídas águas subterrâneas através de um poço de água.

Este tipo é um subtipo de “HydrogeologicalUnit”.

**Atributos do tipo de objeto geográfico “Aquifer”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| aquiferType | Tipo de aquífero. | AquiferTypeValue |  |
| mediaType | Classificação do meio em que ocorre o fluxo de águas subterrâneas. | AquiferMediaTypeValue |  |
| isExploited | Indica se as águas subterrâneas do aquífero são exploradas através de poços ou estão em recarga. | Boolean | voidable |
| isMainInSystem | Indica se o aquífero é o principal aquífero útil no sistema aquífero. | Boolean | voidable |
| vulnerabilityToPollution | Valor de índice ou intervalo de valores que determina o potencial grau de risco do aquífero decorrente da estrutura geológica, das condições hidrogeológicas e da existência de uma real ou potencial fonte de contaminação. | QuantityValue | voidable |
| permeabilityCoefficient | Volume de um fluido incompressível que se escoa durante uma unidade de tempo através de uma unidade de volume cúbica constituída por uma substância porosa na qual é mantida uma diferença de pressão unitária. | QuantityValue | voidable |
| storativityCoefficient | Capacidade de armazenamento de água de um aquífero. | QuantityValue | voidable |
| hydroGeochemicalRockType | Tipo de rocha no que diz respeito às suas componentes rochosas solúveis e à sua influência hidrogeoquímica nas águas subterrâneas. | HydroGeochemicalRockTypeValue | voidable |

**Associações do tipo de objeto geográfico “Aquifer”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| aquitard | Aquitardo(s) que separa(m) o aquífero. | Aquitard | voidable |
| hydrogeologicalObject | O(s) “HydrogeologicalObject” relacionados com o aquífero. | HydrogeologicalObject | voidable |
| aquiferSystem | “AquiferSystem” específico em que ocorre o “Aquitard”. | AquiferSystem | voidable |

**4.4.1.4. Sistema aquífero (AquiferSystem)**

Uma coleção de aquíferos e aquitardos que, no seu conjunto, constituem o meio ambiente das águas subterrâneas – “vasos comunicantes”, que estão cheios ou podem ser cheios com água.

Este tipo é um subtipo de “HydrogeologicalUnit”.

**Atributos do tipo de objeto geográfico “AquiferSystem”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| isLayered | Indica se o “AquiferSystem” é constituído por mais de uma camada. | Boolean | voidable |

**Associações do tipo de objeto geográfico “AquiferSystem”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| aquitard | Aquitardo(s) contido(s) no “AquiferSystem”. | Aquitard | voidable |
| aquiclude | Aquiclude que envolve o “AquiferSystem” | Aquiclude | voidable |
| aquifer | O(s) aquífero(s) contido(s) no “AquiferSystem”. | Aquifer | voidable |

**4.4.1.5. Aquitardo (Aquitard)**

Um leito saturado, mas pouco permeável, que dificulta a circulação das águas subterrâneas.

Este tipo é um subtipo de “HydrogeologicalUnit”.

**Atributos do tipo de objeto geográfico “Aquitard”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| approximatePermeabilityCoefficient | Volume de um fluido incompressível que se escoa durante uma unidade de tempo através de uma unidade de volume cúbica constituída por uma substância porosa na qual é mantida uma diferença de pressão unitária. | QuantityValue | voidable |
| approximateStorativityCoefficient | Capacidade de armazenamento de água de um aquífero. | QuantityValue | voidable |

**Associações do tipo de objeto geográfico “Aquitard”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| aquiferSystem | “AquiferSystem” de que faz parte o “Aquitard”. | AquiferSystem | voidable |
| aquifer | Aquíferos separados pelo aquitardo. | Aquifer | voidable |

**4.4.1.6. Massa de águas subterrâneas (GroundWaterBody)**

Um volume distinto de águas subterrâneas num aquífero ou sistema de aquíferos, que está isolado do ponto de vista hidráulico de massas de água subterrâneas próximas.

**Atributos do tipo de objeto geográfico “GroundWaterBody”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| approximateHorizontalExtend | Geometria que define a fronteira da “GroundWaterBody”. | GM_Surface | voidable |
| conditionOfGroundWaterBody | Grau aproximado de alteração nas águas subterrâneas resultante da atividade humana. | ConditionOfGroundwaterValue |  |
| mineralization | Uma das principais características químicas da água. O seu valor é a soma das concentrações químicas de todos os componentes da água. | WaterSalinityValue | voidable |
| piezometricState | Especifica o estado piezométrico do lençol freático “GroundwaterBody”. | PiezometricState | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

**Associações do tipo de objeto geográfico “GroundWaterBody”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| activeWell | “ActiveWell” que altera o estado da “GroundwaterBody” através da extração de recursos freáticos. | ActiveWell | voidable |
| aquiferSystem | “AquiferSystem” que inclui a “GroundWaterBody”. | AquiferSystem | voidable |
| hydrogeologicalObjectNatural | “HydrogeologicalObjectNatural” que interage com o “GroundwaterBody”. | HydrogeologicalObjectNatural | voidable |
| observationWell | Poços de observação que monitorizam a “GroundWaterBody” | EnvironmentalMonitoringFacility | voidable |

**4.4.1.7. Objeto hidrogeológico (HydrogeologicalObject)**

Uma classe abstrata para meios artificiais ou características naturais que têm uma interação com o sistema hidrogeológico.

Este tipo é abstrato.

**Atributos do tipo de objeto geográfico “HydrogeologicalObject”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| geometry | Geometria que define a localização espacial do “HydrogeologicalObject”. | GM_Primitive |  |
| name | Nome ou código do “HydrogeologicalObject”. | PT_FreeText | voidable |
| description | Descrição do “HydrogeologicalObject”. | PT_FreeText | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

**Associações do tipo de objeto geográfico “HydrogeologicalObject”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| aquifer | Aquífero no qual ocorre o “HydrogeologicalObject”. | Aquifer | voidable |

**4.4.1.8. Objeto hidrogeológico artificial (HydrogeologicalObjectManMade)**

Um objeto hidrogeológico criado pelo homem.

Este tipo é um subtipo de “HydrogeologicalObject”.

Este tipo é abstrato.

**Atributos do tipo de objeto geográfico “HydrogeologicalObjectManMade”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| validFrom | Data e hora oficiais em que o objeto hidrogeológico foi/será legalmente estabelecido. | DateTime | voidable |
| validTo | Data e hora em que o objeto hidrogeológico deixou/deixará de ser legalmente utilizado. | DateTime | voidable |
| statusCode | Código que define o estatuto formal de um objeto hidrogeológico artificial. | StatusCodeTypeValue | voidable |

**4.4.1.9. Objeto hidrogeológico natural (HydrogeologicalObjectNatural)**

Objeto hidrogeológico que foi gerado por processos naturais.

Este tipo é um subtipo de “HydrogeologicalObject”.

**Atributos do tipo de objeto geográfico “HydrogeologicalObjectNatural”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| naturalObjectType | Tipo de objeto hidrogeológico natural. | NaturalObjectTypeValue |  |
| waterPersistence | Grau de persistência do fluxo de água. | WaterPersistenceValue | voidable |
| approximateQuantityOfFlow | Valor aproximado que define o débito de água num objeto hidrogeológico natural. | QuantityValue | voidable |

**Associações do tipo de objeto geográfico “HydrogeologicalObjectNatural”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| groundWaterBody | “GroundWateBody” com que a qual o objeto hidrogeológico natural interage. | GroundWaterBody | voidable |

**4.4.1.10. Unidade hidrogeológica (HydrogeologicalUnit)**

Uma parte da litosfera com parâmetros distintivos para o armazenamento e o transporte de água.

Este tipo é um subtipo de “GeologicUnit”.

**Atributos do tipo de objeto geográfico “HydrogeologicalUnit”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| description | Descrição da “HydrogeologicalUnit”. | PT_FreeText | Voidable |
| approximateDepth | Profundidade aproximada da ocorrência de “HydrogeologicalUnit”. | QuantityValue | Voidable |
| approximateThickness | Espessura aproximada da “HydrogeologicalUnit”. | QuantityValue | Voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | Voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | Voidable |

**Associações do tipo de objeto geográfico “HydrogeologicalUnit”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| geologicStructure | Relaciona uma ou muitas HydrogeologicalUnit» com uma “GeologicStructure”. | GeologicStructure | Voidable |

**4.4.2. Tipos de dados**

**4.4.2.1. Superfície hidrogeológica (HydrogeologicalSurface)**

Uma superfície que representa o lençol freático interpolado ou outra superfície, para uma área local ou regional.

Este tipo é um tipo de união.

**Atributos do tipo de união “HydrogeologicalSurface”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| surfaceRectifiedGrid | Superfície cujo domínio consiste numa quadrícula retificada. | RectifiedGridCoverage |  |
| surfaceReferenceableGrid | Superfície cujo domínio consiste numa quadrícula referenciável. | ReferenceableGridCoverage |  |
| surfacePointCollection | Superfície hidrogeológica representada por uma coleção de observações pontuais. | PointObservationCollection |  |

**4.4.2.2. Estado piezométrico (PiezometricState)**

O estado piezométrico de uma “GroundWaterBody”

**Atributos do tipo de dados “PiezometricState”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| observationTime | Data e hora da observação do estado das águas subterrâneas. | DateTime |  |
| piezometricSurface | Superfície que representa o nível a que a água subirá em poços fortemente confinados. | HydrogeologicalSurface |  |

**4.4.2.3. Valor quantitativo (QuantityValue)**

Um contentor de dados com um único valor quantitativo ou com uma gama de valores quantitativos.

Este tipo é um tipo de união.

**Atributos do tipo de união “QuantityValue”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| singleQuantity | Componente escalar com representação decimal e uma unidade de medida utilizada para armazenar o valor de uma quantidade contínua. | Quantity |  |
| quantityInterval | Par decimal para especificar uma gama de quantidades com uma unidade de medida. | QuantityRange |  |

**4.4.3. Listas de códigos**

**4.4.3.1. Tipo de poço em atividade (ActiveWellTypeValue)**

Tipos de poços ativos.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “ActiveWellTypeValue”**

<table> <tbody> <tr> <td>Valor</td> <td>Nome</td> <td>Definição</td> </tr> <tr> <td>exploitation</td> <td>exploração</td> <td>Extração de águas subterrâneas de um aquífero para vários fins (urbanos, industriais, captação de água e outros fins)</td> </tr> <tr> <td>recharge</td> <td>recarga</td> <td><table> <tbody> <tr> <td>a)</td> <td>Poços de recarga de aquíferos: Utilizados para recarregar aquíferos esgotados injetando água a partir de uma variedade de fontes, como lagos, cursos de água, instalações de tratamento de águas residuais urbanas, outros aquíferos, etc.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>b)</td> <td>Poços de barreira à intrusão de água salina: Utilizados para injetar água em aquíferos de água doce a fim de evitar a intrusão de água salgada em aquíferos de água doce.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>c)</td> <td>Poços de controlo da subsidência: Utilizados para injetar fluidos numa zona não produtora de petróleo ou de gás a fim de reduzir ou eliminar a subsidência associada ao excesso de extração de água doce.</td> </tr> </tbody> </table></td> </tr> <tr> <td>dewatering</td> <td>secagem</td> <td>Eliminação de água de um material sólido ou do solo de um aquífero com o objetivo de baixar o nível do lençol freático, por exemplo, durante a fase de desenvolvimento do estaleiro de um grande projeto de construção devido ao nível elevado do lençol freático. Normalmente implica a utilização de bombas de “secagem”.</td> </tr> <tr> <td>decontamination</td> <td>descontaminação</td> <td>Poço utilizado em sistemas de reabilitação para reduzir a poluição de um aquífero.</td> </tr> <tr> <td>disposal</td> <td>eliminação</td> <td>Poço, frequentemente um poço de petróleo ou de gás esgotado, no qual podem ser injetados fluidos de resíduos para fins de eliminação. Os poços de eliminação estão normalmente sujeitos a requisitos regulamentares com vista a evitar a contaminação dos aquíferos de água doce.</td> </tr> <tr> <td>waterExploratory</td> <td>prospeção de água</td> <td>Poço perfurado para procurar novas águas subterrâneas.</td> </tr> <tr> <td>thermal</td> <td>termal</td> <td>Poço utilizado para a extração de águas termais para vários fins termais (por exemplo, balneologia).</td> </tr> <tr> <td>observation</td> <td>observação</td> <td>Poço utilizado para fins de observação.</td> </tr> </tbody> </table>

**4.4.3.2. Tipo de meio aquífero (AquiferMediaTypeValue)**

Valores que descrevem as características do meio aquífero.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “AquiferMediaTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| fractured | fraturado | Os aquíferos fraturados são rochas em que as águas subterrâneas fluem através de fissuras, juntas ou fraturas em rochas que seriam de outra forma sólidas |
| porous | poroso | Meios porosos são os aquíferos constituídos por agregados de partículas individuais como areia ou gravilha e em que as águas subterrâneas fluem e passam através do espaço entre os grãos. |
| karstic | cársico | Os aquíferos cársicos são aquíferos fraturados em que as fissuras e fraturas foram alargadas por dissolução, formando grandes canais ou mesmo grutas. |
| compound | composto | Combinação de um aquífero poroso, cársico e/ou fraturado |
| karsticAndFractured | cársico e fraturado | Combinação de um aquífero simultaneamente cársico e fraturado |
| porousAndFractured | poroso e fraturado | Combinação de um aquífero simultaneamente poroso e fraturado |

**4.4.3.3. Tipo de aquífero (AquiferTypeValue)**

Tipos de aquíferos.

Os valores autorizados para esta lista de códigos incluem apenas os valores especificados no quadro infra.

**Valores para a lista de códigos “AquiferTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| confinedSubArtesian | subartesiano confinado | Aquífero que contém água entre duas fronteiras relativamente impermeáveis. O nível da água num poço perfurado num aquífero confinado situa-se acima da parte superior do aquífero confinado e pode estar mais acima ou mais abaixo do lençol freático que pode estar presente no material situado acima deste. O nível da água não sobe acima da superfície do solo. |
| confinedArtesian | artesiano confinado | Aquífero que contém água entre duas fronteiras relativamente impermeáveis. O nível da água num poço perfurado num aquífero confinado situa-se acima da parte superior do aquífero confinado e pode estar mais acima ou mais abaixo do lençol freático que pode estar presente no material situado acima deste. O nível da água sobe acima da superfície do solo, o que permite obter um poço artesiano. |
| unconfined | não confinado | Aquífero que contém água que não se encontra sob pressão. O nível da água num poço é igual ao do lençol freático fora do poço. |

**4.4.3.4. Estado das águas subterrâneas (ConditionOfGroundwaterValue)**

Valores que indicam o grau aproximado da alteração ocorrida no estado natural das águas subterrâneas.

Os valores autorizados para esta lista de códigos incluem apenas os valores especificados no quadro infra.

**Valores para a lista de códigos “ConditionOfGroundwaterValue”**

| Valor | Nome | Definição |
|---|---|---|
| natural | natural | A quantidade ou qualidade das águas subterrâneas está exclusivamente dependente de fatores naturais. |
| lightlyModified | ligeiramente modificado | A quantidade ou qualidade das águas subterrâneas depende principalmente de fatores naturais, mas verifica-se alguma influência da atividade humana |
| modified | modificado | A quantidade ou qualidade das águas subterrâneas é modificada pela atividade humana. |
| stronglyModified | fortemente modificado | A quantidade ou qualidade das águas subterrâneas é modificada pela atividade humana e os valores de uma série de parâmetros ultrapassam as normas relativas à água potável. |
| unknown | desconhecido | É desconhecido o estado natural das águas subterrâneas. |

**4.4.3.5. Tipo hidrogeoquímico da rocha (HydroGeochemicalRockTypeValue)**

Valores que descrevem o estado hidrogeoquímico do ambiente freático.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “HydroGeochemicalRockTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| silicatic | silicatado | Tipo hidroquímico silicatado de águas subterrâneas. |
| carbonatic | carbonatado | Tipo hidroquímico carbonatado de águas subterrâneas. |
| sulfatic | sulfatado | Tipo hidroquímico sulfatado de águas subterrâneas. |
| chloridic | cloretado | Tipo hidroquímico cloretado de águas subterrâneas. |
| organic | orgânico | Tipo hidroquímico orgânico de águas subterrâneas. |

**4.4.3.6. Tipo de objeto natural (NaturalObjectTypeValue)**

Tipos de objetos hidrogeológicos naturais.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “NaturalObjectTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| spring | nascente | Qualquer situação natural em que as águas subterrâneas emergem à superfície da Terra. Por conseguinte, uma nascente é um local em que a superfície do aquífero chega à superfície do solo. |
| seep | infiltração | Local húmido ou molhado em que as águas subterrâneas atingem a superfície da Terra a partir de um aquífero subterrâneo. |
| swallowHole | poço natural | Depressão ou furo natural na superfície da Terra, também conhecido como pia, escoadouro natural, racha, rio subterrâneo, dolina ou cenote, que é principalmente formado por processos cársicos – a dissolução química de rochas carbonatadas ou processos de sufusão, por exemplo, em arenitos. |
| fen | charco | Terras baixas cobertas total ou parcialmente por água e que têm geralmente solos turfosos alcalinos e uma flora característica (como carriços e juncos). |
| notSpecified | não especificado | Locais não especificados em que as águas subterrâneas atingem a superfície. |

**4.4.3.7. Tipo de código de estatuto (StatusCodeTypeValue)**

Os valores que descrevem os estatutos de objetos hidrogeológicos artificiais.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “StatusCodeTypeValue”**

| Valor | Nome | Definição |
|---|---|---|
| abandonedDry | abandonado, seco | Abandonado devido à ausência de água. |
| abandonedInsufficient | abandonado, água insuficiente | Abandonado devido à quantidade insuficiente de água. |
| abandonedQuality | abandonado, má qualidade da água | Abandonado devido à qualidade da água. |
| deepened | aprofundado | Profundidade do furo aumentada. |
| new | novo | Furo num local ainda não utilizado anteriormente. |
| notInUse | não utilizado | Já não utilizado para fim algum. |
| reconditioned | recondicionado | Poço que foi objeto de obras corretivas para melhorar o seu funcionamento. |
| standby | de reserva | Captação utilizada apenas quando não estão disponíveis outras. |
| unfinished | inacabado | Furo ou construção não completado. |
| unknown | desconhecido | Estatuto não conhecido ou definido. |

**4.4.3.8. Persistência da água (WaterPersistenceValue)**

Tipos de persistência hidrológica.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “WaterPersistenceValue”**

| Valor | Nome | Definição |
|---|---|---|
| intermittent | intermitente | Cheio e/ou a correr durante parte do ano. |
| seasonal | sazonal | Cheio e/ou a correr em determinadas estações do ano, por exemplo, outono/inverno. |
| perennial | permanente | Cheio e/ou a correr continuamente ao longo de todo o ano uma vez que o seu leito se encontra abaixo do lençol freático. |
| notSpecified | não especificado | O tipo de persistência hidrológica não está especificado. |
| ephemeral | efémero | Cheio e/ou a correr durante e imediatamente após precipitações. |

**4.4.3.9. Salinidade da água (WaterSalinityValue)**

Uma lista de códigos que indique as classes de salinidade na água.

Os valores autorizados para esta lista de códigos incluem os valores constantes do quadro infra e valores adicionais a qualquer nível definidos pelos fornecedores de dados.

**Valores para a lista de códigos “WaterSalinityValue”**

| Valor | Nome | Definição |
|---|---|---|
| ultraFreshWater | água ultradoce | Águas com um grau de salinidade muito baixo. A salinidade é equivalente ou quase equivalente à das águas pluviais. |
| freshWater | água doce | Água doce designa massas de água, como lagoas, lagos, rios e cursos de água que contêm baixas concentrações de sais dissolvidos. |
| brackishWater | água salobra | Água salobra é a água com um grau de salinidade superior ao da água doce, mas não tão elevado como o da água do mar. Pode resultar da mistura de água do mar com água doce, como acontece nos estuários, ou pode ocorrer em aquíferos de águas salobras fósseis. |
| salineWater | água salina | Águas salinas são águas que contêm uma concentração significativa de sais dissolvidos. A água do mar tem uma salinidade de cerca de 35 000 ppm, equivalente a 35 g/l. |
| brineWater | salmoura | Salmoura é água saturada ou praticamente saturada com sal. |

**4.5. Camadas**

**Camadas para a categoria temática de dados geográficos “Geologia”**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| GE.GeologicUnit | Unidades geológicas | «MappedFeature» (objetos geográficos cuja propriedade especificada é do tipo «GeologicUnit») |
| GE. <Valor de lista de códigos> (1) | <nome legível para as pessoas> | «MappedFeature» (objetos geográficos cuja propriedade especificada é do tipo «GeologicFeature» e que estão classificados (utilizando a propriedade «themeClass») de acordo com a mesma classificação temática) |
| Exemplo: GE.ShrinkingAndSwelling Clays | Exemplo: Argilas expansivas e contráteis | (themeClassification: ThematicClassificationValue) |
| GE.GeologicFault | Falhas geológicas | «MappedFeature» (objetos geográficos cuja propriedade especificada é do tipo «ShearDisplacementStructure») |
| GE.GeologicFold | Dobras geológicas | «MappedFeature» (objetos geográficos cuja propriedade especificada é do tipo «Fold») |
| GE.GeomorphologicFeature | Características geomorfológicas | «MappedFeature» (objetos geográficos cuja propriedade especificada é do tipo «GeomorphologicFeature») |
| GE.Borehole | Furos | Borehole |
| GE.Aquifer | Aquíferos | «MappedFeature» (objetos geográficos cuja propriedade especificada é do tipo «Aquifer») |
| GE.Aquiclude | Aquicludes | «MappedFeature» (objetos geográficos cuja propriedade especificada é do tipo «Aquiclude») |
| GE.Aquitard | Aquitardos | «MappedFeature» (objetos geográficos cuja propriedade especificada é do tipo «Aquitard») |
| GE.AquiferSystems | Sistemas aquíferos | «MappedFeature» (objetos geográficos cuja propriedade especificada é do tipo «AquiferSystem») |
| GE.Groundwaterbody | Massas de águas subterrâneas | Groundwaterbody |
| GE.ActiveWell | Poços em atividade | ActiveWell |
| GE. <Valor de lista de códigos> (2) | <nome legível para as pessoas> | GeophStation (stationType: StationTypeValue) |
| Exemplo: GE.gravityStation | Exemplo: Estações gravimétricas |  |
| GE. <Valor de lista de códigos> (3) | <nome legível para as pessoas> | GeophStation (profilType: ProfileTypeValue) |
| Exemplo: GE.seismicLine | Exemplo: Linhas sísmicas |  |
| GE. <Valor de lista de códigos> (4) | <nome legível para as pessoas> | GeophStation (surveyType: SurveyTypeValue) |
| Exemplo: GE.groundGravitySurvey | Exemplo: Levantamentos da gravidade no solo |  |
| GE. <Valor de lista de códigos> (5) | <nome legível para as pessoas> | Campaign (surveyType: SurveyTypeValue) |
| Exemplo: GE.groundMagneticSurvey | Exemplo: Levantamentos magnéticos no solo |  |
| GE.Geophysics.3DSeismics | Sísmica 3D | GeophSwath |

(1) Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3

(2) Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3

(3) Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3

(4) Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3

(5) Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3»
