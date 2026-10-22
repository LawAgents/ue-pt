---
id: "regulamento-ue-2010-1089-anexo-iii"
celex: "32010R1089"
title: "Regulamento (UE) n. ° 1089/2010 da Comissão, de 23 de Novembro de 2010 , que estabelece as disposições de execução da Directiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Anexo III"
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
part: "Anexo III"
---

# Regulamento (UE) n. ° 1089/2010 da Comissão, de 23 de Novembro de 2010 , que estabelece as disposições de execução da Directiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Anexo III

## Anexo III

**Requisitos relativos a categorias temáticas de dados geográficos enumeradas no anexo II da Diretiva 2007/2/CE**

**1. ALTITUDE (ELEVATION)**

**1.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) «Modelo Numérico Altimétrico» (Digital Elevation Model - DEM) : Modelo Numérico Topográfico (DSM) ou Modelo Digital do Terreno (DTM).

(2) «Modelo Numérico Topográfico» (Digital Surface Model - DSM) : uma superfície que descreve a forma tridimensional da superfície terrestre, incluindo todos elementos estáticos sobre esta. Os fenómenos temporários não fazem parte da superfície, mas, devido às dificuldades técnicas de eliminação desses fenómenos, alguns desses elementos podem também estar presentes na superfície.

(3) «Modelo Digital do Terreno» (Digital Terrain Model - DTM) : uma superfície que descreve a forma tridimensional da superfície terrestre nua, excluindo tanto quanto possível outros elementos sobre esta.

(4) «Altitude»(elevation) : uma propriedade dimensional de um objeto geográfico delimitada na vertical que consiste numa medição absoluta referenciada a uma superfície bem definida que é normalmente tomada como origem.

(5) «Altura»(height) : uma propriedade altimétrica medida ao longo de uma linha de fio de prumo num sentido oposto ao do campo de gravidade da Terra (para cima).

(6) «Profundidade»(depth) : uma propriedade altimétrica medida ao longo de uma linha de fio de prumo num sentido coincidente com o do campo de gravidade da Terra (para baixo).

**1.2. Estrutura da categoria temática de dados geográficos «Altitude»**

Os tipos especificados para a categoria temática de dados geográficos «Altitude» estão estruturados nos seguintes pacotes:

— Altitude - Tipos de base (Elevation – Base Types)

— Altitude - Cobertura matricial (Elevation – Grid Coverage)

— Altitude - Elementos vetoriais (Elevation – Vector Elements)

— Altitude - TIN (Elevation – TIN)

Devem ser disponibilizados conjuntos de dados geográficos que descrevam a morfologia da altimetria terrestre utilizando, pelo menos, os tipos de objetos geográficos incluídos no pacote «Altitude - Cobertura Matricial».

Devem ser disponibilizados conjuntos de dados geográficos que descrevam a morfologia da batimetria terrestre utilizando, pelo menos, os tipos de objetos geográficos incluídos no pacote «Altitude - Cobertura Matricial» ou no pacote «Altitude - Elementos Vetoriais».

**1.3. Altitude - Tipos de base**

**1.3.1. Listas de códigos**

1.3.1.1. Tipo de propriedade altimétrica (ElevationPropertyTypeValue)

Tipo de lista de códigos que determina a propriedade altimétrica que foi medida ou calculada.

1.3.1.2. Tipo de superfície (SurfaceTypeValue)

Tipo de lista de códigos que determina a superfície altimétrica no que diz respeito à sua relativa similitude com a superfície nua da Terra.

**1.4. Altitude - Cobertura matricial**

**1.4.1. Tipos de objetos geográficos**

O pacote «Altitude - Cobertura Matricial» contém o tipo de objeto geográfico «Altitude - Cobertura Matricial».

1.4.1.1. Cobertura altimétrica matricial (ElevationGridCoverage)

Cobertura contínua que utiliza uma tesselação sistemática baseada numa quadrícula quadrilateral retificada regular para cobrir o seu domínio, quando o valor da propriedade altimétrica é geralmente conhecido para cada uma das cotas que formam este domínio.

Este tipo é um subtipo de «RectifiedGridCoverage».

Atributos do tipo de objeto geográfico «ElevationGridCoverage»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| domainExtent | Extensão do domínio espaciotemporal da cobertura. | EX_Extent |  |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| propertyType | Atributo que determina a propriedade altimétrica representada pela cobertura altimétrica matricial. | ElevationPropertyTypeValue |  |
| surfaceType | Atributo que indica o tipo de superfície altimétrica que a cobertura descreve em relação à superfície nua da Terra. | SurfaceTypeValue |  |

Associações do tipo de objeto geográfico «ElevationGridCoverage»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| contributingElevationGridCoverage | Referência às coberturas altimétricas matriciais que compõem uma cobertura altimétrica matricial agregada. <br> A associação tem propriedades adicionais conforme definido na classe de associação «ElevationGridCoverageAggregation». | ElevationGridCoverage |  |

Restrições do tipo de objeto geográfico «ElevationGridCoverage»

A dimensão da quadrícula deve ser sempre 2 para uma cobertura altimétrica matricial.

O atributo «domainExtent» deve estar preenchido, pelo menos, com um subtipo de «EX_GeographicExtent».

Deve ser fornecido o sistema de referência de coordenadas utilizado para referenciar a quadrícula.

Todas as instâncias de «ElevationGridCoverage», a que se refere uma instância de «ElevationGridCoverage» agregada, devem partilhar a mesma orientação de eixos da quadrícula e o mesmo espaçamento de quadrículas em cada direção.

A origem da quadrícula deve ser descrita em duas dimensões.

Os valores no conjunto da gama de valores devem ser descritos pelo tipo «Float».

**1.4.2. Tipos de dados**

1.4.2.1. Agregação da cobertura altimétrica matricial (ElevationGridCoverageAggregation)

Características geométricas da agregação da cobertura altimétrica matricial.

Este tipo é uma classe de associação.

Atributos do tipo de dados «ElevationGridCoverageAggregation»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| contributingFootprint | Representação geométrica que delimita a área geográfica da cobertura altimétrica matricial que contribui para a cobertura altimétrica matricial agregada. | GM_MultiSurface |  |

**1.5. Altitude - Elementos vetoriais**

**1.5.1. Tipos de objetos geográficos**

O pacote «Altitude - Elementos Vetoriais» contém os seguintes tipos de objetos geográficos:

— Objeto altimétrico vetorial

— Cota altimétrica

— Curva de nível

— Linha de rutura

— Área vazia

— Área isolada

1.5.1.1. Objeto altimétrico vetorial (ElevationVectorObject)

Objeto geográfico altimétrico que faz parte de um conjunto de dados vetoriais e que participa na descrição da propriedade altimétrica de uma superfície no mundo real. Consiste numa base de identificação de todos os objetos vetoriais que podem ser incluídos como parte de um conjunto de dados altimétricos.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «ElevationVectorObject»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| localDepthDatum | Identificação de um sistema local de referência de coordenadas verticais não incluído num registo, que é utilizado para referir medições de profundidade. | ChartDatum |  |
| propertyType | Atributo que classifica o objeto altimétrico vetorial como um objeto geográfico altimétrico ou batimétrico. Determina a propriedade altimétrica representada pelo objeto. | ElevationPropertyTypeValue |  |

1.5.1.2. Cota altimétrica (SpotElevation)

Objeto geográfico com representação pontual que descreve a altitude de uma superfície terrestre num local específico. Fornece um valor único de propriedade altimétrica.

Este tipo é um subtipo de «ElevationVectorObject».

Atributos do tipo de objeto geográfico «SpotElevation»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| classification | Classe da cota altimétrica de acordo com a Especificação LAS da Sociedade Americana de Fotogrametria e Teledeteção (American Society for Photogrammetry and Remote Sensing - ASPRS). | SpotElevationClassValue | voidable |
| geographicalName | Topónimo que é utilizado para identificar uma determinada localização de uma superfície terrestre ou imersa no mundo real, que é representado pelo objeto geográfico de cota altimétrica. | GeographicalName | voidable |
| geometry | Representa as propriedades geométricas do objeto geográfico. | GM_Point |  |
| propertyValue | Valor da propriedade altimétrica do objeto geográfico referido a um determinado sistema de referência de coordenadas verticais. | DirectPosition |  |
| spotElevationType | O tipo da cota altimétrica. | SpotElevationTypeValue | voidable |

