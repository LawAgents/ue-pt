---
id: "regulamento-ue-2010-1089-anexo-v-a-anexo-vii"
celex: "32010R1089"
title: "Regulamento (UE) n. ° 1089/2010 da Comissão, de 23 de Novembro de 2010 , que estabelece as disposições de execução da Directiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Anexo V a Anexo VII"
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
part: "Anexo V a Anexo VII"
---

# Regulamento (UE) n. ° 1089/2010 da Comissão, de 23 de Novembro de 2010 , que estabelece as disposições de execução da Directiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Anexo V a Anexo VII

## Anexo V — REGRAS DE EXECUÇÃO PARA OS SERVIÇOS DE DADOS GEOGRÁFICOS INVOCÁVEIS

**PARTE A**

**Convenções de escrita**

À semelhança do Regulamento (CE) n.º 1205/2008, são utilizadas as seguintes convenções de escrita para os metadados do serviço de dados geográficos.

Quando indicado na descrição dos elementos dos metadados, os domínios de valores serão utilizados com a multiplicidade expressa nos quadros correspondentes. Em relação a um determinado domínio, cada valor é definido por:

— um identificador numérico;

— um nome textual para os utilizadores humanos, que pode ser traduzido nas diferentes línguas comunitárias;

— um nome linguisticamente neutro para os computadores (valor expresso entre parêntesis);

— uma descrição ou definição opcional.

O quadro apresenta as seguintes informações:

— a primeira coluna indica a referência ao parágrafo do anexo que define o elemento de metadados ou o grupo de elementos de metadados;

— a segunda coluna indica o nome do elemento de metadados ou do grupo de elementos de metadados;

— a terceira coluna indica a multiplicidade de um elemento de metadados. A expressão da multiplicidade segue a notação de multiplicidade da linguagem de modelação unificada (Unified Modelling Language — UML), em que:

— N significa que só poderá haver N ocorrências deste elemento de metadados num conjunto de resultados,

— 1..* significa que deve haver, pelo menos, uma ocorrência deste elemento de metadados num conjunto de resultados,

— 0..1 indica que a presença do elemento de metadados num conjunto de resultados é condicional, mas pode ocorrer apenas uma vez,

— 0..* indica que a presença do elemento de metadados num conjunto de resultados é condicional, mas que pode haver uma ou mais ocorrências desse elemento,

— quando a multiplicidade é 0..1 ou 0..*, a condição define quando o elemento de metadados é obrigatório;

— a quarta coluna contém uma declaração condicional se a multiplicidade do elemento não se aplicar a todos os tipos de recursos. Todos os elementos são obrigatórios noutras circunstâncias.

**PARTE B**

**Elemento de metadados «Categoria»**

**1. Categoria**

Trata-se de uma referência ao estatuto do serviço de dados geográficos face à invocabilidade.

O domínio de valores deste elemento de metadados é o seguinte:

**1.1. Invocável (invocable)**

O serviço de dados geográficos é um serviço de dados geográficos invocável.

**1.2. Interoperável (interoperable)**

O serviço de dados geográficos invocável é um serviço de dados geográficos interoperável.

**1.3. Harmonizado (harmonised)**

O serviço de dados geográficos interoperável é um serviço de dados geográficos harmonizado.

**PARTE C**

**Instruções sobre multiplicidade e condições dos elementos de metadados**

Os novos metadados que descrevem o serviço de dados geográficos devem incluir os elementos de metadados ou grupos de elementos de metadados que constam da lista do quadro 1.

Esses elementos de metadados ou grupos de elementos de metadados devem estar em conformidade com a multiplicidade prevista e as respetivas condições enumeradas no quadro 1.

Quando não são indicadas condições para um determinado elemento de metadados, esse elemento é obrigatório.

**Quadro 1**

**Metadados para serviços de dados geográficos invocáveis**

| Referência | Novos elementos de metadados | Multiplicidade | Condição |
|---|---|---|---|
| 1 | Categoria | 0..1 | obrigatórios para um serviço de dados geográficos invocável |

**PARTE D**

**Requisitos adicionais sobre metadados previstos no Regulamento (CE) n.º 1205/2008**

**1. Localizador do recurso**

O elemento de metadados Localizador do Recurso estabelecido no Regulamento (CE) n.º 1205/2008 deve também conter todos os pontos de acesso do prestador de serviços de dados geográficos e esses pontos de acesso devem ser inequivocamente identificados como tal.

**2. Especificação**

O elemento de metadados Especificação estabelecido no Regulamento (CE) n.º 1205/2008 deve também referir ou conter especificações técnicas (como as orientações técnicas INSPIRE, mas não só), com as quais o serviço de dados geográficos invocável está totalmente conforme, fornecendo todos os elementos técnicos necessários (humanos e, sempre que relevante, legíveis por máquina) a fim de permitir a respetiva invocação.

