---
id: "regulamento-ue-2017-2400-apendice-15-a-anexo-xi"
celex: "32017R2400"
title: "Regulamento (UE) 2017/2400 da Comissão, de 12 de dezembro de 2017, que dá execução ao Regulamento (CE) n.° 595/2009 do Parlamento Europeu e do Conselho no que respeita à determinação das emissões de CO2 e ao consumo de combustível dos veículos pesados e altera a Diretiva 2007/46/CE do Parlamento Europeu e do Conselho e o Regulamento (UE) n.° 582/2011 do Conselho e da Comissão (Texto relevante para efeitos do EEE. ) — Apêndice 15 a Anexo XI"
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
part: "Apêndice 15 a Anexo XI"
---

# Regulamento (UE) 2017/2400 da Comissão, de 12 de dezembro de 2017, que dá execução ao Regulamento (CE) n.° 595/2009 do Parlamento Europeu e do Conselho no que respeita à determinação das emissões de CO2 e ao consumo de combustível dos veículos pesados e altera a Diretiva 2007/46/CE do Parlamento Europeu e do Conselho e o Regulamento (UE) n.° 582/2011 do Conselho e da Comissão (Texto relevante para efeitos do EEE. ) — Apêndice 15 a Anexo XI

## Apêndice 15

**Parâmetros de entrada para a ferramenta de simulação**

**Introdução**

O presente apêndice descreve a lista de parâmetros que devem ser fornecidos pelo fabricante dos componentes como dados de entrada para a ferramenta de simulação. O modelo XML aplicável e vários exemplos de dados estão disponíveis na plataforma de distribuição eletrónica específica.

**Definições**

(1) «ID do parâmetro»: identificador único utilizado na ferramenta de simulação para um determinado parâmetro de entrada ou conjunto de dados de entrada;

(2) «Tipo»: tipo de dados do parâmetro;

| «string»… | sequência de carateres na codificação ISO8859-1; |
|---|---|
| «token»… | sequência de carateres na codificação ISO8859-1, sem espaços em branco à frente e atrás; |
| «date»… | data e hora TUC com o seguinte formato: AAAA-MM-DDTHH:MM:SSZ com carateres em itálico representando carateres fixos, p. ex., «2002-05-30T09:30:10Z»; |
| «integer»… | valor com um tipo de dados inteiro, sem zeros à frente, p. ex., «1800»; |
| «double, X»… | número fracionário contendo exatamente X dígitos a seguir ao sinal decimal («.») e sem zeros à frente, p. ex., «double, 2»: «2345,67»; para «double, 4»: «45,6780»; |

(3) «Unidade» … unidade física do parâmetro.

**Conjunto de parâmetros de entrada para o sistema de máquina elétrica**

**Quadro 1**

**Parâmetros de entrada «Electric machine system/General» (sistema de máquina elétrica/generalidades)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| Manufacturer | P450 | token | [-] |  |
| Model | P451 | token | [-] |  |
| CertificationNumber | P452 | token | [-] |  |
| Date | P453 | dateTime | [-] | Data e hora de criação do valor da dispersão do componente |
| AppVersion | P454 | token | [-] | Entrada específica do fabricante relativamente às ferramentas utilizadas para a avaliação e o tratamento dos dados dos componentes medidos |
| ElectricMachineType | P455 | string | [-] | Determinado de acordo com o ponto 2, subponto 21, do presente anexo. <br> Valores admitidos: «ASM», «ESM», «PSM», «RM» |
| CertificationMethod | P456 | string | [-] | Valores admitidos: «Measured», «Standard values» |
| R85RatedPower | P457 | integer | [W] | Determinado em conformidade com o anexo 2, ponto 1.9, do Regulamento n.º 85 da ONU, Rev. 1. |
| RotationalInertia | P458 | double, 2 | [kgm2] | Determinado de acordo com o apêndice 8, ponto 8, do presente anexo. |
| DcDcConverterIncluded | P465 | boolean | [-] | Definir como «true» (verdadeiro) se o conversor CC/CC fizer parte do sistema de máquina elétrica em conformidade com o ponto 4.1 do presente anexo. Se o parâmetro «CertificationMethod» for «Standard values», o parâmetro deve ser sempre definido como «true» |
| IHPCType | P466 | string | [-] | Valores admitidos: «None», «IHPC Type 1» |

**Quadro 2**

