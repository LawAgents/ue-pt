---
id: "regulamento-ue-2017-2400-anexo-iii"
celex: "32017R2400"
title: "Regulamento (UE) 2017/2400 da Comissão, de 12 de dezembro de 2017, que dá execução ao Regulamento (CE) n.° 595/2009 do Parlamento Europeu e do Conselho no que respeita à determinação das emissões de CO2 e ao consumo de combustível dos veículos pesados e altera a Diretiva 2007/46/CE do Parlamento Europeu e do Conselho e o Regulamento (UE) n.° 582/2011 do Conselho e da Comissão (Texto relevante para efeitos do EEE. ) — Anexo III"
type: "Regulamento"
number: "2017/2400"
year: 2017
date: 2017-12-12
status: "em vigor"
text_version: "consolidado"
last_amended: 2026-01-01
consolidated_celex: "02017R2400-20260101"
source: "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:02017R2400-20260101"
eli: "http://data.europa.eu/eli/reg/2017/2400/oj"
retrieved: 2026-10-21
legal_notice: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
part_of: "regulamento-ue-2017-2400"
part: "Anexo III"
---

# Regulamento (UE) 2017/2400 da Comissão, de 12 de dezembro de 2017, que dá execução ao Regulamento (CE) n.° 595/2009 do Parlamento Europeu e do Conselho no que respeita à determinação das emissões de CO2 e ao consumo de combustível dos veículos pesados e altera a Diretiva 2007/46/CE do Parlamento Europeu e do Conselho e o Regulamento (UE) n.° 582/2011 do Conselho e da Comissão (Texto relevante para efeitos do EEE. ) — Anexo III

## Anexo III

**INFORMAÇÃO DE ENTRADA RELATIVA ÀS CARACTERÍSTICAS DO VEÍCULO**

**1. Introdução**

O presente anexo descreve a lista de parâmetros que devem ser fornecidos pelo fabricante do veículo para inserção na ferramenta de simulação. O modelo XML aplicável e vários exemplos de dados estão disponíveis na plataforma de distribuição eletrónica específica.

**2. Definições**

(1) «ID do parâmetro»: identificador único utilizado na ferramenta de simulação para um determinado parâmetro de entrada ou conjunto de dados de entrada;

(2) «Tipo»: tipo de dados do parâmetro;

| «string» … | sequência de carateres na codificação ISO8859-1; |
|---|---|

| «token» … | sequência de carateres na codificação ISO8859-1, sem espaços em branco à frente e atrás; |
|---|---|

| «date» … | data e hora TUC com o seguinte formato: AAAA-MM-DDTHH:MM:SSZ com carateres em itálico representando carateres fixos, p. ex., «2002-05-30T09:30:10Z»; |
|---|---|

| «integer» … | valor com um tipo de dados inteiro, sem zeros à frente, p. ex., «1 800 »; |
|---|---|

| «double, X» … | número fracionário contendo exatamente X dígitos a seguir ao sinal decimal («.») e sem zeros à frente, p. ex., «double, 2»: «2 345,67 »; para «double, 4»: «45.6780»; |
|---|---|

(3) «Unidade» … unidade física do parâmetro;

(4) «Massa efetiva do veículo corrigida»: a massa especificada na «massa efetiva do veículo» em conformidade com o Regulamento (UE) n.º 1230/2012 da Comissão (*), com exceção do(s) reservatório(s) que deve(m) ser enchido(s) a, pelo menos, 50 % da(s) sua(s) capacidade(s). Os sistemas contendo líquidos são enchidos até 100 % da capacidade especificada pelo fabricante, com exceção dos que se destinam a águas residuais, que devem permanecer vazios.

No caso dos camiões rígidos médios, dos camiões rígidos pesados e dos tratores, a massa é determinada sem superstrutura e corrigida pelo peso adicional do equipamento-padrão não instalado, conforme especificado no ponto 4.3. A massa de uma carroçaria-padrão, semirreboque-padrão ou reboque-padrão para simular o veículo completo ou a combinação veículo completo-(semi)reboque é adicionada automaticamente pela ferramenta de simulação. Todas as partes montadas em ou por cima da estrutura principal são consideradas partes da superestrutura, se estiverem instaladas apenas para facilitar uma superstrutura, independentemente das peças que são necessárias para as condições em ordem de marcha.

No caso dos autocarros pesados que são veículos primários, a «massa efetiva do veículo corrigida» não é aplicável, uma vez que o valor genérico da massa é atribuído pela ferramenta de simulação;

(5) «Altura da carroçaria integrada»: a diferença, na direção «Z», entre o ponto de referência «A» do ponto mais alto e o ponto mais baixo «B» de uma carroçaria integrada (ver figura 1). Aos veículos que se desviam do caso normal aplicam-se os seguintes casos (ver figura 2):

Caso especial 1, dois níveis: A altura da carroçaria integrada é a média de h1 e h2, em que:

— h1 é a diferença entre o ponto A, mas determinado na secção transversal do veículo na extremidade traseira da primeira porta de passageiros, e o ponto B,

— h2 é a diferença entre o ponto A e o ponto B.

Caso especial 2, inclinado: A altura da carroçaria integrada é a média de h1 e h2, em que:

— h1 é a diferença entre o ponto A, mas determinado na secção transversal do veículo na extremidade traseira da primeira porta de passageiros, e o ponto B,

— h2 é a diferença entre o ponto A e o ponto B.

Caso especial 3, apenas com secção de tejadilho:

— altura da carroçaria integrada determinada na secção de tejadilho existente.

Caso especial 4, sem tejadilho:

— a altura da carroçaria integrada é a diferença entre o ponto mais elevado do veículo a um metro na direção longitudinal do para-brisas ou do para-brisas superior, no caso de um veículo de dois andares, e o ponto B.

Para todos os outros casos não abrangidos pelo caso normal ou pelos casos especiais 1 a 4, a altura da carroçaria integrada é a diferença entre o ponto mais elevado do veículo e o ponto B. Este parâmetro é relevante apenas para os autocarros pesados.

Figura 1

Altura da carroçaria integrada — caso normal

image

Figura 2

Altura da carroçaria integrada — casos especiais

image

(6) O ponto de referência «A» é o ponto mais alto da carroçaria (figura 1). Não devem ser considerados painéis de carroçaria e/ou de design, suportes para montagem, por exemplo, de sistemas AVAC, escotilhas e elementos semelhantes;

(7) O ponto de referência «B» é o ponto mais baixo do bordo inferior da parte exterior da carroçaria (figura 1). Os suportes, por exemplo, para a montagem dos eixos, não devem ser tidos em conta;

(8) «Comprimento do veículo»: a dimensão do veículo em conformidade com o quadro I constante do anexo I, apêndice 1, do Regulamento (UE) n.º 1230/2012; Além disso, não devem ser tidos em conta os dispositivos de suporte de carga amovíveis, os dispositivos de engate não amovíveis e quaisquer outras partes exteriores não amovíveis que não afetem o espaço utilizável pelos passageiros. Este parâmetro só é relevante para os autocarros pesados;

(9) «Largura do veículo»: a dimensão do veículo em conformidade com o quadro II constante do anexo I, apêndice 1, do Regulamento (UE) n.º 1230/2012. Em derrogação destas disposições, os dispositivos de suporte de carga amovíveis, os dispositivos de engate não amovíveis e quaisquer outras partes exteriores não amovíveis que não afetem o espaço utilizável pelos passageiros não devem ser considerados;

(10) «Altura de entrada em posição não inclinada»: o nível do piso acima do solo medido na primeira abertura da porta mais dianteira do veículo quando este se encontra na posição não inclinada (sistema de kneeling não acionado);

(11) «Pilha de combustível»: um conversor de energia que transforma energia química (à entrada) em energia elétrica (à saída) ou vice-versa;

(12) «Veículo a pilha de combustível» ou «FCV» (fuel cell vehicle): um veículo cujo grupo motopropulsor contém conversor(es) de energia de propulsão que consistem exclusivamente em pilha(s) de combustível e máquina(s) elétrica(s):

(13) «Veículo híbrido a pilha de combustível» ou «FCHV» (fuel cell hybrid vehicle): um veículo com pilha de combustível equipado com um grupo motopropulsor que contém, pelo menos, um sistema de armazenamento de combustível e, pelo menos, um sistema recarregável de armazenamento de energia elétrica como sistemas de armazenamento de energia de propulsão;

(14) «Veículo MCI puro»: um veículo em que todos os conversores de energia de propulsão são motores de combustão interna;

(15) «Máquina elétrica» ou «ME»: um conversor de energia que transforma energia elétrica em energia mecânica e vice-versa;

(16) «Sistema de armazenamento de energia»: um sistema que armazena energia e liberta-a sob a mesma forma da energia de entrada;

(17) «Sistema de armazenamento de energia de propulsão»: um sistema de armazenamento de energia do grupo motopropulsor que não seja um dispositivo periférico, cuja energia de saída é utilizada direta ou indiretamente para fins de propulsão do veículo;

(18) «Categoria de sistema de armazenamento de energia de propulsão»: um sistema de armazenamento de combustível, um sistema recarregável de armazenamento de energia elétrica (SRAEE) ou um sistema recarregável de armazenamento de energia mecânica;

(19) «A jusante»: uma posição no grupo motopropulsor do veículo mais próxima das rodas do que a posição real de referência;

(20) «Sistema de tração»: os elementos do grupo motopropulsor ligados entre si para efeitos da transmissão da energia mecânica entre o(s) conversor(es) de energia de propulsão e as rodas;

(21) «Conversor de energia»: um sistema no qual a energia de saída é diferente da energia de entrada;

(22) «Conversor de energia de propulsão»: um conversor de energia do grupo motopropulsor que não seja um dispositivo periférico, cuja energia de saída é utilizada direta ou indiretamente para fins de propulsão do veículo;

(23) «Categoria de conversor de energia de propulsão»: um motor de combustão interna, uma máquina elétrica ou uma pilha de combustível;

(24) «Forma de energia»: energia elétrica, mecânica ou química (incluindo combustíveis);

(25) «Sistema de armazenamento de combustível»: um sistema de armazenamento de energia de propulsão que armazena energia química enquanto combustível líquido ou gasoso;

(26) «Veículo híbrido» ou «HV» (hybrid vehicle): um veículo cujo grupo motopropulsor contém pelo menos duas categorias distintas de conversores de energia de propulsão e pelo menos duas categorias distintas de sistemas de armazenamento de energia de propulsão;

(27) «Veículo híbrido elétrico» ou «VHE»: um veículo híbrido em que um dos conversores de energia de propulsão é uma máquina elétrica e o outro é um motor de combustão interna;

(28) «VHE de série»: um VHE com uma arquitetura do grupo motopropulsor em que o MCI alimenta um ou mais canais de conversão de energia elétrica sem ligação mecânica entre o MCI e as rodas do veículo;

(29) «Motor de combustão interna» ou «MCI»: um conversor de energia com oxidação intermitente ou contínua de combustível que transforma energia química em energia mecânica;

(30) «Veículo híbrido elétrico com carregamento do exterior» ou «VHE-CE»: um veículo híbrido elétrico que pode ser carregado a partir de uma fonte exterior;

(31) «VHE paralelo»: um VHE com uma arquitetura do grupo motopropulsor em que o MCI alimenta apenas um único canal ligado mecanicamente entre o motor e as rodas do veículo;

(32) «Dispositivos periféricos»: qualquer dispositivo que consome, converte, armazena ou fornece energia que não é utilizada, direta ou indiretamente, para a propulsão do veículo, mas é essencial para o funcionamento do grupo motopropulsor;

(33) «Grupo motopropulsor», todo o conjunto de sistema(s) de armazenamento de energia de propulsão, conversor(es) de energia de propulsão e sistema(s) de tração que fornece energia mecânica às rodas de um veículo para efeitos de propulsão, incluindo os dispositivos periféricos;

(34) «Veículo exclusivamente elétrico» ou «VEE»: um veículo a motor nos termos do Regulamento (UE) 2018/858, artigo 3.º, ponto 16, equipado com um grupo motopropulsor que contém exclusivamente máquinas elétricas como conversores de energia de propulsão e sistemas recarregáveis de armazenamento de energia elétrica como sistemas de armazenamento de energia de propulsão e/ou, em alternativa, quaisquer outros meios de fornecimento condutor ou indutivo direto de energia elétrica a partir da rede elétrica que forneçam a energia de propulsão ao veículo a motor;

