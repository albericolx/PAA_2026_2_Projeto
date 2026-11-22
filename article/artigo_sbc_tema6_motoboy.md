# Resolução Otimizada do Problema do Motoboy (BeeCrowd 1286) via Programação Dinâmica: Estudo de Caso da Mochila Binária

**Autor:** José Albérico Rocha da Silva  
**Instituição:** Departamento de Computação – Universidade Federal Rural de Pernambuco (UFRPE)  
**Disciplina:** Projeto e Análise de Algoritmos (PAA) – 2026.2  
**Docente:** Profª. Drª. Jeane Melo  
**Tema:** Tema 6 – BeeCrowd Problema 1286: Motoboy  

---

## Resumo

Este artigo apresenta a formulação teórica, a fundamentação histórica e a implementação computacional orientada à resolução do problema 1286 (*Motoboy*) da plataforma BeeCrowd, estruturado em conformidade com o padrão científico da Sociedade Brasileira de Computação (SBC) e normas da ABNT. O problema aborda a tomada de decisão logística de um entregador de pizzas que busca maximizar seu tempo total de trabalho diário, sob estrita restrição de capacidade volumétrica no baú da motocicleta. Demonstra-se a redução formal e o isomorfismo com o Problema da Mochila Binária (*0-1 Knapsack Problem*), pertencente à classe NP-completo. Apresenta-se uma sólida revisão teórica do algoritmo da mochila, detalhando seu funcionamento e justificando sua indispensabilidade perante o fracasso de heurísticas gulosas e da busca exaustiva por força bruta. Contextualiza-se a evolução histórica da Programação Dinâmica, concebida por Richard Bellman na década de 1950 durante a Guerra Fria na RAND Corporation, consolidada pelo Princípio da Otimidade. Adicionalmente, exploram-se aplicações práticas contemporâneas da Programação Dinâmica em sistemas cotidianos como roteirizadores GPS, bioinformática, computação em nuvem e corretores ortográficos. O algoritmo foi implementado em linguagem Python 3, incorporando a equação de recorrência de Bellman, rastreamento analítico elemento a elemento, reconstrução de solução por retrocesso (*backtracking*), comprovação de aceite experimental no juiz eletrônico e a declaração de integridade acadêmica referente à Portaria nº 2.664/2026 do CNPq.

**Palavras-chave:** Projeto e análise de algoritmos. Programação dinâmica. Problema da mochila binária. BeeCrowd 1286. Richard Bellman. Aplicações cotidianas. Python 3.

---

## Abstract

This paper presents the theoretical formulation, historical context, and computational implementation aimed at solving problem 1286 (*Motoboy*) from the BeeCrowd platform, following the Brazilian Computer Society (SBC) academic template. The problem models the operational logistics of a pizza courier seeking to maximize total delivery working time subject to a strict motorcycle box capacity constraint. We formally reduce this scenario to the classical 0-1 Knapsack Problem (NP-complete). A comprehensive theoretical review of the knapsack algorithm is provided, detailing its internal mechanics and justifying why exhaustive brute-force search and greedy heuristics inevitably fail. The historical background of Dynamic Programming is examined, highlighting Richard Bellman's work at the RAND Corporation during the Cold War and the formulation of the Principle of Optimality. Real-world applications of Dynamic Programming in daily technologies—such as GPS routing, bioinformatics, cloud resource provisioning, and spell checking—are thoroughly discussed. The algorithm was coded in Python 3, incorporating Bellman's recurrence equation, analytical matrix trace, backtracking subset reconstruction, verified acceptance in the online judge, and full compliance with CNPq Ordinance No. 2,664/2026.

**Keywords:** Design and analysis of algorithms. Dynamic programming. 0-1 knapsack problem. BeeCrowd 1286. Richard Bellman. Real-world applications. Python 3.

---

## 1. Introdução e Contextualização do Problema

