---
id: "regulamento-ue-2024-2594-anexo-xi-a-anexo-xxiii"
celex: "32024R2594"
title: "Regulamento (UE) 2024/2594 do Parlamento Europeu e do Conselho, de 18 de setembro de 2024, que estabelece medidas de conservação, de gestão e de controlo aplicáveis na área abrangida pela Convenção sobre a Futura Cooperação Multilateral nas Pescas do Atlântico Nordeste, que altera o Regulamento (UE) 2019/1241 do Parlamento Europeu e do Conselho e o Regulamento (CE) n.° 1224/2009 do Conselho e que revoga o Regulamento (UE) n.° 1236/2010 do Parlamento Europeu e do Conselho e os Regulamentos (CEE) n.° 1899/85 e (CEE) n.° 1638/87 do Conselho — Anexo XI a Anexo XXIII"
type: "Regulamento"
number: "2024/2594"
year: 2024
date: 2024-09-18
status: "em vigor"
text_version: "consolidado"
last_amended: 2025-11-13
consolidated_celex: "02024R2594-20251113"
source: "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:02024R2594-20251113"
eli: "http://data.europa.eu/eli/reg/2024/2594/oj"
retrieved: 2026-10-21
legal_notice: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
part_of: "regulamento-ue-2024-2594"
part: "Anexo XI a Anexo XXIII"
---

# Regulamento (UE) 2024/2594 do Parlamento Europeu e do Conselho, de 18 de setembro de 2024, que estabelece medidas de conservação, de gestão e de controlo aplicáveis na área abrangida pela Convenção sobre a Futura Cooperação Multilateral nas Pescas do Atlântico Nordeste, que altera o Regulamento (UE) 2019/1241 do Parlamento Europeu e do Conselho e o Regulamento (CE) n.° 1224/2009 do Conselho e que revoga o Regulamento (UE) n.° 1236/2010 do Parlamento Europeu e do Conselho e os Regulamentos (CEE) n.° 1899/85 e (CEE) n.° 1638/87 do Conselho — Anexo XI a Anexo XXIII

## Anexo XI — COMUNICAÇÕES EM FORMATO NAF

**1. Formato da transmissão de dados**

As transmissões de dados têm a seguinte estrutura:

— Carateres em conformidade com a norma ISO 8859.1;

— As transmissões de dados têm a seguinte estrutura:

— duas barras oblíquas («//») e os carateres «SR» assinalam o início de uma mensagem,

— duas barras oblíquas («//») e um código assinalam o início de um elemento de dados,

— uma barra oblíqua simples («/») assinala a separação entre o código e os dados,

— os pares de dados são separados por um espaço,

— os carateres «ER» e duas barras oblíquas («//») assinalam o fim de um registo.

**2. Formato para a troca eletrónica de dados relativos à monitorização, inspeção e vigilância da pesca**

<table> <tbody> <tr> <td colspan="6">Formato para a troca eletrónica de dados relativos à monitorização, inspeção e vigilância da pesca</td> </tr> <tr> <td>Categoria</td> <td>Elemento de dados</td> <td>Código do campo</td> <td>Tipo</td> <td>Conteúdo</td> <td>Definições</td> </tr> <tr> <td rowspan="4">Dados relativos ao sistema</td> <td>Início do registo</td> <td>SR</td> <td></td> <td></td> <td>Indica o início do registo</td> </tr> <tr> <td>Fim do registo</td> <td>ER</td> <td></td> <td></td> <td>Indica o fim do registo</td> </tr> <tr> <td>Estatuto da receção</td> <td>RS</td> <td>Car*3</td> <td>Códigos</td> <td>ACK/NAK = recebido/não recebido</td> </tr> <tr> <td>Código de erro de receção</td> <td>RE</td> <td>Num*3</td> <td>001-999</td> <td>Códigos de erro recebidos no centro das operações, ver anexo XI, ponto 3</td> </tr> <tr> <td rowspan="11">Dados relativos à mensagem</td> <td>Endereço do destinatário</td> <td>AD</td> <td>Car*3</td> <td>Endereço ISO-3166</td> <td>Endereço da parte destinatária da mensagem, «XNE» para NEAFC</td> </tr> <tr> <td>Remetente</td> <td>FR</td> <td>Car*3</td> <td>Endereço ISO-3166</td> <td>Endereço da parte que transmite a mensagem (parte contratante)</td> </tr> <tr> <td>Tipo de mensagem</td> <td>TM</td> <td>Car*3</td> <td>Código</td> <td>Três primeiras letras do tipo de mensagem</td> </tr> <tr> <td>Número sequencial</td> <td>SQ</td> <td>Num*6</td> <td>NNNNNN</td> <td>Número sequencial das mensagens enviadas por um navio para o destinatário final (XNE). Trata-se de um número único por navio e por ano civil. No início de cada ano, a numeração recomeça em 1 para cada navio, aumentando com cada mensagem enviada.</td> </tr> <tr> <td>Número do registo</td> <td>RN</td> <td>Num*6</td> <td>NNNNNN</td> <td>Número sequencial dos registos enviados pelo CVP a XNE. Trata-se de um número único por CVP e por ano civil. No início de cada ano, a numeração recomeça em 1, aumentando com cada registo enviado.</td> </tr> <tr> <td>Data de registo</td> <td>RD</td> <td>Num*8</td> <td>AAAAMMDD</td> <td>Ano, mês e dia TUC do CVP</td> </tr> <tr> <td>Hora do registo</td> <td>RT</td> <td>Num*4</td> <td>HHMM</td> <td>Horas e minutos TUC do CVP</td> </tr> <tr> <td>Data</td> <td>DA</td> <td>Num*8</td> <td>AAAAMMDD</td> <td>Ano, mês e dia TUC da primeira transmissão. No caso das mensagens RET, a primeira transmissão provém do CVP, em todos os outros casos a primeira transmissão provém do navio.</td> </tr> <tr> <td>Hora</td> <td>TI</td> <td>Num*4</td> <td>HHMM</td> <td>Horas e minutos TUC da primeira transmissão. No caso das mensagens RET, a primeira transmissão provém do CVP, em todos os outros casos a primeira transmissão provém do navio.</td> </tr> <tr> <td>Comunicação anulada</td> <td>CR</td> <td>Num*6</td> <td>NNNNNN</td> <td>Número de registo da comunicação a anular</td> </tr> <tr> <td>Ano da comunicação anulada</td> <td>YR</td> <td>Num*4</td> <td>NNNN</td> <td>Ano TUC da comunicação a anular</td> </tr> <tr> <td rowspan="9">Dados relativos ao registo do navio</td> <td>Indicativo de chamada rádio</td> <td>RC</td> <td>Car*7</td> <td>Código IRCS</td> <td>Indicativo de chamada rádio internacional do navio</td> </tr> <tr> <td>Nome do navio</td> <td>NA</td> <td>Car*45</td> <td></td> <td>Nome do navio</td> </tr> <tr> <td>Número IMO</td> <td>IM</td> <td>Num*12</td> <td>NNNNNNNNNNNN</td> <td>Número OMI do navio</td> </tr> <tr> <td>Número de registo externo</td> <td>XR</td> <td>Car*14</td> <td></td> <td>Número lateral do navio</td> </tr> <tr> <td>Estado do pavilhão</td> <td>FS</td> <td>Car*3</td> <td>ISO-3166</td> <td>Estado em que o navio está registado</td> </tr> <tr> <td>Número de referência interno da parte contratante</td> <td>IR</td> <td>Car*3 Car*9</td> <td>ISO-3166 +máx. 9 carateres</td> <td>Código de três letras do país seguido do identificador único do navio de 9 carateres atribuído pelo Estado do pavilhão segundo o registo</td> </tr> <tr> <td>Nome do porto</td> <td>PO</td> <td>Car*45</td> <td></td> <td>Porto de registo do navio</td> </tr> <tr> <td>Proprietário do navio</td> <td>VO</td> <td>Car*250</td> <td></td> <td>Nome e endereço do proprietário do navio</td> </tr> <tr> <td>Afretador do navio</td> <td>VC</td> <td>Car*250</td> <td></td> <td>Nome e endereço do afretador do navio</td> </tr> <tr> <td rowspan="5">Dados do navio</td> <td>Unidade de capacidade do navio</td> <td>VT</td> <td>Car*2 Num*5</td> <td>Arqueação «OC» ou «LC»</td> <td>«OC» (Convenção de Oslo de 1947)/«LC» (Convenção ICTM de Londres, 1969) Capacidade do navio em toneladas</td> </tr> <tr> <td>Unidade de potência do navio</td> <td>VP</td> <td>Car*2 Num*5</td> <td>0-99999</td> <td>Indicação da unidade de medida utilizada: «Hp» ou «kW». Potência total do motor principal</td> </tr> <tr> <td>Comprimento do navio</td> <td>VL</td> <td>Car*2 Num*3</td> <td>Comprimento em metros «AO» ou «PP»</td> <td>«AO» = comprimento de fora a fora; «PP» = comprimento entre perpendiculares Comprimento total do navio em metros, arredondado ao metro inteiro mais próximo</td> </tr> <tr> <td>Tipo de navio</td> <td>TP</td> <td>Car*3</td> <td>Código</td> <td></td> </tr> <tr> <td>Arte de pesca</td> <td>GE</td> <td>Car*3</td> <td>Código FAO</td> <td>Classificação estatística normalizada internacional das artes de pesca</td> </tr> <tr> <td rowspan="5">Dados relativos à licença</td> <td>Data de emissão</td> <td>IS</td> <td>Num*8</td> <td>AAAAMMDD</td> <td>Data da autorização de pescar uma ou várias espécies regulamentadas</td> </tr> <tr> <td>Recursos regulamentados</td> <td>RR</td> <td>Car*3</td> <td>Código FAO da espécie</td> <td>Código FAO da espécie para os recursos regulamentados, separado por um espaço</td> </tr> <tr> <td>Data de início</td> <td>SD</td> <td>Num*8</td> <td>AAAAMMDD</td> <td>Data em que começa a validade da autorização/suspensão</td> </tr> <tr> <td>Data de fim</td> <td>ED</td> <td>Num*8</td> <td>AAAAMMDD</td> <td>Data do termo de validade da autorização de pescar um recurso regulamentado</td> </tr> <tr> <td>Autorização limitada</td> <td>LU</td> <td>Car*1</td> <td></td> <td>«Y» (sim) ou «N» (não) para indicar se existe ou não uma autorização limitada</td> </tr> <tr> <td rowspan="11">Dados relativos à vigilância/ observação</td> <td>Latitude</td> <td>LA</td> <td>Car*5</td> <td>NGGMM (WGS-84)</td> <td>Por exemplo, //LA/N6535 = 65º35′ Norte</td> </tr> <tr> <td>Longitude</td> <td>LO</td> <td>Car*6</td> <td>E/WGGGMM (WGS-84)</td> <td>Por exemplo, //LO/W02134 = 21º34′ Oeste</td> </tr> <tr> <td>Velocidade</td> <td>SP</td> <td>Num*3</td> <td>Nós*10</td> <td>Por exemplo, //SP/105 = 10,5 nós</td> </tr> <tr> <td>Meios de vigilância</td> <td>MI</td> <td>Car*3</td> <td>Código NEAFC</td> <td>«VES» para os navios de superfície, «AIR» para as aeronaves de asa fixa e «HEL» para os helicópteros</td> </tr> <tr> <td>ID da PC do inspetor designado</td> <td>AI</td> <td>Car*7</td> <td>Código NEAFC</td> <td>Código ISO-3166 da parte contratante seguido de um número de 4 dígitos, repetido se necessário</td> </tr> <tr> <td>Número sequencial da observação</td> <td>OS</td> <td>Num*3</td> <td>0-999</td> <td>Número sequencial da observação para a patrulha que opera na área de regulamentação</td> </tr> <tr> <td>Data do avistamento</td> <td>DA</td> <td>Num*8</td> <td>AAAAMMDD</td> <td>Data em que o navio é avistado</td> </tr> <tr> <td>Hora do avistamento</td> <td>TI</td> <td>Num*4</td> <td>HHMM</td> <td>Hora TUC em que o navio é avistado</td> </tr> <tr> <td>Identificação do objeto</td> <td>OI</td> <td>Car*7</td> <td>Código IRCS</td> <td>Indicativo de chamada rádio internacional do navio avistado</td> </tr> <tr> <td>Fotografia</td> <td>PH</td> <td>Car*1</td> <td></td> <td>«Y» (sim) ou «N» (não) para indicar se foi tirada uma fotografia</td> </tr> <tr> <td>Texto livre</td> <td>MS</td> <td>Car*255</td> <td></td> <td>Zona para texto livre</td> </tr> </tbody> </table>

**3. Avisos de receção**

As especificações do formato para o envio de comunicações do Secretariado da NEAFC (XNE) a um CVP são as seguintes:

| Formato do aviso de receção |  |  |  |
|---|---|---|---|
| Elemento de dados | Código do campo |  | Observações |
| Início do registo | SR | O | Dados relativos ao sistema; indica o início do registo |
| Endereço | AD | O | Dados relativos à mensagem; destinatário, parte contratante que envia a comunicação |
| Remetente | FR | O | Dados relativos à mensagem; XNE é a NEAFC (que emite o aviso de receção) |
| Tipo de mensagem | TM | O | Dados relativos à mensagem; tipo de mensagem, RET para aviso de receção |
| Número sequencial | SQ | F | Dados relativos à comunicação; número sequencial da comunicação do navio para o ano em causa, copiado da comunicação recebida |
| Indicativo de chamada rádio | RC | F | Dados relativos à comunicação; indicativo de chamada rádio internacional do navio, copiado da comunicação recebida |
| Estatuto da receção | RS | O | Dados relativos à comunicação; código que indica se a receção da comunicação/mensagem foi confirmada ou não (ACK ou NAK) |
| Código de erro de receção | RE | F | Dados relativos à comunicação; número que indica o tipo de erro |
| Número do registo | RN | O | Dados relativos à comunicação; número do registo da comunicação/mensagem recebida |
| Data | DA | O | Dados relativos à mensagem; data de transmissão da mensagem RET da NEAFC (XNE) ao CVP |
| Hora | TI | O | Dados relativos à mensagem; hora da transmissão da mensagem RET da NEAFC (XNE) ao CVP |
| Fim do registo | ER | O | Dados relativos ao sistema; indica o fim do registo |

**4. Código de erro de receção**

| Recusada (NAK) Ação de seguimento exigida |  | Aceite e armazenada (ACK) com aviso | Causa do erro |
|---|---|---|---|
| 101 |  |  | Mensagem ilegível |
| 102 |  |  | Valor ou dimensão dos dados não respeita a série definida |
| 104 |  |  | Dados obrigatórios omitidos |
| 105 |  |  | Esta comunicação é uma repetição; tentativa de reenviar uma comunicação anteriormente recusada |
| 106 |  |  | Fonte de dados não autorizada |
|  |  | 150 | Erro de sequência |
|  |  | 151 | Data/hora no futuro |
|  |  | 155 | Esta comunicação é uma repetição; tentativa de reenviar uma comunicação anteriormente aceite |
|  |  | 250 | Tentativa de nova notificação a um navio |
|  | 251 |  | Navio não notificado |
|  | 252 |  | Espécie não AUT, LIM ou SUS |

**5. Tipos de mensagens e comunicações**

| Código | Mensagem/ Comunicação | Observações |
|---|---|---|
| RET | Receção | Mensagem eletrónica automática na sequência da receção dos registos |
| SEN | Entrada de vigilância | Comunicação transmitida pela parte contratante sobre a entrada de navio ou aeronave de vigilância na área de regulamentação |
| SEX | Saída de vigilância | Comunicação transmitida pela parte contratante sobre a saída de navio ou aeronave de vigilância da área de regulamentação |
| OBS | Observação | Comunicação transmitida pela parte contratante sobre as observações dos navios de pesca na área de regulamentação efetuadas pelos seus inspetores afetados nos termos do presente regulamento |

A lista de códigos de tipos dos navios de pesca e artes de pesca deve estar em conformidade com o registo dos dados de referência da NEAFC, disponível em https://www.neafc.org/mdr.

## Anexo XII — MARCAÇÃO DO CVP

O CVP deve utilizar os seguintes códigos para marcar as comunicações antes de as transmitir ao Secretariado da NEAFC, quando necessário:

| Código (uma letra) | Designação |
|---|---|
| D | Comunicações enviadas com atraso e sem alterações por parte do CVP |
| C | Comunicações corrigidas ou anuladas pelo CVP |
| M | Comunicações registadas manualmente pelo CVP |

As comunicações devem satisfazer todos os requisitos técnicos e requisitos de formato.

## Anexo XIII — IDENTIFICAÇÃO DOS INSPETORES

image

image

O cartão deve medir 10 × 7 cm e pode ser plastificado. O número do cartão é formado pelo código alfa-3 do país, seguido do número de série de quatro dígitos da parte contratante.

## Anexo XIV — NOTIFICAÇÃO DOS INSPETORES E DAS PLATAFORMAS DE INSPEÇÃO

**1. Inspetores**

| Elemento de dados | Código do campo |  | Observações |
|---|---|---|---|
| Nome dos inspetores | NA | O | O nome do inspetor |
| ID único da PC | ID | O | O número único da parte contratante precedido pelo código alfa-3 do país |
| Endereço eletrónico: | \* | O | Endereço eletrónico do inspetor |

**2. Plataformas de inspeção**

| Elemento de dados | Código do campo |  | Observações |
|---|---|---|---|
| Tipo | \* | O | Navio, aeronave ou helicóptero |
| Estado do pavilhão | FS | O | O Estado do pavilhão da plataforma |
| Número de registo | \* | F | O registo do Estado do pavilhão, se disponível |
| Nome | NA | F | Nome da plataforma, se disponível |
| Indicativo de chamada rádio | RC | O | Indicativo de chamada rádio internacional (IRCS) |
| Radiofrequências | \* | O | Radiofrequências disponíveis (2 182 kHz, canal 16, etc.) |
| Telefone | \* | F | Número(s) de telefone, se disponível |
| Endereço de correio eletrónico | \* | F | Endereço(s) eletrónico(s) (se disponível) |

## Anexo XV — SINAL DE INSPEÇÃO DA NEAFC

Dois galhardetes, colocados diretamente um acima do outro, a utilizar de dia e em condições de visibilidade normais.

image

Os botes de acostagem devem arvorar um galhardete de inspeção como indicado infra. O galhardete pode ser reduzido a meia escala. Pode ser pintado no costado ou em qualquer face vertical do bote. Neste caso, não é necessário reproduzir as letras pretas «NE».

## Anexo XVI — NOTIFICAÇÃO DAS ATIVIDADES DE VIGILÂNCIA

**1. Comunicação relativa à entrada de um navio ou aeronave de vigilância na área de regulamentação**

| Mensagem de entrada do meio de vigilância (SEN) |  |  |
|---|---|---|
| Elemento de dados |  | Observações |
| Remetente | O | Dados relativos à mensagem; endereço da parte contratante que transmite a mensagem |
| Número do registo | O | Dados relativos à mensagem; número sequencial da mensagem no ano em curso |
| Tipo de mensagem | O | Dados relativos à mensagem; tipo de mensagem, «SEM» para comunicação relativa à entrada de um navio ou aeronave de vigilância na área de regulamentação |
| Data de registo | O | Dados relativos à mensagem; data da transmissão |
| Hora do registo | O | Dados relativos à mensagem; hora da transmissão |
| Meios de vigilância | O | Dados relativos à vigilância; «VES» para os navios de superfície, «AIR» para as aeronaves de asa fixa e «HEL» para os helicópteros |
| Indicativo de chamada rádio | O | Dados relativos à vigilância; indicativo de chamada rádio internacional do navio ou aeronave de vigilância |
| ID dos inspetores designados | O | Dados relativos à vigilância; número do cartão, repetido se necessário |
| Data | O | Dados relativos à vigilância; data da entrada () |
| Hora | O | Dados relativos à vigilância; hora da entrada () |
| Latitude | O | Dados relativos à vigilância; posição no momento da entrada () |
| Longitude | O | Dados relativos à vigilância; posição no momento da entrada () |
| Fim do registo | O | Dados relativos ao sistema; indica o fim do registo |
| (1) <br> Estimada, quando a mensagem é enviada antes da entrada do navio ou aeronave de vigilância |  |  |

**2. Comunicação relativa à saída de um navio ou aeronave de vigilância da área de regulamentação**

| Mensagem de saída do meio de vigilância (SEX) |  |  |
|---|---|---|
| Elemento de dados |  | Observações |
| Remetente | O | Dados relativos à mensagem; endereço da parte contratante que transmite a mensagem |
| Número do registo | O | Dados relativos à mensagem; número sequencial da mensagem no ano em curso |
| Tipo de mensagem | O | Dados relativos à mensagem; tipo de mensagem, «SEX» para comunicação relativa à saída de um navio ou aeronave de vigilância da área de regulamentação |
| Data de registo | O | Dados relativos à mensagem; data da transmissão |
| Hora do registo | O | Dados relativos à mensagem; hora da transmissão |
| Meios de vigilância | O | Dados relativos à vigilância; «VES» para os navios de superfície, «AIR» para as aeronaves de asa fixa e «HEL» para os helicópteros |
| Indicativo de chamada rádio | O | Dados relativos à vigilância; indicativo de chamada rádio internacional do navio ou aeronave de vigilância |
| Data | O | Dados relativos à vigilância; data da saída () |
| Hora | O | Dados relativos à vigilância; hora da saída () |
| Latitude | O | Dados relativos à vigilância; posição na hora da saída () |
| Longitude | O | Dados relativos à vigilância; posição na hora da saída () |
| Fim do registo | O | Dados relativos ao sistema; indica o fim do registo |
| (1) <br> Corresponde aos dados relativos à vigilância estimados na mensagem «SEN», se esta mensagem for anulada. |  |  |

## Anexo XVII — RELATÓRIO DE AVISTAMENTO

| Relatório de avistamento (OBS) |  |  |  |
|---|---|---|---|
| Elemento de dados | Código |  | Observações |
| Início do registo | SR | O | Dados relativos ao sistema; indica o início do registo |
| Endereço | AD | O | Dados relativos à mensagem; destino, «XNE» para a NEAFC |
| Remetente | FR | O | Dados relativos à mensagem; endereço da parte contratante que transmite a mensagem |
| Número do registo | RN | O | Dados relativos à mensagem; número sequencial no ano em curso |
| Tipo de mensagem | TM | O | Dados relativos à mensagem; tipo de mensagem, «OBS» para relatório de observação |
| Indicativo de chamada rádio | RC | O | Dados relativos à vigilância; indicativo de chamada rádio internacional do navio ou aeronave de vigilância |
| Data de registo | RD | O | Dados relativos à mensagem; data da transmissão |
| Hora do registo | RT | O | Dados relativos à mensagem; hora da transmissão |
| Número sequencial da observação | OS | O | Dados relativos à vigilância; número sequencial da observação |
| Data | DA | O | Dados relativos à vigilância; data em que o navio foi avistado |
| Hora | TI | O | Dados relativos à vigilância; hora em que o navio foi avistado |
| Latitude | LA | O | Dados relativos à vigilância; latitude em que o navio foi avistado |
| Longitude | LO | O | Dados relativos à vigilância; longitude em que o navio foi avistado |
| Identificação do objeto | OI | O | Dados relativos ao registo do navio; indicativo de chamada rádio do navio avistado |
| Número de registo externo | XR | O | Dados relativos ao registo do navio; número lateral do navio avistado ou, na sua ausência, número OMI |
| Nome do navio | NA | F | Dados relativos ao registo do navio; nome do navio avistado |
| Estado do pavilhão | FS | O | Dados relativos ao registo do navio; Estado do pavilhão do navio avistado |
| Tipo de navio | TP | F | Características do navio; tipo do navio avistado |
| Velocidade | SP | F | Dados relativos à vigilância; velocidade do navio avistado |
| Rumo | CO | F | Dados relativos à vigilância; direção do navio avistado |
| Atividade | AC | O | Dados relativos à vigilância; atividade do navio avistado |
| Fotografia | PH | O | Dados relativos à vigilância; «Y» (sim) ou «N» (não) para indicar se foi tirada uma fotografia do navio avistado |
| Observações | MS | F | Dados relativos à vigilância; texto livre para completar o relatório |
| Fim do registo | ER | O | Dados relativos ao sistema; indica o fim do registo |

A identificação formal do navio só pode ser feita por verificação visual do indicativo de chamada rádio ou do número de registo externo ostentado pelo navio.

Se não for possível uma identificação formal, indicar o motivo no campo destinado às «observações».

A lista de atividades do navio avistado deve estar em conformidade com o registo dos dados de referência da NEAFC, disponível em https://www.neafc.org/mdr.

## Anexo XVIII

image

image

image

image

image

image

image

image

image

image

image

image

image

## Anexo XIX — CONSTRUÇÃO E UTILIZAÇÃO DE ESCADAS DE PORTALÓ

1. Será instalada uma escada de portaló com a necessária eficiência para permitir que os inspetores embarquem e desembarquem em segurança no mar. A escada de portaló será mantida limpa e em bom estado.

2. A escada será colocada e fixada de modo a que:

a) Esteja protegida de quaisquer possíveis descargas do navio;

b) Esteja afastada das arestas mais vivas do navio de pesca e, na medida do possível, colocada a meio comprimento do navio;

c) Todos os degraus fiquem firmemente apoiados contra o casco do navio.