(35) «A montante»: uma posição no grupo motopropulsor do veículo mais afastada das rodas do que a posição real de referência;

(36) «IEPC»: um componente do grupo motopropulsor elétrico integrado (integrated electric powertrain component) em conformidade com o anexo X-B, ponto 2, subponto 36;

(37) «IHPC tipo 1»: um componente do grupo motopropulsor híbrido elétrico integrado (integrated hybrid electric vehicle powertrain component) do tipo 1 em conformidade com o anexo X-B, ponto 2, subponto 38;

(38) «Tecnologia de carregamento dinâmico»: tecnologia que permite ligar o veículo em movimento a uma fonte externa de energia elétrica, fornecendo energia diretamente aos sistemas de propulsão e/ou auxiliares do veículo e/ou carregando as baterias;

(39) «Pantógrafo aéreo»: tecnologia de carregamento dinâmico para ligação e alimentação elétrica com a infraestrutura da catenária nas estradas;

(40) «Pértiga aérea»: tecnologia de carregamento dinâmico com varas coletoras de corrente para ligação com a infraestrutura da catenária;

(41) «Calha no solo»: tecnologia de carregamento dinâmico que transfere condutivamente a energia elétrica para o veículo através de calhas incorporadas na estrada ou sobre a sua superfície;

(42) «Sem fios»: tecnologia de carregamento dinâmico que transfere indutivamente a energia elétrica para o veículo através de dispositivos incorporados na estrada ou sobre a sua superfície, fornecendo campos magnéticos;

(43) «Hidrogénio gasoso comprimido»: tecnologia de armazenamento de hidrogénio que armazena hidrogénio em forma gasosa;

(44) «Hidrogénio líquido»: tecnologia de armazenamento de hidrogénio que armazena hidrogénio em forma líquida;

(45) «Hidrogénio criocomprimido»: tecnologia de armazenamento de hidrogénio que armazena hidrogénio a temperaturas desde próximo da liquefação até à temperatura ambiente e a uma pressão de, pelo menos, 200 bar. A tecnologia de armazenamento de hidrogénio pode ser capaz de funcionar à temperatura ambiente, mas a sua capacidade nominal só pode ser atingida próximo da temperatura de liquefação do hidrogénio;

(46) «Estado vazio do reservatório de hidrogénio»: o estado de um reservatório de hidrogénio a partir do qual ainda é possível atingir um reservatório cheio num único evento de reabastecimento sem ventilação e que satisfaz uma das seguintes condições:

a) Abaixo desse estado, é apresentada ao condutor uma indicação de «vazio», «quase vazio» ou semelhante;

b) Abaixo desse estado, o sistema de conversão de energia do hidrogénio proporciona um desempenho significativamente limitado;

(47) «Veículo híbrido com carregamento do exterior» ou «VH-CE»: um veículo híbrido que pode ser carregado a partir de uma fonte exterior;

(48) «Veículo híbrido a pilha de combustível com carregamento do exterior» ou «VH-PCCE»: um veículo híbrido a pilha de combustível que pode ser carregado a partir de uma fonte exterior;

(49) «Modo a selecionar pelo condutor»: uma determinada condição a selecionar pelo condutor suscetível de afetar as emissões ou o consumo de combustível e/ou energia;

(50) «Modo predominante»: um único modo a selecionar pelo condutor que é sempre selecionado quando o veículo é ligado, independentemente do modo a selecionar pelo condutor que estava ativado quando o veículo foi previamente desligado, que satisfaz as seguintes condições:

a) Não pode ser redefinido para outro modo;

b) Só pode ser comutado para outro modo a selecionar pelo condutor por uma ação intencional do condutor depois de o veículo ter sido ligado;

(51) «Modo predominante apenas a bateria», um modo predominante em que um VH-CE funciona com a energia de propulsão fornecida exclusivamente pelo SRAEE.

**3. Conjunto de parâmetros de entrada**

Nos quadros 1 a 17, são especificados os conjuntos de parâmetros de entrada a fornecer relativamente às características do veículo. São definidos diferentes conjuntos consoante o caso de aplicação (camiões médios, camiões pesados e autocarros pesados).

No caso dos autocarros pesados, é feita uma distinção entre os parâmetros de entrada a fornecer para as simulações no veículo primário e para as simulações no veículo completo ou completado. Aplicam-se as seguintes disposições:

— Os fabricantes de veículos primários devem fornecer todos os parâmetros enumerados na coluna do veículo primário.

— Os fabricantes de veículos primários podem, além disso, fornecer parâmetros de entrada adicionais relacionados com o veículo completo ou completado, que podem ser determinados já nesta fase inicial. Neste caso, devem ser fornecidas informações sobre o fabricante (P235), o endereço do fabricante (P252), o NIV (P238) e a data (P239), tanto para o conjunto de parâmetros de entrada primários como para o conjunto de parâmetros de entrada adicionais.

— Os fabricantes intermédios devem fornecer parâmetros de entrada relativos ao veículo completo ou completado que possam ser determinados nesta fase e que estejam sob a sua responsabilidade. Se um parâmetro já fornecido numa fase de fabrico anterior for atualizado, deve ser especificado todo o estado do parâmetro (por exemplo, se for adicionada uma segunda bomba de calor ao veículo, deve ser fornecida a tecnologia de ambos os sistemas). Informações sobre o fabricante (P235), endereço do fabricante (P252), NIV (P238) e data (P239) devem ser fornecidas pelos fabricantes intermédios em todos os casos;

— Os fabricantes do veículo completado devem fornecer parâmetros de entrada que possam ser determinados nesta fase e que estejam sob a sua responsabilidade. Para as atualizações necessárias de parâmetros já fornecidos em fases de fabrico anteriores, aplicam-se as mesmas disposições que para os fabricantes intermédios. As informações sobre o fabricante (P235), endereço do fabricante (P252), NIV (P238), data (P239) e massa efetiva corrigida (P038) devem ser fornecidas em todos os casos. Para poder efetuar as simulações necessárias, o conjunto de dados consolidados de todas as fases de fabrico deve conter todas as informações enumeradas na coluna relativa ao veículo completo ou completado;

— Os fabricantes relacionados com a fase completa devem fornecer todos os parâmetros de entrada. Devem ser fornecidas informações sobre o fabricante (P235), o endereço do fabricante (P252), o NIV (P238) e a data (P239), tanto para os parâmetros primários de entrada como para os parâmetros de entrada do veículo completo;

— O parâmetro «VehicleDeclarationType» (P293) deve ser fornecido por todas as fases de fabrico que forneçam qualquer um dos parâmetros enumerados para o veículo completo ou completado.

**Quadro 1**

