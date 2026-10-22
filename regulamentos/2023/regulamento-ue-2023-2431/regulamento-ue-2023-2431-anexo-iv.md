---
id: "regulamento-ue-2023-2431-anexo-iv"
celex: "32023R2431"
title: "Regulamento (UE) 2023/2431 da Comissão, de 24 de outubro de 2023, que altera o Regulamento (UE) n.o 1089/2010 que estabelece as disposições de execução da Diretiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Anexo IV"
type: "Regulamento"
number: "2023/2431"
year: 2023
date: 2023-10-24
status: "em vigor"
text_version: "original sem consolidação"
source: "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32023R2431"
eli: "http://data.europa.eu/eli/reg/2023/2431/oj"
retrieved: 2026-10-21
legal_notice: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
part_of: "regulamento-ue-2023-2431"
part: "Anexo IV"
---

# Regulamento (UE) 2023/2431 da Comissão, de 24 de outubro de 2023, que altera o Regulamento (UE) n.o 1089/2010 que estabelece as disposições de execução da Diretiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Anexo IV

## Anexo IV

O anexo IV do Regulamento (UE) n.º 1089/2010 é alterado do seguinte modo:

(1) No ponto 1.3.1, no proémio, a expressão «O pacote “Modelo Vetorial”» é substituída pela expressão «O pacote “Unidades Estatísticas — Modelo Vetorial”»;

(2) No ponto 1.3.1.1, o primeiro quadro é substituído pelo seguinte quadro:

| «Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| thematicId | Identificador descritivo de objeto único aplicado a objetos geográficos numa categoria temática de informação definida. | ThematicIdentifier |  |
| country | Código do país a que o objeto pertence. | CountryCode |  |
| geographicalName | Possíveis nomes geográficos do objeto. | GeographicalName |  |
| statisticalUnitType | Tipo de unidade territorial utilizada para fins de divulgação. | StatisticalUnitTypeValue |  |
| validityPeriod | Período em que supostamente a unidade estatística deve ou não ser preferencialmente utilizada. | TM_Period |  |
| referencePeriod | Período em que os dados dão supostamente uma imagem da divisão territorial em unidades estatísticas. | TM_Period |  |
| beginLifespanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifespanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable» |

(3) O ponto 1.3.3 passa a ter a seguinte redação:

\**«1.3.3. Listas de códigos**

\**1.3.3.1. Tipo de geometria (GeometryTypeValue)**

Os valores dos códigos para os tipos de geometrias.

\**1.3.3.2. Tipo de evolução (EvolutionTypeValue)**

Os valores dos códigos para tipos de evolução.

\**1.3.3.3. Tipo de unidade estatística (StatisticalUnitTypeValue)**

Os valores dos códigos para os tipos de unidades estatísticas.»;

(4) No ponto 1.4.1.1, o texto que se segue ao segundo quadro é substituído, na totalidade, pelo seguinte:

«Restrições do tipo de objeto geográfico «StatisticalGridCell”

A posição da célula deve ser dentro da quadrícula, de acordo com a sua largura e altura.

Deve ser fornecido, no mínimo, um dos atributos «code», «geographicalPosition», «gridPosition” ou «geometry».

Quando são fornecidas várias representações espaciais (“code», «geographicalPosition», «gridPosition” e «geometry»), estas devem ser coerentes.

O código deve ser constituído por:

(1) O código de duas letras do país conforme definido no Código de Redação Interinstitucional publicado pelo Serviço das Publicações da União Europeia;

(2) Uma parte de um sistema de referência de coordenadas, representada pela palavra CRS, seguida do código EPSG;

(3) Uma parte de posição e resolução:

— Se o sistema de referência de coordenadas for um sistema de projeção, a palavra RES, seguida da resolução da quadrícula em metros e da letra m. Depois, a letra N, seguida do valor da coordenada Norte em metros, e a letra E, seguida do valor da coordenada Este em metros.

— Se o sistema de referência de coordenadas não for um sistema de projeção, a palavra RES, seguida da resolução da quadrícula em graus-minutos-segundos, seguida da palavra dms. Depois, a palavra LON, seguida do valor da longitude em graus-minutos-segundos, e a palavra LAT, seguida do valor da latitude em graus-minutos-segundos.

Em ambos os casos, a posição dada deve ser a posição do canto inferior esquerdo da célula.»;

(5) O ponto 1.5 passa a ter a seguinte redação:

\**«1.5. Requisitos específicos de categorias temáticas**

(1) Deve também ser fornecida, pelo menos, a geometria das unidades estatísticas para as quais os dados estatísticos são disponibilizados no âmbito da INSPIRE. Este requisito aplica-se a categorias temáticas INSPIRE que dizem respeito a unidades estatísticas.

(2) Para fins de utilização pan-europeia, devem ser utilizadas as quadrículas com células da mesma dimensão referidas no ponto 2.2.1 do anexo II. Igualmente para fins de utilização pan-europeia, as dimensões admitidas para as células de quadrículas são 2 m, 5 m, 20 m, 50 m, 200 m, 500 m, 2 000 m, 5 000 m, 20 000 m e 50 000 m.

(3) Os dados estatísticos devem remeter para a respetiva unidade estatística através do identificador de objeto externo (“inspireId”), do identificador temático (para unidades vetoriais) ou do código da unidade (para células de quadrículas).

(4) Os dados estatísticos devem remeter para uma versão específica de uma unidade estatística.»;

(6) No ponto 2.3.1.3, o quadro é substituído pelo seguinte quadro:

| «Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| parts | Partes que compõem o edifício. | BuildingPart do pacote “Edifícios — Base” | voidable» |

(7) O ponto 2.3.3 passa a ter a seguinte redação:

\**«2.3.3. Listas de códigos**

\**2.3.3.1. Natureza do edifício (BuildingNatureValue)**

Valores que indicam a natureza de um edifício.

\**2.3.3.2. Estado da construção (ConditionOfConstructionValue)**

Valores que indicam o estado de uma construção.

\**2.3.3.3. Utilização atual (CurrentUseValue)**

Valores que indicam a utilização atual.

\**2.3.3.4. Referência altimétrica (ElevationReferenceValue)**

Lista de possíveis elementos considerados para representar uma geometria vertical.