Restrições do tipo de objeto geográfico «SpotElevation»

A dimensão da coordenada do valor da propriedade deve ser 1.

O valor da propriedade deve ser expresso por referência a um sistema de referência de coordenadas verticais.

1.5.1.3. Curva de nível (ContourLine)

Objeto geográfico linear composto por um conjunto de localizações adjacentes caracterizadas por terem o mesmo valor de propriedade altimétrica. Descreve, juntamente com outras curvas de nível presentes na área, a morfologia local da superfície terrestre.

Este tipo é um subtipo de «ElevationVectorObject».

Atributos do tipo de objeto geográfico «ContourLine»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| contourLineType | Tipo de curva de nível no que diz respeito ao intervalo da curva de nível normal vertical (caso exista). | ContourLineTypeValue | voidable |
| downRight | Propriedade que indica que o objeto geográfico de curva de nível está digitalizado de um modo que a altura da superfície altimétrica é inferior no lado direito da curva. | Boolean | voidable |
| geometry | Representa as propriedades geométricas do objeto geográfico. | GM_Curve |  |
| propertyValue | Valor da propriedade altimétrica do objeto geográfico referenciado a um determinado sistema de referência de coordenadas verticais. | DirectPosition |  |

Restrições do tipo de objeto geográfico «ContourLine»

A dimensão da coordenada do valor da propriedade deve ser 1.

O valor da propriedade deve ser expresso por referência a um sistema de referência de coordenadas verticais.

1.5.1.4. Linha de rutura (BreakLine)

Uma linha crítica que descreve a forma de uma superfície altimétrica e indica uma descontinuidade no declive da superfície (ou seja, uma alteração abrupta da sua inclinação). Os triângulos incluídos num modelo TIN não devem nunca atravessá-la.

Este tipo é um subtipo de «ElevationVectorObject».

Atributos do tipo de objeto geográfico «BreakLine»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| breakLineType | Tipo de linha de rutura relativamente à característica natural ou artificial do mundo real que representa, ou à função específica que tem no cálculo de um Modelo Numérico Altimétrico (DEM). | BreakLineTypeValue |  |
| geometry | Representa as propriedades geométricas do objeto geográfico. | GM_Curve |  |
| manMadeBreak | Linha que representa uma descontinuidade altimétrica devida a uma construção artificial presente no terreno. | Boolean | voidable |

1.5.1.5. Área vazia (VoidArea)

Área da superfície terrestre em que o modelo altimétrico é desconhecido devido à falta de dados de entrada. Esta área deve ser excluída de um modelo DEM.

Este tipo é um subtipo de «ElevationVectorObject».

Atributos do tipo de objeto geográfico «VoidArea»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Representa as propriedades geométricas do objeto geográfico. | GM_Surface |  |

1.5.1.6. Área isolada (IsolatedArea)

Delimitação de uma área da superfície terrestre em que existe uma parte isolada do modelo altimétrico. As suas áreas circundantes exteriores não têm informação altimétrica.

Este tipo é um subtipo de «ElevationVectorObject».

Atributos do tipo de objeto geográfico «IsolatedArea»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Representa as propriedades geométricas do objeto geográfico. | GM_Surface |  |

**1.5.2. Tipos de dados**

1.5.2.1. Datum cartográfico (ChartDatum)

Sistema local de referência de coordenadas verticais que é utilizado para referir e representar as medições de profundidade como valores de propriedades.

Atributos do tipo de dados «ChartDatum»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| datumWaterLevel | Nível da água que determina a origem das medições da profundidade para o datum cartográfico. | WaterLevelValue |  |
| offset | Diferença relativa entre a altura de cada ponto de referência e a altura do nível da água que determina o datum cartográfico. | Measure |  |
| referencePoint | Posição(ões) geográfica(s) de: - Caso A: um ponto único que é utilizado para referir os valores de profundidade no âmbito geográfico do datum cartográfico. - Caso B: um conjunto de pontos em que são efetuadas medições do nível da água para determinar o nível da água do datum cartográfico. | GM_Point |  |
| scope | Âmbito geográfico em que o datum de profundidade local é na prática utilizado. | EX_Extent |  |

—————

**1.5.4. Listas de códigos**

1.5.4.1. Tipo de linha de rutura (BreakLineTypeValue)

Lista de possíveis valores do tipo para linhas de rutura com base nas características físicas da linha de rutura [na superfície altimétrica].

1.5.4.2. Classificação da cota altimétrica (SpotElevationClassValue)

Valores possíveis de classificação das cotas altimétricas baseados na especificação LAS elaborada pela Sociedade Americana de Fotogrametria e Teledeteção (ASPRS).

1.5.4.3. Tipo de cota altimétrica (SpotElevationTypeValue)

Valores possíveis para pontos de cota altimétrica que descrevem uma singularidade da superfície.

1.5.4.4. Tipo de curvas de nível (ContourLineTypeValue)

Lista de categorias possíveis de curvas de nível baseadas no parâmetro equidistância do conjunto de dados.

**1.6. Altitude - TIN**

**1.6.1. Tipos de objetos geográficos**

O pacote «Altitude – TIN» contém o tipo de objeto geográfico «TIN Altimétrica».

1.6.1.1. TIN altimétrica (ElevationTIN)

Coleção de objetos geográficos altimétricos que formam uma determinada tesselação do espaço com base numa «

Triangulated Irregular Network

» (TIN) (rede irregular de triângulos) de acordo com a geometria «GM_Tin» definida na norma ISO 19107:2003). Os seus componentes são um conjunto de pontos de controlo cujos valores da propriedade altimétrica são conhecidos e um conjunto de linhas de rutura e de linhas de paragem.

Atributos do tipo de objeto geográfico «ElevationTIN»

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

(1) Se os dados altimétricos forem atualizados com base em novos dados-fonte, deve ser atribuído aos objetos atualizados um novo identificador de objeto externo.

**1.7.2. Requisitos para as coberturas altimétricas matriciais**

(1) Em derrogação ao requisito estabelecido no ponto 2.2 do anexo II, qualquer quadrícula compatível com um dos seguintes sistemas de referência de coordenadas pode ser utilizada para a disponibilização de dados altimétricos matriciais:

— coordenadas geodésicas bidimensionais (latitude e longitude) baseadas num datum especificado no ponto 1.2. do anexo II e que utilizam os parâmetros da elipsoide do GRS80;

— coordenadas planas utilizando o sistema de referência de coordenadas de projeção cónica conforme de Lambert do ETRS89;

— coordenadas planas utilizando o sistema de referência de coordenadas de projeção transversa de Mercator do ETRS89;

Não deve ser utilizada a quadrícula referida no ponto 2.2.1 do anexo II.

(2) O atributo «domainExtent» de cada instância de

«ElevationGridCoverage»

deve ser preenchido, pelo menos, com um subtipo do tipo

«EX_GeographicExtent»

.

(3) Os valores da propriedade altimétrica incluídos no conjunto de gamas de valores de uma única «ElevationGridCoverage» devem ser referenciados a um único sistema de referência de coordenadas verticais.

(4) Todas as instâncias de «ElevationGridCoverage», a que se refere uma instância de «ElevationGridCoverage» agregada, devem ser coerentes. Isto significa que devem ter o mesmo tipo de gama de valores, sistema de referência de coordenadas e resolução. Devem também suportar o alinhamento de quadrículas, ou seja os pontos da quadrícula numa instância de «ElevationGridCoverage» devem estar alinhados com os pontos da quadrícula de outras instâncias de «ElevationGridCoverage», de modo a que as células das quadrículas não se sobreponham parcialmente.

(5) As «pegadas» (footprints) de quaisquer duas instâncias de «ElevationGridCoverage» a que se refere a mesma instância de «ElevationGridCoverage» agregada devem ser adjacentes ou não adjacentes.