**Parâmetros de entrada «Electric machine system/VoltageLevels» (sistema de máquina elétrica/níveis de tensão) para cada nível de tensão medido**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| VoltageLevel | P467 | integer | [V] | Se o parâmetro «CertificationMethod» (método de certificação) for «Standard values» (valores normalizados), não é necessário fornecer dados. |
| ContinuousTorque | P459 | double, 2 | [Nm] |  |
| TestSpeedContinuousTorque | P460 | double, 2 | [1/min] |  |
| OverloadTorque | P461 | double, 2 | [Nm] |  |
| TestSpeedOverloadTorque | P462 | double, 2 | [1/min] |  |
| OverloadDuration | P463 | double, 2 | [s] |  |

**Quadro 3**

**Parâmetros de entrada «Electric machine system/MaxMinTorque» (sistema de máquina elétrica/binário máx. mín.) para cada ponto de funcionamento e cada nível de tensão medido**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| OutputShaftSpeed | P468 | double, 2 | [1/min] |  |
| MaxTorque | P469 | double, 2 | [Nm] |  |
| MinTorque | P470 | double, 2 | [Nm] |  |

**Quadro 4**

**Parâmetros de entrada «Electric machine system/DragTorque» (sistema de máquina elétrica/binário resistente) para cada ponto de funcionamento**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| OutputShaftSpeed | P471 | double, 2 | [1/min] |  |
| DragTorque | P472 | double, 2 | [Nm] |  |

**Quadro 5**

**Parâmetros de entrada «Electric machine system/ElectricPowerMap» para cada ponto de funcionamento e para cada nível de tensão medido.**

**No caso de um IHPC tipo 1 (em conformidade com a definição constante do ponto 2, subponto 42, do presente anexo), para cada ponto de funcionamento, para cada nível de tensão medido e para cada velocidade de marcha avante.**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| OutputShaftSpeed | P473 | double, 2 | [1/min] |  |
| Binário | P474 | double, 2 | [Nm] |  |
| ElectricPower | P475 | double, 2 | [W] |  |

**Quadro 6**

**Parâmetros de entrada «Electric machine system/Conditioning» (sistema de máquina elétrica/condicionamento) para cada circuito de arrefecimento com ligação a um permutador de calor externo**

**Se o parâmetro «CertificationMethod» (método de certificação) for «Standard values» (valores normalizados), não é necessário fornecer dados.**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| CoolantTempInlet | P476 | integer | [°C] | Determinado em conformidade com os pontos 4.1.5.1 e 4.3.6 do presente anexo. <br> A entrada deve ser especificada como valor médio em ambos os níveis de tensão. |
| CoolingPower | P477 | integer | [W] | Determinado em conformidade com os pontos 4.1.5.1 e 4.3.6 do presente anexo. <br> A entrada deve ser especificada como valor médio em ambos os níveis de tensão. |

**Conjunto de parâmetros de entrada para IEPC**

**Quadro 1**

**Parâmetros de entrada «IEPC/General» (IEPC/generalidades)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| Manufacturer | P478 | token | [-] |  |
| Model | P479 | token | [-] |  |
| CertificationNumber | P480 | token | [-] |  |
| Date | P481 | dateTime | [-] | Data e hora de criação do valor da dispersão do componente |
| AppVersion | P482 | token | [-] | Entrada específica do fabricante relativamente às ferramentas utilizadas para a avaliação e o tratamento dos dados dos componentes medidos |
| ElectricMachineType | P483 | string | [-] | Determinado de acordo com o ponto 2, subponto 21, do presente anexo. <br> Valores admitidos: «ASM», «ESM», «PSM», «RM» |
| CertificationMethod | P484 | string | [-] | Valores admitidos: «Measured for complete component», <br> «Measured for EM and standard values for other components», «Standard values for all components» |
| R85RatedPower | P485 | integer | [W] | Determinado em conformidade com o anexo 2, ponto 1.9, do Regulamento n.º 85 da ONU. |
| RotationalInertia | P486 | double, 2 | [kgm2] | Determinado de acordo com o apêndice 8, ponto 8, do presente anexo. |
| DifferentialIncluded | P493 | boolean | [-] | Definir como «true» (verdadeiro) no caso de um diferencial fazer parte do IEPC |
| DesignTypeWheelMotor | P494 | boolean | [-] | Definir como «true» no caso de um motor de roda com tipo de conceção IEPC |
| NrOf DesignTypeWheelMotorMeasured | P495 | integer | [-] | Entrada relevante apenas no caso de um motor de roda com tipo de conceção IEPC, em conformidade com o ponto 4.1.1.2 do presente anexo. <br> Valores admitidos: «1», «2» |
| DisengagementClutch | P565 | boolean | [-] | Se o IEPC estiver equipado com uma funcionalidade que, de forma ativa, em determinadas condições de funcionamento, permita desligar mecanicamente todas as ME no interior do componente do resto do grupo motopropulsor do veículo em direção às rodas, esta entrada deve ser definida como «true». <br> A localização exata da desconexão pode também ser a jusante dos veios de saída das ME e incluir o desengate de algumas das partes de engrenagem do IEPC. |

