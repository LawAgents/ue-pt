---
id: "regulamento-ue-2005-782"
celex: "32005R0782"
title: "Regulamento (CE) n.° 782/2005 da Comissão, de 24 de Maio de 2005, que estabelece o formato para a transmissão dos resultados das estatísticas de resíduos   (Texto relevante para efeitos do EEE)"
type: "Regulamento"
number: "782/2005"
year: 2005
date: 2005-05-24
status: "em vigor"
text_version: "consolidado"
last_amended: 2008-01-01
consolidated_celex: "02005R0782-20080101"
source: "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:02005R0782-20080101"
eli: "http://data.europa.eu/eli/reg/2005/782/oj"
retrieved: 2026-10-21
legal_notice: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
---

# Regulamento (CE) n.° 782/2005 da Comissão, de 24 de Maio de 2005, que estabelece o formato para a transmissão dos resultados das estatísticas de resíduos   (Texto relevante para efeitos do EEE)

## Artigo 1.º

O formato apropriado para a transmissão dos resultados das estatísticas de resíduos à Comissão (Eurostat) é o que consta do anexo do presente regulamento.

Os Estados-Membros utilizarão este formato para os dados relativos ao ano de referência 2004 e para os anos subsequentes.

## Artigo 2.º

Os Estados-Membros transmitirão à Comissão (Eurostat) os dados e os metadados exigidos pelo Regulamento (CE) n.º 2150/2002, em formato electrónico, de acordo com um padrão de intercâmbio proposto pela Comissão (Eurostat).

## Artigo 3.º

O presente regulamento entra em vigor no vigésimo dia seguinte ao da sua publicação no Jornal Oficial da União Europeia.

O presente regulamento é obrigatório em todos os seus elementos e directamente aplicável em todos os Estados-Membros.

## Anexo

**FORMATO PARA A TRANSMISSÃO DOS RESULTADOS DAS ESTATÍSTICAS DE RESÍDUOS**

Os dados devem ser transmitidos de forma independente do sistema. Serão transmitidos em conformidade com um padrão de intercâmbio proposto pela Comissão (Eurostat).

**Conjuntos de dados**

O domínio abrangido pelo Regulamento (CE) n.º 2150/2002 relativo às estatísticas de resíduos é constituído por cinco conjuntos de informações:

— produção de resíduos (GENER),

— incineração (INCIN),

— operações que podem conduzir à valorização (RECOV),

— eliminação (DISPO),

— número e capacidade das unidades de valorização e eliminação; cobertura do sistema de recolha de resíduos por região NUTS 2 (REGIO).

Deve ser transmitido um ficheiro para cada conjunto. O nome do ficheiro é composto por seis partes:

| Domínio | 5 | Valor: WASTE |
|---|---|---|
| Conjunto | 5 | GENER, INCIN, RECOV, DISPO, REGIO |
| Periodicidade | 2 | Valor: A2 |
| Código do país | 2 | Código do país com duas letras (ver lista A) |
| Ano | 4 | Ano de referência (primeiro ano de referência: 2004) |
| Período | 4 | Valor: 0000 (zero, zero, zero, zero) para dados anuais |

As partes que compõem o nome do ficheiro são separadas por um sublinhado. Será usado um formato de base textual. Por exemplo, o conjunto relativo à produção de resíduos da Bélgica em 2004 terá o seguinte nome: WASTE_GENER_A2_BE_2004_0000.

**Valores em falta**

Não haverá valores em falta nas variáveis de classificação (categoria de resíduos, actividade económica, região NUTS 2, tipo de unidade de tratamento de resíduos). Devem ser fornecidos registos relativos a todas as combinações das variáveis de classificação. Todos os registos em que essa combinação não ocorra devem ser enviados com um valor de 0 (zero). Os registos relativamente aos quais não haja dados disponíveis devem, ainda assim, ser fornecidos com o valor adequadamente codificado como estando em falta (codificado com a letra «M»). Os valores em falta terão de ser explicados no relatório de qualidade; poderão, por exemplo, ser um resultado dos métodos usados. É importante distinguir zeros reais de valores em falta, na medida em que não é possível calcular agregados com dados em falta. Se uma determinada combinação não for possível por motivos lógicos, a célula deve ser fornecida com o código «L»; é o caso, por exemplo, das lamas de efluentes industriais produzidas pelo sector doméstico. Para facilitar as verificações de coerência e a correcção de erros, devem ser igualmente transmitidos os totais.

**Confidencialidade**

Os dados confidenciais devem ser transmitidos convenientemente assinalados como confidenciais. Aquilo que se deve considerar confidencial depende da política nacional de confidencialidade. Em geral, a informação pode ser confidencial se puder ser divulgada a identidade do seu fornecedor. É o que acontece se a informação se basear em um ou dois inquiridos ou se um ou dois inquiridos dominar(em) os dados. Os dados provenientes das entidades públicas não são, em geral, considerados confidenciais.

Deve ainda ser indicada a confidencialidade de segundo grau. Esta deve ser aplicada de forma a que os (sub)totais permaneçam disponíveis para publicação. A Comissão (Eurostat) usará a informação confidencial para calcular agregados (UE) sem revelar a informação confidencial ao nível do país.

**Medidas**

