---
id: "regulamento-ue-2017-2400-apendice-1"
celex: "32017R2400"
title: "Regulamento (UE) 2017/2400 da Comissão, de 12 de dezembro de 2017, que dá execução ao Regulamento (CE) n.° 595/2009 do Parlamento Europeu e do Conselho no que respeita à determinação das emissões de CO2 e ao consumo de combustível dos veículos pesados e altera a Diretiva 2007/46/CE do Parlamento Europeu e do Conselho e o Regulamento (UE) n.° 582/2011 do Conselho e da Comissão (Texto relevante para efeitos do EEE. ) — Apêndice 1"
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
part: "Apêndice 1"
---

# Regulamento (UE) 2017/2400 da Comissão, de 12 de dezembro de 2017, que dá execução ao Regulamento (CE) n.° 595/2009 do Parlamento Europeu e do Conselho no que respeita à determinação das emissões de CO2 e ao consumo de combustível dos veículos pesados e altera a Diretiva 2007/46/CE do Parlamento Europeu e do Conselho e o Regulamento (UE) n.° 582/2011 do Conselho e da Comissão (Texto relevante para efeitos do EEE. ) — Apêndice 1

## Apêndice 1 — Principais etapas e equações de avaliação realizadas pela ferramenta numa simulação de procedimento de ensaio de verificação

O presente apêndice descreve as principais etapas da avaliação e as equações básicas subjacentes que são aplicadas pela ferramenta de simulação num procedimento de ensaio de verificação.

**PARTE A: Determinação do fator CVTP**

Para determinar o fator CVTPdescrito no ponto 7.2.2, aplicam-se os seguintes procedimentos de cálculo:

1. Cálculo da potência de roda

Os dados do binário lidos a partir dos dados de medição tratados em conformidade com o quadro 4 são corrigidos em função da deriva do medidor de binário do seguinte modo:

image

em que:

| i | \= | índice para a roda direita e esquerda do eixo motor |
|---|---|---|

| Tcorr | \= | sinal do binário corrigido com a deriva [Nm] |
|---|---|---|

| T | \= | sinal do binário antes da correção com a deriva [Nm] |
|---|---|---|

| Tdrift | \= | deriva do medidor de binário registada durante a verificação da deriva no final do ensaio de verificação [Nm] |
|---|---|---|

| t | \= | nó temporal [s] |
|---|---|---|

| tstart | \= | primeira marca temporal nos dados de medição tratados em conformidade com o quadro 4 [s] |
|---|---|---|

| tend | \= | última marca temporal nos dados de medição tratados em conformidade com o quadro 4 [s] |
|---|---|---|

A potência de roda é calculada a partir do binário da roda e da velocidade de rotação da roda corrigidos, do seguinte modo:

image

em que:

| i | \= | índice para a roda direita e esquerda do eixo motor |
|---|---|---|

| t | \= | nó temporal [s] |
|---|---|---|

| Pwheel | \= | potência de roda [kW] |
|---|---|---|

| nwheel | \= | velocidade de rotação da roda [rpm] |
|---|---|---|

| Tcorr | \= | sinal do binário corrigido com a deriva [Nm] |
|---|---|---|

A potência total de roda é então calculada como a soma da potência das rodas esquerda e direita:

image

2. Determinação do consumo de combustível medido específico da travagem (FCm-c)

O resultado relativo ao «consumo de combustível específico da travagem medido e corrigido em função de uma fase de rodagem» (BSFCm-c), conforme aplicado no 7.2.2, é calculado pela ferramenta de simulação do modo a seguir descrito.

Numa primeira etapa, o valor bruto do consumo de combustível medido específico da travagem para o ensaio de verificação BSFCm é calculado do seguinte modo:

image

em que:

| BSFCm | \= | valor bruto do consumo de combustível medido específico da travagem no ensaio de verificação [g/kWh] |
|---|---|---|

| FCm (t) | \= | caudal mássico instantâneo do combustível medido durante o ensaio de verificação [g/s] |
|---|---|---|

| Δt | \= | duração do incremento de tempo = 0,5 [s] |
|---|---|---|

| Wwheel,pos,m | \= | trabalho positivo das rodas medido no ensaio de verificação [kWh] |
|---|---|---|

image

Numa segunda etapa, o BSFCm é corrigido em função do poder calorífico inferior (NCV) do combustível utilizado no ensaio de verificação, resultando no BSFCm,corr:

image

em que:

| BSFCm,corr | \= | valor do consumo de combustível específico da travagem medido no ensaio de verificação e corrigido em função da influência do NCV [g/kWh] |
|---|---|---|

| NCVmeas | \= | NCV do combustível utilizado no ensaio de verificação, determinado em conformidade com o anexo V, ponto 3.2, [MJ/kg] |
|---|---|---|

