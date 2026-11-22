# Roteiro Completo de Apresentação de Slides (20 min ± 5 min)
## Projeto VA2 – Tema 6: BeeCrowd 1286 – Motoboy (Mochila 0-1 e Programação Dinâmica)
**Disciplina:** Projeto e Análise de Algoritmos (PAA) – UFRPE 2026.2  
**Professora:** Dra. Jeane Melo  
**Apresentador:** José Albérico Rocha da Silva  

---

## ⏱️ Planejamento e Gestão de Tempo (Total: 20 Minutos)

| Bloco | Slides | Conteúdo Principal | Tempo Alocado |
| :--- | :--- | :--- | :--- |
| **1. Introdução** | Slides 1 a 3 | Abertura, Enunciado do Problema e Analogia com o Mundo Real | 3 min |
| **2. Modelagem** | Slides 4 a 5 | Formulação Matemática da Mochila 0-1 e Falha de Outras Técnicas | 3 min |
| **3. A Técnica Teórica** | Slides 6 a 8 | Programação Dinâmica, Subestrutura Ótima e Dedução de Bellman | 4 min |
| **4. Implementação & Decisões** | Slides 9 a 10 | Decisões de Projeto em Python 3 (Matriz 2D vs Vetor 1D e Backtracking) | 3 min |
| **5. Demonstração Prática** | Slide 11 | **Solução Rodando Ao Vivo** (Execução do Script com Rastreamento) | 4 min |
| **6. Complexidade e Validação** | Slides 12 a 13 | Análise de Complexidade Assintótica e Print de Aceite do BeeCrowd | 2 min |
| **7. Encerramento & Ética** | Slides 14 a 15 | Considerações Finais, Portaria CNPq 2.664 e Referências | 1 min |

---

# Estrutura dos Slides e Roteiro de Fala Oral

---

### SLIDE 1: Capa da Apresentação
* **Título:** Resolução Otimizada do Problema do Motoboy (BeeCrowd 1286) via Programação Dinâmica
* **Subtítulo:** Estudo de Caso do Problema da Mochila Binária (0-1 Knapsack)
* **Aluno:** José Albérico Rocha da Silva
* **Instituição:** Universidade Federal Rural de Pernambuco (UFRPE) – Departamento de Computação
* **Disciplina:** Projeto e Análise de Algoritmos (PAA) | Profª. Jeane Melo | 2026.2
* **Tempo sugerido:** 1 minuto

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Bom dia a todos, bom dia professora Jeane. Meu nome é José Albérico Rocha da Silva e hoje apresento o projeto da nossa Segunda Verificação de Aprendizagem de Projeto e Análise de Algoritmos. O tema que escolhi trabalhar foi o Tema 6, referente ao problema 1286 do BeeCrowd: 'Motoboy'. Veremos hoje como um problema prático de logística de entregas mapeia-se com perfeição ao clássico Problema da Mochila Binária, por que técnicas gulosas e força bruta são inadequadas, e como a Programação Dinâmica nos fornece uma solução ótima com garantia matemática e eficiência computacional."*

---

### SLIDE 2: O Problema do Motoboy (BeeCrowd 1286)
* **Personagem:** José, entregador de uma conceituada pizzaria.
* **O Cenário Diário:**
  * José recebe uma lista de $N$ pedidos no início do turno ($1 \le N \le 20$).
  * Cada pedido $i$ exige um **tempo de entrega** $t_i$ (minutos) e ocupa **$p_i$ pizzas** no baú da moto.
  * A motocicleta tem uma capacidade física estrita de $P$ pizzas ($1 \le P \le 30$).
* **O Dilema de Otimização:**
  * Maximizar o tempo total de trabalho em rota (maior remuneração/benefício para José).
  * Respeitar a capacidade $P$ (não exceder as pizzas suportadas pela moto).
  * Cada pedido é indivisível: ou é entregue integralmente ou não é atendido (0 ou 1).
* **Tempo sugerido:** 1,5 minuto

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Vamos entender o contexto. José é um motoboy que quer maximizar o tempo total de suas entregas, pois seu rendimento é proporcional aos minutos em rota. Porém, a moto possui um limite físico $P$, que é o número de pizzas que cabem no baú. Cada cliente pede uma quantidade específica de pizzas $p_i$ e demanda um tempo $t_i$ de deslocamento. O detalhe fundamental é que uma entrega não pode ser fracionada: José não pode entregar metade das pizzas de uma família e deixar o restante para trás. Essa característica de decisão atômica — levar ou não levar — é exatamente o que define uma mochila 0-1."*