Os campos exigidos são alfanuméricos, ou seja, não devem conter separadores nem símbolos decimais, excepto para o valor dos dados. As quantidades de resíduos são expressas em milhares de toneladas por ano, com três posições decimais. Deve usar-se a vírgula como símbolo decimal. O método de estimação nem sempre permitirá a precisão de três dígitos. Nesse caso, os valores devem ser comunicados apenas com os dígitos significativos. Em relação a todas as categorias de resíduos, a quantidade baseia-se nos resíduos húmidos (normais); em relação à produção de lamas (artigos de resíduos 11, 12, 40), a quantidade é igualmente calculada em milhares de toneladas de matéria seca. Também nos conjuntos relativos ao tratamento de resíduos, as lamas têm de ser medidas em resíduos húmidos (normais) e em matéria seca, o que só será aplicado se as lamas constituírem um artigo em separado; esta disposição aplica-se às lamas comuns (artigo 12) no conjunto relativo à incineração e eliminação.

O número de unidades de tratamento de resíduos é expresso através de um número inteiro. São usadas várias medidas para descrever a capacidade de tratamento de resíduos, dependendo do tipo de operação de valorização ou eliminação (ver lista I). Para melhorar a comparabilidade, prefere-se que a capacidade de incineração seja comunicada em milhares de toneladas. Os países que também puderem fornecer a capacidade de incineração em terajoules (1012 joules) são convidados a fazê-lo. Os países que não puderem fornecer a capacidade de incineração em terajoules devem comunicar o valor como estando em falta (usar o código «M»). A capacidade de valorização é medida em milhares de toneladas e tem de ser comunicada em metros cúbicos ou em toneladas, dependendo do tipo de eliminação. Apenas os valores medidos em milhares de toneladas são fornecidos sob a forma de um número real com três posições decimais, devendo todos os outros valores ser fornecidos como números inteiros.

A cobertura do sistema de recolha de resíduos mistos domésticos e similares deve ser comunicada em percentagem da população ou em percentagem das habitações.

**Revisões**

Os conjuntos devem ser enviados em ficheiros separados que contenham todos os registos. Por exemplo, o conjunto relativo à produção de resíduos contém 51 categorias de resíduos por 21 grupos da NACE, medidos em resíduos húmidos e três categorias de resíduos por 21 grupos da NACE, medidos em matéria seca. O conjunto contém 1 134 registos.

Além disso, os dados revistos devem ser enviados num conjunto completo, com as células revistas devidamente assinaladas (R). Os dados provisórios são indicados com o sinal de actualização P e exigem sempre uma revisão. Tanto os dados provisórios como os dados revistos exigem uma explicação no relatório de qualidade.

Conjunto 1: Produção de resíduos

| Campo | Comprimento máximo | Valores |
|---|---|---|
| Domínio | 8 | Valor: WASTE |
| Conjunto | 6 | Valor: GENER (o conjunto é constituído por 51 × 21 registos medidos em resíduos húmidos e 3 × 21 medidos em matéria seca por país) |
| Código do país | 2 | Código do país com duas letras (ver lista A) |
| Ano | 4 | Ano de referência (primeiro ano de referência: 2004) |
| Artigo de resíduos | 2 | Código relativo à CER-Stat/versão 3 (ver lista B) |
| Artigo de actividade | 2 | Código relativo à NACE (ver lista C) |
| Húmidos/secos | 1 | Para todas as categorias de resíduos, quantidade em resíduos húmidos (normais) (código W); para as lamas (artigos de resíduos 11, 12, 40), quantidade também indicada em matéria seca (código D) |
| Resíduos produzidos | 12 | Quantidade em milhares de toneladas por ano. A quantidade é indicada sob a forma de um número real com três posições decimais. Deve usar-se a vírgula como símbolo decimal. Por exemplo: 19,876. Este campo deve conter sempre um valor. Se a combinação não ocorreu, o valor será 0 (zero). Os dados em falta devem ser codificados com a letra «M». A impossibilidade lógica de uma combinação é indicada com a letra «L». |
| Sinal de actualização | 1 | Para indicar dados provisórios (P) ou dados revistos (R); caso contrário, em branco |
| Sinal de confidencialidade | 1 | Indica dados confidenciais (ver lista D) |

Conjunto 2: Incineração

| Campo | Comprimento máximo | Valores |
|---|---|---|
| Domínio | 8 | Valor: WASTE |
| Conjunto | 6 | Valor: INCIN (o conjunto é constituído por 17 × 2 registos medidos em resíduos húmidos e 1 × 2 medidos em matéria seca por região NUTS 1) |
| Código do país | 2 | Código do país com duas letras (ver lista A) |
| Ano | 4 | Ano de referência (primeiro ano de referência: 2004) |
| Código NUTS 1 | 3 | Código da região, de acordo com a classificação NUTS no Regulamento (CE) n.º 1059/2003 do Parlamento Europeu e do Conselho (1); o total nacional deve ser fornecido usando o código TT |
| Artigo de resíduos | 2 | Código relativo à CER-Stat/versão 3 (ver lista E) |
| Operação de valorização ou eliminação | 1 | Código relativo aos anexos da Directiva 75/442/CEE do Conselho (2) (ver lista F); neste conjunto apenas se aplicam as operações 1 e 2 |
| Húmidos/secos | 1 | Para todas as categorias de resíduos, quantidade em resíduos húmidos (normais) (código W); para as lamas (artigo de resíduos 12), também a quantidade em matéria seca (código D) |
| Resíduos incinerados | 12 | Quantidade em milhares de toneladas por ano. A quantidade é indicada sob a forma de um número real com três posições decimais. Deve usar-se a vírgula como símbolo decimal. Por exemplo: 19,876. Este campo deve conter sempre um valor. Se a combinação não ocorreu, o valor será 0 (zero). Os dados em falta devem ser codificados com a letra «M». A impossibilidade lógica de uma combinação é indicada com a letra «L» |
| Sinal de actualização | 1 | Para indicar dados provisórios (P) ou dados revistos (R); caso contrário, em branco |
| Sinal de confidencialidade | 1 | Indica dados confidenciais (ver lista D) |
| (1) JO L 154 de 21.6.2003, p. 1 <br> (2) JO L 194 de 25.7.1975, p. 39. Directiva com a última redacção que lhe foi dada pelo Regulamento (CE) n.º 1882/2003 do Parlamento Europeu e do Conselho (JO L 284 de 31.10.2003, p. 1). |  |  |