**Quadro 2**

**Parâmetros de entrada «IEPC/Gears» (IEPC/velocidades) para cada velocidade de marcha avante**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| GearNumber | P496 | integer | [-] |  |
| Ratio | P497 | double, 3 | [-] | Relação entre a velocidade do rotor da máquina elétrica e a velocidade do veio de saída IEPC |
| MaxOutputShaftTorque | P498 | integer | [Nm] | Facultativo. <br> No caso de um motor de roda com tipo de conceção IEPC, o valor declarado para o binário máximo no veio de saída do componente deve corresponder à configuração medida em conformidade com o ponto 4.1.1.2 do presente anexo (ou seja, se dois desses componentes tiverem sido medidos, o valor declarado deve ser duas vezes mais elevado do que se fosse medido um único componente). |
| MaxOutputShaftSpeed | P499 | integer | [1/min] | Facultativo |

**Quadro 3**

**Parâmetros de entrada «IEPC/VoltageLevels» (IEPC/níveis de tensão) para cada nível de tensão medido**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| VoltageLevel | P500 | integer | [V] | Se o parâmetro «CertificationMethod» (método de certificação) for «Standard values for all components» (valores normalizados para todos os componentes), não é necessário fornecer dados. |
| ContinuousTorque | P487 | double, 2 | [Nm] |  |
| TestSpeedContinuousTorque | P488 | double, 2 | [1/min] |  |
| OverloadTorque | P489 | double, 2 | [Nm] |  |
| TestSpeedOverloadTorque | P490 | double, 2 | [1/min] |  |
| OverloadDuration | P491 | double, 2 | [s] |  |

**Quadro 4**

**Parâmetros de entrada «IEPC/MaxMinTorque» para cada ponto de funcionamento, cada nível de tensão medido e cada velocidade de marcha avante medida (medição facultativa dependente da velocidade em conformidade com o ponto 4.2.2, alínea c), do presente anexo)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| OutputShaftSpeed | P501 | double, 2 | [1/min] |  |
| MaxTorque | P502 | double, 2 | [Nm] |  |
| MinTorque | P503 | double, 2 | [Nm] |  |

**Quadro 5**

**Parâmetros de entrada «IEPC/DragTorque» (IEPC/binário resistente) para cada ponto de funcionamento e cada velocidade de marcha avante medida (medição facultativa dependente da velocidade em conformidade com o ponto 4.2.3)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| OutputShaftSpeed | P504 | double, 2 | [1/min] |  |
| DragTorque | P505 | double, 2 | [Nm] |  |

**Quadro 6**

**Parâmetros de entrada «IEPC/ElectricPowerMap» (IEPC/mapa de potência elétrica) para cada ponto de funcionamento, cada nível de tensão medido e cada velocidade de marcha avante**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| OutputShaftSpeed | P506 | double, 2 | [1/min] |  |
| Torque | P507 | double, 2 | [Nm] |  |
| ElectricPower | P508 | double, 2 | [W] |  |

**Quadro 7**

**Parâmetros de entrada «IEPC/Conditioning»(IEPC/condicionamento) para cada circuito de arrefecimento com ligação a um permutador de calor externo**

**Se o parâmetro «CertificationMethod» (método de certificação) for «Standard values for all components» (valores normalizados para todos os componentes), não é necessário fornecer dados.**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| CoolantTempInlet | P509 | integer | [°C] | Determinado em conformidade com os pontos 4.1.5.1 e 4.3.6 do presente anexo. <br> A entrada deve ser especificada como valor médio em ambos os níveis de tensão. |
| CoolingPower | P510 | integer | [W] | Determinado em conformidade com os pontos 4.1.5.1 e 4.3.6 do presente anexo. <br> A entrada deve ser especificada como valor médio em ambos os níveis de tensão. |

