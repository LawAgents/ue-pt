---
id: "regulamento-ue-2022-1379-anexo-iii"
celex: "32022R1379"
title: "Regulamento (UE) 2022/1379 da Comissão, de 5 de julho de 2022, que altera o Regulamento (UE) 2017/2400 no que respeita à determinação das emissões de CO2 e ao consumo de combustível dos camiões médios e pesados e dos autocarros pesados, bem como à introdução de veículos elétricos e outras novas tecnologias (Texto relevante para efeitos do EEE) — Anexo III"
type: "Regulamento"
number: "2022/1379"
year: 2022
date: 2022-07-05
status: "em vigor"
text_version: "original sem consolidação"
source: "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32022R1379"
eli: "http://data.europa.eu/eli/reg/2022/1379/oj"
retrieved: 2026-10-21
legal_notice: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
part_of: "regulamento-ue-2022-1379"
part: "Anexo III"
---

# Regulamento (UE) 2022/1379 da Comissão, de 5 de julho de 2022, que altera o Regulamento (UE) 2017/2400 no que respeita à determinação das emissões de CO2 e ao consumo de combustível dos camiões médios e pesados e dos autocarros pesados, bem como à introdução de veículos elétricos e outras novas tecnologias (Texto relevante para efeitos do EEE) — Anexo III

## Anexo III

«ANEXO III

**INFORMAÇÃO DE ENTRADA RELATIVA ÀS CARACTERÍSTICAS DO VEÍCULO**

**1. Introdução**

O presente anexo descreve a lista de parâmetros que devem ser fornecidos pelo fabricante do veículo para inserção na ferramenta de simulação. O modelo XML aplicável e vários exemplos de dados estão disponíveis na plataforma de distribuição eletrónica específica.

**2. Definições**

(1) “ID do parâmetro”: identificador único utilizado na ferramenta de simulação para um determinado parâmetro de entrada ou conjunto de dados de entrada;

(2) “Tipo”: tipo de dados do parâmetro;

| “string” … | sequência de carateres na codificação ISO8859-1; |
|---|---|
| “token” … | sequência de carateres na codificação ISO8859-1, sem espaços em branco à frente e atrás; |
| “date” … | data e hora TUC com o seguinte formato: AAAA-MM-DDTHH:MM:SSZ com carateres em itálico representando carateres fixos, p. ex., “2002-05-30T09:30:10Z”; |
| “integer” … | valor com um tipo de dados inteiro, sem zeros à frente, p. ex., “1 800”; |
| “double, X” … | número fracionário contendo exatamente X dígitos a seguir ao sinal decimal (“.”) e sem zeros à frente, p. ex., “double, 2”: “2 345,67”; para “double, 4”: “45.6780”; |

(3) “Unidade” … unidade física do parâmetro;

(4) “Massa efetiva do veículo corrigida”: a massa especificada na “massa efetiva do veículo” em conformidade com o Regulamento (UE) n.º 1230/2012 da Comissão (*), com exceção do(s) reservatório(s) que deve(m) ser enchido(s) a, pelo menos, 50 % da(s) sua(s) capacidade(s). Os sistemas contendo líquidos são enchidos até 100 % da capacidade especificada pelo fabricante, com exceção dos que se destinam a águas residuais, que devem permanecer vazios.

No caso dos camiões rígidos médios, dos camiões rígidos pesados e dos tratores, a massa é determinada sem superstrutura e corrigida pelo peso adicional do equipamento-padrão não instalado, conforme especificado no ponto 4.3. A massa de uma carroçaria-padrão, semirreboque-padrão ou reboque-padrão para simular o veículo completo ou a combinação veículo completo-(semi)reboque é adicionada automaticamente pela ferramenta de simulação. Todas as partes montadas em ou por cima da estrutura principal são consideradas partes da superestrutura, se estiverem instaladas apenas para facilitar uma superstrutura, independentemente das peças que são necessárias para as condições em ordem de marcha.

No caso dos autocarros pesados que são veículos primários, a “massa efetiva do veículo corrigida” não é aplicável, uma vez que o valor genérico da massa é atribuído pela ferramenta de simulação;

(5) “Altura da carroçaria integrada”: a diferença, na direção “Z”, entre o ponto de referência “A” do ponto mais alto e o ponto mais baixo “B” de uma carroçaria integrada (ver figura 1). Aos veículos que se desviam do caso normal aplicam-se os seguintes casos (ver figura 2):

Caso especial 1, dois níveis: A altura da carroçaria integrada é a média de h1 e h2, em que:

h1 é a diferença entre o ponto A, mas determinado na secção transversal do veículo na extremidade traseira da primeira porta de passageiros, e o ponto B,

h2 é a diferença entre o ponto A e o ponto B.

Caso especial 2, inclinado: A altura da carroçaria integrada é a média de h1 e h2, em que:

h1 é a diferença entre o ponto A, mas determinado na secção transversal do veículo na extremidade traseira da primeira porta de passageiros, e o ponto B,

h2 é a diferença entre o ponto A e o ponto B.

Caso especial 3, apenas com secção de tejadilho:

altura da carroçaria integrada determinada na secção de tejadilho existente.

Caso especial 4, sem tejadilho:

a altura da carroçaria integrada é a diferença entre o ponto mais elevado do veículo a um metro na direção longitudinal do para-brisas ou do para-brisas superior, no caso de um veículo de dois andares, e o ponto B.

Para todos os outros casos não abrangidos pelo caso normal ou pelos casos especiais 1 a 4, a altura da carroçaria integrada é a diferença entre o ponto mais elevado do veículo e o ponto B. Este parâmetro é relevante apenas para os autocarros pesados.

\**Figura 1**

\**Altura da carroçaria integrada — caso normal**

Image 3

\**Figura 2**

\**Altura da carroçaria integrada — casos especiais**

Image 4

(6) O ponto de referência “A” é o ponto mais alto da carroçaria (figura 1). Não devem ser considerados painéis de carroçaria e/ou de design, suportes para montagem, por exemplo, de sistemas AVAC, escotilhas e elementos semelhantes;

(7) O ponto de referência “B” é o ponto mais baixo do bordo inferior da parte exterior da carroçaria (figura 1). Os suportes, por exemplo, para a montagem dos eixos, não devem ser tidos em conta;

(8) “Comprimento do veículo”: a dimensão do veículo em conformidade com o quadro I constante do anexo I, apêndice 1, do Regulamento (UE) n.º 1230/2012; Além disso, não devem ser tidos em conta os dispositivos de suporte de carga amovíveis, os dispositivos de engate não amovíveis e quaisquer outras partes exteriores não amovíveis que não afetem o espaço utilizável pelos passageiros. Este parâmetro só é relevante para os autocarros pesados;

(9) “Largura do veículo”: a dimensão do veículo em conformidade com o quadro II constante do anexo I, apêndice 1, do Regulamento (UE) n.º 1230/2012. Em derrogação destas disposições, os dispositivos de suporte de carga amovíveis, os dispositivos de engate não amovíveis e quaisquer outras partes exteriores não amovíveis que não afetem o espaço utilizável pelos passageiros não devem ser considerados;

(10) “Altura de entrada em posição não inclinada”: o nível do piso acima do solo medido na primeira abertura da porta mais dianteira do veículo quando este se encontra na posição não inclinada (sistema de kneeling não acionado);

(11) “Pilha de combustível”: um conversor de energia que transforma energia química (à entrada) em energia elétrica (à saída) ou vice-versa;

(12) “Veículo a pilha de combustível” ou “FCV” (fuel cell vehicle): um veículo cujo grupo motopropulsor contém conversor(es) de energia de propulsão que consistem exclusivamente em pilha(s) de combustível e máquina(s) elétrica(s):

(13) “Veículo híbrido a pilha de combustível” ou “FCHV” (fuel cell hybrid vehicle): um veículo com pilha de combustível equipado com um grupo motopropulsor que contém, pelo menos, um sistema de armazenamento de combustível e, pelo menos, um sistema recarregável de armazenamento de energia elétrica como sistemas de armazenamento de energia de propulsão;

(14) “Veículo MCI puro”: um veículo em que todos os conversores de energia de propulsão são motores de combustão interna;

(15) “Máquina elétrica” ou “ME”: um conversor de energia que transforma energia elétrica em energia mecânica e vice-versa;

(16) “Sistema de armazenamento de energia”: um sistema que armazena energia e liberta-a sob a mesma forma da energia de entrada;

(17) “Sistema de armazenamento de energia de propulsão”: um sistema de armazenamento de energia do grupo motopropulsor que não seja um dispositivo periférico, cuja energia de saída é utilizada direta ou indiretamente para fins de propulsão do veículo;

(18) “Categoria de sistema de armazenamento de energia de propulsão”: um sistema de armazenamento de combustível, um sistema recarregável de armazenamento de energia elétrica (SRAEE) ou um sistema recarregável de armazenamento de energia mecânica;

(19) “A jusante”: uma posição no grupo motopropulsor do veículo mais próxima das rodas do que a posição real de referência;

(20) “Sistema de tração”: os elementos do grupo motopropulsor ligados entre si para efeitos da transmissão da energia mecânica entre o(s) conversor(es) de energia de propulsão e as rodas;

(21) “Conversor de energia”: um sistema no qual a energia de saída é diferente da energia de entrada;

(22) “Conversor de energia de propulsão”: um conversor de energia do grupo motopropulsor que não seja um dispositivo periférico, cuja energia de saída é utilizada direta ou indiretamente para fins de propulsão do veículo;

(23) “Categoria de conversor de energia de propulsão”: um motor de combustão interna, uma máquina elétrica ou uma pilha de combustível;

(24) “Forma de energia”: energia elétrica, mecânica ou química (incluindo combustíveis);

(25) “Sistema de armazenamento de combustível”: um sistema de armazenamento de energia de propulsão que armazena energia química enquanto combustível líquido ou gasoso;

(26) “Veículo híbrido” ou “HV” (hybrid vehicle): um veículo cujo grupo motopropulsor contém pelo menos duas categorias distintas de conversores de energia de propulsão e pelo menos duas categorias distintas de sistemas de armazenamento de energia de propulsão;

(27) “Veículo híbrido elétrico” ou “VHE”: um veículo híbrido em que um dos conversores de energia de propulsão é uma máquina elétrica e o outro é um motor de combustão interna;

(28) “VHE de série”: um VHE com uma arquitetura do grupo motopropulsor em que o MCI alimenta um ou mais canais de conversão de energia elétrica sem ligação mecânica entre o MCI e as rodas do veículo;

(29) “Motor de combustão interna” ou “MCI”: um conversor de energia com oxidação intermitente ou contínua de combustível que transforma energia química em energia mecânica;

(30) “Veículo híbrido elétrico com carregamento do exterior” ou “VHE-CE”: um veículo híbrido elétrico que pode ser carregado a partir de uma fonte exterior;

(31) “VHE paralelo”: um VHE com uma arquitetura do grupo motopropulsor em que o MCI alimenta apenas um único canal ligado mecanicamente entre o motor e as rodas do veículo;

(32) “Dispositivos periféricos”: qualquer dispositivo que consome, converte, armazena ou fornece energia que não é utilizada, direta ou indiretamente, para a propulsão do veículo, mas é essencial para o funcionamento do grupo motopropulsor;