Conjunto 3: Operações que podem conduzir à valorização (com exclusão da valorização energética)

| Campo | Comprimento máximo | Valores |
|---|---|---|
| Domínio | 8 | Valor: WASTE |
| Conjunto | 6 | Valor: RECOV (o conjunto é constituído por 20 registos por região NUTS 1) |
| Código do país | 2 | Código do país com duas letras (ver lista A) |
| Ano | 4 | Ano de referência (primeiro ano de referência: 2004) |
| Código NUTS 1 | 3 | Código da região, de acordo com a classificação NUTS no Regulamento (CE) n.º 1059/2003; o total nacional deve ser fornecido usando o código TT |
| Artigo de resíduos | 2 | Código relativo à CER-Stat/versão 3 (ver lista G) |
| Operação de valorização ou eliminação | 1 | Código relativo aos anexos da Directiva 75/442/CEE (ver lista F); neste conjunto apenas se aplica a operação 3 |
| Húmidos/secos | 1 | Para todas as categorias de resíduos, quantidade em resíduos húmidos (normais) (código W) |
| Resíduos valorizados | 12 | Quantidade em milhares de toneladas por ano. A quantidade é indicada sob a forma de um número real com três posições decimais. Deve usar-se a vírgula como símbolo decimal. Por exemplo: 19,876. Este campo deve conter sempre um valor. Se a combinação não ocorreu, o valor será 0 (zero). Os dados em falta devem ser codificados com a letra «M». A impossibilidade lógica de uma combinação é indicada com a letra «L» |
| Sinal de actualização | 1 | Para indicar dados provisórios (P) ou dados revistos (R); caso contrário, em branco |
| Sinal de confidencialidade | 1 | Indica dados confidenciais (ver lista D) |

Conjunto 4: Eliminação (excepto incineração)

| Campo | Comprimento máximo | Valores |
|---|---|---|
| Domínio | 8 | Valor: WASTE |
| Conjunto | 6 | Valor: DISPO (o conjunto é constituído por 19 × 2 registos medidos em resíduos húmidos e 1 × 2 medidos em matéria seca por região NUTS 1) |
| Código do país | 2 | Código do país com duas letras (ver lista A) |
| Ano | 4 | Ano de Referência (primeiro ano de referência: 2004) |
| Código NUTS 1 | 3 | Código da região, de acordo com a classificação NUTS no Regulamento (CE) n.º 1059/2003; o total nacional deve ser fornecido usando o código TT |
| Artigo de resíduos | 2 | Código relativo à CER-Stat/versão 3 (ver lista H) |
| Operação de valorização ou eliminação | 1 | Código relativo aos anexos da Directiva 75/442/CEE (ver lista F); neste conjunto apenas se aplicam as operações 4 e 5 |
| Húmidos/secos | 1 | Para todas as categorias de resíduos, quantidade em resíduos húmidos (normais) (código W); para as lamas (artigo de resíduos 12), também a quantidade em matéria seca (código D) |
| Resíduos eliminados | 12 | Quantidade em milhares de toneladas por ano. A quantidade é indicada sob a forma de um número real com três posições decimais. Deve usar-se a vírgula como símbolo decimal. Por exemplo: 19,876. Este campo deve conter sempre um valor. Se a combinação não ocorreu, o valor será 0 (zero). Os dados em falta devem ser codificados com a letra «M». A impossibilidade lógica de uma combinação é indicada com a letra «L» |
| Sinal de actualização | 1 | Para indicar dados provisórios (P) ou dados revistos (R); caso contrário, em branco |
| Sinal de confidencialidade | 1 | Indica dados confidenciais (ver lista D) |

Conjunto 5: Número e capacidade das unidades de valorização e eliminação e população servida por um sistema de recolha por região

| Campo | Comprimento máximo | Valores |
|---|---|---|
| Domínio | 8 | Valor: WASTE |
| Conjunto | 6 | Valor: REGIO (o conjunto é constituído por 14 registos por região NUTS 2) |
| Código do país | 2 | Código do país com duas letras (ver lista A) |
| Ano | 4 | Ano de referência (primeiro ano de referência: 2004) |
| Código NUTS 2 | 4 | Código da região, de acordo com a classificação NUTS no Regulamento (CE) n.º 1059/2003; o total nacional deve ser fornecido usando o código TT |
| Operação de valorização ou eliminação | 1 | Código relativo aos anexos da Directiva 75/442/CEE (ver lista F); em branco para a população servida pelo sistema de recolha |
| Variável | 1 | Número de unidades (N), capacidade (C) ou população servida pelo sistema de recolha (P) |
| Medida | 1 | Código para a medida de capacidade dependendo do tipo de operação de valorização ou eliminação (ver lista I); para o número de unidades código N, para a população servida pelo sistema de recolha código P (população) ou D (habitações) |
| Valor | 12 | Todos os valores – o número de unidades, a percentagem da população ou de habitações cobertas pelo sistema de recolha e a capacidade – são expressos através de um número inteiro. Este campo deve conter sempre um valor. Se a combinação não ocorreu, o valor será 0 (zero). Os dados em falta devem ser codificados com a letra «M». A impossibilidade lógica de uma combinação é indicada com a letra «L» |
| Sinal de actualização | 1 | Para indicar dados provisórios (P) ou dados revistos (R); caso contrário, em branco |
| Sinal de confidencialidade | 1 | Indica dados confidenciais (ver lista D) |

