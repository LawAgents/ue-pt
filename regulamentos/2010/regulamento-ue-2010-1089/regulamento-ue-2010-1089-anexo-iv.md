---
id: "regulamento-ue-2010-1089-anexo-iv"
celex: "32010R1089"
title: "Regulamento (UE) n. ° 1089/2010 da Comissão, de 23 de Novembro de 2010 , que estabelece as disposições de execução da Directiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Anexo IV"
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
part: "Anexo IV"
---

# Regulamento (UE) n. ° 1089/2010 da Comissão, de 23 de Novembro de 2010 , que estabelece as disposições de execução da Directiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Anexo IV

## Anexo IV

**Requisitos aplicáveis a categorias temáticas de dados geográficos enumeradas no anexo III da Diretiva 2007/2/CE**

**1. UNIDADES ESTATÍSTICAS**

**1.1. Estrutura da categoria temática de dados geográficos «Unidades Estatísticas»**

Os tipos especificados para a categoria temática de dados geográficos «Unidades Estatísticas» estão estruturados nos seguintes pacotes:

— Unidades estatísticas – Base (Statistical Units Base)

— Unidades estatísticas – Modelo vetorial (Statistical Units Vector)

— Unidades estatísticas – Modelo matricial (Statistical Units Grid)

**1.2. Unidades estatísticas - Base**

**1.2.1. Tipos de objetos geográficos**

O pacote «Unidades Estatísticas – Base» contém o tipo de objeto geográfico Unidade Estatística.

1.2.1.1. Unidade estatística (StatisticalUnit)

Unidade para fins de divulgação ou utilização de informação estatística.

Este tipo é abstrato.

**1.3. Unidades estatísticas – Modelo vetorial**

**1.3.1. Tipos de objetos geográficos**

O pacote «Unidades Estatísticas — Modelo Vetorial»

contém os seguintes tipos de objetos geográficos:

— Unidade estatística vetorial

— Unidade estatística de área

— Tesselação estatística

— Evolução

1.3.1.1. Unidade estatística – Modelo vetorial (VectorStatisticalUnit)

Unidade estatística representada como uma geometria vetorial (ponto, linha ou superfície).

Este tipo é um subtipo de «StatisticalUnit».

Atributos do tipo de objeto geográfico «VectorStatisticalUnit»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| thematicId | Identificador descritivo de objeto único aplicado a objetos geográficos numa categoria temática de informação definida. | ThematicIdentifier |  |
| country | Código do país a que o objeto pertence. | CountryCode |  |
| geographicalName | Possíveis nomes geográficos do objeto. | GeographicalName |  |
| statisticalUnitType | Tipo de unidade territorial utilizada para fins de divulgação. | StatisticalUnitTypeValue |  |
| validityPeriod | Período em que supostamente a unidade estatística deve ou não ser preferencialmente utilizada. | TM_Period |  |
| referencePeriod | Período em que os dados dão supostamente uma imagem da divisão territorial em unidades estatísticas. | TM_Period |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

Associações do tipo de objeto geográfico «VectorStatisticalUnit»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Representações geométricas da unidade estatística vetorial. | VectorStatisticalUnitGeometry |  |
| evolutions | Todas as evoluções verificadas na unidade estatística. | Evolution | voidable |

Restrições do tipo de objeto geográfico «VectorStatisticalUnit»

As unidades estatísticas vetoriais com uma instância de geometria de referência

«GM_MultiSurface»

devem ser instâncias da classe especializada

«AreaStatisticalUnit».

1.3.1.2. Unidade estatística de área (AreaStatisticalUnit)

Unidade estatística vetorial com uma geometria de referência de superfície.

Este tipo é um subtipo de «VectorStatisticalUnit».

Atributos do tipo de objeto geográfico «AreaStatisticalUnit»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| areaValue | Área da geometria de referência. | Area |  |
| landAreaValue | Área da parte acima da água. | Area | voidable |
| livableAreaValue | Área da parte habitável. | Area | voidable |

Associações do tipo de objeto geográfico «AreaStatisticalUnit»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| administrativeUnit | Unidades administrativas utilizadas para construir a unidade estatística de área. | AdministrativeUnit | voidable |
| lowers | Unidades estatísticas de área do nível imediatamente inferior. | AreaStatisticalUnit | voidable |
| uppers | Unidades estatísticas de área do nível imediatamente superior. | AreaStatisticalUnit | voidable |
| successors | Sucessores da unidade estatística de área. | AreaStatisticalUnit | voidable |
| predecessors | Predecessores da unidade estatística de área. | AreaStatisticalUnit | voidable |
| tesselation | Tesselação composta de unidades. | StatisticalTessellation | voidable |

Restrições do tipo de objeto geográfico «AreaStatisticalUnit»

A geometria de referência de uma unidade estatística de área deve ser uma

«GM_MultiSurface».

1.3.1.3. Tesselação estatística (StatisticalTessellation)

Uma tesselação composta de unidades estatísticas de área.

Atributos do tipo de objeto geográfico «StatisticalTessellation»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |

Associações do tipo de objeto geográfico «StatisticalTessellation»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| units | Unidades que compõem uma tesselação. | AreaStatisticalUnit | voidable |
| lower | Tesselação estatística imediatamente inferior. | StatisticalTessellation | voidable |
| upper | Tesselação estatística imediatamente superior. | StatisticalTessellation | voidable |

1.3.1.4. Evolução (Evolution)

Representação da evolução de unidades estatísticas vetoriais.

Atributos do tipo de objeto geográfico «Evolution»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| date | Data em que ocorreu a alteração. | DateTime |  |
| evolutionType | Tipo de evolução. | EvolutionTypeValue |  |
| areaVariation | Variação da área durante a evolução. Este atributo só tem de ser preenchido se o tipo for «change» (alteração). | Area | voidable |
| populationVariation | Variação da população durante a evolução. Este atributo só tem de ser preenchido se o tipo for «change» (alteração). | Integer | voidable |

Associações do tipo de objeto geográfico «Evolution»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| finalUnitVersions | Todas as versões finais da unidade afetada pela evolução. | VectorStatisticalUnit | voidable |
| units | Todas as unidades afetadas pela evolução. | VectorStatisticalUnit | voidable |
| initialUnitVersions | Todas as versões iniciais da unidade afetadas pela evolução. | VectorStatisticalUnit | voidable |

Restrições do tipo de objeto geográfico «Evolution»

As representações da evolução devem ser consistentes com as versões dos objetos em causa.

Uma evolução com um «typeValue»

«creation» (criação) não deve ter quaisquer versões iniciais da unidade e apenas deve ter uma final.

Uma evolução com um «typeValue»

«deletion» (supressão) deve ter uma versão inicial da unidade e não deve ter uma final.

Uma evolução com um «typeValue»

«aggregation» (agregação) deve ter, pelo menos, duas versões iniciais das unidades (as unidades a agregar) e uma única final (a agregação resultante).

Uma evolução com um «typeValue»

«change» (alteração) deve ter uma versão inicial da unidade e uma final.

Uma evolução com um «typeValue»

«splitting» (divisão) deve ter uma única versão de unidade inicial (a unidade a dividir) e, pelo menos, duas finais (as unidades resultantes da divisão).

**1.3.2. Tipos de dados**

1.3.2.1. Geometria de unidade estatística vetorial (VectorStatisticalUnitGeometry)

Uma representação geométrica para as unidades estatísticas vetoriais.

Atributos do tipo de dados «VectorStatisticalUnitGeometry»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Geometria. | GM_Object |  |
| geometryDescriptor | Descritor da geometria da unidade estatística. | GeometryDescriptor |  |

1.3.2.2. Descritor de geometria (GeometryDescriptor)

Um descritor para a geometria da unidade estatística vetorial.

Atributos do tipo de dados «GeometryDescriptor»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometryType | Tipo de geometria. | GeometryTypeValue |  |
| mostDetailedScale | Escala mais detalhada a que se pensa que a geometria generalizada é adequada (expressa como o inverso de uma escala indicativa). | Integer |  |
| leastDetailedScale | Escala menos detalhada a que se pensa que a geometria generalizada é adequada (expressa como o inverso de uma escala indicativa). | Integer |  |

Restrições do tipo de dados «GeometryDescriptor»

Os campos

«mostDetailedScale»

e

«leastDetailedScale»

devem ser fornecidos apenas para descritores de geometria com um tipo de

«generalisedGeometry»

Quando fornecida, a

«mostDetailedScale»

deve ser mais pequena que a

«leastDetailedScale»

**1.3.3. Listas de códigos**

1.3.3.1. Tipo de geometria (GeometryTypeValue)

Os valores dos códigos para os tipos de geometrias.

1.3.3.2. Tipo de evolução (EvolutionTypeValue)

Os valores dos códigos para tipos de evolução.

1.3.3.3. Tipo de unidade estatística (StatisticalUnitTypeValue)

Os valores dos códigos para os tipos de unidades estatísticas.

**1.4. Unidades estatísticas – Modelo matricial (Statistical Units Grid)**

**1.4.1. Tipos de objetos geográficos**

O pacote «Quadrículas» contém os seguintes tipos de objetos geográficos:

— Célula de quadrícula estatística

— Quadrícula estatística

1.4.1.1. Célula de quadrícula estatística (StatisticalGridCell)

Unidade para a divulgação ou utilização de informação estatística que é representada por uma célula de quadrícula.

Este tipo é um subtipo de «StatisticalUnit».

Atributos do tipo de objeto geográfico «StatisticalGridCell»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| code | Código da célula. | CharacterString | voidable |
| geographicalPosition | Posição geográfica do canto inferior esquerdo da célula da quadrícula. | DirectPosition | voidable |
| gridPosition | Posição da célula da quadrícula dentro da quadrícula baseada nas coordenadas da quadrícula. | GridPosition | voidable |
| geometry | Geometria da célula da quadrícula. | GM_Surface | voidable |

Associações do tipo de objeto geográfico «StatisticalGridCell»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| lowers | Células da quadrícula estatística imediatamente inferiores. | StatisticalGridCell | voidable |
| upper | Célula da quadrícula estatística imediatamente superior. | StatisticalGridCell | voidable |
| grid | Quadrícula constituída por células. | StatisticalGrid |  |

Restrições do tipo de objeto geográfico «StatisticalGridCell»

A posição da célula deve ser dentro da quadrícula, de acordo com a sua largura e altura.

Deve ser fornecido, no mínimo, um dos atributos «code», «geographicalPosition», «gridPosition» ou «geometry».

Quando são fornecidas várias representações espaciais («code», «geographicalPosition», «gridPosition» e «geometry»), estas devem ser coerentes.

O código deve ser constituído por:

(1) O código de duas letras do país conforme definido no Código de Redação Interinstitucional publicado pelo Serviço das Publicações da União Europeia;

(2) Uma parte de um sistema de referência de coordenadas, representada pela palavra CRS, seguida do código EPSG;

(3) Uma parte de posição e resolução:

— Se o sistema de referência de coordenadas for um sistema de projeção, a palavra RES, seguida da resolução da quadrícula em metros e da letra m. Depois, a letra N, seguida do valor da coordenada Norte em metros, e a letra E, seguida do valor da coordenada Este em metros.

— Se o sistema de referência de coordenadas não for um sistema de projeção, a palavra RES, seguida da resolução da quadrícula em graus-minutos-segundos, seguida da palavra dms. Depois, a palavra LON, seguida do valor da longitude em graus-minutos-segundos, e a palavra LAT, seguida do valor da latitude em graus-minutos-segundos.

Em ambos os casos, a posição dada deve ser a posição do canto inferior esquerdo da célula.

1.4.1.2. Quadrícula estatística (StatisticalGrid)

Uma quadrícula composta de células estatísticas.

Atributos do tipo de objeto geográfico «StatisticalGrid»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| EPSGCode | Código EPSG para identificar o sistema de coordenadas de referência da quadrícula. | Integer |  |
| resolution | Resolução da quadrícula. | StatisticalGridResolution |  |
| origin | Posição do ponto de origem da quadrícula no sistema de coordenadas de referência especificado (se definido). | DirectPosition |  |
| width | Largura da quadrícula, em número de células (se definido). | Integer |  |
| height | Altura da quadrícula, em número de células (se definido). | Integer |  |

Associações do tipo de objeto geográfico «StatisticalGrid»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| cells | Células que compõem a quadrícula. | StatisticalGridCell |  |
| lower | Quadrícula estatística imediatamente inferior. | StatisticalGrid | voidable |
| upper | Quadrícula estatística imediatamente superior. | StatisticalGrid | voidable |

Restrições do tipo de objeto geográfico «StatisticalGrid»

Se o sistema de coordenadas de referência é um sistema de projeção, a resolução deve ser um comprimento. Caso contrário, deve ser um ângulo.

**1.4.2. Tipos de dados**

1.4.2.1. Posição da quadrícula (GridPosition)

A posição de uma célula de quadrícula dentro de uma quadrícula.

Atributos do tipo de dados «GridPosition»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| x | Posição da célula no eixo horizontal, da esquerda para a direita, de 0 para a largura de quadrícula -1. | Integer |  |
| y | Posição da célula no eixo vertical, de baixo para cima, de 0 para a altura de quadrícula -1. | Integer |  |

1.4.2.2. Resolução da quadrícula estatística (StatisticalGridResolution)

Um valor da resolução da unidade estatística.

Este tipo é um tipo de união.

Atributos do tipo de união «StatisticalGridResolution»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| lengthResolution | Resolução de uma distância. | Length |  |
| angleResolution | Resolução de um ângulo. | Angle |  |

**1.5. Requisitos específicos de categorias temáticas**

(1) Deve também ser fornecida, pelo menos, a geometria das unidades estatísticas para as quais os dados estatísticos são disponibilizados no âmbito da INSPIRE. Este requisito aplica-se a categorias temáticas INSPIRE que dizem respeito a unidades estatísticas.

(2) Para fins de utilização pan-europeia, devem ser utilizadas as quadrículas com células da mesma dimensão referidas no ponto 2.2.1 do anexo II. Igualmente para fins de utilização pan-europeia, as dimensões admitidas para as células de quadrículas são 2 m, 5 m, 20 m, 50 m, 200 m, 500 m, 2 000 m, 5 000 m, 20 000 m e 50 000 m.

(3) Os dados estatísticos devem remeter para a respetiva unidade estatística através do identificador de objeto externo («inspireId»), do identificador temático (para unidades vetoriais) ou do código da unidade (para células de quadrículas).

(4) Os dados estatísticos devem remeter para uma versão específica de uma unidade estatística.

**1.6. Camadas**

**Camadas para a categoria temática de dados geográficos «Unidades Estatísticas»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| SU.VectorStatisticalUnit | Unidades estatísticas vetoriais | VectorStatisticalUnit |
| SU.StatisticalGridCell | Células de quadrículas estatísticas | StatisticalGridCell |

**2. EDIFÍCIOS**

**2.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) «Dados 2D» (2D data) : os dados em que a geometria dos objetos geográficos é representada num espaço bidimensional.

(2) «Dados 2.5D» (2.5D data) : os dados em que a geometria dos objetos geográficos é representada num espaço tridimensional com a restrição que, para cada posição (X, Y), há apenas um Z.

(3) «Dados 3D» (3D data) : os dados em que a geometria dos objetos geográficos é representada num espaço tridimensional.

(4) «Componente de edifício» (building component) : qualquer subdivisão ou elemento de um edifício.

**2.2. Estrutura da categoria temática de dados geográficos «Edifícios»**

Os tipos especificados para a categoria temática de dados geográficos «Edifícios» estão estruturados nos seguintes pacotes:

— Edifícios - Base (Buildings Base)

— Edifícios 2D (Buildings 2D)

— Edifícios 3D (Buildings 3D)

**2.3. Edifícios - Base**

**2.3.1. Tipos de objetos geográficos**

O pacote «Edifícios – Base» contém os seguintes tipos de objetos geográficos:

— Construção abstrata

— Edifício abstrato

— Edifício

— Parte de edifício

2.3.1.1. Construção abstrata (AbstractConstruction)

Um tipo de objeto geográfico abstrato que agrupa as propriedades semânticas de edifícios, partes de edifícios.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «AbstractConstruction»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| name | Nome da construção. | GeographicalName | voidable |
| dateOfConstruction | Data de construção. | DateOfEvent | voidable |
| dateOfDemolition | Data de demolição. | DateOfEvent | voidable |
| dateOfRenovation | Data da última grande renovação. | DateOfEvent | voidable |
| elevation | Propriedade dimensional restringida à vertical que consiste numa medição absoluta referenciada a uma superfície bem definida que é normalmente tomada como a origem (geoide, nível da água, etc.). | Elevation | voidable |
| externalReference | Referência a um sistema externo de informação que contenha qualquer elemento de informação relacionado com o objeto geográfico. | ExternalReference | voidable |
| heightAboveGround | Altura acima do solo. | HeightAboveGround | voidable |
| conditionOfConstruction | Estado de construção. | ConditionOfConstructionValue | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

2.3.1.2. Edifício abstrato (AbstractBuilding)

Tipo de objeto geográfico abstrato que agrupa as propriedades semânticas comuns dos tipos de objetos geográficos «Building» e «BuildingPart».

Este tipo é um subtipo de «AbstractConstruction».

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «AbstractBuilding»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| buildingNature | Característica do edifício que o torna geralmente de interesse para aplicações cartográficas. A característica pode estar relacionada com o aspeto físico e/ou a função do edifício. | BuildingNatureValue | voidable |
| currentUse | Atividade realizada dentro do edifício. Este atributo visa sobretudo os edifícios em que se realizam atividades humanas. | CurrentUse | voidable |
| numberOfDwellings | Número de habitações. | Integer | voidable |
| numberOfBuildingUnits | Número de unidades habitacionais no edifício. Uma «BuildingUnit» é uma subdivisão de um «Building» com acesso próprio que pode ser fechado à chave a partir do exterior ou de uma área comum (ou seja, não a partir de outra «BuildingUnit»), que é individual e funcionalmente independente e que pode ser separadamente vendida, alugada, herdada, etc. | Integer | voidable |
| numberOfFloorsAboveGround | Número de pisos acima do solo. | Integer | voidable |

2.3.1.3. Edifício (Building)

Um edifício é uma construção fechada acima e/ou abaixo do solo, utilizada ou destinada a ser utilizada para abrigar seres humanos, animais ou objetos ou para a produção de bens económicos. Edifício designa qualquer estrutura construída ou erigida de forma permanente no respetivo local.

Este tipo é um subtipo de «AbstractBuilding».

Este tipo é abstrato.

Associações do tipo de objeto geográfico «Building»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| parts | Partes que compõem o edifício. | BuildingPart do pacote «Edifícios — Base» | voidable |

2.3.1.4. Parte de edifício (BuildingPart)

Uma «BuildingPart» é uma subdivisão de um «Building» que pode ser considerada ela própria um edifício.

Este tipo é um subtipo de «AbstractBuilding».

Este tipo é abstrato.

**2.3.2. Tipos de dados**

2.3.2.1. Utilização atual (CurrentUse)

Este tipo de dados permite detalhar a ou as atuais utilizações.

Atributos do tipo de dados «CurrentUse»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| currentUse | Atual utilização. | CurrentUseValue |  |
| percentage | Parte, expressa em percentagem, dedicada à atual utilização. | Integer |  |

Restrições do tipo de dados «CurrentUse»

O total de todas as percentagens deve ser inferior ou igual a 100.

2.3.2.2. Data do evento (DateOfEvent)

Este tipo de dados inclui as diferentes formas possíveis de definir a data de um evento.

Atributos do tipo de dados «DateOfEvent»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| anyPoint | Data e hora de qualquer ponto do evento, entre o seu início e o seu termo. | DateTime | voidable |
| beginning | Data e hora em que o evento teve início. | DateTime | voidable |
| end | Data e hora em que o evento terminou. | DateTime | voidable |

Restrições do tipo de dados «DateOfEvent»

Deve ser fornecido, no mínimo, um dos atributos «beginning», «end» ou «anyPoint».

Quando fornecido, o atributo «beginning» não deve estar após o atributo «anyPoint» e o atributo «end», e o atributo «anyPoint» não deve estar após o atributo «end».

2.3.2.3. Altitude (Elevation)

Este tipo de dados inclui o valor altimétrico em si mesmo e informações sobre a forma como foi medido.

Atributos do tipo de dados «Elevation»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| elevationReference | Elemento onde foi medida a altitude. | ElevationReferenceValue |  |
| elevationValue | Valor altimétrico. | DirectPosition |  |

2.3.2.4. Referência externa (ExternalReference)

Referência a um sistema externo de informação que contenha qualquer elemento de informação relacionado com o objeto geográfico.

Atributos do tipo de dados «ExternalReference»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| informationSystem | Identificador Uniforme de Recursos (Uniform Resource Identifier) do sistema de informação externa. | URI |  |
| informationSystemName | Nome do sistema de informação externa. | PT_FreeText |  |
| reference | Identificador temático do objeto geográfico ou de qualquer elemento de informação relacionado com o objeto geográfico. | CharacterString |  |

2.3.2.5. Altura acima do solo (HeightAboveGround)

Distância na vertical entre um ponto de referência baixo e alto.

Atributos do tipo de dados «HeightAboveGround»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| heightReference | Elemento utilizado como o ponto de referência alto. | ElevationReferenceValue | voidable |
| lowReference | Elemento utilizado como o ponto de referência baixo. | ElevationReferenceValue | voidable |
| status | Forma como foi obtida a altura. | HeightStatusValue | voidable |
| value | Valor da altura acima do solo. | Length |  |

Restrições do tipo de dados «HeightAboveGround»

O valor de «HeightAboveGround» deve ser expresso em metros.

2.3.2.6. Geometria 2D do edifício (BuildingGeometry2D)

Estes tipos de dados incluem a geometria do edifício e informação de metadados sobre qual o elemento do edifício que foi obtido e o modo como foi obtido.

Atributos do tipo de dados «BuildingGeometry2D»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Representação geométrica 2D ou 2.5D. | GM_Object |  |
| horizontalGeometryEstimatedAccuracy | Exatidão posicional absoluta estimada das coordenadas (X, Y) da geometria do edifício, no Sistema de Referência de Coordenadas INSPIRE oficial. A exatidão posicional absoluta é definida como o valor médio das incertezas posicionais relativamente a um conjunto de posições em que as incertezas posicionais são definidas como a distância entre uma posição medida e a que é considerada a correspondente posição verdadeira. | Length | voidable |
| horizontalGeometryReference | Elemento do edifício que foi representado pelas coordenadas (X Y). | HorizontalGeometryReferenceValue |  |
| referenceGeometry | Geometria a ter em conta pelos serviços de visualização, para fins de representação. | Boolean |  |
| verticalGeometryEstimatedAccuracy | Exatidão posicional absoluta estimada das coordenadas Z da geometria do edifício, no Sistema de Referência de Coordenadas INSPIRE oficial. A exatidão posicional absoluta é definida como o valor médio das incertezas posicionais relativamente a um conjunto de posições em que as incertezas posicionais são definidas como a distância entre uma posição medida e a que é considerada a correspondente posição verdadeira. | Length | voidable |
| verticalGeometryReference | Elemento do edifício que foi representado por coordenadas verticais. | ElevationReferenceValue |  |

Restrições do tipo de dados «BuildingGeometry2D»

A geometria deve ser do tipo «GM_Point», «GM_Surface» ou «GM_MultiSurface».

O valor de «horizontalGeometryEstimatedAccuracy» deve ser expresso em metros.

Para exatamente um elemento de «BuildingGeometry», o valor do atributo «referenceGeometry» deve ser verdadeiro («true»).

O valor de «verticalGeometryEstimatedAccuracy» deve ser expresso em metros.

**2.3.3. Listas de códigos**

2.3.3.1. Natureza do edifício (BuildingNatureValue)

Valores que indicam a natureza de um edifício.

2.3.3.2. Estado da construção (ConditionOfConstructionValue)

Valores que indicam o estado de uma construção.

2.3.3.3. Utilização atual (CurrentUseValue)

Valores que indicam a utilização atual.

2.3.3.4. Referência altimétrica (ElevationReferenceValue)

Lista de possíveis elementos considerados para representar uma geometria vertical.

2.3.3.5. Estatuto da altura (HeightStatusValue)

Valores que indicam o método utilizado para medir uma altura.

2.3.3.6. Referência de geometria horizontal (HorizontalGeometryReferenceValue)

Valores que indicam o elemento considerado para representar uma geometria horizontal.

**2.4. Edifícios 2D (Buildings 2D)**

**2.4.1. Tipos de objetos geográficos**

O pacote «Edifícios 2D» contém os seguintes tipos de objetos geográficos:

— Edifício

— Parte de edifício

2.4.1.1. Edifício (Building)

Um edifício é uma construção fechada acima e/ou abaixo do solo, utilizada ou destinada a ser utilizada para abrigar seres humanos, animais ou objetos ou para a produção de bens económicos. Edifício designa qualquer estrutura construída ou erigida de forma permanente no respetivo local.

Este tipo é um subtipo «Edifício» do pacote «Edifícios - Base».

Atributos do tipo de objeto geográfico «Building»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry2D | Representação geométrica 2D ou 2,5D do edifício. | BuildingGeometry2D |  |

Restrições do tipo de objeto geográfico «Building»

Exatamente um atributo «geometry2D» deve ser uma geometria de referência, ou seja, uma «geometry2D» com um atributo «referenceGeometry» definido como «true» (verdadeiro).

As partes do edifício devem ser representadas utilizando o tipo «BuildingPart» do pacote «Buildings2D».

2.4.1.2. Parte de edifício (BuildingPart)

Uma «BuildingPart» é uma subdivisão de um «Building» que pode ser considerada ela própria um edifício.

Este tipo é um subtipo de «BuildingPart» do pacote «Edifícios - Base».

Atributos do tipo de objeto geográfico «BuildingPart»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry2D | Representação geométrica 2D ou 2.5D da parte do edifício. | BuildingGeometry2D |  |

Restrições do tipo de objeto geográfico «BuildingPart»

Exatamente um atributo «geometry2D» deve ser uma geometria de referência, ou seja, o atributo «referenceGeometry» deve ser «true».

**2.5. Edifícios 3D (Buildings 3D)**

**2.5.1. Tipos de objetos geográficos**

O pacote «Edifícios 3D» contém os seguintes tipos de objetos geográficos:

— Edifício

— Parte de edifício

2.5.1.1. Edifício (Building)

Um edifício é uma construção fechada acima e/ou abaixo do solo, utilizada ou destinada a ser utilizada para abrigar seres humanos, animais ou objetos ou para a produção de bens económicos. Edifício designa qualquer estrutura construída ou erigida de forma permanente no respetivo local.

Este tipo é um subtipo de «Building» do pacote «Edifícios - Base».

Atributos do tipo de objeto geográfico «Building»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry2D | Representação geométrica 2D ou 2.5D. | BuildingGeometry2D | voidable |
| geometry3DLoD1 | Representação geométrica 3D ao nível de detalhe (LoD) 1, constituída pela representação generalizada do limite exterior por superfícies laterais verticais e polígonos de base horizontal. | BuildingGeometry3DLoD1 | — |
| geometry3DLoD2 | Representação geométrica ao nível de detalhe (LoD) 2 constituída pela representação generalizada do limite exterior por superfícies laterais verticais e uma forma prototípica de telhado ou cobertura (a partir de uma lista definida de formas de telhado). | BuildingGeometry3DLoD2 | — |
| geometry3DLoD3 | Representação geométrica ao nível de detalhe (LoD) 3, que consiste na representação detalhada do limite exterior (incluindo protuberâncias, elementos da fachada e aberturas de janelas) bem como da forma do telhado (incluindo janelas de águas-furtadas, chaminés). | BuildingGeometry3DLoD | — |
| geometry3DLoD4 | Representação geométrica ao nível de detalhe (LoD) 4, que consiste na representação detalhada do limite exterior (incluindo protuberâncias, elementos da fachada e aberturas de janelas) bem como da forma do telhado (incluindo janelas de águas-furtadas, chaminés). | BuildingGeometry3DLoD | — |

Restrições do tipo de objeto geográfico «Building»

Se um Edifício não tem quaisquer «BuildingParts», devem ser fornecidos, pelo menos, os atributos «geometry3DLoD1», «geometry3DLoD2», «geometry3DLoD3» ou «geometry3DLoD4».

As partes do edifício devem ser representadas utilizando o tipo «BuildingPart» do pacote «Buildings3D».

2.5.1.2. Parte de edifício (BuildingPart)

Uma «BuildingPart» é uma subdivisão de um «Building» que pode ser considerada ela própria um edifício.

Este tipo é um subtipo de «BuildingPart» no pacote «Edifícios - Base».

Atributos do tipo de objeto geográfico «BuildingPart»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry2D | Representação geométrica 2D ou 2.5D. | BuildingGeometry2D | voidable |
| geometry3DLoD1 | Representação geométrica 3D ao nível de detalhe (LoD) 1, constituída pela representação generalizada do limite exterior por superfícies laterais verticais e polígonos de base horizontal. | BuildingGeometry3DLoD1 | — |
| geometry3DLoD2 | Representação geométrica 3D ao nível de detalhe (LoD) 2, constituída pela representação generalizada do limite externo por superfícies laterais verticais e uma forma prototípica de telhado ou cobertura (a partir de uma lista definida de formas de telhado). | BuildingGeometry3DLoD2 | — |
| geometry3DLoD3 | Representação geométrica 3D ao nível de detalhe (LoD) 3, que consiste na representação detalhada do limite exterior (incluindo protuberâncias, elementos da fachada e aberturas de janelas) bem como da forma do telhado (incluindo janelas de águas-furtadas, chaminés). | BuildingGeometry3DLoD | — |
| geometry3DLoD4 | Representação geométrica 3D ao nível de detalhe (LoD) 4, que consiste na representação detalhada do limite exterior (incluindo protuberâncias, elementos da fachada e aberturas de janelas) bem como da forma do telhado (incluindo janelas de águas-furtadas, chaminés). | BuildingGeometry3DLoD | — |

Restrições do tipo de objeto geográfico «BuildingPart»

Deve ser fornecido, no mínimo, um dos atributos «geometry3DLoD1», «geometry3DLoD2», «geometry3DLoD3» ou «geometry3DLoD4».

**2.5.2. Tipos de dados**

2.5.2.1. Geometria de edifício 3D LoD (BuildingGeometry3DLoD)

Tipo de dados que agrupa a geometria 3D de um edifício ou parte de edifício e a informação de metadados associada a essa geometria.

Atributos do tipo de dados «BuildingGeometry3DLoD»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometryMultiSurface | Representação do limite exterior de uma multissuperfície, que - em contraste com uma representação sólida – pode não ser topologicamente nítida. Pode, em especial, faltar a superfície do solo. | GM_MultiSurface |  |
| geometrySolid | Representação do limite exterior através de um sólido. | GM_Solid |  |
| terrainIntersection | Linha ou multilinhas em que o objeto geográfico («Building», «BuildingPart») toca a representação do terreno. | GM_MultiCurve | voidable |
| horizontalGeometryEstimatedAccuracy | Exatidão posicional absoluta estimada das coordenadas (X, Y) da geometria, no Sistema de Referência de Coordenadas INSPIRE oficial. A exatidão posicional absoluta é definida como o valor médio das incertezas posicionais relativamente a um conjunto de posições em que as incertezas posicionais são definidas como a distância entre uma posição medida e a que é considerada a correspondente posição verdadeira. | Length | voidable |
| verticalGeometryEstimatedAccuracy | Exatidão posicional absoluta estimada da coordenada Z da geometria, no Sistema de Referência de Coordenadas INSPIRE oficial. A exatidão posicional absoluta é definida como o valor médio das incertezas posicionais relativamente a um conjunto de posições em que as incertezas posicionais são definidas como a distância entre uma posição medida e a que é considerada a correspondente posição verdadeira. | Length | voidable |
| verticalGeometryReference3DBottom | Nível altimétrico a que a altura inferior do modelo (valor Z do polígono horizontal inferior) se refere. | ElevationReferenceValue |  |