(33) “Grupo motopropulsor”, todo o conjunto de sistema(s) de armazenamento de energia de propulsão, conversor(es) de energia de propulsão e sistema(s) de tração que fornece energia mecânica às rodas de um veículo para efeitos de propulsão, incluindo os dispositivos periféricos;

(34) “Veículo exclusivamente elétrico” ou “VEE”: um veículo a motor nos termos do Regulamento (UE) 2018/858, artigo 3.º, ponto 16, equipado com um grupo motopropulsor que contém exclusivamente máquinas elétricas como conversores de energia de propulsão e sistemas recarregáveis de armazenamento de energia elétrica como sistemas de armazenamento de energia de propulsão e/ou, em alternativa, quaisquer outros meios de fornecimento condutor ou indutivo direto de energia elétrica a partir da rede elétrica que forneçam a energia de propulsão ao veículo a motor;

(35) “A montante”: uma posição no grupo motopropulsor do veículo mais afastada das rodas do que a posição real de referência;

(36) “IEPC”: um componente do grupo motopropulsor elétrico integrado (integrated electric powertrain component) em conformidade com o anexo X-B, ponto 2, subponto 36;

(37) “IHPC tipo 1”: um componente do grupo motopropulsor híbrido elétrico integrado (integrated hybrid electric vehicle powertrain component) do tipo 1 em conformidade com o anexo X-B, ponto 2, subponto 38.

**3. Conjunto de parâmetros de entrada**

Nos quadros 1 a 11, são especificados os conjuntos de parâmetros de entrada a fornecer relativamente às características do veículo. São definidos diferentes conjuntos consoante o caso de aplicação (camiões médios, camiões pesados e autocarros pesados).

No caso dos autocarros pesados, é feita uma distinção entre os parâmetros de entrada a fornecer para as simulações no veículo primário e para as simulações no veículo completo ou completado. Aplicam-se as seguintes disposições:

— Os fabricantes de veículos primários devem fornecer todos os parâmetros enumerados na coluna do veículo primário.

— Os fabricantes de veículos primários podem, além disso, fornecer parâmetros de entrada adicionais relacionados com o veículo completo ou completado, que podem ser determinados já nesta fase inicial. Neste caso, devem ser fornecidas informações sobre o fabricante (P235), o endereço do fabricante (P252), o NIV (P238) e a data (P239), tanto para o conjunto de parâmetros de entrada primários como para o conjunto de parâmetros de entrada adicionais.

— Os fabricantes intermédios devem fornecer parâmetros de entrada relativos ao veículo completo ou completado que possam ser determinados nesta fase e que estejam sob a sua responsabilidade. Se um parâmetro já fornecido numa fase de fabrico anterior for atualizado, deve ser especificado todo o estado do parâmetro (por exemplo, se for adicionada uma segunda bomba de calor ao veículo, deve ser fornecida a tecnologia de ambos os sistemas). Informações sobre o fabricante (P235), endereço do fabricante (P252), NIV (P238) e data (P239) devem ser fornecidas pelos fabricantes intermédios em todos os casos;

— Os fabricantes do veículo completado devem fornecer parâmetros de entrada que possam ser determinados nesta fase e que estejam sob a sua responsabilidade. Para as atualizações necessárias de parâmetros já fornecidos em fases de fabrico anteriores, aplicam-se as mesmas disposições que para os fabricantes intermédios. As informações sobre o fabricante (P235), endereço do fabricante (P252), NIV (P238), data (P239) e massa efetiva corrigida (P038) devem ser fornecidas em todos os casos. Para poder efetuar as simulações necessárias, o conjunto de dados consolidados de todas as fases de fabrico deve conter todas as informações enumeradas na coluna relativa ao veículo completo ou completado;

— Os fabricantes relacionados com a fase completa devem fornecer todos os parâmetros de entrada. Devem ser fornecidas informações sobre o fabricante (P235), o endereço do fabricante (P252), o NIV (P238) e a data (P239), tanto para os parâmetros primários de entrada como para os parâmetros de entrada do veículo completo;

— O parâmetro “VehicleDeclarationType” (P293) deve ser fornecido por todas as fases de fabrico que forneçam qualquer um dos parâmetros enumerados para o veículo completo ou completado.

**Quadro 1**

**Parâmetros de entrada “Vehicle/General” (veículo/generalidades)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Camiões pesados | Camiões médios | Autocarros pesados (veículo primário) | Autocarros pesados (veículos completos e completados) |
|---|---|---|---|---|---|---|---|---|
| Manufacturer | P235 | Token | [-] |  | X | X | X | X |
| Manufacturer Address | P252 | Token | [-] |  | X | X | X | X |
| Model_CommercialName | P236 | Token | [-] |  | X | X | X | X |
| VIN | P238 | Token | [-] |  | X | X | X | X |
| Date | P239 | Date Time | [-] | Data e hora de criação dos dados e informações de entrada | X | X | X | X |
| Legislative Category | P251 | String | [-] | Valores admitidos: “N2”, “N3”, “M3” | X | X | X | X |
| ChassisConfiguration | P036 | String | [-] | Valores admitidos: “Rigid Lorry”, “Tractor”, “Van”, “Bus” | X | X | X |  |
| AxleConfiguration | P037 | String | [-] | Valores admitidos: “4 × 2”, “4 × 2F”, “6 × 2”, “6 × 4”, “8 × 2”, “8 × 4” em que “4 × 2F” se refere a veículos 4 × 2 com um eixo motor dianteiro | X | X | X |  |
| Articulated | P281 | boolean |  | Em conformidade com o artigo 3.º, ponto 37 |  |  | X |  |
| CorrectedActualMass | P038 | Int | [kg] | De acordo com a “massa efetiva do veículo corrigida” conforme especificada no ponto 2, subponto 4 | X | X |  | X |
| TechnicalPermissibleMaximum LadenMass | P041 | int | [kg] | Em conformidade com o artigo 2.º, ponto 7, do Regulamento (UE) n.º 1230/2012 | X | X | X | X |
| IdlingSpeed | P198 | int | [1/min] | Em conformidade com o ponto 7.1 <br> Para VEE, não é necessário introduzir dados. | X | X | X |  |
| RetarderType | P052 | string | [-] | Valores admitidos: “None”, “Losses included in Gearbox”, “Engine Retarder”, “Transmission Input Retarder”, “Transmission Output Retarder”, “Axlegear Input Retarder” <br> “Axlegear Input Retarder” é aplicável apenas às arquiteturas do grupo motopropulsor “E3”, “S3”, “S-IEPC” e “E-IEPC” | X | X | X |  |
| RetarderRatio | P053 | double, 3 | [-] | Razão de multiplicação nos termos do quadro 2 do anexo VI | X | X | X |  |
| AngledriveType | P180 | string | [-] | Valores admitidos: “None”, “Losses included in Gearbox”, “Separate Angledrive” | X | X | X |  |
| PTOShafts GearWheels (1) | P247 | string | [-] | Valores admitidos: “none”, “only the drive shaft of the PTO”, “drive shaft and/or up to 2 gear wheels”, “drive shaft and/or more than 2 gear wheels”, “only one engaged gearwheel above oil level”, “PTO which includes 1 or more additional gearmesh(es), without disconnect clutch” | X |  |  |  |
| PTOOther Elements (1) | P248 | string | [-] | Valores admitidos: “none”, “shift claw, synchroniser, sliding gearwheel”, “multi-disc clutch”, “multi-disc clutch, oil pump” | X |  |  |  |
| CertificationNumberEngine | P261 | token | [-] | Aplicável apenas se o componente estiver presente no veículo | X | X | X |  |
| CertificationNumberGearbox | P262 | token | [-] | Aplicável apenas se o componente estiver presente no veículo e forem fornecidos dados de entrada certificados | X | X | X |  |
| CertificationNumberTorqueconverter | P263 | token | [-] | Aplicável apenas se o componente estiver presente no veículo e forem fornecidos dados de entrada certificados | X | X | X |  |
| CertificationNumberAxlegear | P264 | token | [-] | Aplicável apenas se o componente estiver presente no veículo e forem fornecidos dados de entrada certificados | X | X | X |  |
| CertificationNumberAngledrive | P265 | token | [-] | Refere-se ao componente adicional da transmissão (ADC) certificado, instalado na posição de transmissão angular. <br> Aplicável apenas se o componente estiver presente no veículo e forem fornecidos dados de entrada certificados | X | X | X |  |
| CertificationNumberRetarder | P266 | token | [-] | Aplicável apenas se o componente estiver presente no veículo e forem fornecidos dados de entrada certificados | X | X | X |  |
| Certification NumberAirdrag | P268 | token | [-] | Aplicável apenas se forem fornecidos dados de entrada certificados | X | X |  | X |
| AirdragModifiedMultistage | P334 | boolean | [-] | Entrada necessária para todas as fases de fabrico subsequentes a uma primeira entrada para a componente de resistência aerodinâmica. <br> Se o parâmetro for definido como “true” (verdadeiro) sem que seja fornecida uma componente certificada de resistência aerodinâmica, a ferramenta de simulação aplica valores normalizados em conformidade com o anexo VIII. |  |  |  | X |
| Certification NumberIEPC | P351 | token | [-] | Aplicável apenas se o componente estiver presente no veículo e forem fornecidos dados de entrada certificados | X | X | X |  |
| ZeroEmissionVehicle | P269 | boolean | [-] | Conforme definido no artigo 3.º, ponto 15. | X | X | X |  |
| VocationalVehicle | P270 | boolean | [-] | Em conformidade com o artigo 3.º, ponto 9, do Regulamento (UE) 2019/1242 | X |  |  |  |
| NgTankSystem | P275 | string | [-] | Valores admitidos: “Compressed”, “Liquefied” <br> Apenas relevante para veículos com motores do tipo de combustível “NG CI” (P193) <br> Se ambos os sistemas de reservatório estiverem presentes num veículo, o sistema capaz de conter a maior quantidade de energia combustível deve ser declarado como dado de entrada da ferramenta de simulação. | X | X |  | X |
| Sleepercab | P276 | boolean | [-] |  | X |  |  |  |
| ClassBus | P282 | string | [-] | Valores admitidos: “I”, “I+II”, “A”, “II”, “II+III”, “III”, “B” em conformidade com o ponto 2 do Regulamento n.º 107 da ONU |  |  |  | X |
| NumberPassengersSeatsLowerDeck | P283 | int | [-] | Número de assentos para passageiros — excluindo os assentos do condutor e da tripulação. <br> No caso de um veículo de dois andares, este parâmetro deve ser utilizado para declarar os assentos para passageiros do andar inferior. No caso de um veículo de um andar, este parâmetro deve ser utilizado para declarar o número total de assentos para passageiros. |  |  |  | X |
| NumberPassengersStandingLowerDeck | P354 | int | [-] | Número de passageiros de pé registados <br> No caso de um veículo de dois andares, este parâmetro deve ser utilizado para declarar os passageiros de pé registados do andar inferior. No caso de um veículo de um andar, este parâmetro deve ser utilizado para declarar o número total de passageiros de pé registados. |  |  |  | X |
| NumberPassengersSeatsUpperDeck | P284 | int | [-] | Número de assentos para passageiros — excluindo os assentos do condutor e da tripulação do andar superior num veículo de dois andares. <br> Para os veículos de um andar, deve ser fornecido “0” como entrada. |  |  |  | X |
| NumberPassengersStandingUpperDeck | P355 | int | [-] | Número de passageiros de pé registados do andar superior num veículo de dois andares. <br> Para os veículos de um andar, deve ser fornecido “0” como entrada. |  |  |  | X |
| BodyworkCode | P285 | int | [-] | Valores admitidos: “CA”, “CB”, “CC”, “CD”, “CE”, “CF”, “CG”, “CH”, “CI”, “CJ” em conformidade com o anexo I, parte C, ponto 3, do Regulamento (UE) 2018/585. <br> No caso de chassis de autocarros com o código de veículo CX, não deve ser fornecida qualquer entrada. |  |  |  | X |
| LowEntry | P286 | boolean | [-] | “Entrada baixa” em conformidade com o anexo I, ponto 1.2.2.3 |  |  |  | X |
| HeightIntegratedBody | P287 | int | [mm] | Em conformidade com o ponto 2, subponto 5 |  |  |  | X |
| VehicleLength | P288 | int | [mm] | Em conformidade com o ponto 2, subponto 8 |  |  |  | X |
| VehicleWidth | P289 | int | [mm] | Em conformidade com o ponto 2, subponto 9 |  |  |  | X |
| EntranceHeight | P290 | int | [mm] | Em conformidade com o ponto 2, subponto 10 |  |  |  | X |
| DoorDriveTechnology | P291 | string | [-] | Valores admitidos: “pneumatic”, “electric”, “mixed” |  |  |  | X |
| Cargo volume | P292 | double, 3 | [m3] | Aplicável apenas aos veículos com configuração de quadro “furgão” |  | X |  |  |
| VehicleDeclarationType | P293 | string | [-] | Valores admitidos: “interim”, “final” |  |  |  | X |
| VehicleTypeApprovalNumber | P352 | token | [-] | Número de homologação do veículo completo <br> No caso de homologações de veículos individuais, o número de homologação do veículo individual | X | X |  | X |