### 1.1 Contexto e Enunciado do Problema BeeCrowd 1286
No problema **BeeCrowd 1286: Motoboy**, somos apresentados a José, um experiente motoboy de uma pizzaria que recebe diariamente uma listagem contendo $N$ pedidos de clientes. Cada pedido $i \in \{1, \dots, N\}$ possui duas grandezas determinísticas associadas:
1. O tempo de entrega $t_i \in \mathbb{Z}^+$ (expresso em minutos), que representa o ganho ou benefício acumulado por José ao realizar aquela rota de entrega;
2. A quantidade de pizzas demandadas $p_i \in \mathbb{Z}^+$, que representa o volume e o peso ocupados no baú de sua motocicleta.

A motocicleta dispõe de uma capacidade máxima de transporte de $P$ pizzas simultâneas. Devido a exigências operacionais e de integridade dos produtos, cada pedido deve ser entregue integralmente ou não entregue (é estritamente proibido fracionar um pedido entre viagens ou motoboys distintos). O objetivo consiste em determinar o subconjunto de pedidos que maximize o somatório dos tempos de entrega, garantindo que o total de pizzas transportadas não ultrapasse a capacidade $P$ da bag.

As restrições fornecidas pela plataforma BeeCrowd são:
* Quantidade de pedidos: $1 \le N \le 20$;
* Capacidade máxima de transporte: $1 \le P \le 30$;
* Tempo de cada pedido: $1 \le t_i \le 100$;
* Pizzas de cada pedido: $1 \le p_i \le 20$;
* A entrada encerra quando $N = 0$.

---

## 2. Revisão Teórica: O Problema da Mochila (Knapsack Problem)

### 2.1 Origem Teórica e Classificação de Complexidade
O **Problema da Mochila (*Knapsack Problem*)** é um dos modelos mais célebres da otimização combinatória e da ciência da computação teórica. Formulado em suas bases modernas por George Dantzig (1957) e formalmente classificado por Richard Karp (1972) como um dos 21 problemas fundamentais **NP-completos**, ele simboliza o dilema fundamental da alocação de recursos escassos sob restrições orçamentárias ou físicas.

Na formulação geral, um mochileiro dispõe de uma mochila com capacidade máxima de sustentação $W$. Diante de um conjunto de $N$ objetos discretos, onde cada objeto $i$ agrega um benefício/valor $v_i$ e exige um consumo de peso $w_i$, deve-se selecionar a combinação de itens que resulte no maior valor cumulativo possível sem romper a capacidade da mochila.

### 2.2 Como Funciona a Mochila Binária (0-1 Knapsack)
A variante binária (0-1) impõe que cada item $i$ deve ser escolhido em sua totalidade ($x_i = 1$) ou totalmente rejeitado ($x_i = 0$), sendo $x_i \in \{0, 1\}$. Matematicamente:

$$\text{Maximizar } Z = \sum_{i=1}^{N} v_i \cdot x_i$$
$$\text{Sujeito a: } \sum_{i=1}^{N} w_i \cdot x_i \le W, \quad x_i \in \{0, 1\}, \forall i \in \{1, \dots, N\}$$

Diferentemente da *Mochila Fracionária* (onde é permitido cortar os itens em partes proporcionais e uma simples ordenação gulosa por densidade de valor resolve o problema de forma ótima), na *Mochila 0-1* a indivisibilidade gera vazios ou capacidade ociosa residual que inviabiliza escolhas míopes locais.

### 2.3 Por que Devemos Usar o Algoritmo da Mochila Neste Projeto?
O cenário do problema do Motoboy apresenta uma correspondência biunívoca perfeita (isomorfismo formal) com o Problema da Mochila 0-1:

| Elemento do Problema Clássico da Mochila | Elemento Correspondente no BeeCrowd 1286 (Motoboy) | Significado Operacional no Projeto |
| :--- | :--- | :--- |
| **Mochila com Capacidade $W$** | **Baú da Motocicleta de José ($P$)** | Restrição rígida de capacidade física de transporte de pizzas. |
| **Peso do item $i$ ($w_i$)** | **Quantidade de pizzas do pedido ($p_i$)** | Custo de ocupação do espaço dentro da bag da moto. |
| **Valor/Benefício do item $i$ ($v_i$)** | **Tempo de entrega do pedido ($t_i$)** | Minutos de trabalho que José acumula ao realizar o pedido. |
| **Decisão Binária ($x_i \in \{0, 1\}$)** | **Aceite ou Rejeição do Pedido ($x_i \in \{0, 1\}$)** | Indivisibilidade da entrega: pedidos não podem ser divididos. |
| **Maximizar valor total $\sum v_i x_i$** | **Maximizar tempo de serviço $\sum t_i x_i$** | Meta de otimização estipulada pela pizzaria. |