**Parâmetros de entrada «Vehicle/General» (veículo/generalidades)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Camiões pesados | Camiões médios | Autocarros pesados (veículo primário) | Autocarros pesados (veículos completos e completados) |
|---|---|---|---|---|---|---|---|---|
| Manufacturer | P235 | Token | [-] |  | X | X | X | X |
| Manufacturer Address | P252 | Token | [-] |  | X | X | X | X |
| Model_CommercialName | P236 | Token | [-] |  | X | X | X | X |
| VIN | P238 | Token | [-] |  | X | X | X | X |
| Date | P239 | Date Time | [-] | Data e hora de criação dos dados e informações de entrada | X | X | X | X |
| Legislative Category | P251 | String | [-] | Valores admitidos: «N2», «N3», «M3» | X | X | X | X |
| ChassisConfiguration | P036 | String | [-] | Valores admitidos: «Rigid Lorry», «Tractor», «Van», «Bus» | X | X | X |  |
| AxleConfiguration | P037 | String | [-] | Valores admitidos: «4 × 2», «4 × 2F», «6 × 2», «6 × 4», «8 × 2», «8 × 4» em que «4 × 2F» se refere a veículos 4 × 2 com um eixo motor dianteiro | X | X | X |  |
| Articulated | P281 | boolean |  | Em conformidade com o artigo 3.º, ponto 37 |  |  | X |  |
| CorrectedActualMass | P038 | Int | [kg] | De acordo com a «massa efetiva do veículo corrigida» conforme especificada no ponto 2, subponto 4 | X | X |  | X |
| TechnicalPermissibleMaximum LadenMass | P041 | int | [kg] | Em conformidade com o artigo 2.º, ponto 7, do Regulamento (UE) n.º 1230/2012 | X | X | X | X |
| IdlingSpeed | P198 | int | [1/min] | Em conformidade com o ponto 7.1 <br> Para VEE e FCHV, não é necessário introduzir dados | X | X | X |  |
| RetarderType | P052 | string | [-] | Valores admitidos: «None», «Losses included in Gearbox», «Engine Retarder», «Transmission Input Retarder», «Transmission Output Retarder», «Axlegear Input Retarder». <br> «Axlegear Input Retarder» é aplicável apenas às arquiteturas do grupo motopropulsor «E3», «S3», «F3», «S-IEPC», «F-IEPC» e «E-IEPC». <br> Entrada separada para cada grupo motopropulsor no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4. | X | X | X |  |
| RetarderRatio | P053 | double, 3 | [-] | Razão de multiplicação nos termos do quadro 2 do anexo VI <br> Entrada separada para cada grupo motopropulsor individual no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4. | X | X | X |  |
| AngledriveType | P180 | string | [-] | Valores admitidos: «None», «Losses included in Gearbox», «Separate Angledrive» <br> Entrada separada para cada grupo motopropulsor individual no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4. | X | X | X |  |
| PTOShafts GearWheels (1) | P247 | string | [-] | Valores admitidos: «none», «only the drive shaft of the PTO», «drive shaft and/or up to 2 gear wheels», «drive shaft and/or more than 2 gear wheels», «only one engaged gearwheel above oil level», «PTO which includes 1 or more additional gearmesh(es), without disconnect clutch» <br> Entrada separada para cada grupo motopropulsor individual no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4. <br> No caso do IEPS e do IHPC, não devem ser facultados dados de entrada. | X |  |  |  |
| PTOOther Elements (1) | P248 | string | [-] | Valores admitidos: «none», «shift claw, synchroniser, sliding gearwheel», «multi-disc clutch», «multi-disc clutch, oil pump» <br> Entrada separada para cada grupo motopropulsor individual no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4. | X |  |  |  |
| Dados de entrada do motor em conformidade com o apêndice 7 do anexo V |  |  |  | Aplicável apenas se o componente estiver presente no veículo | X | X | X |  |
| Dados de entrada da transmissão em conformidade com os quadros 1 a 3 do apêndice 12 do anexo VI |  |  |  | Aplicável apenas se o componente estiver presente no veículo. «Entrada separada para cada grupo motopropulsor individual no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4» | X | X | X |  |
| Dados de entrada do conversor de binário em conformidade com os quadros 4 e 5 do apêndice 12 do anexo VI |  |  |  | Aplicável apenas se o componente estiver presente no veículo. «Entrada separada para cada grupo motopropulsor individual no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4» | X | X | X |  |
| Dados de entrada do eixo em conformidade com os quadros 1 e 2 do apêndice 6 do anexo VII |  |  |  | Aplicável apenas se o componente estiver presente no veículo. «Entrada separada para cada grupo motopropulsor individual no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4» | X | X | X |  |
| Dados de entrada da transmissão angular em conformidade com os quadros 6 e 7 do apêndice 12 do anexo VI |  |  |  | Refere-se ao componente adicional da transmissão (ADC) certificado, instalado na posição de transmissão angular. <br> Aplicável apenas se o componente estiver presente no veículo. <br> Entrada separada para cada grupo motopropulsor no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4. | X | X | X |  |
| Dados de entrada do retardador em conformidade com os quadros 8 e 9 do apêndice 12 do anexo VI |  |  |  | Aplicável apenas se o componente estiver presente no veículo e as perdas do retardador não forem fornecidas juntamente com os dados de entrada relativos ao componente da transmissão. <br> Entrada separada para cada grupo motopropulsor no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4. | X | X | X |  |
| Dados de entrada da resistência aerodinâmica em conformidade com o quadro 1 do apêndice 9 do anexo VIII | P268 | token | [-] | Aplicável apenas se forem fornecidos dados de entrada certificados | X | X |  | X |
| AirdragModifiedMultistage | P334 | boolean | [-] | Entrada necessária para todas as fases de fabrico subsequentes a uma primeira entrada para a componente de resistência aerodinâmica. <br> Se o parâmetro for definido como «true» (verdadeiro) sem que seja fornecida uma componente certificada de resistência aerodinâmica, a ferramenta de simulação aplica valores normalizados em conformidade com o anexo VIII. |  |  |  | X |
| Dados de entrada do IEPC em conformidade com o apêndice 15 do anexo X-B |  |  |  | Aplicável apenas se o componente estiver presente no veículo.«Entrada separada para cada grupo motopropulsor individual no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4» | X | X | X |  |
| ZeroEmissionVehicle | P269 | boolean | [-] | Conforme definido no artigo 3.º, ponto 15. | X | X | X |  |
| VocationalVehicle | P270 | boolean | [-] | Em conformidade com o artigo 3.º, ponto 9, do Regulamento (UE) 2019/1242 | X |  |  |  |
| NgTankSystem | P275 | string | [-] | Valores admitidos: «Compressed», «Liquefied» <br> Apenas relevante para veículos com motores do tipo de combustível «NG CI» (P193) <br> Se ambos os sistemas de reservatório estiverem presentes num veículo, o sistema capaz de conter a maior quantidade de energia combustível deve ser declarado como dado de entrada da ferramenta de simulação. | X | X |  | X |
| Sleepercab | P276 | boolean | [-] |  | X |  |  |  |
| ClassBus | P282 | string | [-] | Valores admitidos: «I», «I+II», «A», «II», «II+III», «III», «B» em conformidade com o ponto 2 do Regulamento n.º 107 da ONU |  |  |  | X |
| NumberPassengersSeatsLowerDeck | P283 | int | [-] | Número de assentos para passageiros — excluindo os assentos do condutor e da tripulação. <br> No caso de um veículo de dois andares, este parâmetro deve ser utilizado para declarar os assentos para passageiros do andar inferior. No caso de um veículo de um andar, este parâmetro deve ser utilizado para declarar o número total de assentos para passageiros. |  |  |  | X |
| NumberPassengersStandingLowerDeck | P354 | int | [-] | Número de passageiros de pé registados <br> No caso de um veículo de dois andares, este parâmetro deve ser utilizado para declarar os passageiros de pé registados do andar inferior. No caso de um veículo de um andar, este parâmetro deve ser utilizado para declarar o número total de passageiros de pé registados. |  |  |  | X |
| NumberPassengersSeatsUpperDeck | P284 | int | [-] | Número de assentos para passageiros — excluindo os assentos do condutor e da tripulação do andar superior num veículo de dois andares. <br> Para os veículos de um andar, deve ser fornecido «0» como entrada. |  |  |  | X |
| NumberPassengersStandingUpperDeck | P355 | int | [-] | Número de passageiros de pé registados do andar superior num veículo de dois andares. <br> Para os veículos de um andar, deve ser fornecido «0» como entrada. |  |  |  | X |
| BodyworkCode | P285 | int | [-] | Valores admitidos: «CA», «CB», «CC», «CD», «CE», «CF», «CG», «CH», «CI», «CJ» em conformidade com a parte C, ponto 3, do anexo I do Regulamento (UE) 2018/858. No caso de chassis de autocarros com o código de veículo CX, não deve ser fornecida qualquer entrada |  |  |  | X |
| LowEntry | P286 | boolean | [-] | «Entrada baixa» em conformidade com o ponto 1.2.3 do anexo I |  |  |  | X |
| HeightIntegratedBody | P287 | int | [mm] | Em conformidade com o ponto 2, subponto 5 |  |  |  | X |
| VehicleLength | P288 | int | [mm] | Em conformidade com o ponto 2, subponto 8 |  |  |  | X |
| VehicleWidth | P289 | int | [mm] | Em conformidade com o ponto 2, subponto 9 |  |  |  | X |
| EntranceHeight | P290 | int | [mm] | Em conformidade com o ponto 2, subponto 10 |  |  |  | X |
| DoorDriveTechnology | P291 | string | [-] | Valores admitidos: «pneumatic», «electric», «mixed» |  |  |  | X |
| Cargo volume | P292 | double, 3 | [m3] | Aplicável apenas aos veículos com configuração de quadro «furgão» |  | X |  |  |
| VehicleDeclarationType | P293 | string | [-] | Valores admitidos: «interim», «final» |  |  |  | X |
| VehicleTypeApprovalNumber | P352 | token | [-] | Número de homologação do veículo completo <br> No caso de homologações de veículos individuais, o número de homologação do veículo individual | X | X |  | X |
| H2StorageUsableCapacity | P545 | double, 1 | [kg] | De acordo com o ponto 12. <br> Relevante apenas para veículos com um sistema de armazenamento de combustível que contenha hidrogénio. <br> Para autocarros pesados, a entrada só deve ser fornecida pelo fabricante responsável pelo sistema de armazenamento de combustível ou se tiverem sido introduzidas alterações num sistema de armazenamento de combustível existente. | X | X | X | X |
| HydrogenStorageTechnology | P546 | string | [-] | Valores admitidos: «Compressed», «Liquid», «Cryo-compressed» <br> Relevante apenas para veículos com um sistema de armazenamento de combustível que contenha hidrogénio. <br> Para autocarros pesados, a entrada só deve ser fornecida pelo fabricante responsável pelo sistema de armazenamento de combustível ou se tiverem sido introduzidas alterações num sistema de armazenamento de combustível existente. | X | X | X | X |
| SimulationToolLicenceNumber | P547 | token | [-] | Número da licença relacionado com a utilização da ferramenta de simulação em conformidade com o artigo 7.º. | X | X | X | X |
| (1) <br> Se existirem várias tomadas de força (PTO) instaladas na transmissão, apenas deve ser declarado o componente com as perdas mais elevadas de acordo com o anexo IX, ponto 3.6, para a combinação dos critérios «PTOShaftsGearWheels» e «PTOShaftsOtherElements». |  |  |  |  |  |  |  |  |

**Quadro 2**

**Parâmetros de entrada «Vehicle/AxleConfiguration» (veículo/configuração dos eixos) por eixo de rodas**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Camiões pesados | Camiões médios | Autocarros pesados (veículo primário) | Autocarros pesados (veículo completo ou completado) |
|---|---|---|---|---|---|---|---|---|
| AxleNumber | P548 | integer | [-] | Posição do eixo da roda no veículo, a contar da frente para a retaguarda, começando com 1 | X | X | X |  |
| Twin Tyres | P045 | boolean | [-] |  | X | X | X |  |
| Axle Type | P154 | string | [-] | Valores admitidos: «VehicleNonDriven», «VehicleDriven» | X | X | X |  |
| Steered | P195 | boolean |  | Apenas os eixos direcionais ativos devem ser declarados como «direcionais» | X | X | X |  |
| Dados de entrada dos pneus em conformidade com o apêndice 3 do anexo X |  |  |  |  | X | X | X |  |
| Wheel End Friction | P549 | double, 1 | [Nm] | Valor declarado de atrito da extremidade da roda <br> Determinado de acordo com o ponto 3.6 do anexo VII-A. As extremidades das rodas instaladas no veículo devem ter valores de atrito iguais ou inferiores. <br> No caso dos valores normalizados, não devem ser facultados dados de entrada. <br> Entrada relevante apenas para os eixos não motores. | X |  | X |  |
| Certification number wheel end | P550 | token | [-] | Número(s) de certificação do(s) certificado(s) para o atrito declarado da extremidade da roda referido pela entrada relativa ao atrito da extremidade da roda (P549) <br> Entrada relevante apenas para os eixos em que é efetivamente fornecida uma entrada relativa ao atrito da extremidade da roda. <br> Várias opções possíveis. | X |  | X |  |

Os quadros 3 e 3-A fornecem as listas dos parâmetros de entrada relativos às unidades auxiliares. As definições técnicas para a determinação destes parâmetros constam do anexo IX. O ID do parâmetro é utilizado para fornecer uma referência clara entre os parâmetros dos anexos III e IX.

**Quadro 3**

**Parâmetros de entrada «Vehicle/Auxiliaries» (veículo/dispositivos auxiliares) para camiões médios e camiões pesados**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| EngineCoolingFan/Technology | P181 | string | [-] | Valores admitidos: «Crankshaft mounted - Electronically controlled visco clutch», «Crankshaft mounted - Bimetallic controlled visco clutch», «Crankshaft mounted - Discrete step clutch», «Crankshaft mounted - On/off clutch», «Belt driven or driven via transm. - Electronically controlled visco clutch», «Belt driven or driven via transm. - Bimetallic controlled visco clutch», «Belt driven or driven via transm. - Discrete step clutch», «Belt driven or driven via transm. - On/off clutch», «Hydraulic driven - Variable displacement pump», «Hydraulic driven - Constant displacement pump», «Electrically driven - Electronically controlled»; |
| SteeringPump/Technology | P182 | string | [-] | Valores admitidos: «Fixed displacement», «Fixed displacement with elec. control», «Dual displacement», «Dual displacement with elec. control», «Variable displacement mech. controlled», «Variable displacement elec. controlled», «Electric driven pump», «Full electric steering gear». <br> Para VEE, FCHV ou VHE com uma configuração do grupo motopropulsor «S» ou «S-IEPC» em conformidade com o ponto 10.1.1, os únicos valores admitidos são «Electric driven pump» ou «Full electric steering gear». <br> Entrada separada para cada eixo direcional ativo exigido em combinação com a posição do eixo a contar da frente para a retaguarda, começando com 1. |
| ElectricSystem/Technology | P183 | string | [-] | Valores admitidos: «Standard technology», «Standard technology - LED headlights, all»; |
| PneumaticSystem/Technology | P184 | string | [-] | Valores admitidos: «Small», «Small + ESS», «Small + visco clutch», «Small + mech. clutch», «Small + ESS + AMS», «Small + visco clutch + AMS», «Small + mech. clutch + AMS», «Medium Supply 1-stage», «Medium Supply 1-stage + ESS», «Medium Supply 1-stage + visco clutch», «Medium Supply 1-stage + mech. clutch», «Medium Supply 1-stage + ESS + AMS», «Medium Supply 1-stage + visco clutch + AMS», «Medium Supply 1-stage + mech. clutch + AMS», «Medium Supply 2-stage», «Medium Supply 2-stage + ESS», «Medium Supply 2-stage + visco clutch», «Medium Supply 2-stage + mech. clutch», «Medium Supply 2-stage + ESS + AMS», «Medium Supply 2-stage + visco clutch + AMS», «Medium Supply 2-stage + mech. clutch + AMS», «Large Supply», «Large Supply + ESS», «Large Supply + visco clutch», «Large Supply + mech. clutch», «Large Supply + ESS + AMS», «Large Supply + visco clutch + AMS», «Large Supply + mech. clutch + AMS», «Vacuum pump», «Small + elec. driven», «Small + ESS + elec. driven», «Medium Supply 1-stage + elec. driven», «Medium Supply 1-stage + AMS + elec. driven», «Medium Supply 2-stage + elec. driven», «Medium Supply 2-stage + AMS + elec. driven», «Large Supply + elec. driven», «Large Supply + AMS + elec. driven», «Vacuum pump + elec. driven» <br> Para VEE ou FCHV, os únicos valores admitidos são as tecnologias «elec. driven» |
| HVAC/Technology | P185 | string | [-] | Valores admitidos: «None», «Default» |

**Quadro 3-A**