(6) \A união das «pegadas» das instâncias de «ElevationGridCoverage» a que se refere a mesma instância de «ElevationGridCoverage» agregada determina a extensão geográfica («domainExtent») da instância da «ElevationGridCoverage» agregada.

(7) O pacote «ElevationGridCoverage» deve ser limitado a geometrias bidimensionais.

(8) Deve ser fornecida informação sobre as datas de aquisição dos dados contidos nas coberturas altimétricas matriciais em, pelo menos, uma das seguintes formas:

(a) Fornecendo o elemento de metadados de referência temporal para cada objeto geográfico através do atributo de metadados do tipo de objeto geográfico

«ElevationGridCoverage»;

(b) Fornecendo o elemento de metadados de referência temporal estabelecido no Regulamento (CE) n.º 1205/2008 como uma extensão temporal.

**1.7.3. Requisitos aplicáveis aos dados altimétricos vetoriais**

(1) Quando os conjuntos de dados altimétricos vetoriais são fornecidos utilizando geometrias 2-D, a componente vertical (terceira dimensão) deve ser fornecida como valores da propriedade altimétrica no atributo «propertyValue».

(2) Quando os conjuntos de dados altimétricos vetoriais são fornecidos utilizando geometrias 2.5-D, os valores da propriedade altimétrica só devem ser incluídos na terceira coordenada (Z) dessas geometrias.

**1.7.4. Requisitos aplicáveis a TIN altimétricas**

(1) Os valores de propriedade incluídos numa única instância do tipo de objeto geográfico «ElevationTIN» (modelo TIN) devem ser referenciados a um único sistema de referência de coordenadas verticais.

(2) Os triângulos que intersetam uma linha de paragem devem ser eliminados de uma superfície TIN, deixando buracos na superfície. Se a coincidência ocorrer em triângulos limitadores de superfícies, o resultado deve ser uma alteração do limite da superfície.

(3) Os objetos geográficos vetoriais fornecidos como componentes de uma coleção TIN devem cumprir as regras genéricas de coerência estabelecidas para objetos vetoriais.

**1.7.5. Requisitos aplicáveis a sistemas de referência**

(1) Para a medição da profundidade do fundo do mar quando se verifica uma apreciável amplitude de marés (águas de maré), deve ser utilizada a maré astronómica mais baixa (Lowest Astronomical Tide - LAT) como superfície de referência.

(2) Para a medição da profundidade do fundo do mar nas zonas marinhas sem uma amplitude de marés apreciável, em oceanos abertos e em águas com uma profundidade superior a 200 metros, a profundidade do fundo do mar deve ser referenciada ao nível médio do mar (Mean Sea Level - MSL), ou a um nível de referência bem definido próximo do MSL.

(3) A altitude do nível de referência a que a profundidade do fundo de uma massa de água interior é medida deve ser referenciada a um sistema de referência vertical relacionado com a gravidade. Esse sistema deve ser o Sistema Europeu de Referência Vertical (European Vertical Reference System - EVRS) no que diz respeito às áreas no âmbito geográfico do EVRS, ou o sistema de referência vertical relacionado com a gravidade identificado pelo Estado-Membro fora do âmbito do EVRS.

(4) Quando fornecem um modelo altimétrico integrado terra-mar, deve ser modelada apenas uma propriedade altimétrica (a altura ou a profundidade), e os seus valores devem ser referenciados a um único sistema de referência de coordenadas verticais.

**1.7.6. Requisitos aplicáveis à qualidade e coerência dos dados**

(1) Se forem utilizadas medições diferentes das medições ISO referentes à qualidade dos dados para avaliar um conjunto de dados altimétricos, o elemento de metadados «Histórico» deve incluir informações sobre essas medições e, se possível, uma referência a um recurso em linha em que estejam disponíveis mais informações.

(2) Os objetos geográficos de curvas de nível ligadas devem ter o mesmo valor altimétrico quando estão referenciados ao mesmo sistema de referência de coordenadas verticais.

(3) Quando os valores altimétricos de objetos geográficos de linha de rutura são fornecidos como terceiras coordenadas (Z), o ponto de intersecção de dois objetos geográficos de linha de rutura devem ter o mesmo valor altimétrico.

(4) Quando um objeto geográfico de curvas de nível e um objeto geográfico de linha de rutura fornecidos no mesmo sistema de referência de coordenadas verticais se intersetam, o ponto de intersecção deve ter o mesmo valor altimétrico (se os valores altimétricos dos objetos geográficos da linha de rutura forem fornecido pela terceira coordenada (Z)).

(5) Os objetos geográficos de curvas de nível que têm diferentes valores altimétricos não devem intersectar-se nem tocar-se quando são referenciados ao mesmo sistema de referência de coordenadas verticais.

(6) O limite de um objeto geográfico de área isolada não deve tocar no limite externo de um objeto geográfico de área vazia quando esses objetos são referenciados ao mesmo sistema de referência de coordenadas verticais.

**1.8. Camadas**

**Camadas para a categoria temática de dados geográficos «Altitude»**

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

(1) «Sistema de classificação»(classification system) : um sistema para a atribuição de objetos a classes, em conformidade com a norma ISO 19144-1:2012;

(2) «Cobertura discreta»(discrete coverage) : uma cobertura que fornece os mesmos valores do atributo de entidade para cada posição direta em qualquer objeto geográfico, objeto temporal ou objeto espaciotemporal simples no seu domínio, em conformidade com a norma EN ISO 19123:2007;

(3) «Objeto de ocupação do solo»(land cover object) : um objeto geográfico (ponto, pixel ou polígono) em que foi observada a ocupação do solo;

(4) «Legenda»(legend) : a aplicação de uma classificação numa área específica utilizando uma escala cartográfica definida e um conjunto de dados específico;

(5) «Unidade cartográfica mínima»(minimal mapping unit) : a menor área de um polígono cuja representação é permitida num determinado conjunto de dados da ocupação do solo;

(6) «Situação»(situation) : o estado de um determinado objeto de ocupação do solo num determinado momento.

**2.2. Estrutura da categoria temática de dados geográficos «Ocupação do Solo»**

Os tipos especificados para a categoria temática de dados geográficos «Ocupação do Solo» estão estruturados nos seguintes pacotes:

— Nomenclatura da ocupação do solo (Land Cover Nomenclature)

— Vetor de ocupação do solo (Land Cover Vector)

— Raster de ocupação do solo (Land Cover Raster)

**2.3. Nomenclatura da ocupação do solo**

**2.3.1. Tipos de dados**

2.3.1.1. Nomenclatura da ocupação do solo (LandCoverNomenclature)

Informação sobre nomenclaturas de referência de ocupação do solo nacionais, institucionais ou locais.

Atributos do tipo de dados «LandCoverNomenclature»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| responsibleParty | Parte responsável pelo desenvolvimento e/ou manutenção da nomenclatura. | RelatedParty |  |
| externalDescription | Documento que descreve a nomenclatura utilizada neste conjunto de dados. | DocumentCitation | voidable |
| embeddedDescription | Uma codificação incorporada do sistema de classificação de acordo com a norma ISO 19144-2. | LC_LandCoverClassificationSystem | voidable |
| nomenclatureCodeList | Um URI http que aponta para a lista de códigos apensa à nomenclatura utilizada. | URI |  |

Restrições do tipo de dados «LandCoverNomenclature»

Deve ser fornecida a descrição incorporada ou a descrição externa.

**2.3.2. Listas de códigos**

2.3.2.1. Classe de ocupação do solo (LandCoverClassValue)

Classificação ou lista de códigos de ocupação do solo.

**2.4. Vetor de ocupação do solo**

**2.4.1. Tipos de objetos geográficos**

O pacote «Vetor de Ocupação do Solo» contém os seguintes tipos de objetos geográficos:

— Conjunto de dados de ocupação do solo

— Unidade de ocupação do solo

2.4.1.1. Conjunto de dados de ocupação do solo (LandCoverDataset)

Uma representação vetorial para dados de Ocupação do Solo.

Atributos do tipo de objeto geográfico «LandCoverDataset»

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