**Lista A — Códigos dos países**

| Bélgica | BE |
|---|---|
| República Checa | CZ |
| Dinamarca | DK |
| Alemanha | DE |
| Estónia | EE |
| Grécia | EL |
| Espanha | ES |
| França | FR |
| Irlanda | IE |
| Itália | IT |
| Chipre | CY |
| Letónia | LV |
| Lituânia | LT |
| Luxemburgo | LU |
| Hungria | HU |
| Malta | MT |
| Países Baixos | NL |
| Áustria | AT |
| Polónia | PL |
| Portugal | PT |
| Eslovénia | SI |
| Eslováquia | SK |
| Finlândia | FI |
| Suécia | SE |
| Reino Unido | UK |
| Bulgária | BG |
| Croácia | HR |
| Roménia | RO |
| Turquia | TR |
| Islândia | IS |
| Listenstaine | LI |
| Noruega | NO |

**Lista B — Categorias de resíduos**

| CER-Stat/Versão 3 (JO L 90 de 27.3.2004, p. 15) |  |  |  |
|---|---|---|---|
| Descrição | Código | Perigosos | Artigo de resíduos |
| Solventes usados | 01.1 | P | 1 |
| Resíduos ácidos, alcalinos ou salinos | 01.2 |  | 2 |
| Resíduos ácidos, alcalinos ou salinos | 01.2 | P | 3 |
| Óleos usados | 01.3 | P | 4 |
| Catalisadores químicos usados | 01.4 |  | 5 |
| Catalisadores químicos usados | 01.4 | P | 6 |
| Resíduos de reacções químicas | 02 |  | 7 |
| Resíduos de reacções químicas | 02 | P | 8 |
| Depósitos e resíduos químicos | 03.1 |  | 9 |
| Depósitos e resíduos químicos | 03.1 | P | 10 |
| Lamas de efluentes industriais | 03.2 |  | 11 |
| Lamas de efluentes industriais | 03.2 | P | 12 |
| Resíduos da prestação de cuidados de saúde e biológicos | 05 |  | 13 |
| Resíduos da prestação de cuidados de saúde e biológicos | 05 | P | 14 |
| Resíduos metálicos | 06 |  | 15 |
| Resíduos metálicos | 06 | P | 16 |
| Resíduos de vidro | 07.1 |  | 17 |
| Resíduos de vidro | 07.1 | P | 18 |
| Resíduos de papel e cartão | 07.2 |  | 19 |
| Resíduos de borracha | 07.3 |  | 20 |
| Resíduos de plásticos | 07.4 |  | 21 |
| Resíduos de madeira | 07.5 |  | 22 |
| Resíduos de madeira | 07.5 | P | 23 |
| Resíduos têxteis | 07.6 |  | 24 |
| Resíduos contendo PCB | 07.7 | P | 25 |
| Equipamento fora de uso (excluindo veículos fora de uso e resíduos de pilhas e acumuladores) | 08 (excl. 08.1, 08.41) |  | 26 |
| Equipamento fora de uso (excluindo veículos fora de uso e resíduos de pilhas e acumuladores) | 08 (excl. 08.1, 08.41) | P | 27 |
| Veículos fora de uso | 08.1 |  | 28 |
| Veículos fora de uso | 08.1 | P | 29 |
| Resíduos de pilhas e acumuladores | 08.41 |  | 30 |
| Resíduos de pilhas e acumuladores | 08.41 | P | 31 |
| Resíduos de origem animal e de origem vegetal (excluindo resíduos de origem animal de preparados e produtos alimentares, bem como fezes urina e estrume de animais) | 09 (excl. 09.11, 09.3) |  | 32 |
| Resíduos de origem animal de preparados e produtos alimentares | 09.11 |  | 33 |
| Fezes, urina e estrume de animais | 09.3 |  | 34 |
| Resíduos domésticos e similares | 10.1 |  | 35 |
| Materiais mistos e não diferenciados | 10.2 |  | 36 |
| Materiais mistos e não diferenciados | 10.2 | P | 37 |
| Resíduos de triagem | 10.3 |  | 38 |
| Resíduos de triagem | 10.3 | P | 39 |
| Lamas comuns (excluindo lamas de dragagem) | 11 (excl. 11.3) |  | 40 |
| Lamas de dragagem | 11.3 |  | 41 |
| Resíduos minerais (com exclusão dos resíduos de combustão, dos solos contaminados e das lamas de dragagem poluídas) | 12 (excl. 12.4, 12.6) |  | 42 |
| Resíduos minerais (com exclusão dos resíduos de combustão, dos solos contaminados e das lamas de dragagem poluídas) | 12 (excl. 12.4, 12.6) | P | 43 |
| Resíduos de combustão | 12.4 |  | 44 |
| Resíduos de combustão | 12.4 | P | 45 |
| Solos contaminados e lamas de dragagem poluídas | 12.6 |  | 46 |
| Resíduos solidificados, estabilizados ou vitrificados | 13 |  | 47 |
| Resíduos solidificados, estabilizados ou vitrificados | 13 | P | 48 |
| Total, não perigosos |  |  | TN |
| Total, perigosos |  | P | TH |
| Total geral |  |  | TT |