Restrições do tipo de dados «BuildingGeometry3DLoD»

Deve ser fornecido o atributo «geometryMultiSurface» ou «geometrySolid».

2.5.2.2. Geometria de edifício 3D LoD1 (BuildingGeometry3DLoD1)

Tipo de dados que agrupa os metadados específicos associados à geometria 3D, quando fornecidos por uma representação LoD1.

Este tipo é um subtipo de «BuildingGeometry3DLoD».

Atributos do tipo de dados «BuildingGeometry3DLoD1»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| horizontalGeometryReference | Elemento representado pelas coordenadas (X, Y) da geometria LoD1 de Multissuperficie ou de Sólido. | HorizontalGeometryReferenceValue |  |
| verticalGeometryReference3DTop | Nível altimétrico a que a altura superior do modelo (valor Z do polígono horizontal superior) se refere. | ElevationReferenceValue |  |

Restrições do tipo de dados «BuildingGeometry3DLoD1»

O atributo «horizontalGeometryReference» não deve tomar o valor de «entrancePoint», «pointInsideBuilding» ou «pointInsideCadastralParcel».

2.5.2.3. Geometria de edifício 3D LoD2 (BuildingGeometry3DLoD2)

Tipo de dados que agrupa os metadados específicos associados à geometria 3D, quando fornecidos por uma representação LoD2.

Este tipo é um subtipo de «BuildingGeometry3DloD».

Atributos do tipo de dados «BuildingGeometry3DLoD2»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| horizontalGeometryReference | Elemento representado pelas coordenadas (X, Y) da geometria LoD2 de Multissuperfície ou de Sólido. | HorizontalGeometryReferenceValue |  |

Restrições do tipo de dados «BuildingGeometry3DLoD2»

O atributo «horizontalGeometryReference» não deve tomar o valor de «entrancePoint», «pointInsideBuilding» ou «pointInsideCadastralParcel».

**2.6. Requisitos específicos de categorias temáticas**

(1) Em derrogação do disposto no artigo 12.º, n.º 1, o domínio de valor das propriedades geográficas utilizado no pacote

«Edifícios 3D»

não deve ser restringido.

**2.7. Camadas**

**Camadas para a categoria temática de dados geográficos «Buildings»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| BU.Building | Edifícios | «Building» (do pacote «Edifícios 2D») |
| BU.BuildingPart | Partes de edifício | «BuildingPart» (do pacote «Edifícios 2D») |

Não estão definidas camadas para o pacote «Edifícios 3D».

**3. SOLO (SOIL)**

**3.1. Tipos de objetos geográficos**

São especificados os seguintes tipos de objetos geográficos para a categoria temática de dados geográficos «Solo»:

— Perfil do solo derivado

— Perfil do solo observado

— Elemento do perfil

— Massa de solo

— Objeto derivado do solo

— Horizonte do solo

— Camada de solo

— Parcela de solo

— Perfil do solo

— Sítio de levantamento do solo

— Cobertura do tema solo

— Cobertura descritiva do tema solo

**3.1.1. Perfil do solo derivado (DerivedSoilProfile)**

Um perfil do solo sem um ponto localizado que serve de perfil de referência para um determinado tipo de solo numa determinada área geográfica.

Este tipo é um subtipo de «SoilProfile».

Associações do tipo de objeto geográfico «DerivedSoilProfile»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| isDerivedFrom | Ligação a um ou vários perfis do solo observados a partir dos quais este perfil foi derivado. | ObservedSoilProfile | voidable |

**3.1.2. Perfil do solo observado (ObservedSoilProfile)**

Uma representação de um perfil do solo numa localização específica que é descrita com base em observações numa vala de sondagem ou num furo.

Este tipo é um subtipo de «SoilProfile».

Associações do tipo de objeto geográfico «ObservedSoilProfile»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| location | A localização de um perfil observado é a parcela de solo. | SoilPlot |  |

**3.1.3. Elemento do perfil (ProfileElement)**

Um tipo de objeto geográfico abstrato que agrupa camadas e/ou horizontes do solo para fins funcionais/operacionais.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «ProfileElement»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| particleSizeFraction | Parte mineral do solo, fracionada com base na dimensão (diâmetro) e limites das partículas. Indica a que ponto o material mineral do solo é composto por partículas de solo da gama de dimensões especificada. | ParticleSizeFractionType | voidable |
| profileElementDepthRange | Profundidade superior e inferior do elemento do perfil (camada ou horizonte) medida desde a superfície (0 cm) do perfil de um solo (em cm). | RangeType (definido no ponto 3.2.6) |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

Associações do tipo de objeto geográfico «ProfileElement»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| isPartOf | Ligação para o perfil do solo constituído pelo elemento do perfil. | SoilProfile |  |
| profileElementObservation | Observação de uma propriedade do solo para caracterizar o elemento do perfil (camada ou horizonte). | OM_Observation | voidable |

Restrições do tipo de objeto geográfico «ProfileElement»

Para preencher a propriedade «featureOfInterest» das observações do elemento do perfil de um objeto «ProfileElement», deve ser utilizado o mesmo objeto de «ProfileElement».

A «observedProperty» da observação do elemento do perfil deve ser especificada utilizando um valor da lista de códigos «ProfileElementParameterNameValue».

O resultado da observação do elemento do perfil deve ser de um dos seguintes tipos: «Number», «

RangeType (definido no ponto 3.2.6)

», «CharacterString».

**3.1.4. Massa de solo (SoilBody)**

Parte da cobertura do solo que é delineada e que é homogénea no que diz respeito a determinadas propriedades do solo e/ou padrões espaciais.

Atributos do tipo de objeto geográfico «SoilBody»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| geometry | Geometria que define a fronteira da Massa de Solo. | GM_MultiSurface |  |
| soilBodyLabel | Etiqueta para identificar a massa de solo de acordo com o quadro de referência especificado (metadados). | CharacterString | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

Associações do tipo de objeto geográfico «SoilBody»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| isDescribedBy | Ligação a um perfil do solo derivado que caracteriza a massa de solo, possivelmente em combinação com outros perfis de solo derivados. <br> A associação tem propriedades adicionais conforme definido na classe de associação «DerivedProfilePresenceInSoilBody». | DerivedSoilProfile | voidable |

**3.1.5. Objeto derivado do solo (SoilDerivedObject)**

Um tipo de objeto geográfico para representação de objetos geográficos com propriedades relacionadas com o solo derivadas a partir de um ou mais solos e possivelmente de outras propriedades não relacionadas com o solo.

Atributos do tipo de objeto geográfico «SoilDerivedObject»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Geometria que define o objeto derivado do solo. | GM_Object |  |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |

Associações do tipo de objeto geográfico «SoilDerivedObject»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| isBasedOnSoilDerivedObject | Ligação a um objeto derivado do solo em cujas propriedades se baseia o valor derivado. | SoilDerivedObject | voidable |
| isBasedOnObservedSoilProfile | Ligação a um perfil do solo observado em cujas propriedades se baseia o valor derivado. | ObservedSoilProfile | voidable |
| isBasedOnSoilBody | Ligação a uma massa de solo em cujas propriedades se baseia o valor derivado. | SoilBody | voidable |
| soilDerivedObjectObservation | Observação de uma propriedade do solo para caracterizar o objeto derivado do solo. | OM_Observation | voidable |

Restrições do tipo de objeto geográfico «SoilDerivedObject»

Para preencher a propriedade «featureOfInterest» da observação do objeto derivado do solo, deve ser utilizado o mesmo objeto «SoilDerivedObject».

A «observedProperty» da observação do objeto derivado do solo deve ser especificada utilizando um valor da lista de códigos «SoilDerivedObjectParameterNameValue».

O resultado da observação do objeto derivado do solo deve ser de um dos seguintes tipos: «Number», «

RangeType (definido no ponto 3.2.6)

», «CharacterString».

**3.1.6. Horizonte do solo (SoilHorizon)**

Domínio de um solo com uma certa extensão vertical, mais ou menos paralelo à superfície e homogéneo no que diz respeito à maior parte das características morfológicas e analíticas, desenvolvido numa camada de material de origem através de processos pedogénicos ou composto no local por resíduos orgânicos sedimentados de plantas de crescimento contínuo (turfa).

Este tipo é um subtipo de «ProfileElement».

Atributos do tipo de objeto geográfico «SoilHorizon»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| FAOHorizonNotation | Designação do horizonte do solo | FAOHorizonNotationType | voidable |
| otherHorizonNotation | Designação do horizonte do solo de acordo com um sistema de classificação específico. | OtherHorizonNotationType | voidable |

**3.1.7. Camada de solo (SoilLayer)**

Domínio de um solo com uma certa extensão vertical desenvolvido através de processos não pedogénicos, apresentando uma alteração na estrutura e/ou composição possivelmente para domínios adjacentes sobrejacentes ou subjacentes, ou um agrupamento de horizontes do solo ou de outros subdomínios com uma finalidade especial.

Este tipo é um subtipo de «ProfileElement».

Atributos do tipo de objeto geográfico «SoilLayer»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| layerType | Atribuição de uma camada de acordo com o conceito que corresponde à sua natureza. | LayerTypeValue |  |
| layerRockType | Tipo de material em que a camada se desenvolveu. | LithologyValue | voidable |
| layerGenesisProcess | Último processo não pedogénico (geológico ou antropogénico) que cunhou a composição do material e a estrutura interna da camada. | EventProcessValue | voidable |
| layerGenesisEnvironment | Contexto em que se verificou o último processo não pedogénico (geológico ou antropogénico) que cunhou a composição do material e a estrutura interna da camada. | EventEnvironmentValue | voidable |
| layerGenesisProcessState | Indicação se o processo especificado em «layerGenesisProcess» está em curso ou cessou no passado. | LayerGenesisProcessStateValue | voidable |

Restrições do tipo de objeto geográfico «SoilLayer»

Os atributos de «layerGenesisProcess», «layerGenesisEnvironment», «layerGenesisProcessState» e «layerRockType» só devem ser fornecidos se o «layerType» tiver o valor «geogénico».

**3.1.8. Parcela de solo (SoilPlot)**

Um local em que é efetuado um determinado estudo do solo.

Atributos do tipo de objeto geográfico «SoilPlot»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| soilPlotLocation | Referência a uma localização na terra; pode ser uma localização pontual identificada pelas coordenadas ou uma descrição da localização através de texto ou de um identificador. | Location |  |
| soilPlotType | Fornece informações sobre o tipo de parcela em que a observação do solo é efetuada. | SoilPlotTypeValue |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

Associações do tipo de objeto geográfico «SoilPlot»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| locatedOn | Ligação para o sítio de levantamento do solo onde está localizada a parcela de solo ou ao qual a parcela de solo pertence. | SoilSite | voidable |
| observedProfile | Ligação para o perfil de solo observado relativamente ao qual a parcela de solo fornece informações. | ObservedSoilProfile | voidable |

**3.1.9. Perfil do solo (SoilProfile)**

Uma descrição do solo que é caracterizada por uma sucessão vertical de elementos do perfil.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «SoilProfile»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| WRBSoilName | Identificação do perfil do solo. | WRBSoilNameType | voidable |
| otherSoilName | Identificação do perfil do solo de acordo com um sistema de classificação específico. | OtherSoilNameType | voidable |
| localIdentifier | Identificador único do perfil do solo dado pelo fornecedor do conjunto de dados. | CharacterString | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | Momento em que o fenómeno começou a existir no mundo real. | DateTime | voidable |
| validTo | Momento em que o fenómeno deixou de existir no mundo real. | DateTime | voidable |

Associações do tipo de objeto geográfico «SoilProfile»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| isDescribedBy | Elementos do perfil (camadas e/ou horizontes) que constituem o perfil do solo. | ProfileElement | voidable |
| soilProfileObservation | Observação de uma propriedade do solo para caracterizar o perfil do solo. | OM_Observation | voidable |

Restrições do tipo de objeto geográfico «SoilProfile»

Para preencher a propriedade «featureOfInterest» das observações do perfil do solo de um objeto «SoilProfile», deve ser utilizado esse mesmo objeto de «SoilProfile».

A «observedProperty» da observação do perfil do solo deve ser especificada utilizando um valor da lista de códigos «SoilProfileParameterNameValue».

O resultado da observação do perfil do solo deve ser de um dos seguintes tipos: «Number», «

RangeType (definido no ponto 3.2.6)

», «CharacterString».

**3.1.10. Sítio de levantamento do solo (SoilSite)**

Uma área no âmbito de um levantamento, estudo ou área monitorizada de maior dimensão em que é efetuada uma determinada investigação do solo.

Atributos do tipo de objeto geográfico «SoilSite»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| geometry | Geometria que define o sítio de levantamento do solo. | GM_Object |  |
| soilInvestigationPurpose | Indicação do motivo por que foi realizado o levantamento. | SoilInvestigationPurposeValue |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | Momento em que o fenómeno começou a existir no mundo real. | DateTime | voidable |
| validTo | Momento em que o fenómeno deixou de existir no mundo real. | DateTime | voidable |

Associações do tipo de objeto geográfico «SoilSite»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| isObservedOnLocation | Ligação para um ou mais locais em que o sítio de levantamento do solo foi investigado. | SoilPlot | voidable |
| soilSiteObservation | Observação de uma propriedade do solo para caracterizar o sítio de levantamento do solo. | OM_Observation | voidable |

Restrições do tipo de objeto geográfico «SoilSite»

Para preencher a propriedade «featureOfInterest» das observações do sítio de levantamento do solo de um objeto «SoilSite», deve ser utilizado esse mesmo objeto de «SoilSite».

A «observedProperty» da observação do sítio de levantamento do solo deve ser especificada utilizando um valor da lista de códigos «SoilSiteParameterNameValue».

O resultado da observação do sítio de levantamento do solo deve ser um dos seguintes tipos: «Number», «

RangeType (definido no ponto 3.2.6)

», «CharacterString».

O resultado da observação do sítio de levantamento do solo deve ser do tipo «SoilObservationResult».

**3.1.11. Cobertura do tema solo (SoilThemeCoverage)**

Um tipo de objeto geográfico que tem valores para uma propriedade baseados num ou mais parâmetros relacionados, e possivelmente não relacionados, com o solo dentro do seu domínio espacial, temporal ou espaciotemporal.

Este tipo é um subtipo de «RectifiedGridCoverage».

Atributos do tipo de objeto geográfico «SoilThemeCoverage»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime |  |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime |  |
| domainExtent | O atributo «domainExtent» deve conter a extensão do domínio espaciotemporal da cobertura. As extensões podem ser especificadas tanto no espaço como no tempo. | EX_Extent |  |
| validTimeFrom | «ValidTime» especifica a janela temporal relativamente à qual foram obtidas medições a fim de calcular a propriedade temática do solo relevante para esse período. O momento de início define o começo do período. | Date | voidable |
| validTimeTo | «ValidTime» especifica a janela temporal relativamente à qual foram obtidas medições a fim de calcular a propriedade temática do solo relevante para esse período. O momento de fim define o termo do período. | Date | voidable |
| soilThemeParameter | Propriedade relacionada com o solo (categoria temática «Solo») que é representada por esta cobertura. | SoilThemeParameterType |  |

Associações do tipo de objecto geográfico «SoilThemeCoverage»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| isDescribedBy | Esta associação permite a uma determinada «SoilThemeCoverage» ter uma «Coverage» relacionada que não tem significado sem a cobertura de base. | SoilThemeDescriptiveCoverage | voidable |

Restrições do tipo de objeto geográfico «SoilThemeCoverage»

Os valores de «rangeSet» devem ser de um dos seguintes tipos: «Number», «

RangeType (definido no ponto 3.2.6)

», «CharacterString».

**3.1.12. Cobertura descritiva do tema solo (SoilThemeDescriptiveCoverage)**

Um tipo de objeto geográfico que está associado à cobertura da categoria temática «Solo» e que tem informação adicional sobre os valores de uma propriedade da cobertura da categoria temática «Solo».

Este tipo é um subtipo de «RectifiedGridCoverage».

Atributos do tipo de objecto geográfico «SoilThemeDescriptiveCoverage»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime |  |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime |  |
| domainExtent | O atributo «domainExtent» deve conter a extensão do domínio espaciotemporal da cobertura. As extensões podem ser especificadas tanto no espaço como no tempo. | EX_Extent |  |
| soilThemeDescriptiveParameter | Propriedade descritiva para a propriedade relacionada com o solo (categoria temática «Solo») que é representada pela sua «SoilThemeCoverage» associada. | SoilThemeDescriptiveParameterType |  |

Associações do tipo de objeto geográfico «SoilThemeDescriptiveCoverage»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| isDescribing | Esta associação permite a uma determinada «SoilThemeCoverage» ter uma «Coverage» relacionada que não tem significado sem a cobertura de base. | SoilThemeCoverage |  |

Restrições do tipo de objeto geográfico «SoilThemeDescriptiveCoverage»

Os valores de «rangeSet» devem ser de um dos seguintes tipos: «Number», «

RangeType (definido no ponto 3.2.6)

», «CharacterString».

**3.2. Tipos de dados**

**3.2.1. Presença do perfil derivado na massa de solo (DerivedProfilePresenceInSoilBody)**

Tipo de dados que indica a gama de percentagens (expressas por um limite inferior e superior) ocupada pelo perfil derivado na massa de solo.

Este tipo é uma classe de associação.

Atributos do tipo de dados «DerivedProfilePresenceInSoilBody»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| derivedProfilePercentageRange | Intervalo que define as percentagens mínima e máxima da área da massa de solo representada por um perfil do solo derivado específico. | RangeType (definido no ponto 3.2.6) | voidable |

**3.2.2. Tipo de notação do horizonte FAO (FAOHorizonNotationType)**

Uma classificação de um horizonte de acordo com o sistema de classificação de horizontes especificado em Guidelines for soil description, 4th edition, Food and Agriculture Organization of the United Nations, Rome, 2006.

Atributos do tipo de dados «FAOHorizonNotationType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| FAOHorizonDiscontinuity | Número utilizado para indicar uma descontinuidade na notação do horizonte. | Integer |  |
| FAOHorizonMaster | Símbolo da parte principal da notação do horizonte. | FAOHorizonMasterValue |  |
| FAOPrime | Pode ser utilizada uma plica ou uma plica dupla para conotar o símbolo do horizonte principal de dois horizontes (plica) ou três horizontes (plica dupla) mais baixos que tenham prefixos idênticos em numerais árabes e combinações idênticas de carateres. | FAOPrimeValue |  |
| FAOHorizonSubordinate | As designações de características e distinções subordinadas no âmbito das camadas e horizontes principais baseiam-se em características do perfil observáveis no terreno e são aplicadas na descrição do solo no sítio. | FAOHorizonSubordinateValue |  |
| FAOHorizonVertical | Número de ordem da subdivisão vertical na notação do horizonte. | Integer |  |
| isOriginalClassification | Valor booleano para indicar se a notação de horizonte FAO foi a notação original utilizada para descrever o horizonte. | Boolean |  |

**3.2.3. Outro tipo de notação do horizonte (OtherHorizonNotationType)**

Uma classificação de um horizonte do solo de acordo com um sistema de classificação específico.

Atributos do tipo de dados «OtherHorizonNotationType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| horizonNotation | Notação que caracteriza o horizonte do solo de acordo com um sistema de classificação especificado. | OtherHorizonNotationTypeValue |  |
| isOriginalClassification | Valor booleano para indicar se o sistema de notação do horizonte especificado foi o sistema de notação original utilizado para descrever o horizonte. | Boolean |  |

**3.2.4. Outro tipo de nome do solo (OtherSoilNameType)**

Uma identificação do perfil do solo de acordo com um sistema de classificação específico.

Atributos do tipo de dados «OtherSoilNameType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| soilName | Nome do perfil do solo de acordo com um sistema de classificação específico. | OtherSoilNameTypeValue |  |
| isOriginalClassification | Valor booleano para indicar se o sistema de classificação especificado foi o sistema de classificação original utilizado para descrever o perfil. | Boolean |  |

**3.2.5. Tipo de fração granulométrica das partículas (ParticleSizeFractionType)**

Parte do solo que é composta por partículas de solo mineral com uma dimensão dentro da gama de dimensões especificada.

Atributos do tipo de dados «ParticleSizeFractionType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| fractionContent | Percentagem da fração definida. | Number |  |
| fractionParticleSizeRange | Limites superior e inferior da dimensão das partículas da fração definida (expressa em μm). | RangeType (definido no ponto 3.2.6) |  |

**3.2.6. Tipo de gama (RangeType)**

Um valor de gama definido por um limite superior e um limite inferior.

Atributos do tipo de dados «RangeType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| upperValue | Valor que define o limite superior de uma propriedade específica. | Real |  |
| lowerValue | Valor que define o limite inferior de uma propriedade específica. | Real |  |
| uom | Unidade de medida utilizada para exprimir os valores da gama. | UnitOfMeasure |  |

Restrições do tipo de dados «RangeType»

No mínimo, um dos valores não deve estar vazio.

**3.2.7. Tipo de parâmetro descritivo do tema solo (SoilThemeDescriptiveParameterType)**

Um tipo de dados que fornece uma propriedade descritiva para a propriedade relacionada com o solo (categoria temática «Solo») que é representado pela sua «SoilThemeCoverage» associada.

Atributos do tipo de dados «SoilThemeDescriptiveParameterType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| soilThemeDescriptiveParameterName | Nome do parâmetro para fornecer informação suplementar sobre os valores da «SoilThemeCoverage» relacionada. | CharacterString |  |
| uom | Unidade de medida que é utilizada para exprimir o «soilThemeDescriptiveParameter». | UnitOfMeasure |  |

**3.2.8. Tipo de parâmetro do tema solo (SoilThemeParameterType)**

Uma propriedade relacionada com o solo (categoria temática «Solo») que é representada por esta cobertura. É composta por um nome de parâmetro proveniente de uma lista de códigos de «SoilDerivedObjectParameterNameValue» e por uma Unidade de Medida utilizada para expressar esse parâmetro.

Atributos do tipo de dados «SoilThemeParameterType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| soilThemeParameterName | Nome do parâmetro representado pela «soilThemeCoverage». | SoilDerivedObjectParameterNameValue |  |
| uom | Unidade de medida que é utilizada para exprimir o «soilThemeParameter». | UnitOfMeasure |  |

**3.2.9. Tipo de grupo qualificador WRB (WRBQualifierGroupType)**

Um tipo de dados para definir o grupo de um qualificador e o ou os seus possíveis especificadores e o seu lugar e posição em relação à World Reference Base (WRB) Reference Soil Group (RSG) (Grupo de Solos de Referencia da Base Mundial de Referência) a que pertence de acordo com a World reference base for soil resources 2006, first update 2007, World Soil Resources Reports No. 103, Food and Agriculture Organization of the United Nations, Rome, 2007.

Atributos do tipo de dados «WRBQualifierGroupType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| qualifierPlace | Atributo para indicar a colocação do qualificador relativamente ao grupo de solos de referência (RSG) da WRB. A posição pode ser antes do RSG, ou seja, «prefixo» (prefix) ou depois do RSG, ou seja, «sufixo» (suffix). | WRBQualifierPlaceValue |  |
| qualifierPosition | Número para indicar a posição de um qualificador no que se refere ao grupo de solos de referência (RSG) da WRB a que pertence e no que diz respeito à sua colocação nessa (RSG), ou seja, como um prefixo ou sufixo. | Integer |  |
| WRBqualifier | Elemento do nome da WRB, segundo nível de classificação. | WRBQualifierValue |  |
| WRBspecifier | Código que indica o grau de expressão de um qualificador ou a gama de profundidades a que o qualificador se aplica. | WRBSpecifierValue |  |

**3.2.10. Tipo de nome de solo WRB (WRBSoilNameType)**

Uma identificação do perfil do solo de acordo com a World reference base for soil resources 2006, first update 2007, World Soil Resources Reports No. 103, Food and Agriculture Organization of the United Nations, Rome, 2007.

Atributos do tipo de dados «WRBSoilNameType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| WRBQualifierGroup | Grupo de um qualificador e o ou os seus possíveis especificadores e o seu lugar e posição relativamente ao «WRBReferenceSoilGroup» a que pertence. | WRBQualifierGroupType |  |
| WRBReferenceSoilGroup | Primeiro nível de classificação da Base Mundial de Referência para os Recursos do Solo. | WRBReferenceSoilGroupValue |  |
| isOriginalClassification | Valor booleano para indicar se o sistema de classificação WRB foi o sistema de classificação original utilizado para descrever o perfil do solo. | Boolean |  |

Associações do tipo de dados «WRBSoilNameType»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| over | Uma associação para indicar que na classificação WRB um perfil do solo cobre um outro solo desenvolvido, mais antigo. | WRBSoilNameType |  |

**3.3. Listas de códigos**

**3.3.1. Horizonte principal FAO (FAOHorizonMasterValue)**

Uma lista de códigos da parte principal da designação de horizonte.

**3.3.2. Horizonte subordinado FAO (FAOHorizonSubordinateValue)**

Uma lista de códigos de designações de características e distinções subordinadas dentro das camadas e horizontes principais que estão baseadas em características do perfil observáveis no terreno e são aplicadas na descrição do solo no sítio.

**3.3.3. Plica segundo a FAO (FAOPrimeValue)**

Pode ser utilizada uma plica ou uma plica dupla para conotar o símbolo de horizonte principal do mais baixo de dois horizontes (plica) ou de três horizontes (plica dupla) que tenham prefixos idênticos em numerais árabes e combinações idênticas de carateres.

**3.3.4. Outro tipo de notação do horizonte (OtherHorizonNotationTypeValue)**

Uma classificação de um horizonte do solo de acordo com um sistema de classificação específico.

**3.3.5. Outro tipo de nome do solo (OtherSoilNameTypeValue)**

Uma identificação do perfil do solo de acordo com um sistema de classificação específico.

**3.3.6. Estado do processo de génese de camadas (LayerGenesisProcessStateValue)**

Indica se o processo especificado no «layerGenesisProcess» está em curso ou cessou.

**3.3.7. Tipo de camada (LayerTypeValue)**

Uma classificação de uma camada de acordo com o conceito de adequação à finalidade.

**3.3.8. Nome do parâmetro do elemento do perfil (ProfileElementParameterNameValue)**

Propriedades que podem ser observadas para caracterizar o elemento do perfil.

**3.3.9. Nome do parâmetro do objeto derivado do solo (SoilDerivedObjectParameterNameValue)**

Propriedades relacionadas com o solo que podem ser derivadas a partir de dados do solo e de outros dados.

**3.3.10. Finalidade da investigação do solo (SoilInvestigationPurposeValue)**

Uma lista de códigos de valores possíveis indicando as razões para a realização de um levantamento.

**3.3.11. Tipo de parcela de solo (SoilPlotTypeValue)**

Uma lista de códigos de termos que especificam em que espécie de parcela é efetuada a observação do solo.

**3.3.12. Nome do parâmetro do perfil do solo (SoilProfileParameterNameValue)**

Propriedades que podem ser observadas para caracterizar o perfil do solo.

**3.3.13. Nome do parâmetro de sítio do solo (SoilSiteParameterNameValue)**

Propriedades que podem ser observadas para caracterizar o sítio de solo.

**3.3.14. Posição do qualificador WRB (WRBQualifierPlaceValue)**

Uma lista de códigos de valores que indicam a posição do qualificador relativamente ao grupo de solos de referência (RSG) da WRB. A posição pode ser antes do RSG, ou seja, «prefixo» (prefix), ou depois do RSG, ou seja, «sufixo» (suffix).

**3.3.15. Qualificadores WRB (WRBQualifierValue)**

Uma lista de códigos de possíveis qualificadores da Base Mundial de Referência para os Recursos do Solo.

**3.3.16. Grupo de solos de referência (RSG) da WRB (WRBReferenceSoilGroupValue)**

Uma lista de códigos de possíveis grupos de solos de referência (ou seja, primeiro nível da classificação da Base Mundial de Referência para os Recursos do Solo).

**3.3.17. Especificadores WRB (WRBSpecifierValue)**

Uma lista de códigos de possíveis especificadores.

**3.4. Requisitos específicos de categorias temáticas**

(1) Os valores das listas de códigos hierárquicas do primeiro nível «ProfileElementParameterNameValue», «SoilDerivedObjectParameterNameValue», «SoilProfileParameterNameValue», «SoilSiteParameterNameValue» («chemicalParameter», «biologicalParameter», «physicalParameter») têm apenas um objetivo de estruturação; devem ser utilizados apenas os valores de nível inferior.

(2) Quando é necessário um parâmetro descritivo adicional relativo ao objeto derivado do solo, deve ser utilizado o atributo do parâmetro do tipo de objeto geográfico «OM_Observation».

(3) Em cada conjunto de dados, deve apenas ser utilizada uma classificação do Outro Tipo de Notação do Horizonte.

(4) Em cada conjunto de dados, deve apenas ser utilizada uma classificação de Outro Tipo de Nome do Solo.

**3.5. Camadas**

**Camadas para a categoria temática de dados geográficos «Solo»**

<table> <tbody> <tr> <td>Nome da camada</td> <td>Título da camada</td> <td>Tipo de objeto geográfico</td> </tr> <tr> <td>SO.SoilBody</td> <td>Solos</td> <td>SoilBody</td> </tr> <tr> <td>SO.ObservedSoilProfile</td> <td>Perfis do solo observados</td> <td>ObservedSoilProfile, SoilPlot</td> </tr> <tr> <td>SO.SoilSite</td> <td>Sítios de levantamento do solo</td> <td>SoilSite</td> </tr> <tr> <td>SO. &lt;Valor de lista de códigos&gt; (1)</td> <td>&lt;nome legível para as pessoas&gt;</td> <td>SoilDerivedObject (basePhenomenon: SoilDerivedObjectParameterNameValue)</td> </tr> <tr> <td>Exemplo: SO. OrganicCarbonContent</td> <td>Exemplo: teor de carbono orgânico</td> <td></td> </tr> <tr> <td>SO.&lt;Valor de lista de códigos&gt;Coverage (2)</td> <td>&lt;nome legível para as pessoas&gt;</td> <td rowspan="2">SoilThemeCoverage (soilThemeParameter / soilThemeParameterName: SoilDerivedObjectParameterNameValue)</td> </tr> <tr> <td>Exemplo: SO. OrganicCarbonContentCoverage</td> <td>Exemplo: cobertura de teor de carbono orgânico</td> </tr> <tr> <td colspan="3">(1) Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3. (2) Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3.</td> </tr> </tbody> </table>

**4. USO DO SOLO (LAND USE)**

**4.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) «Uso do solo existente» (existing land use) : uma descrição objetiva do uso e funções de um território tal como tem sido e continua efetivamente ainda a ser na vida real.

