---
id: "regulamento-ue-2007-416-anexo"
celex: "32007R0416"
title: "Regulamento (CE) n. o 416/2007 da Comissão, de 22 de Março de 2007 , relativo às especificações técnicas dos avisos à navegação a que se refere o artigo 5. o da Directiva 2005/44/CE do Parlamento Europeu e do Conselho relativa a serviços de informação fluvial (RIS) harmonizados nas vias navegáveis interiores da Comunidade — Anexo"
type: "Regulamento"
number: "416/2007"
year: 2007
date: 2007-03-13
status: "em vigor"
text_version: "consolidado"
last_amended: 2018-12-29
consolidated_celex: "02007R0416-20181229"
source: "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:02007R0416-20181229"
eli: "http://data.europa.eu/eli/reg/2007/416/oj"
retrieved: 2026-10-21
legal_notice: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
part_of: "regulamento-ue-2007-416"
part: "Anexo"
---

# Regulamento (CE) n. o 416/2007 da Comissão, de 22 de Março de 2007 , relativo às especificações técnicas dos avisos à navegação a que se refere o artigo 5. o da Directiva 2005/44/CE do Parlamento Europeu e do Conselho relativa a serviços de informação fluvial (RIS) harmonizados nas vias navegáveis interiores da Comunidade — Anexo

## Anexo

ÍNDICE

**1. DISPOSIÇÕES GERAIS**

**1.1. Definições**

Os serviços de informações da via navegável (FIS) asseguram o fornecimento de informações geográficas, hidrológicas e administrativas respeitantes ao canal navegável (via navegável) utilizadas pelos condutores de embarcações e gestores de frotas para planear, executar e acompanhar o transporte. Os termos «condutor de embarcação» e «comandante» utilizados na presente norma devem ser considerados equivalentes ao termo «comandante de embarcação» utilizado nas diretrizes para os serviços de informação fluvial (RIS) [Regulamento (CE) n.º 414/2007 da Comissão (

1

)], enquanto o termo «gestor da frota» é definido no Regulamento (CE) n.º 415/2007 da Comissão (

2

).

Os FIS fornecem uma informação dinâmica (por exemplo, nível da água, incluindo previsões) e estática (por exemplo, horário de serviço das eclusas e pontes) sobre o estado e a utilização da infraestrutura da via navegável, facilitando assim a tomada de decisões náuticas táticas e estratégicas.

Estes serviços são normalmente fornecidos por meio de ajudas visuais à navegação, avisos à navegação por escrito, emissões de rádio e telefonia fixa nas eclusas. A telefonia móvel possibilitou outras formas de transmissão de mensagens vocais e de dados, mas a rede celular não está disponível em todo o lado e a toda a hora. É possível fornecer FIS personalizados para as vias navegáveis interiores por radiotelefonia, Internet ou um serviço de fornecimento de cartas náuticas eletrónicas, tais como o Inland Electronic Chart Display and Information System (ECDIS-fluvial) com carta náutica eletrónica (CNE).

**1.2. Funções principais e requisitos de desempenho dos avisos à navegação (NtS)**

A presente especificação técnica dos avisos à navegação (NtS – Notices to Skippers) contém regras para a transmissão das informações do canal navegável pela Internet.

Os avisos à navegação (NtS) devem:

(a) Fornecer informações relativas ao estado da via navegável, ao tráfego, às condições meteorológicas, aos níveis da água e ao gelo para os serviços de informações da via navegável;

(b) Possibilitar a tradução automática dos dados mais importantes neles contidos, utilizando um vocabulário normalizado baseado em listas de códigos (as tabelas de referência dos NtS constantes do apêndice E);

(c) Obedecer a uma estruturação uniforme dos conjuntos de dados, facilitando a integração dos avisos nos sistemas de planificação da viagem;

(d) Assegurar a compatibilidade com a estrutura dos dados do Índice RIS e do ECDIS-Fluvial, facilitando a integração dos NtS no ECDIS-fluvial tal como dispõe a Diretiva 2005/44/CE, de 7 de setembro de 2005, relativa a serviços de informação fluvial (RIS) harmonizados nas vias navegáveis interiores da Comunidade.

As especificações técnicas dos avisos à navegação facilitam o intercâmbio de dados entre os sistemas NtS dos diferentes países e a transmissão para outras aplicações que utilizam dados NtS, incluindo o ECDIS-fluvial.

Algumas informações contidas nas mensagens NtS podem ser normalizadas, mas outras não.

A normalização deve abranger a informação:

(a) Importante para a segurança da navegação interior (por exemplo: embarcação de pequeno porte afundada no corredor direito da via navegável do Danúbio, ao quilómetro 2010);

(b) Necessária para a planificação da viagem, nomeadamente o encerramento de eclusas ou a redução da altura livre.

As informações adicionais que não sejam pertinentes para a segurança ou para a planificação da viagem, incluindo o motivo do encerramento de uma eclusa, podem ser fornecidas em texto livre, sem tradução automática. O texto livre deve ser limitado ao mínimo.

**2. TRANSMISSÃO DE AVISOS À NAVEGAÇÃO**

Os Estados-Membros devem assegurar que as mensagens NtS estão acessíveis em linha e através de um serviço Web NtS normalizado, em conformidade com as especificações técnicas descritas no presente anexo e respetivos apêndices. As especificações normalizadas do serviço Web NtS são apresentadas no apêndice D sob a forma de uma linguagem para descrição de serviços web (Web Service Description Language — WSDL).

Os serviços Web NtS normalizados devem oferecer ao utilizador a funcionalidade de seleção de mensagens com base em pelo menos um dos seguintes critérios:

(a) Um troço específico de uma via navegável;

(b) Um troço específico de uma via navegável definido pela baliza quilométrica dos extremos;

(c) Um período de validade do aviso (data de início e de fim do período de validade);

(d) As datas de publicação dos avisos (data e hora de publicação).

As mensagens NtS que obedecem às normas constantes do presente anexo podem ser transmitidas, entre outros meios, através de:

(a) Aplicações móveis (apps);

(c) Correio eletrónico.

Pode haver intercâmbio de dados entre os sistemas NtS utilizados em diferentes países. Todos os sistemas que utilizam as normas constantes do anexo do presente regulamento podem integrar NtS de outros sistemas nos seus próprios serviços, desde que o conteúdo da mensagem não seja alterado. Os utilizadores devem ser informados caso a ligação a uma fonte de NtS integrados seja interrompida ou não esteja disponível.

**3. TIPOS DE MENSAGENS NTS**

Os avisos à navegação são mensagens essenciais tão normalizadas quanto possível.

Existem quatro tipos de mensagens NtS, a saber:

(a) Mensagens relativas à via navegável e ao tráfego (FTM);

(b) Mensagens relativas à água (WRM);

(c) Mensagens relativas ao gelo (ICEM);

(d) Mensagens relativas às condições meteorológicas (WERM).

**4. ESTRUTURA DOS NTS E CODIFICAÇÃO DE MENSAGENS NTS**

Descreve-se neste capítulo a estrutura e a codificação dos avisos à navegação eletrónicos normalizados.

Um aviso à navegação (NtS) é uma mensagem estruturada que utiliza elementos normalizados, sempre que possível. O texto livre deve ser limitado ao mínimo nos elementos informativos.

No apêndice C apresenta-se o esquema normalizado de Linguagem de Marcação Expansível (esquema XML), designado na presente norma por XSD, utilizado nos NtS, o qual contém os valores normalizados dos códigos e os possíveis formatos.

Os valores normalizados dos códigos e os marcadores (tags) XML, o seu significado e a sua tradução são apresentados nas tabelas de referência dos NtS constantes do apêndice E e estão igualmente disponíveis em formato eletrónico no Sistema Europeu de Gestão de Dados de Referência (European Reference Data Management System — ERDMS) gerido pela Comissão Europeia.

**4.1. Estrutura geral**

Uma mensagem NtS é constituída pelas seguintes secções:

(a) Uma secção «identificação»;

(b) Uma secção que define o(s) objeto(s) ou troço(s) de via navegável a que a mensagem diz respeito;

(c) A(s) restrição(ões) nas mensagens relativas à via navegável e ao tráfego, as medições nas mensagens relativas à água, o estado do gelo nas mensagens relativas ao gelo ou o(s) comunicado(s) meteorológico(s) nas mensagens relativas às condições meteorológicas.

**Figura 1**

**Estrutura dos avisos à navegação**

image

**4.1.1. Secção «identificação»**

Cada mensagem deve conter uma secção «identificação» com informações de caráter geral sobre o emissor e a data de publicação da mensagem.

**4.1.2. Mensagem relativa à via navegável e ao tráfego**

As mensagens relativas à via navegável e ao tráfego contêm informações sobre troço(s) ou objeto(s) da via navegável e são utilizadas para indicar restrições com as seguintes finalidades:

(a)

«Alerta»: relevante para a segurança. O alerta deve conter pelo menos uma restrição de que resultem perigos diretos e concretos para pessoas, embarcações ou instalações, tais como trabalhos de soldadura numa ponte que produzam faíscas, uma gaiola de inspeção ou trabalhadores suspensos de uma ponte, um obstáculo na via navegável, etc.,

(b)

«Comunicado»: relevante para a planificação da viagem ou para a segurança. O comunicado pode conter restrições, como a obstrução da caldeira de uma eclusa devido a trabalhos de manutenção ou a dragagem da via navegável,

(c)

«Serviço de informação»: informações de caráter geral não diretamente relacionadas com a planificação da viagem ou a segurança. O serviço de informação não deve conter restrições específicas, pelo que não é diretamente relevante para a planificação da viagem ou para a segurança. Pode incluir informações gerais como as regras de tráfego locais ou uma atualização do ECDIS-fluvial.

**4.1.3. Mensagem relativa à água**

A secção «água» contém valores ou previsões referentes:

(a) Aos níveis da água,

(b) À profundidade mínima medida,

(c) À altura livre,

(d) Ao status das barragens,

(e) Às descargas,

(f) Ao regime.

Em geral, as informações relativas à água são criadas e publicadas automaticamente com base nos dados recebidos de sensores (como os mareómetros), sistemas (como os modelos do nível da água) ou infraestruturas (como o status das barragens). A publicação pode ser desencadeada por diferentes fatores, tais como a periodicidade ou a chegada a determinado valor.

**4.1.4. Mensagem relativa ao gelo**

As mensagens relativas ao gelo contêm informações sobre a presença efetiva ou prevista de gelo em troços da via navegável. Tais informações são normalmente produzidas por pessoal competente com base na observação no local e numa avaliação profissional.

**4.1.5. Mensagem relativa às condições meteorológicas**

As mensagens relativas às condições meteorológicas contêm informações sobre as condições (de perigo) para a navegação interior.

Estas mensagens podem ser publicadas para facilitar a transmissão de informações produzidas pelas redes hidrometeorológicas à navegação.

**4.2. Explicação dos marcadores XML e dos valores dos códigos constantes das tabelas de referência dos avisos à navegação (NtS)**

O significado dos diversos elementos utilizados no esquema XML (XSD) dos NtS é descrito nas tabelas de referência NtS constantes do apêndice E. A estrutura, o formato e os valores possíveis de todos os elementos XML são descritos no XSD dos NtS no apêndice C.

(a) A latitude e a longitude são codificadas de acordo com o sistema geodésico mundial de 1984 (WGS 84) e indicadas em graus e minutos, com pelo menos três (preferivelmente quatro) casas decimais ([g]g mm.mmm[m] N, [g][g]g mm.mmm[m] E).

(b) Nos campos numéricos, o separador decimal é o ponto («.»). Não se utilizam separadores de milhares.

(c) Nos avisos à navegação, admitem-se apenas as seguintes unidades de medida para os valores incluídos na mensagem XML: cm, m3/s, h, km/h e kW, m/s (vento), mm/h (chuva) e grau Celsius. As aplicações nacionais podem converter as unidades de medida para torná-las mais compreensíveis.

**4.3. Identificação de troços de via navegável e objetos nas mensagens NtS**

A fim de cumprir os requisitos mínimos em matéria de dados no que diz respeito à transmissão de informações sobre os objetos relevantes para a navegação interior, tal como referidos no artigo 4.º, n.º 3, alínea a), da Diretiva 2005/44/CE, deve utilizar-se o código ISRS de local (ISRS location code) na secção «objeto». O código ISRS de local é utilizado para identificar inequivocamente objetos e troços de via navegável e para assegurar a interoperabilidade dos sistemas e serviços RIS (por exemplo, a combinação de informações sobre as infraestruturas provenientes do Índice RIS, do ECDIS-fluvial e dos NtS, para a planificação da viagem).

O código ISRS de local consiste num código alfanumérico com 20 dígitos utilizado para estabelecer uma relação única e normalizada entre objetos nos serviços de informação fluvial. É composto pelos seguintes elementos informativos obrigatórios, organizados em quatro blocos:

(a) Bloco 1: UN/LOCODE (5 carateres alfanumérico), compreendendo,

— Código de país (2 dígitos, alfanumérico) (

3

) e

— Código de local (3 dígitos, alfanumérico, «XXX» se não estiver disponível)

(b) Bloco 2: Código de troço de via navegável (5 dígitos, alfanumérico, a determinar pela autoridade nacional)

(c) Bloco 3: Código de referência de objeto (5 dígitos, alfanumérico, «XXXXX», se não estiver disponível)

(d) Bloco 4: Hectómetro do troço da via navegável (5 dígitos, numérico, hectómetro no centro da área ou «00000», se não estiver disponível).

Os códigos ISRS de local e os dados de referência dos objetos são mantidos pelos Estados-Membros no Índice RIS e comunicados ao ERDMS, gerido pela Comissão Europeia, em conformidade com os procedimentos de manutenção do Índice RIS publicados no sítio Web do ERDMS.

**4.4. Regras de codificação das mensagens NtS**

As mensagens NtS devem ser codificadas em conformidade com o Guia de Codificação de NtS para Editores (apêndice A) e com o Guia de Codificação de NtS para Informáticos (anexo B).

GUIA DE CODIFICAÇÃO DE AVISOS À NAVEGAÇÃO PARA EDITORES

ÍNDICE

**Abreviaturas**