**Parâmetros de entrada «Vehicle/Auxiliaries» (veículo/dispositivos auxiliares) para autocarros pesados**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Autocarros pesados (veículo primário) | Autocarros pesados (veículo completo ou completado) |
|---|---|---|---|---|---|---|
| EngineCoolingFan/Technology | P181 | string | [-] | Valores admitidos: «Crankshaft mounted - Electronically controlled visco clutch», «Crankshaft mounted - Bimetallic controlled visco clutch», «Crankshaft mounted - Discrete step clutch 2 stages», «Crankshaft mounted - Discrete step clutch 3 stages», «Crankshaft mounted - On/off clutch», «Belt driven or driven via transm. - Electronically controlled visco clutch», «Belt driven or driven via transm. - Bimetallic controlled visco clutch», «Belt driven or driven via transm. - Discrete step clutch 2 stages», «Belt driven or driven via transm. - Discrete step clutch 3 stages», «Belt driven or driven via transm. - On/off clutch», «Hydraulic driven - Variable displacement pump», «Hydraulic driven - Constant displacement pump», «Electrically driven - Electronically controlled»; | X |  |
| SteeringPump/Technology | P182 | string | [-] | Valores admitidos: «Fixed displacement», «Fixed displacement with elec. control», «Dual displacement», «Dual displacement with elec. control», «Variable displacement mech. controlled», «Variable displacement elec. controlled», «Electric driven pump», «Full electric steering gear». <br> Para VEE, FCHV ou VHE com uma configuração do grupo motopropulsor «S» ou «S-IEPC» em conformidade com o ponto 10.1.1, os únicos valores admitidos são «Electric driven pump» ou «Full electric steering gear». <br> Entrada separada para cada eixo direcional ativo exigido em combinação com a posição do eixo a contar da frente para a retaguarda, começando com 1. | X |  |
| ElectricSystem/AlternatorTechnology | P294 | string | [-] | Valores admitidos: «conventional», «smart», «no alternator» <br> Entrada única por veículo <br> Para veículos MCI puros, os únicos valores admitidos são «conventional» ou «smart» <br> Para VHE com uma configuração do grupo motopropulsor «S» ou «S-IEPC» em conformidade com o ponto 10.1.1, os únicos valores admitidos são «no alternator» ou «conventional». <br> Para VEE ou FCHV, não é necessário introduzir dados | X |  |
| ElectricSystem/SmartAlternatorRatedCurrent | P295 | integer | [A] | Entrada separada por alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorRatedVoltage | P296 | Integer | [V] | Valores admitidos: «12», «24», «48» <br> Entrada separada por alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorBatteryTechnology | P297 | string | [-] | Valores admitidos: «lead-acid battery – conventional», «lead-acid battery –AGM», «lead-acid battery – gel», «li-ion battery - high power», «li-ion battery - high energy» <br> Entrada separada por bateria carregada por sistema de alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorBatteryNominalVoltage | P298 | Integer | [V] | Valores admitidos: «12», «24», «48» <br> Se as baterias estiverem configuradas em série (p. ex., duas unidades de 12 V para um sistema de 24 V), deve ser fornecida a tensão nominal real das unidades de bateria individuais (12 V neste exemplo). <br> Entrada separada por bateria carregada por sistema de alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorBatteryRatedCapacity | P299 | Integer | [Ah] | Entrada separada por bateria carregada por sistema de alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorCapacitorTechnology | P300 | string | [-] | Valores admitidos: «with DCDC converter» <br> Entrada separada por condensador carregado por sistema de alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorCapacitorRatedCapacitance | P301 | integer | [F] | Entrada separada por condensador carregado por sistema de alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorCapacitorRatedVoltage | P302 | Integer | [V] | Entrada separada por condensador carregado por sistema de alternador inteligente | X |  |
| ElectricSystem/SupplyFromHEVPossible | P303 | boolean | [-] | Entrada relevante apenas para os VHE em combinação com tecnologia de alternador «convencional» ou «inteligente». | X |  |
| ElectricSystem/InteriorlightsLED | P304 | boolean | [-] |  |  | X |
| ElectricSystem/DayrunninglightsLED | P305 | boolean | [-] |  |  | X |
| ElectricSystem/PositionlightsLED | P306 | boolean | [-] |  |  | X |
| ElectricSystem/BrakelightsLED | P307 | boolean | [-] |  |  | X |
| ElectricSystem/HeadlightsLED | P308 | boolean | [-] |  |  | X |
| PneumaticSystem/SizeOfAirSupply | P309 | string | [-] | Valores admitidos: «Small», «Medium Supply 1-stage», «Medium Supply 2-stage», «Large Supply 1-stage», «Large Supply 2-stage», «not applicable». <br> Para o compressor elétrico, deve ser indicado «not applicable». <br> Para VEE ou FCHV, não é necessário introduzir dados; | X |  |
| PneumaticSystem/CompressorDrive | P310 | string | [-] | Valores admitidos: «mechanically», «electrically». <br> Para VEE ou FCHV, o único valor admitido é «electrically» | X |  |
| PneumaticSystem/Clutch | P311 | string | [-] | Valores admitidos: «none», «visco», «mechanically». <br> Para VEE ou FCHV, não é necessário introduzir dados | X |  |
| PneumaticSystem/SmartRegenerationSystem | P312 | boolean | [-] |  | X |  |
| PneumaticSystem/SmartCompressionSystem | P313 | boolean | [-] | Para VEE, FCHV ou VHE com uma configuração do grupo motopropulsor «S» ou «S-IEPC» de acordo com o ponto 10.1.1, não é necessário introduzir dados | X |  |
| PneumaticSystem/Ratio Compressor ToEngine | P314 | double, 3 | [-] | Para o compressor elétrico, deve ser indicado «0.000». <br> Para VEE ou FCHV, não é necessário introduzir dados | X |  |
| PneumaticSystem/Air suspension control | P315 | string | [-] | Valores admitidos: «mechanically», «electronically» | X |  |
| PneumaticSystem/SCRReagentDosing | P316 | boolean | [-] |  | X |  |
| HVAC/SystemConfiguration | P317 | int | [-] | Valores admitidos: «0» a «10» <br> No caso de um sistema AVAC incompleto, deve ser indicado «0». «0» não é aplicável a veículos completos ou completados. |  | X |
| HVAC/ HeatPumpTypeDriverCompartmentCooling | P318 | string | [-] | Valores admitidos: «none», «not applicable», «R-744», «non R-744 2-stage», «non R-744 3-stage», «non R-744 4-stage», «non R-744 continuous» <br> «não aplicável» deve ser declarado para as configurações 6 e 10 do sistema de AVAC devido à alimentação a partir da bomba de calor de passageiros. |  | X |
| HVAC/ HeatPumpTypeDriverCompartmentHeating | P319 | string | [-] | Valores admitidos: «none», «not applicable», «R-744», «non R-744 2-stage», «non R-744 3-stage», «non R-744 4-stage», «non R-744 continuous» <br> «não aplicável» deve ser declarado para as configurações 6 e 10 do sistema de AVAC devido à alimentação a partir da bomba de calor de passageiros. |  | X |
| HVAC/ HeatPumpTypePassengerCompartmentCooling | P320 | string | [-] | Valores admitidos: «none», «R-744», «non R-744 2-stage», «non R-744 3-stage», non R-744 4-stage», «non R-744 continuous» <br> No caso de bombas de calor múltiplas com diferentes tecnologias para arrefecer o compartimento dos passageiros, deve ser declarada a tecnologia dominante (p. ex., de acordo com a potência disponível ou a utilização preferida em funcionamento). |  | X |
| HVAC/ HeatPumpTypePassengerCompartmentHeating | P321 | string | [-] | Valores admitidos: «none», «R-744», «non R-744 2-stage», «non R-744 3-stage», non R-744 4-stage», «non R-744 continuous» <br> No caso de bombas de calor múltiplas com diferentes tecnologias para arrefecer o compartimento dos passageiros, deve ser declarada a tecnologia dominante (p. ex., de acordo com a potência disponível ou a utilização preferida em funcionamento). |  | X |
| HVAC/AuxiliaryHeaterPower | P322 | integer | [W] | Introduzir «0» se não estiver instalado nenhum aquecedor auxiliar. |  | X |
| HVAC/Double glazing | P323 | boolean | [-] |  |  | X |
| HVAC/AdjustableCoolantThermostat | P324 | boolean | [-] |  | X |  |
| HVAC/AdjustableAuxiliaryHeater | P325 | boolean | [-] |  |  | X |
| HVAC/EngineWasteGasHeatExchanger | P326 | boolean | [-] | Para VEE ou FCHV, não é necessário introduzir dados | X |  |
| HVAC/SeparateAirDistributionDucts | P327 | boolean | [-] |  |  | X |
| HVAC/WaterElectricHeater | P328 | boolean | [-] | Introduzir dados apenas para VHE, FCHV e VEE |  | X |
| HVAC/AirElectricHeater | P329 | boolean | [-] | Introduzir dados apenas para VHE, FCHV e VEE |  | X |
| HVAC/OtherHeating Technology | P330 | boolean | [-] | Introduzir dados apenas para VHE, FCHV e VEE |  | X |

**Quadro 4**

**Parâmetros de entrada «VehicleTorqueLimits» por velocidade (facultativo)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Camiões pesados | Camiões médios | Autocarros pesados (veículo primário) | Autocarros pesados (veículo completo ou completado) |
|---|---|---|---|---|---|---|---|---|
| Velocidade engrenada | P196 | integer | [-] | Apenas têm de ser especificados números de velocidades nos casos em que são aplicáveis limites do binário relativos ao veículo em conformidade com o ponto 6 | X | X | X |  |
| MaxTorque | P197 | integer | [Nm] | Binário de entrada máximo do motor ou da transmissão para a velocidade específica definida em conformidade com o ponto 6. | X | X | X |  |

**Quadro 5**

**Parâmetros de entrada para veículos isentos nos termos do artigo 9.º**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Camiões pesados | Camiões médios | Autocarros pesados (veículo primário) | Autocarros pesados (veículo completo e completado) |
|---|---|---|---|---|---|---|---|---|
| Manufacturer | P235 | token | [-] |  | X | X | X | X |
| ManufacturerAddress | P252 | token | [-] |  | X | X | X | X |
| Model_CommercialName | P236 | token | [-] |  | X | X | X | X |
| VIN | P238 | token | [-] |  | X | X | X | X |
| Date | P239 | dateTime | [-] | Data e hora de criação dos dados e informações de entrada | X | X | X | X |
| LegislativeCategory | P251 | string | [-] | Valores admitidos: «N2», «N3», «M3» | X | X | X | X |
| ChassisConfiguration | P036 | string | [-] | Valores admitidos: «Rigid Lorry», «Tractor», «Van», «Bus» | X | X | X |  |
| AxleConfiguration | P037 | string | [-] | Valores admitidos: «4 × 2», «4 × 2F», «6 × 2», «6 × 4», «8 × 2», «8 × 4» em que «4 × 2F» se refere a veículos 4 × 2 com um eixo motor dianteiro | X | X | X |  |
| Articulated | P281 | boolean |  | Em conformidade com a definição estabelecida no anexo I do presente regulamento. |  |  | X |  |
| CorrectedActualMass | P038 | int | [kg] | De acordo com a «massa efetiva do veículo corrigida» conforme especificada no ponto 2, subponto 4 | X | X |  | X |
| TechnicalPermissibleMaximumLadenMass | P041 | int | [kg] | Em conformidade com o artigo 2.º, ponto 7, do Regulamento (UE) n.º 1230/2012 | X | X | X | X |
| ZeroEmissionVehicle | P269 | boolean | [-] | Conforme definido no artigo 3.º, ponto 15. | X | X | X |  |
| Sleepercab | P276 | boolean | [-] |  | X |  |  |  |
| ClassBus | P282 | string | [-] | Valores admitidos: «I», «I+II», «A», «II», «II+III», «III», «B» em conformidade com o ponto 2 do Regulamento n.º 107 da ONU |  |  |  | X |
| NumberPassengersSeatsLowerDeck | P283 | int | [-] | Número de assentos para passageiros — excluindo os assentos do condutor e da tripulação. <br> No caso de um veículo de dois andares, este parâmetro deve ser utilizado para declarar os assentos para passageiros do andar inferior. No caso de um veículo de um andar, este parâmetro deve ser utilizado para declarar o número total de assentos para passageiros. |  |  |  | X |
| NumberPassengersStandingLowerDeck | P354 | int | [-] | Número de passageiros de pé registados <br> No caso de um veículo de dois andares, este parâmetro deve ser utilizado para declarar os passageiros de pé registados do andar inferior. No caso de um veículo de um andar, este parâmetro deve ser utilizado para declarar o número total de passageiros de pé registados. |  |  |  | X |
| NumberPassengersSeatsUpperDeck | P284 | int | [-] | Número de assentos para passageiros — excluindo os assentos do condutor e da tripulação do andar superior num veículo de dois andares. <br> Para os veículos de um andar, deve ser fornecido «0» como entrada. |  |  |  | X |
| NumberPassengersStandingUpperDeck | P355 | int | [-] | Número de passageiros de pé registados do andar superior num veículo de dois andares. <br> Para os veículos de um andar, deve ser fornecido «0» como entrada. |  |  |  | X |
| BodyworkCode | P285 | int | [-] | Valores admitidos: «CA», «CB», «CC», «CD», «CE», «CF», «CG», «CH», «CI», «CJ» em conformidade com a parte C, ponto 3, do anexo I do Regulamento (UE) 2018/858 |  |  |  | X |
| LowEntry | P286 | boolean | [-] | «Entrada baixa» em conformidade com o anexo I, ponto 1.2.2.3 |  |  |  | X |
| HeightIntegratedBody | P287 | int | [mm] | Em conformidade com o ponto 2, subponto 5 |  |  |  | X |
| SumNetPower | P331 | int | [W] | Soma máxima possível da potência de propulsão positiva de todos os conversores de energia ligados ao sistema de tração do veículo ou às rodas | X | X | X |  |
| Technology | P332 | string | [-] | Em conformidade com o quadro 1 do apêndice 1. <br> Valores admitidos: «FCV Article 9 exempted», «Dual-fuel vehicle Article 9 exempted», «HEV Article 9 exempted», «PEV Article 9 exempted», «In-motion charging Article 9 exempted», «Multiple powertrains Article 9 exempted», «H2 ICE Article 9 exempted», «HV Article 9 exempted», «Other technology Article 9 exempted» | X | X | X |  |
| SimulationToolLicenceNumber | P551 | token | [-] | Número da licença relacionado com a utilização da ferramenta de simulação em conformidade com o artigo 7.º. | X | X | X | X |