**Quadro 2**

**Parâmetros de entrada “Vehicle/AxleConfiguration” (veículo/configuração dos eixos) por eixo de rodas**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Camiões pesados | Camiões médios | Autocarros pesados (veículo primário) | Autocarros pesados (veículo completo ou completado) |
|---|---|---|---|---|---|---|---|---|
| Twin Tyres | P045 | boolean | [-] |  | X | X | X |  |
| Axle Type | P154 | string | [-] | Valores admitidos: “VehicleNonDriven”, “VehicleDriven” | X | X | X |  |
| Steered | P195 | boolean |  | Apenas os eixos direcionais ativos devem ser declarados como “direcionais” | X | X | X |  |
| Certification NumberTyre | P267 | token | [-] |  | X | X | X |  |

Os quadros 3 e 3-A fornecem as listas dos parâmetros de entrada relativos às unidades auxiliares. As definições técnicas para a determinação destes parâmetros constam do anexo IX. O ID do parâmetro é utilizado para fornecer uma referência clara entre os parâmetros dos anexos III e IX.

**Quadro 3**

**Parâmetros de entrada “Vehicle/Auxiliaries” (veículo/dispositivos auxiliares) para camiões médios e camiões pesados**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| EngineCoolingFan/Technology | P181 | string | [-] | Valores admitidos: “Crankshaft mounted - Electronically controlled visco clutch”, “Crankshaft mounted - Bimetallic controlled visco clutch”, “Crankshaft mounted - Discrete step clutch”, “Crankshaft mounted - On/off clutch”, “Belt driven or driven via transmission - Electronically controlled visco clutch”, “Belt driven or driven via transmission - Bimetallic controlled visco clutch”, “Belt driven or driven via transmission - Discrete step clutch”, “Belt driven or driven via transmission - On/off clutch”, “Hydraulic driven - Variable displacement pump”, “Hydraulic driven - Constant displacement pump”, “Electrically driven - Electronically controlled” |
| SteeringPump/Technology | P182 | string | [-] | Valores admitidos: “Fixed displacement”, “Fixed displacement with elec. control”, “Dual displacement”, “Dual displacement with elec. control”“Variable displacement mech. controlled”, “Variable displacement elec. controlled”, “Electric driven pump”, “Full electric steering gear” <br> Para VEE ou VHE com uma configuração do grupo motopropulsor “S” ou “S-IEPC” em conformidade com o ponto 10.1.1, “Electric driven pump” ou “Full electric steering gear” são os únicos valores admitidos. <br> Entrada separada para cada eixo direcional exigido, |
| ElectricSystem/Technology | P183 | string | [-] | Valores admitidos: “Standard technology”, “Standard technology - LED headlights, all”; |
| PneumaticSystem/Technology | P184 | string | [-] | Valores admitidos: “Small”, “Small + ESS”, “Small + visco clutch ”, “Small + mech. clutch”, “Small + ESS + AMS”, “Small + visco clutch + AMS”, “Small + mech. clutch + AMS”, “Medium Supply 1-stage”, “Medium Supply 1-stage + ESS”, “Medium Supply 1-stage + visco clutch”, “Medium Supply 1-stage + mech. clutch”, “Medium Supply 1-stage + ESS + AMS”, “Medium Supply 1-stage + visco clutch + AMS”, “Medium Supply 1-stage + mech. clutch + AMS”, “Medium Supply 2-stage”, “Medium Supply 2-stage + ESS”, “Medium Supply 2-stage + visco clutch ”, “Medium Supply 2-stage + mech. clutch”, “Medium Supply 2-stage + ESS + AMS”, “Medium Supply 2-stage + visco clutch + AMS”, “Medium Supply 2-stage + mech. clutch + AMS”, “Large Supply”, “Large Supply + ESS”, “Large Supply + visco clutch ”, “Large Supply + mech. clutch”, “Large Supply + ESS + AMS”, “Large Supply + visco clutch + AMS”, “Large Supply + mech. clutch + AMS”, “Vacuum pump”, “Small + elec. driven”, “Small + ESS + elec. driven ”, “Medium Supply 1-stage + elec. driven”, “Medium Supply 1-stage + AMS + elec. driven”, “Medium Supply 2-stage + elec. driven”, “Medium Supply 2-stage + AMS + elec. driven”, “Large Supply + elec. driven”, “Large Supply + AMS + elec. driven”, “Vacuum pump + elec. driven”; <br> Para os VEE, os únicos valores admitidos são as tecnologias “elec. driven”. |
| HVAC/Technology | P185 | string | [-] | Valores admitidos: “None”, “Default” |

**Quadro 3-A**

