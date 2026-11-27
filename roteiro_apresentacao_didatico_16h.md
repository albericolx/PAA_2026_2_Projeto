# 🎯 ROTEIRO DIDÁTICO DE APRESENTAÇÃO — TEMA 6: MOTOBOY (BEECROWD 1286)
**Disciplina:** Projeto e Análise de Algoritmos (PAA) — UFRPE 2026.2  
**Docente:** Profª. Drª. Jeane Melo  
**Apresentador:** José Albérico Rocha da Silva (`albericolx@gmail.com`)  
**Horário:** 16:00 | **Duração estimada:** 14 a 18 minutos (+ 3 min de perguntas)  
**Links da Apresentação:**
- 🌐 **Simulador Web:** [albericolx.github.io/PAA_2026_2_Projeto](https://albericolx.github.io/PAA_2026_2_Projeto/)
- 💻 **Código Oficial:** [github.com/albericolx/PAA_2026_2_Projeto/blob/main/code/solucao_beecrowd_1286.py](https://github.com/albericolx/PAA_2026_2_Projeto/blob/main/code/solucao_beecrowd_1286.py)

---

## 🧭 POSTURA GERAL PARA A APRESENTAÇÃO
1. **Respire e comece tranquilo:** Seus colegas não são juízes; eles querem entender como resolver um problema prático sem se afogar em fórmulas matemáticas.
2. **A regra de ouro:** Nunca mostre uma fórmula ou código sem antes contar a **história** ou o **motivo** que fez aquele código existir.
3. **Contato visual:** Olhe nos olhos de três pontos da sala (esquerda, centro e direita). Use pausas dramáticas de 2 segundos após perguntas retóricas.

---

## 🍕 SLIDE 1: Capa e Boas-Vindas (1 minuto)
* **Visual:** Título do Tema 6, UFRPE, Profª Jeane Melo, seu nome.
* **Objetivo:** Estabelecer empatia, quebrar o gelo e contextualizar o tema de forma leve.

### 🎙️ O Que Falar (Script Passo a Passo):
> *"Boa tarde, pessoal! Boa tarde, professora Jeane.*
> 
> *Hoje nós vamos resolver juntos um desafio clássico da computação, mas vestido com um problema super comum do nosso dia a dia aqui em Recife: **como um motoboy de pizzaria pode organizar as entregas no seu baú para trabalhar o tempo máximo e faturar mais, sem violar o limite físico da sua moto?***
> 
> *Esse é o problema **1286 do BeeCrowd**, e a técnica que vamos explorar para resolvê-lo da forma mais inteligente possível é a famosa **Programação Dinâmica**, modelando-o como uma **Mochila Binária 0-1**.*
> 
> *Vocês vão ver que, por trás de nomes complicados, a ideia central é incrivelmente simples: nunca recalcular o que você já descobriu. Vamos lá?"*

* **Transição para o Slide 2:** *"Para começar, vamos olhar de perto o dilema desse motoboy..."*

---

## 📦 SLIDE 2: O Problema: O Baú da Moto (1,5 a 2 minutos)
* **Visual:** Dados do problema: $N$ pedidos, tempo $t_i$, pizzas $p_i$, capacidade $P=10$, tabela com os 4 pedidos somando 17 pizzas.
* **Objetivo:** Fazer a turma sentir a dor do problema. Mostrar por que métodos ingênuos (força bruta ou ganância) falham.

### 🎙️ O Que Falar:
> *"Imaginem a cena: sexta-feira à noite, a pizzaria está lotada. Chegaram **4 pedidos** para entrega, mas o motoboy só tem uma moto com um baú que aguenta no máximo **10 pizzas**.*
> 
> *Olhem a nossa tabela:*
> - *O Pedido 1 tem 5 pizzas e leva 20 minutos.*
> - *O Pedido 2 tem 7 pizzas e leva 70 minutos.*
> - *O Pedido 3 tem 2 pizzas e leva 15 minutos.*
> - *O Pedido 4 tem 3 pizzas e leva 25 minutos.*
> 
> *Se o motoboy tentasse levar tudo, ele precisaria carregar $5 + 7 + 2 + 3 = \mathbf{17	ext{ pizzas}}$. Mas o baú só cabe 10! Não cabe tudo. E tem uma regra sagrada: **não existe meia entrega**. Ou você entrega o pedido completo para o cliente, ou você não leva.*
> 
> *Agora eu pergunto a vocês: qual seria a primeira reação de alguém? 'Ah, vou ser guloso! Pego o pedido que dá mais tempo de cara: o Pedido 2 (70 min e 7 pizzas)'. Sobram 3 espaços. Nesses 3 espaços, cabe o Pedido 4 (3 pizzas, 25 min). Total: $70 + 25 = 95$ minutos.*
> 
> *Mas e se tivéssemos 20 pedidos com combinações diferentes? Testar todas as combinações na mão daria $2^{20}$, que é mais de um milhão de testes! Não dá para fazer no 'olhômetro'. Precisamos de um modelo formal."*

* **Transição para o Slide 3:** *"E como a ciência da computação enxerga esse baú de pizza? Como uma Mochila!"*

---

## 🎒 SLIDE 3: Modelagem: É uma Mochila 0-1 (1,5 minuto)
* **Visual:** Comparação lado a lado (Motoboy vs Mochila Clássica), formulação matemática e citação a Richard Karp (1972).
* **Objetivo:** Mostrar que problemas do mundo real se traduzem em problemas clássicos da literatura. Explicar o que significa "0-1" e por que é difícil (NP-completo).

### 🎙️ O Que Falar:
> *"Olhem que interessante este paralelo:*
> - *A capacidade do baú de $P$ pizzas é a **capacidade $W$ da mochila**.*
> - *A quantidade de pizzas de cada pedido é o **peso do item** ($w_i$).*
> - *O tempo de entrega é o **valor do item** ($v_i$) que queremos maximizar.*
> - *E a decisão $x_i \in \{0, 1\}$ é a nossa chave: ou levamos o pedido ($1$), ou recusamos ($0$). Por isso se chama **Mochila 0-1**.*
> 
> *Em 1972, um cientista chamado Richard Karp provou que a Mochila 0-1 pertence aos problemas **NP-completos**. Isso significa que ninguém conhece um algoritmo milagroso que resolva esse problema em tempo polinomial perfeito para qualquer tamanho.*
> 
> *Porém, para os limites do mundo real — como o do nosso motoboy com até 30 pizzas — existe uma técnica espetacular que resolve em frações de milissegundo: a **Programação Dinâmica**."*

* **Transição para o Slide 4:** *"Mas de onde veio essa técnica? A história por trás dela é curiosa e divertida..."*

---

## 📜 SLIDE 4: De Onde Vem a Programação Dinâmica? (1,5 minuto)
* **Visual:** Anos 1950, Guerra Fria, Richard Bellman, RAND Corporation, Princípio da Otimalidade.
* **Objetivo:** Humanizar o conteúdo com uma história marcante e fixar o Princípio da Otimalidade com uma intuição simples.

### 🎙️ O Que Falar:
> *"Nos anos 1950, em plena Guerra Fria, um matemático brilhante chamado **Richard Bellman** trabalhava na **RAND Corporation**, desenvolvendo pesquisas para a Força Aérea americana.*
> 
> *Sabe por que a técnica se chama 'Programação Dinâmica'? Porque o Secretário de Defesa da época tinha aversão à palavra 'pesquisa' e não queria liberar dinheiro para matemáticos teorizarem. Bellman então pensou: 'Que palavras soam imponentes e não despertam desconfiança de nenhum político? Programação — que na época significava planejar — e Dinâmica — porque muda ao longo do tempo'. Foi quase uma estratégia de sobrevivência política para conseguir verba!*
> 
> *Mas a sacada matemática dele foi genial: o **Princípio da Otimalidade de Bellman**.*
> 
> *O que ele diz? Imagine que você vai viajar do Recife para Caruaru pela melhor rota possível, passando por Gravatá. Se a rota inteira é ótima, o trecho entre Gravatá e Caruaru também TEM que ser a melhor rota possível a partir de Gravatá!*
> 
> *Em termos computacionais: **um problema grande é formado por subproblemas menores. Se você resolve cada subproblema uma única vez e anota o resultado, você nunca mais precisa recalcular!**"*

* **Transição para o Slide 5:** *"E como Bellman traduziu isso em matemática para a nossa mochila de pizzas? Vejam a equação dele..."*

---

## 🧠 SLIDE 5: A Equação de Bellman (2 minutos)
* **Visual:** Matriz $DP[i][w]$, caso não cabe, caso cabe ($\max(	ext{não levar}, 	ext{levar})$), casos base com zero, resposta em $DP[N][P]$.
* **Objetivo:** Desmistificar a equação. Fazer cada estudante entender que são apenas 2 escolhas lógicas na vida do motoboy.

### 🎙️ O Que Falar:
> *"Não se assustem com a fórmula na tela. Ela nada mais é do que o diálogo que você teria com o motoboy:*
> 
> *Definimos $DP[i][w]$ como: **'Qual é o maior tempo que consigo entregar olhando os primeiros $i$ pedidos, se o meu baú tivesse espaço para apenas $w$ pizzas?'***
> 
> *Para cada pedido que você olha, só existem duas situações possíveis:*
> 
> 1. **Cenário 1 — Não cabe no baú ($p_i > w$):**  
>    *Se o pedido tem 7 pizzas e o baú só tem espaço para 5, você não pode fazer nada a não ser dizer 'não'. Você simplesmente herda a melhor resposta da linha de cima: $DP[i][w] = DP[i-1][w]$.*
> 
> 2. **Cenário 2 — O pedido cabe ($p_i \le w$):**  
>    *Agora você tem um poder de escolha! E você avalia duas opções:*  
>    - **Opção A (Não levar):** Fica com o resultado anterior: $DP[i-1][w]$.  
>    - **Opção B (Levar):** Você ganha o tempo desse pedido ($t_i$) **MAIS** a melhor solução que você já tinha calculado para o espaço que sobra no baú: $w - p_i$ pizzas!  
>    *E o que o algoritmo faz? Pega o $\max()$ entre as duas opções: a melhor vence!*
> 
> *E os casos base? Se eu tenho 0 pedidos ou se o baú tem 0 de espaço, o ganho é zero. Começamos com zeros e vamos construindo a resposta até a última célula: $DP[N][P]$, que terá a perfeição matemática."*

* **Transição para o Slide 6:** *"Agora, como nós implementamos isso para rodar em milissegundos no juiz eletrônico do BeeCrowd?"*

---

## 💻 SLIDE 6: Código e Complexidade: Otimização Espacial O(P) (2 minutos)
* **Visual:** Código Python compacto com vetor unidimensional `dp = [0] * (max_pizzas + 1)`, iteração decrescente `range(max_pizzas, pizzas - 1, -1)`, complexidades $\Theta(N \cdot P)$ e $O(P)$.
* **Objetivo:** Explicar a 'sacada' da otimização de memória. Por que varrer ao contrário evita duplicar pedidos.

### 🎙️ O Que Falar:
> *"Muitas pessoas aprendem programação dinâmica construindo uma matriz 2D com linhas e colunas. Isso é ótimo para visualizar, mas consome memória $O(N \cdot P)$.*
> 
> *Reparem neste código Python de apenas 7 linhas:*
> - *Nós alocamos **apenas um vetor de 1 dimensão**: `dp = [0] * (max_pizzas + 1)`. Para 30 pizzas, são apenas 31 números na memória! Isso é espaço $O(P)$, minúsculo!*
> 
> *Agora prestem muita atenção nesta linha:*  
> `for w in range(max_pizzas, pizzas - 1, -1):`
> 
> *Por que nós estamos percorrendo as pizzas de trás para frente, de 10 descendo até o tamanho do pedido?*
> 
> *Essa é a **pergunta clássica de prova de PAA**:*  
> *Se nós percorrêssemos para frente (de 0 até 10), ao atualizar uma capacidade maior, estaríamos consultando um valor que acabou de ser alterado na mesma rodada! Isso significaria permitir que o mesmo pedido fosse colocado duas ou três vezes no baú — o que resolveria a 'Mochila Ilimitada', mas violaria a regra da Mochila 0-1!*
> 
> *Ao varrer de trás para frente, garantimos que qualquer valor consultado veio obrigatoriamente da rodada anterior. Cada pedido entra no máximo uma única vez!*
> 
> *Complexidade? São no máximo $20 	imes 30 = 600$ operações básicas. Para um computador que faz 100 milhões de operações por segundo, isso roda em piscar de olhos."*

* **Transição para o Slide 7:** *"Vamos ver o fluxo visual dessa lógica em diagrama de blocos..."*

---

## 🔄 SLIDE 7: Fluxograma do Algoritmo (1 a 1,5 minuto)
* **Visual:** 4 blocos de fluxo (Alocação -> Laço Externo -> Varredura Reversa -> Decisão de Bellman) e retornos.
* **Objetivo:** Reforçar a lógica visual para quem aprende melhor com diagramas do que com código.

### 🎙️ O Que Falar:
> *"Este fluxograma sintetiza toda a execução do nosso programa:*
> 
> 1. **Bloco 1:** *Inicializamos nosso vetor unidimensional com zeros na memória.*
> 2. **Bloco 2 (Laço Externo):** *Enquanto houver pedidos na lista da pizzaria, pegamos o próximo pedido com seu tempo e suas pizzas.*
> 3. **Bloco 3 (Laço Interno Reverso):** *Iniciamos $w$ na capacidade máxima do baú e vamos descendo até o limite em que o pedido ainda cabe.*
> 4. **Bloco 4 (Decisão de Bellman In-Place):** *Avaliamos: `dp[w - pizzas] + tempo > dp[w]`?*  
>    - *Se **SIM**: atualizamos a célula na hora: venceu levar o pedido!*  
>    - *Se **NÃO**: mantemos o que estava antes, porque a combinação prévia já era mais vantajosa.*
> 
> *Quando todos os pedidos são processados, a posição final do vetor já guarda o tempo máximo ótimo absoluto."*

* **Transição para o Slide 8:** *"E para que ninguém tenha que apenas imaginar essa matriz funcionando, nós desenvolvemos um simulador web interativo ao vivo!"*

---

## 🌐 SLIDE 8: Demonstração ao Vivo no Simulador Web (2,5 a 3 minutos) — [CLÍMAX DA APRESENTAÇÃO]
* **Visual:** Screenshot do simulador, links públicos no GitHub Pages e GitHub Code, roteiro dos 4 passos.
* **Ação:** Projetar a aba do simulador no navegador (`albericolx.github.io/PAA_2026_2_Projeto`).
* **Objetivo:** Mostrar o funcionamento prático, a construção da matriz e a auditoria do backtracking.

### 🎙️ O Que Falar:
> *(Abre o navegador no link ou mostra o slide enquanto projeta)*
> 
> *"Para comprovar visualmente como a matemática acontece, este é o nosso **Simulador Visual Interativo**, hospedado publicamente no GitHub Pages.*
> 
> *(Navegando no simulador ou apontando os passos):*
> 
> 1. **Passo 1 (Cenário Real):** *Aqui estão os nossos dados: Capacidade $P=10$ e os 4 pedidos de exemplo.*
> 2. **Passo 2 (Construção da Matriz):** *Ao clicarmos em 'Executar Tudo', o algoritmo preenche a matriz de Programação Dinâmica diante dos nossos olhos. Vejam que o resultado final na última célula é exatamente **95 minutos**!*
> 3. **Passo 3 (O Segredo do Backtracking):** *Agora vem a pergunta de 1 milhão de dólares: **'Como o algoritmo sabe QUAIS pedidos levar para dar esses 95 minutos?'***  
>    *Ao clicar em 'Avançar Backtracking', o algoritmo faz o caminho inverso, da última célula para o início:*  
>    - *Na linha 4 (Pedido 4): o valor é 95, mas na linha de cima era 85. Mudou! Logo, **o Pedido 4 (25 min, 3 pizzas) FOI ESCOLHIDO!** Sobram $10 - 3 = 7$ pizzas de espaço.*  
>    - *Vamos para a linha 3 com 7 pizzas: o valor é 70, e na linha de cima também era 70. Não mudou! Logo, **o Pedido 3 foi DESCARTADO!** O espaço continua 7.*  
>    - *Na linha 2 com 7 pizzas: o valor é 70, mas na linha de cima era 20. Mudou! Logo, **o Pedido 2 (70 min, 7 pizzas) FOI ESCOLHIDO!** Espaço restante: $7 - 7 = 0$.*  
>    - *Resultado: Pedidos 2 e 4 selecionados: $70 + 25 = 95	ext{ minutos}$ e $7 + 3 = 10	ext{ pizzas}$ cravadas no baú!*
> 
> *Também deixamos disponível no slide o link direto para o código-fonte em Python oficial no repositório, com comentários didáticos linha a linha."*

* **Transição para o Slide 9:** *"Mas a Programação Dinâmica não serve só para entregar pizza. Onde mais nós a usamos sem perceber?"*

---

## 🌍 SLIDE 9: Onde a Programação Dinâmica Aparece no Dia a Dia? (1,5 a 2 minutos)
* **Visual:** 6 aplicações modernas: GPS/Trânsito, Delivery/Logística, Corretor e Git diff, Bioinformática, Nuvem e Reconhecimento de Voz.
* **Objetivo:** Conectar a teoria da disciplina com a indústria e com as ferramentas que os colegas usam diariamente.

### 🎙️ O Que Falar:
> *"Vejam como a Programação Dinâmica está rodando nos nossos bolsos e servidores neste exato momento:*
> 
> 1. **GPS e Aplicativos de Trânsito (Waze, Google Maps):** *Algoritmos como Dijkstra e Bellman-Ford encontram o caminho mais rápido recalculando sub-rotas sem precisar testar os bilhões de caminhos possíveis.*
> 2. **Delivery e Empacotamento (iFood, Rappi, Amazon):** *O problema do nosso motoboy é a base do Problema de Roteamento de Veículos (VRP), que define quais encomendas colocar na van de entrega sob restrição de peso e volume.*
> 3. **Git Diff e Corretores Ortográficos:** *Quando vocês dão `git diff` e veem as linhas verdes e vermelhas, o Git está rodando o algoritmo LCS (Maior Subsequência Comum) via Programação Dinâmica para encontrar a menor quantidade de mudanças!*
> 4. **Bioinformática e Medicina:** *Os algoritmos de Smith-Waterman alinham sequências de DNA e RNA para encontrar mutações genéticas e parentesco evolutivo.*
> 5. **Computação em Nuvem (AWS, Google Cloud):** *Empacotar centenas de máquinas virtuais e contêineres Docker dentro do menor número de servidores físicos para economizar energia é a variação Bin Packing da mochila.*
> 6. **Reconhecimento de Voz (Siri, Alexa):** *O Dynamic Time Warping (DTW) alinha o sinal de áudio se você falar rápido ou devagar, casando os fonemas por programação dinâmica.*
> 
> *Tudo isso bebe da mesmíssima fonte de Richard Bellman."*

* **Transição para o Slide 10:** *"Chegamos então aos nossos resultados finais e conclusões..."*

---

## 🏆 SLIDE 10: Resultados e Conclusões (1,5 minuto)
* **Visual:** Veredito Accepted no BeeCrowd (0,095s), três pilares (Modelar, Resolver, Comprovar), contato e agradecimento.
* **Objetivo:** Fechar com chave de ouro, demonstrar rigor acadêmico e sucesso na submissão.

### 🎙️ O Que Falar:
> *"Para consolidar nosso trabalho:*
> 
> - **Modelamos:** *Transformamos um problema real de entregas na formulação formal da Mochila 0-1.*
> - **Resolvemos:** *Implementamos a recorrência ótima com compactação espacial em $O(P)$ e complexidade pseudo-polinomial $\Theta(N \cdot P)$.*
> - **Comprovamos:** *Submetemos ao juiz online oficial do BeeCrowd e obtivemos **ACCEPTED** com tempo de execução de apenas **0,095 segundos**, menos de um décimo do limite de 1 segundo estipulado pela plataforma.*
> - *E além disso, entregamos o simulador web e o relatório técnico completo para auditar a tomada de decisão via backtracking.*
> 
> *Agradeço a atenção de todos vocês e a orientação da professora Jeane. Estou aberto a dúvidas e perguntas!"*

* **Transição para o Slide 11:** *(Apenas passe para as referências e deixe visível enquanto responde perguntas).*

---

## 📚 SLIDE 11: Referências (Enquanto responde perguntas)
* Deixe este slide de fundo enquanto a professora e os colegas fazem perguntas.
* Se alguém perguntar sobre a complexidade: mencione Cormen e Kleinberg-Tardos.
* Se alguém perguntar sobre a história: mencione a autobiografia de Bellman (1984), *Eye of the Hurricane*.

---

## 💡 PERGUNTAS QUE A PROFESSORA OU COLEGAS PODEM FAZER (E SUAS RESPOSTAS PREPARADAS):

1. **Pergunta:** *"Por que a complexidade é chamada de 'pseudo-polinomial' e não polinomial pura?"*
   - **Sua Resposta:** *"Excelente pergunta! Ela é $\Theta(N \cdot P)$, onde $N$ é o número de itens e $P$ é a capacidade. Mas o tamanho da entrada na memória para representar o número $P$ não é $P$, e sim $\log_2(P)$ bits. Quando um algoritmo depende do valor numérico da entrada e não apenas da quantidade de bits, dizemos que ele é pseudo-polinomial. Para valores razoáveis de $P$ (como $P \le 30$), ele é extremamente veloz."*

2. **Pergunta:** *"O que aconteceria se a gente varresse o vetor $w$ em ordem crescente em vez de decrescente?"*
   - **Sua Resposta:** *"Se varrêssemos em ordem crescente, um item poderia ser somado a ele mesmo em capacidades maiores na mesma iteração, permitindo que o motoboy levasse duas ou mais pizzas do mesmo pedido. Isso resolveria a Mochila Não-Limitada (Unbounded Knapsack), mas violaria a regra de ouro da Mochila 0-1, onde cada pedido só pode ser levado no máximo uma vez."*

3. **Pergunta:** *"Por que o algoritmo guloso (ordenar por tempo/pizzas) não funciona para a Mochila 0-1?"*
   - **Sua Resposta:** *"O algoritmo guloso funciona perfeitamente para a Mochila Fracionária, onde podemos cortar itens. Mas na Mochila 0-1, pegar um item com alta densidade pode deixar um espaço 'morto' no baú que não cabe mais nada, enquanto duas peças menores poderiam preencher o baú perfeitamente e somar um tempo maior. Só a Programação Dinâmica garante a solução ótima global."*