(2) «Uso do solo existente em representação matricial» (gridded existing land use) : uma descrição objetiva sob a forma de uma quadrícula ortorretificada (imagem) regular do uso e funções de um território tal como tem sido e continua efetivamente ainda a ser na vida real.

(3) «Sistema hierárquico de classificação do uso do solo INSPIRE» (Hierarchical INSPIRE Land Use Classification System - HILUCS) : um sistema de classificação multiníveis aplicável ao Uso do Solo cuja utilização é obrigatória ao nível mais adequado.

(4) «Unidade mínima de interesse» (minimum unit of interest) : a área poligonal de menor dimensão para os objetos de uso do solo tomados em consideração no conjunto de dados.

(5) «Uso do solo planeado» (planned land use) : os planos de ordenamento do território, definidos pelas autoridades de ordenamento do território, que descrevem a possível utilização do solo no futuro.

(6) «Uso do solo existente por amostragem» (sampled existing land use) : uma descrição objetiva do uso e funções de um território [tal como tem sido e continua efetivamente ainda a ser] na vida real conforme observado num local que é objeto de amostragem.

(7) «Zonamento» (zoning) : uma partição em que é descrito o uso do solo planeado, tornando explícitos os direitos e proibições relativos a novas construções que são aplicáveis dentro de cada elemento da partição.

**4.2. Estrutura da categoria temática de dados geográficos «Uso do Solo»**

Os tipos especificados para a categoria temática de dados geográficos «Uso do Solo» estão estruturados nos seguintes pacotes:

— Nomenclatura de ocupação do solo (Land Cover Nomenclature)

— Uso do solo existente (Existing land use)

— Uso do solo existente em representação matricial (Gridded existing land use)

— Uso do solo existente objeto por amostragem (Sampled existing land use)

— Uso do solo planeado (Planned land use)

**4.3. Nomenclatura de ocupação do solo**

**4.3.1. Tipos de dados**

4.3.1.1. Percentagem HILUCS (HILUCSPercentage)

Percentagem do objeto de uso do solo que é coberto por esta presença de valores HILUCS.

Atributos do tipo de dados «HILUCSPercentage»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| hilucsValue | Categoria HILUCS para esta percentagem HILUCS. | HILUCSValue |  |
| percentage | Percentagem do objeto de uso do solo que é coberto por esta presença de valores HILUCS. | Integer |  |

4.3.1.2. Presença do HILUCS (HILUCSPresence)

Presença de um ou vários valores HILUCS numa área, indicada quer como a percentagem coberta para cada valor quer como os valores enumerados pela sua ordem de importância.

Este tipo é um tipo de união.

Atributos do tipo de união «HILUCSPresence»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| orderedList | lista ordenada da presença de valor do uso do solo | HILUCSValue |  |
| percentageList | lista da percentagem do valor de uso do solo | HILUCSPercentage |  |

4.3.1.3. Percentagem específica (SpecificPercentage)

Percentagem de um objeto de uso do solo que é coberto por uma presença específica.

Atributos do tipo de dados «SpecificPercentage»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| specificValue | Categoria de valor específico para esta percentagem específica. | LandUseClassificationValue |  |
| percentage | Percentagem do objeto de uso do solo que é coberto por esta presença específica. | Integer |  |

4.3.1.4. Presença específica (SpecificPresence)

Presença de um ou vários valores de classificação do uso do solo numa área, de acordo com a lista de códigos fornecida pelo fornecedor de dados, indicada quer como a percentagem coberta para cada valor quer como os valores enumerados pela sua ordem de importância.

Este tipo é um tipo de união.

Atributos do tipo de união «SpecificPresence»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| orderedList | lista ordenada do valor do uso do solo | LandUseClassificationValue |  |
| percentageList | lista de percentagem do valor de uso do solo | SpecificPercentage |  |

**4.3.2. Listas de códigos**

4.3.2.1. HILUCS (HILUCSValue)

Lista de categorias de uso do solo a utilizar na categoria temática «Uso do Solo» INSPIRE.

4.3.2.2. Classificação do uso do solo (LandUseClassificationValue)

Lista de categorias de uso do solo a utilizar na categoria temática «Uso do Solo» INSPIRE e acordada a nível nacional ou local.

**4.4. Uso do solo existente**

**4.4.1. Tipos de objetos geográficos**

O pacote «Uso do Solo Existente» contém os seguintes tipos de objetos geográficos:

— Conjunto de dados de uso do solo existente

— Objeto de uso do solo existente

4.4.1.1. Conjunto de dados de uso do solo existente (ExistingLandUseDataSet)

Um conjunto de dados de uso do solo existente é uma coleção de áreas relativamente às quais são fornecidas informações sobre os usos do solo existentes (presentes ou passados).

Atributos do tipo de objeto geográfico «ExistingLandUseDataSet»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| extent | Fronteira da união geométrica de todas as instâncias do tipo de objeto geográfico «typeExistingLandUseObject». | GM_MultiSurface |  |
| name | Nome do conjunto de dados legível para as pessoas. | CharacterString |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | O momento em que o conjunto de dados de uso do solo existente começou a existir no mundo real. | DateTime | voidable |
| validTo | O momento em que o conjunto de dados de uso do solo existente deixou de existir no mundo real. | DateTime | voidable |

Associações do tipo de objeto geográfico «ExistingLandUseDataSet»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| member | Referência aos «LandUseObjects» que pertencem a este «ExistingLandUseDataSet» | ExistingLandUseObject |  |

4.4.1.2. Objeto de uso do solo existente (ExistingLandUseObject)

Um objeto de uso do solo existente descreve o uso do solo de uma área que tem uma combinação homogénea de tipos de uso do solo.

Atributos do tipo de objeto geográfico «ExistingLandUseObject»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| geometry | Representação geométrica da área geográfica abrangida por esse objeto. | GM_MultiSurface |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| hilucsPresence | Presença efetiva de uma categoria de uso do solo de acordo com o sistema HILUCS dentro do objeto. | HILUCSPresence | voidable |
| hilucsLandUse | Classes de uso do solo HILUCS que estão presentes neste objeto de uso do solo existente. | HILUCSValue |  |
| specificLandUse | Categoria de uso do solo de acordo com a nomenclatura específica para este conjunto de dados. | LandUseClassificationValue | voidable |
| specificPresence | Presença efetiva de uma categoria de uso do solo dentro do objeto. | SpecificPresence | voidable |
| observationDate | A data de observação associada a uma descrição. | Date | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | O momento em que o fenómeno começou a existir no mundo real. | DateTime | voidable |
| validTo | O momento em que o fenómeno deixou de existir no mundo real. | DateTime | voidable |

Associações do tipo de objeto geográfico «ExistingLandUseObject»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| dataSet | Conjunto de dados de uso do solo existente ao qual pertence este objeto de uso do solo. | ExistingLandUseDataSet |  |

**4.5. Uso do solo de representação matricial**

**4.5.1. Tipos de objetos geográficos**

O pacote «Uso do Solo de Representação Matricial» contém o tipo de objeto geográfico Quadrícula de Uso do Solo Existente.

4.5.1.1. Quadrícula de uso do solo existente (ExistingLandUseGrid)

Uma quadrícula de uso do solo existente é uma coleção de pixels relativamente à qual são fornecidas informações sobre o uso do solo existente (presente ou passado). O sistema HILUCS deve ser utilizado para fins de classificação.

Este tipo é um subtipo de «RectifiedGridCoverage».

Atributos do tipo de objeto geográfico «ExistingLandUseGrid»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| name | Nome do conjunto de dados legível para as pessoas. | CharacterString |  |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| extent | Contém a extensão do conjunto de dados. | EX_Extent |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | Primeira data em que esta quadrícula é uma representação válida da realidade. | DateTime | voidable |
| validTo | Data a partir da qual a quadrícula já não é uma representação válida da realidade. | DateTime | voidable |

Restrições do tipo de objeto geográfico «ExistingLandUseGrid»

Os valores «rangeSet» devem ser do tipo «CategoryOrNilReason».

A gama baseia-se quer no sistema HILUCS quer num sistema específico de classificação do uso do solo definido pelo fornecedor de dados.

**4.6. Uso do solo por amostragem**

**4.6.1. Tipos de objetos geográficos**

O pacote «Uso do Solo por Amostragem» contém os seguintes tipos de objetos geográficos:

— Amostra do uso do solo existente

— Conjunto de dados de uso do solo existente por amostragem

4.6.1.1. Amostra do uso do solo existente (ExistingLandUseSample)

Descrição do uso do solo existente presente num determinado local.

Atributos do tipo de objeto geográfico «ExistingLandUseSample»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| location | Local em que a amostra do uso do solo é recolhida. | GM_Point |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| hilucsLandUse | Classes de uso do solo HILUCS presentes nesta amostra de uso do solo existente. | HILUCSValue |  |
| hilucsPresence | Presença efetiva de uma categoria de uso do solo de acordo com o sistema HILUCS dentro do objeto. | HILUCSPresence | voidable |
| specificLandUse | Categoria de uso do solo de acordo com a nomenclatura específica para este conjunto de dados. | LandUseClassificationValue | voidable |
| observationDate | Data de observação associada a uma descrição. | Date | voidable |
| specificPresence | Presença efetiva de uma categoria de uso do solo dentro do objeto. | SpecificPresence | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | O momento em que o fenómeno começou a existir no mundo real. | DateTime | voidable |
| validTo | O momento em que o fenómeno deixou de existir no mundo real. | DateTime | voidable |

Associações do tipo de objeto geográfico «ExistingLandUseSample»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| dataset | Conjunto de dados ao qual pertence esta amostra. | SampledExistingLandUseDataSet |  |

4.6.1.2. Conjunto de dados de uso do solo existente por amostragem (SampledExistingLandUseDataSet)

Um conjunto de dados de uso do solo existente por amostragem é uma coleção de locais relativamente aos quais são fornecidas informações sobre os usos do solo existentes (presentes ou passados).

Atributos do tipo de objeto geográfico «SampledExistingLandUseDataSet»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| extent | Envolvente convexa de todas as instâncias do tipo de objeto geográfico «ExistingLandUseSample». | GM_MultiSurface |  |
| name | Nome do conjunto de dados legível para as pessoas. | CharacterString |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | Primeira data em que este conjunto de dados é válido na realidade. | DateTime | voidable |
| validTo | O momento em que o conjunto de dados deixou de existir no mundo real. | DateTime | voidable |

Associações do tipo de objeto geográfico «SampledExistingLandUseDataSet»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| member | Referência aos membros do conjunto de dados de uso do solo existente por amostragem. | ExistingLandUseSample |  |

**4.7. Uso do solo planeado**

**4.7.1. Tipos de objetos geográficos**

O pacote «Uso do Solo Planeado» contém os seguintes tipos de objetos geográficos:

— Documentação oficial

— Plano de ordenamento do território

— Regulamentação suplementar

— Elemento de zonamento

4.7.1.1. Documentação oficial (OfficialDocumentation)

A documentação oficial que compõe o plano de ordenamento do território; pode ser composta pela legislação e regulamentação aplicáveis, elementos cartográficos e elementos descritivos que podem estar associados ao plano de ordenamento do território completo, a um elemento de zonamento ou a regulamentação suplementar. Em alguns Estados-Membros a regulamentação textual em si mesma fará parte do conjunto de dados (e pode ser integrada no atributo de texto de regulamentação), noutros Estados-Membros o texto não fará parte do conjunto de dados e será referenciado através da referência a um documento ou ato jurídico. Deve ser fornecido, pelo menos, um dos três valores «voidable» (potencialmente vazios).

Atributos do tipo de objeto geográfico «OfficialDocumentation»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| legislationCitation | Referência ao documento que contém o texto da regulamentação. | LegislationCitation | voidable |
| regulationText | Texto da regulamentação. | CharacterString | voidable |
| planDocument | Citação dos planos e desenhos estruturais digitalizados, que podem ou não estar georreferenciados. | DocumentCitation | voidable |

Restrições do tipo de objeto geográfico «OfficialDocumentation»

Deve ser fornecido, no mínimo, um dos atributos «legislationCitation», «regulationText» ou «planDocument» com um valor não vazio («non-void»).

4.7.1.2. Plano de ordenamento do território (SpatialPlan)

Um conjunto de documentos que indica uma orientação estratégica para o desenvolvimento de uma determinada área geográfica, estabelece as políticas, prioridades, programas e atribuição de solos que implementarão a orientação estratégica e que influencia a distribuição de pessoas e atividades em espaços a várias escalas. Podem ser desenvolvidos planos de ordenamento do território para planeamento urbano, planeamento regional, planeamento ambiental, planeamento paisagístico, planos de ordenamento do território nacionais ou planos de ordenamento do território a nível da União.

Atributos do tipo de objeto geográfico «SpatialPlan»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| extent | União geométrica de todas as instâncias do tipo de objeto geográfico «typesZoningElement» e «SupplementaryRegulation». Quando um «SpatialPlan» é composto por apenas um documento, o atributo «extent» é a fronteira da imagem cartográfica que contém a informação sobre o uso do solo (ou seja, a extensão do mapa do uso do solo). | GM_MultiSurface |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| officialTitle | Título oficial do plano de ordenamento do território. | CharacterString |  |
| levelOfSpatialPlan | Nível das unidades administrativas abrangidas pelo plano. | LevelOfSpatialPlanValue |  |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | Primeira data em que este plano de ordenamento do território é válido na realidade. | DateTime | voidable |
| validTo | O momento em que o plano de ordenamento do território deixou de existir no mundo real. | DateTime | voidable |
| alternativeTitle | Título alternativo (não oficial) do plano de ordenamento do território. | CharacterString | voidable |
| planTypeName | Nome de tipo de plano que o Estado-Membro deu ao plano. | PlanTypeNameValue |  |
| processStepGeneral | Indicação geral da etapa do processo de planeamento em que o plano se encontra. | ProcessStepGeneralValue | voidable |
| backgroundMap | Identificação do mapa de base que foi utilizado para a realização deste plano. | BackgroundMapValue | voidable |
| ordinance | Referência à portaria administrativa relevante. | OrdinanceValue | voidable |

Associações do tipo de objeto geográfico «SpatialPlan»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| officialDocument | Ligação aos documentos oficiais que estão relacionados com o plano de ordenamento do território. | OfficialDocumentation | voidable |
| member | Referência aos «ZoningElements» que pertencem a este «SpatialPlan» | ZoningElement |  |
| restriction | Ligações a regulamentação suplementar que estabelece informação e/ou limitação sobre o uso do solo/água que suplementa o zonamento como parte deste plano de ordenamento do território. | SupplementaryRegulation |  |

4.7.1.3. Regulamentação suplementar (SupplementaryRegulation)

Um objeto geográfico (ponto, linha ou polígono) de um plano de ordenamento do território que estabelece informação suplementar e/ou limitação sobre o uso do solo/água, necessário por questões de ordenamento do território ou para formalizar regras externas definidas num texto jurídico.

Atributos do tipo de objeto geográfico «SupplementaryRegulation»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| geometry | Geometria do terreno a que a regulamentação suplementar é aplicável. | GM_Object |  |
| validFrom | Primeira data em que esta versão desta regulamentação suplementar é válida na realidade. | DateTime | voidable |
| validTo | Data em que a regulamentação suplementar deixa de ser válida. | DateTime | voidable |
| regulationNature | Natureza jurídica da regulamentação sobre o uso do solo. | RegulationNatureValue |  |
| specificSupplementaryRegulation | Referência a uma categoria de regulamentação suplementar fornecida numa nomenclatura específica de regulamentações suplementares fornecida pelo fornecedor de dados. | SpecificSupplementaryRegulationValue | voidable |
| supplementaryRegulation | Código da regulamentação suplementar constante da lista hierárquica de códigos de regulamentações suplementares acordada a nível europeu. | SupplementaryRegulationValue |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| processStepGeneral | Indicação geral da etapa do processo de planeamento em que se encontra a regulamentação suplementar. | ProcessStepGeneralValue | voidable |
| backgroundMap | Identificação do mapa de base que foi utilizado para a elaboração da regulamentação suplementar. | BackgroundMapValue | voidable |
| dimensioningIndication | Especificações sobre o dimensionamento que são aditadas ao dimensionamento dos elementos de zonamento que coincidem com a geometria da regulamentação suplementar. | DimensioningIndicationValue | voidable |
| inheritedFromOtherPlans | Indicação se a regulamentação suplementar é herdada de outro plano de ordenamento do território. | Boolean | voidable |
| specificRegulationNature | Natureza jurídica da regulamentação sobre o uso do solo numa perspetiva nacional. | CharacterString | voidable |
| name | Nome oficial da regulamentação suplementar | CharacterString | voidable |

Associações do tipo de objeto geográfico «SupplementaryRegulation»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| officialDocument | Ligação para os regulamentos textuais que correspondem a esta regulamentação suplementar. | OfficialDocumentation | voidable |
| plan | Ligação para o plano de que faz parte esta regulamentação suplementar. | SpatialPlan |  |

4.7.1.4. Elemento de zonamento (ZoningElement)

Um objeto geográfico que é homogéneo no que diz respeito aos usos do solo autorizados com base no zonamento que separa um conjunto de usos do solo de outro conjunto.

Atributos do tipo de objeto geográfico «ZoningElement»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| geometry | Geometria deste elemento de zonamento. | GM_MultiSurface |  |
| validFrom | Data em que o fenómeno começou a existir no mundo real. | DateTime | voidable |
| validTo | Data em que o fenómeno deixou de existir no mundo real. | DateTime | voidable |
| hilucsLandUse | Classe de uso do solo HILUCS que é predominante neste objeto de uso do solo. | HILUCSValue |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| hilucsPresence | Presença efetiva de uma categoria de uso do solo dentro do objeto. | HILUCSPresence | voidable |
| specificLandUse | Categoria de uso do solo de acordo com a nomenclatura específica para este conjunto de dados. | LandUseClassificationValue | voidable |
| specificPresence | Presença efetiva de uma categoria de uso do solo dentro do objeto. | SpecificPresence | voidable |
| regulationNature | Natureza jurídica da indicação de uso do solo. | RegulationNatureValue |  |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| processStepGeneral | Indicação geral da etapa do processo de planeamento em que se encontra o elemento de zonamento. | ProcessStepGeneralValue | voidable |
| backgroundMap | Identificação do mapa de base que foi utilizado para a elaboração deste elemento de zonamento. | BackgroundMapValue | voidable |
| dimensioningIndication | Especificações sobre o dimensionamento do desenvolvimento urbano. | DimensioningIndicationValue | voidable |

Associações do tipo de objeto geográfico «ZoningElement»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| plan | «SpatialPlan» a que pertence este «ZoningElement». | SpatialPlan |  |
| officialDocument | Regulamentação textual que faz parte deste elemento de zonamento. | OfficialDocumentation | voidable |

**4.7.2. Tipos de dados**

4.7.2.1. Mapa de base (BackgroundMapValue)

Informação sobre o mapa que tem sido utilizado como base na definição de um plano de ordenamento do território, de um elemento de zonamento ou de uma regulamentação suplementar.

Atributos do tipo de dados «BackgroundMapValue»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| backgroundMapDate | Data do mapa de base utilizado. | DateTime |  |
| backgroundMapReference | Referência ao mapa de base utilizado. | CharacterString |  |
| backgroundMapURI | URI que referencia o serviço que fornece o mapa de base. | URI | voidable |

4.7.2.2. Indicação do dimensionamento do caráter aferido (DimensioningIndicationCharacterValue)

Indicação do dimensionamento cujo valor é do tipo «CharacterString».

Este tipo é um subtipo de «DimensioningIndicationValue».

Atributos do tipo de dados «DimensioningIndicationCharacterValue»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| value | Valor das indicações da dimensão. | CharacterString |  |

4.7.2.3. Indicação do dimensionamento aferido por números inteiros (DimensioningIndicationIntegerValue)

Indicação do dimensionamento cujo valor é do tipo número inteiro («integer»).

Este tipo é um subtipo de «DimensioningIndicationValue».

Atributos do tipo de dados «DimensioningIndicationIntegerValue»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| value | Valor das indicações da dimensão. | Integer |  |

4.7.2.4. Indicação do dimensionamento aferido por medição (DimensioningIndicationMeasureValue)

Indicação do dimensionamento cujo valor é uma medição.

Este tipo é um subtipo de «DimensioningIndicationValue».

Atributos do tipo de dados «DimensioningIndicationMeasureValue»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| value | Valor das indicações da dimensão. | Measure |  |

4.7.2.5. Indicação do dimensionamento aferido pelo valor real (DimensioningIndicationRealValue)

Indicação do dimensionamento cujo valor é um número de vírgula flutuante.

Este tipo é um subtipo de «DimensioningIndicationValue».

Atributos do tipo de dados «DimensioningIndicationRealValue»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| value | Valor das indicações da dimensão. | Real |  |

4.7.2.6. Indicação do dimensionamento (DimensioningIndicationValue)

Especificações sobre o dimensionamento do desenvolvimento urbano.

Atributos do tipo de dados «DimensioningIndicationValue»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| indicationReference | Descrição da indicação da dimensão. | CharacterString |  |

4.7.2.7. Portaria (OrdinanceValue)

Referência à portaria administrativa. Portaria é um regulamento/regra que é adotado por uma autoridade que está legalmente habilitada para adotar tais portarias.

Atributos do tipo de dados «OrdinanceValue»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| ordinanceDate | Data da portaria administrativa relevante. | DateTime |  |
| ordinanceReference | Referência à portaria administrativa relevante. | CharacterString |  |

**4.7.3. Listas de códigos**

4.7.3.1. Nível do plano de ordenamento do território (LevelOfSpatialPlanValue)

Hierarquia territorial do plano.

4.7.3.2. Fase do processo geral (ProcessStepGeneralValue)

Indicação geral da fase do processo de planeamento em que o plano se encontra.

4.7.3.3. Natureza da regulamentação (RegulationNatureValue)

Natureza jurídica da indicação de uso do solo.

4.7.3.4. Nome do tipo de plano (PlanTypeNameValue)

Tipos de planos definidos nos Estados-Membros.

4.7.3.5. Regulamentação suplementar específica (SpecificSupplementaryRegulationValue)

Categoria de regulamentação suplementar fornecida numa nomenclatura específica de regulamentações suplementares fornecida pelo fornecedor de dados.

4.7.3.6. Regulamentação suplementar (SupplementaryRegulationValue)

Tipos de condições e restrições nos planos de ordenamento do território.

**4.8. Requisitos específicos de categorias temáticas**

(1) Os conjuntos de dados de Uso do Solo devem atribuir a cada polígono, pixel ou localização um tipo de uso do solo baseado no Sistema Hierárquico de Classificação do Uso do Solo INSPIRE (HILUCS) ao nível mais adequado e detalhado da hierarquia.

(2) O tipo de objeto geográfico «CoverageByDomainAndRange» só pode ser dos subtipos de «GridCoverage».

(3) Nos casos em que tenha sido estabelecida uma zona para regulamentar o uso do solo planeado e definida no âmbito de um plano de ordenamento do território juridicamente vinculativo, essa zona fica abrangida pela categoria temática «Uso do Solo» e deve ser codificada como «SupplementaryRegulation». No entanto, se a zona tiver sido estabelecida por via legislativa mas não tiver sido definida no âmbito de um plano de ordenamento do território juridicamente vinculativo, então a zona deve ser codificada como uma «ManagementRestrictionOrRegulationZone».

(4) Com base no sistema de referência de coordenadas horizontais INSPIRE, cada Estado-Membro deve definir uma projeção ou um conjunto de projeções adequado para trabalhar com as parcelas cadastrais subjacentes no território nacional e nas áreas transfronteiras quando aplicável a um «SpatialPlan». Uma projeção é adequada se apresentar poucas alterações lineares (idealmente menos de 50 cm por 500 m) e permitir assim aos utilizadores medir distâncias e superfícies de uma forma com significado. Esta projeção ou conjunto de projeções tem de ser definida/o em acordo com os países vizinhos. Esta projeção ou conjunto de projeções deve ser bem documentada/o a fim de permitir a conversão de e para o Sistema de Coordenadas de Referência comum. A documentação deve ser fornecida de acordo com a norma ISO 19111, que estabelece como deve ser descrito um sistema de referência de coordenadas projetado.

(5) A utilização do elemento de metadados comum «Resolução Espacial» (Spatial Resolution) (de acordo com a parte B, ponto 6.2, do anexo ao Regulamento (CE) n.º 1205/2008) deve limitar-se à apresentação de uma distância de resolução.

(6) Os fornecedores de dados devem incluir as seguintes palavras-chave para além das palavras-chave obrigatórias definidas no Regulamento (CE) n.º 1205/2008/CE:

(a) Uma das seguintes palavras-chave linguisticamente neutras para descrever o tipo de conjunto de dados de uso do solo: «ExistingLandUse», «SampledExistingLandUse», «GriddedExistingLandUse», «PlannedLandUse».

(b) Se o conjunto de dados contém objetos do «SpatialPlan», uma palavra-chave que descreva o nível das unidades administrativas abrangidas pelo plano, conforme definido na lista de códigos «LevelOfSpatialPlan».

**4.9. Camadas**

**Camadas para a categoria temática de dados geográficos «Uso do Solo»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| LU.ExistingLandUse | Objetos de Uso do Solo Existente, de acordo com o Sistema Hierárquico de Classificação de Uso do Solo INSPIRE ao nível mais adequado. | ExistingLandUseObject |
| LU.SpatialPlan | Extensão de um plano de ordenamento do território. | SpatialPlan |
| LU.ZoningElement | Objetos de Zonamento do plano de ordenamento do território, de acordo com o Sistema Hierárquico de Classificação do Uso do Solo INSPIRE ao nível mais adequado. | ZoningElement |
| LU.SupplementaryRegulation | Regulamentações que suplementam o zonamento e que afetam o uso do solo | SupplementaryRegulation |

**5. SAÚDE HUMANA E SEGURANÇA (HUMAN HEALTH AND SAFETY)**

**5.1. Tipos de objetos geográficos**

São especificados os seguintes tipos de objetos geográficos para a categoria temática de dados geográficos «Saúde Humana e Segurança»:

— Dados estatísticos sobre saúde

— Biomarcador

— Doença

— Estatísticas de saúde geral

— Estatísticas de serviços de saúde

— Medida ambiental determinante da saúde

— Dados estatísticos ambientais determinantes da saúde

**5.1.1. Dados estatísticos sobre saúde (HealthStatisticalData)**

Dados relacionados com a saúde humana, desde doenças e problemas relacionados com a saúde (de acordo com listas de códigos internacionalmente aceites, como a ICD-10), expressos sob a forma de morbilidade ou mortalidade, até dados sobre o estado geral de saúde (BMI, autoperceção do estado de saúde, etc.), dados sobre os serviços de cuidados de saúde (despesas com cuidados de saúde, doentes em ambulatório, etc.) e dados sobre biomarcadores. Estes são índices estatísticos agregados em diferentes unidades estatísticas, recolhidos/comunicados em diferentes grupos da população. A inclusão de dados de biomonitorização humana proporciona uma oportunidade para explorar ligações potenciais, diretas ou indiretas, entre a saúde humana e o ambiente.

Este tipo é abstrato.

Associações do tipo de objeto geográfico «HealthStatisticalData»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| aggregationUnit | Unidade estatística a que os dados estatísticos de saúde se referem. | StatisticalUnit |  |

**5.1.2. Biomarcador (Biomarker)**

Um biomarcador (de exposição) é a concentração de uma substância química, seu metabolito ou produto de uma interação entre uma substância química e uma molécula-alvo ou célula-alvo que é medida num sistema de um organismo.

Este tipo é um subtipo de «HealthStatisticalData».

Atributos do tipo de objeto geográfico «Biomarker»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| biomarkerName | É o identificador único de um biomarcador, que fornece informações sobre a substância química que é determinada e a matriz em que a substância química foi determinada. | BiomarkerType |  |
| biomarkerStatisticalParameter | O resumo estatístico de um estudo de biomonitorização humana que representa as características estatísticas mais importantes de um biomarcador medidas nesse estudo específico. | BiomarkerStatisticalParameterType |  |
| referencePeriod | Período de tempo a que se referem os dados. | ReferencePeriodType |  |
| ageRange | Intervalo etário de uma subpopulação específica, expresso como uma idade de início e um intervalo, ambos alternativamente expressos em anos, meses ou semanas. | AgeRangeType |  |
| gender | Sexo da população considerada. | GenderValue |  |

Associações do tipo de objeto geográfico «Biomarker»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| refersTo | Dados de biomarcadores descritos por metadados | BiomarkerThematicMetadata |  |

**5.1.3. Doença (Disease)**

Informações estatísticas relacionadas com patologias ligadas direta ou indiretamente à qualidade do ambiente.

Este tipo é um subtipo de «HealthStatisticalData».

Atributos do tipo de objeto geográfico «Disease»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| ageRange | Intervalo etário de uma subpopulação específica, expresso como uma idade de início e um intervalo, ambos alternativamente expressos em anos, meses ou semanas. | AgeRangeType | voidable |
| diseaseMeasure | Diferentes formas possíveis de comunicação de dados sobre doenças e problemas de saúde conexos. | DiseaseMeasure |  |
| gender | Sexo da população considerada. | GenderValue | voidable |
| referencePeriod | Período de tempo a que se referem os dados. | ReferencePeriodType |  |
| pathology | Tipo de patologias. | ICDValue |  |
| COD | Os dados sobre as causas da morte (causes of death - COD) que fornecem informações sobre os padrões de mortalidade e constituem um elemento importante da informação sobre saúde pública. | CODValue |  |

Restrições do tipo de objeto geográfico «Disease»

O atributo COD deve ser preenchido apenas se o atributo «diseaseMeasureType» tiver um valor que representa a mortalidade.

Pelo menos um dos atributos de patologia e COD não devem estar vazios.

**5.1.4. Estatísticas de saúde geral (GeneralHealthStatistics)**

Números sobre alguns aspetos da saúde relacionados com uma população ou uma área. Para efeitos deste modelo de dados, os dados sobre «saúde geral» incluem questões como autoperceção do estado de saúde, distribuição demográfica de vários problemas de saúde, fumadores, etc., expressos em números brutos, taxas, percentagens, estratificação por sexo, idade e/ou fatores socioeconómicos, culturais, étnicos ou outros.

Este tipo é um subtipo de «HealthStatisticalData».

Atributos do tipo de objeto geográfico «GeneralHealthStatistics»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| ageRange | Intervalo etário de uma subpopulação específica, expresso como uma idade de início e um intervalo, ambos alternativamente expressos em anos, meses ou semanas. | AgeRangeType | voidable |
| gender | Sexo da população considerada. | GenderValue | voidable |
| generalHealthName | Indicador do estado de saúde. | GeneralHealthTypeValue |  |
| generalHealthValue | Expressão numérica de um índice/indicador de saúde. | Real |  |
| referencePeriod | Período de tempo a que se referem os dados. | ReferencePeriodType |  |

**5.1.5. Estatísticas de serviços de saúde (HealthServicesStatistic)**

Dados estatísticos de serviços/cuidados de saúde ao nível NUTS 1 e 2 e de municípios.

Este tipo é um subtipo de «HealthStatisticalData».

Atributos do tipo de objeto geográfico «HealthServicesStatistic»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| healthServiceType | Tipo de serviços de saúde. | HealthServicesTypeValue |  |
| healthServiceValue | Número do tipo considerado. | Real |  |
| referencePeriod | Período de tempo a que se referem os dados. | ReferencePeriodType |  |

