# 📐 Diagrama de Blocos e Fluxo de Tomada de Decisão: Otimização Espacial O(P)
> **Universidade Federal Rural de Pernambuco (UFRPE)**  
> **Departamento de Computação — Projeto e Análise de Algoritmos (PAA) – 2026.2**  
> **Docente:** Profª. Drª. Jeane Melo  
> **Discente / Autor:** José Albérico Rocha da Silva  
> **Tema:** Tema 6 – BeeCrowd 1286: Motoboy (Mochila Binária 0-1)  

---

## 1. Código de Produção Analisado

```python
def resolver_caso(n, max_pizzas, pedidos):
    # 1. Alocação do vetor 1D inicializado com zeros
    dp = [0] * (max_pizzas + 1)
    
    # 2. Laço Externo: Processa cada pedido sequencialmente
    for tempo, pizzas in pedidos:
        # 3. Laço Interno: Varredura DECRESCENTE para garantir propriedade 0-1
        for w in range(max_pizzas, pizzas - 1, -1):
            # 4. Decisão de Bellman In-Place: Levar vs Manter
            if dp[w - pizzas] + tempo > dp[w]:
                dp[w] = dp[w - pizzas] + tempo
                
    # 5. O valor ótimo global reside na última posição
    return dp[max_pizzas]
```

---

## 2. Fluxograma em Mermaid (Diagrama de Blocos Completo)

```mermaid
flowchart TD
    Inicio(["🏁 INÍCIO: resolver_caso(n, max_pizzas, pedidos)"]) --> Alocacao["📦 1. Alocar Vetor 1D:<br>dp = [0] * (max_pizzas + 1)<br><i>Espaço O(P) em memória contígua</i>"]
    
    Alocacao --> LoopPedidos{"🔄 2. LAÇO EXTERNO:<br>Há mais pedidos em 'pedidos'?"}
    
    LoopPedidos -- NÃO: Todos processados --> Retorno["🏆 5. Retornar dp[max_pizzas]<br><i>Valor ótimo global</i>"]
    Retorno --> Fim(["🛑 FIM"])
    
    LoopPedidos -- SIM: Pega próximo pedido --> ExtrairItem["📋 Extrair Pedido Atual:<br>tempo (ganho) e pizzas (peso)"]
    
    ExtrairItem --> InitW["⏱️ 3. Inicializar Varredura Reversa:<br>w = max_pizzas"]
    
    InitW --> ChecaW{"🔍 w >= pizzas?<br><i>(O pedido cabe na capacidade w?)</i>"}
    
    ChecaW -- NÃO: w < pizzas --> LoopPedidos
    
    ChecaW -- SIM: w >= pizzas --> DecisaoBellman{"⚖️ 4. DECISÃO DE BELLMAN:<br>dp[w - pizzas] + tempo > dp[w]?"}
    
    DecisaoBellman -- "SIM (Vence LEVAR)" --> Atualiza["✅ ATUALIZAR IN-PLACE:<br>dp[w] = dp[w - pizzas] + tempo<br><i>Ganha tempo e consome espaço residual</i>"]
    
    DecisaoBellman -- "NÃO (Vence MANTER)" --> Mantem["⏸️ MANTER ANTERIOR:<br>dp[w] permanece inalterado<br><i>Solução prévia é melhor ou igual</i>"]
    
    Atualiza --> DecrementaW["⬅️ Decrementar:<br>w = w - 1"]
    Mantem --> DecrementaW
    
    DecrementaW --> ChecaW

    classDef startend fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef process fill:#1e293b,stroke:#64748b,stroke-width:1.5px,color:#f8fafc;
    classDef decision fill:#312e81,stroke:#818cf8,stroke-width:2px,color:#fff;
    classDef success fill:#065f46,stroke:#34d399,stroke-width:2px,color:#fff;
    classDef keep fill:#78350f,stroke:#f59e0b,stroke-width:1.5px,color:#fff;
    classDef loop fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#fff;

    class Inicio,Fim,Retorno startend;
    class Alocacao,ExtrairItem,InitW,DecrementaW process;
    class LoopPedidos,ChecaW loop;
    class DecisaoBellman decision;
    class Atualiza success;
    class Mantem keep;
```