**Parâmetros de entrada “Vehicle/Auxiliaries” (veículo/dispositivos auxiliares) para autocarros pesados**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Autocarros pesados (veículo primário) | Autocarros pesados (veículo completo ou completado) |
|---|---|---|---|---|---|---|
| EngineCoolingFan/Technology | P181 | string | [-] | Valores admitidos: “Crankshaft mounted - Electronically controlled visco clutch”, “Crankshaft mounted - Bimetallic controlled visco clutch”, “Crankshaft mounted - Discrete step clutch 2 stages”, “Crankshaft mounted - Discrete step clutch 3 stages”, “Crankshaft mounted - On/off clutch”, “Belt driven or driven via transmission - Electronically controlled visco clutch”, “Belt driven or driven via transmission - Bimetallic controlled visco clutch”, “Belt driven or driven via transmission - Discrete step clutch 2 stages”, “Belt driven or driven via transmission - Discrete step clutch 3 stages”, “Belt driven or driven via transmission - On/off clutch”, “Hydraulic driven - Variable displacement pump”, “Hydraulic driven - Constant displacement pump”, “Electrically driven - Electronically controlled” | X |  |
| SteeringPump/Technology | P182 | string | [-] | Valores admitidos: “Fixed displacement”, “Fixed displacement with elec. control”, “Dual displacement”, “Dual displacement with elec. control”, “Variable displacement mech. controlled”, “Variable displacement elec. controlled”, “Electric driven pump”, “Full electric steering gear” <br> Para VEE ou VHE com uma configuração do grupo motopropulsor “S” ou “S-IEPC” em conformidade com o ponto 10.1.1, “Electric driven pump” ou “Full electric steering gear” são valores admitidos. <br> Entrada separada para cada eixo direcional exigido ativo | X |  |
| ElectricSystem/AlternatorTechnology | P294 | string | [-] | Valores admitidos: “conventional”, “smart”, “no alternator” <br> Entrada única por veículo <br> Para veículos MCI puros, os únicos valores admitidos são “conventional” ou “smart” <br> Para VHE com uma configuração do grupo motopropulsor “S” ou “S-IEPC” em conformidade com o ponto 10.1.1, os únicos valores admitidos são “no alternator” ou “conventional”. | X |  |
| ElectricSystem/SmartAlternatorRatedCurrent | P295 | integer | [A] | Entrada separada por alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorRatedVoltage | P296 | Integer | [V] | Valores admitidos: “12”, “24”, “48” <br> Entrada separada por alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorBatteryTechnology | P297 | string | [-] | Valores admitidos: “lead-acid battery – conventional”, “lead-acid battery –AGM”, “lead-acid battery – gel”, “li-ion battery - high power”, “li-ion battery - high energy” <br> Entrada separada por bateria carregada por sistema de alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorBatteryNominalVoltage | P298 | Integer | [V] | Valores admitidos: “12”, “24”, “48” <br> Se as baterias estiverem configuradas em série (p. ex., duas unidades de 12 V para um sistema de 24 V), deve ser fornecida a tensão nominal real das unidades de bateria individuais (12 V neste exemplo). <br> Entrada separada por bateria carregada por sistema de alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorBatteryRatedCapacity | P299 | Integer | [Ah] | Entrada separada por bateria carregada por sistema de alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorCapacitorTechnology | P300 | string | [-] | Valores admitidos: “with DCDC converter” <br> Entrada separada por condensador carregado por sistema de alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorCapacitorRatedCapacitance | P301 | integer | [F] | Entrada separada por condensador carregado por sistema de alternador inteligente | X |  |
| ElectricSystem/SmartAlternatorCapacitorRatedVoltage | P302 | Integer | [V] | Entrada separada por condensador carregado por sistema de alternador inteligente | X |  |
| ElectricSystem/SupplyFromHEVPossible | P303 | boolean | [-] |  | X |  |
| ElectricSystem/InteriorlightsLED | P304 | boolean | [-] |  |  | X |
| ElectricSystem/DayrunninglightsLED | P305 | boolean | [-] |  |  | X |
| ElectricSystem/PositionlightsLED | P306 | boolean | [-] |  |  | X |
| ElectricSystem/BrakelightsLED | P307 | boolean | [-] |  |  | X |
| ElectricSystem/HeadlightsLED | P308 | boolean | [-] |  |  | X |
| PneumaticSystem/SizeOfAirSupply | P309 | string | [-] | Valores admitidos: “Small”, “Medium Supply 1-stage”, “Medium Supply 2-stage”, “Large Supply 1-stage”, “Large Supply 2-stage”, “not applicable” <br> Para a transmissão do compressor eletricamente, deve ser indicado “not applicable”. <br> Para VEE, não é necessário introduzir dados. | X |  |
| PneumaticSystem/CompressorDrive | P310 | string | [-] | Valores admitidos: “mechanically”, “electrically” <br> Para VEE, o único valor admitido é “electrically”. | X |  |
| PneumaticSystem/Clutch | P311 | string | [-] | Valores admitidos: “none”, “visco”, “mechanically” <br> Para VEE, não é necessário introduzir dados. | X |  |
| PneumaticSystem/SmartRegenerationSystem | P312 | boolean | [-] |  | X |  |
| PneumaticSystem/SmartCompressionSystem | P313 | boolean | [-] | Para VEE ou VHE com uma configuração do grupo motopropulsor “S” ou “S-IEPC” de acordo com o ponto 10.1.1, não é necessário introduzir dados. | X |  |
| PneumaticSystem/Ratio Compressor ToEngine | P314 | double, 3 | [-] | Para a transmissão do compressor eletricamente, deve ser indicado “0.000”. <br> Para VEE, não é necessário introduzir dados. | X |  |
| PneumaticSystem/Air suspension control | P315 | string | [-] | Valores admitidos: “mechanically”, “electronically” | X |  |
| PneumaticSystem/SCRReagentDosing | P316 | boolean | [-] |  | X |  |
| HVAC/SystemConfiguration | P317 | int | [-] | Valores admitidos: “0” a “10” <br> No caso de um sistema AVAC incompleto, deve ser indicado “0”. “0” não é aplicável a veículos completos ou completados. |  | X |
| HVAC/ HeatPumpTypeDriverCompartmentCooling | P318 | string | [-] | Valores admitidos: “none”, “not applicable”, “R-744”, “non R-744 2-stage”, “non R-744 3-stage”, “non R-744 4-stage”, “non R-744 continuous” <br> “não aplicável” deve ser declarado para as configurações 6 e 10 do sistema de AVAC devido à alimentação a partir da bomba de calor de passageiros. |  | X |
| HVAC/ HeatPumpTypeDriverCompartmentHeating | P319 | string | [-] | Valores admitidos: “none”, “not applicable”, “R-744”, “non R-744 2-stage”, “non R-744 3-stage”, “non R-744 4-stage”, “non R-744 continuous” <br> “não aplicável” deve ser declarado para as configurações 6 e 10 do sistema de AVAC devido à alimentação a partir da bomba de calor de passageiros. |  | X |
| HVAC/ HeatPumpTypePassengerCompartmentCooling | P320 | string | [-] | Valores admitidos: “none”, “R-744”, “non R-744 2-stage”, “non R-744 3-stage”, non R-744 4-stage», “non R-744 continuous” <br> No caso de bombas de calor múltiplas com diferentes tecnologias para arrefecer o compartimento dos passageiros, deve ser declarada a tecnologia dominante (p. ex., de acordo com a potência disponível ou a utilização preferida em funcionamento). |  | X |
| HVAC/ HeatPumpTypePassengerCompartmentHeating | P321 | string | [-] | Valores admitidos: “none”, “R-744”, “non R-744 2-stage”, “non R-744 3-stage”, non R-744 4-stage», “non R-744 continuous” <br> No caso de bombas de calor múltiplas com diferentes tecnologias para arrefecer o compartimento dos passageiros, deve ser declarada a tecnologia dominante (p. ex., de acordo com a potência disponível ou a utilização preferida em funcionamento). |  | X |
| HVAC/AuxiliaryHeaterPower | P322 | integer | [W] | Introduzir “0” se não estiver instalado nenhum aquecedor auxiliar. |  | X |
| HVAC/Double glazing | P323 | boolean | [-] |  |  | X |
| HVAC/AdjustableCoolantThermostat | P324 | boolean | [-] |  | X |  |
| HVAC/AdjustableAuxiliaryHeater | P325 | boolean | [-] |  |  | X |
| HVAC/EngineWasteGasHeatExchanger | P326 | boolean | [-] | Para VEE, não é necessário introduzir dados. | X |  |
| HVAC/SeparateAirDistributionDucts | P327 | boolean | [-] |  |  | X |
| HVAC/WaterElectricHeater | P328 | boolean | [-] | Introduzir dados apenas para VHE e VEE |  | X |
| HVAC/AirElectricHeater | P329 | boolean | [-] | Introduzir dados apenas para VHE e VEE |  | X |
| HVAC/OtherHeating Technology | P330 | boolean | [-] | Introduzir dados apenas para VHE e VEE |  | X |

**Quadro 4**

**Parâmetros de entrada “Vehicle/EngineTorqueLimits” (veículo/limites de binário do motor) por velocidade (facultativo)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Camiões pesados | Camiões médios | Autocarros pesados (veículo primário) | Autocarros pesados (veículo completo ou completado) |
|---|---|---|---|---|---|---|---|---|
| Velocidade engrenada | P196 | integer | [-] | Apenas têm de ser especificados números de velocidades nos casos em que são aplicáveis os limites do binário do motor relativos ao veículo em conformidade com o ponto 6 | X | X | X |  |
| MaxTorque | P197 | integer | [Nm] |  | X | X | X |  |

**Quadro 5**

**Parâmetros de entrada para veículos isentos nos termos do artigo 9.º**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Camiões pesados | Camiões médios | Autocarros pesados (veículo primário) | Autocarros pesados (veículo completo e completado) |
|---|---|---|---|---|---|---|---|---|
| Manufacturer | P235 | token | [-] |  | X | X | X | X |
| ManufacturerAddress | P252 | token | [-] |  | X | X | X | X |
| Model_CommercialName | P236 | token | [-] |  | X | X | X | X |
| VIN | P238 | token | [-] |  | X | X | X | X |
| Date | P239 | dateTime | [-] | Data e hora de criação dos dados e informações de entrada | X | X | X | X |
| LegislativeCategory | P251 | string | [-] | Valores admitidos: “N2”, “N3”, “M3” | X | X | X | X |
| ChassisConfiguration | P036 | string | [-] | Valores admitidos: “Rigid Lorry”, “Tractor”, “Van”, “Bus” | X | X | X |  |
| AxleConfiguration | P037 | string | [-] | Valores admitidos: “4 × 2”, “4 × 2F”, “6 × 2”, “6 × 4”, “8 × 2”, “8 × 4” em que “4 × 2F” se refere a veículos 4 × 2 com um eixo motor dianteiro | X | X | X |  |
| Articulated | P281 | boolean |  | Em conformidade com a definição estabelecida no anexo I do presente regulamento. |  |  | X |  |
| CorrectedActualMass | P038 | int | [kg] | De acordo com a “massa efetiva do veículo corrigida” conforme especificada no ponto 2, subponto 4 | X | X |  | X |
| TechnicalPermissibleMaximumLadenMass | P041 | int | [kg] | Em conformidade com o artigo 2.º, ponto 7, do Regulamento (UE) n.º 1230/2012 | X | X | X | X |
| ZeroEmissionVehicle | P269 | boolean | [-] | Conforme definido no artigo 3.º, ponto 15. | X | X | X |  |
| Sleepercab | P276 | boolean | [-] |  | X |  |  |  |
| ClassBus | P282 | string | [-] | Valores admitidos: “I”, “I+II”, “A”, “II”, “II+III”, “III”, “B” em conformidade com o ponto 2 do Regulamento n.º 107 da ONU |  |  |  | X |
| NumberPassengersSeatsLowerDeck | P283 | int | [-] | Número de assentos para passageiros — excluindo os assentos do condutor e da tripulação. <br> No caso de um veículo de dois andares, este parâmetro deve ser utilizado para declarar os assentos para passageiros do andar inferior. No caso de um veículo de um andar, este parâmetro deve ser utilizado para declarar o número total de assentos para passageiros. |  |  |  | X |
| NumberPassengersStandingLowerDeck | P354 | int | [-] | Número de passageiros de pé registados <br> No caso de um veículo de dois andares, este parâmetro deve ser utilizado para declarar os passageiros de pé registados do andar inferior. No caso de um veículo de um andar, este parâmetro deve ser utilizado para declarar o número total de passageiros de pé registados. |  |  |  | X |
| NumberPassengersSeatsUpperDeck | P284 | int | [-] | Número de assentos para passageiros — excluindo os assentos do condutor e da tripulação do andar superior num veículo de dois andares. <br> Para os veículos de um andar, deve ser fornecido “0” como entrada. |  |  |  | X |
| NumberPassengersStandingUpperDeck | P355 | int | [-] | Número de passageiros de pé registados do andar superior num veículo de dois andares. <br> Para os veículos de um andar, deve ser fornecido “0” como entrada. |  |  |  | X |
| BodyworkCode | P285 | int | [-] | Valores admitidos: “CA”, “CB”, “CC”, “CD”, “CE”, “CF”, “CG”, “CH”, “CI”, “CJ” em conformidade com o anexo I, parte C, ponto 3, do Regulamento (UE) 2018/585 |  |  |  | X |
| LowEntry | P286 | boolean | [-] | “Entrada baixa” em conformidade com o anexo I, ponto 1.2.2.3 |  |  |  | X |
| HeightIntegratedBody | P287 | int | [mm] | Em conformidade com o ponto 2, subponto 5 |  |  |  | X |
| SumNetPower | P331 | int | [W] | Soma máxima possível da potência de propulsão positiva de todos os conversores de energia ligados ao sistema de tração do veículo ou às rodas | X | X | X |  |
| Technology | P332 | string | [-] | Em conformidade com o quadro 1 do apêndice 1. <br> Valores admitidos: “Dual-fuel vehicle Article 9 exempted”, “In-motion charging Article 9 exempted”, “Multiple powertrains Article 9 exempted”, “FCV Article 9 exempted”, “H2 ICE Article 9 exempted”, “HEV Article 9 exempted”, “PEV Article 9 exempted”, “HV Article 9 exempted” | X | X | X |  |

**Quadro 6**

**Parâmetros de entrada “Advanced driver assistance systems” (sistemas avançados de assistência à condução)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Camiões pesados | Camiões médios | Autocarros pesados (veículo primário) | Autocarros pesados (veículo completo e completado) |
|---|---|---|---|---|---|---|---|---|
| EngineStopStart | P271 | boolean | [-] | Em conformidade com o ponto 8.1.1 <br> Só devem ser introduzidos dados para veículos MCI puros e VHE. | X | X | X | X |
| EcoRollWithoutEngineStop | P272 | boolean | [-] | Em conformidade com o ponto 8.1.2 <br> Só devem ser introduzidos dados para veículos MCI puros. | X | X | X | X |
| EcoRollWithEngineStop | P273 | boolean | [-] | Em conformidade com o ponto 8.1.3 <br> Só devem ser introduzidos dados para veículos MCI puros. | X | X | X | X |
| PredictiveCruiseControl | P274 | string | [-] | Em conformidade com o ponto 8.1.4, valores admitidos: “1,2”, “1,2,3” | X | X | X | X |
| APTEcoRollReleaseLockupClutch | P333 | boolean | [-] | Relevante apenas no caso de transmissões APT-S e APT-P em combinação com qualquer função de “eco-rol”. Definir como “true” (verdadeiro) se a funcionalidade 2, tal como definida no ponto 8.1.2, for o modo de “eco-rol” predominante. <br> Só devem ser introduzidos dados para veículos MCI puros. | X | X | X | X |