**Lista C — Artigo de actividade**

<table> <tbody> <tr> <td>Número do artigo</td> <td>Código da NACE Rev. 2</td> <td>Descrição</td> </tr> <tr> <td rowspan="2">1</td> <td>Divisão 01</td> <td>Produção vegetal e animal, caça e actividades dos serviços relacionados</td> </tr> <tr> <td>Divisão 02</td> <td>Silvicultura e exploração florestal</td> </tr> <tr> <td>2</td> <td>Divisão 03</td> <td>Pesca e aquacultura</td> </tr> <tr> <td>3</td> <td>Secção B</td> <td>Indústrias extractivas</td> </tr> <tr> <td rowspan="3">4</td> <td>Divisão 10</td> <td>Indústrias alimentares</td> </tr> <tr> <td>Divisão 11</td> <td>Indústria das bebidas</td> </tr> <tr> <td>Divisão 12</td> <td>Indústria do tabaco</td> </tr> <tr> <td rowspan="3">5</td> <td>Divisão 13</td> <td>Indústrias têxteis</td> </tr> <tr> <td>Divisão 14</td> <td>Indústria do vestuário</td> </tr> <tr> <td>Divisão 15</td> <td>Indústria do couro e dos produtos do couro</td> </tr> <tr> <td>6</td> <td>Divisão 16</td> <td>Indústrias da madeira e da cortiça e suas obras, excepto mobiliário; fabricação de artigos de espartaria e cestaria</td> </tr> <tr> <td rowspan="2">7</td> <td>Divisão 17</td> <td>Fabricação de pasta, de papel, de cartão e seus artigos</td> </tr> <tr> <td>Divisão 18</td> <td>Impressão e reprodução de suportes gravados</td> </tr> <tr> <td>8</td> <td>Divisão 19</td> <td>Fabricação de coque e de produtos petrolíferos refinados</td> </tr> <tr> <td rowspan="3">9</td> <td>Divisão 20</td> <td>Fabricação de produtos químicos e de fibras sintéticas e artificiais</td> </tr> <tr> <td>Divisão 21</td> <td>Fabricação de produtos farmacêuticos de base e de preparações farmacêuticas</td> </tr> <tr> <td>Divisão 22</td> <td>Fabricação de artigos de borracha e de matérias plásticas</td> </tr> <tr> <td>10</td> <td>Divisão 23</td> <td>Fabricação de outros produtos minerais não metálicos</td> </tr> <tr> <td rowspan="2">11</td> <td>Divisão 24</td> <td>Fabricação de metais de base</td> </tr> <tr> <td>Divisão 25</td> <td>Fabricação de produtos metálicos, excepto máquinas e equipamento</td> </tr> <tr> <td rowspan="5">12</td> <td>Divisão 26</td> <td>Fabricação de equipamentos informáticos, equipamentos para comunicação, produtos electrónicos e ópticos</td> </tr> <tr> <td>Divisão 27</td> <td>Fabricação de equipamento eléctrico</td> </tr> <tr> <td>Divisão 28</td> <td>Fabricação de máquinas e equipamentos, n.e.</td> </tr> <tr> <td>Divisão 29</td> <td>Fabricação de veículos automóveis, reboques e semi-reboques</td> </tr> <tr> <td>Divisão 30</td> <td>Fabricação de outro equipamento de transporte</td> </tr> <tr> <td rowspan="3">13</td> <td>Divisão 31</td> <td>Fabricação de mobiliário e de colchões</td> </tr> <tr> <td>Divisão 32</td> <td>Outras indústrias transformadoras</td> </tr> <tr> <td>Divisão 33</td> <td>Reparação, manutenção e instalação de máquinas e equipamentos</td> </tr> <tr> <td>14</td> <td>Secção D</td> <td>Produção e distribuição de electricidade, gás, vapor e ar frio</td> </tr> <tr> <td rowspan="3">15</td> <td>Divisão 36</td> <td>Captação, tratamento e distribuição de água</td> </tr> <tr> <td>Divisão 37</td> <td>Recolha e tratamento de águas residuais</td> </tr> <tr> <td>Divisão 39</td> <td>Actividades de despoluição e outros serviços de gestão de resíduos</td> </tr> <tr> <td>16</td> <td>Divisão 38</td> <td>Actividades de recolha, tratamento e eliminação de resíduos; recuperação de materiais</td> </tr> <tr> <td>17</td> <td>Secção F</td> <td>Construção</td> </tr> <tr> <td rowspan="16">18</td> <td></td> <td>Actividades de serviços:</td> </tr> <tr> <td>Secção G, excepto 46.77</td> <td>Comércio por grosso e a retalho; reparação de veículos automóveis e motociclos</td> </tr> <tr> <td>Secção H</td> <td>Transportes e armazenagem</td> </tr> <tr> <td>Secção I</td> <td>Actividades de alojamento e restauração</td> </tr> <tr> <td>Secção J</td> <td>Informação e comunicação</td> </tr> <tr> <td>Secção K</td> <td>Actividades financeiras e de seguros</td> </tr> <tr> <td>Secção L</td> <td>Actividades imobiliárias</td> </tr> <tr> <td>Secção M</td> <td>Actividades de consultoria, científicas, técnicas e similares</td> </tr> <tr> <td>Secção N</td> <td>Actividades administrativas e dos serviços de apoio</td> </tr> <tr> <td>Secção O</td> <td>Administração pública e defesa; segurança social obrigatória</td> </tr> <tr> <td>Secção P</td> <td>Educação</td> </tr> <tr> <td>Secção Q</td> <td>Saúde humana e acção social</td> </tr> <tr> <td>Secção R</td> <td>Actividades artísticas, de espectáculos e recreativas</td> </tr> <tr> <td>Secção S</td> <td>Outras actividades de serviços</td> </tr> <tr> <td>Secção T</td> <td>Actividades das famílias empregadoras de pessoal doméstico; actividades de produção de bens e serviços pelas famílias para uso próprio</td> </tr> <tr> <td>Secção U</td> <td>Actividades dos organismos internacionais e outras instituições extraterritoriais</td> </tr> <tr> <td>19</td> <td>Classe 46.77</td> <td>Comércio por grosso de desperdícios e sucata</td> </tr> <tr> <td>20</td> <td></td> <td>Resíduos domésticos (Não é uma categoria da NACE.)</td> </tr> <tr> <td>TA</td> <td>Total</td> <td>Total</td> </tr> </tbody> </table>