| Abreviatura | Significado |
|---|---|
| CEVNI | European Code for Inland Waterways (Código Europeu das Vias de Navegação Interior) (http://www.unece.org/trans/main/sc3/sc3res.html) |
| ENC/CNE | Carta náutica eletrónica |
| FTM: | Mensagem relativa à via navegável e ao tráfego |
| ICEM: | Mensagem relativa ao gelo |
| ECDIS-fluvial | Sistema de informação e apresentação de cartas náuticas eletrónicas para a navegação interior |
| Código ISRS de local | Código de local da «International Ship Reporting Standard» (norma internacional de notificação de navios) |
| NtS | Avisos à navegação |
| RIS | Serviços de informação fluvial (River Information Services) |
| VHF | Banda móvel marítima |
| WERM: | Mensagem relativa às condições meteorológicas |
| WRM | Mensagem relativa à água |
| WSDL | Web Services Description Language (linguagem para descrição de serviços Web) |
| XML | Extended Markup Language (Linguagem de Marcação Expansível) |
| XSD | XML Schema Definition (definição de esquema XML) |

**1. Antecedentes, estrutura e finalidade dos guias de codificação de NtS**

A Norma NtS é continuamente melhorada e um dos principais progressos foi o lançamento do serviço Web NtS, que facilitou o intercâmbio de mensagens entre as autoridades e entre estas e os utilizadores de NtS.

Foram elaborados dois documentos para facilitar a codificação harmonizada das mensagens NtS a nível nacional e internacional: o Guia de Codificação de NtS para Editores e o Guia de Codificação de NtS para Informáticos. Estes guias são aplicáveis ao XSD 4.0 NtS e ao serviço Web WSDL 2.0.4.0 NtS.

Tendo em conta o aumento da utilização do serviço Web NtS, há que prosseguir a harmonização das mensagens NtS para garantir a correta visualização dos conteúdos nos sistemas de terceiros. A codificação uniforme das mensagens é igualmente indispensável para que estas possam ser tidas em conta nas aplicações de planificação da viagem.

Os elementos que apenas contenham valores normalizados ou por defeito devem ser omitidos, se forem condicionais, uma vez que sobrecarregam a mensagem sem lhe trazerem qualquer valor acrescentado.

O Guia de Codificação de NtS para Editores destina-se a profissionais que editam (e publicam) mensagens NtS e inclui instruções pormenorizadas para criar os tipos de mensagens adequados, bem como uma explicação dos códigos. Explica como devem ser aplicados os quatro tipos de mensagens NtS e fornece instruções sobre a sua redação e os códigos a utilizar em determinadas circunstâncias. O Guia de Codificação de NtS para Editores está incluído no presente apêndice A.

O Guia de Codificação de NtS para Informáticos contém orientações para o desenvolvimento e a utilização de aplicações NtS, explicando a sua lógica, os processos e os valores automáticos/por defeito, e consta do apêndice B incluído no anexo do presente regulamento.

**2. Seleção do tipo de mensagem NtS**

— FTM: Este tipo deve ser escolhido quando se pretende criar uma «mensagem relativa à via navegável e ao tráfego» sobre os canais navegáveis e os objetos que neles se encontram [ir para o capítulo 3].

— WRM: Este tipo deve ser escolhido quando se pretende criar uma «mensagem relativa à água», que permite fornecer informações sobre o nível da água atual e previsto, bem como outras informações. As mensagens relativas à água contêm informações sobre objetos ou troços de via navegável. O objeto é identificado pelo seu código ISRS de local e o troço de via navegável pelos códigos ISRS de local dos seus extremos inicial e final.

— ICEM: Este tipo deve ser escolhido quando se pretende criar uma «mensagem relativa ao gelo». A secção «gelo» da mensagem contém informações sobre a presença de gelo num troço da via navegável definido pelos códigos ISRS de local dos seus extremos inicial e final.

— WERM: Este tipo deve ser escolhido quando se pretende criar uma «mensagem relativa às condições meteorológicas», que permite fornecer informações sobre as condições meteorológicas atuais e previstas num troço de via navegável definido pelos códigos ISRS de local dos seus extremos inicial e final.

**3. Considerações básicas sobre as mensagens FTM, etapas da publicação de uma FTM**

No capítulo 4, são dadas informações pormenorizadas sobre os códigos que devem ser utilizados. As considerações formuladas a partir do ponto 3.3 não seguem necessariamente a ordem de introdução de dados utilizada pelas ferramentas de edição de FTM.

3.1. É necessário publicar informações através de uma mensagem FTM de acordo com a Norma NtS? Todas as informações pertinentes para a segurança e a planificação da viagem devem ser publicadas através de mensagens NtS, embora também se possam publicar informações que não tenham tal pertinência. Cada tema/incidente/evento deve ser publicado numa mensagem separada.

3.2. Já existe uma mensagem FTM válida sobre a situação atual (em termos de conteúdo e período de validade)?

3.2.1. Sim:

a FTM já existente deve ser atualizada. A mensagem publicada em causa deve ser selecionada e atualizada na ferramenta de edição de FTM. Não é possível atualizar uma FTM que já tenha expirado.

3.2.2. Não:

é necessário elaborar uma nova FTM. Se um evento semelhante já tiver sido codificado numa FTM existente, esta pode ser utilizada como rascunho para criar uma nova FTM (se esta função estiver disponível), ou pode utilizar-se um modelo para esse efeito (se esta função estiver disponível).

3.3. A amplitude da validade geográfica deve ser determinada.

3.3.1. Se a FTM disser respeito a um troço específico de uma via navegável, esse troço deve ser incluído, sendo definido pelos seus extremos inicial e final. Se o conteúdo for aplicável a vários troços da mesma via ou de diferentes vias navegáveis, todos eles podem ser enumerados na FTM.

3.3.2. Se a FTM disser respeito a um objeto específico (p. ex., uma ponte ou uma eclusa) na via navegável, esse objeto deve ser selecionado a partir da lista de objetos disponíveis (se a seleção estiver disponível). Não há necessidade de definir um troço de via navegável na mensagem. Se uma FTM for aplicável a vários objetos, todos eles podem ser incluídos na FTM.

3.3.3. É possível combinar informações relativas a objetos e vias navegáveis numa só mensagem, desde que as informações se refiram a uma causa ou um evento específico (mesmo código de matéria e de motivo).

3.3.4. Embora as coordenadas sejam condicionais, devem ser fornecidas para facilitar a visualização nos mapas (muitas vezes estas coordenadas são automaticamente fornecidas pela aplicação NtS).

3.4. O conteúdo da FTM deve ser inserido.

Todas as informações que possam ser expressas utilizando as tabelas de referência NtS devem ser codificadas nos campos normalizados da mensagem. Só as informações adicionais (que não podem ser codificadas) devem ser introduzidas nos campos de texto livre.

3.5. Os grupos-alvo referentes ao tipo de navios e aos sentidos de tráfego em causa devem ser introduzidos, se for caso disso.

3.5.1. Caso a mensagem seja válida para todas as embarcações (todos os tipos de navios) em todos os sentidos, os grupos-alvo devem ser suprimidos para apenas serem codificadas as informações essenciais. Se a mensagem/restrição visar um grupo-alvo ou uma direção específicos, devem selecionar-se os códigos respetivos.

3.5.2. Se toda a mensagem for válida para grupos-alvo específicos, a informação relativa ao grupo-alvo deve ser fornecida na parte geral da FTM [e não repetida na(s) secção(ões) referente(s) à(s) restrição(ões)].

3.5.3. Caso existam diferentes grupos-alvo para diferentes restrições, a informação relativa aos grupos-alvo deve ser fornecida no âmbito das respetivas restrições (e não repetida na parte geral).

3.5.4. Se as autoridades competentes concederem isenções das restrições a determinados navios ou ao tráfego local (por exemplo, navios participantes num evento ao qual seja aplicável um bloqueio geral, tráfego de ferries local em zonas bloqueadas), não é necessário ter tais isenções em conta na codificação dos grupos-alvo. Essas informações podem ser inseridas no campo de texto livre reservado a informações adicionais.

3.6. Deve introduzir-se uma secção referente à comunicação, se for caso disso.

Se forem disponibilizadas informações adicionais através de uma fonte específica, esta deve ser indicada nesta secção. Se existir uma obrigação adicional de comunicação através de um meio específico, este deve ser indicado nesta secção.

3.7. A secção relativa às restrições deve ser introduzida, se for caso disso.

Se existirem restrições aplicáveis, esta secção deve ser preenchida. Se os valores associados às restrições forem conhecidos, devem ser indicados. É obrigatório fornecer os valores relativos às dimensões dos navios, ao limite de velocidade e ao espaço disponível para a navegação.

Todas as restrições devem incluir os períodos de restrição, a fim de permitir a realização dos cálculos adequados nas aplicações de planificação da viagem (para facilitar o trabalho, a aplicação NtS pode disponibilizar uma função que permita copiar os períodos de restrição ou selecionar mais de uma restrição para cada período de restrições).

3.8. Deve indicar-se a data de início da validade da mensagem.

Se já for conhecida, a data de termo da validade da mensagem deve ser igualmente indicada. A data de termo da validade não deve ser anterior à data atual.

Note-se que a informação sobre o período de validade será utilizada pelas aplicações para selecionar as mensagens, que devem poder ser visualizadas pelos utilizadores durante um determinado período.

Se o aviso for anulado:

a) antes do início do seu período de validade, é a data da anulação que deve ser indicada como data de início e data de termo;

b) e o período de validade já tiver começado, as novas datas de termo de todas as restrições devem ser remetidas para o passado e deve considerar-se que a data da anulação é a data de termo da validade.

3.9. A mensagem pode ser publicada.

**4. Explicação dos códigos das mensagens FTM**

**4.1. Subject_code (código de matéria):**

Definição da utilização de códigos de matéria:

— «Alerta»: relevante para a segurança. O alerta deve conter pelo menos uma restrição de que resultem perigos diretos e concretos para pessoas, embarcações ou instalações, tais como trabalhos de soldadura numa ponte que produzam faíscas, uma gaiola de inspeção ou trabalhadores suspensos de uma ponte, um obstáculo na via navegável, etc.,

— «Comunicado»: relevante para a planificação da viagem ou para a segurança. O comunicado pode conter restrições, como a obstrução da caldeira de uma eclusa devido a trabalhos de manutenção, a dragagem da via navegável, regras de tráfego complementares à legislação nacional, etc.,

—

«Serviço de informação»: informações de caráter geral não diretamente relacionadas com a planificação da viagem ou com a segurança. O serviço de informação não tem de conter restrições específicas e, por conseguinte, não é diretamente relevante para a planificação da viagem ou para a segurança. Pode incluir informações gerais como as regras de tráfego locais ou uma atualização do ECDIS-fluvial. O período de validade indica o período durante o qual a mensagem de serviço de informação pode ser visualizada pelos utilizadores e não o período de validade das informações fornecidas (por exemplo, 1 mês ou o tempo definido nos procedimentos nacionais).

—

«Aviso anulado»

— O código de matéria «aviso anulado» só é utilizado se

—

— a data atual for anterior à data de início da validade. Neste caso, só o conteúdo do campo «informações adicionais na língua nacional» pode ser alterado, devendo o restante conteúdo da mensagem permanecer inalterado. O código «aviso anulado» é utilizado para retirar um aviso antes de este se tornar válido. Por conseguinte, só se utiliza para avisos que não tenham atingido a data de início da validade e/ou para medidas programadas que não se irão concretizar (por exemplo, trabalhos de dragagem planeados mas que não podem ser iniciados devido a um nível alto da água).

— o período de validade já tiver começado e as novas datas de termo de todas as restrições forem remetidas para o passado. A data da anulação deve ser indicada como data de termo da validade.

— Neste caso as medidas/eventos terminam antes de terminar o período de validade inicialmente definido para uma FTM já existente.

**4.2. Reason_code (código de motivo)**

O código de motivo deve ser preenchido para fornecer informações adicionais à navegação.

Definição da utilização dos códigos de motivo:

| obras de construção | Comunicado de obras de construção |
|---|---|
| acidente | Alerta de acidente |
| alterações da via navegável | Comunicado de alterações da via navegável |
| mudança da sinalização | Comunicado de alteração da sinalização das vias navegáveis |
| estrangulamento da via navegável | Comunicado de redução da largura da via navegável se nenhum outro motivo (reason_code) for aplicável |
| marcas/sinais danificados | Comunicado de existência de marcas/sinais danificados |
| mergulhador debaixo de água | Alerta de mergulhador debaixo de água |
| dragagem | Comunicado de trabalhos de dragagem |
| evento | Comunicado de eventos, por exemplo, competições de natação, vela ou remo. |
| exercícios | Comunicado de exercícios, por exemplo, exercícios de salvamento ou militares |
| operação de desminagem | Comunicado de operação de desminagem |
| regime de descarga máximo | Comunicado de débitos de descarga superiores ao normal através dos diques ou eclusas por razões de gestão da água |
| queda de materiais | Comunicado de quedas de materiais, por exemplo, estalactites de gelo e ramos de árvores |
| ecos radar falsos | Comunicado de possibilidade de emissão de ecos radar falsos |
| fogo-de-artifício | Comunicado de fogo-de-artifício |
| material flutuante | Comunicado de materiais flutuantes acima do nível da água (visíveis) e abaixo do nível da água (invisíveis) |
| medição dos caudais | Comunicado de trabalhos de medição |
| risco para a saúde | Alerta ou comunicado sobre, por exemplo, processionárias do carvalho, fugas de gás, etc. |
| linha de alta tensão | Comunicado de cruzamento com um cabo de alta tensão |
| nível alto da água | Comunicado de situação de nível alto da água antes de ser atingido o nível da água que impossibilita a navegação |
| gelo | Comunicado de gelo; serão enviadas informações adicionais através de uma mensagem relativa ao gelo |
| Atualização do ECDIS-fluvial | Serviço de informação sobre uma atualização do ECDIS-fluvial |
| inspeção | Comunicado de trabalhos de inspeção; unicamente utilizado em caso de inspeção e não para obras de reparação/construção. Pode haver restrições devido a veículos/gaiolas ou andaimes utilizados na inspeção |
| lançamento | Comunicado de saída de um navio da doca |
| regras de tráfego locais | Serviço de informação sobre regras suplementares ou alterações da legislação ou regulamentação em vigor sem restrições especiais, datas de restrição ou datas de validade |
| nível baixo da água | Comunicado de situação de nível baixo da águaantes de ser atingido o nível de água que impossibilita a navegação |
| descida do nível da água | Comunicado de descida controlada do nível da água por motivos de inspeção, obras ou gestão da água |
| regime de descarga mínimo | Comunicado de débitos de descarga inferiores ao normal através dos diques ou eclusas por razões de gestão da água |
| novo objeto | Comunicado de informação sobre um novo objeto disponível, por exemplo, uma ponte ou um cais |
| obstáculo | Comunicado de altura livre reduzida e/ou de redução da largura da via navegável devido a um obstáculo acima do nível da água |
| obstrução debaixo de água | Comunicado de redução da profundidade disponível e/ou da largura da via navegável devido a um obstáculo debaixo de água |
| nível de água que impossibilita a navegação | Comunicado de nível de água (alto ou de estiagem) que impossibilita a navegação |
| cobertura rádio | Comunicado sobre a cobertura rádio |
| remoção de objeto | Comunicado acerca de objetos removidos |
| reparação | Comunicado de que algo está danificado ou fora de serviço e tem de ser reparado, por exemplo, um sistema de controlo de eclusas; também pode ser utilizado para reparações programadas |
| subida do nível da água | Aviso de subida dos níveis da água por razões naturais e não devido à gestão da água |
| assoreamento | Comunicado de redução da profundidade disponível devido a assoreamento |
| trabalhos de sondagem | Comunicado de trabalhos de sondagem |
| sinalização especial | Comunicado de utilização de sinalização especial, por exemplo, para bloquear zonas aquáticas ou de pesca |
| transporte especial | Comunicado de transportes especiais |
| greve | Comunicado de greve do pessoal de exploração com impacto na disponibilidade das infraestruturas das vias navegáveis |
| nível da água que obriga a navegação prudente | Comunicado de nível da água (alto ou baixo) que obriga a navegação prudente |
| obras | Comunicado de obras de caráter geral em objetos, nas margens e/ou no leito das vias navegáveis (rios ou canais) |
| restrições | A utilizar unicamente como indicação de restrições existentes se não houver nenhum outro código de motivo aplicável |
| outros | Não deve ser utilizado. Se nenhum outro código do motivo for adequado, este campo não deve ser preenchido. |

**4.3. Limitation_code (Tipo de restrição):**

Definição da utilização de códigos relativos ao tipo de restrição:

— obstrução:

— Quando é impossível a navegação:

—

— através de uma caldeira,

— através da abertura de uma ponte,

— através de um ponto específico da via navegável,

— num troço específico da via navegável.

— obstrução parcial:

— Todas as partes das infraestruturas (por exemplo, caldeiras de eclusas, aberturas de pontes) devem possuir um ISRS Location Code próprio. Caso tais códigos ainda não existam, pode utilizar-se o código de obstrução parcial quando a navegação estiver limitada mas ainda for possível (por exemplo, se só parte de uma eclusa com duas caldeiras paralelas estiver disponível)

—

— numa ou mais caldeiras de uma eclusa, havendo pelo menos uma aberta,

— através de uma ou mais aberturas de ponte, havendo pelo menos uma aberta.

— interrupção do serviço:

— a utilizar caso uma ponte móvel não esteja operacional num determinado período, durante o horário normal de serviço.

— A interrupção de serviço de uma ponte móvel significa que ainda é possível passar sob a ponte, caso contrário trata-se de uma «obstrução». A interrupção do serviço de uma eclusa deve ser codificada como «obstrução».

— mudança de serviço:

— a utilizar em caso de alteração, prolongamento ou redução do horário normal de serviço de objetos [por exemplo, eclusas ou pontes (móveis)].

— Caso existam restrições relacionadas com as dimensões permitidas do navio/comboio (não diretamente relacionadas com as infraestruturas), a restrição deve ser codificada com os seguintes elementos textuais:

—

— calado (embarcação),

— boca (embarcação),

— largura do comboio,

— comprimento (embarcação),

— comprimento do comboio,

— altura acima linha de água (embarcação).

— Se existir um valor absoluto, deve ser fornecido.

— Se existirem restrições relacionadas com a dimensão disponível de um objeto ou de um troço de via navegável, utilizam-se os seguintes códigos:

—

— altura livre,

— comprimento disponível,

— largura livre,

— profundidade disponível.

— Se existir um valor absoluto, deve ser fornecido.

— profundidade mínima medida: deve utilizar-se caso a profundidade possa causar problemas (por exemplo, devido a assoreamento). Deve ser fornecido um valor para a profundidade absoluta (em relação a um valor de referência) ou para a redução da profundidade. Se existir um valor absoluto, este deve ser indicado.

— demora: a utilizar em caso de obstrução/incidente com uma duração limitada, num objeto ou num troço da via navegável, entre determinadas datas de início e de fim.

— A duração máxima estimada da obstrução/incidente deve ser codificada. Não se deve utilizar o código de «demora» quando uma de várias caldeiras de uma eclusa não está disponível.

— Em caso de proibição de manobras ou ações específicas, devem codificar-se as respetivas restrições. Estas restrições só podem ser codificadas se não estiverem já anunciadas através de sinais de navegação ou de regulamentos codificados nas CNEF oficiais:

—

— potência mínima,

— sentido alternado

— proibição de inverter marcha,

— proibição de passar,

— proibição de cruzar ou ultrapassar,

— proibição de atracar,

— proibição de amarrar,

— proibição de ancorar,

— não causar ondulação,

— limite de velocidade,

— proibição de ir a terra.

— Se disponível, deve ser fornecido um valor absoluto para o limite de velocidade e a potência mínima.

— atenção especial: Se a FTM (ou parte de uma FTM) estiver relacionada com um canal/via navegável, esta restrição deve ser utilizada para indicar a localização da via navegável/rio/canal/lago onde ocorre um incidente.

— Além disso, deve ser utilizada nos casos em que a restrição não possa ser descrita em pormenor, mas se afigure útil ou necessário advertir ou informar os comandantes de embarcações de que devem acompanhar e prestar atenção às informações transmitidas via rádio.

— sem restrições: utilizar apenas se for necessário declarar expressamente que não existem restrições durante um determinado período.

**4.4. Limitation interval_code: Definição da utilização dos códigos de intervalo:**

— «contínuo»: deve utilizar-se para as restrições aplicáveis a partir de uma data/hora de início até uma data/hora de termo sem interrupção (por exemplo, uma obstrução de 01.01.2016, às 00h00, até 31.03.2016, às 23h59, mas também uma obstrução em 17.09.2016 das 08h00 até às 18h00).

— «diário»: deve utilizar-se para a aplicação regularmente repetida de uma restrição (por exemplo, proibição de criar ondulação durante as horas de serviço num local de dragagem — 07.04.2016 até 11.04.2016, todos os dias, entre as 06h00 e as 18h00).

— período diurno (tal como definido no Código Europeu das Vias de Navegação Interior — CEVNI): O termo «dia» designa o período entre o nascer e o pôr do sol.

— período noturno (tal como definido no CEVNI): O termo «noite» designa o período entre o pôr do sol e o nascer do sol.

— Dias da semana: se existirem intervalos relacionados com diferentes dias da semana, estes devem ser selecionados de entre os seguintes elementos textuais:

—

— segunda,

— terça,

— quarta,

— quinta,

— sexta,

— sábado,

— domingo,

— segunda a sexta,

— sábado e domingo.

— «com visibilidade reduzida»: deve utilizar-se se a restrição só estiver em vigor em condições de visibilidade reduzida devido a nevoeiro, bruma, neve, chuva ou outros motivos.

— «excetuando»: não deve ser utilizado; os intervalos de interrupção devem ser indicados como períodos de restrição distintos dentro da mesma restrição. Isto deve-se ao facto de o software de planificação da viagem não ser capaz de interpretar este código corretamente como uma indicação de não aplicação da restrição na data ou hora em causa. Em consequência, não é possível calcular adequadamente as ETA (horas de chegada previstas).

— «segunda a sexta exceto feriados»: só deve ser utilizado se houver dias feriados durante o período de validade da restrição. A título de serviço aos utilizadores, os feriados podem ser indicados na secção de texto livre da FTM. O software de planificação da viagem não consegue ter em conta os feriados nacionais para calcular as ETA.

**4.5. Indication_code (indicação de restrição):**

O indication_code destina-se a ser utilizado para fornecer informações sobre valores específicos respeitantes a certas restrições (por exemplo, limite de velocidade, potência mínima ou profundidade disponível). A fim de determinar certas dimensões, é necessário tomar como referência um sistema de referência externo (geográfico ou hidrológico) (por exemplo, altura livre, profundidade disponível ou profundidade mínima medida) ou as dimensões conhecidas de estruturas artificiais (por exemplo, o comprimento disponível ou a largura livre).

4.5.1. Se as dimensões absolutas ou as referências forem conhecidas, devem ser utilizadas. Só se devem utilizar valores relativos se não for possível tomar como referência um sistema de referência externo.

4.5.2.

| reduzido de | → trata-se de um valor relativo |
|---|---|

4.5.3.

| máximo | → trata-se de um valor absoluto |
|---|---|

4.5.4.

| mínimo | → trata-se de um valor absoluto |
|---|---|

4.5.5. Se a dimensão indicadora de uma restrição se referir a uma coordenada geográfica ou hidrológica, deve indicar-se o sistema de referência respetivo na mensagem NtS (por exemplo, altura livre mínima de 4 m em relação ao nível máximo navegável; profundidade disponível mínima de 1,7 m relativamente ao caudal de estiagem regulamentado)

4.5.6. Se a dimensão indicadora de uma restrição se referir à dimensão de uma estrutura artificial (por exemplo, ponte ou eclusa), a referência pode ser dada em relação às dimensões conhecidas (por exemplo, altura livre reduzida em 1,5 m, comprimento disponível reduzido em 27 m).

**4.6. Position_code (Localização) dos objetos:**

Sempre que possível, o Position_code deve referir-se ao corredor do canal navegável onde o objeto está localizado em relação ao eixo do canal navegável (esquerdo/centro/direito) ou a outras informações comummente conhecidas (objeto antigo/novo) ou a direção geográfica (norte/sul/leste/oeste). O «position_code» dos objetos pode ser automaticamente preenchido com base nos dados de referência do Índice RIS. O corredor esquerdo/direito do canal navegável é definido olhando para jusante.

**4.7. Position_code (Localização) dos canais/vias navegáveis:**

O Position_code não é fornecido no caso das FTM (ou parte de FTM) relativas a um canal ou uma via navegável. Para indicar em que corredor da via navegável/canal/rio/lago ocorre um incidente, utiliza-se a restrição «precaução especial» conjugada com o «Position_code» da restrição adequado.

**4.8. Position_code (Localização) das restrições:**

4.8.1. Sempre que possível, o Position_code deve referir-se ao corredor do canal navegável ou ao lado do objeto em que a restrição ocorre (esquerdo/direito). O corredor esquerdo/direito do canal navegável é definido olhando para jusante.

4.8.2. O Position_code deve direcionar a atenção do condutor para o corredor do canal onde se encontra, por exemplo, uma zona de especial interesse, um perigo ou um obstáculo. Por conseguinte, basta uma indicação aproximada (por exemplo, margem esquerda — corredor esquerdo — corredor do meio — corredor direito — margem direita). Não está prevista uma subdivisão mais precisa.

4.8.3. Se forem necessárias informações de localização mais precisas, estas devem ser preferencialmente fornecidas através de mapas ou esquemas (ficheiro agregado, ver capítulo 3.6)

4.8.4. Nos troços em que não se afigure adequado indicar a localização por corredor do canal navegável (esquerdo/direito) como habitualmente (por exemplo, bacias portuárias, certos troços de canal que não têm um sentido do caudal claro), utilizam-se os pontos cardeais (norte/leste/sul/oeste).

**4.9. Target_group_code (código dos destinatários) (ver capítulo 3.5)**

**4.10. Reporting_code (regime de transmissão)**

4.10.1. O Reporting_code só deve ser, em regra, utilizado em caso de necessidade especial de comunicação (p. ex., obrigação adicional de notificar a autoridade local no que diz respeito ao tráfego local) ou se houver informações complementares disponíveis (por exemplo, ponto de contacto VHF como o nome do canal ou o indicativo de chamada da posição atual de uma draga) com relevância direta para a FTM.

4.10.2. Devem evitar-se repetições de rotina dos dados de comunicação publicamente disponíveis (por exemplo, números de telefone das autoridades locais, canais VHF das eclusas, etc.) se não houver uma causa direta para essa comunicação no que se refere à FTM.

4.10.3. Os meios de comunicação geralmente aplicáveis de acordo com a regulamentação oficial (por exemplo, comunicações VHF navio-navio e navio-terra, conforme estabelecido pelo CEVNI ou pelas regras regionais ou nacionais de navegação) não devem, por norma, ser repetidos pelo «Reporting_code» se não houver uma causa direta para essa comunicação no que se refere à FTM).

**4.11. Communication_code (meio de comunicação)**

deve utilizar-se o seguinte formato (exemplos):

— «Número, indicativo de chamada» VHF: «10, Schifffahrtsaufsicht Wien»

— Número de telefone ou Fax: «+43123456789, Schifffahrtsaufsicht Wien»

— Endereço Internet: «http://example.com»

— Sinalização acústica: «long blast / langer Ton»

— Correio eletrónico: «example@authority.eu»

— Número da caixa postal EDI: «900012345@edi.bics.nl»

— Teletexto: «ARD, 992-995»

**4.12. Type_code (Tipo de via navegável):**

Uma via navegável é um canal, um lago ou um rio.

— fundeadouro

— margem

— baliza

— cais

— posto fronteiriço

— ponte

— ponte a abrir

— boia

— cabo aéreo

— canal [o termo «canal» é utilizado quando uma mensagem disser respeito a todo o canal (e não apenas à via navegável)]

— ponte-aqueduto: aqueduto

— aqueduto