**Quadro 7**

**Parâmetros gerais de entrada para VHE e VEE**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência | Camiões pesados | Camiões médios | Autocarros pesados (veículo primário) | Autocarros pesados (veículo completo ou completado) |
|---|---|---|---|---|---|---|---|---|
| ArchitectureID | P400 | string | [-] | Em conformidade com o ponto 10.1.3, são admitidos os seguintes valores: <br> “E2”, “E3”, “E4”, “E-IEPC”, “P1”, “P2”, “P2.5”, “P3”, “P4”, “S2”, “S3”, “S4”, “S-IEPC” | X | X | X |  |
| OvcHev | P401 | boolean | [-] | Em conformidade com o ponto 2, subponto 31 | X | X | X |  |
| MaxChargingPower | P402 | Integer | [W] | A potência máxima de carga permitida pelo veículo para o carregamento do exterior deve ser declarada como dado de entrada da ferramenta de simulação. <br> Relevante apenas quando o parâmetro “OvcHev” for definido como “true” (verdadeiro). | X | X | X |  |

**Quadro 8**

**Parâmetros de entrada por posição da máquina elétrica**

**(Aplicável apenas se o componente estiver presente no veículo)**

<table> <tbody> <tr> <td>Nome do parâmetro</td> <td>ID do parâmetro</td> <td>Tipo</td> <td>Unidade</td> <td>Descrição/referência</td> </tr> <tr> <td>PowertrainPosition</td> <td>P403</td> <td>string</td> <td>[-]</td> <td>Posição da ME no grupo motopropulsor do veículo em conformidade com os pontos 10.1.2 e 10.1.3. Valores admitidos: “1”, “2”, “2.5”, “3”, “4”, “GEN”. Só é permitida uma posição de ME por grupo motopropulsor, exceto para a arquitetura “S”. A arquitetura “S” exige a posição de ME “GEN” e, adicionalmente, que uma outra posição de ME seja “2”, “3” ou “4”. A posição “1” não é admitida para arquiteturas “S” e “E” A posição “GEN” é apenas admitida para a arquitetura “S”</td> </tr> <tr> <td>Count</td> <td>P404</td> <td>integer</td> <td>[-]</td> <td>Número de máquinas elétricas idênticas na posição de ME especificada. No caso de o parâmetro “PowertrainPosition” ser “4”, a contagem deve ser composta por múltiplos de 2(p. ex., 2, 4, 6).</td> </tr> <tr> <td>CertificationNumberEM</td> <td>P405</td> <td>token</td> <td>[-]</td> <td></td> </tr> <tr> <td>CertificationNumberADC</td> <td>P406</td> <td>token</td> <td>[-]</td> <td>Entrada facultativa no caso de uma relação de transmissão única adicional (componente adicional da transmissão) entre o veio da ME e o ponto de ligação ao grupo motopropulsor do veículo, em conformidade com o ponto 10.1.2. Não é permitido se o parâmetro “IHPCType” for definido como “IHPC Type 1”.</td> </tr> <tr> <td>P2.5GearRatios</td> <td>P407</td> <td>double, 3</td> <td>[-]</td> <td>Aplicável apenas no caso de o parâmetro “PowertrainPosition” ser fixado em “P2.5” Declarado para cada relação de transmissão para a marcha à frente. Valor declarado para a relação de transmissão definido por “nGBX_in / nEM” no caso de ME sem componente adicional da transmissão ou “nGBX_in / nADC” no caso de ME com componente adicional da transmissão. <table> <tbody> <tr> <td>nGBX_in</td> <td>=</td> <td>velocidade de rotação no veio de entrada da transmissão</td> </tr> <tr> <td>nEM</td> <td>=</td> <td>velocidade de rotação no veio de saída da ME</td> </tr> <tr> <td>nADC</td> <td>=</td> <td>velocidade de rotação no veio de saída do componente adicional da transmissão</td> </tr> </tbody> </table></td> </tr> </tbody> </table>

**Quadro 9**

**Limitações do binário por posição da máquina elétrica (facultativo)**

**Declaração de um conjunto de dados separado para cada nível de tensão medido em “CertificationNumberEM”. Não é permitido se o parâmetro “IHPCType” for definido como “IHPC Type 1”.**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| OutputShaftSpeed | P408 | double, 2 | [1/min] | As mesmas entradas para a velocidade de rotação a declarar em “CertificationNumberEM” para o parâmetro “P468” constante do anexo X-B, apêndice 15. |
| MaxTorque | P409 | double, 2 | [Nm] | Binário máximo da ME (referente ao veio de saída) como função dos pontos de velocidade de rotação declarados no parâmetro “P469” constante do anexo X-B, apêndice 15. <br> Cada valor do binário máximo declarado deve ser inferior a 0,9 vezes o valor original à respetiva velocidade de rotação ou corresponder exatamente ao valor original à respetiva velocidade de rotação. <br> Os valores do binário máximo declarado não podem ser inferiores a zero. <br> Se o parâmetro “Count” (P404) for superior a um, o binário máximo deve ser declarado para uma única ME (tal como está presente no ensaio de componente para a ME em “CertificationNumberEM”). |
| MinTorque | P410 | double, 2 | [Nm] | Binário mínimo da ME (referente ao veio de saída) como função dos pontos de velocidade de rotação declarados no parâmetro “P470” constante do anexo X-B, apêndice 15. <br> Cada valor do binário mínimo declarado deve ser superior a 0,9 vezes o valor original à respetiva velocidade de rotação ou corresponder exatamente ao valor original à respetiva velocidade de rotação. <br> Os valores do binário mínimo declarado não podem ser superiores a zero. <br> Se o parâmetro “Count” (P404) for superior a um, o binário mínimo deve ser declarado para uma única ME (tal como está presente no ensaio de componente para a ME em “CertificationNumberEM”). |

**Quadro 10**

**Parâmetros de entrada por SRAEE**

**(Aplicável apenas se o componente estiver presente no veículo)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| StringID | P411 | integer | [-] | A disposição dos subsistemas representativos de bateria em conformidade com o anexo X-B a nível do veículo é declarada atribuindo a cada subsistema de bateria uma cadeia (string) específica definida por este parâmetro. Todas as cadeias específicas estão ligadas em paralelo, todos os subsistemas de bateria localizados numa cadeia paralela específica estão ligados em série. <br> Valores admitidos: “1”, “2”, “3”,... |
| CertificationNumberREESS | P412 | token | [-] |  |
| SOCmin | P413 | integer | [%] | Introdução facultativa. <br> Relevante apenas no caso de tipo de SRAEE “bateria”. <br> Parâmetro apenas eficaz na ferramenta de simulação quando o valor introduzido é superior ao valor genérico, tal como documentado no manual do utilizador. |
| SOCmax | P414 | integer | [%] | Introdução facultativa. <br> Relevante apenas no caso de tipo de SRAEE “bateria”. <br> Parâmetro apenas eficaz na ferramenta de simulação quando o valor introduzido é inferior ao valor genérico, tal como documentado no manual do utilizador. |

**Quadro 11**

**Aumento das limitações para VHE paralelo (facultativo)**

**Só é permitido se a configuração do grupo motopropulsor em conformidade com o ponto 10.1.1 for “P” ou “IHPC Type 1”.**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| RotationalSpeed | P415 | double, 2 | [1/min] | Referente à velocidade do veio de entrada da transmissão |
| BoostingTorque | P416 | double, 2 | [Nm] | De acordo com o ponto 10.2 |

**4. Massa do veículo para tratores e camiões rígido médios, tratores e camiões rígidos pesados**

|  | 4.1 | A massa do veículo utilizada como dado de entrada da ferramenta de simulação deve ser a massa efetiva do veículo corrigida. |
|---|---|---|

<table> <tbody> <tr> <td></td> <td>4.2</td> <td>Se nem todo o equipamento-padrão estiver instalado, o fabricante deve juntar a massa dos seguintes elementos de construção à massa efetiva do veículo corrigida: <table> <tbody> <tr> <td>a)</td> <td>A proteção à frente contra o encaixe em conformidade com o disposto no Regulamento (UE) 2019/2144 (**) do Parlamento Europeu e do Conselho;</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>b)</td> <td>Proteção à retaguarda contra o encaixe em conformidade com o Regulamento (UE) 2019/2144;</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>c)</td> <td>Proteção lateral em conformidade com o Regulamento (UE) 2019/2144;</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>d)</td> <td>Prato de engate em conformidade com o Regulamento (UE) 2019/2144.</td> </tr> </tbody> </table></td> </tr> </tbody> </table>

<table> <tbody> <tr> <td></td> <td>4.3</td> <td>A massa dos elementos de construção referidos no ponto 4.2 é a seguinte: Para os veículos dos grupos 1s, 1, 2 e 3 definidos no quadro 1 do anexo I, e para os grupos de veículos 51 e 53 definidos no quadro 2 do anexo I. <table> <tbody> <tr> <td>a)</td> <td>Proteção à frente contra o encaixe</td> <td>45 kg;</td> </tr> <tr> <td>b)</td> <td>Proteção à retaguarda contra o encaixe</td> <td>40 kg;</td> </tr> <tr> <td>c)</td> <td>Proteção lateral</td> <td>8,5 kg/m × entre-eixo [m] – 2,5 kg.</td> </tr> </tbody> </table> Para os veículos dos grupos 4, 5, 9 a 12 e 16 definidos no quadro 1 do anexo I. <table> <tbody> <tr> <td>a)</td> <td>Proteção à frente contra o encaixe</td> <td>50 kg;</td> </tr> <tr> <td>b)</td> <td>Proteção à retaguarda contra o encaixe</td> <td>45 kg;</td> </tr> <tr> <td>c)</td> <td>Proteção lateral</td> <td>14 kg/m × entre-eixo [m] – 17 kg;</td> </tr> <tr> <td>d)</td> <td>Prato de engate</td> <td>210 kg.</td> </tr> </tbody> </table></td> </tr> </tbody> </table>

**5. Eixos hidráulicos e mecânicos**

No caso de veículos equipados com:

a) Eixos hidráulicos, os eixos devem ser considerados não acionáveis e não são tidos em conta pelo fabricante ao estabelecer a configuração dos eixos de um veículo;

b) Eixos mecânicos, os eixos devem ser considerados acionáveis e são tidos em conta pelo fabricante ao estabelecer a configuração dos eixos de um veículo.

**6. Limites do binário do motor dependentes da velocidade e desativação de velocidades**

**6.1. Limites do binário do motor dependentes da velocidade**

Para 50 % das velocidades mais altas (por exemplo, da velocidade 7 à 12 numa caixa de 12 velocidades), o fabricante do veículo pode declarar um limite para o binário máximo do motor dependente das velocidades que não ultrapasse 95 % do binário máximo do motor.

**6.2 Desativação de velocidades**