**5.1.6. Medida ambiental determinante da saúde (EnvHealthDeterminantMeasure)**

Uma medição bruta efetuada num local que seja de interesse para a análise de determinantes da saúde humana.

Atributos do tipo de objeto geográfico «EnvHealthDeterminantMeasure»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| location | Localização da medição. | GM_Object |  |
| type | Tipo de determinante ambiental da saúde. | EnvHealthDeterminantTypeValue |  |
| measureTime | Período em que a medição foi efetuada. | TM_Period |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | Momento em que a informação começará a ser utilizada. | DateTime | voidable |
| validTo | Momento em que a informação deixará de ser utilizada. | DateTime | voidable |
| measure | Medição do determinante ambiental da saúde. | Measure |  |
| category | Categoria da medição do determinante ambiental da saúde. | MeasureCategoryTypeValue |  |

Restrições do tipo de objeto geográfico «EnvHealthDeterminantMeasure»

A medição do determinante ambiental da saúde deve ser fornecida como medida (atributo «measure») ou como categoria de medição (atributo «category»).

**5.1.6-A Medição «ruído» de determinantes ambientais da saúde (EnvHealthDeterminantNoiseMeasure)**

Uma medição de ruído com interesse para a análise dos determinantes da saúde humana.

Este tipo é um subtipo de «EnvHealthDeterminantMeasure».

**Atributos do tipo de objeto geográfico «EnvHealthDeterminantNoiseMeasure»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| source | Tipo de fonte de ruído. | NoiseSourceTypeValue |  |

**5.1.6-B Medição «concentração» de determinantes ambientais da saúde (EnvHealthDeterminantConcentrationMeasure)**

Uma medição de concentração com interesse para a análise dos determinantes da saúde humana.

Este tipo é um subtipo de «EnvHealthDeterminantMeasure».

**Atributos do tipo de objeto geográfico «EnvHealthDeterminantConcentrationMeasure»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| component | O componente cuja concentração é medida. | ComponentTypeValue |  |
| Media | O meio no qual a concentração é medida. | MediaTypeValue |  |

**5.1.7. Dados estatísticos de determinantes ambientais da saúde (EnvHealthDeterminantStatisticalData)**

Um dado estatístico de interesse para a análise de determinantes da saúde humana, resultante da agregação de medições brutas localizadas no interior de uma unidade estatística.

Este tipo é um subtipo de «HealthStatisticalData».

Atributos do tipo de objeto geográfico «EnvHealthDeterminantStatisticalData»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| statisticalMethod | Tipo de método estatístico utilizado para agregar os dados das medições brutas na unidade estatística. | StatisticalAggregationMethodValue |  |
| type | Tipo de determinante ambiental da saúde. | EnvHealthDeterminantTypeValue |  |

Associações do tipo de objeto geográfico «EnvHealthDeterminantStatisticalData»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| measure | As medições | Measure |  |

**5.2. Tipos de dados**

**5.2.1. Idade (Age)**

A idade das pessoas pode ser expressa de várias formas (por exemplo, anos em relação a adultos, meses ou semanas em relação a bebés e crianças).

Este tipo é um tipo de união.

Atributos do tipo de união «Age»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| month | Período de tempo. | Integer |  |
| week | Período de tempo. | Integer |  |
| year | Período de tempo. | Integer |  |

**5.2.2. Faixa etária (AgeRangeType)**

Intervalo etário de uma subpopulação específica, expresso como uma idade de início e um intervalo, ambos alternativamente expressos em anos, meses ou semanas.

Atributos do tipo de dados «OthAgeRangeType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| startAge | Início do intervalo de idade. | Age |  |
| range | Duração do intervalo de idade. | Age |  |

**5.2.3. Parâmetro estatístico de biomarcador (BiomarkerStatisticalParameterType)**

Um conjunto de características estatísticas de um biomarcador medido em relação a um biomarcador específico.

Atributos do tipo de dados «BiomarkerStatisticalParameterType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometricMean | Média geométrica. | Measure |  |
| CI95ofGM | Intervalo de confiança de 95 % da média geométrica. | Measure |  |
| P50 | Percentil 50, ou valor mediano. Valor abaixo do qual se encontram 50 por cento das observações. | Measure |  |
| P90 | Percentil 90. Valor abaixo do qual se encontram 90 por cento das observações. | Measure |  |
| P95 | Percentil 95. Valor abaixo do qual se encontram 95 por cento das observações. | Measure |  |
| CI95ofP95 | Intervalo de confiança de 95 % do percentil 95. | Measure |  |
| maximum | Valor mais elevado do biomarcador determinado num participante individual no levantamento de biomonitorização. | Measure |  |
| pinLOD | Percentagem de indivíduos com níveis não detetáveis do parâmetro testado (abaixo do limite de deteção). | Real |  |
| LOQ | Limite de quantificação | Real |  |
| numberOfParticipants | Número de participantes que forneceram amostras que contribuíram para o cálculo do parâmetro estatístico do biomarcador. | Integer |  |

**5.2.4. Metadados temáticos do biomarcador (BiomarkerThematicMetadata)**

Metadados temáticos que descrevem o objetivo do estudo, a população-alvo e a característica das áreas estudadas.

Atributos do tipo de dados «BiomarkerThematicMetadata»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| studyType | Objetivo do estudo (baseado em hipóteses, levantamento geral da população, oportunístico), quando estas escolhas são predefinidas. | PT_FreeText |  |
| areaType | Características da área de amostragem (urbana, rural, semiurbana) quando estas escolhas são predefinidas num estudo da biomonitorização humana. | PT_FreeText |  |
| specificSubPopulation | Características da população objeto de amostragem no que se refere à idade, sexo e outras características da população quando essas escolhas são predefinidas num levantamento de biomonitorização humana. | PT_FreeText |  |
| meanAge | Média etária da subpopulação específica. | Age |  |

Associações do tipo de dados «BiomarkerThematicMetadata»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| describedBy | Metadados que estão ligados a dados do biomarcador | Biomarker |  |

**5.2.5. Tipo de biomarcador (BiomarkerType)**

Um biomarcador é definido tanto por uma substância química quantificada ou determinada (por exemplo, cádmio, chumbo) e pelo seu metabolito, como pela matriz (por exemplo, sangue, urina) que é utilizada para fins de quantificação; por exemplo - cádmio na urina, chumbo no sangue.

Atributos do tipo de dados «BiomarkerType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| chemical | Identificação do composto pelo nome ou abreviatura, fórmula química, CAS-PubChem ou qualquer outro número que é quantificado pela medição. | ChemicalValue |  |
| matrix | Tipo de material biológico ou sistema do corpo humano que é objeto de amostragem para determinar ou quantificar um biomarcador. | MatrixValue |  |

**5.2.6. Medição da doença (DiseaseMeasure)**

Diferentes formas possíveis de comunicação de dados sobre doenças e problemas de saúde conexos numa população.

Atributos do tipo de dados «DiseaseMeasure»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| diseaseMeasureType | Diferentes formas possíveis de comunicação de dados sobre doenças e problemas de saúde conexos. | DiseaseMeasureTypeValue |  |
| value | Valor do indicador de doença medido. | Real |  |

**5.2.7. Período de referência (ReferencePeriodType)**

Período ao qual se referem os dados.

Atributos do tipo de dados «ReferencePeriodType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| startDate | Início do período de referência. | Date |  |
| endDate | Termo do período de referência. | Date |  |

—————

**5.3. Listas de códigos**

**5.3.1. Causa de morte (CODValue)**

Dados sobre as causas de morte (Cause of Death — COD) que fornecem informações sobre os padrões de mortalidade e constituem um elemento importante da informação sobre saúde pública.

**5.3.2. Substância química (ChemicalValue)**

Nome da substância química.

**5.3.3. Tipo de componente ambiental da saúde (ComponentTypeValue)**

Tipo de componente específico (substância química, espécie biológica etc.) cuja concentração é medida num meio ambiental.

**5.3.4. Tipo de medida de doença (DiseaseMeasureTypeValue)**

Diferentes formas possíveis de comunicação de dados sobre doenças e problemas de saúde conexos.

**5.3.5. Tipo de determinante ambiental da saúde (EnvHealthDeterminantTypeValue)**

Tipo de determinante ambiental da saúde.

**5.3.6. Tipo de saúde geral (GeneralHealthTypeValue)**

Tipo do indicador do estado de saúde.

**5.3.7. Tipo de serviços de saúde (HealthServicesTypeValue)**

Tipo do indicador de cuidados de saúde.

**5.3.8. Classificação internacional das doenças (ICDValue)**

Doença conforme definido na International Classification of Diseases, 10.ª revisão.

**5.3.9. Matriz (MatrixValue)**

Tipo de sistema ou tecido humano para medição do biomarcador.

**5.3.10. Tipo de meio ambiental de saúde (MediaTypeValue)**

O meio em que é medida a concentração de um componente da saúde.

**5.3.11. Tipo de fonte de ruído (NoiseSourceTypeValue)**

Os valores do tipo de fonte de ruído.

**5.3.12. Método de agregação estatística (StatisticalAggregationMethodValue)**

Os tipos de métodos estatísticos utilizados para agregar dados de medições brutos na unidade estatística.

**5.4. Requisitos específicos de categorias temáticas**

(1) A informação estatística relativa à categoria temática de dados geográficos «Saúde Humana e Segurança» deve referir-se a objetos geográficos conforme definido na categoria temática de dados geográficos «Unidades Estatísticas».

(2) Sempre que possível, deve ser utilizada a lista de códigos de «ICDValue» para identificar o nome da doença.

(3) Os dados de medições brutas devem basear-se na norma ISO/TS 19103:2005.

(4) Os dados estatísticos de determinantes da saúde devem ser modelizados como dados estatísticos de saúde caracterizados por um valor de medição baseado na norma ISO/TS 19103:2005 e num método de agregação estatística.

(5) As coberturas de determinantes da saúde devem ser representadas utilizando os tipos de objetos geográficos definidos na secção 6 do anexo I. No que diz respeito a coberturas contínuas, deve ser utilizado um subtipo da classe «CoverageByDomainAndRange» cujo domínio é limitado aos valores de medições baseadas na norma ISO/TS 19103:2005.

**5.5. Camadas**

**Camadas para a categoria temática de dados geográficos «Saúde Humana e Segurança»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| HH.HealthStatisticalData | Dados estatísticos de saúde | StatisticalUnit |
| HH.HealthDeterminantMeasure | Medida de determinante da saúde | EnvHealthDeterminantMeasure |

**6. SERVIÇOS DE UTILIDADE PÚBLICA E DO ESTADO (UTILITY AND GOVERNMENTAL SERVICES)**

**6.1. Estrutura da categoria temática de dados geográficos «Serviços de Utilidade Pública e do Estado»**

Os tipos especificados para a categoria temática de dados geográficos «Serviços de Utilidade Pública e do Estado» estão estruturados nos seguintes pacotes:

— Elementos comuns de redes de utilidade pública (Common Utility Network Elements)

— Rede de eletricidade (Electricity Network)

— Rede de petróleo-gás-substâncias químicas (Oil-Gas-Chemicals Network)

— Rede de esgotos (Sewer Network)

— Rede térmica (Thermal Network)

— Rede de água (Water Network)

— Instalações de gestão ambiental (Environmental Management Facilities)

— Serviços administrativos e sociais do Estado (Administrative And Social Governmental Services)

**6.2. Elementos comuns de redes de utilidade pública**

**6.2.1. Tipos de objetos geográficos**

O pacote «Elementos Comuns de Redes de Utilidade Pública» contém os seguintes tipos de objetos geográficos:

— Rede de utilidade pública

— Elemento de rede de utilidade pública

— Conjunto de segmentos de rede de utilidade pública

— Nó de rede de utilidade pública

— Contentor de nó de rede de utilidade pública

— Elemento acessório

— Cabina

— Cabo

— Ducto

— Câmara de visita

— Conduta

— Poste

— Torre

6.2.1.1. Rede de utilidade pública (UtilityNetwork)

Coleção de elementos da rede que pertencem a um único tipo de rede de utilidade pública.

Atributos do tipo de objeto geográfico «UtilityNetwork»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| utilityNetworkType | Tipo de rede de utilidade pública ou categoria temática de rede de utilidade pública. | UtilityNetworkTypeValue |  |
| authorityRole | Partes autorizadas a gerir uma rede de utilidade pública, como os responsáveis pela manutenção, operadores ou proprietários. | RelatedParty |  |
| utilityFacilityReference | Referência a um complexo de atividades da instalação que está ligado a essa rede de utilidade pública. | ActivityComplex | voidable |
| disclaimer | Texto jurídico que descreve as cláusulas de confidencialidade aplicáveis às informações sobre a rede de utilidade pública. | PT_FreeText | voidable |

Associações do tipo de objeto geográfico «UtilityNetwork»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| networks | Uma única sub-rede que pode ser considerada como fazendo parte de uma rede de utilidade pública de ordem superior. | UtilityNetwork | voidable |

Restrições do tipo de objeto geográfico «UtilityNetwork»

Todas as redes de utilidade pública devem ter um identificador de objeto externo.

6.2.1.2. Elemento de rede de utilidade pública (UtilityNetworkElement)

Tipo de base abstrato que representa um elemento da rede de utilidade pública numa rede de utilidade pública. Cada elemento numa rede de utilidade pública desempenha uma função que é de interesse na rede de utilidade pública.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «UtilityNetworkElement»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| currentStatus | Estatuto de um objeto de utilidade pública no que diz respeito à sua completude e utilização. | ConditionOfFacilityValue | voidable |
| validFrom | Momento em que o elemento da rede de utilidade pública começou a existir no mundo real. | DateTime | voidable |
| validTo | Momento em que o elemento da rede de utilidade pública deixou de existir no mundo real. | DateTime | voidable |
| verticalPosition | Posição vertical do objeto de utilidade pública em relação ao solo. | VerticalPositionValue | voidable |
| utilityFacilityReference | Referência a um complexo de atividades que está ligado a (relacionado com) este elemento de rede de utilidade pública. | ActivityComplex | voidable |
| governmentalServiceReference | Referência a um objeto de serviço do Estado que está ligado a (relacionado com) este elemento de rede de utilidade pública. | GovernmentalService | voidable |

6.2.1.3. Conjunto de segmentos de utilidade pública (UtilityLinkSet)

Uma coleção de sequências de segmentos e/ou de segmentos individuais que tem uma função ou significado específico numa rede de utilidade pública.

Este tipo é um subtipo de «UtilityNetworkElement».

Este tipo é um subtipo de «LinkSet».

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «UtilityLinkSet»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| utilityDeliveryType | Rede de fornecimento de serviços de utilidade pública, por exemplo, transporte, distribuição, recolha. | UtilityDeliveryTypeValue | voidable |
| warningType | Mecanismo de aviso visível acima do solo utilizado para indicar um elemento subterrâneo de uma rede de utilidade pública. | WarningTypeValue | voidable |

Restrições do tipo de objeto geográfico «UtilityLinkSet»

Um conjunto de segmentos de utilidade pública deve ser composto por segmentos ou por sequências de segmentos todos eles pertencentes à mesma rede.

Todos os conjuntos de segmentos de utilidade pública devem ter um identificador de objeto externo.

6.2.1.4. Segmento de utilidade pública (UtilityLink)

Um objeto geográfico linear que descreve a geometria e a conectividade de uma rede de utilidade pública entre dois pontos da rede.

Este tipo é um subtipo de «UtilityNetworkElement».

Este tipo é um subtipo de «Link».

6.2.1.5. Sequência de segmentos de utilidade pública (UtilityLinkSequence)

Um objeto geográfico linear, constituído por uma coleção ordenada de segmentos de utilidade pública, que representa um traçado contínuo na rede de utilidade pública sem quaisquer ramificações. O elemento tem um início e um fim definidos e cada posição na sequência de segmentos de utilidade pública é identificável com um parâmetro único.

Este tipo é um subtipo de «UtilityNetworkElement».

Este tipo é um subtipo de «LinkSequence».

6.2.1.6. Nó de utilidade pública (UtilityNode)

Um objeto geográfico com representação pontual que é utilizado para fins de conectividade.

Este tipo é um subtipo de «UtilityNetworkElement».

Este tipo é um subtipo de «Node».

Este tipo é abstrato.

Restrições do tipo de objeto geográfico «UtilityNode»

Todos os nós de utilidade pública têm um identificador de objeto externo.

6.2.1.7. Contentor de nó de utilidade pública (UtilityNodeContainer)

Um objeto geográfico com representação pontual que é utilizado para fins de conectividade e também pode conter outros objetos geográficos (não necessariamente pertencentes à mesma rede de utilidade pública).

Este tipo é um subtipo de «UtilityNetworkElement».

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «UtilityNodeContainer»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| geometry | Localização do contentor do nó de utilidade pública. | GM_Point |  |

Associações do tipo de objeto geográfico «UtilityNodeContainer»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| nodes | Nós de utilidade pública contidos. | UtilityNode | voidable |

6.2.1.8. Elemento acessório (Appurtenance)

Um elemento acessório é um objeto do nó que é descrito pelo seu tipo (através do atributo «appurtenanceType»).

Este tipo é um subtipo de «UtilityNode».

Atributos do tipo de objeto geográfico «Appurtenance»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| appurtenanceType | Tipo de elemento acessório, de acordo com a classificação do tipo de elementos acessórios INSPIRE. | AppurtenanceTypeValue | voidable |
| specificAppurtenanceType | Tipo de elemento acessório de acordo com uma classificação específica de domínio. | SpecificAppurtenanceTypeValue | voidable |

6.2.1.9. Cabina (Cabinet)

Objeto de cabina simples que pode transportar objetos de utilidade pública para redes de utilidade pública quer únicas quer múltiplas.

Este tipo é um subtipo de «UtilityNodeContainer».

6.2.1.10. Cabo (Cable)

Um segmento ou sequência de segmentos de utilidade pública para transportar eletricidade ou dados de um local para outro.

Este tipo é um subtipo de «UtilityLinkSet».

Este tipo é abstrato.

6.2.1.11. Ducto (Duct)

Um segmento ou sequência de segmentos de utilidade pública utilizados para proteger e guiar cabos e condutas mediante uma construção de confinamento.

Este tipo é um subtipo de «UtilityLinkSet».

Atributos do tipo de objeto geográfico «Duct»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| ductWidth | A largura do ducto. | Length | voidable |

Associações do tipo de objeto geográfico «Duct»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| cables | Um ducto pode conter um ou mais cabos. | Cable | voidable |
| ducts | Um ducto único ou um conjunto de ductos que constituem o ducto interior. | Duct | voidable |
| pipes | O conjunto de condutas que constitui o banco de condutas. | Pipe | voidable |

Restrições do tipo de objeto geográfico «Duct»

A multiplicidade do atributo «utilityDeliveryType» deve ser 0.

6.2.1.12. Câmara de visita (Manhole)

Um objeto de contentor simples que pode conter objetos de redes de utilidade pública simples ou múltiplos.

Este tipo é um subtipo de «UtilityNodeContainer».

6.2.1.13. Conduta (Pipe)

Um segmento ou sequência de segmentos de utilidade pública para o transporte de sólidos, líquidos, substâncias químicas ou gases de um local para outro. Uma conduta pode também ser utilizada como um objeto para envolver vários cabos (um feixe de cabos) ou outras condutas (de menor dimensão).

Este tipo é um subtipo de «UtilityLinkSet».

Atributos do tipo de objeto geográfico «Pipe»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| pipeDiameter | Diâmetro exterior da conduta. | Measure | voidable |
| pressure | A pressão de funcionamento máxima autorizada a que um produto é transportado através de uma conduta. | Measure | voidable |

Associações do tipo de objeto geográfico «Pipe»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| cable | Cabo contido na conduta. | Cable | voidable |
| pipe | Conduta contida na conduta. | Pipe | voidable |

6.2.1.14. Poste (Pole)

Objeto simples de poste (pilar) que pode suportar objetos de utilidade pública pertencentes a redes de utilidade pública quer únicas quer múltiplas.

Este tipo é um subtipo de «UtilityNodeContainer».

Atributos do tipo de objeto geográfico «Pole»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| poleHeight | Altura do poste. | Length | voidable |

6.2.1.15. Torre (Tower)

Objeto de torre simples que pode suportar objetos de utilidade pública pertencentes a redes de utilidade pública quer únicas quer múltiplas.

Este tipo é um subtipo de «UtilityNodeContainer».

Atributos do tipo de objeto geográfico «Tower»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| towerHeight | Altura da torre. | Length | voidable |

**6.2.2. Listas de códigos**

6.2.2.1. Tipo de elemento acessório (AppurtenanceTypeValue)

Classificação de elementos acessórios.

Esta lista de códigos inclui os valores constantes das listas de códigos seguintes ou de outras listas de códigos especificadas pelos fornecedores dos dados:

— Tipo de elemento acessório de rede de eletricidade (ElectricityAppurtenanceTypeValue): Classificação de elementos acessórios de redes de eletricidade, conforme especificado no ponto 6.3.2.1.

— Tipo de elemento acessório de redes de petróleo, gás e substâncias químicas (OilGasChemicalsAppurtenanceTypeValue): Classificação de elementos acessórios de redes de petróleo, gás e substâncias químicas, conforme especificado no ponto 6.4.2.1.

— Tipo de elemento acessório de rede de esgotos (SewerAppurtenanceTypeValue): Classificação de elementos acessórios de redes de esgotos, conforme especificado no ponto 6.5.2.1.

— Tipo de elemento acessório de rede térmica (ThermalAppurtenanceTypeValue): Classificação de elementos acessórios de redes térmicas, conforme especificado no ponto 6.6.2.1.

— Tipo de elemento acessório de rede de água (WaterAppurtenanceTypeValue): Classificação de elementos acessórios de redes de água, conforme especificado no ponto 6.7.2.1.

6.2.2.2. Tipo de elemento acessório específico (SpecificAppurtenanceTypeValue)

Classificação de elementos acessórios específicos de domínios.

6.2.2.3. Tipo de fornecimento de utilidade pública (UtilityDeliveryTypeValue)

Classificação dos tipos de fornecimento de utilidade pública.

6.2.2.4. Tipo de rede de utilidade pública (UtilityNetworkTypeValue)

Classificação dos tipos de redes de utilidade pública.

6.2.2.5. Tipo de aviso (WarningTypeValue)

Classificação dos tipos de avisos.

**6.3. Rede de eletricidade**

**6.3.1. Tipos de objetos geográficos**

O pacote «Rede de Eletricidade» contém o tipo de objeto geográfico Cabo de Eletricidade.

6.3.1.1. Cabo de eletricidade (ElectricityCable)

Um segmento ou sequência de segmentos de utilidade pública para transportar eletricidade de um local para outro.

Este tipo é um subtipo de «Cable».

Atributos do tipo de objeto geográfico «ElectricityCable»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| operatingVoltage | Tensão de serviço ou tensão de funcionamento do equipamento que consome eletricidade. | Measure | voidable |
| nominalVoltage | Tensão nominal do sistema no ponto de fornecimento. | Measure | voidable |

**6.3.2. Listas de códigos**

6.3.2.1. Tipo de elemento acessório de rede de eletricidade (ElectricityAppurtenanceTypeValue)

Classificação de elementos acessórios de redes de eletricidade.

**6.4. Rede de petróleo-gás-substâncias químicas (Oil-Gas-Chemicals Network)**

**6.4.1. Tipos de objetos geográficos**

O pacote «Rede de Petróleo-Gás-Substâncias Químicas» contém o tipo de objeto geográfico Conduta de Petróleo, Gás e Substâncias Químicas.

6.4.1.1. Conduta de petróleo, gás e substâncias químicas (OilGasChemicalsPipe)

Conduta utilizada para transportar petróleo, gás ou substâncias químicas de um local para outro.

Este tipo é um subtipo de «Pipe».

Atributos do tipo de objeto geográfico «OilGasChemicalsPipe»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| oilGasChemicalsProductType | Tipo de petróleo, gás ou produto químico que é transportado pelas condutas de petróleo, gás e substâncias químicas. | OilGasChemicalsProductTypeValue | voidable |

**6.4.2. Listas de códigos**

6.4.2.1. Tipo de elemento acessório de redes de petróleo, gás e substâncias químicas (OilGasChemicalsAppurtenanceTypeValue)

Classificação de elementos acessórios de redes de petróleo, gás, substâncias químicas.

6.4.2.2. Tipo de produtos de petróleo, gás e substâncias químicas (OilGasChemicalsProductTypeValue)

Classificação de produtos de petróleo, gás e substâncias químicas.

**6.5. Rede de esgotos**

**6.5.1. Tipos de objetos geográficos**

O pacote «Rede de Esgotos» contém o tipo de objeto geográfico Conduta de Esgotos.

6.5.1.1. Conduta de esgotos (SewerPipe)

Uma conduta de esgotos utilizada para transportar águas residuais (esgotos) de um local para outro.

Este tipo é um subtipo de «Pipe».

Atributos do tipo de objeto geográfico «SewerPipe»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| sewerWaterType | Tipo de águas residuais. | SewerWaterTypeValue | voidable |

**6.5.2. Listas de códigos**

6.5.2.1. Tipo de elemento acessório de rede de esgotos (SewerAppurtenanceTypeValue)

Classificação de elementos acessórios de redes de esgotos.

6.5.2.2. Tipo de águas de esgotos (SewerWaterTypeValue)

Classificação dos tipos de águas de esgotos.

**6.6. Rede térmica (Thermal Network)**

**6.6.1. Tipos de objetos geográficos**

O pacote «Rede Térmica» contém o tipo de objeto geográfico Conduta Térmica.

6.6.1.1. Conduta térmica (ThermalPipe)

Conduta utilizada para difundir calor ou frio de um local para outro.

Este tipo é um subtipo de «Pipe».

Atributos do tipo de objeto geográfico «ThermalPipeonstruction»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| thermalProductType | Tipo de produto térmico que é transmitido através da conduta térmica. | ThermalProductTypeValue | voidable |

**6.6.2. Listas de códigos**

6.6.2.1. Tipo de elemento acessório de rede térmica (ThermalAppurtenanceTypeValue)

Classificação de elementos acessórios de redes térmicas.

6.6.2.2. Tipo de produto térmico (ThermalProductTypeValue)

Classificação de produtos térmicos.

**6.7. Rede de água (Water Network)**

**6.7.1. Tipos de objetos geográficos**

O pacote «Rede de Água» contém o tipo de objeto geográfico Conduta de Água.

6.7.1.1. Conduta de água (WaterPipe)

Uma conduta de água utilizada para transportar água de um local para outro.

Este tipo é um subtipo de «Pipe».

Atributos do tipo de objeto geográfico «WaterPipe»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| waterType | Tipo de água. | WaterTypeValue | voidable |

**6.7.2. Listas de códigos**

6.7.2.1. Tipo de elemento acessório de rede de água (WaterAppurtenanceTypeValue)

Classificação de elementos acessórios de redes de água.

6.7.2.2. Tipo de águas (WaterTypeValue)

Classificação dos tipos de águas.

**6.8. Instalações de gestão ambiental (Environmental Management Facilities)**

**6.8.1. Tipos de objetos geográficos**

O pacote «Instalações de Gestão Ambiental» contém o tipo de objeto geográfico Instalação de Gestão Ambiental.

6.8.1.1. Instalação de gestão ambiental (EnvironmentalManagementFacility)

Uma estrutura física concebida, construída ou instalada para servir funções específicas relacionadas com fluxos de materiais ambientais, tais como fluxos de resíduos ou de águas residuais, ou uma área delimitada de terreno ou água utilizada para servir essas funções.

Este tipo é um subtipo de «ActivityComplex».

Atributos do tipo de objeto geográfico «EnvironmentalManagementFacility»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| type | Tipo de instalação, como uma instalação técnica ou sítio. | EnvironmentalManagementFacilityTypeValue | voidable |
| serviceHours | Horas de serviço da instalação. | PT_FreeText | voidable |
| facilityDescription | Informações adicionais sobre uma instalação de gestão ambiental, incluindo o seu endereço, dados de contacto, partes relacionadas e uma descrição em texto livre. | ActivityComplexDescription | voidable |
| physicalCapacity | Quantificação de uma capacidade real ou potencial para desenvolver uma atividade. | Capacity | voidable |
| permission | Decisão oficial (consentimento formal) que concede a autorização para explorar toda ou parte de uma instalação de gestão ambiental | Permission | voidable |
| status | Estatuto da instalação de gestão ambiental, como operacional ou desmantelada. | ConditionOfFacilityValue | voidable |

Associações do tipo de objeto geográfico «EnvironmentalManagementFacility»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| parentFacility | Uma instalação-mãe, ou seja uma instalação a que esta instalação pertence. | EnvironmentalManagementFacility | voidable |

**6.8.2. Listas de códigos**

6.8.2.1. Classificação da instalação ambiental (EnvironmentalManagementFacilityTypeValue)

Classificação das instalações ambientais, por exemplo, sítios e instalações técnicas.

**6.9. Serviços administrativos e sociais do Estado (Administrative And Social Governmental Services)**

**6.9.1. Tipos de objetos geográficos**

O pacote «Serviços Administrativos e Sociais do Estado» contém o tipo de objeto geográfico Serviço do Estado.

6.9.1.1. Serviço do Estado (GovernmentalService)

Serviços administrativos e sociais do Estado, tais como administrações públicas, sítios da proteção civil, escolas e hospitais, prestados por órgãos das administrações públicas ou por instituições privadas na medida em que estejam abrangidos pela Diretiva 2007/2/CE. Este âmbito é cartografado em função dos valores da lista de códigos correspondente «ServiceTypeValue».

Atributos do tipo de objeto geográfico «GovernmentalService»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| areaOfResponsibility | Responsabilidade geográfica de uma instância do serviço. | AreaOfResponsibilityType | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| pointOfContact | Contém as informações necessárias para obter acesso a um serviço e/ou informação inicial sobre um serviço. | Contact | voidable |
| serviceLocation | Local em que o serviço é oferecido. | ServiceLocationType |  |
| serviceType | Tipo de um serviço administrativo e do Estado. | ServiceTypeValue |  |

**6.9.2. Tipos de dados**

6.9.2.1. Tipo de área de responsabilidade (AreaOfResponsibilityType)

Conjunto de tipos para a descrição da responsabilidade geográfica.

Este tipo é um tipo de união.

Atributos do tipo de dados «AreaOfResponsibilityType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| areaOfResponsibilityByAdministrativeUnit | Unidade administrativa que descreve a extensão geográfica sob a responsabilidade de um serviço. | AdministrativeUnit |  |
| areaOfResponsibilityByNamedPlace | Objeto geográfico que descreve a extensão geográfica sob a responsabilidade de um serviço. | NamedPlace |  |
| areaOfResponsibilityByNetwork | Parte de uma rede que descreve a extensão geográfica da competência de um serviço. | NetworkReference |  |
| areaOfResponsibilityByPolygon | Polígono que descreve a extensão geográfica sob a responsabilidade de um serviço. | GM_MultiSurface |  |

6.9.2.2. Tipo de localização do serviço (ServiceLocationType)

Conjunto de tipos de referências para localizar um serviço.

Este tipo é um tipo de união.

