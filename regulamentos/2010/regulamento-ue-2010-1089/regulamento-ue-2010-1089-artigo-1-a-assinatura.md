---
id: "regulamento-ue-2010-1089-artigo-1-a-assinatura"
celex: "32010R1089"
title: "Regulamento (UE) n. ° 1089/2010 da Comissão, de 23 de Novembro de 2010 , que estabelece as disposições de execução da Directiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Artigo 1.º a Assinatura"
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
part: "Artigo 1.º a Assinatura"
---

# Regulamento (UE) n. ° 1089/2010 da Comissão, de 23 de Novembro de 2010 , que estabelece as disposições de execução da Directiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos — Artigo 1.º a Assinatura

## Artigo 1.º — Objeto e âmbito de aplicação

1. O presente regulamento estabelece os requisitos relativos às disposições técnicas de interoperabilidade e, quando exequível, à harmonização dos conjuntos e serviços de dados geográficos correspondentes às categorias temáticas enumeradas nos anexos I, II e III da Diretiva 2007/2/CE.

2. O presente regulamento não se aplica aos serviços de rede que se inserem no âmbito de aplicação do Regulamento (CE) n.º 976/2009 da Comissão (

1

).

## Artigo 2.º — Definições

Para efeitos do presente regulamento, são aplicáveis as definições seguintes, bem como as definições específicas de temas constantes dos anexos:

1. «Tipo abstracto» (abstract type): um tipo que não pode ser instanciado, mas que pode ter atributos e associações;

2. «Associação» (association role): uma função que designa um valor ou objecto com o qual um tipo tem uma relação, conforme referido no artigo 8.º, n.º 2, alínea b), da Directiva 2007/2/CE;

3. «Atributo» (attribute), uma característica de um tipo, conforme referido no artigo 8.º, n.º 2, alínea c), da Directiva 2007/2/CE;

—————

5. «Lista de códigos» (code list): um tipo de dados cujas instâncias formam uma lista de valores literais denominados;

6. «Tipo de dados» (data type): descritor de um conjunto de valores sem identidade, em conformidade com

a norma ISO/TS 19103:2005 ;

—————

8. «Identificador de objecto externo» (external object identifier): um identificador de objecto único publicado pela entidade responsável, que pode ser utilizado em aplicações externas para referenciar o objecto geográfico;

9. «Identificador» (identifier): uma sequência de caracteres linguisticamente independente capaz de identificar de forma única e permanente aquilo a que está associada, em conformidade com

a norma EN ISO 19135:2007 ;

10. «Instanciar» (instantiate): criar um objecto que está em conformidade com a definição, os atributos, as associações e as restrições especificadas para o tipo instanciado;

11. «Camada» (layer): uma unidade de base de informação geográfica que pode ser solicitada a um servidor sob a forma de um mapa, em conformidade com

a norma EN ISO 19128:2008 ;

12. «Informação do ciclo de vida» (life-cycle information): um conjunto de propriedades de um objecto geográfico que descreve as características temporais de uma versão de um objecto geográfico ou as alterações entre versões;

13. «Elemento de metadados» (metadata element): uma unidade discreta de metadados, de acordo com o estabelecido

a norma EN ISO 19115:2005/AC:2008 ;

14. «Pacote» (package): um mecanismo para fins gerais de organização de elementos em grupos;

15. «Registo» (register

): um conjunto de ficheiros que contém identificadores atribuídos a itens com descrição dos itens associados, de acordo com

a norma EN ISO 19135:2007 ;

16. «Tipo de objecto geográfico» (spatial object type): uma classificação de objectos geográficos;

17. «Estilo» (style): a correspondência entre tipos de objectos geográficos e suas propriedades e restrições, por um lado, e os símbolos parametrizados utilizados no desenho de mapas, por outro;

18. «Subtipo de» (sub-type of): uma relação entre um tipo mais específico e um tipo mais geral, em que o tipo mais específico é plenamente coerente com o tipo mais geral e contém informação adicional, conforme adaptado

a norma ISO/TS 19103:2005 ;

19. «Tipo» (type): tipo de objecto geográfico ou de dados;

20. «Voidable»

(potencialmente vazio): o facto de, relativamente a um atributo ou associação, poder ser disponibilizado um valor «void»

(vazio) se os conjuntos de dados geográficos geridos pelos Estados-Membros não contiverem qualquer valor correspondente ou se não for possível derivar qualquer valor correspondente dos valores existentes a custos razoáveis. Se um atributo ou associação for «voidable,»

a célula da tabela que especifica a sua «voidability» (capacidade de estar potencialmente vazio) é deixada em branco;

21. «Propriedade»(property): um atributo ou associação;