\**2.3.3.5. Estatuto da altura (HeightStatusValue)**

Valores que indicam o método utilizado para medir uma altura.

\**2.3.3.6. Referência de geometria horizontal (HorizontalGeometryReferenceValue)**

Valores que indicam o elemento considerado para representar uma geometria horizontal.»;

(8) Nos pontos 3.1.3, 3.1.5, 3.1.9, 3.1.10, 3.1.11, 3.1.12, 3.2.1 e 3.2.5, as ocorrências de «RangeType» são substituídas por «RangeType (definido no ponto 3.2.6)»;

(9) O ponto 3.3 passa a ter a seguinte redação:

\**«3.3. Listas de códigos**

\**3.3.1. Horizonte principal FAO (FAOHorizonMasterValue)**

Uma lista de códigos da parte principal da designação de horizonte.

\**3.3.2. Horizonte subordinado FAO (FAOHorizonSubordinateValue)**

Uma lista de códigos de designações de características e distinções subordinadas dentro das camadas e horizontes principais que estão baseadas em características do perfil observáveis no terreno e são aplicadas na descrição do solo no sítio.

\**3.3.3. Plica segundo a FAO (FAOPrimeValue)**

Pode ser utilizada uma plica ou uma plica dupla para conotar o símbolo de horizonte principal do mais baixo de dois horizontes (plica) ou de três horizontes (plica dupla) que tenham prefixos idênticos em numerais árabes e combinações idênticas de carateres.

\**3.3.4. Outro tipo de notação do horizonte (OtherHorizonNotationTypeValue)**

Uma classificação de um horizonte do solo de acordo com um sistema de classificação específico.

\**3.3.5. Outro tipo de nome do solo (OtherSoilNameTypeValue)**

Uma identificação do perfil do solo de acordo com um sistema de classificação específico.

\**3.3.6. Estado do processo de génese de camadas (LayerGenesisProcessStateValue)**

Indica se o processo especificado no “layerGenesisProcess” está em curso ou cessou.

\**3.3.7. Tipo de camada (LayerTypeValue)**

Uma classificação de uma camada de acordo com o conceito de adequação à finalidade.

\**3.3.8. Nome do parâmetro do elemento do perfil (ProfileElementParameterNameValue)**

Propriedades que podem ser observadas para caracterizar o elemento do perfil.

\**3.3.9. Nome do parâmetro do objeto derivado do solo (SoilDerivedObjectParameterNameValue)**

Propriedades relacionadas com o solo que podem ser derivadas a partir de dados do solo e de outros dados.

\**3.3.10. Finalidade da investigação do solo (SoilInvestigationPurposeValue)**

Uma lista de códigos de valores possíveis indicando as razões para a realização de um levantamento.

\**3.3.11. Tipo de parcela de solo (SoilPlotTypeValue)**

Uma lista de códigos de termos que especificam em que espécie de parcela é efetuada a observação do solo.

\**3.3.12. Nome do parâmetro do perfil do solo (SoilProfileParameterNameValue)**

Propriedades que podem ser observadas para caracterizar o perfil do solo.

\**3.3.13. Nome do parâmetro de sítio do solo (SoilSiteParameterNameValue)**

Propriedades que podem ser observadas para caracterizar o sítio de solo.

\**3.3.14. Posição do qualificador WRB (WRBQualifierPlaceValue)**

Uma lista de códigos de valores que indicam a posição do qualificador relativamente ao grupo de solos de referência (RSG) da WRB. A posição pode ser antes do RSG, ou seja, “prefixo” (prefix), ou depois do RSG, ou seja, “sufixo” (suffix).

\**3.3.15. Qualificadores WRB (WRBQualifierValue)**

Uma lista de códigos de possíveis qualificadores da Base Mundial de Referência para os Recursos do Solo.

\**3.3.16. Grupo de solos de referência (RSG) da WRB (WRBReferenceSoilGroupValue)**

Uma lista de códigos de possíveis grupos de solos de referência (ou seja, primeiro nível da classificação da Base Mundial de Referência para os Recursos do Solo).

\**3.3.17. Especificadores WRB (WRBSpecifierValue)**

Uma lista de códigos de possíveis especificadores.»;

(10) O ponto 4.3.2 passa a ter a seguinte redação:

\**«4.3.2. Listas de códigos**

\**4.3.2.1. HILUCS (HILUCSValue)**

Lista de categorias de uso do solo a utilizar na categoria temática “Uso do Solo” INSPIRE.

\**4.3.2.2. Classificação do uso do solo (LandUseClassificationValue)**

Lista de categorias de uso do solo a utilizar na categoria temática “Uso do Solo” INSPIRE e acordada a nível nacional ou local.»;

(11) No ponto 4.7.2.1, o quadro é substituído pelo seguinte quadro:

| «Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| backgroundMapDate | Data do mapa de base utilizado. | DateTime |  |
| backgroundMapReference | Referência ao mapa de base utilizado. | CharacterString |  |
| backgroundMapURI | URI que referencia o serviço que fornece o mapa de base. | URI | voidable» |

(12) O ponto 4.7.3 passa a ter a seguinte redação:

\**«4.7.3. Listas de códigos**

\**4.7.3.1. Nível do plano de ordenamento do território (LevelOfSpatialPlanValue)**

Hierarquia territorial do plano.

\**4.7.3.2. Fase do processo geral (ProcessStepGeneralValue)**

Indicação geral da fase do processo de planeamento em que o plano se encontra.

\**4.7.3.3. Natureza da regulamentação (RegulationNatureValue)**

Natureza jurídica da indicação de uso do solo.

\**4.7.3.4. Nome do tipo de plano (PlanTypeNameValue)**

Tipos de planos definidos nos Estados-Membros.

\**4.7.3.5. Regulamentação suplementar específica (SpecificSupplementaryRegulationValue)**

Categoria de regulamentação suplementar fornecida numa nomenclatura específica de regulamentações suplementares fornecida pelo fornecedor de dados.

\**4.7.3.6. Regulamentação suplementar (SupplementaryRegulationValue)**

Tipos de condições e restrições nos planos de ordenamento do território.»;

(13) O ponto 5.1.6 é substituído pelo seguinte:

\**«5.1.6. Medida ambiental determinante da saúde (EnvHealthDeterminantMeasure)**

Uma medição bruta efetuada num local que seja de interesse para a análise de determinantes da saúde humana.

\**Atributos do tipo de objeto geográfico “EnvHealthDeterminantMeasure”**

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

\**Restrições do tipo de objeto geográfico “EnvHealthDeterminantMeasure”**

A medição do determinante ambiental da saúde deve ser fornecida como medida (atributo “measure”) ou como categoria de medição (atributo “category”).»;

(14) São inseridos dois pontos, 5.1.6-A e 5.1.6-B, com a seguinte redação:

\**«5.1.6-A Medição “ruído” de determinantes ambientais da saúde (EnvHealthDeterminantNoiseMeasure)**

Uma medição de ruído com interesse para a análise dos determinantes da saúde humana.

Este tipo é um subtipo de “EnvHealthDeterminantMeasure”.

\**Atributos do tipo de objeto geográfico “EnvHealthDeterminantNoiseMeasure”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| source | Tipo de fonte de ruído. | NoiseSourceTypeValue |  |

\**5.1.6-B Medição “concentração” de determinantes ambientais da saúde (EnvHealthDeterminantConcentrationMeasure)**

Uma medição de concentração com interesse para a análise dos determinantes da saúde humana.

Este tipo é um subtipo de “EnvHealthDeterminantMeasure”.

\**Atributos do tipo de objeto geográfico “EnvHealthDeterminantConcentrationMeasure”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| component | O componente cuja concentração é medida. | ComponentTypeValue |  |
| Media | O meio no qual a concentração é medida. | MediaTypeValue» |  |

(15) São suprimidos os pontos 5.2.8, 5.2.9, 5.2.10 e 5.2.11.

(16) O ponto 5.3 passa a ter a seguinte redação:

\**«5.3. Listas de códigos**

\**5.3.1. Causa de morte (CODValue)**

Dados sobre as causas de morte (Cause of Death — COD) que fornecem informações sobre os padrões de mortalidade e constituem um elemento importante da informação sobre saúde pública.

\**5.3.2. Substância química (ChemicalValue)**

Nome da substância química.

\**5.3.3. Tipo de componente ambiental da saúde (ComponentTypeValue)**

Tipo de componente específico (substância química, espécie biológica etc.) cuja concentração é medida num meio ambiental.

\**5.3.4. Tipo de medida de doença (DiseaseMeasureTypeValue)**

Diferentes formas possíveis de comunicação de dados sobre doenças e problemas de saúde conexos.

\**5.3.5. Tipo de determinante ambiental da saúde (EnvHealthDeterminantTypeValue)**

Tipo de determinante ambiental da saúde.

\**5.3.6. Tipo de saúde geral (GeneralHealthTypeValue)**

Tipo do indicador do estado de saúde.

\**5.3.7. Tipo de serviços de saúde (HealthServicesTypeValue)**

Tipo do indicador de cuidados de saúde.

\**5.3.8. Classificação internacional das doenças (ICDValue)**

Doença conforme definido na International Classification of Diseases, 10.ª revisão.

\**5.3.9. Matriz (MatrixValue)**

Tipo de sistema ou tecido humano para medição do biomarcador.

\**5.3.10. Tipo de meio ambiental de saúde (MediaTypeValue)**

O meio em que é medida a concentração de um componente da saúde.

\**5.3.11. Tipo de fonte de ruído (NoiseSourceTypeValue)**

Os valores do tipo de fonte de ruído.

\**5.3.12. Método de agregação estatística (StatisticalAggregationMethodValue)**

Os tipos de métodos estatísticos utilizados para agregar dados de medições brutos na unidade estatística.»;

(17) O ponto 6.2.2 passa a ter a seguinte redação:

\**«6.2.2. Listas de códigos**

\**6.2.2.1. Tipo de elemento acessório (AppurtenanceTypeValue)**

Classificação de elementos acessórios.

Esta lista de códigos inclui os valores constantes das listas de códigos seguintes ou de outras listas de códigos especificadas pelos fornecedores dos dados:

— Tipo de elemento acessório de rede de eletricidade (ElectricityAppurtenanceTypeValue): Classificação de elementos acessórios de redes de eletricidade, conforme especificado no ponto 6.3.2.1.

— Tipo de elemento acessório de redes de petróleo, gás e substâncias químicas (OilGasChemicalsAppurtenanceTypeValue): Classificação de elementos acessórios de redes de petróleo, gás e substâncias químicas, conforme especificado no ponto 6.4.2.1.

— Tipo de elemento acessório de rede de esgotos (SewerAppurtenanceTypeValue): Classificação de elementos acessórios de redes de esgotos, conforme especificado no ponto 6.5.2.1.

— Tipo de elemento acessório de rede térmica (ThermalAppurtenanceTypeValue): Classificação de elementos acessórios de redes térmicas, conforme especificado no ponto 6.6.2.1.

— Tipo de elemento acessório de rede de água (WaterAppurtenanceTypeValue): Classificação de elementos acessórios de redes de água, conforme especificado no ponto 6.7.2.1.

\**6.2.2.2. Tipo de elemento acessório específico (SpecificAppurtenanceTypeValue)**

Classificação de elementos acessórios específicos de domínios.

\**6.2.2.3. Tipo de fornecimento de utilidade pública (UtilityDeliveryTypeValue)**

Classificação dos tipos de fornecimento de utilidade pública.

\**6.2.2.4. Tipo de rede de utilidade pública (UtilityNetworkTypeValue)**

Classificação dos tipos de redes de utilidade pública.

\**6.2.2.5. Tipo de aviso (WarningTypeValue)**

Classificação dos tipos de avisos.»;

(18) O ponto 6.3.2 passa a ter a seguinte redação:

\**«6.3.2. Listas de códigos**

\**6.3.2.1. Tipo de elemento acessório de rede de eletricidade (ElectricityAppurtenanceTypeValue)**

Classificação de elementos acessórios de redes de eletricidade.»;

(19) O ponto 6.4.2 passa a ter a seguinte redação:

\**«6.4.2. Listas de códigos**