3. Os degraus da escada de portaló:

a) Serão de madeira rija, ou outro material com propriedades equivalentes, e feitos de uma só peça isenta de nós; os quatro degraus inferiores podem ser de borracha com resistência e firmeza suficientes ou de outro material adequado com características equivalentes;

b) Terão uma superfície antiderrapante eficiente;

c) Terão pelo menos 480 mm de comprimento, 115 mm de largura e 23 mm de espessura, com exclusão de qualquer dispositivo antiderrapante ou entalhe;

d) Estarão a espaços iguais de, pelo menos, 300 mm e, no máximo, 380 mm;

e) Serão fixados de modo a manterem-se horizontais.

4. Nenhuma escada de portaló terá mais do que dois degraus sobresselentes fixados por um método diferente do usado na construção original da escada e qualquer degrau fixado desse modo será substituído logo que possível por degraus fixados pelo método utilizado na construção original da escada. Sempre que qualquer degrau sobresselente esteja fixado nos cabos laterais da escada por meio de entalhes feitos nas laterais do degrau, os entalhes encontrar-se-ão nos lados maiores do degrau.

5. Os cabos laterais da escada serão constituídos por dois cabos de manila não revestidos ou por cabos equivalentes com, pelo menos, 60 mm de perímetro; os cabos não serão revestidos de qualquer outro material e serão contínuos, sem junções até ao degrau superior. Deverão estar prontos a ser utilizados, em caso de necessidade, dois cabos de portaló devidamente fixados ao navio com, pelo menos, 65 mm de perímetro, assim como um cabo de segurança.