Atributos do tipo de união «ServiceLocationType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| serviceLocationByAddress | Localização do serviço por referência a um endereço. | Address |  |
| serviceLocationByBuilding | Localização do serviço por referência a um edifício. | Building («Edifício») do pacote «Edifícios 2D» |  |
| serviceLocationByActivityComplex | Localização do serviço por referência a um complexo de atividades. | ActivityComplex |  |
| serviceLocationByGeometry | Localização do serviço por referência a uma geometria. | GM_Object |  |
| serviceLocationByUtilityNode | Localização do serviço por referência a um nó relacionado com uma rede de utilidade pública (água, eletricidade etc.), por exemplo hidrante ou ponto de chamada de emergência. | UtilityNode |  |

**6.9.3. Listas de códigos**

6.9.3.1. Tipo de serviço (ServiceTypeValue)

Lista de códigos que contém uma classificação dos serviços estatais.

**6.10. Camadas**

**Camadas da categoria temática de dados geográficos «Serviços de Utilidade Pública e do Estado»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| US.UtilityNetwork | Rede de utilidade pública | Appurtenance, Manhole, Tower, Pole, Cabinet, Duct, Pipe |
| US.ElectricityNetwork | Rede de eletricidade | Electricity Cable, Appurtenance (se incluído na rede de eletricidade) |
| US. OilGasChemicalsNetwork | Rede de petróleo, gás ou substâncias químicas | OilGasChemicalsPipe, Appurtenance (se incluído numa rede de petróleo, gás ou substâncias químicas) |
| US.SewerNetwork | Rede de esgotos | SewerPipe, Appurtenance (se incluído numa rede de esgotos) |
| US.ThermalNetwork | Rede térmica | ThermalPipe, Appurtenance (se incluído numa rede térmica) |
| US.WaterNetwork | Rede de água | WaterPipe, Appurtenance (se incluído numa rede de água) |
| US. <Valor de lista de códigos> (1) | <nome legível para as pessoas> | GovernmentalService |
| Exemplo: Serviço de polícia | Exemplo: US.PoliceService | (serviceType: ServiceTypeValue) |
| US.EnvironmentalManagementFacility | Instalação de gestão do ambiente | EnvironmentalManagementFacility |
| (1) <br> Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3 |  |  |

**7. INSTALAÇÕES DE MONITORIZAÇÃO DO AMBIENTE (ENVIRONMENTAL MONITORING FACILITIES)**

**7.1. Tipos de objetos geográficos**

São especificados os seguintes tipos de objetos geográficos para a categoria temática de dados geográficos «Instalações de Monitorização do Ambiente»:

— Característica de monitorização abstrata

— Objeto de monitorização abstrato

— Atividade de monitorização do ambiente

— Instalação de monitorização do ambiente

— Rede de monitorização do ambiente

— Programa de monitorização do ambiente

— Capacidade de observação

— Período de atividade operacional

**7.1.1. Característica de monitorização abstrata (AbstractMonitoringFeature)**

Uma classe de base abstrata para características de monitorização do ambiente no mundo real («EnvironmentalMonitoringNetwork», «EnvironmentalMonitoringFacility»).

Este tipo é um subtipo de «AbstractMonitoringObject».

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «AbstractMonitoringFeature»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| reportedTo | Informação sobre o envolvimento da «AbstractMonitoringFeature» na comunicação de informações. | ReportToLegalAct | voidable |

Associações do tipo de objeto geográfico «AbstractMonitoringFeature»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| involvedIn | «Environmentalmonitoringactivity(s)» em que está envolvida a «AbstractMonitoringFeature». | EnvironmentalMonitoringActivity | voidable |
| hasObservation | Observações de emissões, do estado dos meios ambientais e de outros parâmetros dos ecossistemas (biodiversidade, condições ecológicas da vegetação, etc.) pelas autoridades públicas ou por conta destas nesta «AbstractMonitoringFeature». | OM_Observation | voidable |

Restrições do tipo de objeto geográfico «AbstractMonitoringFeature»

Se a ou as observações estiverem ligadas a uma «AbstractMonitoringFeature», esta deve ter uma «ObservingCapability» apensa. A «ObservingCapability» deve referenciar o mesmo «Domain», «Phenomenon» e «ProcessUsed» da(s) observação(ões).

**7.1.2. Objeto de monitorização abstrato (AbstractMonitoringObject)**

Uma classe de base abstrata para objetos de monitorização do ambiente.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «AbstractMonitoringObject»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| thematicId | Identificador de objeto temático. | ThematicIdentifier | voidable |
| name | Denotação em texto simples do «AbstractMonitoringObject» | CharacterString | voidable |
| additionalDescription | Descrição em texto simples de informações adicionais que não se integrem noutros atributos. | CharacterString | voidable |
| mediaMonitored | Meio ambiental monitorizado. | MediaValue |  |
| legalBackground | Contexto jurídico em que a gestão e a regulamentação do «AbstractMonitoringObject» são definidas. | LegislationCitation | voidable |
| responsibleParty | Parte responsável pelo «AbstractMonitoringObject». | RelatedParty | voidable |
| geometry | Geometria associada ao «AbstractMonitoringObject». Para instalações móveis, a geometria representa a área em que presumivelmente a instalação efetua medições. | GM_Object |  |
| onlineResource | Uma ligação a um documento externo que fornece outras informações sobre o «AbstractMonitoringObject». | URL | voidable |
| purpose | Razão pela qual o «AbstractMonitoringObject» foi gerado. | PurposeOfCollectionValue | voidable |

Associações do tipo de objeto geográfico «AbstractMonitoringObject»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| observingCapability | Ligação que aponta para uma capacidade explícita de um «AbstractMonitoringObject». Fornece uma ligação clara entre a propriedade observada e o procedimento utilizado, bem como o local da medição. | ObservingCapability | voidable |
| broader | Ligação que aponta para um «AbstractMonitoringObject» mais vasto (um nível mais elevado numa estrutura hierárquica). <br> A associação tem propriedades adicionais conforme definido na classe de associação Hierarquia. | AbstractMonitoringObject | voidable |
| narrower | Ligação que aponta para um «AbstractMonitoringObject» mais restrito (um nível mais baixo numa estrutura hierárquica). <br> A associação tem propriedades adicionais conforme definido na classe de associação Hierarquia. | AbstractMonitoringObject | voidable |
| supersedes | Numa genealogia, o ou os «AbstractMonitoringObject(s)» que tenham sido desativados/substituídos por outro. | AbstractMonitoringObject | voidable |
| supersededBy | Numa genealogia, o ou os novos «AbstractMonitoringObject(s)» ativos que substituem o suplantado. | AbstractMonitoringObject | voidable |

**7.1.3. Atividade de monitorização do ambiente (EnvironmentalMonitoringActivity)**

Conjunto específico de «AbstractMonitoringFeatures» utilizado para um determinado domínio com uma escala temporal, área e finalidade coerentes e concisas. Geralmente, a informação recolhida é tratada como uma etapa temporal num programa de monitorização a longo prazo. É uma realização concreta de um determinado «EnvironmentalMonitoringProgramme».

Atributos do tipo de objeto geográfico «EnvironmentalMonitoringActivity»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| activityTime | Duração da «EnvironmentalMonitoringActivity». | TM_Object | voidable |
| activityConditions | Descrição textual da «EnvironmentalMonitoringActivity». | CharacterString | voidable |
| boundingBox | Caixa envolvente em que se realiza a «EnvironmentalMonitoringActivity». | GM_Boundary | voidable |
| responsibleParty | Parte responsável pela «EnvironmentalMonitoringActivity». | RelatedParty | voidable |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| onlineResource | Ligação a um documento externo que fornece outras informações sobre a «EnvironmentalMonitoringActivity». | URL | voidable |

Associações do tipo de objeto geográfico «EnvironmentalMonitoringActivity»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| setUpFor | «EnvironmentalMonitoringProgramme(s)» relativamente aos quais é criada a «EnvironmentalMonitoringActivity». | EnvironmentalMonitoringProgramme | voidable |
| uses | Conjunto específico de «AbstractMonitoringFeature(s)» envolvido numa «EnvironmentalMonitoringActivity». | AbstractMonitoringFeature | voidable |

**7.1.4. Instalação de monitorização do ambiente(EnvironmentalMonitoringFacility)**

Um objeto georreferenciado que recolhe ou trata dados diretamente sobre objetos cujas propriedades (por exemplo, físicas, químicas, biológicas ou outros aspetos das condições ambientais) são repetidamente observadas ou medidas. Uma instalação de monitorização do ambiente pode também acolher outras instalações de monitorização do ambiente.

Este tipo é um subtipo de «AbstractMonitoringFeature».

Atributos do tipo de objeto geográfico «EnvironmentalMonitoringFacility»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| representativePoint | Localização representativa da «EnvironmentalMonitoringFacility». | GM_Point | voidable |
| measurementRegime | Regime da medição | MeasurementRegimeValue | voidable |
| mobile | Indica se a «EnvironmentalMonitoringFacility» é móvel (reposicionável) durante a aquisição da observação. | Boolean | voidable |
| resultAcquisitionSource | Fonte de aquisição dos resultados. | ResultAcquisitionSourceValue | voidable |
| specialisedEMFType | Categorização das «EnvironmentalMonitoringFacilities» geralmente utilizada por domínio e em contextos nacionais. | SpecialisedEMFTypeValue | voidable |
| operationalActivityPeriod | O(s) período(s) em que a «EnvironmentalMonitoringFacility» foi criada e está em funcionamento. | TM_Object | voidable |

Associações do tipo de objeto geográfico «EnvironmentalMonitoringFacility»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| relatedTo | Qualquer ligação temática a uma instalação de monitorização do ambiente. <br> A associação tem propriedades adicionais conforme definido na classe de associação «AnyDomainLink». | EnvironmentalMonitoringFacility | voidable |
| belongsTo | Uma ligação que aponta para a(s) «EnvironmentalMonitoringNetwork(s)» a que esta «EnvironmentalMonitoringFacility» pertence. <br> A associação tem propriedades adicionais conforme definido na classe de associação «NetworkFacility». | EnvironmentalMonitoringNetwork | voidable |

Restrições do tipo de objeto geográfico «EnvironmentalMonitoringFacility»

A geometria e «representativePoint» não podem estar ambos vazios.

**7.1.5. Rede de monitorização do ambiente (EnvironmentalMonitoringNetwork)**

Agrupamento organizacional ou administrativo de «EnvironmentalMonitoringFacilities» gerido da mesma forma para um fim específico e visando uma área específica. Cada rede respeita regras comuns destinadas a garantir a coerência das observações, especialmente para fins das «EnvironmentalMonitoringFacilities», da seleção de parâmetros obrigatórios, dos métodos de medição e do regime de medição.

Este tipo é um subtipo de «AbstractMonitoringFeature».

Atributos do tipo de objeto geográfico «EnvironmentalMonitoringNetwork»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| organisationLevel | Nível de organização jurídica a que está associada a «EnvironmentalMonitoringNetwork». | LegislationLevelValue | voidable |

Associações do tipo de objeto geográfico «EnvironmentalMonitoringNetwork»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| contains | Ligação que aponta para a(s) «EnvironmentalMonitoringFacility(s)» incluídas nesta «EnvironmentalMonitoringNetwork». <br> A associação tem propriedades adicionais conforme definido na classe de associação «NetworkFacility». | EnvironmentalMonitoringFacility | voidable |

**7.1.6. Programa de monitorização do ambiente (EnvironmentalMonitoringProgramme)**

Quadro baseado em documentos relevantes para as políticas que define o objetivo de uma coleção de observações e/ou a implantação de «AbstractMonitoringFeatures» no terreno. Geralmente um programa de monitorização do ambiente tem uma perspetiva a longo prazo durante, pelo menos, alguns anos.

Este tipo é um subtipo de «AbstractMonitoringObject».

Associações do tipo de objeto geográfico «EnvironmentalMonitoringProgramme»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| triggers | «EnvironmentalMonitoringActivity(s)» desencadeada(s) pelo «EnvironmentalMonitoringProgramme». | EnvironmentalMonitoringActivity | voidable |

**7.1.7. Capacidade de observação (ObservingCapability)**

Capacidade explícita de um «AbstractMonitoringObject».

Atributos do tipo de objeto geográfico «ObservingCapability»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| observingTime | Descreve o período de tempo em que se podem esperar observações deste «AbstractMonitoringObject». Pode ser apenas um tempo de início para medições em curso ou um intervalo. | TM_Object | voidable |
| processType | Tipo de objeto utilizado para descrever o processo. | ProcessTypeValue | voidable |
| resultNature | Estado do resultado fornecido. | ResultNatureValue | voidable |
| onlineResource | Ligação a um documento externo que fornece outras informações sobre um modelo de dados conforme à norma ISO 19156 sobre «Observations and Measurements» utilizada para o armazenamento ou intercâmbio das observações e medições adquiridas. | URL | voidable |

Associações do tipo de objeto geográfico «ObservingCapability»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| observedProperty | A propriedade observada ou medida neste «AbstractMonitoringObject». | GF_PropertyType |  |
| featureOfInterest | Esta característica é o objeto do mundo real cujas propriedades estão sob observação, ou é uma característica que funciona como amostragem do objeto do mundo real. | GFI_Feature | voidable |
| procedure | Ligação ao processo utilizado para gerar o resultado. O «OM_Process» deve ser adequado à propriedade observada. Como corolário, os dados detalhados sobre a propriedade observada estão restringidos pelo procedimento utilizado. | OM_Process |  |

**7.2. Tipos de dados**

**7.2.1. Ligação a qualquer domínio (AnyDomainLink)**

Qualquer ligação, relevante para um domínio, a uma «EnvironmentalMonitoringFacility» que não é hierárquica nem está associada a uma noção de genealogia.

Este tipo é uma classe de associação.

Atributos do tipo de dados «AnyDomainLink»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| Comment | Informação adicional sobre a ligação ao domínio. | CharacterString | voidable |

**7.2.2. Hierarquia (Hierarchy)**

Ligação hierárquica entre «AbstractMonitoringObjects».

Este tipo é uma classe de associação.

Atributos do tipo de dados «Hierarchy»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| linkingTime | Período de tempo da ligação. | TM_Object | voidable |

**7.2.3. Instalação de rede (NetworkFacility)**

Ligação entre «EnvironmentalMonitoringNetwork» e «EnvironmentalMonitoringFacility».

Este tipo é uma classe de associação.

Atributos do tipo de dados «NetworkFacility»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| linkingTime | Período de tempo da ligação. | TM_Object | voidable |

**7.2.4. Relatório para ato jurídico (ReportToLegalAct)**

Informação sobre o envolvimento de uma «AbstractMonitoringFeature» na comunicação de informações. A informação é específica por conjunto de informações apresentadas e não por obrigação/acordo.

Atributos do tipo de dados «ReportToLegalAct»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| legalAct | «LegalAct» a que está ligada a comunicação de informações. | LegislationCitation |  |
| reportDate | Data da comunicação de informações. | DateTime | voidable |
| reportedEnvelope | Ligação para o conjunto de dados que é objeto da comunicação de informações de acordo com a data indicada no atributo «reportDate». | URI | voidable |
| observationRequired | Indica se é exigida uma observação para a «AbstractMonitoringFeature». | Boolean | voidable |
| observingCapabilityRequired | Indica se é exigida a «observingCapability» para a «AbstractMonitoringFeature». | Boolean | voidable |
| description | Informação adicional sobre os dados efetivos comunicados. | CharacterString | voidable |

**7.3. Listas de códigos**

**7.3.1. Regime de medição (MeasurementRegimeValue)**

Categorias para diferentes tipos de «MeasurementRegime».

**7.3.2. Meios (MediaValue)**

Categorias para diferentes tipos de meios.

**7.3.3. Tipo de processo (ProcessTypeValue)**

Categorias para diferentes tipos de processos.

**7.3.4. Finalidade da coleção (PurposeOfCollectionValue)**

Categorias para diferentes finalidades das coleções.

**7.3.5. Fonte de aquisição dos resultados (ResultAcquisitionSourceValue)**

Categorias para diferentes tipos de «ResultAcquisitionSource».

**7.3.6. Natureza do resultado (ResultNatureValue)**

Estado do resultado de uma observação.

**7.3.7. Tipo EMF especializado (SpecialisedEMFTypeValue)**

Categorias para diferentes tipos de «EnvironmentalMonitoringFacilities».

**7.4. Camadas**

**Camadas para a categoria temática de dados geográficos «Instalações de Monitorização do Ambiente»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| EF.EnvironmentalMonitoringFacilities | Instalações de monitorização do ambiente | EnvironmentalMonitoringFacility |
| EF.EnvironmentalMonitoringNetworks | Redes de monitorização do ambiente | EnvironmentalMonitoringNetwork |
| EF.EnvironmentalMonitoringProgrammes | Programas de monitorização do ambiente | EnvironmentalMonitoringProgramme |

**8. INSTALAÇÕES INDUSTRIAIS E DE PRODUÇÃO (PRODUCTION AND INDUSTRIAL FACILITIES)**

**8.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) «Emissão» (emission) : a libertação direta ou indireta de substâncias, vibrações, calor ou ruído para o ar, a água ou o solo, a partir de fontes pontuais ou difusas na instalação;

(2) «Produção» (production) : uma atividade que consiste numa série de ações ou operações num contexto produtivo.

**8.2. Tipos de objetos geográficos**

São especificados os seguintes tipos de objetos geográficos para a categoria temática de dados geográficos «Instalações Industriais e de Produção»:

— Instalação de produção

— Instalação técnica de produção

— Parte da instalação técnica de produção

— Sítio de produção

— Parcela de produção

— Edifício de produção

**8.2.1. Instalação de produção (ProductionFacility)**

Uma ou mais instalações técnicas no mesmo sítio, exploradas pela mesma pessoa singular ou coletiva, projetadas, construídas ou instaladas para fins específicos industriais ou de produção, compreendendo todas as infraestruturas, equipamentos e materiais.

Este tipo é um subtipo de «ActivityComplex».

Atributos do tipo de objeto geográfico «ProductionFacility»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| surfaceGeometry | Propriedade espacial do objeto geográfico. | GM_Surface | voidable |
| riverBasinDistrict | Identificador e/ou nome do código atribuído à bacia hidrográfica de um curso de água. | RiverBasinDistrictValue |  |
| status | Estado ou condição da instalação, no que se refere à ordem funcional e operacional, em que se encontra durante um período de tempo limitado ou alargado. | StatusType | voidable |

Associações do tipo de objeto geográfico «ProductionFacility»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| groupedBuilding | Edifícios geridos pela instalação de produção. | ProductionBuilding | voidable |
| groupedPlot | Parcelas geridas pela instalação de produção. | ProductionPlot | voidable |
| hostingSite | Sítios numa localização geográfica distinta em que a instalação de produção está localizada. | ProductionSite | voidable |
| groupedInstallation | Instalações técnicas que fazem técnica ou juridicamente parte da instalação de produção. | ProductionInstallation | voidable |

**8.2.2. Instalação técnica de produção (ProductionInstallation)**

Uma unidade técnica fixa, como máquinas, aparelhos, dispositivos ou equipamentos colocados em posição ou ligados para utilização, no interior da qual são realizadas uma ou mais das atividades enumeradas no anexo I do Regulamento (CE) n.º 166/2006 do Parlamento Europeu e do Conselho (

12

) e no anexo I ou no anexo VII, parte 1, da Diretiva 2010/75/UE do Parlamento Europeu e do Conselho (

13

) e quaisquer outras atividades a elas diretamente associadas que tenham uma relação técnica com as atividades enumeradas e possam ter efeitos nas emissões e na poluição.

**Atributos do tipo de objeto geográfico «ProductionInstallation»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| thematicId | Identificador de objeto temático. | ThematicIdentifier |  |
| pointGeometry | Propriedade espacial do objeto geográfico. | GM_Point |  |
| surfaceGeometry | Propriedade espacial do objeto geográfico. | GM_Surface | voidable |
| name | Denominação oficial ou nome próprio ou convencional da instalação técnica. | CharacterString | voidable |
| description | Enunciado descritivo sobre a instalação técnica. | CharacterString | voidable |
| status | Estado ou condição da instalação técnica, no que se refere a funcionamento e operacionalidade, em que a mesma se encontra durante um período limitado ou alargado. | StatusType | voidable |
| type | Género especial de uma instalação técnica que denota a função operativa a desempenhar. | InstallationTypeValue | voidable |

**Associações do tipo de objeto geográfico «ProductionInstallation»**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| groupedInstallationPart | Pequenas instalações técnicas que fazem técnica ou juridicamente parte de uma instalação técnica. | ProductionInstallationPart | Voidable |

**8.2.3. Parte de instalação técnica de produção (ProductionInstallationPart)**

Uma única instalação de engenharia que executa funcionalidades específicas relacionadas com uma atividade produtiva.

Este nível de descrição abrange partes específicas da instalação técnica de produção que devem ser registadas por mandato legal das autoridades competentes, incluindo pontos de emissão como chaminés (para os poluentes) ou tanques (para produtos especiais).

Atributos do tipo de objeto geográfico «ProductionInstallationPart»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| thematicId | Identificador de objeto temático. | ThematicIdentifier |  |
| pointGeometry | Propriedade espacial do objeto geográfico. | GM_Point |  |
| surfaceGeometry | Propriedade espacial do objeto geográfico. | GM_Surface | voidable |
| name | Denominação oficial ou nome próprio ou convencional da parte da instalação técnica. | CharacterString | voidable |
| description | Enunciado descritivo sobre a parte da instalação técnica. | CharacterString | voidable |
| status | Estado ou condição da parte da instalação técnica, no que se refere a funcionamento e operacionalidade, em que se a mesma se encontra durante um período limitado ou alargado. | StatusType | voidable |
| type | Género especial de uma parte da instalação técnica que denota a função operativa a desempenhar. | InstallationPartTypeValue | voidable |
| technique | Método para reduzir a concentração de poluentes decorrente das emissões de um componente técnico, geralmente uma chaminé. | PollutionAbatementTechniqueValue | voidable |

**8.2.4. Sítio de produção (ProductionSite)**

Todo o terreno numa localização geográfica distinta em que a instalação de produção foi, é ou será localizada. Neste conceito estão incluídas todas as infraestruturas, equipamentos e materiais.

Atributos do tipo de objeto geográfico «ProductionSite»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| thematicId | Identificador de objeto temático. | ThematicIdentifier |  |
| geometry | Propriedade espacial do objeto geográfico. | GM_MultiSurface |  |
| sitePlan | Declaração descritiva sobre o projeto relativa à configuração e organização do sítio de produção. | DocumentCitation | voidable |
| name | Denominação oficial ou nome próprio ou convencional do sítio. | CharacterString | voidable |
| description | Declaração descritiva sobre o sítio. | CharacterString | voidable |
| status | Estado ou condição do sítio, no que se refere à ordem funcional e operacional, em que se encontra durante um período de tempo limitado ou alargado. | StatusType | voidable |

**8.2.5. Parcela de produção (ProductionPlot)**

Uma parte de terreno ou massa de água de uma instalação destinada a fins funcionais.

Atributos do tipo de objeto geográfico «ProductionPlot»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| thematicId | Identificador de objeto temático. | ThematicIdentifier |  |
| geometry | Propriedade espacial do objeto geográfico. | GM_Surface |  |
| status | Estado ou condição da parcela, no que se refere à ordem funcional e operacional, em que se encontra durante um período de tempo limitado ou alargado. | StatusType | voidable |

**8.2.6. Edifício de produção (ProductionBuilding)**

Construção artificial, parte da instalação de produção que é útil para acolher ou proteger o desenvolvimento de atividades.

Atributos do tipo de objeto geográfico «ProductionBuilding»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| thematicId | Identificador de objeto temático. | ThematicIdentifier |  |
| typeOfBuilding | Descrição classificada do edifício industrial e de produção. | TypeOfProductionBuildingValue | voidable |
| status | Estado ou condição do edifício industrial e de produção, no que se refere à ordem funcional e operacional, em que se encontra durante um período de tempo limitado ou alargado. | StatusType | voidable |
| geometry | Propriedade espacial do objeto geográfico. | GM_Object | voidable |

Associações do tipo de objeto geográfico «ProductionBuilding»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| building | Representação do edifício de produção num conjunto de dados Edifícios. | AbstractBuilding | voidable |

Restrições do tipo de objeto geográfico «Production Building»

Deve ser fornecida a geometria se a propriedade de edifício estiver vazia.

**8.3. Tipos de dados**

**8.3.1. Tipo de estatuto (StatusType)**

O estado ou condição de um componente técnico, no que se refere à ordem funcional e operacional, em que se encontra durante um período de tempo limitado ou alargado.

Atributos do tipo de dados «StatusType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| StatusType | Estado ou condição de um componente técnico que se refere a uma lista de valores potenciais predefinidos. | ConditionOfFacilityValue |  |
| description | Declaração descritiva sobre o estatuto declarado. | CharacterString | voidable |
| validFrom | Data de início da validade de um tipo de estatuto. | Date | voidable |
| validTo | Data de termo da validade de um tipo de estatuto. | Date | voidable |

**8.4. Listas de códigos**

**8.4.1. Técnica de redução da poluição (PollutionAbatementTechniqueValue)**

Métodos para reduzir a concentração de poluentes decorrente das emissões de um componente técnico, geralmente uma chaminé.

**8.4.2. Tipo de instalação técnica (InstallationTypeValue)**

Valores que denotam a função operativa a executar por uma instalação técnica.

**8.4.3. Tipo da parte da instalação técnica (InstallationPartTypeValue)**

Valores que denotam a função operativa a executar por uma parte da instalação técnica.

**8.4.4. Bacia hidrográfica (RiverBasinDistrictValue)**

Identificadores em código e/ou nomes atribuídos às bacias hidrográficas.

**8.4.5. Tipo de edifício de produção (TypeOfProductionBuildingValue)**

Classificação dos edifícios industriais e de produção.

**8.5. Camadas**

**Camadas da categoria temática de dados geográficos «Instalações Industriais e de Produção»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| PF.ProductionSite | Sítio industrial e de produção | ProductionSite |
| PF. <Valor de lista de códigos> (1) | <nome legível para as pessoas> | ProductionFacility |
| Exemplo: PF.Manufacturing | Exemplo: Indústrias transformadoras | (atividade: EconomicActivityValue) |
| PF.ProductionPlot | Parcela industrial e de produção | ProductionPlot |
| PF.ProductionInstallation | Instalação técnica industrial e de produção | ProductionInstallation |
| PF.ProductionInstallationPart | Parte de instalação técnica industrial e de produção | ProductionInstallationPart |
| PF.ProductionBuilding | Edifício industrial e de produção | ProductionBuilding |
| (1) <br> Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3 |  |  |

**9. INSTALAÇÕES AGRÍCOLAS E AQUÍCOLAS (AGRICULTURAL AND AQUACULTURE FACILITIES)**

**9.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) «Agricultura» (agriculture) : um conjunto de processos e atividades que consistem no cultivo de solos, na produção de culturas e na criação de animais. Inclui a colheita, a ordenha, a criação de animais e a detenção de animais para fins de produção. Nos termos do Regulamento (CE) n.º 73/2009, a manutenção dos terrenos em boas condições agrícolas e ambientais é considerada uma atividade agrícola.

(2) «Efetivo pecuário» (livestock) : animais criados e mantidos para fins de utilização ou exploração (abrangidos pela atividades definidas pelo códigos NACE A.1.4. e A.1.5).

(3) «Aquacultura» (aquaculture) : o conjunto de atividades e técnicas relacionadas com a produção, cultura e tratamento de peixes, moluscos, algas e outras espécies de recursos aquáticos (vegetais ou animais).

**9.2. Tipos de objetos geográficos**

São especificados os seguintes tipos de objetos geográficos para a categoria temática de dados geográficos «Instalações Agrícolas e Aquícolas»:

— Exploração

— Sítio

**9.2.1. Exploração (Holding)**

Toda a área e todas as infraestruturas nela integradas que abrangem o mesmo ou diferentes «sítios», sob o controlo de um operador para a realização de atividades agrícolas ou aquícolas.

Este tipo é um subtipo de «ActivityComplex».

Associações do tipo de objeto geográfico «Holding»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| contains | Sítios que fazem parte da exploração especificada. | Site |  |

Restrições do tipo de objeto geográfico «Holding»

Deve ser fornecido, pelo menos, um dos atributos de função do objeto geográfico Exploração utilizando a lista de códigos «EconomicActivityNACEValue» (para o atributo atividade do tipo de dados Função).

9.2.1.1. Sítio (Site)

Todo o terreno numa mesma ou numa diferente localização geográfica sob o controlo da gestão de uma exploração, abrangendo atividades, produtos e serviços. Neste conceito estão incluídas todas as infraestruturas, equipamentos e materiais.

Atributos do tipo de objeto geográfico «Site»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Geometria que define a extensão ou posição do sítio. | GM_Object |  |
| activity | Classificação da atividade económica do sítio, de acordo com a codificação da NACE, rev. 2.0. | EconomicActivityNACEValue |  |
| includesAnimal | Presença de animais no sítio. | FarmAnimalSpecies | voidable |

**9.3. Tipos de dados**

**9.3.1. Espécie de animais de criação (FarmAnimalSpecies)**

Identifica um animal ou grupo de animais (Efetivo Pecuário ou Aquacultura) da mesma espécie mantidos no sítio específico.

Atributos do tipo de dados «FarmAnimalSpecies»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| livestock | Presença de espécies pecuárias no sítio. | LivestockSpeciesValue | voidable |
| aquaculture | Presença de espécies aquícolas no sítio. | AquacultureSpeciesValue | voidable |

**9.4. Listas de códigos**

**9.4.1. Espécies pecuárias (LivestockSpeciesValue)**

Classificação das espécies pecuárias.

**9.4.2. Espécies aquícolas (AquacultureSpeciesValue)**

Classificação das espécies aquícolas.

**9.5. Camadas**

**Camadas da categoria temática de dados geográficos «Instalações Agrícolas e Aquícolas»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| AF. AgriculturalHolding | Exploração agrícola | Holding (objetos geográficos cujo atributo de atividade tem o valor = «A1 - Crop and animal production, hunting and related service activities» (da lista de códigos «EconomicActivityNACEValue») ou um valor mais restrito) |
| AF. AquacultureHolding | Exploração aquícola | Exploração (objetos geográficos cujo atributo de atividade tem o valor = «A3 - Fishing and aquaculture activities» (da lista de códigos «EconomicActivityNACEValue») ou um valor mais restrito) |
| AF.Site | Sítios agrícolas e aquícolas | Site |

**10. DISTRIBUIÇÃO DA POPULAÇÃO - DEMOGRAFIA (POPULATION DISTRIBUTION AND DEMOGRAPHY)**

**10.1. Tipos de objetos geográficos**

É especificado o seguinte tipo de objeto geográfico para a categoria temática de dados geográficos «Distribuição da População — Demografia: Distribuição Estatística».

**10.1.1. Distribuição estatística (StatisticalDistribution)**

Conjunto de medidas que descrevem a forma como um fenómeno se distribui numa parte do mundo 2D.