Para as 2 velocidades mais elevadas (por exemplo, as velocidades 5 e 6 numa caixa de 6 velocidades), o fabricante do veículo pode declarar uma desativação total das velocidades introduzindo na ferramenta de simulação 0 Nm como limite de binário específico das velocidades.

**6.3 Requisitos de verificação**

Os limites do binário do motor dependentes da velocidade, em conformidade com o ponto 6.1, e a desativação de velocidades em conformidade com o ponto 6.2 são sujeitos a verificação no procedimento de ensaio de verificação (VTP) estabelecido no anexo X-A, ponto 6.1.1.1, alínea c).

**7. Velocidade de ralenti específica do veículo**

|  | 7.1. | A velocidade de marcha lenta sem carga (ralenti) tem de ser declarada para cada veículo com um MCI. Esse ralenti declarado do veículo deve ser igual ou superior ao especificado nos dados de homologação do motor. |
|---|---|---|

**8. Sistemas avançados de assistência à condução**

<table> <tbody> <tr> <td></td> <td>8.1</td> <td>Devem ser declarados nos dados de entrada da ferramenta de simulação os seguintes tipos de sistemas avançados de assistência à condução, destinados principalmente a reduzir o consumo de combustível e as emissões de CO2: <table> <tbody> <tr> <td>8.1.1</td> <td>Função “para/arranca” do motor durante as paragens do veículo: sistema que automaticamente desliga e liga de novo o motor de combustão interna durante as paragens do veículo, para reduzir o tempo de ralenti. Para o motor desligar automaticamente, o tempo decorrido após a paragem do veículo não pode ser superior a 3 segundos.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>8.1.2</td> <td>“Eco-rol” sem função “para/arranca” do motor: sistema que automaticamente desacopla o motor de combustão interna do sistema de tração em condições específicas de circulação em declive, com gradiente negativo reduzido. O sistema deve estar ativo, pelo menos, em todas as velocidades superiores a 60 km/h definidas no controlo de cruzeiro. Qualquer sistema a declarar nas informações de entrada para a ferramenta de simulação deve abranger uma ou ambas as seguintes funcionalidades: <table> <tbody> <tr> <td>Funcionalidade (1) O motor de combustão é desacoplado do sistema de tração e o motor funciona em ralenti. No caso das transmissões com mudanças rápidas de velocidade automáticas (APT), a embraiagem de bloqueio do conversor de binário é fechada.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>Funcionalidade (2) Embraiagem de bloqueio do conversor de binário aberta A embraiagem de bloqueio do conversor de binário é aberta durante o modo “eco-rol”. Tal permite que o motor funcione em modo de marcha em roda livre a velocidades inferiores do motor e reduz ou mesmo elimina a injeção de combustível. A funcionalidade (2) é relevante apenas para as transmissões APT.</td> </tr> </tbody> </table></td> </tr> </tbody> </table> <table> <tbody> <tr> <td>8.1.3</td> <td>“Eco-rol” com função “para/arranca” do motor: sistema que automaticamente desacopla o motor de combustão interna do sistema de tração em condições específicas de circulação em declive, com gradiente negativo reduzido. Nestas fases “eco-rol”, o motor de combustão interna desliga-se após um curto período e permanece desligado durante a maior parte da fase “eco-rol”. O sistema deve estar ativo, pelo menos, a todas as velocidades superiores a 60 km/h definidas no controlo de cruzeiro.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>8.1.4</td> <td>Regulação preditiva da velocidade (predictive cruise control, PCC): sistema que otimiza a utilização de energia potencial durante um ciclo de condução, através da previsão disponível de dados relativos ao gradiente da rodovia e utilização de um sistema GPS. O sistema PCC declarado nos dados de entrada da ferramenta de simulação deve garantir uma previsão do gradiente numa distância superior a 1 000 m e incluir todas as seguintes funcionalidades: <table> <tbody> <tr> <td>(1)</td> <td>Roda livre em aproximação do topo Ao atingir o topo de uma elevação, a velocidade do veículo reduz antes de atingir o ponto em que o veículo começa a acelerar apenas por força da gravidade, face à velocidade definida do controlo de cruzeiro, permitindo reduzir a travagem na fase seguinte de descida.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(2)</td> <td>Aceleração sem potência do motor Na condução em declive a baixa velocidade com um gradiente negativo acentuado, a aceleração do veículo é assegurada sem utilizar a potência do motor, permitindo reduzir a travagem durante a descida.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(3)</td> <td>Roda livre em declive Na condução em declive, quando o veículo trava em velocidade excessiva, o sistema PCC aumenta essa velocidade durante um curto período de modo a terminar a fase de descida com uma velocidade mais elevada. Velocidade excessiva significa, neste caso, uma velocidade do veículo superior à velocidade definida pelo sistema de controlo de cruzeiro.</td> </tr> </tbody> </table></td> </tr> </tbody> </table> Um sistema PCC pode ser declarado enquanto dado de entrada da ferramenta de simulação se incluir as funcionalidades referidas ou nos pontos 1) e 2) ou nos pontos 1), 2) e 3).</td> </tr> </tbody> </table>

<table> <tbody> <tr> <td></td> <td>8.2</td> <td>As onze combinações de sistemas avançados de assistência à condução indicadas no quadro 12 constituem parâmetros de entrada na ferramenta de simulação. As combinações 2 a 11 não podem ser declaradas para transmissões manuais sincronizadas (SMT). As combinações n.ºs 3, 6, 9 e 11 não podem ser declaradas no caso das transmissões APT. Quadro 12 Combinações dos sistemas avançados de assistência à condução que constituem parâmetros de entrada na ferramenta de simulação <table> <tbody> <tr> <td>N.º da combinação</td> <td>Função “para/arranca” do motor durante as paragens do veículo</td> <td>“Eco-rol” sem função “para/arranca” do motor</td> <td>“Eco-rol” com função “para/arranca” do motor</td> <td>Regulação preditiva da velocidade</td> </tr> <tr> <td>1</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Não</td> </tr> <tr> <td>2</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td>Não</td> </tr> <tr> <td>3</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Não</td> </tr> <tr> <td>4</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> </tr> <tr> <td>5</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Não</td> </tr> <tr> <td>6</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> </tr> <tr> <td>7</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Sim</td> </tr> <tr> <td>8</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td>Sim</td> </tr> <tr> <td>9</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> </tr> <tr> <td>10</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Sim</td> </tr> <tr> <td>11</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Sim</td> </tr> </tbody> </table></td> </tr> </tbody> </table>

|  | 8.3 | Qualquer sistema avançado de assistência à condução declarado nos dados de entrada da ferramenta de simulação deve ser regulado por defeito no modo de economia de combustível, após cada ciclo em que o veículo é ligado e desligado na ignição. |
|---|---|---|

|  | 8.4 | Se um sistema avançado de assistência à condução for declarado nos dados de entrada da ferramenta de simulação, deve ser possível verificar a presença desse sistema com base numa condução em condições reais e nas definições do sistema de acordo com o ponto 8.1. Se for declarada uma determinada combinação de sistemas, deve ser também demonstrada a interação das funcionalidades (por exemplo, regulação preditiva da velocidade e “eco-rol” com função “para/arranca” do motor). No procedimento de verificação, deve ser tido em conta que a ativação dos sistemas requer determinadas condições (por exemplo, motor a temperatura de funcionamento para a função “para-arranca”, determinados intervalos de velocidade para o PCC e certos gradientes das estradas para o sistema “eco-rol”). O fabricante do veículo tem de apresentar uma descrição funcional das condições-limite em que os sistemas estão “inativos” ou quando a sua eficiência se encontra reduzida. A entidade homologadora pode solicitar ao requerente uma justificação técnica dessas condições e avaliá-la para efeitos de conformidade. |
|---|---|---|

**9. Volume de carga**

<table> <tbody> <tr> <td></td> <td>9.1.</td> <td>Para os veículos com configuração do quadro “furgão”, o volume de carga deve ser calculado pela seguinte equação: Formula em que as dimensões devem ser determinadas em conformidade com o quadro 13 e a figura 3. Quadro 13 Definições relacionadas com o volume de carga para camiões médios de tipo furgão <table> <tbody> <tr> <td>Símbolo da fórmula</td> <td>Dimensão</td> <td>Definição</td> </tr> <tr> <td>LC,floor</td> <td>Comprimento do compartimento de carga no piso</td> <td><table> <tbody> <tr> <td>—</td> <td>Distância longitudinal do ponto mais recuado da última fila de assentos ou da divisória ao ponto mais avançado da traseira fechada do compartimento, projetada até ao plano de simetria longitudinal</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>Medido à altura da superfície do piso de carga</td> </tr> </tbody> </table></td> </tr> <tr> <td>LC</td> <td>Comprimento do comprimento da carga</td> <td><table> <tbody> <tr> <td>—</td> <td>Distância longitudinal do plano X tangente ao ponto mais recuado do encosto do banco, incluindo apoios de cabeça da última fila de assentos ou da divisória, até ao plano X mais avançado tangente à traseira fechada do compartimento, isto é, ao taipal traseiro ou às portas traseiras ou a qualquer outra superfície limite</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>Medido à altura do ponto mais recuado da última fila de assentos ou da divisória</td> </tr> </tbody> </table></td> </tr> <tr> <td>WC,max</td> <td>Largura máxima do compartimento de carga</td> <td><table> <tbody> <tr> <td>—</td> <td>Distância lateral máxima do compartimento de carga</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>Medida entre o piso de carga e 70 mm acima do piso</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>A medição exclui o arco de transição, saliências pontuais, depressões ou bolsas, caso existam</td> </tr> </tbody> </table></td> </tr> <tr> <td>WC,wheelhouse</td> <td>Largura do compartimento de carga entre as cavas das rodas</td> <td><table> <tbody> <tr> <td>—</td> <td>Distância lateral mínima entre as interferências limitadoras das cavas das rodas (passagem)</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>Medida entre o piso de carga e 70 mm acima do piso</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>A medição exclui o arco de transição, saliências pontuais, depressões ou bolsas, caso existam</td> </tr> </tbody> </table></td> </tr> <tr> <td>HC,max</td> <td>Altura máxima do compartimento de carga</td> <td><table> <tbody> <tr> <td>—</td> <td>Distância vertical máxima entre o piso de carga e o revestimento interior do tejadilho ou outra superfície limite</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>Medida atrás da última fila de assentos ou divisória na linha central do veículo</td> </tr> </tbody> </table></td> </tr> <tr> <td>HC,rearwheel</td> <td>Altura do compartimento de carga na roda traseira</td> <td><table> <tbody> <tr> <td>—</td> <td>Distância vertical entre o topo do piso de carga e o revestimento interior do tejadilho ou a superfície limite</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>Medida na coordenada X da roda traseira na linha central do veículo</td> </tr> </tbody> </table></td> </tr> </tbody> </table></td> </tr> </tbody> </table>

**Figura 3**

**Definição do volume de carga para camiões médios**

Image 5

**10. VHE e VEE**

As disposições que se seguem aplicam-se apenas no caso de VHE e VEE.

**10.1 Definição da arquitetura do grupo motopropulsor do veículo**

**10.1.1 Definição da configuração do grupo motopropulsor**