— canal navegável (o termo «canal navegável» refere-se à parte da via navegável que pode ser efetivamente utilizada pelos navios).

— ferry

— doca flutuante

— comporta (as comportas são utilizadas para proteger uma zona em situações de nível de água alto)

— porto

— instalação portuária

— capitania do porto

— lago [o termo «lago» é utilizado se uma mensagem for relativa ao lago inteiro (e não apenas ao canal navegável)]

— luz

— bacia de eclusa: caldeira individual da eclusa

— eclusa: todo o complexo da eclusa

— posto de amarração

— painel de sinalização

— conduta

— conduta aérea

— rampa

— instalação de recolha de resíduos

— ponto de notificação

— albufeira

— rio [o termo «rio» é utilizado se uma mensagem for relativa a todo o rio (e não apenas ao canal navegável)]

— elevador de navios

— estaleiro

— estação de sinalização

— terminal

— fluviómetro/marégrafo

— túnel

— bacia de viragem

— centro de tráfego de embarcações

— barragem (as barragens são utilizadas para controlar o nível de água nos rios)

**5. Considerações básicas sobre as mensagens WRM**

Regra geral, as mensagens relativas à água devem ser geradas automaticamente. Se tal não for possível, a produção manual de WRM deve respeitar o mais possível os processos estabelecidos para as WRM geradas automaticamente (ver Guia de Codificação de NtS para Informáticos).

**6. Considerações básicas sobre as mensagens ICEM, etapas da publicação de uma ICEM**

As mensagens relativas ao gelo dependem da observação e avaliação no local e são normalmente geradas por pessoal autorizado.

As ICEM devem ser emitidas em caso de gelo. Este não causa necessariamente restrições à navegação, mas podem ser fornecidas informações sobre a presença de gelo, mesmo que não prejudique a navegação.

6.1. É necessário publicar informações através de mensagens NtS ICEM?

A primeira mensagem relativa à presença de gelo num troço só deve ser publicada se houver gelo na via navegável ou nos seus afluentes, mesmo que não existam restrições.

6.2. Já existe uma ICEM válida para o troço de via navegável em causa?

6.2.1. Sim:

Se já existir uma mensagem (ainda) válida para o troço em causa, esta deve ser atualizada. É possível atualizar as mensagens relativas ao gelo existentes mesmo que a zona em que são aplicáveis sofra alterações (por exemplo, se o gelo se estiver a expandir, aumentando a extensão de troço afetado).

6.2.2. Não:

Caso não exista uma mensagem relativa ao gelo válida para o troço afetado, deve criar-se uma nova mensagem.

6.3. No entanto, podem ser fornecidas informações sobre uma presença de gelo que não crie obstáculos à navegação.

6.4. Uma mensagem ICEM é sempre válida para um único troço de via navegável. A área geográfica da validade deve ser fixada através da definição da via navegável e dos respetivos pontos de início e de termo (hectómetro) ou da escolha de certos troços consecutivos, dependendo da aplicação nacional).

6.5. A hora da medição deve ser indicada. O respetivo estado do gelo deve ser introduzido utilizando, pelo menos, uma das listas de códigos (em função dos requisitos nacionais).

6.5.1. Ice_condition_code (estado do gelo)

6.5.2. Ice_accessibility_code (acessibilidade do gelo)

6.5.3. Ice_classification_code (classificação do gelo)

6.5.4. Ice_situation_code (restrições devidas à presença de gelo) (este código deve ser sempre indicado para permitir que essas restrições sejam representadas num mapa utilizando as cores de um semáforo).

6.6. A ICEM pode ser publicada. As mensagens relativas ao gelo são automaticamente válidas até ao dia seguinte após a sua publicação ou pelo tempo definido nos procedimentos nacionais.

**7. Considerações básicas sobre as mensagens WERM**

Tendo em conta a grande disponibilidade de serviços Web e aplicações de previsões e alertas meteorológicos, as WERM só devem ser utilizadas para divulgar informações de importância específica para a navegação que não sejam cobertas pelos serviços de informação meteorológica geral.

Regra geral, as mensagens relativas às condições meteorológicas são geradas automaticamente. Se isso não for possível, a produção manual de WERM deve respeitar o mais possível os processos estabelecidos para as mensagens WERM geradas automaticamente (ver Guia de Codificação de NtS para Informáticos).

**8. Regras aplicáveis a determinados elementos**

**8.1. Regras para o elemento «name» relativo a objetos**

As designações de objetos são normalmente preenchidas pela ferramenta de edição NtS com base nos dados de referência do RIS Index. As designações devem ser introduzidas na língua local, pelo que também podem ser utilizados, por exemplo, diacríticos ou carateres cirílicos (caso, por exemplo, de Baarlerbrücke, Volkeraksluis ou Mannswörth).

Não se devem incluir informações sobre características de funcionalidade e o tipo de objeto geográfico não deve ser repetido na designação, salvo se essa repetição acrescentar informação sobre o tipo de objeto.

Exemplo: A eclusa «Freudenau Schleuse» só deve ser designada por «Freudenau», sendo o tipo de objeto «eclusa» automaticamente aditado com base no tipo de objeto geográfico (type_code).

Exemplo: A designação de objeto da ponte ferroviária de Krems (AT) é «Eisenbahnbrücke Krems». A informação «ponte ferroviária» está incluída nesta designação, uma vez que acrescenta informações adicionais ao «type_code»«ponte».

Exemplo: A designação de objeto de uma ponte em Linz (AT) é «Nibelungenbrücke». O termo «Brücke» permanece nessa designação porque faz parte do próprio nome da ponte.

Exemplo: O fluviómetro «Pegelstelle Wildungsmauer» é designado por «Wildungsmauer» porque a informação de que esse objeto é um fluviómetro já está codificada no «type_code».

Se um troço de via navegável for a fronteira entre dois países com línguas diferentes, a denominação nacional do objeto pode ser indicada em ambas as línguas (por exemplo, «Staatsgrenze AT-SK/Statna hranica AT-SK»).

**8.2. Regras para o elemento «name» relativo às vias navegáveis**

As designações das vias navegáveis são normalmente preenchidas pela ferramenta de edição NtS com base nos dados de referência do RIS Index. O campo «name» deve incluir o nome local do respetivo troço de canal navegável (por exemplo, «Rhein»). Dependendo dos processos nacionais, poderá ser possível editar a designação do canal navegável para incluir os nomes normalmente utilizados a nível local ou fazer aditamentos (por exemplo, «Rhein am Deutschen Eck»).

**8.3. Regras relativas aos elementos «value» e «unit» utilizados nas restrições**

Salvo indicação em contrário, nas mensagens NtS só podem ser utilizadas as seguintes unidades de medida: cm, m3/s, h, km/h e kW, m/s (vento), mm/h (chuva) e grau Celsius.

GUIA DE CODIFICAÇÃO (NTS ENCODING GUIDE) DE AVISOS À NAVEGAÇÃO PARA INFORMÁTICOS

ÍNDICE

**1. Antecedentes e Estrutura**

Os avisos à navegação (NtS) eram aplicados em diversos países europeus, com base no Regulamento (CE) n.º 416/2007 da Comissão, relativo às especificações técnicas dos avisos à navegação a que se refere o artigo 5.º da Diretiva 2005/44/CE do Parlamento Europeu e do Conselho. A norma NtS é continuamente melhorada e um dos principais progressos foi o lançamento do Serviço Web NtS, que facilitou o intercâmbio de mensagens NtS entre as diversas autoridades, bem como entre estas e os utilizadores de NtS. Outro progresso foi a utilização do XSD 4.0 para NtS, que simplifica a codificação das mensagens NtS.

**1.1. Objetivo do Guia de Codificação de NtS — NtS Encoding Guide**

O Guia de Codificação de NtS explica como devem ser aplicados os quatro tipos de mensagens NtS e os códigos a utilizar caso se verifiquem determinados acontecimentos. Fornece aos editores de NtS instruções sobre a elaboração das mensagens NtS, permitindo, assim, a sua codificação harmonizada a nível nacional e internacional.

Tendo em conta o aumento da utilização do serviço Web NtS, há que prosseguir a harmonização das mensagens NtS para garantir a correta visualização dos conteúdos nos sistemas de terceiros. A codificação uniforme das mensagens é igualmente indispensável para que estas possam ser tidas em conta nas aplicações de planificação da viagem. A versão 1.0 do Guia de Codificação de NtS é aplicável ao XSD 4.0 para NtS e ao Serviço Web WSDL 2.0.4.0 para NtS.

**1.1.1. Guia de Codificação de NtS para Editores**

O Guia de Codificação de NtS para Editores destina-se ao pessoal que edita (e publica) mensagens NtS, incluindo instruções pormenorizadas sobre a criação dos tipos de mensagens adequados, bem como uma explicação dos códigos. Inclui igualmente informações relevantes para os informáticos.

**1.1.2. Guia de Codificação de NtS para Informáticos (presente documento)**

O Guia de Codificação de NtS para Informáticos inclui orientações para a execução de aplicações NtS que explicam a lógica, os processos e os valores automáticos/por defeito.

**2. Mensagens NtS e respetivas secções**

Uma mensagem NtS é constituída por:

— uma secção «identificação»

— uma secção que define o(s) objeto(s) ou troço(s) de via navegável a que a mensagem diz respeito;

— uma ou mais das secções a seguir enumeradas, em função do tipo de mensagem:

—

— a(s) restrição(ões) no caso das mensagens relativas à via navegável e ao tráfego,

— a(s) medições, no caso das mensagens relativas ao nível da água,

— as condições do gelo, no caso das mensagens relativas ao gelo,

— os boletins meteorológicos no caso das mensagens relativas às condições meteorológicas.

**Figura 2**

image

A secção «identificação» é obrigatória e inclui informações de caráter geral sobre a entidade de origem, o remetente, a data de emissão, o país e língua de origem. Acompanha um dos quatro tipos de secções das mensagens NtS:

— Secção relativa à via navegável e ao tráfego: uma «mensagem relativa à via navegável e ao tráfego» (FTM) é geralmente criada pelos editores NtS de acordo com o Guia de Codificação de NtS para Editores. Está relacionada com troços de vias navegáveis (definidos pelos seus códigos ISRS de local de início e de termo) e/ou com objetos presentes na via navegável, definidos pelo respetivo código ISRS de local [ir para capítulo 6].

— Secção relativa ao nível da água: uma «mensagem relativa à água» (WRM) facilita o fornecimento de informações sobre os níveis de água atuais e previstos, bem como outras informações. Normalmente as WRM são criadas automaticamente (e periodicamente) com base nas medições de sensores ou no estado das infraestruturas, não exigindo qualquer interação com o editor de NtS. A secção de mensagens relativas à água contém informações sobre um objeto (por exemplo, estação hidrométrica) ou um troço de via navegável (por exemplo, a profundidade mínima medida ou o regime aplicável num determinado troço). O objeto é identificado pelo seu código ISRS de local e o troço de via navegável pelos códigos ISRS de local dos seus extremos inicial e final [ir para capítulo 3].

— Secção relativa ao gelo: uma «mensagem relativa ao gelo» (ICEM) contém informações sobre o estado do gelo num troço da via navegável definido pelos códigos ISRS de local dos seus extremos inicial e final [ir para capítulo 4].

— Secção relativa às condições meteorológicas: uma «mensagem relativa às condições meteorológicas» (WERM) permite fornecer informações sobre as situações meteorológicas atuais e previstas num troço de via navegável definido pelos códigos ISRS de local dos seus extremos inicial e final. [ir para capítulo 5].

Além disso, o ISRS Location Code (código de local da International Ship Reporting Standard) é utilizado para definir o(s) objeto(s) ou troço(s) de via navegável a que a mensagem é aplicável.

O código ISRS de local é definido no ponto 4.3 do anexo do presente regulamento.

**3. Considerações básicas sobre as mensagens WRM**

As informações sobre o nível da água têm grande importância para a planificação e a segurança da viagem. Atualmente, não existe qualquer norma comum para a expressão destes dados. A graduação dos fluviómetros é feita por referência a diferentes níveis da água do mar ou a pontos específicos. Para fornecer uma referência adequada, deve indicar-se sempre a respetiva referência (reference_code) juntamente com o valor. As WRM podem ser utilizadas para fornecer as seguintes informações:

— Nível da água (incluindo previsões),

— Profundidade mínima medida (incluindo previsões),

— Altura livre (incluindo previsões),

— Descargas (incluindo previsões),

— Status das barragens,

— Regime.

São fornecidos esclarecimentos para as traduções na folha de cálculo «reference_code» [Esclarecimentos para as traduções na folha de cálculo «reference_code» (referência)] no capítulo 7.11.

Normalmente, as mensagens WRM são automaticamente criadas e publicadas com base nas informações recebidas de sensores ou das infraestruturas (por exemplo, previsões ou status das barragens). A publicação de WRM pode ser desencadeada por diferentes fatores, tais como a periodicidade ou a chegada a determinado valor.

**3.1. Preenchimento da secção «nts_number» (número do NtS) nas WRM**

No XSD 4.0 para NtS o número do NtS é opcional no caso das mensagens WRM. Se for fornecido, cada número deve ser único (Organização/Ano/Número/Série) para cada tipo de mensagem e compete ao organismo que fornece a WRM garantir que o seu número é único (não é necessário que os números sejam consecutivos).

**3.2. Redação de mensagens WRM incluindo previsões**

A data de início (date_start) do período de validade (validity_period) deve ser preenchida com a data atual (date_issue) e a data de termo (date_end) do período de validade com a data do dia seguinte à data atual.

Para indicar as alterações, por exemplo do nível da água, de uma forma facilmente compreensível, pode inserir-se a diferença em relação a uma medição comparativa anterior na secção da WRM relativa às diferenças. Para além da alteração do valor (por exemplo, -5 [cm]), também se deve indicar o hiato temporal em relação à medição comparativa.

No caso das previsões, a data da medição («measure_date») é a data/hora para a qual a previsão é válida.

As previsões do nível da água contêm sempre um fator de incerteza. Normalmente, são calculados modelos com parâmetros diferentes (por exemplo, previsões meteorológicas), que conduzem à previsão de diferentes valores do nível da água. Para possibilitar o fornecimento de previsões dos valores mínimos e máximos, por exemplo a visualização de um intervalo de confiança de uma previsão do nível da água, incluem-se mais dois campos de dados opcionais na secção «medida» da WRM.