**Conjunto de parâmetros de entrada para o sistema de máquina elétrica**

**Quadro 1**

**Parâmetros de entrada «Battery system/General» (sistema de bateria/generalidades)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| Manufacturer | P511 | token | [-] |  |
| Model | P512 | token | [-] |  |
| CertificationNumber | P513 | token | [-] |  |
| Date | P514 | dateTime | [-] | Data e hora de criação do valor da dispersão do componente |
| AppVersion | P515 | token | [-] | Entrada específica do fabricante relativamente às ferramentas utilizadas para a avaliação e o tratamento dos dados dos componentes medidos |
| CertificationMethod | P517 | string | [-] | Valores admitidos: «Measured», «Standard values» |
| BatteryType | P518 | string | [-] | Valores admitidos: «HPBS», «HEBS» |
| RatedCapacity | P519 | double, 2 | [Ah] | Se o parâmetro «CertificationMethod» for «Standard values», esses valores devem ser determinados em conformidade com o ponto 1, alínea b), do apêndice 10 |
| ConnectorsSubsystemsIncluded | P520 | boolean | [-] | Relevante apenas se o subsistema representativo de bateria for ensaiado: definir como «true» (verdadeiro) se o chicote de fios representativo para ligar subsistemas de bateria tiver sido incluído no ensaio. Definir sempre como «true» se o sistema completo de baterias tiver sido ensaiado. |
| JunctionboxIncluded | P516 | boolean | [-] | Relevante apenas se o subsistema representativo de bateria for ensaiado: Definir como «true» se tiver sido incluída no ensaio uma caixa de junção representativa com dispositivo de corte e fusíveis. Definir sempre como «true» se o sistema completo de baterias tiver sido ensaiado. |
| TestingTemperature | P521 | integer | [°C] | Determinado em conformidade com o pontos 5.1.4 do presente anexo. <br> Se o parâmetro «CertificationMethod» (método de certificação) for «Standard values» (valores normalizados), não é necessário fornecer dados. |

**Quadro 2**

**Parâmetros de entrada «Battery system/OCV» (sistema de bateria/TCA) para cada nível de estado de carga medido**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| SOC | P522 | integer | [%] |  |
| OCV | P523 | double, 2 | [V] |  |

**Quadro 3**

**Parâmetros de entrada «Battery system/DCIR» (sistema de bateria/RICC) para cada nível de estado de carga medido**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| SOC | P524 | integer | [%] | Se o parâmetro «CertificationMethod» (método de certificação) for «Standard values» (valores normalizados), devem ser fornecidos os mesmos valores de RICC para dois valores de estado de carga diferentes, 0 % e 100 %. |
| DCIR RI2 | P525 | double, 2 | [mOhm] | Se o parâmetro «CertificationMethod» for «Standard values», deve ser fornecido o valor de RICC determinado em conformidade com o ponto 1, alínea d) do apêndice 10. |
| DCIR RI10 | P526 | double, 2 | [mOhm] | Se o parâmetro «CertificationMethod» for «Standard values», deve ser fornecido o valor de RICC determinado em conformidade com o ponto 1, alínea d) do apêndice 10. |
| DCIR RI20 | P527 | double, 2 | [mOhm] | Se o parâmetro «CertificationMethod» for «Standard values», deve ser fornecido o valor de RICC determinado em conformidade com o ponto 1, alínea d) do apêndice 10. |
| DCIR RI120 | P528 | double, 2 | [mOhm] | Facultativo, apenas exigido para as baterias do tipo HEBS. <br> Se o parâmetro «CertificationMethod» for «Standard values», deve ser fornecido o valor de RICC determinado em conformidade com o ponto 1, alínea d) do apêndice 10. |

**Quadro 4**

**Parâmetros de entrada «Battery system/Current limits» (sistema de bateria/limites de corrente) para cada nível de estado de carga medido**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| SOC | P529 | integer | [%] | — |
| MaxChargingCurrent | P530 | double, 2 | [A] | Se o parâmetro «CertificationMethod» for «Standard values», esses valores devem ser determinados em conformidade com o ponto 1, alínea e), do apêndice 10 e todos os valores devem ter um sinal prévio positivo. |
| MaxDischargingCurrent | P531 | double, 2 | [A] | Se o parâmetro «CertificationMethod» for «Standard values», esses valores devem ser determinados em conformidade com o ponto 1, alínea e), do apêndice 10 e todos os valores devem ter um sinal prévio positivo. |