Portanto, o uso do algoritmo da Mochila Binária via Programação Dinâmica não é apenas uma escolha técnica recomendada, mas uma **exigência conceitual indispensável**:
1. É a única modelagem matemática exata capaz de traduzir a restrição física de volume com indivisibilidade de pedidos.
2. Contorna comprovadamente as armadilhas dos algoritmos gulosos e evita a explosão combinatória da força bruta.

---

## 3. Breve Histórico da Programação Dinâmica

### 3.1 Richard Bellman e a RAND Corporation na Guerra Fria
A técnica de **Programação Dinâmica (PD)** foi desenvolvida no início da década de 1950 pelo notável matemático norte-americano **Richard Bellman** (1920–1984), enquanto atuava como pesquisador na **RAND Corporation** (*Research and Development*), em Santa Monica, Califórnia. A RAND era a principal entidade de pesquisa estratégica e consultoria científica para a Força Aérea dos Estados Unidos durante o auge das tensões geopolíticas da Guerra Fria.

Bellman dedicava-se ao estudo de processos de decisão em múltiplos estágios (*multi-stage decision processes*), buscando métodos matemáticos rigorosos para planejar trajetórias balísticas de mísseis, logística de reabastecimento militar e alocação sequencial de recursos bélicos.

### 3.2 A Origem Curiosa do Nome "Programação Dinâmica"
Em sua autobiografia, *Eye of the Hurricane: An Autobiography* (1984), Richard Bellman revelou a curiosa história política por trás da criação do termo. O então Secretário de Defesa dos Estados Unidos na administração Eisenhower, **Charles Wilson**, nutria profunda aversão por pesquisas científicas básicas e declarava abertamente desprezo pelo trabalho de matemáticos, cortando sumariamente qualquer verba rotulada como *"pesquisa"* (*research*).

Para proteger o financiamento de seu grupo na RAND contra auditorias do Pentágono, Bellman necessitava de um nome para a técnica que soasse expressivo, puramente aplicado e impossível de ser contestado ou cortado por burocratas governamentais:
* **"Programação"**: na época (início dos anos 1950), o vocábulo não se referia à codificação de software em computadores (que ainda estavam em seus primórdios), mas sim ao sentido militar e logístico de **planejamento, escalonamento e confecção de cronogramas tabulares** (como em "programação linear" de George Dantzig).
* **"Dinâmica"**: denotava que as tomadas de decisão variavam ao longo do tempo em estágios encadeados, possuindo uma conotação moderna, sofisticada e incontestável.

Nas palavras do próprio Bellman: *"Foi um termo que até mesmo um Secretário de Defesa não poderia vetar ou associar a pesquisas puramente teóricas"*.

### 3.3 O Princípio da Otimidade de Bellman (1957)
A pedra fundamental que sustenta toda a Programação Dinâmica é o **Princípio da Otimidade**, formalizado por Bellman em seu livro clássico *Dynamic Programming* (1957):

> *"Uma política ótima tem a propriedade de que, quaisquer que sejam o estado inicial e as decisões iniciais, as decisões restantes devem constituir uma política ótima com relação ao estado resultante da primeira decisão."*

Esse teorema estabelece que problemas complexos de otimização global podem ser resolvidos resolvendo subproblemas locais, armazenando seus resultados e compondo a solução final de forma ascendente (*bottom-up*), sem necessidade de retrocessos com recálculos caros.

---

## 4. Exemplos de Aplicação da Programação Dinâmica no Cotidiano

A Programação Dinâmica não se restringe a ambientes acadêmicos ou problemas de maratona de programação. Ela atua nos bastidores das tecnologias digitais mais utilizadas no cotidiano moderno:

### 4.1 Roteirizadores de GPS e Navegação Veicular (Waze, Google Maps)
Ao solicitar a rota mais rápida no aplicativo de navegação, algoritmos derivados da Programação Dinâmica (como o algoritmo de **Bellman-Ford** e a subestrutura de **Dijkstra**) decompõem a viagem em cruzamentos e segmentos viários intermediários. O sistema calcula e reutiliza o tempo mínimo acumulado até cada cruzamento para compor o trajeto global mais rápido, evitando a reavaliação de milhões de combinações redundantes de ruas a cada atualização do trânsito em tempo real.

### 4.2 Plataformas de Delivery e Logística Urbana (iFood, Rappi, Loggi, Amazon)
Sistemas inteligentes de distribuição precisam despachar centenas de milhares de entregas diárias alocando-as em motocicletas, vans e caminhões. A Programação Dinâmica é empregada na resolução do Problema de Roteirização de Veículos (*Vehicle Routing Problem - VRP*) e no empacotamento de cargas (*Knapsack*), definindo exatamente quais pacotes um motoboy ou motorista deve carregar para maximizar o cumprimento de prazos e o faturamento, sem exceder o volume do compartimento de carga.

### 4.3 Correção Ortográfica e Sugestão de Palavras (Smartphones e Ferramentas de Diff)
Os teclados de smartphones utilizam o algoritmo de **Distância de Edição de Levenshtein** (*Edit Distance*), fundamentado em Programação Dinâmica. O algoritmo preenche uma matriz bidimensional que computa o número mínimo de operações de inserção, remoção ou substituição de caracteres necessárias para transformar a palavra digitada com erros pelo usuário na palavra correta armazenada no dicionário. Similarmente, comandos como `git diff` usam o algoritmo de **Maior Subsequência Comum (LCS - Longest Common Subsequence)** para comparar alterações em linhas de código.

### 4.4 Bioinformática e Alinhamento de Sequências Genéticas (DNA e RNA)
O sequenciamento genético e a medicina personalizada utilizam os algoritmos de **Needleman-Wunsch** (alinhamento global) e **Smith-Waterman** (alinhamento local). Ambos constroem tabelas de Programação Dinâmica comparando milhões de pares de bases nitrogenadas (A, T, C, G) para detectar mutações genéticas, avaliar parentescos evolutivos entre espécies e identificar alvos terapêuticos para novos medicamentos.

### 4.5 Computação em Nuvem e Alocação de Servidores (AWS, Google Cloud, Azure)
Provedores de infraestrutura em nuvem precisam hospedar milhares de máquinas virtuais (VMs) e contêineres Docker em servidores físicos de datacenters. O particionamento ótimo de recursos de hardware (CPU, memória RAM e largura de banda de rede) sob restrições rígidas de capacidade é resolvido por variações multidimensionais do problema da mochila via Programação Dinâmica, minimizando o consumo energético e reduzindo a quantidade de servidores ociosos.

### 4.6 Reconhecimento de Voz e Assistentes Virtuais (Siri, Alexa, Google Assistente)
O algoritmo de **Dynamic Time Warping (DTW)** utiliza Programação Dinâmica para mensurar a similaridade entre duas sequências temporais de áudio que podem apresentar velocidades de fala diferentes. Isso permite que um assistente virtual compreenda com precisão um comando de voz, independentemente de a pessoa ter falado de forma rápida ou arrastada.

---

## 5. Análise da Técnica: Por que Força Bruta e Algoritmos Gulosos Falham?

### 5.1 Busca Exaustiva / Força Bruta
Como cada pedido $i$ oferece duas alternativas exclusivas ($x_i = 0$ ou $x_i = 1$), o espaço amostral completo consiste em $2^N$ subconjuntos.
* Para $N = 20$, temos $2^{20} = 1.048.576$ combinações possíveis (viável em frações de segundo);
* Para $N = 50$, teríamos $2^{50} \approx 1,12 \times 10^{15}$ operações;
* Para $N = 100$, temos $2^{100} \approx 1,26 \times 10^{30}$ operações, o que exigiria bilhões de anos de computação contínua.
A complexidade exponencial $O(2^N)$ torna a abordagem impraticável para instâncias reais.