**Quadro 6**

**Parâmetros de entrada «Advanced driver assistance systems» (sistemas avançados de assistência à condução)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Camiões pesados | Camiões médios | Autocarros pesados (veículo primário) | Autocarros pesados (veículo completo e completado) |
|---|---|---|---|---|---|---|---|---|
| EngineStopStart | P271 | boolean | [-] | Em conformidade com o ponto 8.1.1 <br> Só devem ser introduzidos dados para veículos MCI puros e VHE. <br> Para VHE-CE, a entrada deve ser definida como «true». | X | X | X | X |
| EcoRollWithoutEngineStop | P272 | boolean | [-] | Em conformidade com o ponto 8.1.2 <br> Só devem ser introduzidos dados para veículos MCI puros. | X | X | X | X |
| EcoRollWithEngineStop | P273 | boolean | [-] | Em conformidade com o ponto 8.1.3 <br> Só devem ser introduzidos dados para veículos MCI puros. | X | X | X | X |
| PredictiveCruiseControl | P274 | string | [-] | Em conformidade com o ponto 8.1.4, os valores admitidos são: «none», «1,2», «1,2,3» | X | X | X | X |
| APTEcoRollReleaseLockupClutch | P333 | boolean | [-] | Relevante apenas no caso de transmissões APT-S e APT-P em combinação com qualquer função de «eco-rol». Definir como «true» (verdadeiro) se a funcionalidade 2, tal como definida no ponto 8.1.2, for o modo de «eco-rol» predominante. <br> Só devem ser introduzidos dados para veículos MCI puros. | X | X | X | X |

**Quadro 7**

**Parâmetros gerais de entrada para VHE, VEE e FCHV**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Camiões pesados | Camiões médios | Autocarros pesados (veículo primário) | Autocarros pesados (veículo completo ou completado) |
|---|---|---|---|---|---|---|---|---|
| ArchitectureID | P400 | string | [-] | Em conformidade com o ponto 10.1.3, são admitidos os seguintes valores: <br> «E2», «E3», «E4», «E-IEPC», «P1», «P2», «P2.5», «P3», «P4», «S2», «S3», «S4», «S-IEPC», «F2», «F3», «F4», «F-IEPC» | X | X | X |  |
| ArchitectureIDPwt2 | P552 | string | [-] | No caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4, deve ser fornecido o ID da arquitetura do segundo grupo motopropulsor. <br> Em conformidade com os pontos 10.1.3 e 10.1.4, são admitidos os seguintes valores: <br> «E2», «E3», «E4», «E-IEPC», «S2», «S3», «S4», «S-IEPC», «F2», «F3», «F4», «F-IEPC» | X |  | X |  |
| OVC | P553 | boolean | [-] | Veículo em que o SRAEE pode ser carregado a partir de uma fonte exterior. <br> Deve ser definido como «true» para: <br> — VHE-CE <br> — VEE <br> — VH-CE, caso o dispositivo de carregamento também seja concebido para o funcionamento normal do veículo e não apenas para fins de serviço | X | X | X |  |
| BatteryOnlyMode | P554 | boolean | [-] | A declarar para VH de acordo com o ponto 2, ponto 50). <br> Para VEE, esta entrada deve ser sempre definida como «true». | X | X | X |  |
| Tecnologia de carregamento dinâmico | P555 | string | [-] | Valores admitidos: «None», «Overhead pantograph», «Overhead trolley», «Ground rail», «Wireless». <br> «Overhead pantograph» não é aplicável aos camiões médios. <br> «Overhead trolley» só é aplicável aos autocarros pesados. | X | X | X | X |

**Quadro 8**

**Parâmetros de entrada por posição da máquina elétrica**

**Entrada separada para cada grupo motopropulsor individual no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4**

**(aplicável apenas se o componente estiver presente no veículo ou no grupo motopropulsor específico).**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| PowertrainPosition | P403 | string | [-] | Posição da ME no grupo motopropulsor do veículo em conformidade com os pontos 10.1.2 e 10.1.3. <br> Valores admitidos: «1», «2», «2.5», «3», «4», «GEN». <br> Só é permitida uma posição de ME por grupo motopropulsor, exceto para a arquitetura «S». A arquitetura «S» exige a posição de ME «GEN» e, adicionalmente, que uma outra posição de ME seja «2», «3» ou «4». <br> A posição «1» não é admitida para arquiteturas «S» e «E» <br> A posição «GEN» é apenas admitida para a arquitetura «S» |
| Count | P404 | integer | [-] | Número de máquinas elétricas idênticas na posição de ME especificada. <br> No caso de o parâmetro «PowertrainPosition» ser «4», a contagem deve ser composta por múltiplos de 2(p. ex., 2, 4, 6). |
| Dados de entrada do sistema de máquina elétrica em conformidade com o apêndice 15 do anexo X-B |  |  |  |  |
| Dados de entrada do ADC em conformidade com o apêndice 12 do anexo VI |  |  |  | Entrada facultativa no caso de uma relação de transmissão única adicional (componente adicional da transmissão) entre o veio da ME e o ponto de ligação ao grupo motopropulsor do veículo, em conformidade com o ponto 10.1.2. <br> No caso de um SME ligado através de uma correia, aplicam-se as disposições previstas no anexo VI, ponto 6.1.3. <br> Não é permitido se o parâmetro «IHPCType» for definido como «IHPC Type 1» |
| P2.5GearRatios | P407 | double, 3 | [-] | Aplicável apenas no caso de o parâmetro «PowertrainPosition» ser fixado em «P2.5» <br> Declarado para cada relação de transmissão para a marcha à frente. Valor declarado para a relação de transmissão definido por «nGBX_in / nEM» no caso de ME sem componente adicional da transmissão ou «nGBX_in / nADC» no caso de ME com componente adicional da transmissão. <br> nGBX_in = velocidade de rotação no veio de entrada da transmissão <br> nEM = velocidade de rotação no veio de saída da ME <br> nADC = velocidade de rotação no veio de saída do componente adicional da transmissão |

**Quadro 9**

**Limitações do binário por posição da máquina elétrica (facultativo)**

**Declaração de um conjunto de dados separado para cada nível de tensão medido em «CertificationNumberEM». Não é permitido se o parâmetro «IHPCType» for definido como «IHPC Type 1».**

**Entrada separada para cada grupo motopropulsor individual no caso de vários grupos motopropulsores independentes mecanicamente, em conformidade com o ponto 10.1.4.**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| OutputShaftSpeed | P408 | double, 2 | [1/min] | As mesmas entradas para a velocidade de rotação a declarar em «CertificationNumberEM» para o parâmetro «P468» constante do anexo X-B, apêndice 15. |
| MaxTorque | P409 | double, 2 | [Nm] | Binário máximo da ME (referente ao veio de saída) como função dos pontos de velocidade de rotação declarados no parâmetro «P469» constante do anexo X-B, apêndice 15. <br> Cada valor do binário máximo declarado deve ser inferior a 0,9 vezes o valor original à respetiva velocidade de rotação ou corresponder exatamente ao valor original à respetiva velocidade de rotação. <br> Os valores do binário máximo declarado não podem ser inferiores a zero. <br> Se o parâmetro «Count» (P404) for superior a um, o binário máximo deve ser declarado para uma única ME (tal como está presente no ensaio de componente para a ME em «CertificationNumberEM»). |
| MinTorque | P410 | double, 2 | [Nm] | Binário mínimo da ME (referente ao veio de saída) como função dos pontos de velocidade de rotação declarados no parâmetro «P470» constante do anexo X-B, apêndice 15. <br> Cada valor do binário mínimo declarado deve ser superior a 0,9 vezes o valor original à respetiva velocidade de rotação ou corresponder exatamente ao valor original à respetiva velocidade de rotação. <br> Os valores do binário mínimo declarado não podem ser superiores a zero. <br> Se o parâmetro «Count» (P404) for superior a um, o binário mínimo deve ser declarado para uma única ME (tal como está presente no ensaio de componente para a ME em «CertificationNumberEM»). |

**Quadro 10**

**Parâmetros de entrada por SRAEE**