| NCVstd | \= | NCV normalizado em conformidade com o quadro 5 do anexo V, ponto 5.4.3.1, [MJ/kg] |
|---|---|---|

Esta correção é aplicada a todos os tipos de combustível, ou seja, também para motores diesel (ver nota de rodapé 2 do quadro 4-A).

Numa terceira etapa, é aplicada a correção em função da uma fase de rodagem:

image

em que:

| BSFCm-c | \= | consumo do combustível específico da travagem, medido e corrigido em função de uma fase de rodagem |
|---|---|---|

| ef | \= | coeficiente de evolução de 0,98 |
|---|---|---|

| mileage | \= | distância de rodagem [km] |
|---|---|---|

Para os veículos com duplo combustível, as três etapas de avaliação são executadas separadamente para ambos os combustíveis.

3. Determinação do consumo de combustível específico da travagem simulado pela ferramenta de simulação (BSFCsim)

No modo de ensaio de verificação da ferramenta de simulação, a potência de roda medida é aplicada como dado de entrada no algoritmo de simulação retrospetivo. As velocidades engatadas durante o ensaio de verificação são determinadas mediante cálculo das velocidades do motor por relação de transmissão à velocidade medida do veículo e selecionando a relação de transmissão que proporciona a velocidade do motor mais próxima da velocidade do motor medida. Para as transmissões APT durante fases com conversor de binário ativo, é utilizado o sinal efetivo da velocidade proveniente da medição.

Os modelos de perda para engrenagem de eixo, transmissão angular, retardadores, transmissões e PTO são aplicados de forma semelhante à do modo de declaração da ferramenta de simulação.

Para o consumo de energia das unidades auxiliares relativas à bomba de direção, ao sistema pneumático, ao sistema elétrico e ao sistema AVAC, aplicam-se os valores genéricos aplicados por tecnologia na ferramenta de simulação. Para autocarros pesados, é igualmente tido em conta o sinal registado do estado do compressor do sistema pneumático. Para o cálculo do consumo de energia da ventoinha de arrefecimento do motor aplicam-se as seguintes fórmulas:

Caso a — Ventoinhas de arrefecimento do motor não elétricas:

image

em que:

| Pfan | \= | consumo de energia da ventoinha de arrefecimento do motor [kW] |
|---|---|---|

| t | \= | nó temporal [s] |
|---|---|---|

| nfan | \= | velocidade de rotação medida da ventoinha [rpm] |
|---|---|---|

| Dfan | \= | diâmetro da ventoinha [mm] |
|---|---|---|

| C1 | \= | 7,32 kW |
|---|---|---|

| C2 | \= | 1 200 rpm |
|---|---|---|

| C3 | \= | 810 mm |
|---|---|---|

| C4 | \= | para autocarros pesados, o fator indicado no quadro 6, para as outras categorias de veículos é igual a 1 |
|---|---|---|

Quadro 6

Fatores C4 para o cálculo do consumo de energia da ventoinha de arrefecimento do motor para autocarros pesados

<table> <tbody> <tr> <td>Grupo de acionamento da ventoinha</td> <td>Controlo da ventoinha</td> <td>C4</td> </tr> <tr> <td rowspan="5">Montado na cambota</td> <td>Embraiagem viscosa com controlo eletrónico</td> <td>1,05</td> </tr> <tr> <td>Embraiagem viscosa com controlo bimetálico</td> <td>1,05</td> </tr> <tr> <td>Engate de embraiagem descontínua, 2 fases (0 % / fase 1 / fase 2)</td> <td>1,05</td> </tr> <tr> <td>Engate de embraiagem descontínua, 3 fases (0 % / fase 1 / fase 2 / fase 3)</td> <td>1,05</td> </tr> <tr> <td>Embraiagem ligada/desligada</td> <td>1,05</td> </tr> <tr> <td rowspan="5">Movido por correia ou por transmissão</td> <td>Embraiagem viscosa com controlo eletrónico</td> <td>1,11</td> </tr> <tr> <td>Embraiagem viscosa com controlo bimetálico</td> <td>1,11</td> </tr> <tr> <td>Engate de embraiagem descontínua, 2 fases (0 % / fase 1 / fase 2)</td> <td>1,11</td> </tr> <tr> <td>Engate de embraiagem descontínua, 3 fases (0 % / fase 1 / fase 2 / fase 3)</td> <td>1,11</td> </tr> <tr> <td>Embraiagem ligada/desligada</td> <td>1,11</td> </tr> <tr> <td rowspan="2">Hidráulico</td> <td>Bomba de deslocamento variável</td> <td>1,75</td> </tr> <tr> <td>Bomba de deslocamento constante</td> <td>2,25</td> </tr> </tbody> </table>

Caso b — Ventoinhas de arrefecimento do motor elétricas:

Pfan(t) = P