6. Serão colocadas, a intervalos que permitam evitar que a escada de portaló se enrole, réguas de madeira rija, ou de outro material com propriedades equivalentes, de uma só peça isenta de nós com 1,80 a 2 m de comprimento. A régua inferior será colocada no quinto degrau da parte inferior da escada e o intervalo entre as diversas réguas não será superior a nove degraus.

7. Serão providenciados meios que assegurem aos inspetores que embarquem e desembarquem do navio uma passagem segura e conveniente a partir do cimo da escada de piloto ou de qualquer escada de portaló ou outro dispositivo existente. No caso de essa passagem se efetuar através de uma abertura na balaustrada ou na borda falsa, serão providenciadas pegas adequadas. Quando a passagem se efetuar por uma escada da borda falsa, essa escada será fixada de modo seguro na balaustrada ou na plataforma da borda falsa e serão fixados dois espeques com pegas no ponto de embarque ou de desembarque do navio de pesca com um intervalo de, pelo menos, 0,70 m e, no máximo, 0,80 m. Os espeques serão firmemente fixados à estrutura do navio pela sua base ou na proximidade desta e também num ponto mais alto, não terão menos de 40 mm de diâmetro e prolongar-se-ão por, pelo menos, 1,20 m acima da parte superior da borda falsa.