**(Aplicável apenas se o componente estiver presente no veículo)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| StringID | P411 | integer | [-] | A disposição dos subsistemas representativos de bateria em conformidade com o anexo X-B a nível do veículo é declarada atribuindo a cada subsistema de bateria uma cadeia (string) específica definida por este parâmetro. Todas as cadeias específicas estão ligadas em paralelo, todos os subsistemas de bateria localizados numa cadeia paralela específica estão ligados em série. <br> Valores admitidos: «1», «2», «3», … |
| Dados de entrada do SRAEE em conformidade com o apêndice 15 do anexo X-B |  |  |  |  |
| DeteriorationPerformanceRatio | P557 | double, 2 | [%] | Para os VEE e os VH-CE, deve ser declarado como dado de entrada o requisito mínimo de desempenho (RMD) aplicável ao veículo no ciclo de vida principal, em conformidade com o anexo II, quadro 3, do Regulamento (UE) 2024/1257 do Parlamento Europeu e do Conselho (1), ou um requisito declarado de desempenho (RDD) superior ao RMD, se, por sua vez, esse RDD for declarado pelo fabricante e avaliado para o veículo no ciclo de vida principal de acordo com as disposições do Regulamento (UE) 2024/1257 e da respetiva legislação de execução. <br> Para os VH que não sejam VH-CE, não devem ser facultados dados de entrada. |
| SOCmin | P413 | double, 1 | [%] | Relevante apenas no caso de tipo de SRAEE «bateria». <br> Para os VEE e os VH-CE com um modo predominante apenas a bateria, em conformidade com o ponto 2, ponto 50), esta entrada deve ser declarada em percentagem da capacidade nominal quando a carga remanescente da bateria for indicada a zero (ou outro limite mínimo definido pelo OEM) ao condutor ou se o funcionamento normal do veículo (2) no modo predominante apenas a bateria não for possível devido à baixa carga da bateria. <br> Para os VH que não sejam VH-CE e para os VH-CE sem um modo predominante apenas a bateria, em conformidade com o ponto 2, ponto 50), esta entrada é facultativa e o parâmetro apenas é eficaz na ferramenta de simulação quando o valor introduzido é superior ao valor genérico, tal como documentado no manual do utilizador. |
| SOCmax | P414 | double, 1 | [%] | Relevante apenas no caso de tipo de SRAEE «bateria». <br> Para os VEE e os VH-CE com um modo predominante apenas a bateria, em conformidade com o ponto 2, ponto 50), esta entrada deve ser declarada em percentagem da capacidade nominal quando o condutor recebe a indicação de que o veículo está totalmente carregado. <br> Para os VH que não sejam VH-CE e para os VH-CE sem um modo predominante apenas a bateria, em conformidade com o ponto 2, ponto 50), esta entrada é facultativa e o parâmetro apenas é eficaz na ferramenta de simulação quando o valor introduzido é inferior ao valor genérico, tal como documentado no manual do utilizador. |
| (1) <br> Regulamento (UE) 2024/1257 do Parlamento Europeu e do Conselho, de 24 de abril de 2024, relativo à homologação de veículos a motor e motores e dos sistemas, componentes e unidades técnicas destinados a esses veículos, no que respeita às suas emissões e à durabilidade da bateria (Euro 7), que altera o Regulamento (UE) 2018/858 do Parlamento Europeu e do Conselho e que revoga os Regulamentos (CE) n.º 715/2007 e (CE) n.º 595/2009 do Parlamento Europeu e do Conselho, o Regulamento (UE) n.º 582/2011 da Comissão, o Regulamento (UE) 2017/1151 da Comissão, o Regulamento (UE) 2017/2400 da Comissão e o Regulamento de Execução (UE) 2022/1362 da Comissão (JO L, 2024/1257, 8.5.2024, ELI: http://data.europa.eu/eli/reg/2024/1257/oj). <br> (2) <br> O «funcionamento normal do veículo» exclui qualquer limitação significativa do funcionamento (por exemplo, o «funcionamento de modo degradado» não é considerado como «funcionamento normal do veículo»). |  |  |  |  |

**Quadro 11**

**Aumento das limitações para VHE paralelo (facultativo)**

**Só é permitido se a configuração do grupo motopropulsor em conformidade com o ponto 10.1.1 for «P» ou «IHPC Type 1».**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| RotationalSpeed | P415 | double, 2 | [1/min] | Referente à velocidade do veio de entrada da transmissão |
| BoostingTorque | P416 | double, 2 | [Nm] | De acordo com o ponto 10.2 |

**Quadro 11-A**

**Parâmetros de entrada por sistema de pilha de combustível**

**(Aplicável apenas se o componente estiver presente no veículo)**

**Um ou dois sistemas de pilha de combustível diferentes, podendo cada um deles ter até três unidades idênticas instaladas.**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| Count | P558 | integer | [-] | Número de unidades idênticas, valores permitidos: «1», «2», «3» |
| MinPower | P559 | integer | [W] | Entrada facultativa para a declaração do limite inferior de potência aplicável do sistema de pilha de combustível ao nível da integração do veículo. |
| MaxPower | P560 | integer | [W] | Entrada facultativa para a declaração do limite superior de potência aplicável do sistema de pilha de combustível ao nível da integração do veículo. |
| Dados de entrada do sistema de pilha de combustível em conformidade com o apêndice 15 do anexo X-B |  |  |  |  |

**4. Massa do veículo para tratores e camiões rígido médios, tratores e camiões rígidos pesados**

4.1 A massa do veículo utilizada como dado de entrada da ferramenta de simulação deve ser a massa efetiva do veículo corrigida.

4.2 Se nem todo o equipamento-padrão estiver instalado, o fabricante deve juntar a massa dos seguintes elementos de construção à massa efetiva do veículo corrigida:

a) A proteção à frente contra o encaixe em conformidade com o disposto no Regulamento (UE) 2019/2144 (**) do Parlamento Europeu e do Conselho;

b) Proteção à retaguarda contra o encaixe em conformidade com o Regulamento (UE) 2019/2144;

c) Proteção lateral em conformidade com o Regulamento (UE) 2019/2144;

d) Prato de engate em conformidade com o Regulamento (UE) 2019/2144.

4.3 A massa dos elementos de construção referidos no ponto 4.2 é a seguinte:

Para os veículos dos grupos 1s, 1, 2 e 3 definidos no quadro 1 do anexo I, e para os grupos de veículos 51 e 53 definidos no quadro 2 do anexo I.

| Proteção à frente contra o encaixe | 45 kg; |
|---|---|

| Proteção à retaguarda contra o encaixe | 40 kg; |
|---|---|

| Proteção lateral | 8,5 kg/m × entre-eixo [m] – 2,5 kg. |
|---|---|

Para os veículos dos grupos 4, 5, 9 a 12 e 16 definidos no quadro 1 do anexo I.

| Proteção à frente contra o encaixe | 50 kg; |
|---|---|

| Proteção à retaguarda contra o encaixe | 45 kg; |
|---|---|

| Proteção lateral | 14 kg/m × entre-eixo [m] – 17 kg; |
|---|---|

| Prato de engate | 210 kg. |
|---|---|

**5. Eixos hidráulicos e mecânicos**

No caso de veículos equipados com:

a) Eixos hidráulicos, os eixos devem ser considerados não acionáveis e não são tidos em conta pelo fabricante ao estabelecer a configuração dos eixos de um veículo;

b) Eixos mecânicos, os eixos devem ser considerados acionáveis e são tidos em conta pelo fabricante ao estabelecer a configuração dos eixos de um veículo.

**6. Limites do binário dependentes da velocidade e desativação de velocidades**

**6.1. Limites do binário do motor dependentes da velocidade**

Para 50 % das velocidades mais altas (por exemplo, da velocidade 7 à 12 numa caixa de 12 velocidades), o fabricante do veículo pode declarar um limite para o binário máximo do motor dependente das velocidades que não ultrapasse 95 % do binário máximo do motor.

**6.2 Desativação de velocidades**

Para a velocidade mais elevada apenas ou para as 2 velocidades mais elevadas (por exemplo, as velocidades 5 e 6 numa caixa de 6 velocidades), o fabricante do veículo pode declarar uma desativação total das velocidades introduzindo na ferramenta de simulação 0 Nm como limite de binário específico das velocidades. Não é permitido declarar essa desativação de velocidades apenas para a segunda velocidade mais elevada.

**6.3 Requisitos de verificação**

Os limites do binário do motor dependentes da velocidade, em conformidade com o ponto 6.1, e a desativação de velocidades em conformidade com o ponto 6.2 são sujeitos a verificação no procedimento de ensaio de verificação (VTP) estabelecido no anexo X-A, ponto 6.1.1.1, alínea c).

**7. Velocidade de ralenti específica do veículo**

7.1. A velocidade de marcha lenta sem carga (ralenti) tem de ser declarada para cada veículo com um MCI. Esse ralenti declarado do veículo deve ser igual ou superior ao especificado nos dados de homologação do motor.

**8. Sistemas avançados de assistência à condução**

8.1 Devem ser declarados nos dados de entrada da ferramenta de simulação os seguintes tipos de sistemas avançados de assistência à condução, destinados principalmente a reduzir o consumo de combustível e as emissões de CO2:

8.1.1 Função «para/arranca» do motor durante as paragens do veículo: sistema que automaticamente desliga e liga de novo o motor de combustão interna durante as paragens do veículo, para reduzir o tempo de ralenti. Para o motor desligar automaticamente, o tempo decorrido após a paragem do veículo não pode ser superior a 3 segundos.

8.1.2 «Eco-rol» sem função «para/arranca» do motor: sistema que automaticamente desacopla o motor de combustão interna do sistema de tração em condições específicas de circulação em declive, com gradiente negativo reduzido. O sistema deve estar ativo, pelo menos, em todas as velocidades superiores a 60 km/h definidas no controlo de cruzeiro. Qualquer sistema a declarar nas informações de entrada para a ferramenta de simulação deve abranger uma ou ambas as seguintes funcionalidades:

Funcionalidade (1)

O motor de combustão é desacoplado do sistema de tração e o motor funciona em ralenti. No caso das transmissões com mudanças rápidas de velocidade automáticas (APT), a embraiagem de bloqueio do conversor de binário é fechada.

Funcionalidade (2) Embraiagem de bloqueio do conversor de binário aberta

A embraiagem de bloqueio do conversor de binário é aberta durante o modo «eco-rol». Tal permite que o motor funcione em modo de marcha em roda livre a velocidades inferiores do motor e reduz ou mesmo elimina a injeção de combustível. A funcionalidade (2) é relevante apenas para as transmissões APT.

8.1.3 «Eco-rol» com função «para/arranca» do motor: sistema que automaticamente desacopla o motor de combustão interna do sistema de tração em condições específicas de circulação em declive, com gradiente negativo reduzido. Nestas fases «eco-rol», o motor de combustão interna desliga-se após um curto período e permanece desligado durante a maior parte da fase «eco-rol». O sistema deve estar ativo, pelo menos, a todas as velocidades superiores a 60 km/h definidas no controlo de cruzeiro.

8.1.4 Regulação preditiva da velocidade (predictive cruise control, PCC): sistema que otimiza a utilização de energia potencial durante um ciclo de condução, através da previsão disponível de dados relativos ao gradiente da rodovia e utilização de um sistema GPS. O sistema PCC declarado nos dados de entrada da ferramenta de simulação deve garantir uma previsão do gradiente numa distância superior a 1 000 m e incluir todas as seguintes funcionalidades:

(1) Roda livre em aproximação do topo

Ao atingir o topo de uma elevação, a velocidade do veículo reduz antes de atingir o ponto em que o veículo começa a acelerar apenas por força da gravidade, face à velocidade definida do controlo de cruzeiro, permitindo reduzir a travagem na fase seguinte de descida.

(2) Aceleração sem potência do motor

Na condução em declive a baixa velocidade com um gradiente negativo acentuado, a aceleração do veículo é assegurada sem utilizar a potência do motor, permitindo reduzir a travagem durante a descida.

(3) Roda livre em declive

Na condução em declive, quando o veículo trava em velocidade excessiva, o sistema PCC aumenta essa velocidade durante um curto período de modo a terminar a fase de descida com uma velocidade mais elevada. Velocidade excessiva significa, neste caso, uma velocidade do veículo superior à velocidade definida pelo sistema de controlo de cruzeiro.

Um sistema PCC pode ser declarado enquanto dado de entrada da ferramenta de simulação se incluir as funcionalidades referidas ou nos pontos 1) e 2) ou nos pontos 1), 2) e 3).

8.2 As onze combinações de sistemas avançados de assistência à condução indicadas no quadro 12 constituem parâmetros de entrada na ferramenta de simulação. As combinações 2 a 11 não podem ser declaradas para transmissões manuais sincronizadas (SMT). As combinações n.ºs 3, 6, 9 e 11 não podem ser declaradas no caso das transmissões APT.

**Quadro 12**

**Combinações dos sistemas avançados de assistência à condução que constituem parâmetros de entrada na ferramenta de simulação**

| N.º da combinação | Função «para/arranca» do motor durante as paragens do veículo | «Eco-rol» sem função «para/arranca» do motor | «Eco-rol» com função «para/arranca» do motor | Regulação preditiva da velocidade |
|---|---|---|---|---|
| 1 | Sim | Não | Não | Não |
| 2 | Não | Sim | Não | Não |
| 3 | Não | Não | Sim | Não |
| 4 | Não | Não | Não | Sim |
| 5 | Sim | Sim | Não | Não |
| 6 | Sim | Não | Sim | Não |
| 7 | Sim | Não | Não | Sim |
| 8 | Não | Sim | Não | Sim |
| 9 | Não | Não | Sim | Sim |
| 10 | Sim | Sim | Não | Sim |
| 11 | Sim | Não | Sim | Sim |

8.3 Qualquer sistema avançado de assistência à condução declarado nos dados de entrada da ferramenta de simulação deve ser regulado por defeito no modo de economia de combustível, após cada ciclo em que o veículo é ligado e desligado na ignição.

8.4 Se um sistema avançado de assistência à condução for declarado nos dados de entrada da ferramenta de simulação, deve ser possível verificar a presença desse sistema com base numa condução em condições reais e nas definições do sistema de acordo com o ponto 8.1. Se for declarada uma determinada combinação de sistemas, deve ser também demonstrada a interação das funcionalidades (por exemplo, regulação preditiva da velocidade e «eco-rol» com função «para/arranca» do motor). No procedimento de verificação, deve ser tido em conta que a ativação dos sistemas requer determinadas condições (por exemplo, motor a temperatura de funcionamento para a função «para-arranca», determinados intervalos de velocidade para o PCC e certos gradientes das estradas para o sistema «eco-rol»). O fabricante do veículo tem de apresentar uma descrição funcional das condições-limite em que os sistemas estão «inativos» ou quando a sua eficiência se encontra reduzida. A entidade homologadora pode solicitar ao requerente uma justificação técnica dessas condições e avaliá-la para efeitos de conformidade.