### 5.2 Algoritmos Gulosos (Heurísticas Míopes)
Estratégias gulosas tomam decisões locais imediatas esperando alcançar o ótimo global, mas falham sistematicamente na Mochila 0-1:
1. **Critério 1 (Maior Tempo Primeiro):** Falha porque um pedido com tempo ligeiramente maior pode exigir quase todo o espaço da bag, impedindo que dois ou três pedidos menores somem um tempo muito superior.
2. **Critério 2 (Menor Quantidade de Pizzas Primeiro):** Falha porque pedidos pequenos podem carregar tempos irrisórios, desperdiçando a jornada do entregador.
3. **Critério 3 (Maior Densidade $t_i / p_i$ - Razão Benefício/Custo):**
   * *Contraexemplo Didático:* Seja a capacidade do baú $P = 10$ pizzas e 3 pedidos disponíveis:
     * Pedido A: Tempo 60 min, Pizzas 6 (Razão = $60 / 6 = 10\text{ min/pz}$)
     * Pedido B: Tempo 50 min, Pizzas 5 (Razão = $50 / 5 = 10\text{ min/pz}$)
     * Pedido C: Tempo 50 min, Pizzas 5 (Razão = $50 / 5 = 10\text{ min/pz}$)
   * A heurística gulosa escolhe o Pedido A (6 pizzas). Restam $10 - 6 = 4$ pizzas de espaço. Nenhum outro pedido cabe no espaço residual de 4 pizzas. O algoritmo encerra entregando apenas **60 minutos**.
   * A solução ótima global consiste em rejeitar o Pedido A e selecionar os **Pedidos B e C**, que juntos consomem exatamente $5 + 5 = 10$ pizzas e geram **100 minutos de trabalho** ($66,7\%$ superior à heurística gulosa).

---

## 6. Modelagem e Dedução da Equação de Recorrência de Bellman

### 6.1 Semântica da Matriz Bidimensional de Estados $DP[i][w]$
Define-se uma matriz de estados $DP[0..N][0..P]$, onde cada posição $DP[i][w]$ armazena a resposta exata para a pergunta:
> *"Qual é o tempo máximo de entrega que José consegue obter considerando exclusivamente um subconjunto dos primeiros $i$ pedidos cadastrados, caso a sua moto possuísse uma capacidade limite de transporte de exatamente $w$ pizzas?"*

### 6.2 Casos Base
* **Primeira Linha ($i = 0$):** $DP[0][w] = 0, \forall w \in [0, P]$. Sem pedidos disponíveis na pizzaria, nenhum minuto de trabalho pode ser acumulado.
* **Primeira Coluna ($w = 0$):** $DP[i][0] = 0, \forall i \in [0, N]$. Com capacidade zero na bag, nenhuma pizza pode ser transportada.

### 6.3 Transição de Estados (Regra de Bellman)
Para cada pedido $i$ com parâmetros $(t_i, p_i)$ e capacidade sob análise $w \in [1..P]$:
* **Caso 1: O pedido excede a capacidade analisada ($p_i > w$):**
  $$DP[i][w] = DP[i-1][w]$$
  *(O pedido não cabe fisicamente; mantém-se a melhor solução conhecida sem ele).*
* **Caso 2: O pedido cabe na capacidade analisada ($p_i \le w$):**
  $$DP[i][w] = \max\Big(DP[i-1][w], \; t_i + DP[i-1][w - p_i]\Big)$$
  *(Avalia-se racionalmente se vale mais a pena ignorar o pedido ou aceitá-lo, somando seu tempo $t_i$ com o melhor resultado obtido para o espaço restante $w - p_i$).*

---

## 7. Projeto e Implementação da Solução em Python 3

### 7.1 Algoritmo de Reconstrução da Solução Ótima (Backtracking)
Para descobrir quais pedidos foram escolhidos a partir do valor final ótimo $DP[N][P]$, executa-se o percurso reverso do Pedido #N até o #1:
1. Inicia-se em $i = N$ e $w = P$.
2. Para $i$ descendo de $N$ até 1:
   * Se $DP[i][w] \neq DP[i-1][w]$: significa que o valor saltou em relação à linha anterior porque o **Pedido $i$ foi obrigatoriamente aceito**! Adiciona-se o pedido à lista de selecionados e subtrai-se seu peso da capacidade: $w \leftarrow w - p_i$.
   * Se $DP[i][w] == DP[i-1][w]$: o valor já existia sem este item, portanto o **Pedido $i$ foi descartado**. Mantém-se a capacidade $w$.