A configuração do grupo motopropulsor do veículo deve ser determinada de acordo com as seguintes definições:

No caso de um VHE:

(a) “P” no caso de um VHE paralelo

(b) “S” no caso de um VHE de série

(c) “S-IEPC” no caso de um componente IEPC estar presente no veículo

(d) “IHPC Type 1”, no caso de o parâmetro “IHPCType” do componente da máquina elétrica ser definido como “IHPC Type 1”

No caso de um VEE:

(a) “E” no caso de um componente de ME estar presente no veículo

(b) “E-IEPC” no caso de um componente IEPC estar presente no veículo

**10.1.2 Definição das posições das ME no grupo motopropulsor do veículo**

Se a configuração do grupo motopropulsor do veículo em conformidade com o ponto 10.1.1 for “P”, “S” ou “E”, a posição da ME instalada no grupo motopropulsor do veículo deve ser determinada em conformidade com as definições constantes do quadro 14.

**Quadro 14**

**Posições possíveis das ME no grupo motopropulsor do veículo**

| Índice de posição de ME | Configuração do grupo motopropulsor nos termos do ponto 10.1.1 | Tipo de transmissão nos termos do anexo VI, apêndice 12, quadro 1 | Definição/Requisitos (2) | Outras explicações |
|---|---|---|---|---|
| 1 | P | AMT, APT-S, APT-P | Ligada ao grupo motopropulsor a montante da embraiagem (no caso de AMT) ou a montante do veio de entrada do conversor de binário (no caso de APT-S ou APT-P). <br> A ME está ligada à cambota do MCI diretamente ou através de um tipo de ligação mecânica (p. ex., correia). | Distinção de P0: As ME que, em princípio, não podem contribuir para a propulsão do veículo (ou seja, alternadores) são tratadas ao introduzir os dados relativos aos sistemas auxiliares (ver o quadro 3, relativo aos camiões, e o quadro 3-A, relativo aos autocarros, do presente anexo e o anexo IX). <br> No entanto, as ME nesta posição, que podem, em princípio, contribuir para a propulsão do veículo, mas para as quais o binário máximo declarado em conformidade com o quadro 9 do presente anexo é fixado em zero, devem ser declaradas como “P1”. |
| 2 | P | AMT | A máquina elétrica está ligada ao grupo motopropulsor a jusante da embraiagem e a montante do veio de entrada da transmissão. |  |
| 2 | E, S | AMT, APT-N, APT-S, APT-P | A máquina elétrica está ligada ao grupo motopropulsor a montante do veio de entrada da transmissão (no caso de AMT ou APT-N) ou a montante do veio de entrada do conversor de binário (no caso de APT-S, APT-P). |  |
| 2,5 | P | AMT, APT-S, APT-P | A máquina elétrica está ligada ao grupo motopropulsor a jusante da embraiagem (no caso de AMT) ou a jusante do veio de entrada do conversor de binário (no caso de APT-S ou APT-P) e a montante do veio de saída da transmissão. | A ME está ligada a um veio específico no interior da transmissão (p. ex., eixo secundário). Deve ser fornecida uma relação de transmissão específica para cada velocidade mecânica na transmissão em conformidade com o quadro 8. |
| 3 | P | AMT, APT-S, APT-P | A máquina elétrica está ligada ao grupo motopropulsor a jusante do veio de saída da transmissão e a montante do eixo. |  |
| 3 | E, S | n.a. | A máquina elétrica está ligada ao grupo motopropulsor a montante do eixo. |  |
| 4 | P | AMT, APT-S, APT-P | A máquina elétrica está ligada ao grupo motopropulsor a jusante do eixo. |  |
| 4 | E, S | n.a. | A máquina elétrica está ligada ao cubo da roda e a mesma configuração está instalada duas vezes em aplicação simétrica (isto é, uma do lado esquerdo e outra do lado direito do veículo, na mesma posição em relação à roda na direção longitudinal). |  |
| GEN | S | n.a. | A máquina elétrica está ligada mecanicamente a um MCI, mas não está ligada mecanicamente às rodas do veículo. |  |

**10.1.3 Definição do ID da arquitetura do grupo motopropulsor**

O valor de entrada do ID da arquitetura do grupo motopropulsor ID exigido em conformidade com o quadro 7 deve ser determinado com base na configuração do grupo motopropulsor em conformidade com o ponto 10.1.1 e na posição da ME no grupo motopropulsor do veículo em conformidade com o ponto 10.1.2 (se aplicável) a partir das combinações válidas de dados de entrada na ferramenta de simulação enumerados no quadro 15.

No caso de a configuração do grupo motopropulsor em conformidade com o ponto 10.1.1 ser “IHPC Type 1”, aplicam-se as seguintes disposições:

(a) O ID “P2” da arquitetura do grupo motopropulsor deve ser declarado em conformidade com o quadro 7 e os dados dos componentes do grupo motopropulsor indicados no quadro 15 para “P2” devem ser introduzidos na ferramenta de simulação com dados de componente separados para a ME e a transmissão, determinados em conformidade com o anexo X-B, ponto 4.4.3.

(b) Os dados de componente para a ME em conformidade com a alínea a) devem ser inseridos na ferramenta de simulação com o parâmetro “PowertrainPosition” definido como “2” em conformidade com o quadro 8.

**Quadro 15**

**Dados de entrada válidos sobre a arquitetura do grupo motopropulsor para a ferramenta de simulação**

<table> <tbody> <tr> <td rowspan="2">Tipo de grupo motopropulsor</td> <td rowspan="2">Configuração do grupo motopropulsor</td> <td rowspan="2">ID da arquitetura para introdução na ferramenta VECTO</td> <td colspan="8">Componente do grupo motopropulsor presente no veículo</td> <td rowspan="2">Observações</td> </tr> <tr> <td>MCI</td> <td>ME posição GEN</td> <td>ME posição 1</td> <td>ME posição 2</td> <td>Transmissão</td> <td>ME posição 3</td> <td>Eixo</td> <td>ME posição 4</td> </tr> <tr> <td rowspan="4">VEE</td> <td rowspan="3">E</td> <td>E2</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td></td> </tr> <tr> <td>E3</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td></td> </tr> <tr> <td>E4</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td></td> </tr> <tr> <td>IEPC</td> <td>E-IEPC</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>(3)</td> <td>Não</td> <td></td> </tr> <tr> <td rowspan="9">VHE</td> <td rowspan="5">P</td> <td>P1</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td></td> </tr> <tr> <td>P2</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td>(4)</td> </tr> <tr> <td>P2.5</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td>(5)</td> </tr> <tr> <td>P3</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>(6)</td> </tr> <tr> <td>P4</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td></td> </tr> <tr> <td rowspan="4">S</td> <td>S2</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Sim</td> <td>Não</td> <td></td> </tr> <tr> <td>S3</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td></td> </tr> <tr> <td>S4</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Sim</td> <td></td> </tr> <tr> <td>S-IEPC</td> <td>Sim</td> <td>Sim</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>Não</td> <td>(3)</td> <td>Não</td> <td></td> </tr> </tbody> </table>

**10.2 Definição de limitação da aceleração para VHE paralelos**

O fabricante do veículo pode declarar limitações ao binário total de propulsão de todo o grupo motopropulsor relativamente ao veio de entrada da transmissão para um VHE paralelo, a fim de restringir as capacidades de aceleração do veículo.

A declaração de tais limitações só é permitida se a configuração do grupo motopropulsor em conformidade com o ponto 10.1.1 for “P” ou “IHPC Type 1”.

As limitações são declaradas como binário adicional permitido no topo da curva do MCI a plena carga, dependendo da velocidade de rotação do veio de entrada da transmissão. A ferramenta de simulação efetua uma interpolação linear para determinar o binário adicional aplicável entre os valores declarados a duas velocidades de rotação específicas. Na gama de velocidade de rotação entre 0 e ralenti (em conformidade com o ponto 7.1), o binário a plena carga disponível a partir do MCI é igual apenas ao binário a plena carga do MCI em ralenti devido à modelização do comportamento da embraiagem durante o arranque do veículo.

Se essa limitação for declarada, os valores para o binário adicional devem ser declarados pelo menos a uma velocidade de rotação de 0 e à velocidade máxima de rotação da curva do MCI a plena carga. Qualquer número arbitrário de valores pode ser declarado na gama entre zero e a velocidade máxima de rotação da curva do MCI a plena carga. Não são permitidos valores declarados inferiores a zero para o binário adicional.

O fabricante do veículo pode declarar limitações que correspondam exatamente à curva do MCI a plena carga, declarando valores de 0 Nm para o binário adicional.

**10.3 Função “para/arranca” do motor para VHE**

Se o veículo estiver equipado com uma função “para/arranca” do motor em conformidade com o ponto 8.1.1, tendo em conta as condições-limite determinadas no ponto 8.4, o parâmetro de entrada P271 nos termos do quadro 6 deve ser definido como verdadeiro.

**11. Transferência dos resultados da ferramenta de simulação para outros veículos**

<table> <tbody> <tr> <td></td> <td>11.1.</td> <td>Os resultados da ferramenta de simulação podem ser transferidos para outros veículos, conforme previsto no artigo 9.º, n.º 6, desde que estejam preenchidas todas as seguintes condições: <table> <tbody> <tr> <td>(a)</td> <td>Os dados e informações de entrada são totalmente idênticos, com exceção do NIV (P238) e da data (P239). No caso de simulações para autocarros pesados primários, as informações e os dados de entrada adicionais relevantes para o veículo intermédio e disponíveis já na fase inicial podem diferir, mas devem ser tomadas medidas especiais neste caso;</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(b)</td> <td>A versão da ferramenta de simulação é idêntica.</td> </tr> </tbody> </table></td> </tr> </tbody> </table>

<table> <tbody> <tr> <td></td> <td>11.2.</td> <td>Para a transferência de resultados, devem ser considerados os seguintes ficheiros de resultados: <table> <tbody> <tr> <td>(a)</td> <td>Camiões médios e pesados: ficheiro de registos do fabricante e ficheiro de informações ao cliente;</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(b)</td> <td>Autocarros pesados primários: ficheiro de registos do fabricante e ficheiro de informações ao cliente;</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(c)</td> <td>Autocarros pesados completos ou completados: ficheiro de registos do fabricante, ficheiro de informações ao cliente e ficheiro de informações do veículo.</td> </tr> </tbody> </table></td> </tr> </tbody> </table>