**9. Volume de carga**

9.1. Para os veículos com configuração do quadro «furgão», o volume de carga deve ser calculado pela seguinte equação:

image

em que as dimensões devem ser determinadas em conformidade com o quadro 13 e a figura 3.

**Quadro 13**

**Definições relacionadas com o volume de carga para camiões médios de tipo furgão**

| Símbolo da fórmula | Dimensão | Definição |
|---|---|---|
| LC,floor | Comprimento do compartimento de carga no piso | — Distância longitudinal do ponto mais recuado da última fila de assentos ou da divisória ao ponto mais avançado da traseira fechada do compartimento, projetada até ao plano de simetria longitudinal <br> — Medido à altura da superfície do piso de carga |
| LC | Comprimento do comprimento da carga | — Distância longitudinal do plano X tangente ao ponto mais recuado do encosto do banco, incluindo apoios de cabeça da última fila de assentos ou da divisória, até ao plano X mais avançado tangente à traseira fechada do compartimento, isto é, ao taipal traseiro ou às portas traseiras ou a qualquer outra superfície limite <br> — Medido à altura do ponto mais recuado da última fila de assentos ou da divisória |
| WC,max | Largura máxima do compartimento de carga | — Distância lateral máxima do compartimento de carga <br> — Medida entre o piso de carga e 70 mm acima do piso <br> — A medição exclui o arco de transição, saliências pontuais, depressões ou bolsas, caso existam |
| WC,wheelhouse | Largura do compartimento de carga entre as cavas das rodas | — Distância lateral mínima entre as interferências limitadoras das cavas das rodas (passagem) <br> — Medida entre o piso de carga e 70 mm acima do piso <br> — A medição exclui o arco de transição, saliências pontuais, depressões ou bolsas, caso existam |
| HC,max | Altura máxima do compartimento de carga | — Distância vertical máxima entre o piso de carga e o revestimento interior do tejadilho ou outra superfície limite <br> — Medida atrás da última fila de assentos ou divisória na linha central do veículo |
| HC,rearwheel | Altura do compartimento de carga na roda traseira | — Distância vertical entre o topo do piso de carga e o revestimento interior do tejadilho ou a superfície limite <br> — Medida na coordenada X da roda traseira na linha central do veículo |

**Figura 3**

**Definição do volume de carga para camiões médios**

image

**10. VHE, FCHV e VEE**

As disposições que se seguem aplicam-se apenas no caso de VHE, FCHV e VEE.

**10.1 Definição da arquitetura do grupo motopropulsor do veículo**

**10.1.1 Definição da configuração do grupo motopropulsor**

A configuração do grupo motopropulsor do veículo deve ser determinada de acordo com as seguintes definições:

No caso de um VHE:

(a) «P» no caso de um VHE paralelo

(b) «S» no caso de um VHE de série

(c) «S-IEPC» no caso de um componente IEPC estar presente no veículo

(d) «IHPC Type 1», no caso de o parâmetro «IHPCType» do componente da máquina elétrica ser definido como «IHPC Type 1»

No caso de um VEE:

(a) «E» no caso de um componente de ME estar presente no veículo

(b) «E-IEPC» no caso de um componente IEPC estar presente no veículo

No caso de um FCHV:

a) «F» no caso de um componente de ME estar presente no veículo;

b) «F-IEPC» no caso de um componente IEPC estar presente no veículo

**10.1.2 Definição das posições das ME no grupo motopropulsor do veículo**

Se a configuração do grupo motopropulsor do veículo em conformidade com o ponto 10.1.1 for «P», «S», «F» ou «E», a posição da ME instalada no grupo motopropulsor do veículo deve ser determinada em conformidade com as definições constantes do quadro 14.

**Quadro 14**

**Posições possíveis das ME no grupo motopropulsor do veículo**

| Índice de posição de ME | Configuração do grupo motopropulsor nos termos do ponto 10.1.1 | Tipo de transmissão nos termos do anexo VI, apêndice 12, quadro 1 | Definição/Requisitos (1) | Outras explicações |
|---|---|---|---|---|
| 1 | P | AMT, APT-S, APT-P | Ligada ao grupo motopropulsor a montante da embraiagem (no caso de AMT) ou a montante do veio de entrada do conversor de binário (no caso de APT-S ou APT-P). <br> A ME está ligada à cambota do MCI diretamente ou através de um tipo de ligação mecânica (p. ex., correia). | Distinção de P0: As ME que, em princípio, não podem contribuir para a propulsão do veículo (ou seja, alternadores) são tratadas ao introduzir os dados relativos aos sistemas auxiliares (ver o quadro 3, relativo aos camiões, e o quadro 3-A, relativo aos autocarros, do presente anexo e o anexo IX). <br> No entanto, as ME nesta posição, que podem, em princípio, contribuir para a propulsão do veículo, mas para as quais o binário máximo declarado em conformidade com o quadro 9 do presente anexo é fixado em zero, devem ser declaradas como «P1». |
| 2 | E, S, F | AMT | A máquina elétrica está ligada ao grupo motopropulsor a jusante da embraiagem e a montante do veio de entrada da transmissão. |  |
| 2 | E, S | AMT, APT-N, APT-S, APT-P | A máquina elétrica está ligada ao grupo motopropulsor a montante do veio de entrada da transmissão (no caso de AMT ou APT-N) ou a montante do veio de entrada do conversor de binário (no caso de APT-S, APT-P). |  |
| 2,5 | P | AMT, APT-S, APT-P | A máquina elétrica está ligada ao grupo motopropulsor a jusante da embraiagem (no caso de AMT) ou a jusante do veio de entrada do conversor de binário (no caso de APT-S ou APT-P) e a montante do veio de saída da transmissão. | A ME está ligada a um veio específico no interior da transmissão (p. ex., eixo secundário). Deve ser fornecida uma relação de transmissão específica para cada velocidade mecânica na transmissão em conformidade com o quadro 8. |
| 3 | P | AMT, APT-S, APT-P | A máquina elétrica está ligada ao grupo motopropulsor a jusante do veio de saída da transmissão e a montante do eixo. |  |
| 3 | E, S, F | n.a. | A máquina elétrica está ligada ao grupo motopropulsor a montante do eixo. |  |
| 4 | P | AMT, APT-S, APT-P | A máquina elétrica está ligada ao grupo motopropulsor a jusante do eixo. |  |
| 4 | E, S, F | n.a. | A máquina elétrica está ligada ao cubo da roda e a mesma configuração está instalada duas vezes em aplicação simétrica (isto é, uma do lado esquerdo e outra do lado direito do veículo, na mesma posição em relação à roda na direção longitudinal). |  |
| GEN | S | n.a. | A máquina elétrica está ligada mecanicamente a um MCI, mas não está ligada mecanicamente às rodas do veículo. |  |
| (1) <br> O termo ME aqui utilizado inclui um componente adicional da transmissão (ADC), se existir. |  |  |  |  |

**10.1.3 Definição do ID da arquitetura do grupo motopropulsor**

O valor de entrada do ID da arquitetura do grupo motopropulsor ID exigido em conformidade com o quadro 7 deve ser determinado com base na configuração do grupo motopropulsor em conformidade com o ponto 10.1.1 e na posição da ME no grupo motopropulsor do veículo em conformidade com o ponto 10.1.2 (se aplicável) a partir das combinações válidas de dados de entrada na ferramenta de simulação enumerados no quadro 15.

No caso de a configuração do grupo motopropulsor em conformidade com o ponto 10.1.1 ser «IHPC Type 1», aplicam-se as seguintes disposições:

(a) O ID «P2» da arquitetura do grupo motopropulsor deve ser declarado em conformidade com o quadro 7 e os dados dos componentes do grupo motopropulsor indicados no quadro 15 para «P2» devem ser introduzidos na ferramenta de simulação com dados de componente separados para a ME e a transmissão, determinados em conformidade com o anexo X-B, ponto 4.4.3.

(b) Os dados de componente para a ME em conformidade com a alínea a) devem ser inseridos na ferramenta de simulação com o parâmetro «PowertrainPosition» definido como «2» em conformidade com o quadro 8.

**Quadro 15**

**Dados de entrada válidos sobre a arquitetura do grupo motopropulsor para a ferramenta de simulação**

<table> <tbody> <tr> <td rowspan="2">Tipo de grupo motopropulsor</td> <td rowspan="2">Configuração do grupo motopropulsor</td> <td rowspan="2">ID da arquitetura para introdução na ferramenta VECTO</td> <td colspan="8">Componente do grupo motopropulsor presente no veículo</td> <td rowspan="2">Observações</td> </tr> <tr> <td>MCI</td> <td>ME posição GEN</td> <td>ME posição 1</td> <td>ME posição 2</td> <td>Transmissão</td> <td>ME posição 3</td> <td>Eixo</td> <td>ME posição 4</td> </tr> <tr> <td rowspan="4">VEE</td> <td rowspan="3">E</td> <td>E2</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td></td> </tr> <tr> <td>E3</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td></td> </tr> <tr> <td>E4</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td></td> </tr> <tr> <td>IEPC</td> <td>E-IEPC</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>(1)</td> <td>Não</td> <td></td> </tr> <tr> <td rowspan="10">VHE</td> <td rowspan="5">P</td> <td>P1</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td></td> </tr> <tr> <td>P2</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td>(2)</td> </tr> <tr> <td>P2.5</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td>(3)</td> </tr> <tr> <td>P3</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>(4)</td> </tr> <tr> <td>P4</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td></td> </tr> <tr> <td rowspan="5">S</td> <td>S2</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td></td> </tr> <tr> <td>S3</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td></td> </tr> <tr> <td>S4</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td></td> </tr> <tr> <td>S-IEPC</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>(1)</td> <td>Não</td> <td></td> </tr> <tr> <td colspan="12"></td> </tr> <tr> <td rowspan="4">FCHV</td> <td rowspan="4">F</td> <td>F2</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td></td> </tr> <tr> <td>F3</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td></td> </tr> <tr> <td>F4</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td></td> </tr> <tr> <td>F-IEPC</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>(1)</td> <td>Não</td> <td></td> </tr> <tr> <td colspan="12">(1) «Sim» (ou seja, componente do eixo presente) apenas no caso de ambos os parâmetros «DifferentialIncluded» e «DesignTypeWheelMotor» serem definidos como «falsos» (2) Não aplicável aos tipos de transmissão APT-S e APT-P (3) Quando o EM está ligado a um veio específico no interior da transmissão (por exemplo, o eixo secundário) em conformidade com a definição estabelecida no quadro 8 (4) Não aplicável aos veículos com tração dianteira.</td> </tr> </tbody> </table>

**10.1.4. Definição do ID da arquitetura para o segundo grupo motopropulsor independente mecanicamente**

Nos casos em que o veículo está equipado com dois grupos motopropulsores e em que cada grupo é propulsor de diferentes eixos de rodas do veículo e os diferentes grupos motopropulsores não podem, em circunstância alguma, ser ligados mecanicamente, o fabricante do veículo deve declarar um segundo ID do grupo motopropulsor definido em conformidade com o ponto 10.1.3. Além disso, os dois grupos motopropulsores devem partilhar o mesmo SRAEE e conversores de energia elétrica em mecânica separados.

A este respeito, os eixos hidráulicos devem, em conformidade com o ponto 5, segundo parágrafo, alínea a), do presente anexo, ser tratados como eixos não motores e, por conseguinte, não devem ser contados como um grupo motopropulsor independente mecanicamente.

Só os grupos motopropulsores de configuração S, S-IEPC, F, F-IEPC e E, em conformidade com o ponto 10.1.1, podem ser declarados em caso de presença de um segundo grupo motopropulsor independente mecanicamente. Além disso, só podem ser declaradas as combinações de ID da arquitetura para o primeiro e segundo grupos motopropulsores indicados com «sim» no quadro 15-A.

**Quadro 15-A**

**Dados de entrada válidos sobre a arquitetura do grupo motopropulsor para a ferramenta de simulação**