**Lista D — Sinal de confidencialidade**

| Número demasiado reduzido de empresas | A | Por exemplo, 1 ou 2 empresas na população |
|---|---|---|
| Uma só empresa domina os dados | B | Número de empresas não demasiado reduzido, mas uma empresa produz/valoriza, por exemplo, mais de 70 % |
| Duas empresas dominam os dados | C | Número de empresas não demasiado reduzido, mas duas empresas produzem/valorizam, por exemplo, mais de 70 % |
| Dados confidenciais devido a confidencialidade de segundo grau | D | Não confidencial em si (sinal A, B, C), mas para evitar revelação indirecta de dados confidenciais |
| O valor não é confidencial | Branco |  |

**Lista E — Categorias de resíduos para incineração**

<table> <tbody> <tr> <td rowspan="2">Artigo de resíduos</td> <td colspan="2">CER-Stat/versão 3 (JO L 90 de 27.3.2004, p. 15)</td> <td rowspan="2">Resíduos perigosos/não perigosos</td> </tr> <tr> <td>Código</td> <td>Descrição</td> </tr> <tr> <td>1</td> <td>01 + 02 + 03</td> <td>Resíduos químicos (Resíduos de compostos químicos + resíduos de reacções químicas + outros resíduos químicos)</td> <td>Não perigosos</td> </tr> <tr> <td>2</td> <td>01 + 02 + 03 excl. 01.3</td> <td>Resíduos químicos, com exclusão dos óleos usados (Resíduos de compostos químicos + resíduos de reacções químicas + outros resíduos químicos)</td> <td>Perigosos</td> </tr> <tr> <td>3</td> <td>01.3</td> <td>Óleos usados</td> <td>Perigosos</td> </tr> <tr> <td>4</td> <td>05</td> <td>Resíduos da prestação de cuidados de saúde e biológicos</td> <td>Não perigosos</td> </tr> <tr> <td>5</td> <td>05</td> <td>Resíduos da prestação de cuidados de saúde e biológicos</td> <td>Perigosos</td> </tr> <tr> <td>6</td> <td>07.7</td> <td>Resíduos contendo PCB</td> <td>Perigosos</td> </tr> <tr> <td>7</td> <td>10.1</td> <td>Resíduos domésticos e similares</td> <td>Não perigosos</td> </tr> <tr> <td>8</td> <td>10.2</td> <td>Materiais mistos e não diferenciados</td> <td>Não perigosos</td> </tr> <tr> <td>9</td> <td>10.2</td> <td>Materiais mistos e não diferenciados</td> <td>Perigosos</td> </tr> <tr> <td>10</td> <td>10.3</td> <td>Resíduos de triagem</td> <td>Não perigosos</td> </tr> <tr> <td>11</td> <td>10.3</td> <td>Resíduos de triagem</td> <td>Perigosos</td> </tr> <tr> <td>12</td> <td>11</td> <td>Lamas comuns</td> <td>Não perigosos</td> </tr> <tr> <td>13</td> <td>06 + 07 + 08 + 09 + 12 + 13</td> <td>Outros resíduos (Resíduos metálicos + resíduos não metálicos + equipamento fora de uso + resíduos de origem animal e de origem vegetal + resíduos minerais + resíduos solidificados, estabilizados ou vitrificados)</td> <td>Não perigosos</td> </tr> <tr> <td>14</td> <td>06 + 07 + 08 + 09 + 12 + 13 excl. 07.7</td> <td>Outros resíduos (Resíduos metálicos + resíduos não metálicos excluindo resíduos contendo PCB + equipamento fora de uso + resíduos de origem animal e de origem vegetal + resíduos minerais + resíduos solidificados, estabilizados ou vitrificados)</td> <td>Perigosos</td> </tr> <tr> <td>TN</td> <td></td> <td>Total, não perigosos</td> <td>Não perigosos</td> </tr> <tr> <td>TP</td> <td></td> <td>Total, perigosos</td> <td>Perigosos</td> </tr> <tr> <td>TT</td> <td></td> <td>Total geral</td> <td></td> </tr> </tbody> </table>

**Lista F — Operações de valorização e eliminação; os códigos remetem para os códigos dos anexos da Directiva 75/442/CEE**

