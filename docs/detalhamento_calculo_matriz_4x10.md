# Detalhamento do Cálculo de Cada Elemento da Matriz (N = 4 x P = 10)
## Instância do Caso 1 do BeeCrowd 1286 (Motoboy)
**Discente / Autor:** José Albérico Rocha da Silva  
**Disciplina:** Projeto e Análise de Algoritmos (PAA 2026.2) - UFRPE  

---

### Dados dos Pedidos:
* **Pedido 1 ($i=1$):** Tempo = $20\text{ min}$, Pizzas = $5$
* **Pedido 2 ($i=2$):** Tempo = $70\text{ min}$, Pizzas = $7$
* **Pedido 3 ($i=3$):** Tempo = $15\text{ min}$, Pizzas = $2$
* **Pedido 4 ($i=4$):** Tempo = $25\text{ min}$, Pizzas = $3$

---

### Regra de Transição da Programação Dinâmica:
* Se $p_i > w$ (não cabe): $DP[i][w] = DP[i-1][w]$ (copia da célula acima)
* Se $p_i \le w$ (cabe): $DP[i][w] = \max(DP[i-1][w], \; t_i + DP[i-1][w - p_i])$

---

### Cálculos Detalhados por Linha e Coluna:

#### Linha 0 (Caso Base: 0 pedidos):
Todos os valores de $DP[0][w]$ para $w=0 \dots 10$ são iguais a **0**.

#### Linha 1 (Pedido 1: 20 min, 5 pizzas):
* $w=0 \dots 4$: $5 > w \implies DP[1][w] = \mathbf{0}$
* $w=5$: $\max(0, 20 + DP[0][0]) = \max(0, 20 + 0) = \mathbf{20}$
* $w=6 \dots 10$: $\max(0, 20 + 0) = \mathbf{20}$

#### Linha 2 (Pedido 2: 70 min, 7 pizzas):
* $w=0 \dots 4$: $7 > w \implies DP[2][w] = DP[1][w] = \mathbf{0}$
* $w=5 \dots 6$: $7 > w \implies DP[2][w] = DP[1][w] = \mathbf{20}$
* $w=7$: $\max(DP[1][7], 70 + DP[1][0]) = \max(20, 70 + 0) = \mathbf{70}$
* $w=8 \dots 10$: $\max(20, 70 + 0) = \mathbf{70}$

#### Linha 3 (Pedido 3: 15 min, 2 pizzas):
* $w=0 \dots 1$: $DP[3][w] = \mathbf{0}$
* $w=2 \dots 4$: $\max(0, 15 + DP[2][0]) = \mathbf{15}$
* $w=5 \dots 6$: $\max(20, 15 + DP[2][3]) = \max(20, 15 + 0) = \mathbf{20}$
* $w=7 \dots 8$: $\max(70, 15 + DP[2][5]) = \max(70, 15 + 20) = \max(70, 35) = \mathbf{70}$
* $w=9$: $\max(DP[2][9], 15 + DP[2][7]) = \max(70, 15 + 70) = \mathbf{85}$
* $w=10$: $\max(DP[2][10], 15 + DP[2][8]) = \max(70, 15 + 70) = \mathbf{85}$

#### Linha 4 (Pedido 4: 25 min, 3 pizzas):
* $w=0 \dots 1$: $DP[4][w] = \mathbf{0}$
* $w=2$: $DP[4][2] = DP[3][2] = \mathbf{15}$
* $w=3 \dots 4$: $\max(15, 25 + DP[3][0]) = \mathbf{25}$
* $w=5 \dots 6$: $\max(20, 25 + DP[3][2]) = \max(20, 25 + 15) = \mathbf{40}$
* $w=7$: $\max(70, 25 + DP[3][4]) = \max(70, 25 + 15) = \mathbf{70}$
* $w=8$: $\max(70, 25 + DP[3][5]) = \max(70, 25 + 20) = \mathbf{70}$
* $w=9$: $\max(85, 25 + DP[3][6]) = \max(85, 25 + 20) = \mathbf{85}$
* $w=10$: $\max(85, 25 + DP[3][7]) = \max(85, 25 + 70) = \mathbf{95}$ (**Solução Ótima**)

---

### Matriz Final DP[i][w]:

| i \ w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** | 0 | 0 | 0 | 0 | 0 | 20 | 20 | 20 | 20 | 20 | 20 |
| **2** | 0 | 0 | 0 | 0 | 0 | 20 | 20 | 70 | 70 | 70 | 70 |
| **3** | 0 | 0 | 15 | 15 | 15 | 20 | 20 | 70 | 70 | 85 | 85 |
| **4** | 0 | 0 | 15 | 25 | 25 | 40 | 40 | 70 | 70 | 85 | **95** |