Associações do tipo de objeto geográfico «LandCoverDataset»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| member | Unidade de ocupação do solo que faz parte do conjunto de dados. | LandCoverUnit |  |

2.4.1.2. Unidade de ocupação do solo (LandCoverUnit)

Um elemento individual do conjunto de dados Ocupação do Solo representado por um ponto ou uma superfície.

Atributos do tipo de objeto geográfico «LandCoverUnit»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| geometry | Representação espacial dos dados Ocupação do Solo. | GM_Object |  |
| landCoverObservation | Informações sobre a ocupação do solo num local e momento específicos. | LandCoverObservation |  |

Restrições do tipo de objeto geográfico «LandCoverUnit»

As geometrias devem ser pontos ou superfícies.

**Associações do tipo de objeto geográfico «LandCoverUnit**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| dataset | Conjunto de dados sobre a ocupação do solo a que pertence este objeto de ocupação do solo. | LandCoverDataset |  |

**2.4.2. Tipos de dados**

2.4.2.1. Observação da ocupação do solo (LandCoverObservation)

Informações sobre a Ocupação do Solo num local e momento específicos.

Atributos do tipo de dados «LandCoverObservation»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| class | Atribuição de uma classe de ocupação do solo a uma unidade de ocupação do solo mediante um identificador de código de classificação. | LandCoverClassValue |  |
| observationDate | Data de observação associada a uma observação. | DateTime | voidable |
| mosaic | Lista de valores de classificação que descreve detalhadamente uma unidade de ocupação do solo, associada a percentagens. | LandCoverValue | voidable |

Restrições do tipo de objeto geográfico «LandCoverObservation»

A soma de todos os atributos «coveredPercentage» associados a cada «LandCoverObservation» deve ser inferior ou igual a 100.

2.4.2.2. Ocupação do solo (LandCoverValue)

Classe genérica subjacente ao valor e percentagem de Ocupação do Solo.

Atributos do tipo de dados «LandCoverValue»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| class | Atribuição de um objeto geográfico de ocupação do solo a uma classe de ocupação do solo mediante um identificador de código de classificação. | LandCoverClassValue |  |
| coveredPercentage | Fração da «LandCoverUnit» a que diz respeito o valor de classificação. | Integer | voidable |

**2.5. Raster de ocupação do solo**

**2.5.1. Tipos de objetos geográficos**

O pacote «

Raster de Ocupação do Solo» contém o tipo de objeto geográfico Cobertura Matricial da Ocupação do Solo.

2.5.1.1. Cobertura matricial da ocupação do solo (LandCoverGridCoverage)

Uma representação rasterizada para dados de Ocupação do Solo.

Este tipo é um subtipo de «RectifiedGridCoverage».

Atributos do tipo de objeto geográfico «LandCoverGridCoverage»

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

Restrições do tipo de objeto geográfico «LandCoverGridCoverage»

Os valores no conjunto da gama de valores estão restringidos a um número inteiro.

**2.6. Requisitos específicos de categorias temáticas**

Se é fornecido

um atributo «externalDescription»

para um tipo de dados «LandCoverNomenclature», a descrição em linha referenciada deve definir, para cada classe, pelo menos um código, um nome, uma definição e um valor RGB a utilizar para fins de representação. Se a descrição em linha descreve a nomenclatura para um objeto «LandCoverGridCoverage», deve também ser fornecido um código de quadrícula do tipo número inteiro («Integer») para cada classe. Este código deve ser utilizado na gama de valores da «LandCoverGridCoverage» a fim de representar a classe correspondente.

**2.7. Camadas**

**Camadas para a categoria temática de dados geográficos «Ocupação do Solo»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| LC.LandCoverPoints | Pontos de ocupação do solo | LandCoverUnit |
| LC.LandCoverSurfaces | Superfícies de ocupação do solo | LandCoverUnit |
| LC.LandCoverRaster | Raster de ocupação do solo | LandCoverGridCoverage |

**3. ORTOIMAGENS (ORTHOIMAGERY)**

**3.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) «Mosaico»(mosaic) : uma imagem composta por uma fusão de múltiplas fotografias ou imagens adjacentes ou em sobreposição.

(2) «Agregação de ortoimagens»(orthoimage aggregation) : uma combinação de subconjuntos provenientes de várias coberturas homogéneas de ortoimagens que formam uma nova cobertura de ortoimagens.

(3) «Raster» : um padrão normalmente retangular de linhas de varrimento paralelas que formam, ou correspondem a, uma visualização num tubo de raios catódicos, em conformidade com a norma EN ISO 19123:2007.

**3.2. Tipos de objetos geográficos**

São especificados os seguintes tipos de objetos geográficos para a categoria temática de dados geográficos «Ortoimagens»:

— Cobertura de ortoimagens

— Elemento de mosaico

— Elemento de mosaico único

— Elemento de mosaico agregado

**3.2.1. Cobertura de ortoimagens (OrthoimageCoverage)**

Imagem rasterizada da superfície da Terra que foi geometricamente corrigida («ortorretificada») a fim de eliminar a distorção causada por diferenças na altimetria e inclinação do sensor e, opcionalmente, pela ótica do sensor.

Este tipo é um subtipo de «RectifiedGridCoverage».

Atributos do tipo de objeto geográfico «OrthoimageCoverage»

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

Associações do tipo de objeto geográfico «OrthoimageCoverage»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| contributingOrthoimageCoverage | Referência às coberturas de ortoimagens que compõem uma cobertura de ortoimagens agregadas. <br> A associação tem propriedades adicionais conforme definido na classe de associação «OrthoimageAggregation». | OrthoimageCoverage |  |
| mosaicElement | Representação espacial do momento de aquisição de uma cobertura de ortoimagens em mosaico. | MosaicElement | voidable |

Restrições do tipo de objeto geográfico «OrthoimageCoverage»

O momento de aquisição da cobertura de ortoimagens deve ser fornecido através do atributo «phenomenonTime» ou da associação «mosaicElement».

A dimensão da quadrícula utilizada deve ser sempre 2.

O atributo «domainExtent» deve estar preenchido, pelo menos, com um subtipo de «EX_GeographicExtent».

Deve ser fornecido o sistema de referência de coordenadas utilizado para referenciar a quadrícula.

Todas as instâncias de «OrthoimageCoverage», a que se refere uma instância de «OrthoimageCoverage» agregada, devem partilhar a mesma orientação dos eixos da quadrícula e o mesmo espaçamento de quadrículas em cada direção.

A origem da quadrícula deve ser descrita em duas dimensões.

Os valores no conjunto da gama de valores devem ser descritos pelo tipo «Integer».

**3.2.2. Elemento de mosaico (MosaicElement)**

Tipo abstrato que identifica tanto a área contribuinte como o tempo de aquisição de uma ou várias imagens de entrada utilizadas para gerar uma cobertura de ortoimagens em mosaico.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «MosaicElement»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| geometry | Representação geométrica que delimita espacialmente a data e a hora de aquisição das várias imagens de entrada que contribuem para o mosaico final. | GM_MultiSurface |  |
| phenomenonTime | Descrição da extensão da aquisição/observação no tempo da(s) imagem(ns) de entrada. | TM_Period |  |

**3.2.3. Elemento de mosaico único (SingleMosaicElement)**

Elemento de mosaico relativo a uma única imagem de entrada.

Este tipo é um subtipo de «MosaicElement».

Atributos do tipo de objeto geográfico «SingleMosaicElement»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| imageSourceReference | Referência à imagem de entrada. | CharacterString | voidable |

**3.2.4. Elemento de mosaico agregado (AggregatedMosaicElement)**

Elemento de mosaico relacionado com várias imagens de entrada que partilham o mesmo momento de aquisição a um determinado nível de definição (por exemplo, dia, mês).

Este tipo é um subtipo de «MosaicElement».

**3.3. Tipos de dados**

**3.3.1. Agregação de ortoimagens (OrthoimageAggregation)**

Características geométricas da agregação de ortoimagens.

Este tipo é uma classe de associação.

Atributos do tipo de dados «OrthoimageAggregation»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| contributingFootprint | Representação geométrica que delimita a área geográfica de uma cobertura de ortoimagens que contribui para a cobertura de ortoimagens agregadas. | GM_MultiSurface |  |