<table> <tbody> <tr> <td>Operação</td> <td>Código</td> <td>Tipo de operações de valorização e eliminação</td> </tr> <tr> <td colspan="3">Incineração</td> </tr> <tr> <td>1</td> <td>R1</td> <td>Utilização principal como combustível ou outro meio de geração de energia</td> </tr> <tr> <td>2</td> <td>D10</td> <td>Incineração em terra</td> </tr> <tr> <td colspan="3">Operações que podem conduzir à valorização (com exclusão da valorização energética)</td> </tr> <tr> <td rowspan="10">3</td> <td>R2 +</td> <td>Recuperação/regeneração de solventes</td> </tr> <tr> <td>R3 +</td> <td>Reciclagem/recuperação de substâncias orgânicas não utilizadas como solventes (incluindo compostagem e outros processos de transformação biológica)</td> </tr> <tr> <td>R4 +</td> <td>Reciclagem/recuperação de metais e compostos metálicos</td> </tr> <tr> <td>R5 +</td> <td>Reciclagem/recuperação de outros materiais inorgânicos</td> </tr> <tr> <td>R6 +</td> <td>Regeneração de ácidos ou bases</td> </tr> <tr> <td>R7 +</td> <td>Valorização de componentes utilizados na redução da poluição</td> </tr> <tr> <td>R8 +</td> <td>Valorização de componentes de catalisadores</td> </tr> <tr> <td>R9 +</td> <td>Refinação de óleos e outras reutilizações de óleos</td> </tr> <tr> <td>R10 +</td> <td>Tratamento do solo para benefício agrícola ou melhoramento ambiental</td> </tr> <tr> <td>R11</td> <td>Utilização de resíduos obtidos em resultado de qualquer das operações R1 a R10</td> </tr> <tr> <td colspan="3">Operações de eliminação</td> </tr> <tr> <td rowspan="5">4</td> <td>D1 +</td> <td>Depósito na terra em profundidade ou à superfície (por exemplo, aterro, etc.)</td> </tr> <tr> <td>D3 +</td> <td>Depósito em aterro (por exemplo, injecção de resíduos por bombagem em poços, cúpulas salinas ou depósitos naturais, etc.)</td> </tr> <tr> <td>D4 +</td> <td>Lagunagem (por exemplo, descarga de resíduos líquidos ou de lamas em poços, lagos naturais ou artificiais, etc.)</td> </tr> <tr> <td>D5 +</td> <td>Depósitos subterrâneos especialmente concebidos (deposição em alinhamentos de células que são seladas e isoladas umas das outras e do ambiente, etc.)</td> </tr> <tr> <td>D12</td> <td>Armazenagem permanente (por exemplo, armazenagem de contentores numa mina, etc.)</td> </tr> <tr> <td rowspan="3">5</td> <td>D2 +</td> <td>Tratamento do solo (por exemplo, biodegradação de efluentes líquidos ou de lamas de depuração nos solos, etc.)</td> </tr> <tr> <td>D6 +</td> <td>Descarga para massas de águas, com excepção dos mares e dos oceanos</td> </tr> <tr> <td>D7</td> <td>Descargas para os mares e/ou oceanos, incluindo inserção nos fundos marinhos</td> </tr> </tbody> </table>

**Lista G — Categorias de resíduos para operações que podem levar à valorização (com exclusão da valorização energética)**

<table> <tbody> <tr> <td rowspan="2">Artigo de resíduos</td> <td colspan="2">CER-Stat/versão 3 (JO L 90 de 27.3.2004, p. 15)</td> <td rowspan="2">Resíduos perigosos/não perigosos</td> </tr> <tr> <td>Código</td> <td>Descrição</td> </tr> <tr> <td>1</td> <td>01.3</td> <td>Óleos usados</td> <td>Perigosos</td> </tr> <tr> <td>2</td> <td>06</td> <td>Resíduos metálicos</td> <td>Não perigosos</td> </tr> <tr> <td>3</td> <td>06</td> <td>Resíduos metálicos</td> <td>Perigosos</td> </tr> <tr> <td>4</td> <td>07.1</td> <td>Resíduos de vidro</td> <td>Não perigosos</td> </tr> <tr> <td>5</td> <td>07.1</td> <td>Resíduos de vidro</td> <td>Perigosos</td> </tr> <tr> <td>6</td> <td>07.2</td> <td>Resíduos de papel e cartão</td> <td>Não perigosos</td> </tr> <tr> <td>7</td> <td>07.3</td> <td>Resíduos de borracha</td> <td>Não perigosos</td> </tr> <tr> <td>8</td> <td>07.4</td> <td>Resíduos de plásticos</td> <td>Não perigosos</td> </tr> <tr> <td>9</td> <td>07.5</td> <td>Resíduos de madeira</td> <td>Não perigosos</td> </tr> <tr> <td>10</td> <td>07.6</td> <td>Resíduos têxteis</td> <td>Não perigosos</td> </tr> <tr> <td>11</td> <td>09 excl. 09.11, 09.3</td> <td>Resíduos de origem animal e de origem vegetal (com exclusão dos resíduos de origem animal de preparados e produtos alimentares, bem como fezes, urina e estrume de animais)</td> <td>Não perigosos</td> </tr> <tr> <td>12</td> <td>09.11</td> <td>Resíduos de origem animal de preparados e produtos alimentares</td> <td>Não perigosos</td> </tr> <tr> <td>13</td> <td>09.3</td> <td>Fezes, urina e estrume de animais</td> <td>Não perigosos</td> </tr> <tr> <td>14</td> <td>12</td> <td>Resíduos minerais</td> <td>Não perigosos</td> </tr> <tr> <td>15</td> <td>12</td> <td>Resíduos minerais</td> <td>Perigosos</td> </tr> <tr> <td>16</td> <td>01 + 02 + 03 + 05 + 08 + 10 + 11 + 13</td> <td>Outros resíduos (resíduos de compostos químicos + resíduos de reacções químicas + outros resíduos químicos + resíduos da prestação de cuidados de saúde e biológicos + equipamento fora de uso + resíduos mistos comuns + lamas comuns + resíduos solidificados, estabilizados ou vitrificados)</td> <td>Não perigosos</td> </tr> <tr> <td>17</td> <td>01 + 02 + 03 + 05 + 07.5 + 07.7 + 08 + 10 + 11 + 13 excl. 01.3</td> <td>Outros resíduos (resíduos de compostos químicos com exclusão dos óleos usados + resíduos de reacções químicas + outros resíduos químicos + resíduos da prestação de cuidados de saúde e biológicos + resíduos de madeira + resíduos contendo PCB + equipamento fora de uso + resíduos mistos comuns + lamas comuns + resíduos solidificados, estabilizados ou vitrificados)</td> <td>Perigosos</td> </tr> <tr> <td>TN</td> <td></td> <td>Total, não perigosos</td> <td>Não perigosos</td> </tr> <tr> <td>TP</td> <td></td> <td>Total perigosos</td> <td>Perigosos</td> </tr> <tr> <td>TT</td> <td></td> <td>Total geral</td> <td></td> </tr> </tbody> </table>

