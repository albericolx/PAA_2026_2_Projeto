# ===============================================================================
# Universidade Federal Rural de Pernambuco (UFRPE)
# Departamento de Computação - Projeto e Análise de Algoritmos (PAA)
# Professora: Jeane Melo | Período: 2026.2
# Projeto VA2 - Tema 6: BeeCrowd 1286 - Motoboy
# Script Didático com comentários linha a linha (linguagem simples e direta)
# Autor: José Albérico Rocha da Silva (autor)
# ===============================================================================

# Importa a ferramenta de medição de tempo para marcar quantos milissegundos o computador gasta
import time


# Função que imprime um texto explicativo na tela para quem está vendo o problema pela primeira vez
def explicar_logica_passo_a_passo():
    
    # Imprime uma linha de separação com 80 asteriscos para organizar a tela
    print("*" * 80)
    
    # Imprime o título do guia explicativo
    print(" GUIA DIDÁTICO: COMO A TABELA É PREENCHIDA E COMO AS CONTAS SÃO FEITAS")
    
    # Imprime outra linha de asteriscos
    print("*" * 80)
    
    # Texto em bloco com explicações sem jargões
    print("""
1. O QUE CADA CASINHA DA TABELA SIGNIFICA:
   A casinha da linha 'i' e coluna 'w' guarda uma resposta simples:
   "Se José só pudesse escolher entre os primeiros 'i' pedidos, e a moto
    só aguentasse 'w' pizzas, qual seria o maior tempo de entrega possível?"

2. POR QUE A PRIMEIRA LINHA E A PRIMEIRA COLUNA SÃO ZERO?
   - Primeira Linha (0 pedidos):
     Se a pizzaria não tem nenhum pedido para entregar, o tempo trabalhado é 0.
   - Primeira Coluna (0 pizzas):
     Se a moto não consegue levar nenhuma pizza, não dá para fazer entrega alguma,
     então o tempo trabalhado também é 0.

3. COMO É FEITA A CONTA PARA CADA CASINHA?
   Para cada pedido, olhamos duas coisas: o tempo dele e quantas pizzas ele tem.
   
   - Se o pedido NÃO CABE na moto (tem mais pizzas do que a moto suporta):
     Não tem o que fazer. O tempo continua sendo o mesmo que já tínhamos sem ele.
     Copiamos o valor da casinha de cima!

   - Se o pedido CABE na moto:
     Temos duas escolhas e ficamos com a que der MAIS TEMPO:
     * Escolha 1: NÃO LEVAR o pedido (o tempo fica sendo o da casinha de cima).
     * Escolha 2: LEVAR o pedido (ganhamos o tempo dele e somamos com o melhor
       resultado que dava para fazer com as pizzas que sobraram de espaço).

4. COMO DESCOBRIR QUAIS PEDIDOS FORAM ESCOLHIDOS NO FINAL?
   Olhamos a última casinha da tabela (canto inferior direito) e fazemos o caminho de volta:
   - Se o valor mudou em relação à casinha de cima, significa que aquele pedido FOI LEVADO.
     Então subtraímos as pizzas dele da capacidade e subimos para a linha anterior.
   - Se o valor for igual ao da casinha de cima, aquele pedido NÃO FOI LEVADO.
   Repetimos isso até voltar ao início!
""")
    
    # Imprime a linha de fechamento
    print("*" * 80 + "\n")