## Anexo VI — REGRAS DE EXECUÇÃO PARA A INTEROPERABILIDADE DOS SERVIÇOS DE DADOS GEOGRÁFICOS INVOCÁVEIS

**PARTE A**

**Requisitos adicionais sobre metadados previstos no Regulamento (CE) n.º 1205/2008**

**1. Condições de acesso e utilização aplicáveis**

As restrições técnicas aplicáveis ao acesso e utilização dos serviços de dados geográficos devem ser documentadas no elemento de metadados «RESTRIÇÕES RELACIONADAS COM O ACESSO E UTILIZAÇÃO», estabelecido no Regulamento (CE) n.º 1205/2008.

**2. Entidade responsável**

A entidade responsável prevista no Regulamento (CE) n.º 1205/2008 deve, pelo menos, descrever a organização tutora (custodian) responsável, correspondente à função de tutor estabelecida no Regulamento (CE) n.º 1205/2008.

**PARTE B**

**Elementos de metadados**

**3. Identificador de sistemas de referência de coordenadas**

Se for caso disso, trata-se da lista de sistemas de referência de coordenadas compatíveis com o serviço de dados geográficos.

Cada sistema de referência de coordenadas compatível deve ser expresso por meio de um identificador.

**4. Qualidade do serviço**

É a qualidade mínima do serviço estimada pela entidade responsável pelo serviço de dados geográficos e que se espera seja válida durante um certo tempo.

**4.1. Critérios**

São os critérios a que as medições se referem.

O domínio de valores deste elemento de metadados é o seguinte:

**4.1.1. Disponibilidade (availability)**

Descreve a percentagem de tempo em que o serviço está disponível.

**4.1.2. Desempenho (performance)**

Descreve a rapidez com que um pedido ao serviço de dados geográficos pode ser satisfeito.

**4.1.3. Capacidade (capacity)**

Descreve o número máximo de pedidos simultâneos que podem ser satisfeitos com o desempenho declarado.

**4.2. Medição**

**4.2.1. Descrição**

Descreve a medição para cada critério.

O domínio de valores deste elemento de metadados é texto livre.

**4.2.2. Valor (value)**

Descreve o valor da medição para cada critério.

O domínio de valores deste elemento de metadados é texto livre.

**4.2.3. Unidade (unit)**

Descreve a unidade da medição para cada critério.

O domínio de valores deste elemento de metadados é texto livre.

**PARTE C**

**Instruções sobre multiplicidade e condições dos elementos de metadados**

Os metadados que descrevem um serviço de dados geográficos interoperável devem incluir os elementos de metadados ou grupos de elementos de metadados que constam da lista do quadro 1.

Esses elementos de metadados ou grupos de elementos de metadados devem estar em conformidade com a multiplicidade prevista e as respetivas condições enumeradas no quadro 1.

Quando não são indicadas condições para um determinado elemento de metadados, esse elemento é obrigatório.

**Quadro 1**

**Metadados para serviços de dados geográficos interoperáveis**

| Referência | Novos elementos de metadados | Multiplicidade | Condição |
|---|---|---|---|
| 1 | Identificador de sistemas de referência de coordenadas | 1..* | Obrigatório, se pertinente |
| 2 | Qualidade do serviço | 3..* |  |

## Anexo VII — REGRAS DE EXECUÇÃO PARA A HORMONIZAÇÃO DOS SERVIÇOS DE DADOS GEOGRÁFICOS INTEROPERÁVEIS

**PARTE A**

**Características**

**1. Qualidade do serviço**

A probabilidade de um serviço de dados geográficos harmonizado estar disponível deve ser de 98 %.

**2. Codificação de saída**

Um serviço de dados geográficos harmonizados que forneça objetos geográficos no quadro da Diretiva 2007/2/CE deve codificar esses objetos geográficos em conformidade com o presente regulamento.

**PARTE B**

**Elementos de metadados**

**3. Metadados de invocação**

O elemento de metadados de invocação documenta as interfaces do serviço de dados geográficos harmonizado e enumera os pontos terminais para permitir a comunicação máquina-máquina.

**PARTE C**

**Instruções sobre multiplicidade e condições dos elementos de metadados**

O serviço de dados geográficos harmonizado deve incluir o elemento de metadados ou o grupo de elementos de metadados que consta da lista do quadro 1.

Esse elemento de metadados ou grupo de elementos de metadados deve ser conforme com a multiplicidade prevista e as condições conexas constantes do quadro 1.

Quando não são indicadas condições para um determinado elemento de metadados, esse elemento é obrigatório.

**Quadro 1**

**Metadados para serviços de dados geográficos harmonizados**

| Referência | Novos elementos de metadados | Multiplicidade | Condição |
|---|---|---|---|
| 1 | Metadados de invocação | 1..* |  |

**PARTE D**

**Operações**

**1. Lista de operações**