**3.4. Listas de códigos**

**3.4.1. Método de interpolação (InterpolationMethodValue)**

Lista dos códigos que identificam os métodos de interpolação que podem ser utilizados para avaliar as coberturas de ortoimagens.

**3.5 Requisitos específicos de categorias temáticas**

**3.5.1. Requisitos aplicáveis a identificadores de objetos externos**

(1) Se uma ortoimagem for atualizada com base em novos dados-fonte, deve ser atribuído aos objetos atualizados um novo identificador de objeto externo.

**3.5.2. Requisitos aplicáveis a coberturas de ortoimagens**

(1) Em derrogação ao requisito estabelecido no ponto 2.2 do anexo II, pode ser utilizada qualquer quadrícula compatível com um dos seguintes sistemas de referência de coordenadas para a disponibilização de dados matriciais de ortoimagens:

— coordenadas geodésicas bidimensionais (latitude e longitude) baseadas num datum especificado no ponto 1.2. do anexo II e nos parâmetros da elipsoide do GRS80;

— coordenadas planas baseadas no sistema de referência de coordenadas de projeção cónica conforme de Lambert do ETRS89;

— coordenadas planas baseadas no sistema de referência de coordenadas de projeção transversa de Mercator do ETRS89;

Não deve ser utilizada a quadrícula referida no ponto 2.2.1 do anexo II.

(2) A «pegada» de uma instância de «OrthoimageCoverage» deve ser espacialmente incluída na sua extensão geográfica que é descrita com a propriedade «domainExtent».

(3) O tipo de valor da propriedade de metadados representado pelo tipo de objeto geográfico «OrthoimageCoverage» deve ser definido como «OM_Observation» quando se utiliza o modelo de metadados «Observation and Measurement» definido na norma ISO 19156:2011.

(4) Todas as instâncias de «OrthoimageCoverage», a que se refere uma instância de «OrthoimageCoverage» agregada, devem ser coerentes. Isto significa que devem partilhar o mesmo tipo de gama de valores, sistema de referência de coordenadas e resolução. Devem também suportar o alinhamento de quadrículas, ou seja os pontos da quadrícula numa instância de «OrthoimageCoverage» devem estar alinhados com os pontos da quadrícula das outras instâncias de «OrthoimageCoverage», para que as células da quadrícula não se sobreponham parcialmente.

(5) A «pegada» de uma instância de «OrthoimageCoverage» referenciada por uma instância de «OrthoimageCoverage» agregada deve ser espacialmente incluída na sua própria pegada.

(6) As «pegadas» de quaisquer duas instâncias de «OrthoimageCoverage» referenciadas pela mesma instância de «OrthoimageCoverage» agregada devem ser adjacentes ou não adjacentes.

(7) A união das pegadas das instâncias de «OrthoimageCoverage» referenciadas pela mesma instância de «OrthoimageCoverage» agregada deve determinar a «pegada» da instância de «OrthoimageCoverage» agregada.

**3.5.3. Requisitos aplicáveis a elementos de mosaico**

(1) Todos os elementos de mosaico relacionados com uma instância de «OrthoimageCoverage» devem ser do mesmo tipo, ou seja, «SingleMosaicElement» ou «AggregatedMosaicElement».

(2) As geometrias que delimitam quaisquer duas instâncias de «MosaicElement» relacionadas com a mesma instância de «OrthoimageCoverage» devem ser adjacente ou não adjacentes.

(3) A união das geometrias que delimitam todas as instâncias do «MosaicElement» relacionadas com a mesma instância de «OrthoimageCoverage» deve incluir a sua «pegada» e estar contida na sua extensão de domínio geográfico.

**3.5.4. Requisitos aplicáveis a sistemas de referência**

(1) Os dados relacionados com a categoria temática de dados geográficos «Ortoimagens» devem ser limitados a geometrias bidimensionais.

(2) Serão utilizados apenas sistemas de referência de coordenadas bidimensionais para representar conjuntos de dados de ortoimagens INSPIRE.

**3.5.5. Requisitos aplicáveis à qualidade dos dados**

(1) As medidas «erro médio quadrático em X» (root mean square error in X - RMSE-x) e «erro médio quadrático em Y» (root mean square error in Y - RMSE-Y) devem ser fornecidas em conjunto quando utilizadas para avaliar a posição dos dados matriciais presentes nos dados de ortoimagens.

**3.6. Camadas**

**Camadas para a categoria temática de dados geográficos «Ortoimagens»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| OI.OrthoimageCoverage | cobertura de ortoimagens | OrthoimageCoverage |
| OI.MosaicElement | elemento de mosaico | MosaicElement |

**4. GEOLOGIA**

**4.1. Estrutura da categoria temática de dados geográficos «Geologia»**

Os tipos especificados para a categoria temática de dados geográficos «Geologia» estão estruturados nos seguintes pacotes:

— Geologia (Geology)

— Geofísica (Geophysics)

— Hidrogeologia (Hydrogeology)

**4.2. Geologia**

**4.2.1. Tipos de objetos geográficos**

O pacote «Geologia» contém os seguintes tipos de objetos geográficos:

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

4.2.1.1. Característica geomorfológica antropogénica (AnthropogenicGeomorphologicFeature)

Uma característica geomorfológica (ou seja, configuração do terreno) que foi criada pela atividade humana.

Este tipo é um subtipo de «GeomorphologicFeature».

Atributos do tipo de objeto geográfico «AnthropogenicGeomorphologicFeature»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| anthropogenicGeomorphologicFeatureType | Termos utilizados para descrever o tipo de uma característica geomorfológica. | AnthropogenicGeomorphologicFeatureTypeValue |  |

4.2.1.2. Furo (Borehole)

Furo é o termo genérico para designar qualquer perfuração de pequena largura no solo.

Atributos do tipo de objeto geográfico «Borehole»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| boreholeLength | Comprimento do furo. | Quantity | voidable |
| elevation | Altura acima do datum do emboquilhamento do furo. | DirectPosition | voidable |
| location | Localização do emboquilhamento do furo. | GM_Point |  |
| purpose | Objetivo da realização do furo. | BoreholePurposeValue | voidable |
| downholeGeometry | Geometria do fundo do furo | GM_Curve | voidable |

Associações do tipo de objeto geográfico «Borehole»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| logElement | Instâncias de «MappedFeature» 1-D que são intervalos registados (interpretados) dentro de um furo. | MappedInterval | voidable |

4.2.1.3. Dobra (Fold)

Uma ou mais camadas, superfícies ou linhas sistematicamente curvas numa massa rochosa.

Este tipo é um subtipo de «GeologicStructure».

Atributos do tipo de objeto geográfico «Fold»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| profileType | Tipo da dobra. | FoldProfileTypeValue | voidable |

4.2.1.4. Coleção geológica (GeologicCollection)

Uma coleção de objetos geológicos ou geofísicos.

Atributos do tipo de objeto geográfico «GeologicCollection»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| name | Nome da coleção. | CharacterString |  |
| collectionType | Tipo da coleção. | CollectionTypeValue |  |
| reference | Referência à coleção. | DocumentCitation | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

Associações do tipo de objeto geográfico «GeologicCollection»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| geophObjectSet | Um membro de «GeophObjectSet» da coleção geológica. | GeophObjectSet | voidable |
| geophObjectMember | Um «GeophObjectMember» da coleção geológica. | GeophObject | voidable |
| boreholeMember | Um membro de «Borehole» de uma coleção geológica. | Borehole | voidable |
| mapMember | Um membro de «MappedFeature» de uma coleção geológica. | MappedFeature | voidable |

4.2.1.5. Evento geológico (GeologicEvent)

Um evento identificável durante o qual um ou mais processos geológicos alteram entidades geológicas.

Atributos do tipo de objeto geográfico «GeologicEvent»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| name | Nome do evento geológico. | CharacterString | voidable |
| eventEnvironment | Contexto físico em que o evento geológico ocorre. | EventEnvironmentValue | voidable |
| eventProcess | O ou os processos que ocorreram durante o evento geológico. | EventProcessValue | voidable |
| olderNamedAge | Limite mais antigo da idade do evento geológico. | GeochronologicEraValue | voidable |
| youngerNamedAge | Limite mais recente da idade do evento geológico. | GeochronologicEraValue | voidable |