Na figura seguinte, apresenta-se um exemplo de intervalo de confiança de uma previsão do nível da água:

**Figura 3**

**Visualização do intervalo de confiança de uma previsão do nível da água: valor mais provável (preto), limite superior do intervalo de confiança (roxo), limite inferior do intervalo de confiança (vermelho)**

image

No XSD NtS estão disponíveis dois elementos:

<value_min> valor mínimo do intervalo de confiança

<value_max> valor máximo do intervalo de confiança

Para além dos níveis da água previstos, o intervalo de confiança também pode ser usado para referir a incerteza das informações publicadas sobre a profundidade mínima medida e a altura livre vertical.

Estes elementos «value_min» e «value_max» do intervalo de confiança permitem que o valor do intervalo de confiança seja fornecido através de mensagens NtS WRM normalizadas para ser utilizado nos gráficos. Os dados brutos não devem ser mostrados aos utilizadores da navegação fluvial (por exemplo, em formato codificado).

O tipo de informação relativa à água (measure_code) «NOM» não deve ser utilizado. Caso não exista nenhuma medição para um determinado tipo de WRM, devem omitir-se os elementos relativos ao valor se a mensagem tiver de ser enviada na mesma.

**4. Processos das mensagens ICEM**

As mensagens relativas ao gelo dependem da observação e avaliação no local e, regra geral, são geradas manualmente (se forem geradas automaticamente, devem seguir as regras aplicáveis à criação manual, ver Guia de Codificação de NtS para Editores).

A ICEM é publicada em relação a um determinado troço da via navegável (fairway_section) definido pelos códigos ISRS de local dos seus extremos inicial e final e indica o estado do gelo (ice_condition) numa determinada data de medição.

A validade da ICEM começa na data de publicação (automaticamente estabelecida pela aplicação NtS). A fim de evitar que a ICEM seja mostrada a utilizadores que já não sejam válidos, a data de termo da validade (date_end) deve ser preenchida automaticamente pela aplicação NtS com o dia seguinte à publicação (exceto se os processos nacionais garantirem a atribuição de uma data de termo da validade às mensagens, assim que a informação nelas incluída deixe de estar atualizada).

No Guia de Codificação de NtS para Editores descreve-se em que circunstâncias um editor de NtS cria uma nova ICEM ou atualiza uma ICEM existente. São aplicáveis os processos a seguir indicados:

**4.1. Mensagem ICEM nova**

1) As aplicações de NtS podem facultar aos editores de NtS

a. A utilização de avisos existentes como rascunhos para a criação de novas ICEM (por exemplo, se as condições do gelo forem semelhantes ao aviso existente) e/ou

b. A utilização de modelos de avisos para determinadas situações.

2) O conteúdo (por exemplo, a hora da medição ou as respetivas condições de gelo) deve ser inserido pelo editor em conformidade com o capítulo 6 do Guia de Codificação de NtS para Editores. A data e a hora da medição também podem ser estabelecidas pela aplicação de acordo com as definições nacionais.

3) Quando um editor de NtS desencadeia a ação de publicação,

a. É verificado se todos os conteúdos obrigatórios são fornecidos em conformidade com o XSD NtS (caso contrário, volta-se a 2),

b. O número do NtS (nts_number) é gerado pela aplicação NtS,

i. a «organização» é preenchida com o nome ou o código do organismo responsável, dependendo da função do utilizador que faz a publicação,

ii. o «ano» é preenchido com o ano em curso,

iii. é atribuído o «número» disponível seguinte,

iv. é atribuído o «número de série» 0.

c. A secção «date_issue» é automaticamente preenchida com a data/hora da ação de publicação,

d. A secção «validity_period» — «date_start» é automaticamente preenchida com a data de publicação efetiva,

e. A secção «validity_period» — «date_end» é automaticamente preenchida com o dia seguinte à data de publicação (exceto se os processos nacionais garantirem a atribuição de uma data de termo da validade às mensagens, assim que a informação nelas incluída deixe de estar atualizada).

**4.2. Atualização de uma mensagem ICEM existente**

1) A mensagem publicada em causa deve ser selecionada para atualização na ferramenta de edição de ICEM. A ICEM original deve ser copiada ou alterada na base de dados [dependendo dos processos nacionais). Uma ICEM expirada (que tenha passado o prazo de validade (validity_date_end)] deixa de poder ser atualizada e, nesse caso, os editores de NtS têm de criar uma nova ICEM.

2) O conteúdo (por exemplo, a hora de medição ou as respetivas condições de gelo) deve ser alterado pelo editor em conformidade com o capítulo 6 do Guia de Codificação de NtS para Editores. A data e a hora de medição também podem ser alteradas pela aplicação de acordo com as definições nacionais.

3) Quando um editor de NtS desencadeia a ação de publicação,

a. É verificado se todos os conteúdos obrigatórios são fornecidos em conformidade com o XSD NtS (caso contrário, volta-se a 2),

b. O número do NtS (nts_number) é gerado pela aplicação NtS,

i. a «organização» mantém-se inalterada,

ii. o «ano» mantém-se inalterado,

iii. o «número» mantém-se inalterado,

iv. o «número de série» é aumentado (aumento de 1)

c. A secção «date_issue» é automaticamente preenchida com a data/hora da ação de publicação

d. A secção «validity_period» — «date_start» é automaticamente preenchida com a data de publicação efetiva

e. A secção «validity_period» — «date_end» é automaticamente preenchida com o dia seguinte à data de publicação (exceto se os processos nacionais garantirem a atribuição de uma data de termo da validade às mensagens, assim que a informação nelas incluída deixe de estar atualizada).

**5. Considerações básicas sobre as mensagens WERM**

Normalmente, as WERM são criadas e publicadas automaticamente com base nas informações recebidas dos sensores ou das infraestruturas. A data de início (date_start) do período de validade (validity_period) deve ser preenchida com a data atual (date_issue) e a data de termo (date_end) do período de validade com a data do dia seguinte à data atual.

Nas WERM, a secção respeitante à via navegável é indicada como um troço da via navegável entre dois pontos da via, ou seja, o espaço de aplicação da estação meteorológica (fluviómetro).

A data e a hora da medição/previsão devem ser fornecidas, ainda que tal não seja obrigatório nas mensagens WERM.

No caso de previsões, a «data de medição» é a data/hora para a qual a previsão é válida.

**5.1. Preenchimento da secção «nts_number» nas mensagens WERM**

No XSD 4.0 para NtS o número do NtS é opcional no caso das mensagens WERM. Se for fornecido, cada número deve ser único (Organização/Ano/Número/Série) para cada tipo de mensagem e compete ao organismo que fornece a WRM garantir que o seu número é único (não é necessário que os números sejam consecutivos).

**5.2. Preenchimento da secção «weather_category_code» das mensagens WERM**

A velocidade do vento indicada nos códigos de categorização das condições meteorológicas («weather_category_code»), com valores de 0 a 12, deve ser fornecida de acordo com a escala de Beaufort publicada pela Organização Meteorológica Mundial, no seu manual sobre serviços meteorológicos marinhos «WMO-No. 558».

A visibilidade deve ser indicada nos códigos de categorização das condições meteorológicas (valores 13 a 22) tal como definido no quadro seguinte:

| Valor, significado | Visibilidade | Informações adicionais |
|---|---|---|
| 13, nevoeiro cerrado | menos de 50 metros |  |
| 14, nevoeiro denso | menos de 100 metros |  |
| 15, nevoeiro moderado | menos de 200 metros |  |
| 16, nevoeiro | menos de 1 000 metros | O nevoeiro é constituído por gotículas de água. |
| 17, névoa | de 1 km a 4 km | A névoa é constituída por gotículas de água. O termo «névoa» é utilizado em caso de «nevoeiro seco»; este fenómeno ocorre normalmente antes do nascer do sol. |
| 18, bruma | de 1 km a 4 km | A bruma é constituída por partículas secas. |
| 19, bruma leve | de 4 km a 10 km |  |
| 20, céu limpo | de 10 km a 20 km |  |
| 21, muito limpo | sem limitações da visibilidade |  |
| 22, ausência de nevoeiro |  | A expressão «ausência de nevoeiro» é utilizada para indicar que não há nevoeiro de acordo com os requisitos nacionais/locais. |

**6. Processos das mensagens FTM**

No Guia de Codificação de NtS para Editores descreve-se em que circunstâncias um editor de NtS cria uma nova FTM ou atualiza uma FTM existente. São aplicáveis os processos a seguir indicados:

**6.1. Nova FTM**

1) As aplicações de NtS podem facultar aos editores de NtS

a. A utilização de avisos existentes como rascunhos para a criação de novas FTM e/ou

b. A utilização de modelos de avisos para determinadas situações.

2) O conteúdo (por exemplo, período de validade ou restrições) tem de ser inscrito pelo editor em conformidade com os capítulos 3 e 4 do Guia de Codificação de NtS para Editores.

3) Quando um editor de NtS desencadeia a ação de publicação,

a. É verificado se todos os conteúdos obrigatórios são fornecidos em conformidade com o XSD NtS (caso contrário, volta-se a 2),

b. O número do NtS (nts_number) é gerado pela aplicação NtS,

i. a «organização» é preenchida com o nome ou o código do organismo responsável, dependendo da função do utilizador que faz a publicação,

ii. o «ano» é preenchido com o ano em curso,

iii. é atribuído o «número» disponível seguinte, caso um número específico tenha sido introduzido pelo editor de NtS ou seja retomado um processo de aplicação utilizado na etapa 2, (visto dado que cada Organização/Ano/Número/Série) é único, conforme explicado no capítulo 15.1.

iv. é atribuído o «número de série» 0

c. A secção «date_issue» é preenchida automaticamente com a data/hora efetiva da ação de publicação

**6.2. Atualização/anulação de uma FTM existente**

1) A mensagem publicada em causa deve ser selecionada para atualização na ferramenta de edição de FTM. A FTM original deve ser copiada ou alterada na base de dados (dependendo dos processos nacionais).

a. Uma FTM expirada [que tenha passado o prazo de validade (validity_date_end)] deixa de poder ser atualizada e, nesse caso, o editor de NtS tem de criar uma nova FTM.

b. O código de matéria «aviso anulado» só é utilizado se

i. A data atual for anterior ao início do período de validade (validity_date_start). Caso só seja possível alterar o conteúdo do campo «informações adicionais na língua nacional», o conteúdo codificado da mensagem (etapa 2) deve permanecer inalterado.

ii. O período de validade já tiver começado e a nova data de termo de todas as restrições já tiver passado. O fim do prazo de prescrição tem de ser indicado na data correta.

c. Se um aviso for anulado, a data final do período de validade tem de coincidir com a data da anulação.

2) O conteúdo (por exemplo, período de validade ou restrições) deve ser alterado pelo editor em conformidade com os capítulos 3 e 4 do Guia de Codificação de NtS para Editores.

3) Quando um editor de NtS desencadeia a ação de publicar,

a. É verificado se todos os conteúdos obrigatórios são fornecidos em conformidade com o XSD NtS (caso contrário, volta-se a 2),

b. O número do NtS (nts_number) é gerado pela aplicação NtS,

i. a «organização» mantém-se inalterada,

ii. o «ano» mantém-se inalterado,

iii. o «número» mantém-se inalterado,

iv. o «número de série» é aumentado (aumento de 1)

c. A secção «date_issue» é automaticamente preenchida com a data/hora da ação de publicação

d. A FTM com o código de matéria «aviso anulado» (já) não deve ser tida em conta para a planificação da viagem.

**6.3. FTM relativa à via navegável e/ou ao objeto**

Uma FTM relativa à via navegável contém informações sobre um ou vários troços da via. Um troço de via navegável é definido na secção «fairway_section» pelos códigos ISRS de local dos seus extremos inicial e final.

Uma FTM relativa a um objeto contém informações sobre um ou vários objetos específicos presentes na via navegável. Um objeto é definido na parte «objeto» pelo seu código ISRS de local.

Uma FTM deve referir-se

— a um ou vários troços da via navegável ou

— a um ou vários objetos presentes num ou vários troços de via navegável

**6.4. Ordenação automática dos códigos de restrição**

As diferentes restrições têm impactos diferentes da navegação. A fim de permitir visualizar a restrição mais grave, por exemplo, numa lista de FTM, deve respeitar-se a ordem seguinte, a partir da restrição mais rigorosa com a classificação 1:

| Classificação | Valor | Meaning (EN) |
|---|---|---|
| 1 | OBSTRU | obstrução |
| 2 | PAROBS | obstrução parcial |
| 3 | NOSERV | interrupção do serviço |
| 4 | SERVIC | mudança de serviço |
| 5 | VESDRA | calado da embarcação |
| 6 | VESBRE | largura do navio |
| 7 | CONBRE | largura do comboio |
| 8 | VESLEN | comprimento do navio |
| 9 | CONLEN | comprimento do comboio |
| 10 | CLEHEI | altura livre |
| 11 | VESHEI | altura da embarcação |
| 12 | AVALEN | comprimento disponível |
| 13 | CLEWID | largura livre |
| 14 | AVADEP | profundidade disponível |
| 15 | LEADEP | profundidade mínima medida |
| 16 | DELAY | demora |
| 17 | ALTER | sentido alternado |
| 18 | TURNIN | proibição de inverter marcha |
| 19 | PASSIN | proibição de passar |
| 20 | OVRTAK | proibição de ultrapassar |
| 21 | NOBERT | proibição de atracar |
| 22 | NOMOOR | proibição de amarrar |
| 23 | ANCHOR | proibição de ancorar |
| 24 | SPEED | limite de velocidade |
| 25 | WAVWAS | proibição de criar ondulação |
| 26 | NOSHORE | proibição de ir a terra |
| 27 | MINPWR | potência mínima |
| 28 | CAUTIO | precaução especial |
| 29 | NOLIM | sem restrições |

**6.5. Tratamento do período de restrições**

— As restrições que tenham os mesmos períodos de duração devem ser agrupadas, conjuntamente enumeradas ou combinadas para que a sua visualização seja facilmente compreensível.