|  | E2 | E3 | E4 | E-IEPC | S2 | S3 | S4 | S-IEPC | F2 | F3 | F4 | F-IEPC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E2 | Sim | Sim | Sim | Sim | Não | Não | Não | Não | Não | Não | Não | Não |
| E3 | Sim | Sim | Sim | Sim | Não | Não | Não | Não | Não | Não | Não | Não |
| E4 | Sim | Sim | Sim | Sim | Não | Não | Não | Não | Não | Não | Não | Não |
| E-IEPC | Sim | Sim | Sim | Sim | Não | Não | Não | Não | Não | Não | Não | Não |
| S2 | Não | Não | Não | Não | Sim | Sim | Sim | Sim | Não | Não | Não | Não |
| S3 | Não | Não | Não | Não | Sim | Sim | Sim | Sim | Não | Não | Não | Não |
| S4 | Não | Não | Não | Não | Sim | Sim | Sim | Sim | Não | Não | Não | Não |
| S-IEPC | Não | Não | Não | Não | Sim | Sim | Sim | Sim | Não | Não | Não | Não |
| F2 | Não | Não | Não | Não | Não | Não | Não | Não | Sim | Sim | Sim | Sim |
| F3 | Não | Não | Não | Não | Não | Não | Não | Não | Sim | Sim | Sim | Sim |
| F4 | Não | Não | Não | Não | Não | Não | Não | Não | Sim | Sim | Sim | Sim |
| F-IEPC | Não | Não | Não | Não | Não | Não | Não | Não | Sim | Sim | Sim | Sim |

**10.2 Definição de limitação da aceleração para VHE paralelos**

O fabricante do veículo pode declarar limitações ao binário total de propulsão de todo o grupo motopropulsor relativamente ao veio de entrada da transmissão para um VHE paralelo, a fim de restringir as capacidades de aceleração do veículo.

A declaração de tais limitações só é permitida se a configuração do grupo motopropulsor em conformidade com o ponto 10.1.1 for «P» ou «IHPC Type 1».

As limitações são declaradas como binário adicional permitido no topo da curva do MCI a plena carga, dependendo da velocidade de rotação do veio de entrada da transmissão. A ferramenta de simulação efetua uma interpolação linear para determinar o binário adicional aplicável entre os valores declarados a duas velocidades de rotação específicas. Na gama de velocidade de rotação entre 0 e ralenti (em conformidade com o ponto 7.1), o binário a plena carga disponível a partir do MCI é igual apenas ao binário a plena carga do MCI em ralenti devido à modelização do comportamento da embraiagem durante o arranque do veículo.

Se essa limitação for declarada, os valores para o binário adicional devem ser declarados pelo menos a uma velocidade de rotação de 0 e à velocidade máxima de rotação da curva do MCI a plena carga. Qualquer número arbitrário de valores pode ser declarado na gama entre zero e a velocidade máxima de rotação da curva do MCI a plena carga. Não são permitidos valores declarados inferiores a zero para o binário adicional.

O fabricante do veículo pode declarar limitações que correspondam exatamente à curva do MCI a plena carga, declarando valores de 0 Nm para o binário adicional.

**10.3 Função «para/arranca» do motor para VHE**

Se o veículo estiver equipado com uma função «para/arranca» do motor em conformidade com o ponto 8.1.1, tendo em conta as condições-limite determinadas no ponto 8.4, o parâmetro de entrada P271 nos termos do quadro 6 deve ser definido como verdadeiro.

**11. Transferência dos resultados da ferramenta de simulação para outros veículos**

11.1. Os resultados da ferramenta de simulação podem ser transferidos para outros veículos, conforme previsto no artigo 9.º, n.º 6, desde que estejam preenchidas todas as seguintes condições:

(a) Os dados e informações de entrada são totalmente idênticos, com exceção do NIV (P238) e da data (P239). No caso de simulações para autocarros pesados primários, as informações e os dados de entrada adicionais relevantes para o veículo intermédio e disponíveis já na fase inicial podem diferir, mas devem ser tomadas medidas especiais neste caso;

(b) A versão da ferramenta de simulação é idêntica.

11.2. Para a transferência de resultados, devem ser considerados os seguintes ficheiros de resultados:

(a) Camiões médios e pesados: ficheiro de registos do fabricante e ficheiro de informações ao cliente;

(b) Autocarros pesados primários: ficheiro de registos do fabricante e ficheiro de informações ao cliente;

(c) Autocarros pesados completos ou completados: ficheiro de registos do fabricante, ficheiro de informações ao cliente e ficheiro de informações do veículo.

11.3. Para efetuar a transferência de resultados, os ficheiros mencionados no ponto 10.2 devem ser alterados, substituindo os elementos de dados indicados nos subpontos seguintes por informações atualizadas. Só são permitidas alterações de elementos de dados relacionados com a fase atual de acabamento.

**11.3.1 Ficheiro de registos do fabricante**

(a) NIV (anexo IV, parte I, ponto 1.1.3)

(b) Data de criação do ficheiro de saída (anexo IV, parte I, ponto 3.2)

**11.3.2 Ficheiro de informações ao cliente**

(a) NIV (anexo IV, parte II, ponto 1.1.1)

(b) Data de criação do ficheiro de saída (anexo IV, parte II, ponto 3.2)

**11.3.3. Ficheiro de informações do veículo**

11.3.3.1. No caso de um autocarro pesado primário:

(a) NIV (anexo IV, parte III, ponto 1.1)

(b) Data de criação do ficheiro de saída (anexo IV, parte III, ponto 1.3.2)

11.3.3.2. Se um fabricante de um autocarro pesado primário fornecer dados que vão além dos requisitos para o veículo primário e que diferem entre o veículo original e o veículo transferido, os elementos de dados correspondentes no ficheiro de informações do veículo devem ser atualizados em conformidade.

11.3.3.3. No caso de um autocarro pesado completo ou completado:

(a) NIV (anexo IV, parte III, ponto 2.1)

(b) Data de criação do ficheiro de saída (anexo IV, parte III, ponto 2.2.2)

| 11.3.4 | Após as alterações acima descritas, os elementos de assinatura a seguir indicados devem ser atualizados. <br> 11.3.4.1. Camiões: <br> (a) Ficheiro de registos do fabricante: Anexo IV, parte I, pontos 3.6 e 3.7 <br> (b) Ficheiro de informações ao cliente: Anexo IV, parte II, pontos 3.3 e 3.4 <br> 11.3.4.2. Autocarros pesados primários: <br> (a) Ficheiro de registos do fabricante: Anexo IV, parte I, pontos 3.3 e 3.4 <br> (b) Ficheiro de informações do veículo: Anexo IV, parte III, pontos 1.4.1 e 1.4.2 <br> 11.3.4.3. Autocarros pesados primários, se tiverem sido fornecidos dados adicionais para o veículo intermédio: <br> (a) Ficheiro de registos do fabricante: Anexo IV, parte I, pontos 3.3 e 3.4 <br> (b) Ficheiro de informações do veículo: Anexo IV, parte III, pontos 1.4.1, 1.4.2 e 2.3.1 <br> 11.3.4.4. Autocarros pesados completos ou completados: <br> (a) Ficheiro de registos do fabricante: Anexo IV, parte I, pontos 3.6 e 3.7 <br> (b) Ficheiro de informações do veículo: Anexo IV, parte III, ponto 2.3.1 |
|---|---|

11.4. Se as emissões de CO2 e o consumo de combustível não puderem ser determinados para o veículo original devido a uma anomalia da ferramenta de simulação, aplicam-se as mesmas medidas aos veículos com resultados transferidos.

11.5. Se um fabricante aplicar a abordagem de transferência de resultados para outros veículos conforme estabelecida no presente ponto, o respetivo processo deve ser demonstrado à entidade homologadora no âmbito da concessão da licença do processo.

**12. Capacidade utilizável do sistema de armazenamento de combustível com hidrogénio**

Para os sistemas de armazenamento de combustível que contenham hidrogénio, deve ser determinada a capacidade utilizável.

**12.1 Hidrogénio gasoso comprimido**

A capacidade utilizável deve ser calculada com base na seguinte equação:

image

em que:

| musable | capacidade utilizável [kg] |
|---|---|
| VCCHSS | volume da tecnologia de armazenamento de hidrogénio comprimido [l] |
| pmin,rel | pressão relativa correspondente ao estado vazio do reservatório de hidrogénio [MPa] |
| ρ15°C, NWP | densidade do hidrogénio gasoso comprimido a 15 °C e à pressão nominal de serviço (PNS), tal como definido no ponto 2.17 do Regulamento n.º 134 da ONU [g/l] <br> Este valor da densidade deve ser determinado a partir do quadro 16 por interpolação linear. |
| ρ15°C, pmin,rel | densidade do hidrogénio gasoso comprimido a 15 °C e pmin,rel [g/l] <br> Este valor da densidade deve ser determinado a partir do quadro 16 por interpolação linear. |

**Quadro 16**

**Densidade do hidrogénio comprimido a 15 °C [g/l]**

<table> <tbody> <tr> <td rowspan="2">Temperatura (°C)</td> <td colspan="13">Pressão (MPa)</td> </tr> <tr> <td>0,5</td> <td>1</td> <td>2</td> <td>3</td> <td>4</td> <td>5</td> <td>6</td> <td>7</td> <td>8</td> <td>9</td> <td>10</td> <td>35</td> <td>70</td> </tr> <tr> <td>15</td> <td>0,5</td> <td>0,9</td> <td>1,7</td> <td>2,6</td> <td>3,4</td> <td>4,2</td> <td>4,9</td> <td>5,7</td> <td>6,5</td> <td>7,3</td> <td>8,0</td> <td>24,0</td> <td>40,2</td> </tr> </tbody> </table>

**12.2. Hidrogénio líquido**

A capacidade utilizável deve ser calculada com base na seguinte equação:

image

em que:

| musable | capacidade utilizável [kg] |
|---|---|

| VLHSS | volume da tecnologia de armazenamento de hidrogénio líquido [l] |
|---|---|

| ρfull ref | densidade do hidrogénio líquido correspondente ao estado cheio do reservatório de hidrogénio [g/l], definida pelas seguintes condições de funcionamento: <br> a) O veículo é utilizado até se atingir o estado vazio do reservatório de hidrogénio; <br> b) O reabastecimento começa imediatamente a seguir; <br> c) No que diz respeito ao estado do hidrogénio fornecido pela infraestrutura de reabastecimento de hidrogénio, deve ser feita referência às normas internacionais, se disponíveis. |
|---|---|

| ρempty | densidade do hidrogénio líquido correspondente ao estado vazio do reservatório de hidrogénio [g/l] <br> O modelo de cálculo das densidades deve ser divulgado à entidade homologadora, a pedido desta. |
|---|---|

**12.3. Hidrogénio criocomprimido**

A capacidade utilizável deve ser calculada com base nas seguintes equações:

image

image

em que:

| musable | capacidade utilizável [kg] |
|---|---|

| VCCHSS | volume da tecnologia de armazenamento de hidrogénio criocomprimido [l] |
|---|---|

| ρfilling | densidade do hidrogénio no final do processo de reabastecimento [g/l] |
|---|---|

| fusable | parte utilizável determinada a partir do quadro 17 por interpolação linear [-] |
|---|---|

| pfilling | pressão absoluta do hidrogénio no reservatório no final do processo de reabastecimento [bar] |
|---|---|

O valor da pressão do hidrogénio no reservatório, no final do processo de reabastecimento, utilizado nos cálculos deve ser documentado na ficha de informações relativa ao sistema de reservatório de hidrogénio criocomprimido. As normas internacionais existentes em matéria de infraestruturas de reabastecimento criocomprimido devem ser tidas em conta na determinação deste valor, se já estiverem disponíveis.

**Quadro 17**

**Parte utilizável da massa de hidrogénio numa tecnologia de armazenamento de hidrogénio criocomprimido [-]**

| Pressão absoluta correspondente ao estado vazio do reservatório de hidrogénio [bar] | fusable (*1) [-] |
|---|---|
| 5 | 0,97 |
| 8 | 0,95 |
| 10 | 0,93 |
| 15 | 0,88 |
| 20 | 0,85 |
| 30 | 0,75 |
| (*1) <br> Os valores especificados para fusable pressupõem que o reservatório dispõe de um sistema de aquecimento interno que é ativado quando é atingida a pressão mínima. Caso não exista tal sistema de aquecimento no reservatório, o fabricante deve aplicar, mediante acordo da entidade homologadora, um valor inferior para fusable. |  |