4.2.1.6. Característica geológica (GeologicFeature)

Uma característica geológica conceptual que se supõe existir de forma coerente no mundo.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «GeologicFeature»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| name | Nome da característica geológica. | CharacterString | voidable |

Associações do tipo de objeto geográfico «GeologicFeature»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| themeClass | Classificação temática da característica geológica. | ThematicClass | voidable |
| geologicHistory | Associação que relaciona um ou mais eventos geológicos com uma característica geológica para descrever a sua idade ou história geológica. | GeologicEvent | voidable |

4.2.1.7. Estrutura geológica (GeologicStructure)

Uma configuração de matéria na Terra baseada na falta de homogeneidade, no padrão ou na fratura passível de descrição num material terrestre.

Este tipo é um subtipo de «GeologicFeature».

Este tipo é abstrato.

4.2.1.8. Unidade geológica (GeologicUnit)

Um volume de rocha com características distintas.

Este tipo é um subtipo de «GeologicFeature».

Atributos do tipo de objeto geográfico «GeologicUnit»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geologicUnitType | Tipo da unidade geológica. | GeologicUnitTypeValue |  |

Associações do tipo de objeto geográfico «GeologicUnit»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| composition | Descreve a composição da unidade geológica. | CompositionPart | voidable |

4.2.1.9. Característica geomorfológica (GeomorphologicFeature)

Um tipo de objeto geográfico abstrato que descreve a forma e a natureza da superfície terrestre da Terra (ou seja, uma configuração do terreno).

Este tipo é um subtipo de «GeologicFeature».

Este tipo é abstrato.

4.2.1.10. Característica cartográfica (MappedFeature)

Uma representação espacial de uma «GeologicFeature»

Atributos do tipo de objeto geográfico «MappedFeature»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| shape | Geometria da característica cartográfica. | GM_Object |  |
| mappingFrame | Superfície sobre a qual a característica cartográfica está projetada. | MappingFrameValue |  |

Associações do tipo de objeto geográfico «MappedFeature»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| specification | Associação descritiva que liga a característica cartográfica a uma noção de característica geológica. | GeologicFeature |  |

4.2.1.11. Intervalo cartográfico (MappedInterval)

Um tipo especial de característica cartográfica cuja forma é um intervalo 1-D e que utiliza o sistema de referência geográfica do furo que a contém.

Este tipo é um subtipo de «MappedFeature».

4.2.1.12. Característica geomorfológica natural (NaturalGeomorphologicFeature)

Característica geomorfológica (ou seja, configuração do terreno) que foi gerada pelos processos naturais da Terra.

Este tipo é um subtipo de «GeomorphologicFeature».

Atributos do tipo de objeto geográfico «NaturalGeomorphologicFeature»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| naturalGeomorphologicFeatureType | Tipo da característica geomorfológica natural. | NaturalGeomorphologicFeatureTypeValue |  |
| activity | Nível de atividade da característica geomorfológica natural. | GeomorphologicActivityValue | voidable |

4.2.1.13. Estrutura de deslocamento de corte (ShearDisplacementStructure)

Estruturas de estilo friável a dúctil ao longo das quais ocorreram deslocamentos.

Este tipo é um subtipo de «GeologicStructure».

Atributos do tipo de objeto geográfico «ShearDisplacementStructure»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| faultType | Refere-se a um vocabulário de termos que descrevem o tipo de estrutura de deslocamento de corte. | FaultTypeValue |  |

**4.2.2. Tipos de dados**

4.2.2.1. Parte da composição (CompositionPart)

A composição de uma unidade geológica em termos de constituintes litológicos.

Atributos do tipo de dados «CompositionPart»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| material | Material que compõe uma parte ou a totalidade da unidade geológica. | LithologyValue |  |
| proportion | Quantidade que especifica a fração da unidade geológica composta pelo material. | QuantityRange | voidable |
| role | Relação da parte da composição com a composição da unidade geológica no seu todo. | CompositionPartRoleValue |  |

4.2.2.2. Classe temática (ThematicClass)

Um classificador temático genérico para permitir a reclassificação de Características Geológicas com classes definidas pelos utilizadores adequadas para mapas temáticos.

Atributos do tipo de dados «ThematicClass»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| themeClass | Valor da classe temática. | ThematicClassValue |  |
| themeClassification | Classificação utilizada. | ThematicClassificationValue |  |

**4.2.3. Listas de códigos**

4.2.3.1. Tipo de característica geomorfológica antropogénica (AnthropogenicGeomorphologicFeatureTypeValue)

Tipos de características geomorfológicas antropogénicas.

4.2.3.2. Finalidade do furo (BoreholePurposeValue)

Fins para os quais foi feito o furo.

4.2.3.3. Tipo de coleção (CollectionTypeValue)

Tipos de coleções de objetos geológicos e geofísicos.

4.2.3.4. Função da parte da composição (CompositionPartRoleValue)

As funções que uma parte da composição desempenha numa unidade geológica.

4.2.3.5. Ambiente do evento (EventEnvironmentValue)

Termos para os ambientes geológicos no âmbito dos quais ocorrem eventos geológicos.

4.2.3.6. Processo do evento (EventProcessValue)

Termos que especificam o processo ou processos que ocorreram durante um evento.

4.2.3.7. Tipo de falha (FaultTypeValue)

Termos utilizados para descrever o tipo de estrutura de deslocamento de corte.

4.2.3.8. Tipo de perfil da dobra (FoldProfileTypeValue)

Termos que especificam o tipo de dobra.

4.2.3.9. Período geocronológico (GeochronologicEraValue)

Termos que especificam unidades geológicas temporais reconhecidas.

4.2.3.10. Tipo de unidade geológica (GeologicUnitTypeValue)

Termos que descrevem o tipo de unidade geológica.

4.2.3.11. Atividade geomorfológica (GeomorphologicActivityValue)

Termos que indicam o nível de atividade de uma característica geomorfológica.

4.2.3.12. Litologia (LithologyValue)

Termos que descrevem a litologia.

4.2.3.13. Quadro cartográfico (MappingFrameValue)

Termos que indicam a superfície sobre a qual é projetada a «MappedFeature».

4.2.3.14. Tipo de característica geomorfológica natural (NaturalGeomorphologicFeatureTypeValue)

Termos que descrevem o tipo de característica geomorfológica natural.

4.2.3.15. Classe temática (ThematicClassValue)

Valores para a classificação temática das características geológicas.

4.2.3.16. Classificação temática (ThematicClassificationValue)

Lista de classificações temáticas para características geológicas.

**4.3. Geofísica**

**4.3.1. Tipos de objetos geográficos**

O pacote «Geofísica» contém os seguintes tipos de objetos geográficos:

— Campanha

— Medição geofísica

— Objeto geofísico

— Conjunto de objetos geofísicos

— Perfil geofísico

— Estação geofísica

— Faixa geofísica

— Geophysical Measurement

4.3.1.1. Campanha (Campaign)

Atividade geofísica que decorre durante um período de tempo limitado e numa área limitada para produzir medições geofísicas similares e processar os resultados ou modelos.

Este tipo é um subtipo de «GeophObjectSet».

Atributos do tipo de objeto geográfico «Campaign»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| campaignType | Tipo de atividade para a produção de dados. | CampaignTypeValue |  |
| surveyType | Tipo de levantamento geofísico. | SurveyTypeValue |  |
| client | Parte para a qual foram criados os dados. | RelatedParty | voidable |
| contractor | Parte através da qual os dados foram criados. | RelatedParty | voidable |

Restrições do tipo de objeto geográfico «Campaign»

O atributo da forma deve ser do tipo «GM_Surface».

4.3.1.2. Objeto geofísico (GeophObject)

Uma classe genérica para objetos geofísicos.