**Conjunto de parâmetros de entrada para o sistema de condensador**

**Quadro 1**

**Parâmetros de entrada «Capacitor system/General» (sistema de condensador/generalidades)**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| Manufacturer | P532 | token | [-] |  |
| Model | P533 | token | [-] |  |
| CertificationNumber | P534 | token | [-] |  |
| Date | P535 | dateTime | [-] | Data e hora de criação do valor da dispersão do componente |
| AppVersion | P536 | token | [-] | Entrada específica do fabricante relativamente às ferramentas utilizadas para a avaliação e o tratamento dos dados dos componentes medidos |
| CertificationMethod | P538 | string | [-] | Valores admitidos: «Measured», «Standard values». |
| Capacidade elétrica | P539 | double, 2 | [F] |  |
| InternalResistance | P540 | double, 2 | [Ohm] <br> [mOhm] |  |
| MinVoltage | P541 | double, 2 | [V] |  |
| MaxVoltage | P542 | double, 2 | [V] |  |
| MaxChargingCurrent | P543 | double, 2 | [A] |  |
| MaxDischargingCurrent | P544 | double, 2 | [A] |  |
| TestingTemperature | P537 | integer | [°C] | Determinado em conformidade com o pontos 6.1.3 do presente anexo. <br> Se o parâmetro «CertificationMethod» (método de certificação) for «Standard values» (valores normalizados), não é necessário fornecer dados. |

**Conjunto de parâmetros de entrada para o sistema de pilha de combustível**

**Quadro 1**

**Parâmetros de entrada «Fuel cell system/General»**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| Manufacturer | P566 | token | - |  |
| Model | P567 | token | - |  |
| CertificationNumber | P568 | token | - |  |
| Date | P569 | dateTime | - | Data e hora de criação do valor da dispersão do componente |
| AppVersion | P570 | token | - | Entrada específica do fabricante relativamente às ferramentas utilizadas para a avaliação e o tratamento dos dados dos componentes medidos |
| CertificationMethod | P571 | string | - | Valores admitidos: «Measured», «Standard values» |
| FCSRatedPower | P572 | integer | kW | Determinado em conformidade com o apêndice 1, ponto 4.6, do anexo 6 do Regulamento n.º 100 da ONU. |

**Quadro 2**

**Parâmetros de entrada «Fuel cell system/FuelMap» para cada ponto de funcionamento medido**

| Nome do parâmetro | ID do parâmetro | Tipo | Unidade | Descrição/referência |
|---|---|---|---|---|
| OutputPower | P573 | double, 2 | kW | Potência elétrica fornecida pelo FCS determinada em conformidade com o ponto 7.5.3 |
| FuelConsumption | P574 | double, 2 | g/h | Caudal mássico do combustível determinado em conformidade com o ponto 7.5.3 |

(*) Determinado em conformidade com os pontos 4.3.5 e 4.3.6 do presente anexo.

(**) Determinado em conformidade com o ponto 5.4.1.4 do presente anexo.

(***) Regulamento n.º 100 da Comissão Económica das Nações Unidas para a Europa (UNECE) — Prescrições uniformes relativas à homologação de veículos no que diz respeito a requisitos específicos relativos ao grupo motopropulsor elétrico (JO L 449 de 15.12.2021, p. 1).

## Anexo XI

**ALTERAÇÕES À DIRETIVA 2007/46/CE**

1) No anexo I, é inserido o seguinte ponto 3.5.7:

| «3.5.7 | Certificação das emissões de CO2 e do consumo de combustível (para veículos pesados, conforme especificado no artigo 6.º do Regulamento (UE) 2017/2400 da Comissão). |
|---|---|

| 3.5.7.1 | Número de licença da ferramenta de simulação:» |
|---|---|

2) Ao anexo III, na parte I, A (categorias M e N), são aditados os pontos 3.5.7. e 3.5.7.1, com a seguinte redação:

| «3.5.7 | Certificação das emissões de CO2 e do consumo de combustível (para veículos pesados, conforme especificado no artigo 6.º do Regulamento (UE) 2017/2400 da Comissão). |
|---|---|