Atributos do tipo de objeto geográfico «StatisticalDistribution»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| areaOfDissemination | Parte do mundo 2D que a «StatisticalDataDistribution» descreve. | GM_Surface |  |
| universe | Quando a distribuição está relacionada com um subconjunto da população e não com a totalidade da população, a descrição literal da forma como este subconjunto foi definido. | PT_FreeText |  |
| domain | Parte dos conhecimentos estatísticos a que se referem os dados. | PT_FreeText |  |
| measure | Medida relacionada com a distribuição. | VariableValue |  |
| measurementMethod | Descrição do método de medição estatística. | StatisticsMeasurementMethodValue |  |
| measurementUnit | Unidade de medição. | UnitOfMeasure |  |
| notCountedProportion | Proporção da população da área de interesse que não é contabilizada em qualquer um dos seus componentes geográficos. | Number |  |
| periodOfMeasurement | Data ou período em que a observação foi efetuada e os dados recolhidos. | TM_Period |  |
| periodOfReference | Período em que os dados deveriam dar uma imagem da área de interesse. | TM_Period |  |
| periodOfValidity | Período em que os dados se mantêm relevantes. | TM_Period |  |
| beginLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| generalStatus | Estatuto da distribuição dos dados estatísticos. | StatisticalDataStatusValue |  |

Associações do tipo de objeto geográfico «StatisticalDistribution»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| value | Valores estatísticos que compõem a distribuição. | StatisticalValue |  |
| classification | Classificações adicionais utilizadas para dividir um valor total do fenómeno descrito. O objeto «StatisticalDistribution» fornecerá na realidade várias distribuições, uma para cada item da classificação utilizada. Quando não é fornecida nenhuma classificação, o valor estatístico é a população total. | Classification |  |

**10.2. Tipos de dados**

**10.2.1. Classificação (Classification)**

Classificação utilizada para uma distribuição estatística.

Atributos do tipo de dados «Classification»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| type | Tipo de classificação. | ClassificationTypeValue |  |

Associações do tipo de dados «Classification»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| item | Itens que compõem a classificação. | ClassificationItem |  |

**10.2.2. Item da classificação (ClassificationItem)**

Um item que compõe uma classificação.

Atributos do tipo de dados «ClassificationItem»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| type | Tipo de item da classificação. | ClassificationItemTypeValue |  |

**10.2.3. Valor estatístico (StatisticalValue)**

As componentes do datum da distribuição.

Atributos do tipo de dados «StatisticalValue»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| value | Valor para o elemento de datum. | Number |  |
| specialValue | Sequência convencional quando não pode ser fornecido um valor para o elemento de datum: valor em falta, valor escondido por questões de confidencialidade. | SpecialValue |  |
| conventionallyLocatedProportion | Proporção da população contabilizada no elemento de datum, mas que não pode ser na realidade fisicamente localizada em qualquer parte da área de interesse. | Number |  |
| approximatelyLocatedPopulationProportion | Proporção da contagem da população que não segue as regras comuns relativas a localização. A «população» pode ser: pessoas se estão contabilizadas pessoas, habitações se a «StatisticalDatadistribution» se referir a habitações, etc. | Number |  |
| comment | Comentário livre sobre o valor. | PT_FreeText |  |
| flags | Conjunto de comentários sobre os dados, codificados com um caráter. | PT_FreeText |  |
| periodOfMeasurement | Período de recolha do valor estatístico. Este período prevalece sobre o período especificado na distribuição estatística associada. | TM_Period | voidable |
| status | Estatuto dos dados estatísticos. | StatisticalDataStatusValue |  |

Associações do tipo de dados «StatisticalValue»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| dimensions | Parte do mundo a que se refere o elemento de datum. As dimensões contêm uma descrição da localização geográfica (dimensão 2D) juntamente com possíveis dimensões adicionais quando são produzidas contagens da população simultaneamente para diferentes características individuais. | Dimensions |  |

Restrições do tipo de dados «StatisticalValue»

Deve ser fornecido o valor ou o atributo «specialValue».

**10.2.4. Dimensões (Dimensions)**

Identificação daquilo a que se refere o elemento de datum em termos de localização geográfica ou de características individuais.

Associações do tipo de dados «Dimensions»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| spatial | Dimensão espacial do valor estatístico. | StatisticalUnit |  |
| thematic | Dimensão temática do valor estatístico. | ClassificationItem |  |

**10.3. Listas de códigos**

**10.3.1. Tipo de classificação (ClassificationTypeValue)**

Valores dos códigos para os tipos de classificação.

**10.3.2. Tipo de item de classificação (ClassificationItemTypeValue)**

Valores dos códigos para os itens de classificação.

Esta lista de códigos inclui os valores constantes das listas de códigos seguintes ou de outras listas de códigos definidas pelos fornecedores dos dados:

— Idade por intervalos de cinco anos (AgeBy5YearsValue): Valores de código para itens de classificação por intervalos de idade de cinco anos.

— Idade por ano (AgeByYearValue): Valores de código para itens de classificação por idade ano a ano, compreendendo um valor para cada intervalo de um ano. O primeiro valor deve ser «0-1», com a etiqueta «0-1» e a definição «0 a menos de 1 ano», e o último valor deve ser «100+», com a etiqueta «100+» e a definição «100 anos ou mais».

— Código NACE (NACECodeValue): Classificação das atividades económicas de acordo com a Classificação NACE do Eurostat, estabelecida no Regulamento (CE) n.º 1893/2006 do Parlamento Europeu e do Conselho, e valores mais restritos definidos pelos fornecedores dos dados.

— Sexo (GenderValue): Sexo de uma pessoa ou grupo de pessoas, conforme especificado no ponto 4.7 do anexo I.

**10.3.3. Variável (VariableValue)**

Valores dos códigos para nomes de variáveis.

**10.3.4. Método de medição estatística (StatisticsMeasurementMethodValue)**

Valores dos códigos para o método de medição estatística.

**10.3.5. Estatuto dos dados estatísticos (StatisticalDataStatusValue)**

Valores dos códigos para o estatuto.

**10.3.6. Valor especial (SpecialValue)**

Valores dos códigos para valores especiais.

**10.4 Camadas**

Não estão definidas camadas para a categoria temática de dados geográficos «Distribuição da População e Demografia».

**11. ZONAS DE GESTÃO/RESTRIÇÃO/REGULAMENTAÇÃO E UNIDADES DE REPORTE (AREA MANAGEMENT/RESTRICTION/REGULATION ZONES AND REPORTING UNITS)**

**11.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) «Gerir» (manage) : planear, executar, monitorizar e controlar atividades para atingir objetivos ambientais específicos juridicamente definidos.

(2) «Restringir» (restrict) : proibir ou limitar determinadas atividades, para que estas só possam ser realizadas dentro de limites e/ou períodos de tempo específicos, a fim de atingir um determinado objetivo de acordo com responsabilidades ou obrigações juridicamente definidas.

(3) «Regulamentar» (regulate) : monitorizar e controlar determinadas atividades (a fim de as permitir, promover, proibir ou restringir) com vista a atingir objetivos ambientais juridicamente definidos. Uma atividade regulamentada pode exigir que, se o estado ambiental estiver degradado, devem então ser executadas ações especiais para fins de recuperação do estatuto de bom estado ambiental.

(4) «Comunicar informações» (report) : avaliar a eficácia das políticas ambientais e publicar dados e informações (ou seja, dados geográficos, observações, estatísticas, indicadores) que podem ser utilizados para avaliar os progressos realizados no sentido de manter ou melhorar o bom estado ambiental e de atingir os objetivos das políticas.

(5) «Unidade de reporte» (reporting unit) : um objeto geográfico que fornece a referência espacial para quaisquer dados não-espaciais trocados ao abrigo das obrigações de comunicação de informações ambientais.

(6) «Instrumento jurídico» (legal instrument) : um documento que especifica as obrigações jurídicas, nomeadamente, mas não exclusivamente, as convenções internacionais, a legislação e atos jurídicos ou a regulamentação de execução a qualquer nível administrativo.

(7) «Gestão integrada da zona costeira» (integrated coastal zone management) : um processo dinâmico para a gestão e utilização sustentáveis das zonas costeiras, que tem simultaneamente em conta a fragilidade dos ecossistemas e paisagens costeiros, a diversidade das atividades e utilizações, as suas interações, a orientação marítima de determinadas atividades e utilizações e o respetivo impacto nas componentes marinha e terrestre.

(8) «Clima» (climate) : a descrição estatística em termos da média e da variabilidade de quantidades relevantes durante um período de tempo que pode ir de meses a milhares ou milhões de anos. Estas quantidades são mais frequentemente variáveis de superfície, como a temperatura, a precipitação e o vento.

**11.2. Tipos de objetos geográficos**

É especificado o seguinte tipo de objeto geográfico para a categoria temática de dados geográficos «Zonas de Gestão/Restrição/Regulamentação» e unidades de reporte: zona de restrição da gestão ou de regulamentação.

**11.2.1. Zona de restrição da gestão ou de regulamentação (ManagementRestrictionOrRegulationZone)**

Área gerida, restringida ou regulamentada em conformidade com um requisito jurídico relacionado com uma política ambiental ou uma política ou atividade que possa ter um impacto no ambiente a qualquer nível da administração (internacional, europeu, nacional, regional e local).

Atributos do tipo de objeto geográfico «ManagementRestrictionOrRegulationZone»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| thematicId | Identificador descritivo de objeto único aplicado a objetos geográficos numa categoria temática de informação definida. | ThematicIdentifier | voidable |
| name | Topónimo que é utilizado para identificar a zona de gestão, restrição ou regulamentação no mundo real. Fornece uma «chave» para associar implicitamente diferentes representações do objeto. | GeographicalName | voidable |
| geometry | Geometria que representa a extensão geográfica do objeto geográfico. | GM_Object |  |
| zoneType | Classificação de alto nível que define o tipo de zona de gestão, restrição ou regulamentação. | ZoneTypeCode |  |
| specialisedZoneType | Valor de classificação adicional que classifica de forma mais especializada o tipo de zona de gestão, regulamentação ou restrição relevante para o domínio. | SpecialisedZoneTypeCode | voidable |
| environmentalDomain | Classificação do ou dos domínios ambientais relativamente aos quais, através da criação da zona, serão atingidos determinados objetivos ambientais. | EnvironmentalDomain |  |
| designationPeriod | Período de tempo que define quando a zona de gestão, restrição ou regulamentação foi legalmente designada ou passou a existir no mundo real. | TM_Period | voidable |
| competentAuthority | Descrição da ou das organizações responsáveis pelas medidas ou atividades de gestão, restrição ou regulamentação dentro da zona. | RelatedParty | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

Associações do tipo de objeto geográfico «ManagementRestrictionOrRegulationZone»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| legalBasis | Referência ou citação do instrumento ou documento jurídico que exigiu o estabelecimento da zona. | LegislationCitation | voidable |
| relatedZone | Referência a uma zona de gestão, regulamentação ou restrição relacionada. | ManagementRestrictionOrRegulationZone | voidable |
| plan | Referência ou citação de um plano (plano de gestão ou de ação) que descreve os objetivos e medidas ambientais que devem ser realizados na zona para fins de proteção do ambiente. | DocumentCitation | voidable |

Restrições do tipo de objeto geográfico «ManagementRestrictionOrRegulationZone»

Deve ser fornecido, pelo menos, o instrumento jurídico mais específico que exigiu o estabelecimento da zona utilizando a associação «legalBasis».

O atributo «role» de «competentAuthority» deve ter o valor «authority».

**11.3. Listas de códigos**

**11.3.1. Código do tipo de zona (ZoneTypeCode)**

Classificação de alto nível que define o tipo de zona de gestão, restrição ou regulamentação.

**11.3.2. Código de tipo de zona especializado (SpecialisedZoneTypeCode)**

Valor de classificação adicional que define o tipo especializado de zona.

**11.3.3. Domínio ambiental (EnvironmentalDomain)**

Domínio ambiental relativamente ao qual podem ser definidos objetivos ambientais.

**11.4. Requisitos específicos de categorias temáticas**

**11.4.1. Zonas de gestão, restrição ou regulamentação**

(1) Quando a geometria do objeto geográfico é derivada de outro objeto geográfico, as geometrias dos dois objetos devem ser coerentes.

(2) Se as geometrias dos objetos geográficos num conjunto de dados «ManagementRestrictionOrRegulationZone» são derivadas das geometrias de objetos geográficos noutro conjunto de dados, então este conjunto de dados fonte (incluindo a sua versão) deve ser descrito como parte do elemento de metadados «Histórico».

(3) Os fornecedores de dados devem incluir as seguintes palavras-chave, para além das palavras-chave obrigatórias definidas no Regulamento (CE) n.º 1205/2008:

(a) Uma ou mais palavras-chave que descrevam a classificação de alto nível do ou dos tipos de zonas incluídos no conjunto de dados, tal como definido na lista de códigos «ZoneTypeCode».

(b) Uma ou mais palavras-chave que descrevam o ou os números dos documentos oficiais do ou dos instrumentos jurídicos em que a ou as zonas incluídas no conjunto de dados estão estabelecidas. No que diz respeito à legislação da União, deve ser utilizado o número CELEX.

**11.4.2. Unidades de reporte**

(1) Os objetos geográficos que funcionam como unidades de reporte devem ser definidos e disponibilizados de acordo com os requisitos da ou das respetivas categorias temáticas de dados geográficos INSPIRE.

(2) Quando os dados ambientais comunicados para estabelecer uma referência geográfica se referem a entidades do mundo real que são disponibilizadas como objetos geográficos em conformidade com este regulamento, os dados comunicados devem incluir uma referência explícita a esses objetos geográficos.

**11.4.3. Requisitos transversais**

(1) Caso uma área tenha sido estabelecida exclusivamente para gerir, regular e restringir atividades para fins de conservação da natureza, da biodiversidade e do património cultural, a área deve ser disponibilizada como um objeto geográfico «ProtectedSite». Caso uma zona tenha sido estabelecida para atingir múltiplos objetivos, incluindo a conservação da natureza, da biodiversidade e do património cultural, a zona deve ser disponibilizada como um objeto geográfico «ManagementRestrictionOrRegulationZone».

(2) Nos casos em que tenha sido estabelecida uma zona para regulamentar o uso do solo planeado e definida no âmbito de um plano de ordenamento do território juridicamente vinculativo, essa zona fica abrangida pela categoria temática «Uso do Solo» e deve ser codificada como «SupplementaryRegulation». No entanto, se a zona tiver sido estabelecida por via legislativa, mas não tiver sido definida no âmbito de um plano de ordenamento do território juridicamente vinculativo, então a zona deve ser codificada como uma «ManagementRestrictionOrRegulationZone».

**11.5 Camadas**

**Camadas para a categoria temática de dados geográficos «Zonas de Gestão/Restrição/Regulamentação e Unidades de Reporte»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| AM.<Valor de lista de códigos> (1) | <nome legível para as pessoas> | ManagementRestrictionOrRegulationZone (zoneType: ZoneTypeCode) |
| Exemplo: AM.AirQualityManagementZone | Exemplo: Zona de gestão da qualidade do ar |  |
| (1) <br> Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3 |  |  |

**12. ZONAS DE RISCO NATURAL (NATURAL RISK ZONES)**

**12.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) «Risco» (risk) : a combinação das consequências de um evento (perigo) e da possibilidade/probabilidade associada da sua ocorrência, em conformidade com a norma ISO/IEC 31010:2009.

(2) «Perigo» (hazard) : um fenómeno, substância, atividade humana ou situação perigoso suscetível de provocar perda de vidas, ferimentos ou outros impactos na saúde, danos patrimoniais ou perda dos meios de subsistência e serviços, perturbações económicas e sociais ou danos para o ambiente.

(3) «Exposição» (exposure) : as pessoas, a propriedade, os sistemas ou outros elementos presentes em zonas de perigo que estão assim sujeitas a potenciais perdas.

(4) «Vulnerabilidade» (vulnerability) : as características e circunstâncias de uma comunidade, sistema ou bem que os tornam sensíveis aos efeitos prejudiciais de um perigo.

**12.2. Tipos de objetos geográficos**

São especificados os seguintes tipos de objetos geográficos para a categoria temática de dados geográficos «Zonas de Risco Natural»:

— Elemento exposto abstrato

— Área de perigo abstrata

— Evento observado abstrato

— Zona de risco abstrata

— Cobertura do elemento exposto

— Elementos expostos

— Área de perigo

— Cobertura do perigo

— Cobertura do evento observado

— Evento observado

— Cobertura do risco

— Zona de risco

**12.2.1. Elemento abstrato exposto (AbstractExposedElement)**

As pessoas, propriedades, sistemas ou outros elementos presentes em zonas de perigo que estão assim sujeitos a potenciais perdas.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «AbstractExposedElement»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| beginLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | Momento em que o elemento exposto começou a existir no mundo real. | DateTime | voidable |
| validTo | Momento em que o elemento exposto deixou de existir no mundo real. | DateTime | voidable |

Associações do tipo de objeto geográfico «AbstractExposedElement»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| sourceOfSpatialRepresentation | Objeto fonte que é utilizado para representar o elemento exposto. | AbstractFeature | voidable |

Restrições do tipo de objeto geográfico «AbstractExposedElement»

Se a associação «sourceOfSpatialRepresentation» estiver vazia, deve ser fornecida a geometria do objeto geográfico «AbstractExposedElement».

**12.2.2. Área de perigo abstrata (AbstractHazardArea)**

Uma área afetada por um perigo natural.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «AbstractHazardArea»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| determinationMethod | Especifica se o resultado da área de perigo é delimitado após modelização ou determinado após interpretação. | DeterminationMethodValue |  |
| endLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| typeOfHazard | Uma classificação genérica e uma classificação específica do tipo de perigo natural. | NaturalHazardClassification |  |
| validityPeriod | Escala temporal a que é aplicável o modelo. | TM_Period | voidable |

Associações do tipo de objeto geográfico «AbstractHazardArea»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| source | O evento observado que desencadeou a modelização de uma área de perigo. | AbstractObservedEvent | voidable |

**12.2.3. Evento observado abstrato (AbstractObservedEvent)**

Um fenómeno natural relevante para o estudo dos perigos naturais que ocorreu ou está a ocorrer e que foi observado.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «AbstractObservedEvent»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| nameOfEvent | Nome comum do evento observado. | CharacterString | voidable |
| typeOfHazard | Uma classificação genérica e uma classificação específica do tipo de perigo. | NaturalHazardClassification |  |
| validFrom | Momento em que o evento observado começou a existir no mundo real. | DateTime | voidable |
| validTo | Momento em que o evento observado deixou de existir no mundo real. | DateTime | voidable |

Associações do tipo de objeto geográfico «AbstractObservedEvent»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| isMonitoredBy | Programa ambiental que monitoriza o evento observado | EnvironmentalMonitoringActivity | voidable |

**12.2.4. Zona de risco abstrata (AbstractRiskZone)**

Uma zona de risco é a extensão geográfica de uma combinação das consequências de um evento (perigo) e da probabilidade/possibilidade associada da sua ocorrência.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «AbstractRiskZone»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| sourceOfRisk | Uma classificação genérica e uma classificação específica do tipo de perigo que é a fonte do risco. | NaturalHazardClassification |  |
| validityPeriod | Escala temporal futura finita em que o modelo é aplicável. | TM_Period | voidable |

Associações do tipo de objeto geográfico «AbstractRiskZone»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| exposedElement | Elemento que se encontra dentro de uma área perigosa | AbstractExposedElement | voidable |
| source | O perigo que é considerado para a criação do objeto de zona de risco. | AbstractHazardArea | voidable |

**12.2.5. Cobertura do elemento exposto (ExposedElementCoverage)**

Uma cobertura que representa informação contínua sobre elementos expostos.

Este tipo é um subtipo de «AbstractExposedElement».

Este tipo é um subtipo de «CoverageByDomainAndRange».

Atributos do tipo de objeto geográfico «ExposedElementCoverage»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| typeOfElement | Classificação do elemento exposto. | ExposedElementClassification | voidable |

Restrições do tipo de objeto geográfico «ExposedElementCoverage»

O conjunto de gama de valores deve ser o nível, ou a intensidade, da avaliação da vulnerabilidade.

O domínio deve ser uma quadrícula retificada ou uma quadrícula referenciável.

**12.2.6. Elemento exposto (ExposedElement)**

Objeto geográfico discreto que representa um elemento exposto.

Este tipo é um subtipo de «AbstractExposedElement».

Atributos do tipo de objeto geográfico «ExposedElement»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Representação geométrica do elemento exposto. | GM_Object |  |
| assessmentOfVulnerability | Avaliação da vulnerabilidade do elemento exposto. | VulnerabilityAssessment | voidable |

**12.2.7. Área de perigo (HazardArea)**

Objetos geográficos discretos que representam um perigo natural.

Este tipo é um subtipo de «AbstractHazardArea».

Atributos do tipo de objeto geográfico «HazardArea»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Representação geométrica da extensão geográfica abrangida pela área de perigo. | GM_Surface |  |
| likelihoodOfOccurrence | Conceito geral relativo à possibilidade de ocorrência de um evento. | LikelihoodOfOccurrence | voidable |
| magnitudeOrIntensity | Expressão da magnitude ou da intensidade de um fenómeno. | LevelOrIntensity | voidable |

**12.2.8. Cobertura do perigo (HazardCoverage)**

Uma cobertura que representa informação contínua sobre o tipo de perigo natural.

Este tipo é um subtipo de «AbstractHazardArea».

Este tipo é um subtipo de «CoverageByDomainAndRange».

Restrições do tipo de objeto geográfico «HazardCoverage»

O conjunto de gama de valores deve ser descrito através da magnitude ou intensidade, ou da possibilidade de ocorrência.

O domínio deve ser uma quadrícula retificada ou uma quadrícula referenciável.

**12.2.9. Cobertura do evento observado (ObservedEventCoverage)**

Uma cobertura que representa informação contínua sobre eventos observados.

Este tipo é um subtipo de «AbstractObservedEvent».

Este tipo é um subtipo de «CoverageByDomainAndRange».

Restrições do tipo de objeto geográfico «ObservedEventCoverage»

O conjunto de gama de valores deve ser descrito através da magnitude ou intensidade, ou da possibilidade de ocorrência.

O domínio deve ser uma quadrícula retificada ou uma quadrícula referenciável.

**12.2.10. Evento observado (ObservedEvent)**

Objetos geográficos discretos que representam um fenómeno natural relevante para o estudo dos perigos naturais que ocorreram ou estão a ocorrer e que foi observado.

Este tipo é um subtipo de «AbstractObservedEvent».

Atributos do tipo de objeto geográfico «ObservedEvent»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Representação geométrica da extensão geográfica abrangida pelo evento observado. | GM_Object |  |
| magnitudeOrIntensity | Expressão da magnitude ou da intensidade de um fenómeno. | LevelOrIntensity | voidable |

**12.2.11. Cobertura do risco (RiskCoverage)**

Uma cobertura que representa informação contínua sobre a intensidade ou o nível do risco.

Este tipo é um subtipo de «AbstractRiskZone».

Este tipo é um subtipo de «CoverageByDomainAndRange».

Restrições do tipo de objeto geográfico «RiskCoverage»

O conjunto da gama de valores deve ser descrito por nível ou intensidade.

O domínio deve ser uma quadrícula retificada ou uma quadrícula referenciável.

**12.2.12. Zona de risco (RiskZone)**

Objetos geográficos discretos que representam a extensão geográfica de uma combinação das consequências de um evento (perigo) e da probabilidade/possibilidade associada da sua ocorrência.

Este tipo é um subtipo de «AbstractRiskZone».

Atributos do tipo de objeto geográfico «RiskZone»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Representação geométrica da extensão geográfica abrangida por esta zona de risco. | GM_Surface |  |
| levelOfRisk | O nível de risco é uma avaliação da combinação das consequências de um evento (perigo) com a probabilidade/possibilidade associada da ocorrência do evento. | LevelOrIntensity | voidable |

**12.3. Tipos de dados**

**12.3.1. Classificação do elemento exposto (ExposedElementClassification)**

Esta classe fornece elementos de informação sobre a natureza do elemento exposto que é relevante para a análise dos riscos.

Atributos do tipo de dados «ExposedElementClassification»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| exposedElementCategory | Classificação genérica dos tipos de elementos que estão expostos a um risco. | ExposedElementCategoryValue |  |
| specificExposedElementType | Denominação adicional do elemento exposto de acordo com uma nomenclatura que é específica do conjunto de dados. | SpecificExposedElementTypeValue | voidable |

**12.3.2. Nível ou intensidade (LevelOrIntensity)**

Avaliação quantitativa ou qualitativa do risco, perigo ou vulnerabilidade.

Atributos do tipo de dados «LevelOrIntensity»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| qualitativeValue | Avaliação qualitativa do nível ou da intensidade. | CharacterString | voidable |
| quantitativeValue | Avaliação quantitativa do nível ou da intensidade. | Measure | voidable |
| assessmentMethod | Citação do método utilizado para exprimir o nível ou a intensidade. | DocumentCitation | voidable |

Restrições do tipo de dados «LevelOrIntensity»

Deve ser fornecido o valor qualitativo ou o valor quantitativo.

**12.3.3. Possibilidade de ocorrência (LikelihoodOfOccurrence)**

O conceito de possibilidade é um conceito geral relativo à hipótese de ocorrência de um evento.

Atributos do tipo de dados «LikelihoodOfOccurrence»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| qualitativeLikelihood | Avaliação qualitativa da possibilidade de ocorrência de um perigo. | CharacterString | voidable |
| quantitativeLikelihood | Frequência da ocorrência ou período de recorrência de um fenómeno de perigo. | QuantitativeLikelihood | voidable |
| assessmentMethod | Citação do método utilizado para exprimir a possibilidade. | DocumentCitation | voidable |

Restrições do tipo de dados «LikelihoodOfOccurrence»

Deve ser fornecida a possibilidade qualitativa ou a possibilidade quantitativa.

**12.3.4. Classificação do perigo natural (NaturalHazardClassification)**

Esta classe fornece um elemento de informação sobre a natureza do perigo natural, bem como sobre o tipo de perigo que é a fonte de risco.

Atributos do tipo de dados «NaturalHazardClassification»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| hazardCategory | Classificação genérica de tipos de perigos naturais. | NaturalHazardCategoryValue |  |
| specificHazardType | Classificação adicional do perigo natural que indica mais pormenorizadamente o tipo de perigo, de acordo com uma nomenclatura específica do conjunto de dados em causa. | SpecificHazardTypeValue | voidable |

**12.3.5. Possibilidade quantitativa (QuantitativeLikelihood)**

Frequência da ocorrência ou período de recorrência de um fenómeno de perigo.

Atributos do tipo de dados «QuantitativeLikelihood»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| probabilityOfOccurrence | Probabilidade de ocorrência de um evento de perigo, expresso como um valor entre 0 e 1. | Probability | voidable |
| returnPeriod | Intervalo de tempo médio a longo prazo ou número de anos durante o qual um evento será igualado ou excedido. | Number | voidable |

**12.3.6. Avaliação da vulnerabilidade (VulnerabilityAssessment)**

Avaliação da vulnerabilidade.

Atributos do tipo de dados «VulnerabilityAssessment»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| sourceOfVulnerability | Tipo de perigo cuja vulnerabilidade é avaliada. | NaturalHazardClassification |  |
| levelOfVulnerability | Nível de vulnerabilidade. | LevelOrIntensity | voidable |
| magnitudeOrIntensityOfHazard | Expressão da magnitude ou da intensidade de um fenómeno. | LevelOrIntensity | voidable |
| typeOfElement | Classificação do elemento exposto. | ExposedElementClassification | voidable |

—————

**12.5. Listas de códigos**

**12.5.1. Categoria do elemento exposto (ExposedElementCategoryValue)**

Classificação do elemento exposto.

**12.5.2. Categoria do perigo natural (NaturalHazardCategoryValue)**

Classificação genérica de tipos de perigos naturais.

**12.5.3. Tipo específico do elemento exposto (SpecificExposedElementTypeValue)**

Uma denominação adicional dos elementos expostos.

**12.5.4. Tipo específico de perigo (SpecificHazardTypeValue)**

Classificação adicional do perigo natural.

**12.5.5. Método de determinação (DeterminationMethodValue)**

Uma lista de códigos para descrever o método utilizado para definir a área de perigo ou de risco.

**12.6. Requisitos específicos de categorias temáticas**

(1) Quando uma «RiskZone» está associada a uma «HazardArea», a «RiskZone» e a «HazardArea» devem sobrepor-se.

(2) Quando uma «RiskZone» está associada a um «ExposedElement», o «ExposedElement» deve sobrepor-se à «RiskZone».

**12.7. Camadas**

**Camadas para a categoria temática de dados geográficos «Zonas de Risco Natural»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| NZ.RiskZone | Zonas de risco | RiskZone |
| NZ.RiskZoneCoverage | Cobertura de zonas de risco | RiskZoneCoverage |
| NZ. <Valor de lista de códigos> (1) | <nome legível para as pessoas> | HazardArea, HazardAreaCoverage (typeOfHazard: NaturalHazardCategoryValue) |
| Exemplo: NZ.Landslide | Exemplo: Deslizamentos de terras |  |
| NZ. <Valor de lista de códigos> (2) | <nome legível para as pessoas> | ObservedEvent, ObservedEventCoverage (typeOfHazard: NaturalHazardCategoryValue) |
| Exemplo: NZ.Flood | Exemplo: Inundações |  |
| NZ.ExposedElements | Elementos expostos | ExposedElements |
| NZ.ExposedElementCoverage | Cobertura do elemento exposto | ExposedElementCoverage |
| (1) <br> Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3 <br> (2) <br> Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3 |  |  |

**13. CONDIÇÕES ATMOSFÉRICAS E CARACTERÍSTICAS GEOMETEOROLÓGICAS (ATMOSPHERIC CONDITIONS AND METEOROLOGICAL GEOGRAPHICAL FEATURES)**

**13.1. Estrutura da categoria temática de dados geográficos «Condições Atmosféricas e Características Geometeorológicas»**

Os tipos especificados para as categorias temáticas de dados geográficos «Condições Atmosféricas» e «Características Geometeorológicas» estão estruturados nos seguintes pacotes:

— Condições atmosféricas e características geometeorológicas

— Observações especializadas (Specialised Observations) (especificadas no ponto 7.4 do anexo I)

— Processos (Processes) (especificados no ponto 7.2 do anexo I)

— Propriedades observáveis (Observable Properties) (especificadas no ponto 7.3 do anexo I)

— Referências de observações (Observation References) (especificadas no ponto 7.1 do anexo I)

**13.2. Condições atmosféricas e características geometeorológicas**

**13.2.1. Listas de códigos**

13.2.1.1. Componente de referência da qualidade do ar da UE (EU_AirQualityReferenceComponentValue)

Definições de fenómenos relativos à qualidade do ar no contexto da comunicação de informações ao abrigo da legislação da União.

13.2.1.2. Quadro 4.2 de Códigos e Marcadores do formato GRIB da Organização Meteorológica Mundial (GRIB_CodeTable4_2Value)

Definições de fenómenos observados em meteorologia.

**13.3. Requisitos específicos de categorias temáticas**

(1) Em derrogação aos requisitos estabelecidos no anexo II, ponto 2.2, os dados matriciais relacionados com as categorias temáticas «Condições Atmosféricas» e «Características Geometeorológicas» podem ser disponibilizados utilizando qualquer quadrícula adequada.

(2) Os dados relativos às categorias temáticas «Condições Atmosféricas» ou «Características Geometeorológicas» devem ser disponibilizados utilizando os tipos definidos no pacote «Observações Especializadas» no anexo I, o tipo de objeto geográfico «OM_Observation» ou subtipos deste.