Este tipo é um subtipo de «SF_SpatialSamplingFeature».

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «GeophObject»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| citation | Citação de documentação geofísica. | DocumentCitation |  |
| projectedGeometry | Projeção 2D da característica na superfície do solo (como um ponto, curva ou polígono delimitador representativo) a utilizar por um serviço de visualização INSPIRE para visualizar a localização do objeto geográfico numa carta. | GM_Object |  |
| verticalExtent | Extensão vertical da gama de interesse. | EX_VerticalExtent | voidable |
| distributionInfo | Metadados de distribuição. | MD_Distributor | voidable |
| largerWork | Identificador de um maior conjunto de dados de trabalho, geralmente uma campanha ou projeto. | Identifier | voidable |

Restrições do tipo de objeto geográfico «GeophObject»

O atributo de «projectedGeometry» deve ser do tipo «GM_Point», «GM_Curve» ou «GM_Surface».

4.3.1.3. Medição geofísica (GeophMeasurement)

Um tipo genérico de objeto geográfico para medições geofísicas.

Este tipo é um subtipo de «GeophObject».

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «GeophMeasurement»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| relatedModel | Identificador do modelo geofísico que foi criado a partir da medição. | Identifier | voidable |
| platformType | Plataforma a partir da qual foi efetuada a medição. | PlatformTypeValue |  |
| relatedNetwork | Nome de uma rede de observação nacional ou internacional a que pertence a instalação, ou à qual são comunicados os dados das medições. | NetworkNameValue | voidable |

4.3.1.4. Conjunto de objetos geofísicos (GeophObjectSet)

Uma classe genérica para coleções de objetos geofísicos.

Este tipo é um subtipo de «SF_SpatialSamplingFeature».

Atributos do tipo de objeto geográfico «GeophObjectSet»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| citation | Citação de documentação geofísica. | DocumentCitation |  |
| verticalExtent | Extensão vertical da gama de interesse. | EX_VerticalExtent | voidable |
| distributionInfo | Metadados de distribuição. | MD_Distributor | voidable |
| projectedGeometry | Projeção 2D da característica na superfície do solo (como um ponto, curva ou polígono delimitador representativo) a utilizar por um serviço de visualização INSPIRE para visualizar a localização do objeto geográfico numa carta. | GM_Object |  |
| largerWork | Identificador de um maior conjunto de dados de trabalho. | Identifier | voidable |

Restrições do tipo de objeto geográfico «GeophObjectSet»

O atributo de «projectedGeometry» deve ser do tipo «GM_Point», «GM_Curve» ou «GM_Surface».

4.3.1.5. Perfil geofísico (GeophProfile)

Uma medição geofísica referenciada espacialmente a uma curva.

Este tipo é um subtipo de «GeophMeasurement».

Atributos do tipo de objeto geográfico «GeophProfile»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| profileType | Tipo de perfil geofísico. | ProfileTypeValue |  |

Restrições do tipo de objeto geográfico «GeophProfile»

O atributo da forma deve ser do tipo «GM_Curve».

4.3.1.6. Estação geofísica (GeophStation)

Medição geofísica referenciada geograficamente a um ponto único.

Este tipo é um subtipo de «GeophMeasurement».

Atributos do tipo de objeto geográfico «GeophStation»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| stationType | Tipo de estação geofísica. | StationTypeValue |  |
| stationRank | As estações geofísicas podem fazer parte de um sistema hierárquico. A ordenação é proporcional à importância da estação. | StationRankValue | voidable |

Restrições do tipo de objeto geográfico «GeophStation»

O atributo da forma deve ser do tipo «GM_Point».

4.3.1.7. Faixa geofísica (GeophSwath)

Uma medição geofísica espacialmente referenciada a uma superfície.

Este tipo é um subtipo de «GeophMeasurement».

Atributos do tipo de objeto geográfico «GeophSwath»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| swathType | Tipo de faixa geofísica. | SwathTypeValue |  |

Restrições do tipo de objeto geográfico «GeophSwath»

O atributo da forma deve ser do tipo «GM_Surface».

**4.3.2. Listas de códigos**

4.3.2.1. Tipo de campanha (CampaignTypeValue)

Um tipo de campanha geofísica.

4.3.2.2. Nome da rede (NetworkNameValue)

Um nome da rede geofísica.

4.3.2.3. Tipo de plataforma (PlatformTypeValue)

Uma plataforma na qual foi efetuada a aquisição de dados.

4.3.2.4. Tipo de perfil (ProfileTypeValue)

Tipo de perfil geofísico.

4.3.2.5. Posição da estação na classificação (StationRankValue)

A posição hierárquica da estação geofísica na classificação.

4.3.2.6. Tipo de estação (StationTypeValue)

Um tipo de estação geofísica.

4.3.2.7. Tipo de levantamento (SurveyTypeValue)

Um tipo de levantamento ou conjunto de dados geofísico.

4.3.2.8. Tipo de faixa (SwathTypeValue)

Um tipo de faixa geofísica.

**4.4. Hidrogeologia (Hydrogeology)**

**4.4.1. Tipos de objetos geográficos**

O pacote «Hidrogeologia» contém os seguintes tipos de objetos geográficos:

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

4.4.1.1. Poço em atividade (ActiveWell)

Um poço que influencia os recursos freáticos do aquífero.

Este tipo é um subtipo de «HydrogeologicalObjectManMade».

Atributos do tipo de objeto geográfico «ActiveWell»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| activityType | Tipo de atividade do poço. | ActiveWellTypeValue |  |

Associações do tipo de objeto geográfico «ActiveWell»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| groundWaterBody | «GroundWaterBody» do qual o «ActiveWell» extrai os recursos fréaticos. | GroundWaterBody | voidable |
| environmentalMonitoringFacility | «Environmentalmonitoringfacility» conexa. | EnvironmentalMonitoringFacility | voidable |
| borehole | «Borehole» em que o «ActiveWell» está baseado. | Borehole | voidable |

4.4.1.2. Aquiclude (Aquiclude)

Uma massa impermeável de rocha ou estrato de sedimentos que funciona como uma barreira ao escoamento de águas subterrâneas.

Este tipo é um subtipo de «HydrogeologicalUnit».

4.4.1.3. Aquífero (Aquifer)

Uma camada subterrânea húmida de rocha permeável com aquífero ou materiais não consolidados (gravilha, areia, limo ou argila) a partir da qual podem ser utilmente extraídas águas subterrâneas através de um poço de água.

Este tipo é um subtipo de «HydrogeologicalUnit».

Atributos do tipo de objeto geográfico «Aquifer»

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

Associações do tipo de objeto geográfico «Aquifer»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| aquitard | Aquitardo(s) que separa(m) o aquífero. | Aquitard | voidable |
| hydrogeologicalObject | O(s) «HydrogeologicalObject» relacionados com o aquífero. | HydrogeologicalObject | voidable |
| aquiferSystem | «AquiferSystem» específico em que ocorre o «Aquitard». | AquiferSystem | voidable |

4.4.1.4. Sistema aquífero (AquiferSystem)

Uma coleção de aquíferos e aquitardos que, no seu conjunto, constituem o meio ambiente das águas subterrâneas – «vasos comunicantes», que estão cheios ou podem ser cheios com água.

Este tipo é um subtipo de «HydrogeologicalUnit».

Atributos do tipo de objeto geográfico «AquiferSystem»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| isLayered | Indica se o «AquiferSystem» é constituído por mais de uma camada. | Boolean | voidable |

Associações do tipo de objeto geográfico «AquiferSystem»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| aquitard | Aquitardo(s) contido(s) no «AquiferSystem». | Aquitard | voidable |
| aquiclude | Aquiclude que envolve o «AquiferSystem» | Aquiclude | voidable |
| aquifer | O(s) aquífero(s) contido(s) no «AquiferSystem». | Aquifer | voidable |

4.4.1.5. Aquitardo (Aquitard)

Um leito saturado, mas pouco permeável, que dificulta a circulação das águas subterrâneas.

Este tipo é um subtipo de «HydrogeologicalUnit».

Atributos do tipo de objeto geográfico «Aquitard»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| approximatePermeabilityCoefficient | Volume de um fluido incompressível que se escoa durante uma unidade de tempo através de uma unidade de volume cúbica constituída por uma substância porosa na qual é mantida uma diferença de pressão unitária. | QuantityValue | voidable |
| approximateStorativityCoefficient | Capacidade de armazenamento de água de um aquífero. | QuantityValue | voidable |