22. «Tipo de união»(union type): um tipo que consiste numa, e apenas numa, de várias alternativas (enumeradas como atributos membros), em conformidade com a norma ISO/TS 19103:2005;

23. «Classe de associação»(association class): um tipo que define propriedades adicionais numa relação entre dois outros tipos;

24. «Cobertura»(coverage): um objeto geográfico que atua como uma função para fornecer valores da sua gama para qualquer posição direta dentro do seu domínio espacial, temporal ou espaciotemporal, em conformidade com a norma ISO 19123:2007;

25. «Domínio»(domain) um conjunto bem definido, em conformidade com a norma ISO/TS 19103:2005;

26. «Gama»(range): um conjunto de valores de atributos de características (features) associado por uma função com os elementos do domínio de uma cobertura, em conformidade com a norma EN ISO 19123:2007;

27. «Quadrícula retificada»(rectified grid): uma quadrícula em que existe uma transformação afim entre as coordenadas da quadrícula e as coordenadas de um sistema de referência de coordenadas, em conformidade com a norma EN ISO 19123:2007;

28. «Quadrícula referenciável»(referenceable grid): uma quadrícula associada a uma transformação que pode ser utilizada para converter valores de coordenadas de quadrículas em valores de coordenadas referenciadas a um sistema de referência de coordenadas externo, em conformidade com a norma EN ISO 19123:2007;

29. «Tesselação»(tessellation): a partição de um espaço num conjunto de subespaços contíguos com a mesma dimensão do espaço particionado; Uma tecelagem num espaço 2D consiste num conjunto de polígonos não sobrepostos que cobrem totalmente uma região de interesse;

30. «Valor mais restrito»(narrower value): um valor que tem uma relação hierárquica com um valor-mãe mais geral;

31. «Ponto terminal» («end point») o endereço Internet utilizado para solicitar diretamente uma operação realizada por um serviço de dados geográficos;

32. «Ponto de acesso» um endereço Internet que contém uma descrição pormenorizada de um serviço de dados geográficos, incluindo uma lista de pontos terminais, a fim de permitir a sua execução;

33. «Serviço de dados geográficos invocável»

tudo o que se segue —

a) um serviço de dados geográficos com metadados que satisfaz os requisitos do Regulamento (CE) n.º 1205/2008 da Comissão (

2

);

b) um serviço de dados geográficos em que, pelo menos, um localizador do recurso é um ponto de acesso;

c) um serviço de dados geográficos conforme com um conjunto documentado e publicamente disponível de especificações técnicas que fornece as informações necessárias para a sua execução;

34. «Serviço de dados geográficos interoperável» um serviço de dados geográficos invocável que satisfaz os requisitos do anexo VI;

35. «Serviço de dados geográficos harmonizado» um serviço de dados geográficos interoperável que satisfaz os requisitos do anexo VII;

36. «Serviço de dados geográficos conforme» um serviço de dados geográficos que satisfaz os requisitos do presente regulamento;

37. «Operação» uma ação apoiada por um serviço de dados geográficos;

38. «Interface» o conjunto designado de operações que caracterizam o comportamento de uma entidade, conforme definida na norma ISO 19119:2005.

## Artigo 3.º — Tipos comuns

Os tipos que são comuns a várias das categorias temáticas enumeradas nos anexos I, II e III da Directiva 2007/2/CE devem estar conformes com as definições e restrições e incluir os atributos e associações estabelecidos no anexo I.

## Artigo 4.º — Tipos para o intercâmbio e classificação de objectos geográficos

1. Para o intercâmbio e classificação de objetos geográficos a partir de conjuntos de dados que satisfaçam as condições estabelecidas no artigo 4.º da Diretiva 2007/2/CE, os Estados-Membros devem utilizar os tipos de objetos geográficos, os tipos de dados associados e as listas de códigos, definidos nos anexos II, III e IV do presente regulamento, no que diz respeito às categorias temáticas com as quais os conjuntos de dados estão relacionados.

2. Ao procederem ao intercâmbio de objetos geográficos, os Estados-Membros devem conformar-se às definições e restrições estabelecidas nos anexos e fornecer valores para todos os atributos e associações definidos nos anexos, relativamente aos tipos de objetos geográficos e tipos de dados correspondentes. No caso dos atributos e das associações potencialmente vazios para os quais não existam valores, os Estados-Membros podem omitir o valor.

—————

—————

## Artigo 5.º — Tipos

1. Para todos os tipos definidos no presente regulamento, é indicado entre parênteses um nome linguisticamente neutro para computadores no título da secção que especifica os requisitos desse tipo. Este nome linguisticamente neutro deve ser utilizado para fins de referência ao tipo correspondente na definição de um atributo ou associação.

2. Os tipos que são um subtipo de outro tipo devem também incluir todos os atributos e associações desse tipo.

3. Os tipos abstractos não são instanciados.