(3) A propriedade observada de uma «OM_Observation» deve ser identificada por um identificador dos vocabulários da Componente de Referência da Qualidade do Ar da UE (EU Air Quality Reference Component), do Quadro 4.2 dos Códigos e Marcadores do formato GRIB da Organização Meteorológica Mundial (WMO GRIB Code & Flags Table 4.2), dos Nomes Padronizados de Previsões e Fenómenos Climáticos (Climate and Forecast Standard Names) ou de qualquer outro vocabulário adequado.

**13.4. Camadas**

Não são especificadas camadas para as categorias temáticas «Condições Atmosféricas» e «Características Geometeorológicas».

**14. CARACTERÍSTICAS OCEANOGRÁFICAS (OCEANOGRAPHIC GEOGRAPHICAL FEATURES)**

**14.1 Estrutura da categoria temática de dados geográficos «Características Oceanográficas»**

Os tipos especificados para a categoria temática de dados geográficos «Características Oceanográficas» estão estruturados nos seguintes pacotes:

— Características oceanográficas (Oceanographic Geographical Features)

— Observações especializadas (Specialised Observations) (especificadas no ponto 0 do anexo I)

— Processos (Processes) (especificados no ponto 0 do anexo I)

— Propriedades observáveis (Observable Properties) (especificadas no ponto 0 do anexo I)

— Referências de observações (Observation References) (especificadas no ponto 0 do anexo I)

**14.2. Características oceanográficas**

**14.2.1. Listas de códigos**

14.2.1.1. Utilização do parâmetro BODC P01 (BODC_P01ParameterUsageValue)

Definições de fenómenos observados em oceanografia.

**14.3. Requisitos específicos de categorias temáticas**

(1) Em derrogação aos requisitos estabelecidos no anexo II, ponto 2.2, os dados matriciais relacionados com a categoria temática «Características Oceanográficas» podem ser disponibilizados utilizando qualquer quadrícula adequada.

(2) Os dados relacionados com a categoria temática «Características Oceanográficas» devem ser disponibilizados utilizando os seguintes tipos definidos no pacote «Observações Especializadas» no anexo I: «PointObservation», «PointTimeSeriesObservation», «MultiPointObservation», «GridObservation», «GridSeriesObservation», «PointObservationCollection».

(3) A propriedade observada de uma «OM_Observation» deve ser identificada por um identificador dos vocabulários Utilização do Parâmetro BODC P01 ou Nomes Padronizados de Previsões e Fenómenos Climáticos.

**14.4. Camadas**

**Camadas para a categoria temática de dados geográficos «Características oceanográficas»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| OF.PointObservation | Observação oceanográfica de pontos | PointObservation |
| OF.PointTimeSeriesObservation | Observação oceanográfica de séries temporais multipontos | PointTimeSeriesObservation |
| OF.MultiPointObservation | Observação oceanográfica multipontos | MultiPointObservation |
| OF.GridObservation | Observação oceanográfica em quadrícula | GridObservation |
| OF.GridSeriesObservation | Observação oceanográfica de séries em quadrícula | GridSeriesObservation |

**15. REGIÕES MARINHAS (SEA REGIONS)**

**15.1 Tipos de objetos geográficos**

São especificados os seguintes tipos de objetos geográficos para a categoria temática de dados geográficos «Regiões Marinhas»:

— Área marinha

— Mar

— Zona marinha de circulação

— Área intertidal

— Linha da margem

— Segmento da margem

— Linha da costa

— Contorno marinho

— Camada marinha

— Área do fundo marinho

— Área da superfície do mar

**15.1.1. Área marinha (SeaArea)**

Uma área de mar definida em função das suas características físicas e químicas. Pode ter múltiplas geometrias (extensão) para representar diferentes estados das marés.

Este tipo é um subtipo de «HydroObject».

Atributos do tipo de objeto geográfico «SeaArea»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| seaAreaType | Tipo de área marinha de acordo com as classificações na lista de códigos «SeaAreaTypeClassificationValue», por exemplo, estuário. | SeaAreaTypeClassificationValue |  |
| extent | Extensão da área marinha com um determinado estado das marés. | MarineExtent |  |
| parameterValue | Valor de um parâmetro atribuído à área marinha. Por exemplo, temperatura média anual da superfície do mar = 12 graus Celsius. | ParameterValuePair |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

Associações do tipo de objeto geográfico «SeaArea»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| subArea | As áreas marinhas podem ser compostas por subáreas, por exemplo, uma área marinha que defina todos os mares europeus poderia ser uma agregação de múltiplas áreas marinhas (Mar do Norte, Mar Mediterrâneo, etc.). | SeaArea |  |

**15.1.2. Mar (Sea)**

Extensão de mar na maré alta (meanHighWater).

Este tipo é um subtipo de «SeaArea».

Restrições do tipo de objeto geográfico «Sea»

«Sea» (mar) é definido ao nível médio da maré alta. Esta restrição pode não ser observada se não houver uma variação significativa no nível de água das marés.

Os tipos de objetos geográficos do tipo «Sea» devem ter apenas um valor para o atributo «extent».

**15.1.3. Zona marinha de circulação (MarineCirculationZone)**

Uma área marinha definida pelos seus padrões de circulação física e química. Geralmente utilizada para fins de gestão e comunicação de informações sobre o meio marinho ou para fins de classificação ambiental do meio marinho.

Este tipo é um subtipo de «SeaArea».

Atributos do tipo de objeto geográfico «MarineCirculationZone»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| zoneType | Tipo de zona marinha de circulação, por exemplo, «sedimentCell». | ZoneTypeValue |  |

Restrições do tipo de objeto geográfico «MarineCirculationZone»

Os tipos de objetos geográficos do tipo MarineCirculationZone devem ter apenas um valor para o atributo «extent».

**15.1.4. Área intertidal (InterTidalArea)**

A parte do meio marinho que está exposta (não coberta de água) durante um ciclo de marés normal; definida como a diferença entre qualquer nível de maré alta e de maré baixa.

Este tipo é um subtipo de «Shore».

Atributos do tipo de objeto geográfico «InterTidalArea»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| lowWaterLevel | O nível de maré baixa que foi utilizado para definir o limite inferior da área intertidal, por exemplo, «meanLowWater». | WaterLevelValue |  |
| highWaterLevel | O nível de maré alta que foi utilizado para definir o limite superior da área intertidal, por exemplo, «meanHighWater». | WaterLevelValue |  |

**15.1.5. Linha da margem (Shoreline)**

Qualquer fronteira entre uma área marinha e terra.

Este tipo é um subtipo de «HydroObject».

Atributos do tipo de objeto geográfico «Shoreline»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| segment | Secção da linha da margem. | ShoreSegment |  |
| waterLevel | Nível da água utilizado para definir esta linha da margem (por exemplo, meanHighWater). | WaterLevelValue | voidable |

—————

**15.1.7. Linha da costa (Coastline)**

Um caso especial de uma linha da margem definida como a linha da margem no nível médio da maré alta (Mean High Water - MHW). Quando não há uma variação significativa no nível do mar, pode ser utilizado o nível médio do mar (Mean Sea Level - MSL) como substituto de MHW.

Este tipo é um subtipo de «Shoreline».

Restrições do tipo de objeto geográfico «Coastline»

A linha da costa é um caso especial de linha da margem no nível médio da maré alta (Mean High Water Level - MHW). A linha da costa é a fronteira entre a terra e o mar a utilizar para aplicações de visualização e pesquisa e para fins gerais quando é necessária a fronteira terra/mar. Quando não há uma variação significativa no nível do mar, pode ser utilizado o nível médio do mar (Mean Sea Level - MSL) como substituto de MHW.

**15.1.8. Contorno marinho (MarineContour)**

Um conjunto de isolinhas que representa o valor de um fenómeno num determinado momento.

Atributos do tipo de objeto geográfico «MarineContour»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| isoline | Isolinha utilizada para gerar o contorno. | MarineIsoline |  |
| phenomenon | Propriedade representada pelas isolinhas (por exemplo, altura de vaga). | AbstractObservableProperty |  |
| validTime | Momento em que este contorno é representativo. | TM_Instant |  |

Associações do tipo de objeto geográfico «MarineContour»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| sourceObservations | Utilizado para ligação a uma coleção de observações subjacentes que foram utilizadas para definir um contorno marinho. | ObservationSet |  |

**15.1.9. Camada marinha (MarineLayer)**

Uma camada marinha descreve uma camada que pode cobrir qualquer parte da superfície do mar ou de um fundo marinho.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «MarineLayer»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Geometria da camada marinha. | GM_Object |  |
| validTime | Período de tempo durante o qual a camada marinha é válida. | TM_Period |  |

Associações do tipo de objeto geográfico «MarineLayer»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| subLayer | Uma camada marinha pode ter uma subcamada, por exemplo um lençol de petróleo pode ter um lençol principal e vários pequenos sublençóis. | MarineLayer |  |

Restrições do tipo de objeto geográfico «MarineLayer»

Uma camada marinha pode ser representada como uma superfície ou como um ponto. A geometria do tipo ponto reflete o facto de terem sido identificadas muitas camadas marinhas por observações pontuais.

**15.1.10. Área do fundo marinho (SeaBedArea)**

Uma área do fundo marinho com um tipo identificado de cobertura, por exemplo, uma área do tipo vegetação ou sedimentos.

Este tipo é um subtipo de «MarineLayer».

Atributos do tipo de objeto geográfico «SeaBedArea»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| surfaceType | Tipo de superfície do fundo marinho. | SeaBedCoverValue |  |

**15.1.11. Área da superfície do mar (SeaSurfaceArea)**

Uma área da superfície do mar com um certo tipo de cobertura, por exemplo, uma área de gelo marinho.

Este tipo é um subtipo de «MarineLayer».

Atributos do tipo de objeto geográfico «SeaSurfaceArea»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| surfaceType | Tipo de superfície da área marinha. | SeaSurfaceClassificationValue |  |

**15.2. Tipos de dados**

**15.2.1. Extensão marinha (MarineExtent)**

A extensão da área marinha num determinado estado das marés.

Atributos do tipo de dados «MarineExtent»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Geometria da extensão marinha. | GM_MultiSurface |  |
| waterLevel | Nível de água a que a extensão é válida. | WaterLevelValue |  |

**15.2.2. Isolinha marinha (MarineIsoline)**

Uma isolinha que representa um determinado valor de um fenómeno marinho físico ou químico, como a temperatura, salinidade ou altura de vaga.

Atributos do tipo de dados «MarineIsoline»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Geometria das isolinhas. | GM_MultiCurve |  |
| value | Valores atribuídos às isolinhas. | Measure |  |

**15.2.3. Par valor-parâmetro (ParameterValuePair)**

Um par valor-parâmetro contém um valor de uma propriedade observada, por exemplo, temperatura anual média da superfície do mar.

Atributos do tipo de dados «ParameterValuePair»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| parameter | Definição do parâmetro observado (por exemplo, temperatura média). | AbstractObservableProperty |  |
| value | Valor do parâmetro observado, por exemplo, 12 graus Celsius. | Measure |  |
| validTime | Momento em que o valor atribuído é válido. Pode ser um instante no tempo ou um período. | TM_Object | Voidable |

**15.2.4. Segmento da margem (ShoreSegment)**

Um segmento da margem é uma secção da «shoreline» (linha de margem).

**Atributos do tipo de dados «ShoreSegment»**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Geometria do «ShoreSegment». | GM_Curve |  |
| shoreClassification | Tipo primário do segmento da margem tirado da lista de códigos de «ShoreTypeClassificationValue». | ShoreTypeClassificationValue | voidable |
| shoreStability | Tipo primário de estabilidade do segmento da margem tirado da lista de códigos de «ShoreStabilityValue». | ShoreStabilityValue | voidable |

**15.3. Listas de códigos**

**15.3.1. Classificação do tipo de área marinha (SeaAreaTypeClassificationValue)**

Tipo de classificação da «SeaArea», por exemplo «estuary», «openOcean».

**15.3.2. Cobertura do fundo marinho (SeaBedCoverValue)**

Tipos de cobertura encontrados nos fundos marinhos.

**15.3.3. Classificação da superfície marinha (SeaSurfaceClassificationValue)**

Tipos de camadas de superfícies marinhas observados em superfícies marinhas.

**15.3.4. Estabilidade da margem (ShoreStabilityValue)**

Tipos de estabilidade de segmentos da margem.

**15.3.5. Classificação do tipo de margem (ShoreTypeClassificationValue)**

Tipos de segmentos da margem.

**15.3.6. Tipo de zona (ZoneTypeValue)**

Tipos de zonas marinhas de circulação.

**15.4. Requisitos específicos de categorias temáticas**

(1) O objeto geográfico «Sea» deve ser utilizado para descrever áreas ou mares (ou oceanos) identificados e designados. Estão excluídas do cumprimento deste requisito as unidades de reporte artificiais.

(2) A «MarineExtent» de um objeto geográfico «Sea» deve ter um valor de «waterLevel» igual a «MeanHighWater», salvo se não houver uma alteração significativa na extensão do mar devido a marés, podendo nesse caso ser utilizado um valor de «MeanSeaLevel».

(3) O nível de maré baixa utilizado para definir uma «IntertidalArea» deve ser fornecido como um valor do atributo «lowWaterLevel». O nível deve ser um nível de maré baixa.

(4) «Oceanográficas» devem ser utilizadas para identificar fenómenos representados por tipos de objetos geográficos «MarineContour».

(5) As «SeaAreas» devem ser representadas por geometrias bidimensionais.

**15.5. Camadas**

**Camadas para a categoria temática de dados geográficos «Regiões Marinhas»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| SR.SeaArea | Área marinha | SeaArea |
| SR.Sea | Mar | Sea |
| SR.MarineCirculationZone | Zona marinha de circulação | MarineCirculationZone |
| SR.InterTidalArea | Área intertidal | InterTidalArea |
| SR.MarineContour | Contorno marinho | MarineContour |
| SR.Shoreline | Linha da margem | Shoreline |
| SR.Coastline | Linha da costa | CoastLine |
| SR.SeaSurfaceArea | Área da superfície do mar | SeaSurfaceArea |
| SR.SeaBedArea | Área do fundo marinho | SeaBedArea |

**16. REGIÕES BIOGEOGRÁFICAS (BIO-GEOGRAPHICAL REGIONS)**

**16.1. Tipos de objetos geográficos**

É especificado o seguinte tipo de objeto geográfico para a categoria temática de dados geográficos «Regiões Biogeográficas»: «Bio-geographical Region».

**16.1.1. Região biogeográfica (Bio-geographicalRegion)**

Uma área em que se verificam condições ecológicas relativamente homogéneas com características comuns.

Atributos do tipo de objeto geográfico «Bio-geographicalRegion»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| geometry | Geometria que define a região ecológica. | GM_MultiSurface |  |
| regionClassification | Código de classe da região, de acordo com um sistema de classificação. | RegionClassificationValue |  |
| regionClassificationScheme | Sistema de classificação utilizado para classificar regiões. | RegionClassificationSchemeValue |  |
| regionClassificationLevel | Nível de classificação da classe de regiões. | RegionClassificationLevelValue | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

**16.2. Listas de códigos**

**16.2.1. Nível de classificação das regiões (RegionClassificationLevelValue)**

Códigos que definem o nível de classificação da classe de regiões.

**16.2.2. Sistema de classificação de regiões (RegionClassificationSchemeValue)**

Códigos que definem as várias regiões biogeográficas.

**16.2.3. Classificação de regiões (RegionClassificationValue)**

Códigos utilizados para definir as várias regiões biogeográficas.

Esta lista de códigos inclui os valores constantes das listas de códigos seguintes ou de outras listas de códigos definidas pelos fornecedores dos dados:

— Classificação da estratificação ambiental («EnvironmentalStratificationClassificationValue»): Códigos para a estratificação climática do ambiente na União, conforme especificado em Metzger, M.J., Shkaruba, A.D., Jongman, R.H.G., Bunce, R.G.H., Descriptions of the European Environmental Zones and Strata. Alterra, Wageningen, 2012.

— Classificação da Diretiva-Quadro Estratégia Marinha (MarineStrategyFrameworkDirectiveClassificationValue): Códigos da classificação da Diretiva-Quadro Estratégia Marinha, enumerados no artigo 4.º da Diretiva 2008/56/CE do Parlamento Europeu e do Conselho (

14

)

.

— Classificação das Regiões Biogeográficas Natura 2000 e da Rede Emerald (Natura2000AndEmeraldBio-geographicalRegionClassificationValue): Codes for the classification of bio-geographical regions, as specified in the Code List for Bio-geographical Regions, Europe 2011, publicados no sítio Web da Agência Europeia do Ambiente.

— Classificação da Vegetação Natural (NaturalVegetationClassificationValue): Códigos para a classificação da vegetação natural, conforme especificado nas principais formações em Bohn, U., Gollub, G., Hettwer, C., Map of the natural vegetation of Europe: scale 1:2,500,000, Part 2: Legend, Bundesamt für Naturschutz (Agência Federal Alemã para a Conservação da Natureza), Bona, 2000.

**16.3. Camadas**

**Camadas para a categoria temática de dados geográficos «Regiões Biogeográficas»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| BR.Bio-geographicalRegion | Regiões biogeográficas | Bio-geographicalRegion |

**17. HABITATS E BIÓTOPOS (HABITATS AND BIOTOPES)**

**17.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) «Biótopo» (biotope) : uma região com condições ambientais relativamente uniformes, ocupada por uma determinada comunidade vegetal e pela sua comunidade animal associada.

(2) «Habitat» : o local em que uma planta ou animal cresce ou vive naturalmente. Pode ser quer a extensão da área geográfica sobre a qual se estende o habitat, quer a estação em particular em que se observa um espécime. Um habitat é caracterizado por uma uniformidade relativa do ambiente físico e por uma interação bastante estreita de todas as espécies biológicas nele presentes.

(3) «Tipo de habitat» (ou tipo de biótopo) (habitat type (or biotope type)) : um tipo abstrato classificado para descrever habitats ou biótopos que têm algumas características comuns a um determinado nível de detalhe. Os critérios de classificação geralmente utilizados podem referir-se à estrutura da vegetação (como florestas, pastagens, charnecas) ou a características abióticas como águas correntes, rochas calcárias ou dunas de areia, mas também a etapas ou fases relevantes do ciclo de vida de uma determinada espécie ou associação ecológica, como áreas de invernada, áreas de nidificação ou corredores de passagem, etc.

(4) «Distribuição (de tipos de habitat)» (distribution (of habitat types)) : uma coleção de objetos geográficos em que ocorre o tipo de habitat, apresentando informações sobre a ocorrência de um tipo de habitat específico no tempo ou no espaço em unidades analíticas. É geralmente representada ou modelizada com base noutros objetos geográficos utilizados como unidades analíticas, por exemplo entre quadrículas-células (muito frequentemente), regiões biogeográficas, sítios de conservação da natureza ou unidades administrativas.

(5) «Característica do habitat» (habitat feature) : habitat em termos da sua localização, dimensão (área ou volume) e informação biológica exatas sobre tipos de habitats, traços estruturais, listas de espécies e tipos de vegetação.

(6) «Espécie» (species) : uma categoria taxonómica que classifica imediatamente abaixo de género e que inclui indivíduos estreitamente relacionados e morfologicamente semelhantes que se podem, potencialmente ou de facto, reproduzir. No contexto da categoria temática «Habitats e Biótopos», entende-se por «espécie» todas as espécies animais, espécies vegetais ou espécies de fungos relevantes para descrever um habitat.

(7) «Vegetação» (vegetation) : as plantas de uma área consideradas em geral ou enquanto comunidades, mas não do ponto de vista taxonómico. A vegetação pode também ser definida como a cobertura vegetal total numa determinada área da Terra no seu conjunto.

(8) «Tipo de vegetação» (vegetation type) : plantas (ou massa total de flora) de uma determinada área consideradas em geral ou como comunidades vegetais, mas não do ponto de vista taxonómico.

**17.2. Tipos de objetos geográficos**

É especificado o seguinte tipo de objeto geográfico para a categoria temática de dados geográficos «Habitats e Biótopos»: «Habitat».

**17.2.1. Habitat (Habitat)**

Áreas geográficas caracterizadas por condições, estruturas, funções e processos ecológicos específicos que sustentam fisicamente os organismos que nelas vivem.

Atributos do tipo de objeto geográfico «Habitat»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Extensão do habitat baseada nas fronteiras naturais. | GM_Object |  |
| habitat | Identificador de uma classe de habitats, definida e descrita num sistema de classificação de habitats internacional, nacional ou local. | HabitatTypeCoverType |  |
| habitatSpecies | Lista de espécies que ocorrem num determinado habitat ou o constituem no momento da elaboração do levantamento. | HabitatSpeciesType | voidable |
| habitatVegetation | Lista de tipos de vegetação (de acordo com um sistema de classificação da vegetação local) que constituem um determinado habitat. | HabitatVegetationType | voidable |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |

**17.3. Tipos de dados**

**17.3.1. Tipo de espécies do habitat (HabitatSpeciesType)**

Espécies presentes num determinado habitat no momento da elaboração do levantamento.

Atributos do tipo de dados «HabitatSpeciesType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| localSpeciesName | Nome científico, acrescido do autor, utilizado na nomenclatura nacional, com o seu conceito taxonómico nacional. | LocalNameType | voidable |
| referenceSpeciesScheme | Lista de referência que define um padrão de nomenclatura ou taxonomia em função do qual será efetuado o levantamento de todos os nomes de espécies e conceitos taxonómicos locais. | ReferenceSpeciesSchemeValue |  |
| referenceSpeciesId | Identificador de uma das listas de referência dada pelo «referenceSpeciesScheme». | ReferenceSpeciesCodeValue |  |

**17.3.2. Tipo de cobertura do tipo de habitat (HabitatTypeCoverType)**

Tipo de habitat de acordo com um sistema de classificação de habitats internacional, nacional ou local.

Atributos do tipo de dados «HabitatTypeCoverType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| areaCovered | Área coberta por um determinado tipo de habitats no âmbito da geometria fornecida para o objeto geográfico habitat. | Area | voidable |
| lengthCovered | Comprimento coberto por um determinado tipo de habitats no âmbito da geometria fornecida para o objeto geográfico habitat. | Length | voidable |
| volumeCovered | Volume de um determinado tipo de habitats no âmbito da geometria fornecida para o objeto geográfico habitat. | Volume | voidable |
| referenceHabitatTypeId | Identificador único (código) de tipo de habitat de acordo com um sistema de classificação pan-europeu. | ReferenceHabitatTypeCodeValue |  |
| referenceHabitatTypeScheme | Um dos sistemas de classificação pan-europeus que são largamente utilizados na Europa. | ReferenceHabitatTypeSchemeValue |  |
| localHabitatName | Tipo de habitat de acordo com um sistema local de classificação de habitats. | LocalNameType | voidable |
| referenceHabitatTypeName | Nome de um determinado tipo de habitat de acordo com um sistema de classificação pan-europeu. | CharacterString | voidable |

**17.3.3. Tipo de vegetação do habitat (HabitatVegetationType)**

Tipo de vegetação presente num determinado habitat.

Atributos do tipo de dados «HabitatVegetationType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| localVegetationName | Classe de vegetação (tipo de vegetação) de acordo com um sistema de classificação local. Nome em linguagem natural de acordo com o sistema de classificação de vegetação local. | LocalNameType |  |

**17.3.4. Tipo de nome local (LocalNameType)**

Nome de acordo com um sistema de classificação local.

Atributos do tipo de dados «LocalNameType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| localScheme | Identificador uniforme de recursos de um sistema de classificação local. | CharacterString |  |
| localNameCode | Nome em linguagem natural de acordo com um sistema de classificação local. | LocalNameCodeValue |  |
| qualifierLocalName | A relação entre o nome local e o nome correspondente no sistema pan-europeu. | QualifierLocalNameValue | voidable |
| localName | Nome de acordo com um sistema de classificação local. | CharacterString | voidable |

**17.4. Listas de códigos**

**17.4.1. Nome do qualificador local (QualifierLocalNameValue)**

Lista de valores que especificam a relação entre um nome utilizado localmente e um nome utilizado a nível pan-europeu.

**17.4.2. Código do tipo de habitat de referência (ReferenceHabitatTypeCodeValue)**

Valores utilizados nos sistemas de classificação de habitats pan-europeus.

Esta lista de códigos compreende os valores das seguintes listas de códigos:

— Código de Tipo de Habitat EUNIS (EunisHabitatTypeCodeValue): Classificação dos tipos de habitats de acordo com a base de dados Biodiversidade EUNIS, conforme especificado na classificação de tipos de habitats EUNIS publicada no sítio Web da Agência Europeia do Ambiente.

— Código da Diretiva Habitats (HabitatsDirectiveCodeValue): Classificação dos tipos de habitats de acordo com o anexo I da Diretiva 92/43/CEE.

— Código da Diretiva-Quadro Estratégia Marinha (MarineStrategyFrameworkDirectiveCodeValue): Classificação de tipos de habitats de acordo com o quadro 1 do anexo III da Diretiva 2008/56/CE.

**17.4.3. Sistema de tipos de habitats de referência (ReferenceHabitatTypeSchemeValue)**

Este valor define qual foi o sistema de classificação de habitats pan-europeu utilizado.

**17.4.4. Código do nome local (LocalNameCodeValue)**

Identificador tirado de um sistema de classificação local.

**17.5. Requisitos específicos de categorias temáticas**

(1) É obrigatório disponibilizar, pelo menos, um tipo de habitat de acordo com um «referenceHabitatTypeScheme» (pan-europeu) enumerado na lista de códigos de «ReferenceHabitatTypeSchemeValue». Esta codificação destina-se a permitir pesquisas sobre os tipos de habitats a um nível harmonizado à escala pan-europeia.

**17.6. Camadas**

**Camada para a categoria temática de dados geográficos «Habitats e Biótopos»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| HB.Habitat | Habitat | Habitat |

**18. DISTRIBUIÇÃO DAS ESPÉCIES (SPECIES DISTRIBUTION)**

**18.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) «Agregação» (aggregation) : o agrupamento de múltiplos objetos numa classe ou agregado.

(2) «Amálgama» (amalgamation) : a combinação de múltiplos objetos numa estrutura única.

**18.2. Tipos de objetos geográficos**

São especificados os seguintes tipos de objetos geográficos para a categoria temática de dados geográficos «Distribuição das Espécies»:

— Conjunto de dados de distribuição das espécies

— Unidade de distribuição das espécies

**18.2.1. Conjunto de dados de distribuição das espécies (SpeciesDistributionDataSet)**

Este conjunto de dados é uma coleção de objetos geográficos individuais (unidades) numa distribuição de espécies.

Atributos do tipo de objeto geográfico «SpeciesDistributionDataSet»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| domainExtent | Extensão geográfica do domínio da coleção de características. | GM_MultiSurface | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| name | Nome de um conjunto de dados específico fornecido para a Distribuição das Espécies. | CharacterString | voidable |

Associações do tipo de objeto geográfico «SpeciesDistributionDataSet»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| member | Objeto geográfico individual numa coleção de objetos geográficos. | SpeciesDistributionUnit |  |
| documentBasis | Referência ou citação de um documento que descreve uma campanha ou ato legislativo que constitui a base para o conjunto de dados. | DocumentCitation | voidable |

**18.2.2. Unidade de distribuição das espécies (SpeciesDistributionUnit)**

Ocorrência de espécies animais e vegetais agregadas por quadrícula, região, unidade administrativa ou outra unidade analítica.

Atributos do tipo de objeto geográfico «SpeciesDistributionUnit»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Geometria de cada unidade numa coleção. | GM_Object |  |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| distributionInfo | Descrição do objeto da distribuição (ocorrências ou população), indicação da contagem de observações ou da dimensão da população de uma dada espécie, grupo de espécies ou ordem de táxon e sua distribuição ou isolamento dentro da unidade de distribuição das espécies. | DistributionInfoType | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| speciesName | Identificador e nome científico, incluindo o autor, tirado de uma lista de referência internacional, opcionalmente completado por um nome utilizado localmente e pela relação do seu conceito taxonómico com o nome de referência. | SpeciesNameType |  |

Associações do tipo de objeto geográfico «SpeciesDistributionUnit»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| spatialObject | Referência a outro objeto geográfico que define a extensão geográfica de uma unidade de distribuição. | AbstractFeature | voidable |

Restrições do tipo de objeto geográfico «SpeciesDistributionUnit»

Se geometria não tiver qualquer valor, é necessário fornecer uma referência a um objeto geográfico.

**18.3. Tipos de dados**

**18.3.1. Tipo de informação da distribuição (DistributionInfoType)**

A descrição do estatuto do objeto da distribuição dentro da unidade de distribuição das espécies, incluindo a indicação da abundância por contagem, estimativa ou cálculo do número de ocorrências ou da dimensão da população dessa determinada espécie.

Atributos do tipo de dados «DistributionInfoType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| occurrenceCategory | Densidade populacional da espécie na unidade de distribuição das espécies. | OccurrenceCategoryValue |  |
| residencyStatus | Informação sobre o estatuto de residência de uma espécie no que diz respeito ao seu caráter local versus introdução e permanência. | ResidencyStatusValue | voidable |
| populationSize | Valor da gama que indica as ocorrências contadas, estimadas ou calculadas ou as dimensões das populações, utilizando um limite superior e inferior. | PopulationSizeType |  |
| sensitiveInfo | Valor booleano que indica se a localização de uma espécie específica é sensível. | Boolean | voidable |
| populationType | Permanência das populações, em particular no que se refere às espécies migratórias, numa dada unidade de distribuição das espécies. | PopulationTypeValue | voidable |
| collectedFrom | Data em que a recolha de dados de ocorrência da espécie original teve início. | Date | voidable |
| collectedTo | Data em que a recolha dos dados de ocorrência da espécie original terminou. | Date | voidable |

**18.3.2. Tipo de dimensão da população (PopulationSizeType)**

Um valor da gama que indica as ocorrências contadas, estimadas ou calculadas ou as dimensões das populações, que é definido por um limite superior e inferior.

Atributos do tipo de dados «PopulationSizeType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| countingMethod | Método para fornecer um número para a indicação da abundância de uma espécie numa unidade de distribuição de espécies específica. | CountingMethodValue |  |
| countingUnit | O que foi contado, estimado ou calculado ao compilar a informação sobre a abundância de uma espécie dentro da unidade de distribuição das espécies. | CountingUnitValue |  |
| populationSize | Valor da gama que indica as ocorrências contadas, estimadas ou calculadas ou as dimensões das populações, utilizando limites superiores e inferiores. | RangeType (definido no ponto 18.3.3) |  |

**18.3.3. Tipo de gama (RangeType)**

Valor que indica os limites superior e inferior da contagem, estimativa ou cálculo de ocorrências.

Atributos do tipo de dados «RangeType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| upperBound | Limite superior da gama de valores. Se o valor deste atributo for nulo e o atributo «lowerBound» estiver preenchido, isso implica que o valor se situa entre «lowerBound» e o infinito. | Integer |  |
| lowerBound | Limite inferior da gama de valores. Se o valor deste atributo for nulo e o atributo «lowerBound» estiver preenchido, isso implica que o valor se situa entre «upperBound» e zero. | Integer |  |

**18.3.4. Tipo de nome da espécie (SpeciesNameType)**

