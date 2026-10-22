- European Union law in Portuguese as markdown: base regulations and directives in force, one file per act, from the Publications Office of the EU.
- Each directive links to the Portuguese laws that transpose it. No delegated or implementing acts, decisions, treaties or Court of Justice case law.
- The same Claude Code plugin as the Portuguese repo (legislacao-pt) reads it with three extra commands: /lei-ue, /artigo-ue and /pesquisar-ue.
- Step-by-step guides in European Portuguese for non-programmers, plus a ready-made kit to build your own personal legal agent.
- Only the Official Journal of the EU is authentic: always confirm in EUR-Lex. Scripts and plugin are MIT; the texts are EU texts, reusable with attribution.

# Direito da União Europeia em português

Os regulamentos de base e as diretivas da União Europeia em vigor, em português, convertidos do Serviço de Publicações da UE
para markdown, com cabeçalho estruturado e ligação ao EUR-Lex em cada ficheiro. Cada artigo tem o seu título. Cada diretiva traz
a lista das leis portuguesas que a transpõem, quando essa lei está no repositório irmão
[LawAgents/pt](https://github.com/LawAgents/pt).

Para consultar com o Claude Code só precisas de instalar o plugin [legislacao-pt](https://github.com/LawAgents/legislacao-pt-plugin),
o mesmo da legislação portuguesa. Os dados não se instalam: o plugin lê os ficheiros deste repositório diretamente e cita a fonte
em cada resposta, com os comandos `/lei-ue`, `/artigo-ue` e `/pesquisar-ue`.

> [!IMPORTANT]
> Só o Jornal Oficial da União Europeia faz fé. Os textos daqui não substituem a publicação oficial: confirma sempre no EUR-Lex
> pela ligação do cabeçalho antes de citar. Onde só existe o texto original, a ficha e as respostas avisam que pode ter sido
> alterado depois.

---

## O que contém

5.439 atos em vigor, em 9.122 ficheiros (os atos grandes estão divididos em partes).

| Tipo de ato | Atos |
| --- | ---: |
| Regulamento | 4.595 |
| Diretiva | 844 |
| **Total** | **5.439** |

Por versão do texto:

| Texto | Atos |
| --- | ---: |
| Original, sem consolidação | 4.009 |
| Consolidado | 1.430 |

Para cada ato escolhe-se o texto consolidado mais recente em português. Quando não há consolidado, entra o original. As contagens
são de 2026-10-22.

### O que fica de fora

- Atos delegados e atos de execução.
- Decisões, tratados e jurisprudência do Tribunal de Justiça da União Europeia.
- Cerca de 2.320 atos sem texto em português utilizável, sobretudo anteriores a 2000.
- Atos que deixaram de estar em vigor: saem da pasta principal e a lista `revogados.md` guarda o id, o título, a data do fim de vigência e a ligação oficial.
- Versões anteriores de um ato: o histórico fica no git, com um commit por atualização.
- Legislação portuguesa: está em [LawAgents/pt](https://github.com/LawAgents/pt).

`COBERTURA.md` e `estatisticas.html` são gerados por `python -I scripts/estatisticas.py` e não se atualizam sozinhos: refazem-se à mão depois de uma atualização.

---

## Estrutura

```
regulamentos/AAAA/regulamento-ue-AAAA-N.md     um ficheiro por regulamento, por ano do ato
diretivas/AAAA/diretiva-ue-AAAA-N.md           um ficheiro por diretiva, por ano do ato
<ato>/<id>/<id>-<parte>.md                     atos grandes: visão geral e partes de até 70 KB
nomes-comuns.md                                nomes e siglas (RGPD, AI Act) para o id certo
indice.md  indice-regulamentos-*.md            índices por tipo e ano (ficheiros de até 40 KB)
indice-diretivas-*.md
revogados.md                                   atos que deixaram de estar em vigor
COBERTURA.md                                   números por tipo, década e versão, e o que ficou de fora
estatisticas.html                              página com gráficos, um único ficheiro para abrir no navegador
config/                                        lista de nomes comuns e ids portugueses
scripts/                                       o código que descarrega, converte, valida e gera os índices e as estatísticas
docs/kit.md                                    kit de agente legal pessoal
```

Os ids são estáveis: `regulamento-ue-2016-679` é o Regulamento (UE) 2016/679, com o ano em quatro dígitos e o número sem zeros à
esquerda. Um ato dividido em partes tem um ficheiro de visão geral com a tabela `## Estrutura` (primeiro e último artigo de cada
parte), e o agente abre só a parte de que precisa.

No fim de cada diretiva há a secção `## Transposição para Portugal`. O id português só aparece quando esse diploma existe em
LawAgents/pt, e a ligação oficial só aparece quando o Serviço de Publicações a fornece.

---

## Formato dos ficheiros

Todo o ficheiro tem cabeçalho YAML e, no corpo, o título em `#` seguido do texto, com um título por artigo:

```markdown
---
id: "regulamento-ue-2016-679"
celex: "32016R0679"
title: "Regulamento (UE) 2016/679 do Parlamento Europeu e do Conselho, de 27 de abril de 2016, ..."
type: "Regulamento"
number: "2016/679"
year: 2016
date: 2016-04-27
status: "em vigor"
text_version: "consolidado"
last_amended: 2016-05-04
consolidated_celex: "02016R0679-20160504"
source: "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:02016R0679-20160504"
eli: "http://data.europa.eu/eli/reg/2016/679/oj"
retrieved: 2026-10-21
legal_notice: "Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. ..."
---
```

Nos textos originais, `text_version` é `original sem consolidação` e não há `last_amended` nem `consolidated_celex`. Os artigos
sem texto na fonte (por exemplo "Não utilizado") levam a marca `*(Sem texto)*`.

---

## Atualização

Uma tarefa do GitHub corre todos os domingos às 04:00 UTC, descarrega o que mudou no Serviço de Publicações, valida e faz um commit por
atualização. Se algo falhar, não publica dados parciais e abre uma issue com o erro. O ensaio no GitHub (sem commit) correu sem erros e
não encontrou alterações. Ainda não vi uma atualização real com alterações do Serviço de Publicações.

---

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
