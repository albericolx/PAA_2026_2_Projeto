# ROTEIRO DIDÁTICO DE APRESENTAÇÃO - PAA 2026.2 (UFRPE)
## Tema 6: BeeCrowd 1286 – Motoboy (Programação Dinâmica)
**Discente / Autor:** José Albérico Rocha da Silva  
**Docente:** Profª. Jeane Melo  
**Instituição:** Universidade Federal Rural de Pernambuco (UFRPE)  
**Tempo Estimado de Apresentação:** 20 minutos (± 5 minutos)  

---

## 🎯 Visão Geral dos 6 Pontos Atendidos

1. **Problema Claro e Ilustrado:** Ilustração visual da analogia do motoboy, das pizzas e do limite da mochila térmica.
2. **O Problema da Mochila (Knapsack 0/1) como Base:** Mapeamento isomorfo direto e justificativa matemática.
3. **Explicação da Técnica e Decisões de Projeto:** Sem passo a passo maçante nos slides, destacando a complexidade assintótica, a relação de recorrência de Bellman, a matriz $O(N \cdot P)$ para rastreabilidade e a otimização de espaço para vetor 1D $O(P)$ no BeeCrowd, acompanhado de exemplo de entrada e saída.
4. **Curiosidades Históricas e Aplicações Reais:** A origem do termo na Guerra Fria com Richard Bellman (RAND Corporation) e aplicações na logística de entregas (iFood/Rappi), alocação em nuvem (AWS/Google Cloud) e criptografia.
5. **Referências Acadêmicas Normatizadas:** Cormen (CLRS), Kleinberg & Tardos, Bellman (1954/1957), Karp (1972) e SBC.
6. **Roteiro Estruturado e Dinâmico:** Focado no essencial de cada tópico do artigo, articulado para prender a atenção da banca.

---

## 📽️ Estrutura Slide a Slide com Roteiro de Fala ("O que falar")

---

### SLIDE 1: Abertura e Identificação Institucional
* **Tempo:** 1 minuto
* **Elementos Visuais:** Brasão da UFRPE, logotipo do Departamento de Computação, Título do Trabalho, Nome do Discente (José Albérico Rocha da Silva) e da Professora (Profª Jeane Melo).
* **O que falar:**
  > "Bom dia a todos, bom dia professora Jeane. Meu nome é José Albérico Rocha da Silva e hoje apresento o projeto da 2ª Verificação de Aprendizagem da disciplina Projeto e Análise de Algoritmos. O nosso tema é o problema 1286 do BeeCrowd — Motoboy —, resolvido sob o paradigma de Programação Dinâmica."

---

### SLIDE 2: O Problema do Motoboy de Forma Clara e Ilustrada
* **Tempo:** 2 minutos
* **Elementos Visuais:** Ilustração gráfica de um entregador com uma mochila térmica (bag) com capacidade máxima limitada a $P$ pizzas, e uma lista de pedidos pendentes na pizzaria.
* **O que falar:**
  > "Vamos imaginar o cenário diário de uma pizzaria movimentada: o motoboy precisa sair para uma rodada de entregas. Ele tem diante de si uma lista com N pedidos disponíveis de clientes. Porém, existe uma limitação física intransponível: a mochila térmica dele suporta no máximo P pizzas.
  > Cada pedido possui duas características: a quantidade de pizzas que o cliente pediu (que ocupa espaço na bag) e o tempo estimado em minutos para que a entrega seja realizada.
  > A missão do motoboy é selecionar uma combinação de pedidos que caiba integralmente na mochila e que maximize o tempo total de entrega alocado. E aqui entra a restrição binária fundamental: um pedido não pode ser fracionado. Ou o motoboy leva o pedido inteiro, ou deixa para a próxima viagem."

---

### SLIDE 3: O Problema da Mochila (Knapsack 0/1) como Base Teórica
* **Tempo:** 3 minutos
* **Elementos Visuais:** Tabela comparativa estabelecendo o isomorfismo direto entre a Mochila Binária Clássica e o Motoboy.
* **Tabela no Slide:**
  | Elemento da Mochila 0-1 Clássica | Equivalente no Problema do Motoboy |
  | :--- | :--- |
  | Capacidade da Mochila ($W$) | Capacidade da Bag ($P$ pizzas) |
  | Itens disponíveis ($N$) | Pedidos de pizza ($N$) |
  | Peso do item ($w_i$) | Quantidade de pizzas do pedido ($p_i$) |
  | Valor/benefício ($v_i$) | Tempo de entrega em minutos ($t_i$) |
  | Decisão binária ($x_i \in \{0, 1\}$) | Entrega integral ou recusa |
* **O que falar:**
  > "Por que este problema é a base do nosso projeto? Porque o problema do Motoboy é um mapeamento isomorfo perfeito do célebre Problema da Mochila Binária (0/1 Knapsack Problem).
  > Esse é um dos problemas mais importantes de toda a Ciência da Computação, catalogado por Richard Karp em 1972 como um dos 21 problemas NP-completos fundamentais.
  > Compreender a mochila binária é o coração do projeto porque ela estabelece a fronteira exata entre abordagens intuitivas que falham e a elegância matemática da Programação Dinâmica."