8. À noite, será providenciada iluminação de modo a que tanto a escada de portaló como também o lugar em que o inspetor embarca no navio sejam adequadamente iluminados. Será mantida à mão, pronta a ser utilizada, uma boia de salvação, equipada com uma luz de autoignição. Além disso, será mantido à mão, pronto a ser utilizado se necessário, um cabo de elevação.

9. Serão providenciados meios para que a escada de portaló possa ser utilizada nos dois bordos do navio. O inspetor pode indicar de que lado gostaria que fosse colocada a escada.

10. O aparelhamento da escada e o embarque e desembarque de um inspetor serão dirigidos por um oficial responsável do navio. O oficial responsável estará em contacto rádio com a ponte.

11. Sempre que, em qualquer navio, características de construção, tais como defensas, possam impedir a execução de qualquer das presentes disposições, serão tomadas providências especiais para assegurar que os inspetores possam embarcar e desembarcar em condições de segurança.

## Anexo XX — INFORMAÇÕES SOBRE OS PORTOS DESIGNADOS

<table> <tbody> <tr> <td colspan="7">Identificação do porto</td> </tr> <tr> <td rowspan="2">País</td> <td rowspan="2">Nome do porto ()</td> <td rowspan="2">Código do porto () (UN/LOCODE, se disponível)</td> <td rowspan="2">Posto de controlo de inspeção fronteiriço (Sim / Não)</td> <td colspan="3">Tipo de porto</td> </tr> <tr> <td>Desembarque</td> <td>Transbordo</td> <td>Outros serviços portuários</td> </tr> <tr> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> </tr> <tr> <td colspan="7">(1) Código e nome constantes da lista UNECE.</td> </tr> </tbody> </table>