### 7.2 Implementação Otimizada em Espaço $O(P)$
Para a submissão no juiz eletrônico, compactou-se a matriz em um vetor unidimensional de dimensão $P + 1$, com iteração decrescente de $w$:

```python
def resolver_caso(n, max_pizzas, pedidos):
    # Vetor unidimensional compacto para economia de memória
    dp = [0] * (max_pizzas + 1)
    
    # Processa cada pedido sequencialmente
    for tempo, pizzas in pedidos:
        # Varredura decrescente para garantir a propriedade 0-1 (sem repetições)
        for w in range(max_pizzas, pizzas - 1, -1):
            if dp[w - pizzas] + tempo > dp[w]:
                dp[w] = dp[w - pizzas] + tempo
                
    return dp[max_pizzas]
```

### 7.3 Simulador Visual Web e Ferramenta Didática Interativa
Com o objetivo de enriquecer a mediação pedagógica e proporcionar uma experiência tangível e interativa sobre a dinâmica do algoritmo, desenvolveu-se uma aplicação em ambiente Web (HTML5/CSS3/JavaScript puro, contida no arquivo `simulador_visual_motoboy.html`). A aplicação enquadra em tela única:
1. **Configuração Dinâmica de Parâmetros:** Permite ao usuário alterar livremente a capacidade da mochila ($P$), a quantidade de pedidos ($N$) e os atributos individuais de tempo e pizzas de cada encomenda.
2. **Construção Visual da Matriz com Destaque de Recorrência:** Exibe o preenchimento célula a célula, iluminando em tempo real qual ramo da equação de Bellman (Caso 1 - Não Cabe vs. Caso 2 - Cabe na Mochila) foi acionado, acompanhado da substituição aritmética dos valores calculados.
3. **Auditoria Passo a Passo do Retrocesso (Backtracking):** Demonstra o caminho inverso percorrido pelo algoritmo do Pedido #N até o #1, comparando $DP[i][w] \neq DP[i-1][w]$, atualizando a capacidade residual da bag e justificando textualmente a decisão de negócio (por que cada pedido foi levado ou descartado).

O código-fonte completo da solução e o simulador interativo encontram-se disponíveis publicamente para replicação acadêmica em:  
🔗 **Acesso ao Simulador e Repositório:** <https://github.com/albericolx/PAA_2026_2_Projeto>  
🌐 **Simulador Web Online (GitHub Pages):** <https://albericolx.github.io/PAA_2026_2_Projeto/>

---

## 8. Análise de Complexidade Assintótica

* **Complexidade Temporal:** $T(N, P) = \Theta(N \cdot P)$. Como são percorridos $N$ laços externos e $P$ laços internos com operações aritméticas em tempo constante $O(1)$, a complexidade é **pseudo-polinomial**. Para os limites do problema ($N \le 20, P \le 30$), realizam-se no máximo $20 \times 30 = 600$ operações fundamentais, executadas em menos de 0,001 segundo pela CPU.
* **Complexidade Espacial:** $S_{2D}(N, P) = O(N \cdot P)$ na versão didática com matriz completa (apenas $21 \times 31 = 651$ inteiros), e estritamente **$S_{1D}(P) = O(P)$** na versão otimizada com vetor unidimensional (apenas 31 posições de memória para $P=30$).

---

## 9. Resultados Experimentais e Validação no BeeCrowd

### 9.1 Rastreamento Completo da Matriz no Caso de Teste Oficial 1 ($N=4, P=10$)

Dados de entrada: Pedido 1 (20 min, 5 pz); Pedido 2 (70 min, 7 pz); Pedido 3 (15 min, 2 pz); Pedido 4 (25 min, 3 pz).