| 3.5.7.1 | Número de licença da ferramenta de simulação:» |
|---|---|

3) No anexo IV, a parte I é alterada do seguinte modo:

a) a linha 41A passa a ter a seguinte redação:

| «41A | Emissões (Euro VI) de veículos pesados/acesso à informação | Regulamento (CE) n.º 595/2009 <br> Regulamento (UE) n.º 582/2011 | X (9) | X (9) | X | X (9) | X (9) | X» |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

b) é aditada a seguinte entrada 41B:

| «41B | Licença da ferramenta de simulação de CO2 (veículos pesados) | Regulamento (CE) n.º 595/2009 <br> Regulamento (UE) 2017/2400 |  |  |  |  | X (16) | X» |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

c) é aditada a seguinte nota explicativa 16:

«(16) Para os veículos com uma massa máxima em carga tecnicamente admissível superior a 7 500 kg.»

4) O anexo IX é alterado do seguinte modo:

a) À parte I, Modelo B, LADO 2, VEÍCULO DA CATEGORIA N2, é aditado o ponto 49, com a seguinte redação:

«49 ««Valor da dispersão» criptográfico do ficheiro de registo do fabricante …»»

b) À parte I, Modelo B, LADO 2, VEÍCULO DA CATEGORIA N3, é aditado o ponto 49, com a seguinte redação:

«49 ««Valor da dispersão» criptográfico do ficheiro de registo do fabricante …»»

5) No anexo XV, no ponto 2, é inserida a seguinte linha:

| «46B | Determinação da resistência ao rolamento | Regulamento (UE) 2017/2400 [Serviço das Publicações, inserir o número de publicação do presente regulamento], anexo X» |
|---|---|---|

(

1

) Regulamento (UE) 2018/858 do Parlamento Europeu e do Conselho, de 30 de maio de 2018, relativo à homologação e à fiscalização do mercado dos veículos a motor e seus reboques, e dos sistemas, componentes e unidades técnicas destinados a esses veículos, que altera os Regulamentos (CE) n.º 715/2007 e (CE) n.º 595/2009 e revoga a Diretiva 2007/46/CE (JO L 151 de 14.6.2018, p. 1).

(

2

) Regulamento (UE) 2017/2400 da Comissão, de 12 de dezembro de 2017, que dá execução ao Regulamento (CE) n.º 595/2009 do Parlamento Europeu e do Conselho no que respeita à determinação das emissões de CO2 e do consumo de combustível dos veículos pesados e altera a Diretiva 2007/46/CE do Parlamento Europeu e do Conselho e o Regulamento (UE) n.º 582/2011 da Comissão (JO L 349 de 29.12.2017, p. 1).»;

(

3

) Regulamento n.º 107 da Comissão Económica das Nações Unidas para a Europa (UNECE) — Disposições uniformes relativas à homologação de veículos das categorias M2 ou M3 no que respeita às suas características gerais de construção (JO L 52 de 23.2.2018, p. 1).

(

4

) Regulamento de Execução (UE) 2020/683 da Comissão, de 15 de abril de 2020, que executa o Regulamento (UE) 2018/858 do Parlamento Europeu e do Conselho no que diz respeito aos requisitos administrativos para a homologação e a fiscalização do mercado dos veículos a motor e seus reboques e dos sistemas, componentes e unidades técnicas destinados a esses veículos (JO L 163 de 26.5.2020, p. 1).

(

5

) Informações e dados de entrada, tal como definidos no anexo III para os veículos primários.

(

6

) Os resultados das emissões de CO2 e do consumo de combustível não precisam de ser apresentados através do FIV, uma vez que estas informações podem ser calculadas a partir dos resultados relativos ao consumo de energia e ao tipo de combustível conhecido.

(

7

) O conteúdo do FIV é especificado em pormenor no anexo IV, parte III.

(

8

) Informações e dados de entrada, tal como definidos no anexo III para veículos completos e completados.

(

9

)

«i» representa o número de fases de fabrico envolvidas no processo até à data.

(

10

) Ver anexo IV, parte III, ponto 1.1.

(

11

)

JO L 349 de 29.12.2017, p. 1

(

12

) Regulamento n.º 49 da Comissão Económica das Nações Unidas para a Europa (UNECE) — Prescrições uniformes no que diz respeito às medidas a tomar contra a emissão de gases e de partículas poluentes provenientes dos motores de ignição por compressão e de ignição comandada utilizados em veículos (JO L 171 de 24.6.2013, p. 1).