\**6.4.2.1. Tipo de elemento acessório de redes de petróleo, gás e substâncias químicas (OilGasChemicalsAppurtenanceTypeValue)**

Classificação de elementos acessórios de redes de petróleo, gás, substâncias químicas.

\**6.4.2.2. Tipo de produtos de petróleo, gás e substâncias químicas (OilGasChemicalsProductTypeValue)**

Classificação de produtos de petróleo, gás e substâncias químicas.»;

(20) O ponto 6.5.2 passa a ter a seguinte redação:

\**«6.5.2. Listas de códigos**

\**6.5.2.1. Tipo de elemento acessório de rede de esgotos (SewerAppurtenanceTypeValue)**

Classificação de elementos acessórios de redes de esgotos.

\**6.5.2.2. Tipo de águas de esgotos (SewerWaterTypeValue)**

Classificação dos tipos de águas de esgotos.»;

(21) O ponto 6.6.2 passa a ter a seguinte redação:

\**«6.6.2. Listas de códigos**

\**6.6.2.1. Tipo de elemento acessório de rede térmica (ThermalAppurtenanceTypeValue)**

Classificação de elementos acessórios de redes térmicas.

\**6.6.2.2. Tipo de produto térmico (ThermalProductTypeValue)**

Classificação de produtos térmicos.»;

(22) O ponto 6.7.2 passa a ter a seguinte redação:

\**«6.7.2. Listas de códigos**

\**6.7.2.1. Tipo de elemento acessório de rede de água (WaterAppurtenanceTypeValue)**

Classificação de elementos acessórios de redes de água.

\**6.7.2.2. Tipo de águas (WaterTypeValue)**

Classificação dos tipos de águas.»;

(23) O ponto 6.8.2 passa a ter a seguinte redação:

\**«6.8.2. Listas de códigos**

\**6.8.2.1. Classificação da instalação ambiental (EnvironmentalManagementFacilityTypeValue)**

Classificação das instalações ambientais, por exemplo, sítios e instalações técnicas.»;

(24) No ponto 6.9.2.2, o quadro é substituído pelo seguinte quadro:

| «Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| serviceLocationByAddress | Localização do serviço por referência a um endereço. | Address |  |
| serviceLocationByBuilding | Localização do serviço por referência a um edifício. | Building (“Edifício”) do pacote “Edifícios 2D” |  |
| serviceLocationByActivityComplex | Localização do serviço por referência a um complexo de atividades. | ActivityComplex |  |
| serviceLocationByGeometry | Localização do serviço por referência a uma geometria. | GM_Object |  |
| serviceLocationByUtilityNode | Localização do serviço por referência a um nó relacionado com uma rede de utilidade pública (água, eletricidade etc.), por exemplo hidrante ou ponto de chamada de emergência. | UtilityNode» |  |

(25) O ponto 6.9.3 passa a ter a seguinte redação:

\**«6.9.3. Listas de códigos**

\**6.9.3.1. Tipo de serviço (ServiceTypeValue)**

Lista de códigos que contém uma classificação dos serviços estatais.»;

(26) No ponto 7.1.2, o primeiro quadro é substituído pelo seguinte quadro:

| «Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| thematicId | Identificador de objeto temático. | ThematicIdentifier | voidable |
| name | Denotação em texto simples do “AbstractMonitoringObject” | CharacterString | voidable |
| additionalDescription | Descrição em texto simples de informações adicionais que não se integrem noutros atributos. | CharacterString | voidable |
| mediaMonitored | Meio ambiental monitorizado. | MediaValue |  |
| legalBackground | Contexto jurídico em que a gestão e a regulamentação do “AbstractMonitoringObject” são definidas. | LegislationCitation | voidable |
| responsibleParty | Parte responsável pelo “AbstractMonitoringObject”. | RelatedParty | voidable |
| geometry | Geometria associada ao “AbstractMonitoringObject”. Para instalações móveis, a geometria representa a área em que presumivelmente a instalação efetua medições. | GM_Object |  |
| onlineResource | Uma ligação a um documento externo que fornece outras informações sobre o “AbstractMonitoringObject”. | URL | voidable |
| purpose | Razão pela qual o “AbstractMonitoringObject” foi gerado. | PurposeOfCollectionValue | voidable» |

(27) O ponto 7.3 passa a ter a seguinte redação:

\**«7.3. Listas de códigos**

\**7.3.1. Regime de medição (MeasurementRegimeValue)**

Categorias para diferentes tipos de “MeasurementRegime”.

\**7.3.2. Meios (MediaValue)**

Categorias para diferentes tipos de meios.

\**7.3.3. Tipo de processo (ProcessTypeValue)**

Categorias para diferentes tipos de processos.

\**7.3.4. Finalidade da coleção (PurposeOfCollectionValue)**

Categorias para diferentes finalidades das coleções.

\**7.3.5. Fonte de aquisição dos resultados (ResultAcquisitionSourceValue)**

Categorias para diferentes tipos de “ResultAcquisitionSource”.

\**7.3.6. Natureza do resultado (ResultNatureValue)**

Estado do resultado de uma observação.

\**7.3.7. Tipo EMF especializado (SpecialisedEMFTypeValue)**

Categorias para diferentes tipos de “EnvironmentalMonitoringFacilities”.»;

(28) O ponto 8.2.2 é substituído pelo seguinte:

\**«8.2.2. Instalação técnica de produção (ProductionInstallation)**

Uma unidade técnica fixa, como máquinas, aparelhos, dispositivos ou equipamentos colocados em posição ou ligados para utilização, no interior da qual são realizadas uma ou mais das atividades enumeradas no anexo I do Regulamento (CE) n.º 166/2006 do Parlamento Europeu e do Conselho (*1) e no anexo I ou no anexo VII, parte 1, da Diretiva 2010/75/UE do Parlamento Europeu e do Conselho (*2) e quaisquer outras atividades a elas diretamente associadas que tenham uma relação técnica com as atividades enumeradas e possam ter efeitos nas emissões e na poluição.

\**Atributos do tipo de objeto geográfico “ProductionInstallation”**

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

\**Associações do tipo de objeto geográfico “ProductionInstallation”**