# Função que monta a tabela, calcula o tempo máximo e descobre quais pedidos foram escolhidos
def resolver_com_rastreamento(n, max_pizzas, pedidos, exibir_passos=True):
    
    # Cria a tabela cheia de zeros: tem (n + 1) linhas e (max_pizzas + 1) colunas
    dp = [[0] * (max_pizzas + 1) for _ in range(n + 1)]
    
    # Percorre cada um dos pedidos, do primeiro (1) até o último (n)
    for i in range(1, n + 1):
        
        # Pega o tempo do pedido atual na lista (lembrando que em Python a lista começa do 0)
        tempo_i = pedidos[i - 1]['tempo']
        
        # Pega a quantidade de pizzas do pedido atual
        pizzas_i = pedidos[i - 1]['pizzas']
        
        # Testa todas as capacidades possíveis de pizzas na moto, de 0 até o limite máximo
        for w in range(max_pizzas + 1):
            
            # Se o pedido atual couber na capacidade atual 'w'...
            if pizzas_i <= w:
                
                # Opção sem levar: valor da casinha de cima (dp[i - 1][w])
                sem_levar = dp[i - 1][w]
                
                # Opção levando: tempo deste pedido + melhor valor para o espaço que sobrou
                levando = dp[i - 1][w - pizzas_i] + tempo_i
                
                # Escolhe o maior entre as duas opções e guarda na tabela
                dp[i][w] = max(sem_levar, levando)
                
            else:
                # Se o pedido não couber, não há escolha: copia o valor da casinha de cima
                dp[i][w] = dp[i - 1][w]
                
    # O melhor tempo possível de todos fica guardado na última casinha da tabela
    tempo_otimo = dp[n][max_pizzas]
    
    # Cria uma lista vazia para guardar quais pedidos foram colocados na moto
    pedidos_escolhidos = []
    
    # Começa com a capacidade máxima de pizzas para fazer o caminho inverso
    w_restante = max_pizzas
    
    # Caminha de trás para frente, do último pedido (n) até o primeiro (1)
    for i in range(n, 0, -1):
        
        # Se o valor for diferente da casinha de cima, significa que este pedido entrou na moto!
        if dp[i][w_restante] != dp[i - 1][w_restante]:
            
            # Adiciona o pedido na nossa lista de escolhidos
            pedidos_escolhidos.append(pedidos[i - 1])
            
            # Desconta a quantidade de pizzas deste pedido da capacidade que tínhamos
            w_restante -= pedidos[i - 1]['pizzas']
            
    # Inverte a lista de pedidos escolhidos para mostrar na ordem em que apareceram no início
    pedidos_escolhidos.reverse()
    
    # Soma todas as pizzas dos pedidos que foram escolhidos para ver quanto do baú foi ocupado
    pizzas_utilizadas = sum(p['pizzas'] for p in pedidos_escolhidos)
    
    # Se pedimos para mostrar o passo a passo na tela...
    if exibir_passos:
        
        # Imprime uma barra horizontal para separar
        print("=" * 78)
        
        # Imprime o cabeçalho informando o número de pedidos e o limite da moto
        print(f" DEMONSTRAÇÃO PRÁTICA: EXECUÇÃO DO CASO DE TESTE (N={n}, P={max_pizzas})")
        
        # Imprime outra barra horizontal
        print("=" * 78)
        
        # Título da listagem de pedidos
        print("Tabela de Pedidos Recebidos na Pizzaria:")
        
        # Cabeçalho das colunas com espaçamento formatado
        print(f" {'ID':<4} | {'Tempo de Entrega (min)':<25} | {'Quantidade de Pizzas':<22}")
        
        # Linha tracejada
        print("-" * 58)
        
        # Passa por cada pedido e imprime seus dados linha por linha
        for p in pedidos:
            print(f" #{p['id']:<3} | {p['tempo']:<25} | {p['pizzas']:<22}")
            
        # Linha tracejada
        print("-" * 58)
        
        # Título da tabela calculada
        print("\nMATRIZ COMPLETA CALCULADA PELO PROGRAMA dp[i][w]:")
        print("(Linhas 'i' = pedidos considerados; Colunas 'w' = capacidade da moto de 0 a P)")
        
        # Monta o cabeçalho superior mostrando os números das colunas (de 0 até max_pizzas)
        header = " i \\ w |" + "".join(f"{w:4d}" for w in range(max_pizzas + 1))
        
        # Linha divisória
        print("-" * len(header))
        
        # Imprime o cabeçalho das colunas
        print(header)
        
        # Linha divisória
        print("-" * len(header))
        
        # Imprime cada linha da tabela com seus valores calculados
        for i in range(n + 1):
            linha = f" {i:4d} |" + "".join(f"{dp[i][w]:4d}" for w in range(max_pizzas + 1))
            print(linha)
            
        # Linha divisória
        print("-" * len(header))
        
        # Imprime a seção de conclusão
        print("\n" + "=" * 78)
        print(" DECISÃO FINAL: RESULTADO QUE JOSÉ DEVE SEGUIR")
        print("=" * 78)
        
        # Mostra o tempo máximo total obtido
        print(f"-> Tempo Máximo de Trabalho: {tempo_otimo} min.")
        
        # Mostra quantas pizzas a moto vai carregar e quantas vagas sobraram
        print(f"-> Pizzas Transportadas:     {pizzas_utilizadas} de {max_pizzas} (Vagas vazias: {max_pizzas - pizzas_utilizadas})")
        
        # Mostra a quantidade de pedidos que ele deve aceitar
        print(f"-> Total de Pedidos Aceitos: {len(pedidos_escolhidos)} pedido(s)")
        
        # Lista cada pedido aceito com seu tempo e pizzas
        for p in pedidos_escolhidos:
            print(f"   * Pedido #{p['id']}: Demora {p['tempo']} min | Ocupa {p['pizzas']} pizzas")
            
        # Barra horizontal final
        print("=" * 78)
        
    # Retorna o tempo ótimo e a lista de pedidos escolhidos
    return tempo_otimo, pedidos_escolhidos