— As ferramentas de edição de NtS devem disponibilizar uma função para evitar que os editores tenham de voltar a datilografar os períodos de restrição.

— Todas as restrições devem incluir o respetivo período com um código de intervalo, a fim de permitir a realização dos cálculos adequados nas aplicações de planificação da viagem. Para facilitar o trabalho dos editores de NtS podem implementar-se as funções seguintes:

—

— A ferramenta de edição de NtS pode disponibilizar uma função de cópia das restrições já inscritas para evitar que o editor de NtS tenha de voltar a datilografar o período de restrições.

— As ferramentas do editor de NtS podem disponibilizar uma função que permita selecionar mais de um código de restrição para um período específico e criar automaticamente as secções de restrição necessárias com base nas informações introduzidas pelo editor de NtS).

— Na expressão «segunda a sexta exceto feriados»: o valor «feriados» é muito difícil para as aplicações de planificação da viagem. É necessária uma lista de feriados de cada país para se fazerem cálculos corretos. Mesmo que tal lista não esteja disponível as respetivas restrições serão atribuídas aos dias feriados.

— O termo «excetuando»: não deve ser utilizado; os intervalos de interrupção devem ser indicados como períodos de restrição distintos dentro da mesma restrição, pelo que este código não deve ser mostrado/disponibilizado aos editores de avisos.

— Lógica e visualização da informação aplicável no caso do código de intervalo «contínuo»:

— <date_start>2015-04-01+01</date_start>

— <date_end>2015-06-30+02</date_end>

— <time_start>06:00:00</time_start>

— <time_end>10:00:00</time_end>

— <interval_code>CON</interval_code>

— Se o período de restrições («interval_code») for contínuo a hora de início («start_time») pertence à data de início («start_date») e a hora de termo («end_time») à data de termo («end_date», por exemplo, das 06h00 de 1 de abril até às 10h00 de 30 de junho

— Lógica e visualização da informação aplicável a qualquer outro intervalo que não o «contínuo»:

— <date_start>2015-04-01+01</date_start>

— <date_end>2015-06-30+02</date_end>

— <time_start>06:00:00</time_start>

— <time_end>10:00:00</time_end>

— <interval_code>WRK</interval_code>

— Se o intervalo («interval_code») tiver outro valor, a hora de início («start_time») e a hora de termo («end_time») pertencem a este intervalo, por exemplo, entre 1 de abril e 30 de junho, de segunda a sexta, das 06h00 às 10h00.

— O termo do período de restrições deve ser sempre preenchido na última versão de uma mensagem.

**7. Regras gerais de execução**

Devem ter-se em conta os seguintes elementos:

— O quadro «GUI_labels» incluído nas Tabelas de Referência dos NtS deve ser tido em conta quando se elaboram as aplicações de NtS (campos de pesquisa, formulário de subscrição de correio eletrónico, visualização de mensagens).

— A data de termo («date_end») não pode ser anterior à data de início («date_start»).

— Os códigos que tiverem sido desativados (que deixarão de ser utilizados) através de pedidos de alteração de NtS (ver observações no XSD NtS) não devem ser mostrados aos editores de NtS aquando da criação de novas mensagens. Os códigos ainda são incluídos nas enumerações do XSD NtS para efeitos de retrocompatibilidade.

**7.1. Preenchimento da secção relativa ao número («number_section»)**

Cada número (Organização/Ano/Número/Série) tem de ser único para cada tipo de mensagem. Isto significa que mensagens de tipos diferentes podem ter o mesmo número NtS.

Para os utilizadores, os números das mensagens só são relevantes no caso das mensagens FTM e ICEM. No caso de todos os outros tipos de mensagens a visualização do número da mensagem pode ser omitida, dependendo dos requisitos nacionais.

Para os utilizadores, o número da mensagem deve ser mostrado no formato seguinte: «Tipo de mensagem/País/Organização/Ano/Número/Série» (a extensão pode ser encurtada consoante os filtros aplicados, se não se perderem informações).

**7.2. Preenchimento dos elementos «from», «originator», «organisation» e «source»**

O elemento «from» na secção «identificação» é preenchido com o nome do sistema nacional que fornece a mensagem (por exemplo, ELWIS, DoRIS, SLOVRIS, FLARIS).

O elemento «originator» corresponde ao organismo que introduz as mensagens nos sistemas nacionais.

O elemento «source» é a autoridade para a qual as FTM são publicadas.

O elemento «organisation» na secção «nts_number» é o nome da organização que atribui esse número (emissor de NtS).

**7.3. Omissão de elementos**

Os elementos que contenham unicamente valores normalizados ou por defeito devem ser omitidos se forem condicionais, uma vez que sobrecarregam a mensagem sem qualquer valor acrescentado.

Estão em causa os seguintes elementos:

— Destinatários: Grupo-alvo (target_group_code) ALL com direção (direction_code) ALL (se não existirem outros grupos-alvo específicos na mensagem),

— position_code: AL,

— reason_code: OTHER.

**7.4. Preenchimento automático da secção «date_issue»)**

Mensagens FTM e ICEM

Nas mensagens FTM e ICEM, o valor do elemento «date_issue» corresponde à data e hora efetivas da publicação. No caso de mensagens atualizadas, «date_issue» é a data e a hora em que a atualização foi publicada.

Mensagens WRM e WERM

Nas mensagens WRM e WERM o valor do elemento «date_issue» corresponde à data e hora do pedido de tratamento, porque podem existir várias medições com diferentes marcadores horários numa só mensagem W(E)RM.

**7.5. Tratamento das informações relativas ao fuso horário nas mensagens NtS**

Nas mensagens XML NtS, a data e a hora devem ser sempre indicadas na hora local, incluindo informações sobre o fuso horário.

As únicas exceções a esta disposição são os elementos «time_start» (hora de início) e «time_end» (hora de termo) na secção «limitation_period» (período de restrição). Estas exceções devem-se à possibilidade de aplicar um intervalo na secção relativa às restrições. Se a data de início e a data de termo tiverem regimes horários diferentes (por exemplo, CEST e CET) haverá uma alteração da informação relativa ao fuso horário neste intervalo. Esta alteração não pode ser expressa através de um único período de restrições. Em vez de se criarem períodos de restrição diferentes para cada alteração da hora, utiliza-se apenas um único período de restrições sem informação sobre o fuso horário, a fim de simplificar o tratamento e a transmissão da mensagem.

**7.6. Tratamento dos segundos nas mensagens NtS**

Regra geral, os segundos devem ser indicados nos campos para a data e a hora, mas não devem ser mostrados aos utilizadores de NtS. Os minutos são suficientes para a granularidade dos NtS.

**7.7. Formato dos separadores decimais nas mensagens NtS**

Nos campos numéricos, o separador decimal é o ponto (.). Não se utilizam separadores de milhares.

O número de casas decimais utilizadas para os valores deve ser limitado de modo a garantir uma visualização facilmente compreensível.

**7.8. Unidades de medidas a utilizar nas mensagens NtS**

Nas mensagens NtS só podem ser utilizadas as seguintes unidades de medida: cm, m3/s, h, km/h e kW, m/s (vento), mm/h (chuva) e grau Celsius. As aplicações podem converter as unidades de medida para facilitar a compreensão.

Caso as unidades de medidas introduzidas sejam diferentes das unidades de medida normalizadas, a aplicação deve converter os valores introduzidos em conformidade.

**7.9. Regras aplicáveis aos elementos «name», «position_code» e «type_code»**

O elemento «name» é automaticamente preenchido a partir dos dados de referência do Índice RIS relativos ao «national object name» (os editores de NtS podem alterar o nome previamente preenchido se algum requisito nacional o exigir). As convenções relativas à designação dos objetos constam da versão 2.0 ou superior do Guia de Codificação do Índice do RIS. No Guia de Codificação de NtS para Editores também se apresentam exemplos de designações de objetos adequadas.

O código de tipo é aditado ao objeto pela aplicação NtS em frente da designação do objeto.

A posição dos objetos é codificada através do código de localização e aditado ao objeto pela aplicação NtS a partir do RIS Index. Os editores podem alterar os códigos de tipo e de localização previamente preenchidos. Não deve ser atribuído um código de localização de objeto aos geo_objects na fairway_section.

Uma designação de objeto completa é composta pelo seu código de localização, o código de tipo e o nome.

Para facilitar o trabalho dos editores de NtS pode implementar-se nas ferramentas de edição NtS uma grelha de correspondências que ajude os editores a encontrar /selecionar os objetos adequados com base no código de função (function_code) do RIS Index ou no código de tipo (type_code) NtS:

**Quadro 1**

**Matching «RIS Index function_code» — «NtS type_code»**

| Function Code | Function Code Meaning | Type Code | Type Code Meaning |
|---|---|---|---|
| — | — |  |  |
| BUAARE | E.1.1 Built-Up Areas |  | to be selected by editor |
| BUISGL | E.1.2 Building of Navigational Significance |  | to be selected by editor |
| brgare | G.1.1 - G.1.6 Bridge Area [C_AGGR()] | BRI | bridge |
| bridge_5 | G.1.1 Bascule Bridge | BRO | bridge opening |
| bridge_1 | G.1.2 Bridges with Bridge Arches | BRO | bridge opening |
| bridge_1 | G.1.3 Fixed Bridge | BRO | bridge opening |
| bridge_4 | G.1.4 Lift Bridge | BRO | bridge opening |
| bridge_12 | G.1.5 Suspension Bridge | BRO | bridge opening |
| bridge_3 | G.1.6 Swing Bridge | BRO | bridge opening |
| cblohd | G.1.8 Overhead Cable | CAB | cable overhead |
| pipohd | G.1.9 Overhead Pipe | PPO | pipeline overhead |
| bridge_7 | G.1.12 Drawbridge | BRO | bridge opening |
| bunsta | G.3.2 Bunker / Fuelling Station | BUS | Bunker / Fuelling Station |
| cranes | G.3.4 Crane |  | to be selected by editor |
| hrbare | G.3.9 Harbour Area | HAR | harbour |
| hrbbsn | G.3.10 Harbour Basin | HAR | harbour |
| ponton | G.3.11 Landing Stage, Pontoon |  | to be selected by editor |
| morfac | G.3.12 Mooring Facility | MOO | mooring facility |
| hulkes | G.3.14 Permanently Moored Vessel or Facility |  | to be selected by editor |
| prtare | G.3.15 Port Area | HAR | harbour |
| refdmp | G.3.17 Refuse Dump | REF | refuse dump |
| termnl | G.3.19 Terminal | TER | terminal |
| trm01 | G.3.19 RORO-terminal | TER | terminal |
| trm03 | G.3.19 Ferry-terminal | TER | terminal |
| trm07 | G.3.19 Tanker-Terminal | TER | terminal |
| trm08 | G.3.19 Passenger Terminal | TER | terminal |
| trm10 | G.3.19 Container Terminal | TER | terminal |
| trm11 | G.3.19 Bulk Terminal | TER | terminal |
| vehtrf | G.3.20 Vehicle Transfer Location | BER | berth |
| lokbsn | G.4.3 Lock Basin | LKB | lock basin |
| lkbspt | G.4.4 Lock Basin Part | LKB | lock basin |
| lokare | G.4.3 / G.4.4 Lock Area [C_AGGR()] | LCK | lock |
| excnst | G.4.8 Exceptional Navigational Structure | SLI | ship lift |
|  |  | TUN | tunnel |
|  |  | CBR | canal bridge |
| gatcon | G.4.9 Opening Barrage | BAR | weir |
|  |  | FLO | flood gate |
| wtwgag | I.3.4 Waterway Gauge | GAU | tide gauge |
| FERYRT_2 | L.2.1 Cable Ferry | FER | ferry |
| FERYRT_1 | L.2.2. Free Moving Ferry | FER | ferry |
| feryrt_4 | L.2.3. Swinging Wire Ferry | FER | ferry |
| dismar | L.3.2 Distance Mark along Waterway Axis | RIV | river |
| achare | M.1.1 Anchorage Area | ANC | anchoring area |
| achbrt | M.1.2 Anchorage Berth | BER | berth |
| berths_3 | M.1.3 Berth / Fleeting Areas | BER | berth |
| berths_1 | M.1.4 Transhipment Berth | BER | berth |
| trnbsn | M.4.5 Turning Basin | TUR | turning basin |
|  |  | CAN | canal |
|  |  | FWY | fairway |
| rdocal | Q.2.1 Radio Calling-In Point (notification point) | REP | reporting point |
| chkpnt | R.1.1 Check Point | BCO | border control |
| sistat_8 | R.2.1 Traffic Sistat — Bridge Passage | SIG | signal station |
| sistat_6 | R.2.2 Traffic Sistat — Lock | SIG | signal station |
| sistat_10 | R.2.3 Traffic Sistat — Oncoming Traffic Indicator | SIG | signal station |
| sistat_2 | R.2.4 Traffic Sitat — Port Entry and Departure | SIG | signal station |
| pas | Passage Points |  | to be selected by editor |
| riscen | RIS centre | VTC | vessel traffic centre |
| specon | Special Construction |  | to be selected by editor |
| trafp | Traffic Points (first reporting points) | REP | reporting point |
| junction | Waterway node / end of waterway / Junction |  | to be selected by editor |
| waypt | Waypoint |  | to be selected by editor |
| Legend: |  |  |  |
| green | Direct match (1:1 relation) |  |  |
| yellow | matching example, other TypeCodes possible (1:n relation) |  |  |
| blue | no direct match / to be selected by editor |  |  |

**7.10. Regras aplicáveis ao elemento «fairway_name»**

Para evitar a lógica/necessidade de aplicação de dados de referência adequados no sistema recetor (software que mostra o aviso ao utilizador) o elemento facultativo «fairway_name» (designação do canal navegável) deve ser sempre incluído no elemento «geo_object» (objeto geo-referenciado) e automaticamente preenchido pela aplicação NtS com o «nome da via navegável» do RIS Index. Os editores NtS não devem alterar o conteúdo do elemento «fairway_name».

**7.11. Esclarecimentos para as traduções na folha de cálculo «reference_code» (referência)**