| Associação | Definição | Tipo | Voidability |
|---|---|---|---|
| groupedInstallationPart | Pequenas instalações técnicas que fazem técnica ou juridicamente parte de uma instalação técnica. | ProductionInstallationPart | Voidable |

(29) No ponto 8.2.3, o quadro é substituído pelo seguinte quadro:

| «Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| thematicId | Identificador de objeto temático. | ThematicIdentifier |  |
| pointGeometry | Propriedade espacial do objeto geográfico. | GM_Point |  |
| surfaceGeometry | Propriedade espacial do objeto geográfico. | GM_Surface | voidable |
| name | Denominação oficial ou nome próprio ou convencional da parte da instalação técnica. | CharacterString | voidable |
| description | Enunciado descritivo sobre a parte da instalação técnica. | CharacterString | voidable |
| status | Estado ou condição da parte da instalação técnica, no que se refere a funcionamento e operacionalidade, em que se a mesma se encontra durante um período limitado ou alargado. | StatusType | voidable |
| type | Género especial de uma parte da instalação técnica que denota a função operativa a desempenhar. | InstallationPartTypeValue | voidable |
| technique | Método para reduzir a concentração de poluentes decorrente das emissões de um componente técnico, geralmente uma chaminé. | PollutionAbatementTechniqueValue | voidable» |

(30) O ponto 8.4 passa a ter a seguinte redação:

\**«8.4. Listas de códigos**

\**8.4.1. Técnica de redução da poluição (PollutionAbatementTechniqueValue)**

Métodos para reduzir a concentração de poluentes decorrente das emissões de um componente técnico, geralmente uma chaminé.

\**8.4.2. Tipo de instalação técnica (InstallationTypeValue)**

Valores que denotam a função operativa a executar por uma instalação técnica.

\**8.4.3. Tipo da parte da instalação técnica (InstallationPartTypeValue)**

Valores que denotam a função operativa a executar por uma parte da instalação técnica.

\**8.4.4. Bacia hidrográfica (RiverBasinDistrictValue)**

Identificadores em código e/ou nomes atribuídos às bacias hidrográficas.

\**8.4.5. Tipo de edifício de produção (TypeOfProductionBuildingValue)**

Classificação dos edifícios industriais e de produção.»;

(31) O ponto 9.4 passa a ter a seguinte redação:

\**«9.4. Listas de códigos**

\**9.4.1. Espécies pecuárias (LivestockSpeciesValue)**

Classificação das espécies pecuárias.

\**9.4.2. Espécies aquícolas (AquacultureSpeciesValue)**

Classificação das espécies aquícolas.»;

(32) O ponto 10.3 passa a ter a seguinte redação:

\**«10.3. Listas de códigos**

\**10.3.1. Tipo de classificação (ClassificationTypeValue)**

Valores dos códigos para os tipos de classificação.

\**10.3.2. Tipo de item de classificação (ClassificationItemTypeValue)**

Valores dos códigos para os itens de classificação.

Esta lista de códigos inclui os valores constantes das listas de códigos seguintes ou de outras listas de códigos definidas pelos fornecedores dos dados:

— Idade por intervalos de cinco anos (AgeBy5YearsValue): Valores de código para itens de classificação por intervalos de idade de cinco anos.

— Idade por ano (AgeByYearValue): Valores de código para itens de classificação por idade ano a ano, compreendendo um valor para cada intervalo de um ano. O primeiro valor deve ser “0-1”, com a etiqueta “0-1” e a definição “0 a menos de 1 ano”, e o último valor deve ser “100+”, com a etiqueta “100+” e a definição “100 anos ou mais”.

— Código NACE (NACECodeValue): Classificação das atividades económicas de acordo com a Classificação NACE do Eurostat, estabelecida no Regulamento (CE) n.º 1893/2006 do Parlamento Europeu e do Conselho, e valores mais restritos definidos pelos fornecedores dos dados.

— Sexo (GenderValue): Sexo de uma pessoa ou grupo de pessoas, conforme especificado no ponto 4.7 do anexo I.

\**10.3.3. Variável (VariableValue)**

Valores dos códigos para nomes de variáveis.

\**10.3.4. Método de medição estatística (StatisticsMeasurementMethodValue)**

Valores dos códigos para o método de medição estatística.

\**10.3.5. Estatuto dos dados estatísticos (StatisticalDataStatusValue)**

Valores dos códigos para o estatuto.

\**10.3.6. Valor especial (SpecialValue)**

Valores dos códigos para valores especiais.»;

(33) O ponto 11.3 passa a ter a seguinte redação:

\**«11.3. Listas de códigos**

\**11.3.1. Código do tipo de zona (ZoneTypeCode)**

Classificação de alto nível que define o tipo de zona de gestão, restrição ou regulamentação.

\**11.3.2. Código de tipo de zona especializado (SpecialisedZoneTypeCode)**

Valor de classificação adicional que define o tipo especializado de zona.

\**11.3.3. Domínio ambiental (EnvironmentalDomain)**

Domínio ambiental relativamente ao qual podem ser definidos objetivos ambientais.»;

(34) No ponto 12.2.1, o primeiro quadro é substituído pelo seguinte quadro:

| «Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| beginLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| validFrom | Momento em que o elemento exposto começou a existir no mundo real. | DateTime | voidable |
| validTo | Momento em que o elemento exposto deixou de existir no mundo real. | DateTime | voidable» |

(35) No ponto 12.2.2, o primeiro quadro é substituído pelo seguinte quadro:

| «Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| determinationMethod | Especifica se o resultado da área de perigo é delimitado após modelização ou determinado após interpretação. | DeterminationMethodValue |  |
| endLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| typeOfHazard | Uma classificação genérica e uma classificação específica do tipo de perigo natural. | NaturalHazardClassification |  |
| validityPeriod | Escala temporal a que é aplicável o modelo. | TM_Period | voidable» |

(36) No ponto 12.2.4, o primeiro quadro é substituído pelo seguinte quadro:

| «Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| beginLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi inserida ou alterada no conjunto de dados geográficos. | DateTime | voidable |
| endLifeSpanVersion | Data e hora em que esta versão do objeto geográfico foi substituída no conjunto de dados geográficos ou dele retirada. | DateTime | voidable |
| inspireId | Identificador de objeto externo do objeto geográfico. | Identifier |  |
| sourceOfRisk | Uma classificação genérica e uma classificação específica do tipo de perigo que é a fonte do risco. | NaturalHazardClassification |  |
| validityPeriod | Escala temporal futura finita em que o modelo é aplicável. | TM_Period | voidable» |