# Função que roda os dois casos oficiais do problema para demonstração
def executar_exemplos_beecrowd():
    
    # 1. Primeiro mostra a explicação didática das contas
    explicar_logica_passo_a_passo()
    
    # Imprime uma faixa divisória
    print("#" * 78)
    print(" EXECUÇÃO DOS CASOS DE TESTE OFICIAIS DO BEECROWD 1286")
    print("#" * 78 + "\n")
    
    # Dados do Caso 1 do problema oficial: 4 pedidos e moto aguenta 10 pizzas
    pedidos_caso1 = [
        {'id': 1, 'tempo': 20, 'pizzas': 5},
        {'id': 2, 'tempo': 70, 'pizzas': 7},
        {'id': 3, 'tempo': 15, 'pizzas': 2},
        {'id': 4, 'tempo': 25, 'pizzas': 3}
    ]
    
    # Avisa que vai rodar o Caso 1
    print(">>> CASO DE TESTE 1 (Oficial do BeeCrowd):")
    
    # Marca o relógio no início
    inicio = time.perf_counter()
    
    # Executa a função que calcula tudo
    tempo_max1, _ = resolver_com_rastreamento(4, 10, pedidos_caso1, exibir_passos=True)
    
    # Marca o relógio no fim
    fim = time.perf_counter()
    
    # Imprime a resposta exatamente como o site BeeCrowd espera
    print(f"Saída no formato do BeeCrowd: {tempo_max1} min.")
    
    # Imprime o tempo que o processador gastou em milissegundos
    print(f"Tempo que o computador gastou: {(fim - inicio)*1000:.4f} ms\n")
    
    # Dados do Caso 2 do problema oficial: 2 pedidos e moto aguenta 20 pizzas
    pedidos_caso2 = [
        {'id': 1, 'tempo': 52, 'pizzas': 9},
        {'id': 2, 'tempo': 10, 'pizzas': 12}
    ]
    
    # Avisa que vai rodar o Caso 2
    print("\n>>> CASO DE TESTE 2 (Oficial do BeeCrowd):")
    
    # Marca o relógio no início
    inicio = time.perf_counter()
    
    # Executa a função que calcula tudo
    tempo_max2, _ = resolver_com_rastreamento(2, 20, pedidos_caso2, exibir_passos=True)
    
    # Marca o relógio no fim
    fim = time.perf_counter()
    
    # Imprime a resposta no formato do BeeCrowd
    print(f"Saída no formato do BeeCrowd: {tempo_max2} min.")
    
    # Imprime o tempo gasto pelo computador
    print(f"Tempo que o computador gastou: {(fim - inicio)*1000:.4f} ms\n")


# Inicia o programa chamando a função de execução dos exemplos
if __name__ == "__main__":
    executar_exemplos_beecrowd()