—————

## Artigo 6.º — Listas de códigos para os conjuntos de dados geográficos

1. As listas de códigos incluídas no presente regulamento estabelecem o glossário multilingue a utilizar para os atributos principais em conformidade com o artigo 8.º, n.º 2, alínea c), da Diretiva 2007/2/CE.

2. Incumbe à Comissão criar e operar um registo de listas de códigos INSPIRE ao nível da União para gerir e disponibilizar ao público os valores incluídos nas listas de códigos a que se refere o n.º 1.

3. Na manutenção e atualização dos valores das listas de códigos, a Comissão é assistida pelo grupo de peritos INSPIRE da Comissão.

4. As listas de códigos devem ser de um dos seguintes tipos:

a) Listas de códigos cujos valores incluem apenas os valores especificados no registo de listas de códigos INSPIRE;

b) Listas de códigos cujos valores incluem os valores especificados no registo de listas de códigos INSPIRE e valores mais restritos definidos pelos fornecedores dos dados;

c) Listas de códigos cujos valores incluem os valores especificados no registo de listas de códigos INSPIRE e valores adicionais, a qualquer nível, definidos pelos fornecedores dos dados;

d) Listas de códigos cujos valores incluem quaisquer valores definidos pelos fornecedores dos dados.

5. As listas de códigos podem ser hierárquicas. Os valores das listas de códigos hierárquicas podem ter um valor-mãe mais geral.

6. Quando, relativamente a um atributo cujo tipo seja uma das listas de códigos referidas no n.º 4, alíneas b), c) ou d), um fornecedor de dados apresentar um valor que não esteja especificado no registo de listas de códigos INSPIRE, esse valor, a sua definição e a sua etiqueta (label) devem ser disponibilizados noutro registo.

## Artigo 7.º — Codificação

1. Cada regra de codificação utilizada para codificar dados geográficos deve estar em conformidade com a norma EN ISO 19118. Em particular, deve especificar as regras de conversão do esquema (schema) aplicáveis a todos os tipos de objectos geográficos e a todos os atributos e associações, bem como a estrutura utilizada para os dados de saída.

2. Devem ser disponibilizadas todas as regras de codificação utilizadas para codificar dados geográficos.

2-A. Cada regra de codificação utilizada para codificar dados geográficos deve especificar também se devem ser representados (e como) os atributos e associações para os quais exista um valor correspondente que não faça parte dos conjuntos de dados geográficos mantidos pelo Estado-Membro ou não possa ser determinado a partir dos valores existentes a custos razoáveis.

## Artigo 8.º — Actualizações

1. Os Estados-Membros devem disponibilizar regularmente actualizações dos dados.

2. Todas as actualizações devem ser efectuadas o mais tardar 6 meses após a integração da alteração no conjunto de dados fonte, a menos que seja estabelecido

nos anexos um período diferente para uma determinada categoria temática de dados geográficos.

3. As atualizações dos dados devem ser disponibilizadas a todos os serviços de dados geográficos conexos, de acordo com o prazo referido no n.º 2.

## Artigo 9.º — Gestão de identificadores

1. O tipo de dados «Identifier» definido no ponto 2.1 do anexo I deve ser utilizado como um tipo para o identificador de objecto externo de um objecto geográfico.

2. O identificador de objecto externo para a identificação única de objectos geográficos não deve ser alterado durante o ciclo de vida de um objecto geográfico.

## Artigo 10.º — Ciclo de vida dos objectos geográficos

1. As diferentes versões do mesmo objecto geográfico serão sempre instâncias do mesmo tipo de objecto geográfico.

2. Os atributos «namespace» e «localId» do identificador de objecto externo devem manter-se inalterados nas diferentes versões de um objecto geográfico.

3. Quando são utilizados os atributos «beginLifespanVersion» e «endLifespanVersion», o valor de «endLifespanVersion» não pode ser anterior ao valor de «beginLifespanVersion».

## Artigo 11.º — Sistemas de referência temporal

1. Deve ser utilizado o sistema de referência temporal predefinido referido no anexo, parte B, ponto 5, do Regulamento (CE) n.º 1205/2008 (

3

) da Comissão, salvo se forem especificados

nos anexos outros sistemas de referência temporal para uma determinada categoria temática de dados geográficos.

2. Se forem utilizados outros sistemas de referência temporal, estes devem ser especificados nos metadados do conjunto de dados.

## Artigo 12.º — Outros requisitos e regras

1. O domínio de valores das propriedades geográficas definidas no presente regulamento deve limitar-se ao esquema geográfico «Simple Feature» conforme definido em Herring, John R. (ed.), OpenGIS® Implementation Standard for Geographic information – Simple feature access – Part 1: Common architecture, version 1.2.1, Open Geospatial Consortium, 2011, salvo quando indicação em contrário para um determinado tipo ou categoria temática de dados geográficos.

