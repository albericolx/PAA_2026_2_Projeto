# ===============================================================================
# Universidade Federal Rural de Pernambuco (UFRPE)
# Departamento de Computação - Projeto e Análise de Algoritmos (PAA)
# Professora: Jeane Melo | Período: 2026.2
# Projeto VA2 - Tema 6: BeeCrowd 1286 - Motoboy
# Código com comentários linha por linha (simples, direto e sem jargões)
# Autor: José Albérico Rocha da Silva (autor)
# ===============================================================================

# Importa ferramentas do sistema para ler todas as entradas de uma vez só
import sys

# Função que descobre o maior tempo de entrega possível para um dia de trabalho
def resolver_caso(n, max_pizzas, pedidos):
    
    # Cria uma lista cheia de zeros com tamanho suficiente para todas as pizzas possíveis (de 0 até max_pizzas).
    # Cada posição dessa lista guarda o melhor tempo que conseguimos para aquele número de pizzas.
    dp = [0] * (max_pizzas + 1)
    
    # Passa por cada pedido da lista, pegando o tempo dele e a quantidade de pizzas que ele tem
    for tempo, pizzas in pedidos:
        
        # Olha as capacidades da moto da maior (max_pizzas) até o tamanho deste pedido (pizzas).
        # Andar de trás para frente garante que cada pedido só seja usado uma única vez na mesma viagem.
        for w in range(max_pizzas, pizzas - 1, -1):
            
            # Testa: se somar o tempo deste pedido com o que sobrava de espaço for melhor do que tínhamos antes...
            if dp[w - pizzas] + tempo > dp[w]:
                
                # ...então atualizamos com esse novo tempo maior!
                dp[w] = dp[w - pizzas] + tempo
                
    # Retorna o melhor tempo encontrado para a capacidade máxima da moto
    return dp[max_pizzas]


# Função principal que controla a leitura das entradas e a exibição das respostas
def main():
    
    # Lê todos os números digitados na tela ou enviados pelo arquivo de teste
    conteudo_completo = sys.stdin.read()
    
    # Divide todo o texto em uma lista de palavras/números separados por espaços ou quebras de linha
    tokens = conteudo_completo.split()
    
    # Se não houver nada para ler, encerra o programa imediatamente
    if not tokens:
        return
    
    # Variável que serve como um ponteiro para saber em qual número da lista estamos no momento
    indice = 0
    
    # Guarda a quantidade total de números lidos
    total_tokens = len(tokens)
    
    # Enquanto ainda existirem números na lista para serem processados...
    while indice < total_tokens:
        
        # Lê a quantidade de pedidos do dia (N)
        n = int(tokens[indice])
        
        # Avança o ponteiro para o próximo número
        indice += 1
        
        # Se N for igual a zero, significa que o programa deve parar (regra do problema)
        if n == 0:
            break
            
        # Lê a capacidade máxima de pizzas que a moto consegue carregar (P)
        max_pizzas = int(tokens[indice])
        
        # Avança o ponteiro para o próximo número
        indice += 1
        
        # Cria uma lista vazia para guardar os pedidos deste dia
        pedidos = []
        
        # Repete N vezes para ler os dados de cada um dos pedidos
        for _ in range(n):
            
            # Lê o tempo de entrega do pedido
            tempo = int(tokens[indice])
            
            # Lê quantas pizzas esse pedido tem
            pizzas = int(tokens[indice + 1])
            
            # Pula 2 números no ponteiro (pois acabamos de ler o tempo e as pizzas)
            indice += 2
            
            # Adiciona o par (tempo, pizzas) dentro da nossa lista de pedidos
            pedidos.append((tempo, pizzas))
            
        # Chama a função para calcular o melhor tempo para esse caso
        resultado = resolver_caso(n, max_pizzas, pedidos)
        
        # Imprime na tela o resultado no formato exigido pelo BeeCrowd (exemplo: "95 min.")
        print(f"{resultado} min.")


# Linha padrão do Python que faz o programa começar a rodar pela função main()
if __name__ == "__main__":
    main()
