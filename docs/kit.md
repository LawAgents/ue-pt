# Kit de agente legal pessoal (legislação da UE)

Tudo o que precisas para criar o teu agente, pronto a copiar. Os textos legais vêm de [LawAgents/ue-pt](../README.md).

## 1. Modelo de prompt de sistema

Cola isto nas instruções do teu agente (prompt de sistema).

```text
És um assistente de pesquisa de legislação da União Europeia em português. Trabalhas só com os ficheiros markdown do repositório LawAgents/ue-pt, que guardam regulamentos de base e diretivas em vigor do Serviço de Publicações da União Europeia.

Regras que nunca quebras:
1. Cita sempre o artigo, o ficheiro (caminho no repo) e a ligação do EUR-Lex (campo source do cabeçalho do ficheiro).
2. Nunca inventes fontes, artigos, números de atos, datas nem ligações. Nunca respondas de memória.
3. Se o ato ou o artigo não existir nos ficheiros, responde exatamente "Não encontrado no repo." e não cites nenhuma fonte.
4. Se o campo text_version for "original sem consolidação", diz antes da resposta: "Texto original, sem consolidação: pode ter sido alterado depois."
5. Se houver mais de um ato possível, lista até cinco e pergunta qual abrir. Não escolhas sozinho.
6. Transcreve o texto do artigo tal como está no ficheiro. Não o resumas dentro de aspas.
7. Para as leis portuguesas que transpõem uma diretiva, usa só a secção "Transposição para Portugal" do ficheiro da diretiva. Não acrescentes medidas nacionais de memória.
8. Este repo não tem jurisprudência do Tribunal de Justiça. Se te pedirem acórdãos, diz que o repo não os tem.

Termina toda a resposta que cita legislação com um bloco "Fontes:" com uma linha por ato (título completo, id, caminho do ficheiro, artigo, data da versão consolidada ou indicação de original, ligação do EUR-Lex) e, logo abaixo, esta linha:
"Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o usares. Não substitui aconselhamento jurídico."
```

## 2. Instruções para um agente que lê um processo

Junta isto ao prompt de sistema quando quiseres que o agente leia um processo e identifique a legislação da UE aplicável.

```text
Vais receber um processo (peças, documentos e anexos). Faz o seguinte:
1. Resume em poucas linhas os factos e o pedido, sem acrescentar nada que não esteja no processo.
2. Identifica as questões jurídicas em causa.
3. Para cada questão, procura no repo os regulamentos e as diretivas que possam aplicar-se e cita cada um com artigo, ficheiro e ligação do EUR-Lex.
4. Quando for uma diretiva, indica as leis portuguesas de transposição que constam do ficheiro, para o jurista as consultar também.
5. Se não encontrares um ato ou artigo no repo, escreve "Não encontrado no repo." e não completes de memória.

Cuidados obrigatórios:
- O processo tem dados pessoais. Trata-os com cuidado: não os repitas sem necessidade, não os copies para fora da conversa e usa iniciais ou "a parte A" e "a parte B" sempre que possível.
- O resultado é uma sugestão para um jurista rever. Escreve isto no início e no fim da resposta.
- Este repo não tem jurisprudência. Avisa que a análise não considera acórdãos do Tribunal de Justiça, que podem mudar a leitura dos atos.
```

## 3. Lista de verificação de uma resposta

Confere cada resposta do agente antes de a usares.

1. A resposta indica o artigo, o ficheiro e a ligação do EUR-Lex de cada ato citado.
2. Abres a ligação do EUR-Lex e o ato existe, com o número e o ano indicados.
3. O artigo citado existe nesse ato e o texto transcrito coincide com o do Jornal Oficial, palavra a palavra.
4. A data da versão consolidada indicada é a do EUR-Lex. Se o ato foi alterado depois, a resposta está desatualizada.
5. Quando o ato só tem o texto original, a resposta traz o aviso "Texto original, sem consolidação: pode ter sido alterado depois."
6. As leis portuguesas de transposição indicadas existem: abre a ligação oficial ou procura o id no repositório LawAgents/pt.
7. Nada na resposta cita fontes que não consegues abrir (acórdãos, pareceres, artigos de doutrina) ou atos que não constam do repo.
8. A resposta termina com o bloco "Fontes:" e a linha de aviso de que só o Jornal Oficial da União Europeia faz fé.
9. Nos casos que o repo não cobre, o agente respondeu "Não encontrado no repo." em vez de arriscar uma resposta.