<table> <tbody> <tr> <td></td> <td>11.3.</td> <td>Para efetuar a transferência de resultados, os ficheiros mencionados no ponto 10.2 devem ser alterados, substituindo os elementos de dados indicados nos subpontos seguintes por informações atualizadas. Só são permitidas alterações de elementos de dados relacionados com a fase atual de acabamento. 11.3.1 Ficheiro de registos do fabricante <table> <tbody> <tr> <td>(a)</td> <td>NIV (anexo IV, parte I, ponto 1.1.3)</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(b)</td> <td>Data de criação do ficheiro de saída (anexo IV, parte I, ponto 3.2)</td> </tr> </tbody> </table> 11.3.2 Ficheiro de informações ao cliente <table> <tbody> <tr> <td>(a)</td> <td>NIV (anexo IV, parte II, ponto 1.1.1)</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(b)</td> <td>Data de criação do ficheiro de saída (anexo IV, parte II, ponto 3.2)</td> </tr> </tbody> </table> 11.3.3. Ficheiro de informações do veículo <table> <tbody> <tr> <td></td> <td>11.3.3.1.</td> <td>No caso de um autocarro pesado primário: <table> <tbody> <tr> <td>(a)</td> <td>NIV (anexo IV, parte III, ponto 1.1)</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(b)</td> <td>Data de criação do ficheiro de saída (anexo IV, parte III, ponto 1.3.2)</td> </tr> </tbody> </table></td> </tr> </tbody> </table> <table> <tbody> <tr> <td></td> <td>11.3.3.2.</td> <td>Se um fabricante de um autocarro pesado primário fornecer dados que vão além dos requisitos para o veículo primário e que diferem entre o veículo original e o veículo transferido, os elementos de dados correspondentes no ficheiro de informações do veículo devem ser atualizados em conformidade.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td></td> <td>11.3.3.3.</td> <td>No caso de um autocarro pesado completo ou completado: <table> <tbody> <tr> <td>(a)</td> <td>NIV (anexo IV, parte III, ponto 2.1)</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(b)</td> <td>Data de criação do ficheiro de saída (anexo IV, parte III, ponto 2.2.2)</td> </tr> </tbody> </table></td> </tr> </tbody> </table> 11.3.4 Após as alterações acima descritas, os elementos de assinatura a seguir indicados devem ser atualizados. <table> <tbody> <tr> <td></td> <td>11.3.4.1.</td> <td>Camiões: <table> <tbody> <tr> <td>(a)</td> <td>Ficheiro de registos do fabricante: Anexo IV, parte I, pontos 3.6 e 3.7</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(b)</td> <td>Ficheiro de informações ao cliente: Anexo IV, parte II, pontos 3.3 e 3.4</td> </tr> </tbody> </table></td> </tr> </tbody> </table> <table> <tbody> <tr> <td></td> <td>11.3.4.2.</td> <td>Autocarros pesados primários: <table> <tbody> <tr> <td>(a)</td> <td>Ficheiro de registos do fabricante: Anexo IV, parte I, pontos 3.3 e 3.4</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(b)</td> <td>Ficheiro de informações do veículo: Anexo IV, parte III, pontos 1.4.1 e 1.4.2</td> </tr> </tbody> </table></td> </tr> </tbody> </table> <table> <tbody> <tr> <td></td> <td>11.3.4.3.</td> <td>Autocarros pesados primários, se tiverem sido fornecidos dados adicionais para o veículo intermédio: <table> <tbody> <tr> <td>(a)</td> <td>Ficheiro de registos do fabricante: Anexo IV, parte I, pontos 3.3 e 3.4</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(b)</td> <td>Ficheiro de informações do veículo: Anexo IV, parte III, pontos 1.4.1, 1.4.2 e 2.3.1</td> </tr> </tbody> </table></td> </tr> </tbody> </table> <table> <tbody> <tr> <td></td> <td>11.3.4.4.</td> <td>Autocarros pesados completos ou completados: <table> <tbody> <tr> <td>(a)</td> <td>Ficheiro de registos do fabricante: Anexo IV, parte I, pontos 3.6 e 3.7</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>(b)</td> <td>Ficheiro de informações do veículo: Anexo IV, parte III, ponto 2.3.1</td> </tr> </tbody> </table></td> </tr> </tbody> </table></td> </tr> </tbody> </table>

|  | 11.4. | Se as emissões de CO2 e o consumo de combustível não puderem ser determinados para o veículo original devido a uma anomalia da ferramenta de simulação, aplicam-se as mesmas medidas aos veículos com resultados transferidos. |
|---|---|---|

|  | 11.5. | Se um fabricante aplicar a abordagem de transferência de resultados para outros veículos conforme estabelecida no presente ponto, o respetivo processo deve ser demonstrado à entidade homologadora no âmbito da concessão da licença do processo. |
|---|---|---|

«Apêndice 1

**Tecnologias de veículos às quais não se aplicam as obrigações estabelecidas no artigo 9.º, n.º 1, primeiro parágrafo, conforme previsto nesse parágrafo**

**Quadro 1**

<table> <tbody> <tr> <td>Categoria tecnológica do veículo</td> <td>Critérios de isenção</td> <td>Valor do parâmetro de entrada em conformidade com o quadro 5 do presente anexo</td> </tr> <tr> <td>Veículos a pilha de combustível</td> <td>Trata-se de um veículo a pilha de combustível ou de um veículo híbrido a pilha de combustível em conformidade com o ponto 2, subpontos 12 ou 13, do presente anexo.</td> <td>“FCV Article 9 exempted”</td> </tr> <tr> <td>MCI a hidrogénio</td> <td>O veículo está equipado com um MCI capaz de funcionar com hidrogénio.</td> <td>“H2 ICE Article 9 exempted”</td> </tr> <tr> <td>Com duplo combustível</td> <td>Veículos com duplo combustível dos tipos 1B, 2B e 3B, tal como definidos no artigo 2.º, pontos 53, 55 e 56, do Regulamento (UE) n.º 582/2011</td> <td>“Dual-fuel vehicle Article 9 exempted”</td> </tr> <tr> <td>VHE</td> <td>Os veículos ficam isentos quando se aplicar, pelo menos, um dos seguintes critérios: <table> <tbody> <tr> <td>—</td> <td>O veículo está equipado com ME múltiplas que não estão colocadas no mesmo ponto de ligação no sistema de tração, em conformidade com o ponto 10.1.2 do presente anexo.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>O veículo está equipado com ME múltiplas que estão colocadas no mesmo ponto de ligação no sistema de tração, em conformidade com o ponto 10.1.2 do presente anexo, mas não têm exatamente as mesmas especificações (ou seja, o mesmo certificado de componente). Este critério não se aplica se o veículo estiver equipado com um IHPC tipo 1.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>O veículo tem uma arquitetura do grupo motopropulsor diferente de P1 a P4, S2 a S4, S-IEPC em conformidade com o ponto 10.1.3 do presente anexo ou com exceção do IHPC tipo 1.</td> </tr> </tbody> </table></td> <td>“HEV Article 9 exempted”</td> </tr> <tr> <td>VEE</td> <td>Os veículos ficam isentos quando se aplicar, pelo menos, um dos seguintes critérios: <table> <tbody> <tr> <td>—</td> <td>O veículo está equipado com ME múltiplas que não estão colocadas no mesmo ponto de ligação no sistema de tração, em conformidade com o ponto 10.1.2 do presente anexo.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>O veículo está equipado com ME múltiplas que estão colocadas no mesmo ponto de ligação no sistema de tração, em conformidade com o ponto 10.1.2 do presente anexo, mas não têm exatamente as mesmas especificações (ou seja, o mesmo certificado de componente). Este critério não se aplica se o veículo estiver equipado com um IEPC.</td> </tr> </tbody> </table> <table> <tbody> <tr> <td>—</td> <td>O veículo tem uma arquitetura do grupo motopropulsor diferente de E2 a E4 ou E-IEPC em conformidade com o ponto 10.1.3 do presente anexo.</td> </tr> </tbody> </table></td> <td>“PEV Article 9 exempted”</td> </tr> <tr> <td>Vários grupos motopropulsores permanentemente independentes mecanicamente</td> <td>O veículo está equipado com mais de um grupo motopropulsor em que cada grupo é propulsor de diferente(s) eixo(s) de rodas do veículo e em que os diferentes grupos motopropulsores não podem, em circunstância alguma, ser ligados mecanicamente. A este respeito, os eixos hidráulicos devem, em conformidade com o ponto 5, alínea a), do presente anexo, ser tratados como eixos não motores e, por conseguinte, não devem ser contados como um grupo motopropulsor independente.</td> <td>“Multiple powertrains Article 9 exempted”</td> </tr> <tr> <td>Carregado em movimento</td> <td>O veículo está equipado com meios de fornecimento condutor ou indutivo de energia elétrica ao veículo em movimento, a qual é, pelo menos em parte, diretamente utilizada para a propulsão do veículo e, opcionalmente, para carregar um SRAEE.</td> <td>“In-motion charging Article 9 exempted”</td> </tr> <tr> <td>Veículos híbridos não elétricos</td> <td>Trata-se de um veículo híbrido, mas não um veículo híbrido elétrico em conformidade com o ponto 2, subpontos 26 e 27, do presente anexo.</td> <td>“HV Article 9 exempted”</td> </tr> </tbody> </table>

| (*) | Regulamento (UE) n.º 1230/2012 da Comissão, de 12 de dezembro de 2012, que dá execução ao Regulamento (CE) n.º 661/2009 do Parlamento Europeu e do Conselho no que respeita aos requisitos de homologação para massas e dimensões dos veículos a motor e seus reboques e altera a Diretiva 2007/46/CE do Parlamento Europeu e do Conselho (JO L 353 de 21.12.2012, p. 31). |
|---|---|

| (**) | Regulamento (UE) 2019/2144 do Parlamento Europeu e do Conselho, de 27 de novembro de 2019, relativo aos requisitos de homologação de veículos a motor e seus reboques e dos sistemas, componentes e unidades técnicas destinados a esses veículos, no que se refere à sua segurança geral e à proteção dos ocupantes dos veículos e dos utentes da estrada vulneráveis, que altera o Regulamento (UE) 2018/858 do Parlamento Europeu e do Conselho e revoga os Regulamentos (CE) n.º 78/2009, (CE) n.º 79/2009 e (CE) n.º 661/2009 do Parlamento Europeu e do Conselho e os Regulamentos (CE) n.º 631/2009, (UE) n.º 406/2010, (UE) n.º 672/2010, (UE) n.º 1003/2010, (UE) n.º 1005/2010, (UE) n.º 1008/2010, (UE) n.º 1009/2010, (UE) n.º 19/2011, (UE) n.º 109/2011, (UE) n.º 458/2011, (UE) n.º 65/2012, (UE) n.º 130/2012, (UE) n.º 347/2012, (UE) n.º 351/2012, (UE) n.º 1230/2012, e (UE) 2015/166 da Comissão (JO L 325 de 16.12.2019, p. 1).. |
|---|---|

»

(1) Se existirem várias tomadas de força (PTO) instaladas na transmissão, apenas deve ser declarado o componente com as perdas mais elevadas de acordo com o anexo IX, ponto 3.6, para a combinação dos critérios “PTOShaftsGearWheels” e “PTOShaftsOtherElements”.

(2) O termo ME aqui utilizado inclui um componente adicional da transmissão (ADC), se existir.

(3)

“Sim” (ou seja, componente do eixo presente) apenas no caso de ambos os parâmetros “DifferentialIncluded” e “DesignTypeWheelMotor” serem definidos como “falsos”

(4) Não aplicável aos tipos de transmissão APT-S e APT-P

(5) Quando o EM está ligado a um veio específico no interior da transmissão (por exemplo, o eixo secundário) em conformidade com a definição estabelecida no quadro 8

(6) Não aplicável aos veículos com tração dianteira.