---

### SLIDE 4: Análise Comparativa de Paradigmas
* **Tempo:** 2 minutos
* **Elementos Visuais:** Gráfico ou blocos comparativos: Força Bruta ($O(2^N)$), Algoritmo Guloso ($O(N \log N)$), e Programação Dinâmica ($O(N \cdot P)$).
* **O que falar:**
  > "Por que não resolvemos de outra forma?
  > Se tentássemos Força Bruta, teríamos que testar todos os subconjuntos possíveis de pedidos. Isso tem complexidade exponencial O de 2 elevado a N. Para apenas 30 pedidos, são mais de 1 bilhão de operações, estourando imediatamente o limite de tempo do BeeCrowd com Time Limit Exceeded.
  > E uma Abordagem Gulosa? Poderíamos pensar em ordenar os pedidos pelo maior tempo, ou pela melhor razão tempo por pizza. Mas a abordagem gulosa é míope: ela pode escolher um pedido grande e bloquear a mochila para uma combinação de pedidos menores que, somados, gerariam um tempo muito superior.
  > A Programação Dinâmica é a única que garante a solução exata em tempo eficiente, explorando o Princípio de Otimalidade de Bellman e a sobreposição de subproblemas."

---

### SLIDE 5: Decisões Arquiteturais de Projeto
* **Tempo:** 3 minutos
* **Elementos Visuais:** Diagrama da relação de recorrência de Bellman e o esquema das duas implementações (Matriz 2D vs Vetor 1D).
* **Equação em Destaque:**
  $$DP[i][w] = \max\left(DP[i-1][w], \, DP[i-1][w - p_i] + t_i\right)$$
* **O que falar:**
  > "Aqui estão as principais decisões de projeto que tomamos na nossa implementação:
  > 1. Princípio de Bellman: A decisão para o i-ésimo pedido com capacidade w resume-se a apenas duas escolhas: ou não levamos o pedido (e copiamos o melhor valor calculado na linha de cima), ou levamos o pedido (somando o tempo dele ao melhor valor obtido com a capacidade que sobrou). O algoritmo escolhe o maior entre os dois.
  > 2. Decisão de Estrutura de Dados: Para fins didáticos e para a nossa demonstração visual, implementamos a matriz bidimensional completa N por P. Isso nos dá a rastreabilidade total e permite executar o procedimento de retrocesso (backtracking) para identificar exatamente quais pedidos foram selecionados.
  > 3. Decisão de Desempenho para o BeeCrowd (Otimização O(P)): Para a submissão no juiz online, reduzimos a complexidade espacial de O(N·P) para O(P). Elaboramos um Diagrama de Blocos completo (disponível em docs/fluxo_otimizacao_espacial_1d.docx) mostrando que usamos um único vetor unidimensional percorrido em ordem decrescente (da direita para a esquerda). Isso impede que o mesmo pedido seja adicionado mais de uma vez e reduz o consumo de memória em 95,2%, aproveitando a cache do processador."

---

### SLIDE 6: Exemplo Concreto de Entrada e Saída
* **Tempo:** 2 minutos
* **Elementos Visuais:** Caixa com exemplo de entrada e saída.
  - **Entrada:**
    ```text
    4 10
    20 4
    15 3
    25 5
    10 2
    ```
  - **Saída:**
    ```text
    50 min.
    ```
* **O que falar:**
  > "Vejam este caso concreto que utilizamos no artigo: temos 4 pedidos e a mochila suporta 10 pizzas.
  > O algoritmo avalia todas as opções e encontra que a combinação ótima são os Pedidos 2, 3 e 4. Eles somam exatamente 3 + 5 + 2 = 10 pizzas, aproveitando 100% da capacidade da mochila, e entregam um tempo total de 15 + 25 + 10 = 50 minutos. A saída oficial do BeeCrowd é impressa no padrão estrito: '50 min.'."

---

### SLIDE 7: Demonstração Visual Interativa (Momento Prático)
* **Tempo:** 4 minutos
* **Ação:** Projetar o **Simulador Visual em HTML** ou o aplicativo **Streamlit**.
* **O que falar:**
  > "Agora, para tornar essa matemática tangível, desenvolvemos um simulador visual interativo.
  > Observem a matriz projetada na tela:
  > - Por que a linha 0 e a coluna 0 são preenchidas com zeros? Porque se a capacidade da bolsa for 0, não cabe nenhuma pizza; e se tivermos 0 pedidos disponíveis, o tempo obtido é nulo. Esses são os nossos casos base.
  > - Ao clicarmos em avançar célula a célula, vejam como o algoritmo calcula o valor: a célula em amarelo consulta apenas a célula verde de cima (não levar) e a célula azul deslocada à esquerda (levar com espaço restante).
  > - Quando a matriz é finalizada, o procedimento de backtracking parte da última célula e sobe a matriz: se o valor mudou em relação à linha anterior, significa que aquele pedido entrou na mochila. Os pedidos são destacados em roxo e exibidos nos cards."