2. Todos os valores medidos devem ser expressos em

unidades SI ou unidades não-SI aceites para utilização com o Sistema Internacional de Unidades, salvo indicação em contrário para uma determinada categoria temática ou tipo de dados geográficos.

3. Quando são utilizados os atributos «validFrom» e «validTo», o valor de «validTo» não pode ser anterior ao valor de «validFrom».

4. Além disso, são aplicáveis todos os requisitos relativos a categorias temáticas estabelecidos no anexo II.

## Artigo 13.º — Metadados necessários para fins de interoperabilidade

Os metadados que descrevem um conjunto de dados geográficos devem incluir os seguintes elementos de metadados necessários para fins de interoperabilidade:

1. Sistema de referência de coordenadas : descrição do(s) sistema(s) de referência de coordenadas utilizado(s) no conjunto de dados.

2. Sistema de referência temporal :

descrição do(s) sistema(s) de referência temporal utilizado(s) no conjunto de dados.

Este elemento é obrigatório apenas quando o conjunto de dados geográficos contém informações temporais que não se referem ao sistema de referência temporal predefinido.

3. Codificação : descrição da(s) estrutura(s) da linguagem informática, especificando a representação dos objectos de dados num registo, ficheiro, mensagem, dispositivo de armazenamento ou canal de transmissão.

4. Coerência topológica :

exactidão das características topológicas explicitamente codificadas do conjunto de dados, conforme descritas no âmbito de aplicação.

Este elemento é obrigatório apenas se o conjunto de dados incluir tipos do Modelo Genérico de Rede (Generic Network Model) e não garantir a topologia do eixo (ou seja, a conectividade dos eixos) da rede.

5. Codificação de caracteres :

a codificação de caracteres utilizada no conjunto de dados.

Este elemento é obrigatório apenas quando a codificação utilizada não se baseia em UTF-8.

6. Tipo de representação espacial :

o método a utilizar para representar espacialmente a informação geográfica.

## Artigo 14.º — Representação

1. Para a representação de conjuntos de dados geográficos com recurso a um serviço de visualização de rede conforme especificado no Regulamento (CE) n.º 976/2009 (

4

), devem estar disponíveis os seguinte elementos:

(a) As camadas especificadas no anexo II relativas à ou às categorias temáticas com as quais o conjunto de dados está relacionado;

(b) Em relação a cada camada, pelo menos um estilo de representação predefinido, no mínimo com um título associado e um identificador único.

2. Em relação a cada camada, o anexo II define o seguinte:

(a) Um título da camada legível para as pessoas a utilizar para visualização na interface do utilizador;

(b) O tipo ou tipos de objetos geográficos, ou um subconjunto destes, que constituem o conteúdo da camada.

3. Podem ser definidas várias camadas em relação a tipos de objetos geográficos cujos objetos podem ser classificados mais pormenorizadamente utilizando um atributo com um valor na lista de códigos. Cada uma destas camadas deve incluir os objetos geográficos correspondentes a um valor específico da lista de códigos. Na definição desses conjuntos de camadas nos anexos II, III e IV, devem ser cumpridos todos os seguintes requisitos:

a) O espaço reservado a <Valor de lista de códigos> deve representar os valores da lista de códigos relevante, com o primeiro caráter em maiúsculas.

b) O espaço reservado a <nome legível para as pessoas> deve representar o nome legível para as pessoas dos valores da lista de códigos;

c) O tipo de objeto geográfico deve incluir o atributo e a lista de códigos relevantes, entre parênteses;

d) Deve ser apresentado um exemplo de uma camada.

## Artigo 14.º-A — Requisitos para os serviços de dados geográficos invocáveis

O mais tardar em 10 de dezembro de 2015, os Estados-Membros devem fornecer os metadados dos serviços de dados geográficos invocáveis em conformidade com os requisitos estabelecidos no anexo V.

## Artigo 14.º-B — Acordos de interoperabilidade e requisitos de harmonização para os serviços de dados geográficos invocáveis

Os serviços de dados geográficos invocáveis respeitantes aos dados contidos em, pelo menos, um conjunto de dados geográficos conforme devem satisfazer os requisitos de interoperabilidade estabelecidos nos anexos V e VI e, se exequível, os requisitos de harmonização enunciados no anexo VII.

## Artigo 15.º — Entrada em vigor

O presente regulamento entra em vigor no [vigésimo] dia seguinte ao da sua publicação no Jornal Oficial da União Europeia.

O presente regulamento é aplicável a partir de 15 de Dezembro de 2010.

## Assinatura

O presente regulamento é obrigatório em todos os seus elementos e directamente aplicável em todos os Estados-Membros.