---

### SLIDE 3: Aplicações no Mundo Real e Relevância Prática
* **Logística e Transporte:** Carregamento ótimo de contêineres, caminhões e aeronaves (limitações de peso e cubagem).
* **Cloud Computing & Sistemas Operacionais:** Alocação de processos e máquinas virtuais sob restrição de memória RAM e vCPUs.
* **Finanças:** Seleção de portfólio de projetos sob restrições orçamentárias (Capital Budgeting).
* **Curiosidade Histórica:** Richard Bellman introduziu o termo 'Programação Dinâmica' nos anos 1950 na RAND Corporation para disfarçar pesquisas matemáticas pioneiras de tomada de decisão sob restrições!
* **Tempo sugerido:** 1 minuto

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Embora o problema use uma metáfora lúdica com pizzas e motoboy, a estrutura matemática subjacente é onipresente na computação. Ela resolve o empacotamento de contêineres em navios de carga, o escalonamento de contêineres Docker e Kubernetes em servidores em nuvem, e até a alocação de investimentos financeiros. Curiosamente, o nome 'Programação Dinâmica' foi cunhado por Richard Bellman na década de 1950 para descrever essa técnica de otimização em etapas sucessivas."*

---

### SLIDE 4: Formulação Matemática Formal (Mochila 0-1)
* **Entradas:**
  * Conjunto de pedidos: $\{1, 2, \dots, N\}$
  * Vetor de ganhos (tempos): $[t_1, t_2, \dots, t_N]$, onde $t_i > 0$
  * Vetor de pesos (pizzas): $[p_1, p_2, \dots, p_N]$, onde $p_i > 0$
  * Capacidade da moto: $P$
* **Variáveis de Decisão:**
  * $x_i \in \{0, 1\}$ (1 se o pedido $i$ for aceito; 0 se recusado)
* **Função Objetivo (Maximizar Tempo):**
  $$\text{Maximizar } Z = \sum_{i=1}^{N} t_i \cdot x_i$$
* **Restrição de Capacidade:**
  $$\sum_{i=1}^{N} p_i \cdot x_i \le P$$
* **Tempo sugerido:** 1,5 minuto

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Matematicamente, temos um problema de Programação Linear Inteira Binária. Temos uma função objetivo $Z$ que soma o tempo $t_i$ de cada pedido multiplicado pela variável binária $x_i$. E temos uma inequação de restrição: o somatório das pizzas $p_i$ vezes $x_i$ não pode exceder $P$. Sendo $x_i$ estritamente binário (zero ou um), trata-se formalmente do Problema da Mochila 0-1, um dos 21 problemas NP-completos clássicos catalogados por Richard Karp em 1972."*

---

### SLIDE 5: Por que Força Bruta e Algoritmos Gulosos Falham?
* **Tentativa 1: Busca Exaustiva (Força Bruta)**
  * Cada pedido tem 2 estados possíveis $\rightarrow 2^N$ combinações.
  * Para $N=20$: $2^{20} = 1.048.576$ testes (viável mas ineficiente).
  * Se $N=100$: $2^{100} \approx 1,26 \times 10^{30}$ (levaria mais que a idade do universo). Custo $O(2^N)$ inaceitável.
* **Tentativa 2: Algoritmos Gulosos (Greedy)**
  * Escolher sempre o maior tempo? Falha (pode entupir a moto e impedir combinações melhores).
  * Escolher quem tem menos pizzas? Falha (pode pegar pedidos rápidos demais).
  * Escolher por densidade de tempo/pizza ($t_i / p_i$)? **Também falha!**
  * *Contraexemplo Didático:* Capacidade $P = 10$.
    * Pedido 1: 60 min, 6 pizzas (razão = 10 min/pizza)
    * Pedido 2: 50 min, 5 pizzas (razão = 10 min/pizza)
    * Pedido 3: 50 min, 5 pizzas (razão = 10 min/pizza)
    * O guloso escolhe o Pedido 1 e para (restam 4 pizzas, não cabe mais nada) $\rightarrow \mathbf{60\text{ min}}$.
    * A escolha ótima é levar Pedidos 2 e 3 $\rightarrow 50 + 50 = \mathbf{100\text{ min}}$.