(37) No ponto 12.3.4, o quadro é substituído pelo seguinte quadro:

| «Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| hazardCategory | Classificação genérica de tipos de perigos naturais. | NaturalHazardCategoryValue |  |
| specificHazardType | Classificação adicional do perigo natural que indica mais pormenorizadamente o tipo de perigo, de acordo com uma nomenclatura específica do conjunto de dados em causa. | SpecificHazardTypeValue | voidable» |

(38) É suprimido o ponto 12.4;

(39) O ponto 12.5 passa a ter a seguinte redação:

\**«12.5. Listas de códigos**

\**12.5.1. Categoria do elemento exposto (ExposedElementCategoryValue)**

Classificação do elemento exposto.

\**12.5.2. Categoria do perigo natural (NaturalHazardCategoryValue)**

Classificação genérica de tipos de perigos naturais.

\**12.5.3. Tipo específico do elemento exposto (SpecificExposedElementTypeValue)**

Uma denominação adicional dos elementos expostos.

\**12.5.4. Tipo específico de perigo (SpecificHazardTypeValue)**

Classificação adicional do perigo natural.

\**12.5.5. Método de determinação (DeterminationMethodValue)**

Uma lista de códigos para descrever o método utilizado para definir a área de perigo ou de risco.»;

(40) O ponto 13.1 passa a ter a seguinte redação:

\**«13.1. Estrutura da categoria temática de dados geográficos “Condições Atmosféricas e Características Geometeorológicas”**

Os tipos especificados para as categorias temáticas de dados geográficos “Condições Atmosféricas” e “Características Geometeorológicas” estão estruturados nos seguintes pacotes:

— Condições atmosféricas e características geometeorológicas

— Observações especializadas (Specialised Observations) (especificadas no ponto 7.4 do anexo I)

— Processos (Processes) (especificados no ponto 7.2 do anexo I)

— Propriedades observáveis (Observable Properties) (especificadas no ponto 7.3 do anexo I)

— Referências de observações (Observation References) (especificadas no ponto 7.1 do anexo I)»;

(41) O ponto 13.2.1 passa a ter a seguinte redação:

\**«13.2.1. Listas de códigos**

\**13.2.1.1. Componente de referência da qualidade do ar da UE (EU_AirQualityReferenceComponentValue)**

Definições de fenómenos relativos à qualidade do ar no contexto da comunicação de informações ao abrigo da legislação da União.

\**13.2.1.2. Quadro 4.2 de Códigos e Marcadores do formato GRIB da Organização Meteorológica Mundial (GRIB_CodeTable4_2Value)**

Definições de fenómenos observados em meteorologia.»;

(42) O ponto 14.2.1 passa a ter a seguinte redação:

\**«14.2.1. Listas de códigos**

\**14.2.1.1. Utilização do parâmetro BODC P01 (BODC_P01ParameterUsageValue)**

Definições de fenómenos observados em oceanografia.»;

(43) O ponto 15.1.2 passa a ter a seguinte redação:

\**«15.1.2. Mar (Sea)**

Extensão de mar na maré alta (meanHighWater).

Este tipo é um subtipo de “SeaArea”.

Restrições do tipo de objeto geográfico “Sea”

“Sea” (mar) é definido ao nível médio da maré alta. Esta restrição pode não ser observada se não houver uma variação significativa no nível de água das marés.

Os tipos de objetos geográficos do tipo “Sea” devem ter apenas um valor para o atributo “extent”.»;

(44) O ponto 15.1.3 é substituído pelo seguinte:

\**«15.1.3. Zona marinha de circulação (MarineCirculationZone)**

Uma área marinha definida pelos seus padrões de circulação física e química. Geralmente utilizada para fins de gestão e comunicação de informações sobre o meio marinho ou para fins de classificação ambiental do meio marinho.

Este tipo é um subtipo de “SeaArea”.

Atributos do tipo de objeto geográfico “MarineCirculationZone”

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| zoneType | Tipo de zona marinha de circulação, por exemplo, “sedimentCell”. | ZoneTypeValue |  |

Restrições do tipo de objeto geográfico “MarineCirculationZone”

Os tipos de objetos geográficos do tipo MarineCirculationZone devem ter apenas um valor para o atributo “extent”.»;

(45) O ponto 15.1.6 é suprimido;

(46) É aditado um ponto 15.2.4, com a seguinte redação:

\**«15.2.4. Segmento da margem (ShoreSegment)**

Um segmento da margem é uma secção da “shoreline” (linha de margem).

\**Atributos do tipo de dados “ShoreSegment”**

| Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| geometry | Geometria do “ShoreSegment”. | GM_Curve |  |
| shoreClassification | Tipo primário do segmento da margem tirado da lista de códigos de “ShoreTypeClassificationValue”. | ShoreTypeClassificationValue | voidable |
| shoreStability | Tipo primário de estabilidade do segmento da margem tirado da lista de códigos de “ShoreStabilityValue”. | ShoreStabilityValue | voidable» |

(47) O ponto 15.3 passa a ter a seguinte redação:

\**«15.3. Listas de códigos**

\**15.3.1. Classificação do tipo de área marinha (SeaAreaTypeClassificationValue)**

Tipo de classificação da “SeaArea”, por exemplo “estuary”, “openOcean”.

\**15.3.2. Cobertura do fundo marinho (SeaBedCoverValue)**

Tipos de cobertura encontrados nos fundos marinhos.

\**15.3.3. Classificação da superfície marinha (SeaSurfaceClassificationValue)**

Tipos de camadas de superfícies marinhas observados em superfícies marinhas.

\**15.3.4. Estabilidade da margem (ShoreStabilityValue)**

Tipos de estabilidade de segmentos da margem.

\**15.3.5. Classificação do tipo de margem (ShoreTypeClassificationValue)**

Tipos de segmentos da margem.

\**15.3.6. Tipo de zona (ZoneTypeValue)**