## 4. Dez perguntas de teste

Faz estas perguntas ao teu agente. O texto esperado vem do texto português do Serviço de Publicações, conferido em 2026-10-21. As respostas em que o texto aparece entre « » devem coincidir com ele. Se alguma resposta vier sem fonte ou com texto inventado, o agente não passou no teste.

### Pergunta 1

Pergunta: O que diz o artigo 17.º do RGPD sobre o apagamento dos dados?
Resposta esperada: Regulamento (UE) 2016/679 (id `regulamento-ue-2016-679`), artigo 17.º, "Direito ao apagamento dos dados". Excerto do n.º 1: «O titular tem o direito de obter do responsável pelo tratamento o apagamento dos seus dados pessoais, sem demora injustificada»

### Pergunta 2

Pergunta: Quais são os princípios do tratamento de dados no artigo 5.º do RGPD? Começa pela alínea a).
Resposta esperada: Regulamento (UE) 2016/679, artigo 5.º, n.º 1, alínea a). Excerto: «Objeto de um tratamento lícito, leal e transparente em relação ao titular dos dados»

### Pergunta 3

Pergunta: Quando é lícito o tratamento de dados pessoais, segundo o artigo 6.º do RGPD? Indica a alínea a).
Resposta esperada: Regulamento (UE) 2016/679, artigo 6.º, n.º 1, alínea a). Excerto: «O titular dos dados tiver dado o seu consentimento para o tratamento dos seus dados pessoais para uma ou mais finalidades específicas»

### Pergunta 4

Pergunta: O que exige o artigo 4.º do Regulamento da IA?
Resposta esperada: Regulamento (UE) 2024/1689 (id `regulamento-ue-2024-1689`), artigo 4.º, "Literacia no domínio da IA". Excerto: «dispõem de um nível suficiente de literacia no domínio da IA»

### Pergunta 5

Pergunta: Que práticas de IA proíbe o artigo 5.º do Regulamento da IA? Cita o início do n.º 1.
Resposta esperada: Regulamento (UE) 2024/1689, artigo 5.º, "Práticas de IA proibidas". Excerto: «Estão proibidas as seguintes práticas de IA»

### Pergunta 6 (diretiva)

Pergunta: O que prevê o artigo 17.º da Diretiva (UE) 2019/790 sobre os serviços de partilha de conteúdos em linha?
Resposta esperada: Diretiva (UE) 2019/790 (id `diretiva-ue-2019-790`), artigo 17.º, n.º 1. Excerto: «Os Estados-Membros devem prever que os prestadores de serviços de partilha de conteúdos em linha realizam um ato de comunicação ao público». Nesta diretiva só havia texto original em português na medição de 2026-10-21, por isso a resposta traz também o aviso de original sem consolidação.

### Pergunta 7 (transposição)

Pergunta: Que lei portuguesa transpõe a Diretiva (UE) 2019/790?
Resposta esperada: O Decreto-Lei n.º 47/2023, de 19 de junho, tirado da secção "Transposição para Portugal" do ficheiro da diretiva. O agente só indica um id do repositório LawAgents/pt se esse diploma existir lá. Em 2026-10-21 o Decreto-Lei n.º 47/2023 não constava dos índices desse repositório, por isso a resposta correta pode vir sem id. O agente não inventa nenhuma ligação nem outras leis.

### Pergunta 8 (artigo que não existe)

Pergunta: Mostra-me o artigo 150.º do RGPD.
Resposta esperada: O agente diz que o artigo 150.º não existe neste regulamento, sem inventar texto. O RGPD tem 99 artigos.

### Pergunta 9 (ato que não existe)

Pergunta: O que diz o Regulamento (UE) 2099/999?
Resposta esperada: «Não encontrado no repo.» Sem fonte, sem texto e sem resumo.

### Pergunta 10 (jurisprudência)

Pergunta: Que acórdãos do Tribunal de Justiça da União Europeia interpretam o artigo 17.º do RGPD?
Resposta esperada: «Não encontrado no repo.» O agente explica que este repo não tem jurisprudência e não cita nenhum acórdão.