Deve utilizar-se a seguinte definição para os valores de referência (reference_code) nas Tabelas de Referência NtS:

— NAP: Nos Países Baixos, a abreviatura NAP é utilizada e compreendida, não sendo traduzida

— KP: «nível de canal» deve traduzir-se na língua nacional

— FZP: só a abreviatura «FZP» deve ser utilizada (atualmente está praticamente em desuso)

— ADR: «Mar Adriático», deve traduzir-se na língua nacional

— TAW/DNG: «Tweede algemene Waterpassing» (neerlandês), «Deuzième Nivellement Général» (francês), trata-se da altura de referência utilizada na Bélgica para expressar as medições da altura. 0 é o valor médio do nível de água do mar na maré baixa em Ostende

—

— Neerlandês: TAW

— Francês: DNG

— Todas as outras línguas: TAW/DNG

— LDC: «nível baixo da água, Comissão do Danúbio», deve traduzir-se na língua nacional,

— HDC: «nível alto da água, Comissão do Danúbio», deve traduzir-se na língua nacional,

— ETRS: «Sistema Europeu de Referência Terrestre de 1989», a abreviatura «ETRS89» é utilizada em todas as línguas

**7.12. Recomendação para o elemento «coordenada»**

Embora o elemento «coordenada» na secção relativa aos objetos geográficos seja condicional, as coordenadas geográficas devem ser fornecidas no WGS84 no formato [d]d mm.mmm[m] N (latitude) e [d][d]d mm.mmm[m] E (longitude). O objetivo é referenciar as mensagens NtS geograficamente.

**7.13. Tratamento dos grupos-alvo**

A secção relativa aos grupos-alvo é constituída pelo código dos grupos-a e o código de direção. Se ambos tiverem o valor ALL, toda a secção deve ser omitida se não existirem outros grupos-alvo específicos na mensagem. Se apenas for indicado um destes dois códigos, o outro deve ser preenchido com o valor por defeito ALL porque ambos os elementos são obrigatórios.

Podem encontrar-se mais informações relativas aos grupos-alvo no Guia de Codificação de NtS para Editores.

**7.14. Visualização de mensagens válidas num dado momento**

O período de validade (validity_period) deve ser utilizado pelas aplicações para selecionar as mensagens que devem ser mostradas aos utilizadores durante um determinado período.

Se o código de matéria (subject_code) for INFSER (serviço de informação), o período de validade é utilizado para indicar o tempo que a mensagem de serviço de informação está disponível para ser visualizada pelos utilizadores e não o período de validade das informações facultadas (por exemplo, 1 mês).

**7.15. Funções opcionais para aumentar a facilidade de utilização das ferramentas de edição NtS**

As funções a seguir descritas podem ser facultadas aos editores de NtS consoante os requisitos nacionais:

— As aplicações NtS podem facultar aos editores de NtS a possibilidade de guardar os rascunhos de mensagens NtS (não é necessário fornecer todos os conteúdos obrigatórios para esses rascunhos serem guardados)