---

### SLIDE 8: Curiosidades Históricas e Aplicações no Mundo Real
* **Tempo:** 3 minutos
* **Elementos Visuais:** Foto histórica de Richard Bellman na RAND Corporation e ícones de empresas modernas (iFood, AWS, Datacenters).
* **O que falar:**
  > "Gostaria de compartilhar uma curiosidade histórica fascinante sobre a origem da técnica:
  > O termo 'Programação Dinâmica' foi cunhado na década de 1950 pelo matemático Richard Bellman enquanto ele trabalhava na RAND Corporation durante a Guerra Fria.
  > O Secretário de Defesa americano da época, Charles Wilson, tinha uma aversão declarada a pesquisas matemáticas puras e teóricas e costumava cortar verbas dessa área. Bellman precisava batizar sua teoria com um nome que soasse prático, aplicado e impossível de ser questionado por militares e burocratas. Ele escolheu 'Programação' porque na época a palavra significava 'planejamento e logística militar', e acrescentou 'Dinâmica' para passar a ideia de movimento e energia. O próprio Bellman confessou em sua autobiografia que o nome foi um escudo protetor para salvar sua pesquisa matemática!
  > E onde isso é usado hoje no mundo real?
  > 1. Na logística de aplicativos como iFood, Rappi e Loggi para agrupamento inteligente de pedidos em tempo real;
  > 2. Na computação em nuvem (AWS e Google Cloud) para empacotamento de máquinas virtuais e contêineres Docker em servidores físicos;
  > 3. Na criptografia de chave pública, como o Criptossistema de Merkle-Hellman, cuja segurança se apoiava diretamente na dificuldade computacional do Knapsack."

---

### SLIDE 9: Validação Experimental no BeeCrowd
* **Tempo:** 1 minuto
* **Elementos Visuais:** Captura de tela oficial da submissão aceita (#50429092) e menção à Portaria CNPq nº 2.664/2026.
* **O que falar:**
  > "Nossa solução foi submetida e validada no juiz eletrônico do BeeCrowd sob a submissão número 50429092, conquistando o veredito de Accepted com um tempo de execução de apenas 0,095 segundos, comprovando a extrema eficiência do algoritmo implementado em Python 3.9."

---

### SLIDE 10: Conclusão e Referências Bibliográficas
* **Tempo:** 1 minuto
* **Elementos Visuais:** Lista de referências acadêmicas normatizadas (Cormen, Bellman, Kleinberg, Karp, SBC).
* **O que falar:**
  > "Para concluir, a Programação Dinâmica confirmou-se como a ferramenta exata e eficiente para contornar a explosão combinatória do problema da mochila. Agradeço a atenção da professora Jeane e dos colegas e coloco-me à disposição para perguntas. Muito obrigado!"

---

## ❓ Banco de Perguntas e Respostas da Professora Jeane Melo

1. **Pergunta da Professora:** *"Por que a abordagem gulosa falha no problema da mochila 0-1, enquanto funciona na mochila fracionária?"*  
   **Sua Resposta:** *"Na mochila fracionária nós podemos dividir os itens livremente, logo ordenar pela razão valor/peso (densidade de valor) garante a melhor escolha a cada passo. Já na mochila 0-1 a restrição é indivisível: escolher um item com alta densidade pode deixar um espaço 'vazio' na bolsa que não pode ser preenchido, enquanto itens com densidade ligeiramente menor poderiam se encaixar perfeitamente e somar um valor total muito maior. Essa indivisibilidade destrói a propriedade da escolha gulosa, exigindo a Programação Dinâmica."*

2. **Pergunta da Professora:** *"Como a otimização de espaço para vetor 1D garante que um mesmo pedido não seja levado duas vezes?"*  
   **Sua Resposta:** *"Porque nós percorremos o vetor de capacidades de trás para frente, de P até o peso do pedido atual. Ao atualizar $DP[w]$ olhando para $DP[w - p]$, nós acessamos um valor que ainda guarda o resultado da iteração do pedido anterior (i-1), e não da iteração atual. Se percorrêssemos de frente para trás, estaríamos resolvendo a mochila com repetição infinita (Unbounded Knapsack), pois o mesmo pedido poderia ser somado sobre si mesmo várias vezes."*

3. **Pergunta da Professora:** *"O algoritmo de Programação Dinâmica para a Mochila é polinomial ou pseudo-polinomial? O que isso significa?"*  
   **Sua Resposta:** *"Ele é pseudo-polinomial, com complexidade $O(N \cdot P)$. Isso significa que ele é polinomial em relação ao valor numérico da capacidade P, mas é exponencial em relação ao tamanho da entrada medido em número de bits, que é $\log_2(P)$. Por isso o problema continua pertencendo à classe dos problemas NP-difíceis no caso geral."*