## Anexo XXI — FORMULÁRIOS DE CONTROLO PELO ESTADO DO PORTO

image

image

image

image

image

image

## Anexo XXII — ORIENTAÇÕES GERAIS PARA A GESTÃO DO RISCO EM RELAÇÃO AO CONTROLO PELO ESTADO DO PORTO

1. Por gestão do risco entende-se a identificação sistemática dos riscos e a aplicação de todas as medidas necessárias para limitar a concretização dos mesmos. Inclui atividades como a recolha de dados e de informações, a análise e a avaliação dos riscos, a preparação e a tomada de medidas e a monitorização e revisão regulares do processo e dos seus resultados.

2. Com base numa avaliação dos riscos, os Estados-Membros, em coordenação com a AECP, definem uma estratégia de gestão dos riscos para facilitar o cumprimento do presente regulamento. Essa estratégia deve abranger a identificação, descrição e atribuição de instrumentos de controlo e meios de inspeção adequados e eficientes em termos de custos, adaptados à natureza e ao nível estimado de cada risco, bem como a consecução dos marcos de referência-alvo.

3. São estabelecidos critérios de avaliação e gestão do risco para as atividades de controlo, inspeção e verificação, de modo a permitir a realização atempada de análises de risco e de avaliações globais das informações pertinentes sobre o controlo e a inspeção.