**Lista H — Categorias de resíduos para eliminação (excepto incineração)**

<table> <tbody> <tr> <td rowspan="2">Número do artigo</td> <td colspan="2">CER-Stat/versão 3 (JO L 90 de 27.3.2004, p. 15)</td> <td rowspan="2">Resíduos perigosos/não perigosos</td> </tr> <tr> <td>Código</td> <td>Descrição</td> </tr> <tr> <td>1</td> <td>01 + 02 + 03</td> <td>Resíduos químicos (Resíduos de compostos químicos + resíduos de reacções químicas + outros resíduos químicos)</td> <td>Não perigosos</td> </tr> <tr> <td>2</td> <td>01 + 02 + 03 excl. 01.3</td> <td>Resíduos químicos, com exclusão dos óleos usados (Resíduos de compostos químicos + resíduos de reacções químicas + outros resíduos químicos)</td> <td>Perigosos</td> </tr> <tr> <td>3</td> <td>01.3</td> <td>Óleos usados</td> <td>Perigosos</td> </tr> <tr> <td>4</td> <td>09 excl. 09.11, 09.3</td> <td>Resíduos de origem animal e de origem vegetal (excluindo os resíduos de origem animal de preparados e produtos alimentares, bem como fezes, urina e estrume de animais)</td> <td>Não perigosos</td> </tr> <tr> <td>5</td> <td>09.11</td> <td>Resíduos de origem animal de preparados e produtos alimentares</td> <td>Não perigosos</td> </tr> <tr> <td>6</td> <td>09.3</td> <td>Fezes, urina e estrume de animais</td> <td>Não perigosos</td> </tr> <tr> <td>7</td> <td>10.1</td> <td>Resíduos domésticos e similares</td> <td>Não perigosos</td> </tr> <tr> <td>8</td> <td>10.2</td> <td>Materiais mistos e não diferenciados</td> <td>Não perigosos</td> </tr> <tr> <td>9</td> <td>10.2</td> <td>Materiais mistos e não diferenciados</td> <td>Perigosos</td> </tr> <tr> <td>10</td> <td>10.3</td> <td>Resíduos de triagem</td> <td>Não perigosos</td> </tr> <tr> <td>11</td> <td>10.3</td> <td>Resíduos de triagem</td> <td>Perigosos</td> </tr> <tr> <td>12</td> <td>11</td> <td>Lamas comuns</td> <td>Não perigosos</td> </tr> <tr> <td>13</td> <td>12</td> <td>Resíduos minerais</td> <td>Não perigosos</td> </tr> <tr> <td>14</td> <td>12</td> <td>Resíduos minerais</td> <td>Perigosos</td> </tr> <tr> <td>15</td> <td>05 + 06 + 07 + 08 + 13</td> <td>Outros resíduos (Resíduos da prestação de cuidados de saúde e biológicos + resíduos de metais + resíduos não metálicos + equipamento fora de uso + resíduos solidificados, estabilizados ou vitrificados)</td> <td>Não perigosos</td> </tr> <tr> <td>16</td> <td>05 + 06 + 07 + 08 + 13</td> <td>Outros resíduos (Resíduos da prestação de cuidados de saúde e biológicos + resíduos de metais + resíduos não metálicos + equipamento fora de uso + resíduos solidificados, estabilizados ou vitrificados)</td> <td>Perigosos</td> </tr> <tr> <td>TN</td> <td></td> <td>Total, não perigosos</td> <td>Não perigosos</td> </tr> <tr> <td>TP</td> <td></td> <td>Total, perigosos</td> <td>Perigosos</td> </tr> <tr> <td>TT</td> <td></td> <td>Total geral</td> <td></td> </tr> </tbody> </table>

**Lista I — Medida de capacidade**

| Operação | Medida de capacidade | Código da medida |
|---|---|---|
| 1 | Milhares de toneladas por ano, com três posições decimais | t |
|  | Terajoules por ano (1012) | j |
| 2 | Milhares de toneladas por ano, com três posições decimais | t |
|  | Terajoules por ano (1012) | j |
| 3 | Milhares de toneladas por ano, com três posições decimais | t |
| 4 | Metros cúbicos por ano | m |
| 5 | Milhares de toneladas por ano, com três posições decimais | t |

(

1

) JO L 332 de 9.12.2002, p. 1. Regulamento com a última redacção que lhe foi dada pelo Regulamento (CE) n.º 574/2004 (JO L 90 de 27.3.2004, p. 15).

(

2

) JO L 181 de 28.6.1989, p. 47.