(

13

) Para motores com duplo combustível, indicar valores para cada tipo de combustível e cada modo de funcionamento separadamente.

(

14

) Especificar a tolerância; devem ter uma aproximação de ± 3 % em relação aos valores declarados pelo fabricante.

(

15

) Regulamento n.º 85 da Comissão Económica das Nações Unidas para a Europa (UNECE) — Prescrições uniformes relativas à homologação de motores de combustão interna ou de unidades de tração elétricas destinadas à propulsão dos veículos a motor das categorias «M» e «N» no que diz respeito à medição da potência útil e da potência máxima de 30 minutos de unidades de tração elétricas (JO L 323 de 7.11.2014, p. 52)

(

16

) Riscar o que não interessa (há casos em que nada precisa de ser suprimido, quando for aplicável mais de uma entrada)

(

17

) Regulamento n.º 54 da Comissão Económica das Nações Unidas para a Europa (UNECE) — Disposições uniformes relativas à homologação dos pneus para veículos comerciais e seus reboques (JO L 183 de 11.7.2008, p. 41).

(

\*1

) Regulamento n.º 107 da Comissão Económica das Nações Unidas para a Europa (UNECE) — Disposições uniformes relativas à homologação de veículos das categorias M2 ou M3 no que respeita às suas características gerais de construção (JO L 52 de 23.2.2018, p. 1).

(

\*2

) Regulamento n.º 48 da Comissão Económica das Nações Unidas para a Europa (UNECE) — Prescrições uniformes relativas à homologação de veículos no que diz respeito à instalação de dispositivos de iluminação e sinalização luminosa (JO L 14 de 16.1.2019, p. 42).

(

\*3

) Regulamento n.º 122 da Comissão Económica das Nações Unidas para a Europa (UNECE) — Prescrições uniformes respeitantes à homologação dos veículos das categorias M, N e O no que diz respeito aos seus sistemas de aquecimento (JO L 19 de 24.1.2020, p. 42).

(

18

) Regulamento n.º 54 da Comissão Económica das Nações Unidas para a Europa (UNECE) — Disposições uniformes relativas à homologação dos pneus para veículos comerciais e seus reboques (JO L 183 de 11.7.2008, p. 41).

(

19

) Regulamento n.º 117 da Comissão Económica das Nações Unidas para a Europa (UNECE) — Prescrições uniformes relativas à homologação de pneus no que diz respeito ao ruído de rolamento e à aderência em pavimento molhado e/ou à resistência ao rolamento [2016/1350] (JO L 218 de 12.8.2016, p. 1).

(

20

) Regulamento (UE) 2020/740 do Parlamento Europeu e do Conselho, de 25 de maio de 2020, relativo à rotulagem dos pneus no que respeita à eficiência energética e a outros parâmetros, que altera o Regulamento (UE) 2017/1369 e revoga o Regulamento (CE) n.º 1222/2009 (JO L 177 de 5.6.2020, p. 1).;

(

21

) Regulamento (CE) n.º 661/2009 do Parlamento Europeu e do Conselho, de 13 de julho de 2009, relativo às prescrições para homologação no que se refere à segurança geral dos veículos a motor, seus reboques e sistemas, componentes e unidades técnicas a eles destinados (JO L 200 de 31.7.2009, p. 1).

(

22

) Regulamento (UE) 2019/2144 do Parlamento Europeu e do Conselho, de 27 de novembro de 2019, relativo aos requisitos de homologação de veículos a motor e seus reboques e dos sistemas, componentes e unidades técnicas destinados a esses veículos, no que se refere à sua segurança geral e à proteção dos ocupantes dos veículos e dos utentes da estrada vulneráveis, que altera o Regulamento (UE) 2018/858 do Parlamento Europeu e do Conselho (JO L 325 de 16.12.2019, p. 1).

(

23

) Regulamento n.º 30 da Comissão Económica das Nações Unidas para a Europa (UNECE) — Disposições uniformes relativas à homologação dos pneus para veículos a motor e seus reboques (JO L 201 de 30.7.2008, p. 70).

(

24

) Para autocarros pesados, apenas o fabricante do veículo primário

(

25

) Determinada em conformidade com os pontos 4.3.5 e 4.3.6 do presente anexo.