4. São submetidos a controlo e inspeção, em função do grau de risco atribuído, navios de pesca individuais, grupos de navios de pesca, operadores e/ou atividades de pesca, relativamente a diferentes espécies e em diferentes partes da área da Convenção, recorrendo designadamente aos seguintes pressupostos gerais de critérios de nível de risco aquando do controlo, pelo Estado do porto, dos desembarques e transbordos no porto:

a) Capturas efetuadas por um navio de uma parte não contratante;

b) Capturas congeladas;

c) Capturas de grande volume;

d) Capturas previamente transbordadas no mar;

e) Capturas efetuadas fora das águas sob a jurisdição das partes contratantes, ou seja, na área de regulamentação;

f) Capturas efetuadas dentro e fora da área da Convenção;

g) Capturas de espécies de valor elevado;

h) Capturas de recursos haliêuticos em relação aos quais as possibilidades de pesca são particularmente reduzidas; e

i) Número de inspeções realizadas anteriormente e número de infrações detetadas relativamente a um navio e/ou operador.

## Anexo XXIII — FORMULÁRIO PARA A INSPEÇÃO NO PORTO

image

image

image

image

image

image

image

(

) Regulamento (CE) n.º 216/2009 do Parlamento Europeu e do Conselho, de 11 de março de 2009, relativo à apresentação de estatísticas de capturas nominais efetuadas pelos Estados-Membros que pescam em certas zonas, com exclusão das do Atlântico Norte (JO L 87 de 31.3.2009, p. 1).