| $i \backslash w$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0 (base)** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1 (20m, 5p)** | 0 | 0 | 0 | 0 | 0 | 20 | 20 | 20 | 20 | 20 | 20 |
| **2 (70m, 7p)** | 0 | 0 | 0 | 0 | 0 | 20 | 20 | 70 | 70 | 70 | 70 |
| **3 (15m, 2p)** | 0 | 0 | 15 | 15 | 15 | 20 | 20 | 70 | 70 | 85 | 85 |
| **4 (25m, 3p)** | 0 | 0 | 15 | 25 | 25 | 40 | 40 | 70 | 70 | 85 | **95** |

* **Auditoria de Backtracking:**
  1. $DP[4][10] = 95 \neq DP[3][10] = 85 \implies$ **Pedido #4 Levado!** ($w = 10 - 3 = 7$)
  2. $DP[3][7] = 70 == DP[2][7] = 70 \implies$ **Pedido #3 Descartado!** ($w = 7$)
  3. $DP[2][7] = 70 \neq DP[1][7] = 20 \implies$ **Pedido #2 Levado!** ($w = 7 - 7 = 0$)
  4. $w = 0 \implies$ **Pedido #1 Descartado.**
* **Resultado:** Pedidos #{2, 4}, Tempo Total = **95 min**, Capacidade = $7 + 3 = 10$ pizzas ($100\%$ de ocupação).

### 9.2 Comprovação de Aceite no BeeCrowd
* **Submissão Oficial:** # 50429092
* **Problema:** 1286 - Motoboy
* **Status:** **Accepted**
* **Tempo de Execução:** $0.095 \text{ s}$
* **Linguagem:** Python 3.9
* **Data/Hora:** 07/11/2026 10:23:03

---

## 10. Considerações Finais

A Programação Dinâmica provou ser a técnica ideal e rigorosa para resolver o problema do Motoboy, transformando um problema NP-completo de natureza combinatória em uma execução computacional instantânea. As contribuições históricas de Richard Bellman continuam vigentes em sistemas cotidianos de ponta, reafirmando a importância do paradigma para a formação em Ciência da Computação na UFRPE.

---

## Declaração de Uso de Inteligência Artificial Generativa (Portaria nº 2.664/2026 – CNPq)

Em cumprimento ao Artigo 9º da Portaria nº 2.664/2026 do CNPq, declara-se que a ferramenta Google Antigravity / Gemini 3.8 Flash foi empregada como suporte auxiliar na concepção teórica, estruturação do artigo conforme o template SBC e revisão analítica da complexidade assintótica. A implementação computacional, testes, depuração e validação experimental foram executados e são de integral responsabilidade autoral do discente **José Albérico Rocha da Silva**.

---

## Referências

* BEECROWD. **Problema 1286: Motoboy**. BeeCrowd Academic Online Judge, 2026. Disponível em: <https://judge.beecrowd.com/pt/problems/view/1286>. Acesso em: 07 nov. 2026.
* BELLMAN, Richard. The theory of dynamic programming. **Bulletin of the American Mathematical Society**, v. 60, n. 6, p. 503-515, 1954.
* BELLMAN, Richard. **Dynamic Programming**. Princeton, NJ: Princeton University Press, 1957.
* BELLMAN, Richard. **Eye of the Hurricane: An Autobiography**. Singapore: World Scientific Publishing, 1984.
* CNPQ. **Portaria nº 2.664, de 6 de março de 2026: Diretrizes para uso de Inteligência Artificial Generativa em atividades de pesquisa e submissão acadêmica**. Brasília: MCTI/CNPq, 2026.
* CORMEN, Thomas H. et al. **Algoritmos: teoria e prática**. 3. ed. Rio de Janeiro: Elsevier, 2012.
* DANTZIG, George B. Discrete-variable extremum problems. **Operations Research**, v. 5, n. 2, p. 266-277, 1957.
* KARP, Richard M. Reducibility among combinatorial problems. *In*: MILLER, R. E.; THATCHER, J. W. (Ed.). **Complexity of Computer Computations**. New York: Plenum Press, 1972. p. 85-103.
* KLEINBERG, Jon; TARDOS, Éva. **Algorithm design**. Boston: Pearson/Addison-Wesley, 2006.
* SOCIEDADE BRASILEIRA DE COMPUTAÇÃO (SBC). **Instruções para autores de artigos da SBC**. Porto Alegre: SBC, 2024.