* **Tempo sugerido:** 2 minutos

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Aqui entra a análise crítica de algoritmos. Por que não usar força bruta? Porque sua complexidade é exponencial $O(2^N)$. E por que não usar um algoritmo guloso? Na mochila fracionária, ordenar pela razão benefício/custo funciona perfeitamente. Mas na mochila 0-1, como ilustrado no slide, a indivisibilidade gera o fenômeno da capacidade ociosa: um item 'guloso' pode desperdiçar espaço que caberia dois itens ligeiramente menores, cuja soma superaria a escolha gulosa. Portanto, heurísticas gulosas não garantem a solução ótima."*

---

### SLIDE 6: A Técnica da Programação Dinâmica
* **Conceito Central:** Resolver problemas complexos decompondo-os em subproblemas mais simples, armazenando os resultados intermediários para nunca recalcular o mesmo estado.
* **Os Dois Pilares Fundamentais:**
  1. **Subestrutura Ótima:** A solução ótima para capacidade $w$ contendo $i$ itens incorpora a solução ótima para capacidades menores com $i-1$ itens.
  2. **Subproblemas Sobrepostos:** Diferentes caminhos de decisão necessitam do valor de $DP(i-1, w')$ repetidas vezes.
* **Abordagem Adotada:** *Bottom-Up* (Tabular, iterativa, sem risco de estouro de pilha de recursão).
* **Tempo sugerido:** 2 minutos

> 🎙️ **Fala sugerida ao apresentador:**  
> *"A Programação Dinâmica é a ferramenta ideal para este problema. Ela se sustenta em dois pilares: Subestrutura Ótima e Subproblemas Sobrepostos. Em vez de recursão ingênua com árvores redundantes, nós construímos uma tabela de forma Bottom-Up, preenchendo os casos menores primeiro e construindo a solução global passo a passo."*

---

### SLIDE 7: A Lógica de Preenchimento da Matriz e a Equação de Bellman
* **O que cada célula $DP[i][w]$ representa?**
  * *"Qual é o tempo máximo de entrega que José consegue fazer usando apenas os primeiros $i$ pedidos, se a moto tivesse capacidade para exatamente $w$ pizzas?"*
* **Por que os primeiros elementos são zero? (Casos Base)**
  * **Linha 0 ($i=0$):** Se José tem 0 pedidos à disposição, mesmo que a moto caiba 10 pizzas, o tempo acumulado é **0** ($DP[0][w] = 0$).
  * **Coluna 0 ($w=0$):** Se a moto não suporta nenhuma pizza ($w=0$), nenhum pedido pode ser transportado, tempo acumulado é **0** ($DP[i][0] = 0$).
* **A Comparação Binária da Equação de Bellman:**
  * Se o pedido não cabe ($p_i > w$):
    $$DP[i][w] = DP[i-1][w] \quad \text{(Herda o valor direto da célula acima)}$$
  * Se o pedido cabe ($p_i \le w$): Comparamos duas alternativas e escolhemos a maior:
    $$\text{Opção A (Sem o pedido): } DP[i-1][w]$$
    $$\text{Opção B (Com o pedido): } DP[i-1][w - p_i] + t_i$$
    $$DP[i][w] = \max\Big(DP[i-1][w], \; DP[i-1][w - p_i] + t_i\Big)$$
* **Tempo sugerido:** 2 minutos

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Prestem bastante atenção na lógica de construção desta matriz. Primeiramente, por que toda a linha 0 e coluna 0 começam com zero? Porque com zero pedidos não há entregas a fazer, e com zero capacidade a moto não carrega nada. Para cada uma das demais células, nós não olhamos valores aleatórios: nós tomamos uma decisão racional. Ou nós não levamos o pedido atual — e nesse caso o valor vem direto da célula de cima, com a mesma capacidade — ou nós levamos o pedido. Ao levá-lo, nós ganhamos o tempo dele ($t_i$) e olhamos na linha anterior quanto conseguiríamos fazer com o espaço que sobrou no baú ($w - p_i$). O algoritmo simplesmente calcula essas duas hipóteses e fica com o maior valor."*

---

### SLIDE 8: Cálculo Passo a Passo dos Elementos e Decisão Final
* **Instância Real do Exemplo:** Capacidade $P = 10$ pizzas.
  * Pedido 1: 20 min, 5 pizzas | Pedido 2: 70 min, 7 pizzas
  * Pedido 3: 15 min, 2 pizzas | Pedido 4: 25 min, 3 pizzas
* **Demonstração dos Primeiros Cálculos Numéricos:**
  1. $DP[1][1]$ a $DP[1][4] = \mathbf{0}$ (Pedido 1 tem 5 pizzas; não cabe em capacidades de 1 a 4).
  2. $DP[1][5] = \max(DP[0][5], DP[0][0] + 20) = \max(0, 20) = \mathbf{20}$ (O pedido cabe!).
  3. $DP[2][5] = \mathbf{20}$ (O Pedido 2 tem 7 pizzas e não cabe em $w=5$; logo, herda o valor de cima).
  4. $DP[2][7] = \max(DP[1][7], DP[1][0] + 70) = \max(20, 70) = \mathbf{70}$ (Substituir o pedido 1 pelo 2 dá mais tempo!).
  5. $DP[3][9] = \max(DP[2][9], DP[2][7] + 15) = \max(70, 70 + 15) = \mathbf{85}$ (Leva pedidos 2 e 3 juntos: $7+2=9$ pizzas).
  6. $DP[4][10] = \max(DP[3][10], DP[3][7] + 25) = \max(85, 70 + 25) = \mathbf{95\text{ min}}$ (**Célula Final Ótima**).
* **A Tomada de Decisão Final (Backtracking):**
  * Em $DP[4][10] = 95 \neq DP[3][10] = 85 \implies$ **Pedido 4 Selecionado!** (Espaço restante: $10 - 3 = 7$).
  * Em $DP[3][7] = 70 == DP[2][7] = 70 \implies$ **Pedido 3 Descartado!** (Espaço continua: $7$).
  * Em $DP[2][7] = 70 \neq DP[1][7] = 20 \implies$ **Pedido 2 Selecionado!** (Espaço restante: $7 - 7 = 0$).
  * **Conclusão:** Pedidos {2 e 4}. Tempo máximo = **95 min**. Ocupação = $7+3 = 10$ pizzas (100% de aproveitamento).
* **Tempo sugerido:** 2,5 minutos

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Vejam como cada número surge de forma transparente. Quando estamos na Linha 1 avaliando o Pedido 1 de 5 pizzas, ele não cabe até a capacidade 4, por isso é tudo zero. No momento em que chegamos na capacidade 5, a conta é: sem ele dá 0, com ele dá 0 + 20 = 20. Quando avaliamos o Pedido 2 com 7 pizzas, na capacidade 7 o algoritmo compara: manter o pedido anterior dava 20 min, mas trocar pelo pedido 2 nos dá 70 min. Ele escolhe 70! E vejam a tomada de decisão final: na capacidade 10, com os pedidos 2 e 3 nós tínhamos 85 minutos. Ao avaliar o Pedido 4, o algoritmo descobre que 70 + 25 dá 95 minutos! Ao fazer o caminho reverso, descobrimos com clareza matemática que a melhor estratégia para José é entregar os pedidos 2 e 4, totalizando 95 minutos e aproveitando 100% do espaço do baú."*

---

### SLIDE 9: Decisões de Projeto e Otimização em Python 3
* **Decisão 1: Otimização de Espaço de $O(N \cdot P)$ para $O(P)$**
  * Para preencher a linha $i$, precisamos somente da linha $i-1$.
  * Podemos substituir a matriz inteira por um **único vetor de tamanho $P+1$**.
  * **Ponto Crítico:** A iteração das capacidades deve ser **de trás para frente** (`range(P, p_i - 1, -1)`). Isso garante que o valor `dp[w - p_i]` consultado pertença à iteração anterior, impedindo que o mesmo pedido seja adicionado mais de uma vez!
* **Decisão 2: Reconstrução da Solução Ótima (Backtracking)**
  * No script didático, preservamos a matriz para demonstrar o caminho inverso: descobrir exatamente quais IDs de pedidos foram embarcados.
* **Decisão 3: Entrada e Saída Rápida**
  * Uso de `sys.stdin.read().split()` para leitura em lote em milissegundos.
* **Tempo sugerido:** 2 minutos

> 🎙️ **Fala sugerida ao apresentador:**  
> *"No projeto do software em Python, tomamos uma decisão de engenharia de software muito elegante: otimizamos o espaço de memória. Em vez de alocar uma matriz bidimensional, alocamos um único vetor de tamanho $P+1$. Mas atenção ao detalhe algorítmico: para isso funcionar na mochila 0-1, o loop de capacidade deve rodar em ordem decrescente, de $P$ descendo até $p_i$. Se rodássemos de forma crescente, usaríamos um mesmo pedido múltiplas vezes, o que transformaria o problema em uma mochila com reposição infinita. A varredura reversa preserva a restrição 0-1 com consumo mínimo de memória."*

---

### SLIDE 10: Análise de Complexidade Assintótica
* **Complexidade de Tempo:**
  $$T(N, P) = \Theta(N \cdot P)$$
  * São $N$ pedidos e para cada um varremos até $P$ posições com operações $O(1)$.
  * É uma complexidade **pseudo-polinomial** (polinomial no valor numérico de $P$).
  * Para os limites do BeeCrowd ($N \le 20, P \le 30$):
    $$\text{Operações Máximas} = 20 \times 30 = 600 \text{ iterações}$$
    Executado em menos de 1 milissegundo!
* **Complexidade de Espaço:**
  * Versão Tabular 2D: $O(N \cdot P)$
  * Versão Otimizada 1D: $O(P)$
  * Para $P = 30$, o vetor armazena apenas 31 números inteiros na memória RAM.
* **Tempo sugerido:** 1,5 minuto

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Quanto à complexidade: o tempo de execução é estritamente $\Theta(N \cdot P)$. Dizemos que é pseudo-polinomial porque depende do valor numérico de $P$. Como no BeeCrowd $N \le 20$ e $P \le 30$, o algoritmo realiza no máximo 600 operações elementares por caso de teste. É computacionalmente instantâneo. E a complexidade espacial na versão otimizada é $O(P)$, consumindo apenas 31 inteiros na memória."*

---

### SLIDE 11: DEMONSTRAÇÃO PRÁTICA – SOLUÇÃO RODANDO AO VIVO
* *(Neste momento, o apresentador alterna a tela para o terminal e executa o script `solucao_didatica_visual.py`)*
* **Comando executado:**
  `python solucao_didatica_visual.py`
* **O que destacar durante a execução ao vivo:**
  1. A leitura dos pedidos e capacidades;
  2. A impressão formatada da Matriz de Programação Dinâmica;
  3. O resultado final destacado: **95 min.** para o Caso 1 e **52 min.** para o Caso 2;
  4. O rastreamento de quais pedidos foram despachados (Pedidos #2 e #4) e quantas pizzas de espaço sobraram;
  5. O tempo de CPU medido em milissegundos.
* **Tempo sugerido:** 4 minutos

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Vou agora executar a solução rodando ao vivo para demonstrarmos o comportamento do algoritmo na prática... [Executa o comando no terminal]. Aqui podemos ver a matriz gerada pelo Python. Observem as linhas sendo computadas. No Caso 1, com capacidade 10, o tempo máximo foi exatamente 95 minutos. E o nosso algoritmo de retrocesso nos mostra que o motoboy deve levar o Pedido 2 e o Pedido 4, totalizando exatamente 10 pizzas, aproveitando 100% da capacidade do baú sem desperdício de espaço."*

---

### SLIDE 12: Resultados e Validação na Plataforma BeeCrowd
* **Submissão Oficial:** # 50429092
* **Problema:** 1286 - Motoboy
* **Veredito:** **ACCEPTED**
* **Linguagem:** Python 3.9 (Python 3.9.4)
* **Tempo de Execução:** $0.095\text{ s}$ (Média excelente, limite era $1.000\text{ s}$).
* **Data da Submissão:** 07/11/2026 às 10:23:03
* **Tamanho do Código:** 2,49 KB

![Print de Aceite no BeeCrowd](C:/Users/Windows%2010/.gemini/antigravity/brain/956bfd38-5e5e-44e4-b291-94e33df23d78/.user_uploaded/media_1794057869926_31a27693.png)

* **Tempo sugerido:** 1 minuto

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Aqui apresento o print de validação na plataforma BeeCrowd. Nossa submissão de número 50429092 foi aceita com o status 'Accepted' e tempo de execução de apenas 0.095 segundos, quase dez vezes mais rápido que o limite máximo de 1 segundo permitido pela plataforma. Isso comprova experimentalmente tanto a corretude do algoritmo de Programação Dinâmica quanto a eficácia da leitura em lote via sys.stdin."*

---

### SLIDE 13: Conclusão e Lições Aprendidas
* A Programação Dinâmica provou ser a técnica exata e ideal para o problema da Mochila 0-1, eliminando a ineficiência da força bruta e a falibilidade das heurísticas gulosas.
* A transição da matriz 2D para o array 1D representou um ganho significativo de maturidade em projeto de algoritmos.
* O domínio da equação de recorrência e da reconstrução de soluções conecta a teoria matemática de PAA às soluções de sistemas reais de logística.
* **Tempo sugerido:** 1 minuto

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Como considerações finais, este projeto consolidou de forma prática os princípios de subestrutura ótima e subproblemas sobrepostos ensinados pela professora Jeane. Vimos que a escolha da técnica adequada é o fator determinante entre um algoritmo impraticável e uma solução que responde em milissegundos."*

---

### SLIDE 14: Declaração de Conformidade Ética com IAG
* Cumprimento ao Art. 9º da **Portaria nº 2.664 de 06/03/2026 do CNPq**:
  * **Ferramenta:** Google Antigravity / Gemini 3.8 Flash
  * **Finalidades:** Apoio na estruturação formal do artigo no modelo SBC, refinamento da formatação visual dos testes e conferência das deduções de complexidade assintótica.
  * **Responsabilidade:** Todo o conteúdo foi implementado, testado, validado e é de integral responsabilidade autoral do estudante.
* **Tempo sugerido:** 0,5 minuto

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Em conformidade com a Portaria nº 2.664 do CNPq e as diretrizes do edital da professora Jeane, consta neste slide e no artigo a declaração formal do uso ético de Inteligência Artificial Generativa como ferramenta de apoio à redação e validação, sendo todo o código e análise de minha autoria e responsabilidade."*

---

### SLIDE 15: Referências Bibliográficas
* Cormen, T. H. et al. *Algoritmos: Teoria e Prática*, 3ª Edição, Elsevier, 2012.
* Kleinberg, J.; Tardos, É. *Algorithm Design*, Addison-Wesley, 2006.
* BeeCrowd Academic Online Judge. *Problema 1286: Motoboy*.
* Sociedade Brasileira de Computação (SBC). *Template para Artigos*.
* CNPq. *Portaria nº 2.664, de 6 de março de 2026*.
* **Tempo sugerido:** 0,5 minuto

> 🎙️ **Fala sugerida ao apresentador:**  
> *"Aqui estão as referências bibliográficas que fundamentaram nosso trabalho. Agradeço a atenção de todos e da professora Jeane Melo e me coloco à disposição para quaisquer perguntas e discussões técnicas."*

---

## 💡 Guia de Perguntas e Respostas para a Banca / Professora Jeane Melo

1. **Pergunta:** *"Por que a abordagem gulosa não funciona para a Mochila 0-1 se ela funciona para a Mochila Fracionária?"*  
   * **Resposta:** *"Na Mochila Fracionária, podemos levar frações de itens, o que nos permite preencher 100% da capacidade do baú sempre pegando os itens de maior razão benefício/custo. Na Mochila 0-1, como os pedidos são indivisíveis, um item com alta razão pode deixar um espaço residual onde não cabe mais nenhum outro item, gerando capacidade ociosa que supera o ganho inicial."*

2. **Pergunta:** *"O que aconteceria se você não fizesse a varredura decrescente no vetor 1D da DP?"*  
   * **Resposta:** *"Se percorrêssemos de forma crescente ($w$ de $p_i$ até $P$), estaríamos usando o valor recém-atualizado $dp[w - p_i]$ que já inclui o próprio item $i$. Isso permitiria que o mesmo pedido fosse incluído duas, três ou mais vezes na moto, transformando o problema na Mochila Não-Limitada (Unbounded Knapsack), violando a restrição do problema."*

3. **Pergunta:** *"A Programação Dinâmica resolve problemas NP-completos em tempo polinomial? Isso significa que P = NP?"*  
   * **Resposta:** *"Não. A complexidade $O(N \cdot P)$ é pseudo-polinomial. O valor $P$ é um número, mas o tamanho de sua representação na entrada é medido em número de bits ($\log_2 P$). Se $P$ for um número com centenas de dígitos, $P$ é exponencial em relação ao tamanho da entrada em bits. Portanto, a Programação Dinâmica só é rápida quando $P$ é de magnitude moderada, o que não viola a hipótese $P \neq NP$."*