Associações do tipo de objeto geográfico «Aquitard»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| aquiferSystem | «AquiferSystem» de que faz parte o «Aquitard». | AquiferSystem | voidable |
| aquifer | Aquíferos separados pelo aquitardo. | Aquifer | voidable |

4.4.1.6. Massa de águas subterrâneas (GroundWaterBody)

Um volume distinto de águas subterrâneas num aquífero ou sistema de aquíferos, que está isolado do ponto de vista hidráulico de massas de água subterrâneas próximas.

Atributos do tipo de objeto geográfico «GroundWaterBody»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| approximateHorizontalExtend | Geometria que define a fronteira da «GroundWaterBody». | GM_Surface | voidable |
| conditionOfGroundWaterBody | Grau aproximado de alteração nas águas subterrâneas resultante da atividade humana. | ConditionOfGroundwaterValue |  |
| mineralization | Uma das principais características químicas da água. O seu valor é a soma das concentrações químicas de todos os componentes da água. | WaterSalinityValue | voidable |
| piezometricState | Especifica o estado piezométrico do lençol freático «GroundwaterBody». | PiezometricState | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

Associações do tipo de objeto geográfico «GroundWaterBody»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| activeWell | «ActiveWell» que altera o estado da «GroundwaterBody» através da extração de recursos freáticos. | ActiveWell | voidable |
| aquiferSystem | «AquiferSystem» que inclui a «GroundWaterBody». | AquiferSystem | voidable |
| hydrogeologicalObjectNatural | «HydrogeologicalObjectNatural» que interage com o «GroundwaterBody». | HydrogeologicalObjectNatural | voidable |
| observationWell | Poços de observação que monitorizam a «GroundWaterBody» | EnvironmentalMonitoringFacility | voidable |

4.4.1.7. Objeto hidrogeológico (HydrogeologicalObject)

Uma classe abstrata para meios artificiais ou características naturais que têm uma interação com o sistema hidrogeológico.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «HydrogeologicalObject»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| geometry | Geometria que define a localização espacial do «HydrogeologicalObject». | GM_Primitive |  |
| name | Nome ou código do «HydrogeologicalObject». | PT_FreeText | voidable |
| description | Descrição do «HydrogeologicalObject». | PT_FreeText | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

Associações do tipo de objeto geográfico «HydrogeologicalObject»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| aquifer | Aquífero no qual ocorre o «HydrogeologicalObject». | Aquifer | voidable |

4.4.1.8. Objeto hidrogeológico artificial (HydrogeologicalObjectManMade)

Um objeto hidrogeológico criado pelo homem.

Este tipo é um subtipo de «HydrogeologicalObject».

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «HydrogeologicalObjectManMade»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| validFrom | Data e hora oficiais em que o objeto hidrogeológico foi/será legalmente estabelecido. | DateTime | voidable |
| validTo | Data e hora em que o objeto hidrogeológico deixou/deixará de ser legalmente utilizado. | DateTime | voidable |
| statusCode | Código que define o estatuto formal de um objeto hidrogeológico artificial. | StatusCodeTypeValue | voidable |

4.4.1.9. Objeto hidrogeológico natural (HydrogeologicalObjectNatural)

Objeto hidrogeológico que foi gerado por processos naturais.

Este tipo é um subtipo de «HydrogeologicalObject».

Atributos do tipo de objeto geográfico «HydrogeologicalObjectNatural»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| naturalObjectType | Tipo de objeto hidrogeológico natural. | NaturalObjectTypeValue |  |
| waterPersistence | Grau de persistência do fluxo de água. | WaterPersistenceValue | voidable |
| approximateQuantityOfFlow | Valor aproximado que define o débito de água num objeto hidrogeológico natural. | QuantityValue | voidable |

Associações do tipo de objeto geográfico «HydrogeologicalObjectNatural»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| groundWaterBody | «GroundWateBody» com que a qual o objeto hidrogeológico natural interage. | GroundWaterBody | voidable |

4.4.1.10. Unidade hidrogeológica (HydrogeologicalUnit)

Uma parte da litosfera com parâmetros distintivos para o armazenamento e o transporte de água.

Este tipo é um subtipo de «GeologicUnit».

Atributos do tipo de objeto geográfico «HydrogeologicalUnit»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| description | Descrição da «HydrogeologicalUnit». | PT_FreeText | Voidable |
| approximateDepth | Profundidade aproximada da ocorrência de «HydrogeologicalUnit». | QuantityValue | Voidable |
| approximateThickness | Espessura aproximada da «HydrogeologicalUnit». | QuantityValue | Voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | Voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | Voidable |

Associações do tipo de objeto geográfico «HydrogeologicalUnit»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| geologicStructure | Relaciona uma ou muitas HydrogeologicalUnit» com uma «GeologicStructure». | GeologicStructure | Voidable |

**4.4.2. Tipos de dados**

4.4.2.1. Superfície hidrogeológica (HydrogeologicalSurface)

Uma superfície que representa o lençol freático interpolado ou outra superfície, para uma área local ou regional.

Este tipo é um tipo de união.

Atributos do tipo de união «HydrogeologicalSurface»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| surfaceRectifiedGrid | Superfície cujo domínio consiste numa quadrícula retificada. | RectifiedGridCoverage |  |
| surfaceReferenceableGrid | Superfície cujo domínio consiste numa quadrícula referenciável. | ReferenceableGridCoverage |  |
| surfacePointCollection | Superfície hidrogeológica representada por uma coleção de observações pontuais. | PointObservationCollection |  |

4.4.2.2. Estado piezométrico (PiezometricState)

O estado piezométrico de uma «GroundWaterBody»

Atributos do tipo de dados «PiezometricState»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| observationTime | Data e hora da observação do estado das águas subterrâneas. | DateTime |  |
| piezometricSurface | Superfície que representa o nível a que a água subirá em poços fortemente confinados. | HydrogeologicalSurface |  |

4.4.2.3. Valor quantitativo (QuantityValue)

Um contentor de dados com um único valor quantitativo ou com uma gama de valores quantitativos.

Este tipo é um tipo de união.

Atributos do tipo de união «QuantityValue»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| singleQuantity | Componente escalar com representação decimal e uma unidade de medida utilizada para armazenar o valor de uma quantidade contínua. | Quantity |  |
| quantityInterval | Par decimal para especificar uma gama de quantidades com uma unidade de medida. | QuantityRange |  |

**4.4.3. Listas de códigos**

4.4.3.1. Tipo de poço em atividade (ActiveWellTypeValue)

Tipos de poços ativos.

4.4.3.2. Tipo de meio aquífero (AquiferMediaTypeValue)

Valores que descrevem as características do meio aquífero.

4.4.3.3. Tipo de aquífero (AquiferTypeValue)

Tipos de aquíferos.

4.4.3.4. Estado das águas subterrâneas (ConditionOfGroundwaterValue)

Valores que indicam o grau aproximado da alteração ocorrida no estado natural das águas subterrâneas.

4.4.3.5. Tipo hidrogeoquímico da rocha (HydroGeochemicalRockTypeValue)

Valores que descrevem o estado hidrogeoquímico do ambiente freático.

4.4.3.6. Tipo de objeto natural (NaturalObjectTypeValue)

Tipos de objetos hidrogeológicos naturais.

4.4.3.7. Tipo de código de estatuto (StatusCodeTypeValue)

Os valores que descrevem os estatutos de objetos hidrogeológicos artificiais.

4.4.3.8. Persistência da água (WaterPersistenceValue)

Tipos de persistência hidrológica.

4.4.3.9. Salinidade da água (WaterSalinityValue)

Uma lista de códigos que indica as classes de salinidade da água.

**4.5. Camadas**

**Camadas para a categoria temática de dados geográficos «Geologia»**

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
| (1) <br> Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3 <br> (2) <br> Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3 <br> (3) <br> Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3 <br> (4) <br> Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3 <br> (5) <br> Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3 |  |  |