Tipos de zonas marinhas de circulação.»;

(48) O ponto 16.2 passa a ter a seguinte redação:

\**«16.2. Listas de códigos**

\**16.2.1. Nível de classificação das regiões (RegionClassificationLevelValue)**

Códigos que definem o nível de classificação da classe de regiões.

\**16.2.2. Sistema de classificação de regiões (RegionClassificationSchemeValue)**

Códigos que definem as várias regiões biogeográficas.

\**16.2.3. Classificação de regiões (RegionClassificationValue)**

Códigos utilizados para definir as várias regiões biogeográficas.

Esta lista de códigos inclui os valores constantes das listas de códigos seguintes ou de outras listas de códigos definidas pelos fornecedores dos dados:

— Classificação da estratificação ambiental (“EnvironmentalStratificationClassificationValue”): Códigos para a estratificação climática do ambiente na União, conforme especificado em Metzger, M.J., Shkaruba, A.D., Jongman, R.H.G., Bunce, R.G.H., Descriptions of the European Environmental Zones and Strata. Alterra, Wageningen, 2012.

— Classificação da Diretiva-Quadro Estratégia Marinha (MarineStrategyFrameworkDirectiveClassificationValue): Códigos da classificação da Diretiva-Quadro Estratégia Marinha, enumerados no artigo 4.º da Diretiva 2008/56/CE do Parlamento Europeu e do Conselho (*3)

.

— Classificação das Regiões Biogeográficas Natura 2000 e da Rede Emerald (Natura2000AndEmeraldBio-geographicalRegionClassificationValue): Codes for the classification of bio-geographical regions, as specified in the Code List for Bio-geographical Regions, Europe 2011, publicados no sítio Web da Agência Europeia do Ambiente.

— Classificação da Vegetação Natural (NaturalVegetationClassificationValue): Códigos para a classificação da vegetação natural, conforme especificado nas principais formações em Bohn, U., Gollub, G., Hettwer, C., Map of the natural vegetation of Europe: scale 1:2,500,000, Part 2: Legend, Bundesamt für Naturschutz (Agência Federal Alemã para a Conservação da Natureza), Bona, 2000.»;

(*3) Diretiva 2008/56/CE do Parlamento Europeu e do conselho, de 17 de junho de 2008, que estabelece um quadro de ação comunitária no domínio da política para o meio marinho (Diretiva-Quadro «Estratégia Marinha») (JO L 164 de 25.6.2008, p. 19.)»

"

(49) O ponto 17.4 passa a ter a seguinte redação:

\**«17.4. Listas de códigos**

\**17.4.1. Nome do qualificador local (QualifierLocalNameValue)**

Lista de valores que especificam a relação entre um nome utilizado localmente e um nome utilizado a nível pan-europeu.

\**17.4.2. Código do tipo de habitat de referência (ReferenceHabitatTypeCodeValue)**

Valores utilizados nos sistemas de classificação de habitats pan-europeus.

Esta lista de códigos compreende os valores das seguintes listas de códigos:

— Código de Tipo de Habitat EUNIS (EunisHabitatTypeCodeValue): Classificação dos tipos de habitats de acordo com a base de dados Biodiversidade EUNIS, conforme especificado na classificação de tipos de habitats EUNIS publicada no sítio Web da Agência Europeia do Ambiente.

— Código da Diretiva Habitats (HabitatsDirectiveCodeValue): Classificação dos tipos de habitats de acordo com o anexo I da Diretiva 92/43/CEE.

— Código da Diretiva-Quadro Estratégia Marinha (MarineStrategyFrameworkDirectiveCodeValue): Classificação de tipos de habitats de acordo com o quadro 1 do anexo III da Diretiva 2008/56/CE.

\**17.4.3. Sistema de tipos de habitats de referência (ReferenceHabitatTypeSchemeValue)**

Este valor define qual foi o sistema de classificação de habitats pan-europeu utilizado.

\**17.4.4. Código do nome local (LocalNameCodeValue)**

Identificador tirado de um sistema de classificação local.»;

(50) No quadro do ponto 18.3.2, na terceira entrada, «populationSize», a expressão «RangeType» que figura na terceira coluna é substituída por «RangeType (definido no ponto 18.3.3)»;

(51) O ponto 18.4 passa a ter a seguinte redação:

\**«18.4. Listas de códigos**

\**18.4.1. Método de contagem (CountingMethodValue)**

Método para a produção de números que indicam a abundância de uma espécie numa unidade agregada.

\**18.4.2. Unidade de contagem (CountingUnitValue)**

Unidade definida utilizada para exprimir um número contado ou estimado que indica a abundância de uma espécie numa “SpeciesDistributionUnit”.

\**18.4.3. Código do nome da espécie local (LocalSpeciesNameCodeValue)**

Identificador da espécie proveniente de um sistema de classificação local.

\**18.4.4. Categoria da ocorrência (OccurrenceCategoryValue)**

Densidade populacional da espécie na “SpeciesDistributionUnit”.

\**18.4.5. Tipo de população (PopulationTypeValue)**

A permanência das populações, em particular no que se refere às espécies migratórias, numa dada unidade de distribuição de espécies.

\**18.4.6. Qualificador (QualifierValue)**

Este valor define a relação entre os conceitos taxonómicos de um nome de espécie local e o nome de referência da espécie dado pelo identificador de referência da espécie ou por um sistema de referência de espécies.

\**18.4.7. Código de espécies de referência (ReferenceSpeciesCodeValue)**

Listas de referência que contêm identificadores das espécies.

Esta lista de códigos compreende os valores das seguintes listas de códigos:

— Código EU-Nomen (EuNomenCodeValue): Listas de referência que contêm os identificadores de espécies EU-Nomen, conforme especificado na Infraestrutura Pan-Europeia de Diretórios de Espécies disponível através do Portal EU-Nomen.

— Código de Espécies EUNIS (EunisSpeciesCodeValue): Listas de referência que contêm os identificadores de espécies EUNIS, conforme especificado na base de dados de Biodiversidade EUNIS publicada no sítio Web da Agência Europeia do Ambiente.