el(t)

. 1,43

| Pfan | \= | consumo de energia da ventoinha de arrefecimento do motor [kW] |
|---|---|---|
| t | \= | nó temporal [s] |
| Pel | \= | potência elétrica nos terminais da(s) ventoinha(s) de arrefecimento do motor, medida em conformidade com o ponto 5.6.1. |

No caso de veículos com eventos de «para/arranca» do motor durante o ensaio de verificação, são aplicadas correções semelhantes às do consumo de energia dos dispositivos auxiliares e da energia para reiniciar o motor, tal como acontece no modo de declaração da ferramenta de simulação.

A simulação do consumo instantâneo de combustível dos motores FCsim(t) é efetuada para cada intervalo de tempo de 0,5 segundos do seguinte modo:

— interpolação a partir do mapa de combustível do motor utilizando a velocidade medida do motor e o binário do motor resultante do cálculo retrospetivo, incluindo inércia de rotação do motor calculada a partir da velocidade medida do motor,

— a solicitação de binário do motor, tal como acima determinada, limita-se às capacidades certificadas de plena carga do motor. Para esses intervalos, a potência de roda na simulação retrospetiva é reduzida em conformidade. No cálculo do BSFCsim, tal como apresentado abaixo, toma-se em consideração este perfil simulado de potência de roda (Pwheel,sim(t)),

— aplicação de um fator de correção WHTC correspondente à atribuição de circulação em zonas urbana, rural e em autoestrada com base nas definições dadas no ponto 2, subpontos 8 a 10, e na velocidade medida do veículo.

O consumo de combustível específico da travagem calculado pela ferramenta de simulação BSFCm-c aplicado no 7.2.2 para o cálculo do fator CVTP é determinado do seguinte modo:

image

em que:

| BSFCsim | \= | consumo de combustível específico da travagem determinado pela ferramenta de simulação para o ensaio de verificação [g/kWh] |
|---|---|---|
| t | \= | nó temporal [s] |
| FCsim | \= | consumo instantâneo de combustível dos motores [g/s] |
| Δt | \= | duração do incremento de tempo = 0,5 [s] |
| FCESS,corr | \= | correção do consumo de combustível no que diz respeito ao consumo de energia dos dispositivos auxiliares resultante da função «para/arranca» do motor (ESS — engine stop start), tal como aplicada no modo de declaração da ferramenta de simulação [g] |
| Wwheel,pos,sim | \= | trabalho positivo das rodas determinado pela ferramenta de simulação para o ensaio de verificação [kWh] |

image

| fs | \= | frequência de simulação = 2 [Hz] |
|---|---|---|
| Pwheel,sim | \= | potência da roda simulada para o ensaio de verificação [kW] |

No caso de motores com duplo combustível, o BSFCsim é determinado separadamente para ambos os combustíveis.

**PARTE B: Determinação das emissões poluentes específicas da travagem**

A potência do motor é calculada a partir dos sinais medidos da velocidade do motor e do binário do motor do seguinte modo:

image

em que:

| Peng,m | \= | potência do motor medida no ensaio de verificação [kW] |
|---|---|---|

| t | \= | nó temporal [s] |
|---|---|---|

| neng | \= | velocidade de rotação do motor medida [rpm] |
|---|---|---|

| Teng | \= | binário medido do motor [Nm] |
|---|---|---|

O trabalho positivo do motor medido no ensaio de verificação é calculado do seguinte modo:

image

| Wwheel,pos,m | \= | trabalho positivo das rodas medido no ensaio de verificação [kWh] |
|---|---|---|

| fs | \= | frequência de amostragem = 2 [Hz] |
|---|---|---|

| tstart | \= | primeira marca temporal nos dados de medição tratados em conformidade com o quadro 4 [s] |
|---|---|---|

| tend | \= | última marca temporal nos dados de medição tratados em conformidade com o quadro 4 [s] |
|---|---|---|

As emissões poluentes específicas da travagem medidas no ensaio de verificação são calculadas do seguinte modo:

image

em que:

| BSEM | \= | emissões poluentes específicas da travagem medidas no ensaio de verificação [g/kWh] |
|---|---|---|

| EM | \= | caudal mássico instantâneo de emissões poluentes medidas durante o ensaio de verificação [g/s] |
|---|---|---|

(*) Diretiva 96/53/CE do Conselho, de 25 de julho de 1996, que fixa as dimensões máximas autorizadas no tráfego nacional e internacional e os pesos máximos autorizados no tráfego internacional para certos veículos rodoviários em circulação na Comunidade (JO L 235 de 17.9.1996, p. 59).

(**) Apenas se for necessário medir este componente em conformidade com o anexo II, apêndice 1, ponto 1, do Regulamento (UE) n.º 582/2011.

(***) Para motores de ignição comandada.