---

## 3. Por que a Varredura DECRESCENTE é o Ponto Crítico da Lógica?

### ❌ Se a varredura fosse CRESCENTE ($w = pizzas \to P$):
O mesmo item seria somado **múltiplas vezes**, violando a restrição binária 0-1 e transformando o algoritmo na Mochila Ilimitada (*Unbounded Knapsack*):
* Suponha um pedido com `tempo = 20`, `pizzas = 2` e vetor inicial zerado:
  * Em $w=2$: $dp[2] = \max(0, dp[0] + 20) = 20$.
  * Em $w=4$: $dp[4] = \max(0, dp[2] + 20) = 20 + 20 = \mathbf{40}$! *(Erro: o pedido foi duplicado na mesma bag!)*

### ✅ Como a varredura DECRESCENTE ($w = P \to pizzas$) resolve perfeitamente:
Como iteramos da direita para a esquerda:
* Ao calcular a posição $w$, a posição $w - pizzas$ ainda **NÃO foi modificada nesta rodada**!
* Portanto, $dp[w - pizzas]$ contém genuinamente o resultado da rodada anterior ($i-1$).
* Cada pedido é computado no máximo **UMA ÚNICA VEZ por rota**, garantindo 100% de precisão matemática sem precisar de matriz bidimensional!

---

## 4. Evolução Numérica do Vetor $DP$ no Caso BeeCrowd 1 ($N=4, P=10$)

| Estágio de Execução | $w=0$ | $w=1$ | $w=2$ | $w=3$ | $w=4$ | $w=5$ | $w=6$ | $w=7$ | $w=8$ | $w=9$ | $w=10$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Inicial (`dp = [0]*11`)** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Após Pedido 1 (20m, 5pz)** | 0 | 0 | 0 | 0 | 0 | **20** | **20** | **20** | **20** | **20** | **20** |
| **Após Pedido 2 (70m, 7pz)** | 0 | 0 | 0 | 0 | 0 | 20 | 20 | **70** | **70** | **70** | **70** |
| **Após Pedido 3 (15m, 2pz)** | 0 | 0 | **15** | **15** | **15** | 20 | 20 | 70 | 70 | **85** | **85** |
| **Após Pedido 4 (25m, 3pz)** | 0 | 0 | 15 | **25** | **25** | **40** | **40** | 70 | 70 | 85 | **🔥 95** |

* **Resultado Ótimo Global:** `dp[10] = 95 minutos`.
* **Consumo de Memória:** Apenas 11 posições inteiras em vez das 55 da matriz $5 \times 11$.

---

## 5. Roteiro Verbal para a Apresentação Oral (Slide de Otimização)

> *"Professora Jeane, na nossa solução oficial do BeeCrowd nós implementamos uma otimização clássica de engenharia de software:*  
> *Em vez de guardarmos a matriz inteira de 55 células, nós notamos que para calcular a linha atual $i$, nós só olhamos para a linha imediatamente acima $i-1$. Por isso, reduzimos toda a matriz a um **único vetor unidimensional de tamanho $P+1$**, economizando mais de $95\%$ de memória RAM.*  
>  
> *O grande segredo matemático dessa implementação é que o laço de capacidades precisa rodar **da direita para a esquerda (decrescente)**. Se rodássemos da esquerda para a direita, um pedido seria somado várias vezes na mesma viagem da moto. Ao rodar de trás para frente, quando calculamos `dp[w]`, a posição `dp[w - pizzas]` ainda guarda o valor da rodada anterior, garantindo que o pedido seja considerado no máximo uma única vez, preservando a propriedade 0-1 da mochila!"*