— Código das Diretivas Natureza (NatureDirectivesCodeValue): Listas de referência que contêm os identificadores de espécies das Diretivas Natureza, conforme especificado no Portal de Referência da Rede Natura 2000 e definido na Decisão de Execução 2011/484/UE da Comissão (*4).

\**18.4.8. Sistema de espécies de referência (ReferenceSpeciesSchemeValue)**

Listas de referência que definem um padrão de nomenclatura e taxonomia em função do qual se pode proceder ao levantamento dos nomes e conceitos taxonómicos locais.

\**18.4.9. Estatuto de residência (ResidencyStatusValue)**

Categoria de residência das ocorrências ou população estimada dentro de uma determinada unidade agregada.

(*4) Decisão de Execução 2011/484/UE da Comissão, de 11 de julho de 2011, relativa a um formulário de informações sobre os sítios da rede Natura 2000 (JO L 198 de 30.7.2011, p. 39).»

"

(52) No ponto 19.3.1.3, o quadro é substituído pelo seguinte quadro:

| «Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| range | Gama dos números que representam a gama de altura ou profundidade de um recurso energético. | VerticalExtentRangeType |  |
| scalar | Número que representa a altura ou profundidade de um recurso energético. | Length» |  |

(53) O ponto 19.3.2 passa a ter a seguinte redação:

\**«19.3.2. Listas de códigos**

\**19.3.2.1. Quadro de classificação e quantificação (ClassificationAndQuantificationFrameworkValue)**

Valores para os sistemas de classificação mais amplamente utilizados para classificar e quantificar os recursos energéticos.

\**19.3.2.2. Classe de combustíveis fósseis (FossilFuelClassValue)**

Valores que indicam os vários níveis de recursos de combustíveis fósseis.

\**19.3.2.3. Energias renováveis e resíduos (RenewableAndWasteValue)**

Tipos de recursos em energias renováveis e resíduos.

\**19.3.2.4. Combustível fóssil (FossilFuelValue)**

Tipos de combustíveis fósseis.

\**19.3.2.5. Referência vertical (VerticalReferenceValue)**

Valores que indicam o nível de referência da extensão vertical.»;

(54) No ponto 19.4.2.5, o quadro é substituído pelo seguinte quadro:

| «Atributo | Definição | Tipo | Voidability |
|---|---|---|---|
| calorificValue | Cada recurso de combustíveis fósseis é caracterizado em função do seu valor calorífico, ou seja, a quantidade de energia disponível numa unidade de massa. | CalorificValueType | voidable |
| quantity | Quantidade do recurso de acordo com a categorização específica. | FossilFuelMeasure | voidable» |
| typeOfResource | Tipo de combustível fóssil. | FossilFuelValue |  |

(55) O ponto 19.5.2 passa a ter a seguinte redação:

\**«19.5.2. Listas de códigos**

\**19.5.2.1. Tipo potencial (PotentialTypeValue)**

Tipos de energia potencial a partir de recursos de energias renováveis e resíduos.»;

(56) O ponto 20.3.3 passa a ter a seguinte redação:

\**«20.3.3. Listas de códigos**

\**20.3.3.1. Método de classificação utilizado (ClassificationMethodUsedValue)**

Códigos que indicam os meios utilizados para calcular a quantidade determinada de minério.

\**20.3.3.2. Código do produto de base (CommodityCodeValue)**

Valores que indicam o tipo de produto de base.

\**20.3.3.3. Potencial de utilização final (EndusePotentialValue)**

Valores que indicam o potencial de utilização final do mineral.

\**20.3.3.4. Tipo de atividade de prospeção (ExplorationActivityTypeValue)**

Tipos de atividades de prospeção realizadas.

\**20.3.3.5. Resultado da prospeção (ExplorationResultValue)**

Valores que indicam o resultado da atividade de prospeção.

\**20.3.3.6. Importância (ImportanceValue)**

Valores que indicam a importância do produto de base no recurso terrestre.

\**20.3.3.7. Estatuto da mina (MineStatusValue)**

Valores que indicam o estatuto operacional da mina.

\**20.3.3.8. Grupo de depósitos minerais (MineralDepositGroupValue)**

Valores que indicam o agrupamento de depósitos minerais com base nas características genéricas destes.

\**20.3.3.9. Tipo de depósito mineral (MineralDepositTypeValue)**

Valores que indicam o tipo de ocorrência ou depósito mineral.

\**20.3.3.10. Tipo de ocorrência mineral (MineralOccurrenceTypeValue)**

O tipo de ocorrência mineral.

\**20.3.3.11. Tipo de atividade mineira (MiningActivityTypeValue)**

O tipo de atividade mineira, atividade de processamento ou produção

\**20.3.3.12. Tipo de atividade de processamento (ProcessingActivityTypeValue)**

Valores que indicam o tipo de processamento efetuado durante a atividade mineira.

\**20.3.3.13. Categoria da reserva (ReserveCategoryValue)**

O nível de confiança da estimativa da reserva.

\**20.3.3.14. Categoria do recurso (ResourceCategoryValue)**

Indica se o recurso é medido, indicado ou inferido.»

(*1) Regulamento (CE) n.º 166/2006 do Parlamento Europeu e do Conselho, de 18 de janeiro de 2006, relativo à criação do Registo Europeu das Emissões e Transferências de Poluentes e que altera as Diretivas 91/689/CEE e 96/61/CE do Conselho (JO L 33 de 4.2.2006, p. 1).

(*2) Diretiva 2010/75/UE do Parlamento Europeu e do Conselho, de 24 de novembro de 2010, relativa às emissões industriais (prevenção e controlo integrados da poluição) (JO L 334 de 17.12.2010. p. 17).»

(*3) Diretiva 2008/56/CE do Parlamento Europeu e do conselho, de 17 de junho de 2008, que estabelece um quadro de ação comunitária no domínio da política para o meio marinho (Diretiva-Quadro «Estratégia Marinha») (JO L 164 de 25.6.2008, p. 19.)»

(*4) Decisão de Execução 2011/484/UE da Comissão, de 11 de julho de 2011, relativa a um formulário de informações sobre os sítios da rede Natura 2000 (JO L 198 de 30.7.2011, p. 39).»

”

ELI: http://data.europa.eu/eli/reg/2023/2431/oj

ISSN 1977-0774 (electronic edition)