— Podem aplicar-se perfis de utilizador diferentes aos diferentes editores (por exemplo, editores que são autorizados a introduzir/alterar avisos, editores que são autorizados a publicar avisos (para além da sua edição)

**8. Estrutura de mensagem XML dos NTS**

A estrutura de uma mensagem XML NtS e o conteúdo e finalidade dos dados nela contidos são definidos e explicados em pormenor no anexo C: Definição do esquema XML (XSD) NtS

**9. O Serviço Web NTS**

**9.1. Objetivo**

O Grupo de Peritos NtS identificou a tecnologia de serviço Web como um meio adequado para fornecer os avisos à navegação.

O presente capítulo constitui a especificação do serviço Web para o fornecimento dos avisos à navegação, a seguir denominado Serviço Web Nts. Nesta especificação, foi conferida especial ênfase à utilização de normas internacionais consolidadas.

Um dos objetivos deste projeto era garantir um equilíbrio adequado entre a flexibilidade e a solidez do serviço Web dele resultante. Os parâmetros de filtragem incorporados nos pedidos correspondem essencialmente aos critérios especificados na norma NtS (troço de via navegável com a indicação opcional da baliza quilométrica, período de validade e data de publicação do aviso). Esta opção afigura-se suficientemente expressiva, atendendo aos casos de utilização do serviço Web, ao mesmo tempo que reduz a complexidade da execução.

O resultado principal é um contrato de serviço Web em que se especificam os pedidos e as respostas. O contrato pode ser invocado pelos consumidores do serviço Web e os fornecedores são obrigados a cumpri-lo. O presente contrato é especificado utilizando a norma internacional WSDL.

Cada Estado-Membro participante deve executar um ou mais serviços Web para os diferentes tipos de mensagens NtS (FTM, WRM, ICEM, WERM) e prestá-los através da Internet («NtS Message Service» — Serviço de Mensagens NtS)

Os pormenores técnicos da execução do Serviço Web NtS, por exemplo, a escolha dos conjuntos de dados, aplicações e plataformas adequados, não estão incluídos no âmbito de aplicação da presente especificação e são da responsabilidade de cada Estado-Membro participante.

Para definir uma comunicação segura, devem ter-se em conta vários aspetos de segurança e objetivos de proteção, mas, dependendo das circunstâncias, nem todos estes aspetos têm de ser considerados. A sua prioridade e o seu grau de cumprimento podem variar. Além disso, a viabilidade de uma determinada medida pode ser limitada pela capacidade de execução a nível técnico. No contexto dos NtS, todas as informações são públicas, pelo que não há necessidade de proteger os próprios dados NtS no que à proteção de dados diz respeito. Por conseguinte, cada fornecedor deve decidir até que ponto este aspeto será aplicado no seu serviço.

**9.2. Princípios básicos e condicionalismos**

**9.2.1. Normas Web**

O Serviço Web NtS deve respeitar o Perfil Básico 1.1 da WS-I. Este perfil fornece orientações em matéria de interoperabilidade para um conjunto básico de especificações de serviços Web não exclusivos, tais como as especificações SOAP, WSDL e UDDI (

4

). As normas mais relevantes neste âmbito são:

— XML Schema Definition (XSD),

— Simples Object Access Protocol (SOAP),

— WSDL (Web Services Description Language) e

— Universal Description, Discovery and Integration (UDDI).

A mensagem de resposta do WS NtS é uma mensagem NtS definida na definição do esquema XML (XSD) no apêndice C do presente regulamento da Comissão.

| SOAP | é um protocolo de aplicação para a transmissão de dados entre sistemas informáticos normalizado pelo World Wide Web Consortium (W3C). <br> Os elementos específicos do Serviço Web NtS são definidos de acordo com as especificações WSDL correspondentes no apêndice D do presente regulamento da Comissão. O esquema da norma NtS (XSD) é incluído com uma instrução de importação. |
|---|---|

| UDDI | (Universal Description, Discovery and Integration) é aqui referido como um registo central, eventualmente internacional, de serviços Web, onde o Serviço Web NtS pode ser registado. Os potenciais consumidores do serviço Web podem pesquisá-lo e encontrá-lo neste registo, mas, uma vez que os potenciais fornecedores do serviço Web NtS estão limitados pelos Estados-Membros participantes e a especificação WSDL faz parte integrante da norma, não há uma necessidade manifesta de um registo independente do serviço Web NtS. |
|---|---|

**9.2.2. Modelo de interação e método de codificação do WS NtS**

O método de codificação Document-literal wrapped é utilizado no Serviço Web NtS porque permite a validação com base num esquema XML e os nomes de operações definidos na especificação WSDL são diretamente utilizados como nomes de marcadores XML nas mensagens SOAP.

**9.3. Especificações e recomendações gerais**

**9.3.1. Especificação: Informação sobre as versões**

A informação sobre a versão do Serviço Web NtS é composta por duas secções:

— versão do próprio serviço Web

— versão do esquema NtS utilizado pelo serviço Web

A secção do serviço Web propriamente dito é constituída por duas partes:

— a versão principal (MajorVersion) do serviço Web

— a versão secundária (MinorVersion) do serviço Web

O parâmetro MajorVersion é indicado por um número inteiro positivo que designa a versão principal do serviço Web.

O parâmetro MinorVersion é indicado por um número inteiro não negativo que designa a versão secundária do serviço Web dentro da versão principal.

A secção do esquema NtS descreve a versão deste esquema tal como definida pelo Grupo de Peritos NtS.

Assim, a versão do Serviço Web NtS aqui referida é a 2.0.4.0, sendo 2.0 a versão do serviço Web e 4.0 a versão do esquema NtS utilizado.

Não são necessárias informações explícitas sobre a versão nos pedidos ou respostas do Serviço Web NtS. Só um pequeno número de versões dos serviços deverá estar em linha em simultâneo. As diferentes versões devem ser fornecidas com diferentes endereços URL. Assim, cada instância de execução do Serviço Web NtS deve suportar uma versão específica do mesmo.

**9.3.2. Especificação: Estrutura dos espaços de nomes**

No Serviço Web NtS, os espaços de nomes (namespaces) são baseados no domínio Web dos Grupos de Peritos RIS, http://www.ris.eu/.

Os espaços de nomes contêm uma partícula que indica o serviço e a versão correspondentes. Deste modo, o serviço aqui especificado utiliza os seguintes espaços de nomes:

Serviço de Mensagens NtS: http://www.ris.eu/nts.ms/2.0.4.0

**9.3.3. Recomendação: Utilização de espaços de nomes**

Para uma maior transparência dos documentos XML, recomenda-se que os espaços de nomes sejam definidos no elemento mais adequado nos esquemas e nos documentos de instância e que não se utilizem definições locais dos espaços de nomes nos elementos encadeados.

**9.3.4. Recomendação: Utilização de prefixos de espaços de nomes**

Os pedidos e respostas no Serviço Web NtS devem utilizar os elementos XML de forma qualificada, ou seja com um prefixo de espaço de nome explícito, e atributos XML de forma não qualificada, ou seja, sem um prefixo de nome de espaço.

Recomenda-se a utilização de prefixos de espaços de nomes intuitivos como «nts» para uma melhor legibilidade pelo ser humano.

**9.3.5. Especificação: Utilização dos ISRS Location Codes**

O ISRS Location Code é explicado no capítulo 2 do Guia de Codificação de NtS para Informáticos bem como no Guia de Codificação do RIS Index.

Ao efetuar pesquisas num Serviço Web NtS, o cliente pode referenciar vários objetos, por exemplo, troços de via navegável, fluviómetros ou eclusas. Se os parâmetros correspondentes, os elementos de identificação, forem utilizados, devem incluir ISRS Location Codes. Estes parâmetros são normalmente fornecidos nos elementos de identificação, que contêm, cada um deles, um ou dois identificadores.

Ao utilizar estes parâmetros, devem respeitar-se as seguintes convenções gerais:

— Os códigos ISRS de local devem ser apresentados como códigos completos de 20 carateres, ou seja, sem truncar zeros significativos.

— Se forem utilizados dois identificadores num elemento de identificação, ambos os códigos ISRS de local têm de ser referentes à mesma via navegável. Isto significa que os códigos devem incluir alguns dígitos idênticos localizados na parte «fairway_section» (via navegável ou troço) do código ISRS de local. O código de via navegável em conjunto com o hectómetro do canal navegável define um troço indicado como um par de elementos de identificação.

Para indicar troços de via navegáveis (pares de elementos de identificação no objeto geo-referenciado da via navegável (fairway_section geo_object) nas mensagens NtS, há que ter em conta os seguintes aspetos relativos aos códigos ISRS de local:

— os dígitos 1 a 2 (Country code):

—

— têm de ser idênticos no par de elementos de identificação, mas

— num só par podem ser definidos diversos códigos de países, se países vizinhos utilizarem o mesmo código de canal navegável para uma via específica e o mesmo sistema para definir os hectómetros,

— os dígitos 3 a 5 (UN Location code):

—

— não são pertinentes, podem ter diferentes conteúdos no par de elementos de identificação

— os dígitos 6 a 10 (Fairway section code):

—

— devem ser idênticos no par de elementos de identificação, mas

— [exceção]: no caso da utilização dos códigos ISRS belgas no âmbito do WS NtS, só se devem utilizar os dígitos 6 a 8 para identificar o troço de via navegável, porque serão publicados mensagens NtS em diferentes troços de uma via navegável,

— os dígitos 11 a 15 (Object Reference Code):

—

— não são pertinentes, podem ter conteúdos diferentes dentro do par de elementos de identificação

— os dígitos 16 a 20 (Fairway Hectometre):

—

— consistem em cinco carateres numéricos que definem o hectómetro, pelo que terão normalmente conteúdos diferentes no par de elementos de identificação. Exemplo: «00235» para o km 23,5 do canal navegável; «00001» para o km 0,1 do canal navegável,

— [exceção]: no caso dos Países Baixos, nem sempre existe uma ligação direta entre o hectómetro de canal navegável e o quilómetro físico do canal navegável devido à definição do início do troço da via navegável no modelo da rede e no mundo real. Nesses casos, o código de referência de objeto para os objetos do tipo «dismar» começa com Kxxxx [xxxx inclui o quilómetro físico, por exemplo, NLSVG00130K000300191 (km 3)]. Porém, há outros tipos de objetos em que não existe qualquer relação direta com o quilómetro físico da via navegável nos códigos ISRS. Por exemplo, a ponte de Sas van Gent no km 2,5 da mesma via navegável tem o código ISRS NLSVG001300521600186. No caso do Kanaal Gent-Terneuzen o km físico 0,0 começa na fronteira entre a Bélgica e os Países Baixos e o hectómetro da via navegável 0,0 começa no início do canal em Gent.

Caso uma mensagem afete mais de um troço de via ou canal navegável, todos os troços devem ser definidos pelo seu ponto de início e de termo em elementos XML «fairway_section» separados.

No caso de alguns países/regiões é necessário introduzir uma funcionalidade de filtragem. Por exemplo, se o código ISRS de local (1-2) for BE, deve utilizar-se o código ISRS de local (6-8) como ID para uma referenciação linear com o hectómetro de via navegável (código ISRS de local 16-20). Exemplos de troços de via navegável (pares de elementos de identificação válidos na «fairway_section») que incluem as exceções acima definidas:

— Os dois códigos ISRS de local NL constituem uma definição válida de troço de via navegável (mostrando a exceção dos NL no que diz respeito ao quilómetro da via navegável): NLSVG00130K000300191 (km 3,0 em Sas van Gent no Kanaal Gent-Terneuzen) — NLWDP00130K000400200 (km 4,0 em Westdorpe no Kanaal Gent-Terneuzen),

— Os dois códigos ISRS de local BE constituem uma definição válida de troço de via navegável [mostrando a exceção da BE relativamente ao código de troço de canal navegável («020» Albertkanaal)]: BEGNK02016L010100414 (eclusa de Genk situada no km 41,4 no Canal Albert) — BEOSH02033L010500772 (eclusa de Ham situada no km 77,2 no Canal Albert).

O gráfico seguinte mostra exemplos contrários de utilização do código ISRS de local para cada uma das convenções gerais (não há exceções às convenções aplicáveis nos troços de vias navegáveis da SK):

image

**Pesquisas de códigos ISRS de local inválidos**

Observação geral: O Serviço Web Nts não suporta um serviço de pesquisa de códigos ISRS de local válidos. Os códigos ISRS de local são fornecidos no âmbito do Sistema de Gestão de Dados de Referência Europeu (ERDMS).

Nos cinco casos a seguir apresentados indica-se a forma correta de utilizar os códigos ISRS de local nas pesquisas e a sua interpretação.

**Caso 1: Nenhum elemento de ID no pedido**

O elemento de ID é uma parte opcional do pedido, ou seja, são permitidas pesquisas sem elementos de ID:

image

**Pesquisa válida sem parâmetro de identificação**

Se nenhum elemento de identificação for fornecido, todas as mensagens serão devolvidas [dependendo, naturalmente, de outros critérios de filtragem como o período de validade (validity_period) ou a data atual (date_issue)].

**Caso 2: Um elemento de ID no pedido de informação**

Cada elemento de identificação pode conter um ou dois identificadores. No gráfico seguinte apresenta-se um exemplo com um identificador:

image

**Pesquisa válida com um parâmetro de ID**

Se um tal pedido for recebido, o servidor deve devolver todas as mensagens correspondentes com um hectómetro de início ≤ ao valor indicado (240,7 , no exemplo) e um hectómetro final igual ou superior a este valor. O gráfico infra ilustra esta seleção de mensagens: A localização pesquisada situa-se entre os valores dos hectómetros de início e de termo das mensagens 1, 3 e 4, que seriam devolvidas. As mensagens 2, 5 e 6 não se sobrepõem com a localização pesquisada, pelo que não seriam devolvidas.

Se o código ISRS de local indicado corresponder a um único objeto, por exemplo um fluviómetro ou uma eclusa, o serviço Web deve devolver as mensagens relativas a este objeto.

image

**Mensagens correspondentes e não correspondentes a um parâmetro de identificação**

**Caso 3: Dois elementos de ID no pedido de informação**

Cada elemento de identificação pode conter um ou dois identificadores. No gráfico seguinte apresenta-se um exemplo com dois identificadores:

image

**Pesquisa válida com dois parâmetros de ID**

Todos os valores de hectómetros pesquisados devem ser considerados válidos, mesmo que o troço de via navegável correspondente tenha pontos de início ou de termo diferentes. Por exemplo, se o troço de via navegável começar no hectómetro 100,0 e terminar no hectómetro 300,0 , será válido um pedido relativo aos hectómetros 20,0 a 400,0 . Internamente, é claro que só a «verdadeira» extensão do troço de via navegável é pesquisada.

Deste modo possibilita-se igualmente a pesquisa de todas as mensagens sobre uma via navegável sem conhecer exatamente a sua extensão em hectómetros (deve enviar-se o código ISRS de local com a indicação dos hectómetros como «00000» ou «99999», respetivamente).

Todas as mensagens correspondentes que intersetem o intervalo de hectómetros em causa serão devolvidas. O diagrama seguinte ilustra esta situação:

image

**Mensagens correspondentes e não correspondentes para dois parâmetros de ID**

A figura supra ilustra a definição de «interseção». Enquanto as extensões das mensagens 1 a 4 se sobrepõem à extensão do intervalo de hectómetros pesquisado (parcial ou totalmente), o mesmo não acontece com as mensagens 5 e 6, pelo que as mensagens 1 a 4 serão devolvidas e as 5 e 6 não.

A condição técnica para uma mensagem intersetar um intervalo [A e B] é a seguinte: O hectómetro inicial da mensagem é ≤ B e o seu hectómetro de termo ≥ A.

**Combinação: Múltiplos elementos de ID num pedido de informação**

image

**Pesquisa válida com múltiplos elementos de identificação**

A combinação de vários elementos de identificação no pedido de informação leva a uma união de mensagens correspondentes. Todos os elementos de ID são tratados separadamente e uma mensagem será devolvida se corresponder, pelo menos, a um deles. Por conseguinte, as mensagens a seguir indicadas serão devolvidas no caso do exemplo apresentado:

— Todas as mensagens relativas ao objeto com o código ISRS de local SKXXX0000010000***** com o hectómetro inicial = 0 e o hectómetro final ≥ 0 (ver Caso 2)

— Todas as mensagens relativas ao objeto com o código ISRS de local SKXXX0000500000***** que intersetam o intervalo de hectómetros [11,0 a 15,0 ] (ver Caso 3)

— Todas as mensagens relativas ao objeto com o código ISRS de local SKXXX0000200000***** com o hectómetro inicial ≤ 110,5 e o hectómetro final ≥ 110,5 (ver Caso 2)

— Todas as mensagens relativas ao objeto com o código ISRS de local SKXXX0000500000***** que intersetam o intervalo de hectómetros [220,0 a 300,0 ] (ver Caso 3)

**9.4. Serviço de mensagens NtS (especificação da aplicação)**

No presente capítulo, descreve-se a especificação da aplicação do NtS message service, deduzida das considerações e escolhas feitas nos capítulos precedentes.

O serviço de mensagens NtS disponibiliza quatro tipos de mensagens NtS:

1. NtS FTM (mensagem relativa à via navegável e ao tráfego)

2. NtS WRM (mensagem relativa à água)

3. NtS ICEM (mensagem relativa ao gelo)

4. NtS WERM (mensagem relativa às condições meteorológicas)

A aplicação do serviço de mensagens NtS pode suportar todos os tipos de mensagens ou apenas uma seleção dos mesmos. É permitido que um Estado-Membro participante preste, em relação a um determinado tipo de mensagem, vários serviços que se complementem mutuamente.

**9.4.1. Pedido de informação**

Para que o serviço Web NtS tenha a maior robustez possível mantendo simultaneamente um baixo nível de complexidade, não se utiliza qualquer linguagem de pesquisa adicional, aplicando-se, em vez disso, as estruturas conceptuais fornecidas pelo próprio WSDL. As operações específicas, em conjunto com os seus parâmetros, são integralmente descritas na especificação WSDL. No caso do Serviço de Mensagens NtS é definida uma única operação.

Os critérios de filtragem relativos a cada matéria são extraídos da norma NtS, mas alargados de modo a abranger a multiplicidade dos parâmetros:

— tipo de mensagem (obrigatório; «FTM», «WRM», «ICEM» ou «WERM»)

— troços de vias navegáveis específicos, ou partes dos mesmos, ou objetos específicos (opcional; descritos por códigos ISRS de local e/ou pares de códigos ISRS de local)

— período de validade (opcional; data de início e de termo)

— data de publicação do aviso (opcional; datas únicas e/ou intervalos de datas)

Só as mensagens que satisfaçam os critérios indicados são devolvidas pelo serviço.

Mecanismo de paginação

O serviço suporta um mecanismo de paginação para controlar a quantidade de dados. O parâmetro de paginação é definido com um tipo complexo que contém os seguintes elementos:

— offset: número de série da primeira mensagem devolvida (número inteiro ≥ 0)

— limite: número máximo de mensagens (número inteiro ≥ 0)

— contagem total: bandeira, se o número total de mensagens for devolvido (valor booleano)

O parâmetro de paginação complexa é opcional, mas se estiver presente, todos os elementos nele contidos devem ser fornecidos. Depois, o mecanismo de paginação funciona do seguinte modo:

O número total de mensagens não excederá o valor do parâmetro limite, com a exceção de que um valor de 0 significa «sem limite». A resposta salta todas as mensagens definidas no parâmetro offset. Para poder disponibilizar este mecanismo, o serviço tem de respeitar uma sequência das mensagens temporariamente estável (mas de outro modo arbitrária), por exemplo entre duas atualizações do conjunto de dados subjacente ao serviço Web com os dados das mensagens. Isto significa que duas chamadas idênticas consecutivas devem devolver as mesmas mensagens segundo a mesma ordem. O parâmetro contagem total determina se a resposta deve fornecer o número total de mensagens correspondentes aos critérios específicos. Normalmente, deverá ser suficiente pedir esta informação juntamente com a primeira resposta, omitindo-a em todas as respostas consecutivas. Deste modo, poderá obter-se um melhor desempenho do serviço Web.

O mecanismo de paginação permite solicitar as mensagens iterativamente em «páginas». Para que o mecanismo de paginação possa funcionar corretamente, devem fornecer-se os mesmos parâmetros específicos em cada chamada.

**9.4.2. Resposta**

Se um pedido for bem sucedido, a resposta do Serviço Web NtS contém as mensagens NtS correspondentes aos parâmetros do pedido. As mensagens NtS têm de respeitar o esquema NtS e podem ser validadas com base no mesmo. Uma vez que o tipo de mensagem é um parâmetro de pedido obrigatório, cada resposta só pode conter mensagens NtS do mesmo tipo, FTM, WRM, ICEM ou WERM, respetivamente.

Se o serviço detetar erros durante o tratamento do pedido pode devolver um número arbitrário de mensagens de erro, utilizando os códigos de erro indicados no subcapítulo seguinte.

Uma resposta de um serviço Web NtS pode conter mensagens NtS e mensagens de erro ao mesmo tempo.

As informações de paginação opcionais são devolvidas se o pedido contiver parâmetros de paginação. Neste caso, o parâmetro offset e o número de mensagens contidas são obrigatórios, a contagem total só tem de existir se for solicitada.

Nota: Parte-se do princípio de que a comunicação entre o serviço Web e o utilizador é estabelecida tecnicamente, isto é, o serviço recebe o pedido e o utilizador recebe a resposta correspondente. Erros técnicos, por exemplo, a interrupção da ligação à Internet ou a inacessibilidade do serviço Web devido a manutenção ou avaria não são aqui considerados. Só as situações de erro que ocorrem «por detrás» do nível do serviço Web percetível pelos utilizadores são aqui consideradas.

Mensagens de erro

Os códigos de erro utilizados nas situações de erro previstas são a seguir enunciados, juntamente com uma explicação. A resposta só contém o código de erro, que é o procedimento habitual no esquema XML do NtS.

**Códigos de erro para o serviço de mensagens NtS**

| Code | Description | Explanation |
|---|---|---|
| e010 | message type not supported | web service does not support the requested message type |
| e030 | paging parameters inconsistent with messages | parameters for paging mechanism do not fit the available messages, e.g. Offset ≥ Total Count |
| e100 | syntax error in request | request violates the schema for requests; can be specified in more detail by further e1xx-Codes |
| e110 | incorrect message type | given message type is not known |
| e120 | incorrect type-specific parameters | type-specific parameters are erroneous |
| e130 | incorrect paging parameters | given parameters for the paging mechanism are erroneous |
| e200 | operation not known | the requested operation is unknown |
| e300 | data source unavailable | data source of the web service for the NtS data is temporarily unavailable (technical problem) |
| e310 | too many results for request, | server is unable to handle number of results |

**9.5. Geração de serviços e clientes**

Se a abordagem «contrato primeiro» for respeitada de forma consequente, ou seja, se um ou mais contratos com descrições completas das interfaces forem facultados sob a forma de documentos WSDL, pode ser automaticamente gerada uma aplicação do(s) serviço(s), bem como uma aplicação de um cliente correspondente utilizando ferramentas de software adequadas. Numa situação ideal, não é necessário introduzir alterações manualmente no código-fonte gerado.

Contudo, na maior parte dos casos são necessárias várias repetições até a especificação WSDL cumprir os requisitos exatos de tais ferramentas. Normalmente, a ferramenta faz solicitações individuais à utilização da norma WSDL para funcionar bem. Em consequência, pode ser necessário fazer alterações à especificação WSDL, ainda que esta fosse à partida válida à luz da norma WSDL. Se a especificação WSDL do serviço Web for alterada depois de o serviço ou o cliente terem sido gerados, pode ser necessário um novo processo de geração, em função das alterações efetuadas.

**Glossário**

| Termo | Explicação |
|---|---|
| ID | Identificação |
| ISRS Location Code | Código de local da «International Ship Reporting Standard» (norma internacional de notificação de navios) |
| NtS | Avisos à navegação |
| RIS | Serviços de informação fluvial (River Information Services) |
| SOAP | Protocolo simples de acesso a objetos (Simple Object Access Protocol); protocolo de rede normalmente utilizado para serviços Web |
| UDDI | Universal Description, Discovery and Integration (descrição, pesquisa e integração universal); Norma para serviços de registo no contexto dos serviços Web |
| ONU | Organização das Nações Unidas |
| URL | Localizador uniforme de recursos (Uniform Resource Locator); localização de um recurso de rede normalmente utilizado para endereços Internet |
| WGS 84 | Sistema Geodésico Mundial 1984 |
| WS | Serviço Web; serviço que disponibiliza as suas interfaces na Internet e é utilizado pela comunicação via Internet |
| WSDL | Web Services Description Language (linguagem para descrição de serviços Web) norma para a especificação de serviços Web |
| WS-I | Web Services Interoperability Organisation; consórcio industrial que tem por objetivo apoiar a interoperabilidade dos serviços Web |
| XML | Linguagem de marcação extensível (Extensible Markup Language) Metalinguagem de representação dos dados estruturada e independente de plataformas |
| XSD | XML Schema Definition (definição de esquema XML ou modelo de mensagem XML) norma para especificar a estrutura dos documentos XML |
