- European Union law in Portuguese as markdown: base regulations and directives in force, one file per act, from the Publications Office of the EU.
- Each directive links to the Portuguese laws that transpose it. No delegated or implementing acts, decisions, treaties or Court of Justice case law.
- The same Claude Code plugin as the Portuguese repo (legislacao-pt) reads it with three extra commands: /lei-ue, /artigo-ue and /pesquisar-ue.
- Step-by-step guides in European Portuguese for non-programmers, plus a ready-made kit to build your own personal legal agent.
- Only the Official Journal of the EU is authentic: always confirm in EUR-Lex. Scripts and plugin are MIT; the texts are EU texts, reusable with attribution.

# Direito da União Europeia em português (LawAgents/ue-pt)

## O que é este repositório, o que cobre e o que não cobre

Este repositório guarda os regulamentos de base e as diretivas da União Europeia em vigor, em português, em markdown. É o par do repositório [LawAgents/pt](https://github.com/LawAgents/pt), que tem a legislação portuguesa. O plugin [legislacao-pt](https://github.com/LawAgents/legislacao-pt-plugin) é o mesmo para os dois: instala-se uma vez e ganha três comandos para a legislação da UE.

Cada ato é um ficheiro markdown, com os metadados no topo e cada artigo como título próprio (por exemplo "Artigo 17.º"). Os ficheiros ficam numa pasta por tipo e por ano do ato, por exemplo `regulamentos/2016/` e `diretivas/2019/`. Os ids seguem o formato `regulamento-ue-AAAA-N` e `diretiva-ue-AAAA-N`, com o ano em quatro dígitos e o número sem zeros à esquerda (o Regulamento (UE) 2016/679 é `regulamento-ue-2016-679`). Os atos grandes dividem-se em partes.

No fim de cada diretiva há uma secção "Transposição para Portugal" com as leis portuguesas que a executam. O id português só aparece quando esse diploma existe no repositório LawAgents/pt, e a ligação oficial só aparece quando o Serviço de Publicações a fornece.

Cobre. Os regulamentos de base e as diretivas em vigor que têm texto em português no Serviço de Publicações da União Europeia. Para cada ato escolhe-se o texto consolidado mais recente. Quando não há consolidado em português, entra o texto original, e a ficha e as respostas dizem "Texto original, sem consolidação: pode ter sido alterado depois." Numa medição de 2026-10-21 havia cerca de 4.010 atos só com o original.

Não cobre:

- Atos delegados e atos de execução.
- Decisões.
- Tratados.
- Jurisprudência do Tribunal de Justiça da União Europeia.
- Atos sem texto em português utilizável, sobretudo anteriores a 2000. Numa medição de 2026-10-21 eram cerca de 2.319 atos.
- Atos que deixaram de estar em vigor. Ficam fora da pasta principal e a lista `revogados.md` guarda o id, o título, a data do fim de vigência e a ligação oficial.
- Versões anteriores de um ato. O histórico fica no git, com um commit por atualização.
- Legislação portuguesa (está em LawAgents/pt).

Os ficheiros de índice na raiz (`nomes-comuns.md`, `indice.md`, `indice-regulamentos-*.md`, `indice-diretivas-*.md` e `revogados.md`) ajudam o agente a encontrar o ato certo sem ler tudo.

## Passo a passo para quem não programa

Escolhe um dos três caminhos. O primeiro é o completo.

### Caminho 1: plugin no Claude Code (o completo)

O plugin tem três comandos para a legislação da UE e cita sempre a fonte: `/lei-ue`, `/artigo-ue` e `/pesquisar-ue`. Os comandos da legislação portuguesa (`/lei`, `/artigo` e `/pesquisar-lei`) continuam iguais. O plugin só lê ficheiros públicos do GitHub, não escreve nada no teu computador e não envia as tuas perguntas a nenhum outro serviço.

1. Instala o Claude Code e abre-o numa pasta qualquer.
2. Escreve `/plugin marketplace add LawAgents/legislacao-pt-plugin` e carrega em Enter.
3. Escreve `/plugin install legislacao-pt@legislacao-pt` e carrega em Enter. Se já tens o plugin por causa da legislação portuguesa, atualiza-o em vez de instalares outro.
4. Experimenta `/artigo-ue RGPD 17`. A resposta termina com o bloco "Fontes" e a linha de aviso.
5. Opcional: cola o texto abaixo no ficheiro `CLAUDE.md` da tua pasta de trabalho.

```text
Para legislação da União Europeia usa sempre o plugin legislacao-pt (comandos /lei-ue, /artigo-ue e /pesquisar-ue).
Cita sempre a fonte: título completo, id do ato, ficheiro no repo, artigo e ligação do EUR-Lex.
Nunca inventes artigos, números de atos, datas ou ligações, e nunca respondas de memória.
Se o plugin não encontrar o que pedi, responde "Não encontrado no repo." e não cites nada.
Se o ato só tem o texto original, avisa: "Texto original, sem consolidação: pode ter sido alterado depois."
Termina com a linha: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
```

### Caminho 2: Projeto do Claude.ai com os atos como conhecimento

1. Abre o claude.ai e cria um Projeto novo.
2. Em https://github.com/LawAgents/ue-pt abre as pastas `regulamentos/` e `diretivas/` e descarrega os ficheiros dos atos de que precisas (em cada ficheiro, botão "Download raw file"). Nos atos divididos em partes, descarrega a visão geral e só as partes que vais usar.
3. No Projeto, abre a zona de conhecimento (Project knowledge) e carrega esses ficheiros.
4. Nas instruções do Projeto, cola o texto abaixo.

```text
Responde sobre legislação da União Europeia usando apenas os ficheiros carregados neste Projeto.
Cita sempre o artigo, o ficheiro de onde o tiraste e a ligação do EUR-Lex que consta no cabeçalho (campo source) desse ficheiro.
Nunca inventes artigos, números de atos, datas ou ligações, e nunca completes de memória.
Se a resposta não estiver nos ficheiros carregados, responde "Não encontrado nos ficheiros carregados." e não cites nada.
Se o campo text_version do ficheiro for "original sem consolidação", avisa: "Texto original, sem consolidação: pode ter sido alterado depois."
Termina sempre com: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
```

### Caminho 3: qualquer agente que leia ficheiros markdown ou abra ligações da web

Serve para agentes que leem uma pasta de ficheiros markdown ou que abrem endereços da web.

Forma A, o agente lê ficheiros. Descarrega o repositório (em https://github.com/LawAgents/ue-pt, botão "Code", "Download ZIP"), descomprime e aponta o agente para a pasta.

Forma B, o agente abre ligações. Dá-lhe o endereço https://github.com/LawAgents/ue-pt e diz-lhe que pode abrir os ficheiros pelo endereço "raw" do GitHub (https://raw.githubusercontent.com/LawAgents/ue-pt/main/, seguido do caminho do ficheiro). Pede-lhe que comece por `nomes-comuns.md`, e que só abra os índices e os atos de que precisar.

Em ambas as formas, cola nas instruções do agente o texto abaixo.

```text
Tens acesso à legislação da União Europeia no repositório LawAgents/ue-pt (ficheiros markdown, um por ato).
Para encontrar um ato lê primeiro nomes-comuns.md; se não o encontrares, lê o índice de regulamentos ou de diretivas; se mesmo assim não existir, lê revogados.md.
Responde só com o que lês nos ficheiros. Cita sempre o artigo, o ficheiro (caminho no repo) e a ligação do EUR-Lex (campo source do cabeçalho).
Nunca inventes artigos, números de atos, datas ou ligações, e nunca respondas de memória.
Se não encontrares, responde "Não encontrado no repo." e não cites nada.
Se o campo text_version for "original sem consolidação", avisa: "Texto original, sem consolidação: pode ter sido alterado depois."
Termina sempre com: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
```

O [kit de agente legal pessoal](docs/kit.md) tem um modelo de prompt de sistema mais completo, instruções para ler um processo, uma lista de verificação e dez perguntas de teste.

## Avisos legais e política de reutilização

Os textos deste repositório vêm do Serviço de Publicações da União Europeia, que publica o Jornal Oficial. Transcrevem-se, em inglês e tal como estão, os dois avisos que foi possível ler (consultados em 2026-10-21).

Aviso de direitos de autor do Serviço de Publicações (https://op.europa.eu/en/web/about-us/legal-notices/publications-office-of-the-european-union-copyright):

> The editorial content of this website, which is owned by the EU, is licensed under the Creative Commons Attribution 4.0 International licence. This means that you can reuse it provided you acknowledge the source and indicate any changes you have made.

Aviso legal do CheckLex, a aplicação do Serviço de Publicações que verifica a edição eletrónica do Jornal Oficial (https://checklex.publications.europa.eu/faces/LegalNotice.xhtml?lang=en):

> Effective 1 July 2013, the only EU legislation deemed authentic is that published in the electronic editions of the OJ.

O primeiro aviso fala do conteúdo editorial desse sítio e remete a reutilização do EUR-Lex para o aviso próprio do EUR-Lex. Esse aviso não foi lido: o EUR-Lex bloqueia pedidos automáticos. Por isso o texto exato da licença que se aplica aos textos legislativos no EUR-Lex não está confirmado. Até haver confirmação, este repositório indica a fonte em cada ficheiro e avisa que só o Jornal Oficial faz fé.

O descarregador deste repositório faz no máximo um pedido por segundo, usa só o endereço publications.europa.eu e identifica-se em cada pedido.

## Licenças

- Os scripts e o plugin têm a licença MIT.
- Os textos são da União Europeia. Reutilizam-se com indicação da fonte (Serviço de Publicações da União Europeia, EUR-Lex), ao abrigo da política de reutilização do Serviço de Publicações citada acima. Este repositório não reivindica direitos sobre o seu conteúdo.

## Como contribuir

- Pull requests só são aceites para a lista de nomes comuns (`config/nomes-comuns.txt`), a documentação e o kit de agente.
- Os ficheiros de legislação não aceitam edições à mão, porque são gerados a partir do Serviço de Publicações.
- Encontraste um erro num ato? Abre uma issue com o id do ato e a ligação do EUR-Lex onde se vê o texto correto.

## Kit de agente legal pessoal

Em [docs/kit.md](docs/kit.md): modelo de prompt de sistema, instruções para um agente que lê um processo, lista de verificação contra o EUR-Lex e dez perguntas de teste com a resposta esperada.