Identificador e nome científico, incluindo o autor, tirado de uma lista de referência internacional, opcionalmente completado por um nome utilizado localmente e pela relação do seu conceito taxonómico com o nome de referência.

Atributos do tipo de dados «SpeciesNameType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| referenceSpeciesId | Identificador de uma das listas de referência dada pelo «referenceSpeciesScheme». | ReferenceSpeciesCodeValue |  |
| referenceSpeciesScheme | Lista de referência que define um padrão de nomenclatura e taxonomia em função do qual será efetuado o levantamento de todos os nomes de espécies e conceitos taxonómicos locais. | ReferenceSpeciesSchemeValue |  |
| referenceSpeciesName | Nome científico utilizado no «ReferenceSpeciesScheme» autorizado. | CharacterString | voidable |
| localSpeciesId | Identificador utilizado na nomenclatura nacional. | LocalSpeciesNameCodeValue | voidable |
| localSpeciesScheme | Nome do sistema de classificação de espécies local («bibliographic reference»). | CharacterString | voidable |
| localSpeciesName | Nome científico utilizado na nomenclatura nacional com o seu conceito taxonómico nacional. | CharacterString | voidable |
| qualifier | Especifica a relação do conceito taxonómico entre o identificador de espécie local e o identificador de espécie de referência. | QualifierValue | voidable |

**18.4. Listas de códigos**

**18.4.1. Método de contagem (CountingMethodValue)**

Método para a produção de números que indicam a abundância de uma espécie numa unidade agregada.

**18.4.2. Unidade de contagem (CountingUnitValue)**

Unidade definida utilizada para exprimir um número contado ou estimado que indica a abundância de uma espécie numa «SpeciesDistributionUnit».

**18.4.3. Código do nome da espécie local (LocalSpeciesNameCodeValue)**

Identificador da espécie proveniente de um sistema de classificação local.

**18.4.4. Categoria da ocorrência (OccurrenceCategoryValue)**

Densidade populacional da espécie na «SpeciesDistributionUnit».

**18.4.5. Tipo de população (PopulationTypeValue)**

A permanência das populações, em particular no que se refere às espécies migratórias, numa dada unidade de distribuição de espécies.

**18.4.6. Qualificador (QualifierValue)**

Este valor define a relação entre os conceitos taxonómicos de um nome de espécie local e o nome de referência da espécie dado pelo identificador de referência da espécie ou por um sistema de referência de espécies.

**18.4.7. Código de espécies de referência (ReferenceSpeciesCodeValue)**

Listas de referência que contêm identificadores das espécies.

Esta lista de códigos compreende os valores das seguintes listas de códigos:

— Código EU-Nomen (EuNomenCodeValue): Listas de referência que contêm os identificadores de espécies EU-Nomen, conforme especificado na Infraestrutura Pan-Europeia de Diretórios de Espécies disponível através do Portal EU-Nomen.

— Código de Espécies EUNIS (EunisSpeciesCodeValue): Listas de referência que contêm os identificadores de espécies EUNIS, conforme especificado na base de dados de Biodiversidade EUNIS publicada no sítio Web da Agência Europeia do Ambiente.

— Código das Diretivas Natureza (NatureDirectivesCodeValue): Listas de referência que contêm os identificadores de espécies das Diretivas Natureza, conforme especificado no Portal de Referência da Rede Natura 2000 e definido na Decisão de Execução 2011/484/UE da Comissão (

15

).

**18.4.8. Sistema de espécies de referência (ReferenceSpeciesSchemeValue)**

Listas de referência que definem um padrão de nomenclatura e taxonomia em função do qual se pode proceder ao levantamento dos nomes e conceitos taxonómicos locais.

**18.4.9. Estatuto de residência (ResidencyStatusValue)**

Categoria de residência das ocorrências ou população estimada dentro de uma determinada unidade agregada.

**18.5. Requisitos específicos de categorias temáticas**

(1) Quando são necessárias representações matriciais das distribuições de espécies, deve ser utilizada a Grid_ETRS89-LAEA tal como definido no anexo II, ponto 2.2.1.

(2) Para objetos geográficos de «SpeciesDistributionUnit»:

(a) Se uma espécie não foi ativamente procurada, o atributo «distributionInfo» deve ficar vazio («void») com a indicação de «unknown» e

(b) Se uma espécie foi ativamente procurada, mas não foi encontrada, o valor do atributo «occurenceCategory» de «DistributionInfoType» deve indicar «absent».

(3) Se as geometrias dos objetos geográficos num conjunto de dados «SpeciesDistributionUnit» forem derivadas das geometrias de objetos geográficos noutro conjunto de dados, então este conjunto de dados fonte (incluindo a respetiva versão) deve ser descrito como parte do elemento de metadados «Histórico».

**18.6. Camada**

**Camada para a categoria temática de dados geográficos «Distribuição das Espécies»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| SD.<Valor de lista de códigos> (1) | Distribuição da espécie (de <nome legível para as pessoas>) | SpeciesDistributionUnit (speciesName / referenceSpeciesId: ReferenceSpeciesCodeValue) |
| Exemplo: SD.SulaBassana | Exemplo: Distribuição da espécie (de Sula bassana) |  |
| (1) <br> Deve ser disponibilizada uma camada para cada valor das listas de códigos, de acordo com o estabelecido no artigo 14.º, n.º 3 |  |  |

**19. RECURSOS ENERGÉTICOS (ENERGY RESOURCES)**

**19.1. Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(4) «Recursos energéticos» (energy resource) : uma concentração ou ocorrência de uma fonte de energia que pode ter estado, estar ou vir a estar presente no futuro.

(5) «Combustíveis fósseis» (fossil fuels) : uma forma de energia primária não renovável formada por processos naturais como a decomposição anaeróbia de organismos mortos enterrados, que contém elevadas percentagens de carbono e inclui o carvão, o petróleo bruto e o gás natural.

(6) «Energia primária» (primary energy) : a energia que não foi sujeita a qualquer processo de conversão ou transformação.

(7) «Energia não renovável» (non-renewable energy) : os recursos naturais que, devido à sua formação a longo prazo, não podem ser produzidos, cultivados, gerados ou utilizados numa escala que possa manter a sua taxa de consumo.

(8) «Energia proveniente de fontes renováveis» (energy from renewable sources) : a energia proveniente de fontes não fósseis renováveis, nomeadamente a energia eólica, solar, aerotérmica, geotérmica, hidrotérmica, oceânica, hidráulica, da biomassa, de gases de aterros, de gases das instalações de tratamento de águas residuais e de biogases, em conformidade com o artigo 2.º da Diretiva 2009/28/CE do Parlamento Europeu e do Conselho (

16

).

(9) «Resíduos como recursos energéticos» (waste as energy resources) : um combustível que pode consistir em diferentes materiais provenientes de resíduos combustíveis industriais, institucionais, hospitalares e urbanos, como a borracha, os plásticos, os resíduos de óleos fósseis e outros produtos similares. Encontram-se numa forma líquida ou sólida, são renováveis ou não renováveis e são biodegradáveis ou não biodegradáveis.

**19.2. Estrutura da categoria temática de dados geográficos «Recursos Energéticos»**

Os tipos especificados para a categoria temática de dados geográficos «Recursos Energéticos» estão estruturados nos seguintes pacotes:

— Base de recursos energéticos (Energy Resources Base)

— Vetor de recursos energéticos (Energy Resources Vector)

— Cobertura de recursos energéticos (Energy Resources Coverage)

**19.3. Base de recursos energéticos**

**19.3.1. Tipos de dados**

19.3.1.1. Tipo de gama de extensão vertical (VerticalExtentRangeType)

Valor que indica os limites superior e inferior da gama altura/profundidade.

Atributos do tipo de dados «VerticalExtentRangeType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| lowerBound | Valor que indica o limite inferior da gama altura/profundidade. | Length | voidable |
| upperBound | Valor que indica o limite superior da gama altura/profundidade. | Length |  |

Restrições do tipo de dados «VerticalExtentRangeType»

O valor de «lowerBound» (limite inferior) deve ser expresso em metros.

O valor de «upperBound» (limite superior) deve ser expresso em metros.

19.3.1.2. Tipo de extensão vertical (VerticalExtentType)

Propriedade dimensional vertical que consiste numa medida absoluta ou gama de medidas referenciada a um nível vertical de referência bem definido que é geralmente tomado como a origem (nível do solo, nível médio do mar, etc.).

Atributos do tipo de dados «VerticalExtentType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| verticalExtent | Extensão da dimensão vertical, representada por uma grandeza escalar ou por uma gama de valores. | VerticalExtentValue |  |
| verticalReference | Nível de referência escolhido para determinar a altura/profundidade vertical. | VerticalReferenceValue |  |

19.3.1.3. Valor da extensão vertical (VerticalExtentValue)

Um único número ou uma gama de valores de altura/profundidade para descrever a posição, em termos de altura/profundidade, de um recurso energético.

Este tipo é um tipo de união.

Atributos do tipo de união «VerticalExtentValue»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| range | Gama dos números que representam a gama de altura ou profundidade de um recurso energético. | VerticalExtentRangeType |  |
| scalar | Número que representa a altura ou profundidade de um recurso energético. | Length |  |

Atributos do tipo de união «VerticalExtentValue»

O valor escalar deve ser expresso em metros.

**19.3.2. Listas de códigos**

19.3.2.1. Quadro de classificação e quantificação (ClassificationAndQuantificationFrameworkValue)

Valores para os sistemas de classificação mais amplamente utilizados para classificar e quantificar os recursos energéticos.

19.3.2.2. Classe de combustíveis fósseis (FossilFuelClassValue)

Valores que indicam os vários níveis de recursos de combustíveis fósseis.

19.3.2.3. Energias renováveis e resíduos (RenewableAndWasteValue)

Tipos de recursos em energias renováveis e resíduos.

19.3.2.4. Combustível fóssil (FossilFuelValue)

Tipos de combustíveis fósseis.

19.3.2.5. Referência vertical (VerticalReferenceValue)

Valores que indicam o nível de referência da extensão vertical.

**19.4. Vetor de recursos energéticos**

**19.4.1. Tipos de objetos geográficos**

O pacote «Vetor de Recursos Energéticos» contém os seguintes tipos de objetos geográficos:

— Recurso energético vetorial

— Recurso de combustíveis fósseis

— Recurso de energias renováveis e resíduos

19.4.1.1. Recurso energético vetorial (VectorEnergyResource)

Um objeto geográfico vetorial que define uma extensão geográfica inferida ou observável de um recurso que pode ser ou foi utilizado como fonte de energia.

Este tipo é abstrato.

Atributos do tipo de objeto geográfico «VectorEnergyResource»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| geometry | Representação geométrica da extensão geográfica abrangida por este recurso energético. | GM_Object |  |
| classificationAndQuantificationFramework | Sistema de classificação de referência para classificar e quantificar recursos energéticos. | ClassificationAndQuantificationFrameworkValue |  |
| verticalExtent | Propriedade dimensional vertical que consiste numa medida absoluta ou gama de medidas referenciada a um nível vertical de referência bem definido que é geralmente tomado como a origem (nível do solo, nível médio do mar, etc.). | VerticalExtentType | voidable |
| exploitationPeriod | O período de exploração («exploitationPeriod») define a data do início e, quando aplicável, a data de termo da aplicação. | ExploitationPeriodType | voidable |
| reportingAuthority | Organização responsável pela comunicação de informações sobre os recursos energéticos estimados e produzidos. | RelatedParty | voidable |
| resourceName | Nome do recurso energético. | GeographicalName | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

19.4.1.2. Recurso de combustíveis fósseis (FossilFuelResource)

Um objeto geográfico que define uma extensão geográfica inferida ou observável de um recurso que pode ser ou foi utilizado como uma fonte de energia fóssil combustível. Os tipos de combustíveis fósseis mais comuns são o carvão, o gás natural e o petróleo bruto.

Este tipo é um subtipo de «VectorEnergyResource».

Atributos do tipo de objeto geográfico «FossilFuelResource»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| resource | Tipo e quantidade de recursos de combustíveis fósseis num único objeto geográfico. | FossilFuelResourceType |  |
| dateOfDiscovery | Data em que a fonte de energia foi descoberta. | TM_Position | voidable |

19.4.1.3. Recurso de energias renováveis e resíduos (RenewableAndWasteResource)

Um objeto geográfico que define uma extensão geográfica inferida ou observável de um recurso que pode ser ou foi utilizado como uma fonte de energia renovável ou de resíduos.

Este tipo é um subtipo de «VectorEnergyResource».

Atributos do tipo de objeto geográfico «RenewableAndWasteResource»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| capacity | Capacidade energética de um recurso de energias renováveis dentro da extensão geográfica. | Measure | voidable |
| dateOfDetermination | Data em que a capacidade do recurso foi determinada. | TM_Position | voidable |
| typeOfResource | Tipo de recurso de energias renováveis ou resíduos. | RenewableAndWasteValue |  |

**19.4.2. Tipos de dados**

19.4.2.1. Tipo de gama de valores caloríficos (CalorificRangeType)

Valor que indica os limites mínimo e máximo da gama de valores caloríficos do recurso energético.

Atributos do tipo de dados «CalorificRangeType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| lowerBound | Valor que indica o limite inferior da gama de valores caloríficos. | Measure |  |
| upperBound | Valor que indica o limite superior da gama de valores caloríficos. | Measure |  |

19.4.2.2. Tipo de valor calorífico (CalorificValueType)

Valor ou gama de valores que descreve o valor calorífico de um recurso energético.

Este tipo é um tipo de união.

Atributos do tipo de união «CalorificValueType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| calorificRange | Gama de valores caloríficos que descreve o valor calorífico de um recurso energético. | CalorificRangeType |  |
| calorificScalar | Medida que quantifica a propriedade calorífica de um recurso energético. | Measure |  |

19.4.2.3. Tipo de período de exploração (ExploitationPeriodType)

O «exploitationPeriod» (período de exploração) define a data de início e, quando aplicável, a data de termo da exploração ou aplicação.

Atributos do tipo de dados «ExploitationPeriodType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginTime | Momento em que a exploração teve início. | TM_Position |  |
| endTime | Momento em que a exploração terminou. | TM_Position |  |

19.4.2.4. Medida de combustível fóssil (FossilFuelMeasure)

Quantidade de recursos de acordo com a categorização específica.

Atributos do tipo de dados «FossilFuelMeasure»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| amount | Quantidade do recurso presente no objeto geográfico. | Measure |  |
| dateOfDetermination | Data em que o recurso foi quantificado. | TM_Position |  |
| resourceClass | Categoria que indica o diferente grau de confiança do recurso de combustíveis fósseis, como inicialmente presente, reservas comprovadas, contingente. | FossilFuelClassValue |  |

19.4.2.5. Tipo de recurso de combustíveis fósseis (FossilFuelResourceType)

Tipo e quantidade do recurso de acordo com a categorização específica.

Atributos do tipo de dados «FossilFuelResourceType»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| calorificValue | Cada recurso de combustíveis fósseis é caracterizado em função do seu valor calorífico, ou seja, a quantidade de energia disponível numa unidade de massa. | CalorificValueType | voidable |
| quantity | Quantidade do recurso de acordo com a categorização específica. | FossilFuelMeasure | voidable |
| typeOfResource | Tipo de combustível fóssil. | FossilFuelValue |  |

**19.5. Cobertura de recursos energéticos**

**19.5.1. Tipos de objetos geográficos**

O pacote «Cobertura de Recursos Energéticos» contém o tipo de objeto geográfico Cobertura Potencial de Recursos de Energias Renováveis e Resíduos.

19.5.1.1. Cobertura Potencial de Recursos de Energias Renováveis e Resíduos (RenewableAndWastePotentialCoverage)

Função que fornece um valor potencial de energia a partir da sua gama para qualquer posição direta no seu domínio espacial, temporal ou espaciotemporal.

Este tipo é um subtipo de «RectifiedGridCoverage».

Atributos do tipo de objeto geográfico «RenewableAndWastePotentialCoverage»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| potentialType | Há vários tipos de energia potencial, cada um deles associado a um determinado tipo de energia. | PotentialTypeValue |  |
| typeOfResource | Tipo de recurso de energias renováveis e resíduos a que o fenómeno medido é aplicável. | RenewableAndWasteValue |  |
| domainExtent | O atributo «domainExtent» deve conter a extensão do domínio espaciotemporal da cobertura. As extensões podem ser especificadas tanto no espaço como no tempo. | EX_Extent |  |
| assessmentMethod | Referência ao método utilizado para avaliar o potencial do recurso energético. | DocumentCitation | voidable |
| name | Nome da cobertura. | CharacterString | voidable |
| validTime | Período de tempo em que esta cobertura é representativa. | TM_Period | voidable |
| verticalExtent | Número ou gama de valores da altura/profundidade para descrever a altura/profundidade a que são válidos os valores do conjunto da gama de valores. | VerticalExtentType | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

Restrições do tipo de objeto geográfico «RenewableAndWastePotentialCoverage»

Os valores de «rangeSet» devem ser do tipo «Measure».

**19.5.2. Listas de códigos**

19.5.2.1. Tipo potencial (PotentialTypeValue)

Tipos de energia potencial a partir de recursos de energias renováveis e resíduos.

**19.6. Requisitos específicos de categorias temáticas**

Quando a geometria do objeto geográfico é derivada de outro objeto geográfico, as geometrias dos dois objetos devem ser coerentes.

**19.7. Camadas**

**Camadas para a categoria temática de dados geográficos «Recursos Energéticos»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| ER. FossilFuelResource | Recursos de combustíveis fósseis | FossilFuelResource |
| ER.RenewableAndWasteResource | Recursos de energias renováveis e resíduos | RenewableAndWasteResource |
| ER.RenewableAndWastePotentialCoverage | Cobertura potencial de energias renováveis e resíduos | RenewableAndWastePotentialCoverage |

**20. RECURSOS MINERAIS (MINERAL RESOURCES)**

**20.1 Definições**

Além das definições estabelecidas no artigo 2.º, são aplicáveis as seguintes definições:

(1) «Produto de base» (commodity) : um material de interesse económico num recurso terrestre.

(2) «Mina» (mine) : uma escavação para a extração de depósitos minerais, incluindo explorações subterrâneas e minas a céu aberto (também designadas de poço aberto) para a extração de matérias-primas metálicas, bem como explorações a céu aberto para a extração de minerais industriais (que são frequentemente referidas como pedreiras).

(3) «Atividade mineira» (mining activity) : o processo de extração de depósitos minerais metálicos ou não metálicos da Terra.

**20.2. Estrutura da categoria temática de dados geográficos «Recursos Minerais»**

Os tipos especificados para a categoria temática de dados geográficos «Recursos Minerais» estão estruturados nos seguintes pacotes:

— Recursos minerais (Mineral Resources)

— Geologia (Geology) (para os tipo de objetos geográficos «MappedFeature», especificados no ponto 0 do anexo III)

**20.3. Recursos minerais**

O pacote «Recursos Minerais» contém os seguintes tipos de objetos geográficos:

— Recurso terrestre

— Ocorrência mineral

— Produto de base

— Atividade de prospeção

— Característica mineira

— Ocorrência da característica mineira

— Mina

— Atividade mineira

**20.3.1. Tipos de objetos geográficos**

20.3.1.1. Recurso terrestre (EarthResource)

As espécies de fenómenos observáveis ou inferidos necessárias para a classificação de recursos terrestres com e sem valor económico.

Este tipo é um subtipo de «GeologicFeature».

Este tipo é abstrato.

Atributos do tipo de objecto geográfico «EarthResource»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| dimension | Dimensão/volume do recurso terrestre. | EarthResourceDimension | voidable |
| expression | Indicador da presença de um «EarthResource» à superfície ou a sua deteção debaixo de uma cobertura rochosa. | Category | voidable |
| form | Relação física e estrutural típica da massa de minério com as rochas encaixantes e rochas associadas. | Category | voidable |
| linearOrientation | Orientação linear do «EarthResource». | CGI_LinearOrientation | voidable |
| planarOrientation | Orientação planar do «EarthResource». | CGI_PlanarOrientation | voidable |
| shape | Forma geométrica típica do «EarthResource» | Categoria | voidable |
| sourceReference | Fonte ou referência para o «EarthResource». | DocumentCitation | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanversion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

Associações do tipo de objeto geográfico «EarthResource»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| oreAmount | Quantidade estimada ou calculada de minério com a identificação dos produtos de base contidos e respetiva qualidade. | OreMeasure | voidable |
| explorationHistory | Lista cronológica dos levantamentos efetuados para definir melhor o potencial da ocorrência mineral. | ExplorationActivity | voidable |
| classification | Classificação do «EarthResource». | MineralDepositModel | voidable |
| resourceExtraction | Um ou mais períodos de atividade mineira do recurso terrestre. | MiningActivity | voidable |
| commodityDescription | Produtos de base presentes no recurso, ordenados por ordem de importância | Commodity |  |

20.3.1.2. Ocorrência mineral (MineralOccurrence)

Uma acumulação mineral na litosfera.

Este tipo é um subtipo de «EarthResource».

Atributos do tipo de objeto geográfico «MineralOccurrence»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| type | Tipo de ocorrência mineral. | MineralOccurrenceTypeValue |  |
| endusePotential | Potencial de uso final do mineral. | EndusePotentialValue | voidable |

20.3.1.3. Produto de base (Commodity)

O material de interesse económico contido no «EarthResource».

Atributos do tipo de objeto geográfico «Produto de Base»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| commodityImportance | Importância do depósito relativamente ao produto de base. | ImportanceValue | voidable |
| commodity | Produto de base do recurso terrestre. | CommodityCodeValue |  |
| commodityRank | Posição do produto de base na classificação em função da importância. | Integer | voidable |

Associações do tipo de objeto geográfico «Commodity»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| source | Depósito/recurso de que o produto de base é proveniente. | EarthResource |  |

20.3.1.4. Atividade de prospeção (ExplorationActivity)

Um período da atividade de prospeção.

Atributos do tipo de objecto geográfico «ExplorationActivity»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| activityDuration | Período, ou extensão no tempo, da atividade de prospeção. | TM_Period |  |
| activityType | Tipo de atividade de prospeção. | ExplorationActivityTypeValue |  |
| explorationResult | Resultado da atividade de prospeção. | ExplorationResultValue |  |

20.3.1.5. Característica mineira (MiningFeature)

Tipo de objeto geográfico que agrupa as propriedades comuns de minas e atividades mineiras.

Este tipo é abstrato.

Atributos do tipo de objecto geográfico «MiningFeature»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |

20.3.1.6. Ocorrência da característica mineira (MiningFeatureOccurrence)

A representação geográfica de uma «MiningFeature»

Atributos do tipo de objeto geográfico «MiningFeatureOccurrence»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| shape | Geometria da «MiningFeature». | GM_Object |  |

Associações do tipo de objeto geográfico «MiningFeatureOccurrence»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| specification | Indica a «MiningFeature» especificada pela «MiningFeatureOccurrence». | MiningFeature |  |

20.3.1.7. Mina (Mine)

Uma escavação efetuada para a extração de depósitos minerais.

Este tipo é um subtipo de «MiningFeature».

Atributos do tipo de objecto geográfico «Mine»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| mineName | Tipo de dados que indica o nome da mina e se é o nome privilegiado. | MineName |  |
| status | Valor do estado operacional da mina. | MineStatusValue |  |
| sourceReference | Referência-fonte da mina. | DocumentCitation | voidable |
| startDate | Data em que a mina começou a funcionar. | TM_Instant | voidable |
| endDate | Data em que a mina deixou de funcionar. | TM_Instant | voidable |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |

Associações do tipo de objecto geográfico «Mine»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| relatedMine | Mina relacionada. | Mine | voidable |
| relatedActivity | «MiningActivity» associada à mina. | MiningActivity |  |

20.3.1.8. Atividade mineira (MiningActivity)

O processo de extração da terra de depósitos rochosos, minerais ou industriais, metálicos e não metálicos.

Este tipo é um subtipo de «MiningFeature».

Atributos do tipo de objecto geográfico «MiningActivity»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| activityDuration | Período, ou extensão no tempo, da atividade mineira. | TM_Period |  |
| activityType | Tipo de atividade mineira. | MiningActivityTypeValue |  |
| oreProcessed | Quantidade de minério processado por essa atividade. | Quantity | voidable |
| processingType | Tipo de processamento efetuado no âmbito da atividade mineira. | ProcessingActivityTypeValue |  |

Associações do tipo de objecto geográfico «MiningActivity»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| associatedMine | Mina em que a atividade mineira tem ou teve lugar. | Mine | voidable |
| deposit | Depósito a que a atividade mineira está associada. | EarthResource | voidable |

**20.3.2. Tipos de dados**

20.3.2.1. Medida do produto de base (CommodityMeasure)

Uma medida da quantidade de produto de base a partir de um cálculo da reserva, do recurso ou da dotação.

Atributos do tipo de dados «CommodityMeasure»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| commodityAmount | Quantidade do produto de base. | QuantityRange | voidable |
| cutOffGrade | Grau-limite utilizado para o cálculo da quantidade do produto de base. | QuantityRange | voidable |
| grade | Qualidade do produto de base. | QuantityRange | voidable |

Associações do tipo de dados «CommodityMeasure»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| commodityOfInterest | Produto de base a que se refere a «CommodityMeasure». | Commodity |  |

20.3.2.2. Dimensão do recurso terrestre (EarthResourceDimension)

A dimensão/volume do recurso terrestre.

Atributos do tipo de dados «EarthResourceDimension»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| area | Área do «Earth Resource». | QuantityRange | voidable |
| depth | Profundidade do «Earth Resource». | QuantityRange | voidable |
| length | Comprimento do «Earth Resource». | QuantityRange | voidable |
| width | Largura do «Earth Resource». | QuantityRange | voidable |

20.3.2.3. Dotação (Endowment)

A quantidade de um mineral (ou de um grupo de minerais no que diz repeito a rochas industriais) em acumulação (depósitos) que reúne as características físicas especificadas, como a qualidade, dimensão e profundidade.

Este tipo é um subtipo de «OreMeasure».

Atributos do tipo de dados «Endowment»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| includesReserves | Marca (flag) que indica se a estimativa inclui o valor das reservas. | Boolean | voidable |
| includesResources | Marca que indica se a estimativa inclui o valor dos recursos. | Boolean | voidable |

20.3.2.4. Nome da mina (MineName)

Tipo de dados que indica o Nome da Mina e se é o nome privilegiado.

Atributos do tipo de dados «MineName»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| isPreferred | Operador booleano que indica se o valor de «mineName» é o nome privilegiado para designar a mina. | Boolean |  |
| mineName | Nome da mina. | CharacterString |  |

20.3.2.5. Modelo de depósito mineral (MineralDepositModel)

Informação organizada de forma sistematizada que descreve os atributos essenciais de uma classe de depósitos minerais. Pode ser empírica (descritiva) ou teórica (genética).

Atributos de «MineralDepositModel»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| mineralDepositGroup | Agrupamento de depósitos minerais definidos por características genéricas. | MineralDepositGroupValue |  |
| mineralDepositType | Estilo da ocorrência ou depósito mineral. | MineralDepositTypeValue | voidable |

20.3.2.6. Medida do minério (OreMeasure)

A estimativa da quantidade de minério da Reserva, do Recurso ou da Dotação.

Este tipo é abstrato.

Atributos do tipo de dados «OreMeasure»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| classificationMethodUsed | Meios de cálculo da medição. | ClassificationMethodUsedValue |  |
| date | Data do valor calculado ou estimado. | TM_GeometricPrimitive |  |
| dimension | Tamanho da massa utilizada no cálculo. | EarthResourceDimension | voidable |
| ore | Quantidade de minério. | QuantityRange |  |
| proposedExtractionMethod | Método proposto para extrair o produto de base. | Category | voidable |
| sourceReference | Referência para os valores de «OreMeasure». | DocumentCitation |  |

Associações do tipo de dados «OreMeasure»

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| measureDetails | Uma medida da quantidade de cada produto de base, baseada num cálculo da reserva, do recurso ou da dotação. | CommodityMeasure |  |

20.3.2.7. Reserva (Reserve)

A parte economicamente passível de exploração mineira de um Recurso Mineral Medido e/ou Indicado.

Este tipo é um subtipo de «OreMeasure».

Atributos do tipo de dados «Reserve»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| category | Nível de confiança da estimativa. | ReserveCategoryValue |  |

20.3.2.8. Recurso (Resource)

Uma acumulação de materiais de interesse económico intrínseco no interior ou à superfície da crosta terrestre com uma forma, qualidade e quantidade tais que cria perspetivas razoáveis quanto ao interesse económico da sua extração.

Este tipo é um subtipo de «OreMeasure».

Atributos do tipo de dados «Resource»

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| category | Indicação se o recurso é medido, indicado ou inferido. | ResourceCategoryValue |  |
| includesReserves | Uma marca que indica se a estimativa dos recursos inclui valores das reservas. | Boolean | voidable |

**20.3.3. Listas de códigos**

20.3.3.1. Método de classificação utilizado (ClassificationMethodUsedValue)

Códigos que indicam os meios utilizados para calcular a quantidade determinada de minério.

20.3.3.2. Código do produto de base (CommodityCodeValue)

Valores que indicam o tipo de produto de base.

20.3.3.3. Potencial de utilização final (EndusePotentialValue)

Valores que indicam o potencial de utilização final do mineral.

20.3.3.4. Tipo de atividade de prospeção (ExplorationActivityTypeValue)

Tipos de atividades de prospeção realizadas.

20.3.3.5. Resultado da prospeção (ExplorationResultValue)

Valores que indicam o resultado da atividade de prospeção.

20.3.3.6. Importância (ImportanceValue)

Valores que indicam a importância do produto de base no recurso terrestre.

20.3.3.7. Estatuto da mina (MineStatusValue)

Valores que indicam o estatuto operacional da mina.

20.3.3.8. Grupo de depósitos minerais (MineralDepositGroupValue)

Valores que indicam o agrupamento de depósitos minerais com base nas características genéricas destes.

20.3.3.9. Tipo de depósito mineral (MineralDepositTypeValue)

Valores que indicam o tipo de ocorrência ou depósito mineral.

20.3.3.10. Tipo de ocorrência mineral (MineralOccurrenceTypeValue)

O tipo de ocorrência mineral.

20.3.3.11. Tipo de atividade mineira (MiningActivityTypeValue)

O tipo de atividade mineira, atividade de processamento ou produção

20.3.3.12. Tipo de atividade de processamento (ProcessingActivityTypeValue)

Valores que indicam o tipo de processamento efetuado durante a atividade mineira.

20.3.3.13. Categoria da reserva (ReserveCategoryValue)

O nível de confiança da estimativa da reserva.

20.3.3.14. Categoria do recurso (ResourceCategoryValue)

Indica se o recurso é medido, indicado ou inferido.

**20.4. Requisitos específicos de categorias temáticas**

O tipo «MappedFeature» especificado no ponto 0 do anexo III deve ser utilizado para descrever as propriedades geométricas dos objetos espaciais de «MineralOccurrence».

**20.5. Camadas**

**Camadas para a categoria temática de dados geográficos «Recursos Minerais»**

| Nome da camada | Título da camada | Tipo de objeto geográfico |
|---|---|---|
| MR.Mine | Minas | MiningFeatureOccurrence |
| MR.Mineral Occurrence | Ocorrências minerais | MappedFeature (objetos geográficos cuja propriedade da especificação é do tipo «MineralOccurrence») |