Um serviço de dados geográficos harmonizado deve assegurar a execução da operação indicada no quadro 2.

**Quadro 2**

**Operações dos serviços de dados geográficos harmonizados**

| Operação | Função |
|---|---|
| Obter metadados do serviço de dados geográficos harmonizado | Fornece todas as informações necessárias acerca do serviço e descreve as suas capacidades |

**2. Operação «Obter metadados do serviço de dados geográficos harmonizado»**

**2.1. Pedido «Obter metadados do serviço de dados geográficos harmonizado»**

**2.1.1. Parâmetros do pedido «Obter metadados do serviço de dados geográficos harmonizado»**

O parâmetro do pedido «Obter metadados do serviço de dados geográficos harmonizado» indica a linguagem natural do conteúdo da resposta a «Obter metadados do serviço de dados geográficos harmonizado».

**2.2. Resposta a «Obter metadados do serviço de dados geográficos harmonizado»**

A resposta a «Obter metadados do serviço de dados geográficos harmonizado» deve conter os seguintes conjuntos de parâmetros:

— Metadados do serviço de dados geográficos harmonizado;

— Metadados das operações;

— Linguagens.

**2.2.1. Parâmetros «Metadados do serviço de dados geográficos harmonizado»**

Os parâmetros «Metadados do serviço de dados geográficos harmonizados» devem conter, pelo menos, os elementos de metadados INSPIRE do serviço de dados geográficos harmonizado estabelecidos pelo presente regulamento e pelo Regulamento (CE) n.º 1205/2008.

**2.2.2. Parâmetros «Metadados das operações»**

O parâmetro «Metadados das operações» fornece metadados acerca das operações do serviço de dados geográficos harmonizado. Deve, pelo menos, descrever cada operação, incluindo, no mínimo, uma descrição dos dados transferidos e o endereço de rede.

**2.2.3. Parâmetro «Linguagens»**

Devem ser fornecidos dois parâmetros respeitantes às linguagens:

— O parâmetro «Linguagem da resposta» (Response Language), que indica a linguagem natural utilizada nos parâmetros da resposta ao pedido «Obter os metadados do serviço de dados geográficos harmonizado»;

— O parâmetro «Linguagens disponíveis», que contém a lista das linguagens naturais utilizadas pelo serviço de dados geográficos harmonizado.

(

1

) Regulamento (CE) n.º 976/2009 da Comissão, de 19 de outubro de 2009, que estabelece as disposições de execução da Diretiva 2007/2/CE do Parlamento Europeu e do Conselho no que respeita aos serviços de rede (JO L 274 de 20.10.2009, p. 9).

(

2

) Regulamento (CE) n.º 1205/2008 da Comissão, de 3 de dezembro de 2008, que estabelece as modalidades de aplicação da Diretiva 2007/2/CE do Parlamento Europeu e do Conselho em matéria de metadados (JO L 326 de 4.12.2008, p. 12).

(

3

)

JO L 326 de 4.12.2008, p. 12.

(

4

)

JO L 274 de 20.10.2009, p. 9.

(

5

)

JO L 393 de 30.12.2006, p. 1.

(

6

)

JO L 393 de 30.12.2006, p. 1.

(

7

)

JO L 332 de 9.12.2002, p. 1.

(

8

)

JO L 312 de 22.11.2008, p. 3.

(

9

)

JO L 145 de 4.6.2008, p. 65.

(

10

)

JO L 226 de 6.9.2000, p. 3.

(

11

) Diretiva 92/43/CEE do Conselho, de 21 de maio de 1992, relativa à preservação dos habitats naturais e da fauna e da flora selvagens (JO L 206 de 22.7.1992, p. 7).

(

12

) Regulamento (CE) n.º 166/2006 do Parlamento Europeu e do Conselho, de 18 de janeiro de 2006, relativo à criação do Registo Europeu das Emissões e Transferências de Poluentes e que altera as Diretivas 91/689/CEE e 96/61/CE do Conselho (JO L 33 de 4.2.2006, p. 1).

(

13

) Diretiva 2010/75/UE do Parlamento Europeu e do Conselho, de 24 de novembro de 2010, relativa às emissões industriais (prevenção e controlo integrados da poluição) (JO L 334 de 17.12.2010. p. 17).

(

14

) Diretiva 2008/56/CE do Parlamento Europeu e do conselho, de 17 de junho de 2008, que estabelece um quadro de ação comunitária no domínio da política para o meio marinho (Diretiva-Quadro «Estratégia Marinha») (JO L 164 de 25.6.2008, p. 19.)

(

15

) Decisão de Execução 2011/484/UE da Comissão, de 11 de julho de 2011, relativa a um formulário de informações sobre os sítios da rede Natura 2000 (JO L 198 de 30.7.2011, p. 39).

(

16

)

JO L 140 de 5.6.2009, p. 16.