(

) Regulamento (UE) 2017/2403 do Parlamento Europeu e do Conselho, de 12 de dezembro de 2017, relativo à gestão sustentável das frotas de pesca externas, e que revoga o Regulamento (CE) n.º 1006/2008 do Conselho (JO L 347 de 28.12.2017, p. 81).

(

) Regulamento (CE) n.º 1005/2008 do Conselho, de 29 de setembro de 2008, que estabelece um regime comunitário para prevenir, impedir e eliminar a pesca ilegal, não declarada e não regulamentada, que altera os Regulamentos (CEE) n.º 2847/93, (CE) n.º 1936/2001 e (CE) n.º 601/2004, e que revoga os Regulamentos (CE) n.º 1093/94 e (CE) n.º 1447/1999 (JO L 286 de 29.10.2008, p. 1).

(

)

JO L 227 de 12.8.1981, p. 22.

(

) Regulamento (UE) 2019/473 do Parlamento Europeu e do Conselho, de 19 de março de 2019, sobre a Agência Europeia de Controlo das Pescas (JO L 83 de 25.3.2019, p. 18).

(

) Regulamento de Execução (UE) 2017/218 da Comissão, de 6 de fevereiro de 2017, relativo ao ficheiro da frota de pesca da União (JO L 34 de 9.2.2017, p. 9).

(

) Regulamento de Execução (UE) n.º 404/2011 da Comissão, de 8 de abril de 2011, que estabelece as regras de execução do Regulamento (CE) n.º 1224/2009 do Conselho que institui um regime comunitário de controlo a fim de assegurar o cumprimento das regras da política comum das pescas (JO L 112 de 30.4.2011, p. 1).

(

) Diretiva (UE) 2019/883 do Parlamento Europeu e do Conselho, de 17 de abril de 2019, relativa aos meios portuários de receção de resíduos provenientes dos navios, que altera a Diretiva 2010/65/UE e revoga a Diretiva 2000/59/CE (JO L 151 de 7.6.2019, p. 116).

(

)

JO L 191 de 22.7.2011, p. 3.

(

)

JO L 75 de 19.3.2015, p. 4.
