# ===============================================================================
# Universidade Federal Rural de Pernambuco (UFRPE)
# Departamento de Computação - Projeto e Análise de Algoritmos (PAA)
# Professora: Jeane Melo | Período: 2026.2
# Projeto VA2 - Tema 6: BeeCrowd 1286 - Motoboy
# Simulador Interativo em Python Puro (Terminal / VS Code)
# Autor: José Albérico Rocha da Silva (autor)
# ===============================================================================

import sys
import time
import os

# Configuração de cores ANSI para o terminal (compatível com VS Code e terminais modernos)
class Cor:
    RESET = "\033[0m"
    NEGRITO = "\033[1m"
    DIM = "\033[2m"
    
    # Cores de texto
    VERDE = "\033[92m"
    VERMELHO = "\033[91m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    CIANO = "\033[96m"
    BRANCO = "\033[97m"
    
    # Fundos
    BG_AZUL = "\033[44m"
    BG_VERDE = "\033[42m"
    BG_MAGENTA = "\033[45m"
    BG_ESCURO = "\033[100m"

# Verifica se o terminal suporta cores ANSI
if not sys.stdout.isatty() and os.name == 'nt':
    os.system('')  # Habilita suporte a ANSI no Windows 10/11 cmd/powershell


def limpar_tela():
    """Limpa o console de forma compatível com Windows e Unix."""
    # Opcional: não limpar agressivamente para permitir rolagem no VS Code
    pass


def imprimir_banner():
    """Imprime o cabeçalho oficial do projeto acadêmico."""
    print(f"\n{Cor.CIANO}{'=' * 80}{Cor.RESET}")
    print(f"{Cor.NEGRITO}{Cor.BRANCO} 🛵 SIMULADOR DIDÁTICO INTERATIVO: MOTOBOY (BEECROWD 1286){Cor.RESET}")
    print(f" {Cor.AMARELO}Paradigma:{Cor.RESET} Programação Dinâmica (Mochila Binária 0-1) | O(N·P)")
    print(f" {Cor.AZUL}UFRPE 2026.2{Cor.RESET} - Projeto e Análise de Algoritmos | Profª Jeane Melo")
    print(f" {Cor.VERDE}Autor:{Cor.RESET} José Albérico Rocha da Silva (autor)")
    print(f"{Cor.CIANO}{'=' * 80}{Cor.RESET}\n")


def menu_configuracao_inicial():
    """Permite ao usuário carregar casos oficiais ou digitar valores personalizados."""
    print(f"{Cor.NEGRITO}⚙️  1. ESCOLHA O CENÁRIO DE DADOS:{Cor.RESET}")
    print(f"  {Cor.VERDE}[1]{Cor.RESET} Caso 1 Oficial BeeCrowd  (N = 4 pedidos, Capacidade P = 10 pizzas)")
    print(f"  {Cor.VERDE}[2]{Cor.RESET} Caso 2 Oficial BeeCrowd  (N = 2 pedidos, Capacidade P = 20 pizzas)")
    print(f"  {Cor.VERDE}[3]{Cor.RESET} Caso Didático Simples   (N = 3 pedidos, Capacidade P = 5 pizzas)")
    print(f"  {Cor.AMARELO}[4]{Cor.RESET} Cenário Personalizado    (Você digita P, N e cada um dos pedidos)")
    print(f"  {Cor.VERMELHO}[0]{Cor.RESET} Sair do Programa")

    while True:
        opcao = input(f"\n{Cor.NEGRITO}Selecione uma opção [1-4] (ou 0 para sair): {Cor.RESET}").strip()
        if opcao == "1":
            P = 10
            pedidos = [
                {"id": 1, "tempo": 20, "pizzas": 5},
                {"id": 2, "tempo": 70, "pizzas": 7},
                {"id": 3, "tempo": 15, "pizzas": 2},
                {"id": 4, "tempo": 25, "pizzas": 3}
            ]
            return P, pedidos
        elif opcao == "2":
            P = 20
            pedidos = [
                {"id": 1, "tempo": 52, "pizzas": 9},
                {"id": 2, "tempo": 10, "pizzas": 12}
            ]
            return P, pedidos
        elif opcao == "3":
            P = 5
            pedidos = [
                {"id": 1, "tempo": 12, "pizzas": 2},
                {"id": 2, "tempo": 18, "pizzas": 3},
                {"id": 3, "tempo": 24, "pizzas": 4}
            ]
            return P, pedidos
        elif opcao == "4":
            return coletar_dados_usuario()
        elif opcao == "0":
            print(f"\n{Cor.AMARELO}Encerrando o simulador. Até logo!{Cor.RESET}\n")
            sys.exit(0)
        else:
            print(f"{Cor.VERMELHO}Opção inválida! Digite 1, 2, 3, 4 ou 0.{Cor.RESET}")


def coletar_dados_usuario():
    """Coleta os dados digitados livremente pelo usuário no terminal."""
    print(f"\n{Cor.CIANO}{'─' * 60}{Cor.RESET}")
    print(f"{Cor.NEGRITO}📝 CONFIGURAÇÃO PERSONALIZADA DOS DADOS{Cor.RESET}")
    print(f"{Cor.CIANO}{'─' * 60}{Cor.RESET}")

    # 1. Capacidade máxima da mochila P
    while True:
        try:
            p_str = input(f"• Capacidade máxima da mochila {Cor.AMARELO}(P pizzas){Cor.RESET} [1 a 50]: ").strip()
            P = int(p_str)
            if 1 <= P <= 50:
                break
            print(f"{Cor.VERMELHO}Por favor, digite uma capacidade entre 1 e 50 pizzas.{Cor.RESET}")
        except ValueError:
            print(f"{Cor.VERMELHO}Valor inválido! Digite um número inteiro.{Cor.RESET}")

    # 2. Quantidade de pedidos N
    while True:
        try:
            n_str = input(f"• Quantidade de pedidos desejada {Cor.AMARELO}(N){Cor.RESET} [1 a 15]: ").strip()
            N = int(n_str)
            if 1 <= N <= 15:
                break
            print(f"{Cor.VERMELHO}Por favor, digite uma quantidade de pedidos entre 1 e 15.{Cor.RESET}")
        except ValueError:
            print(f"{Cor.VERMELHO}Valor inválido! Digite um número inteiro.{Cor.RESET}")

    pedidos = []
    print(f"\n{Cor.NEGRITO}Agora digite o Tempo e a Quantidade de Pizzas de cada pedido:{Cor.RESET}")
    for i in range(1, N + 1):
        print(f"\n{Cor.CIANO}--- Pedido #{i} ---{Cor.RESET}")
        while True:
            try:
                t = int(input(f"  Tempo de entrega em minutos (t_{i}): ").strip())
                if t > 0:
                    break
                print(f"{Cor.VERMELHO}O tempo deve ser maior que zero!{Cor.RESET}")
            except ValueError:
                print(f"{Cor.VERMELHO}Número inválido! Digite um número inteiro.{Cor.RESET}")

        while True:
            try:
                pz = int(input(f"  Quantidade de pizzas do pedido (p_{i}): ").strip())
                if pz > 0:
                    break
                print(f"{Cor.VERMELHO}A quantidade de pizzas deve ser maior que zero!{Cor.RESET}")
            except ValueError:
                print(f"{Cor.VERMELHO}Número inválido! Digite um número inteiro.{Cor.RESET}")

        pedidos.append({"id": i, "tempo": t, "pizzas": pz})

    return P, pedidos


def exibir_tabela_pedidos(pedidos, P):
    """Exibe um quadro formatado dos pedidos recebidos e dados da bag."""
    demanda_total_pizzas = sum(p['pizzas'] for p in pedidos)
    tempo_bruto_total = sum(p['tempo'] for p in pedidos)

    print(f"\n{Cor.CIANO}{'─' * 65}{Cor.RESET}")
    print(f"{Cor.NEGRITO}📦 TABELA DE PEDIDOS CADASTRADOS{Cor.RESET}")
    print(f"{Cor.CIANO}{'─' * 65}{Cor.RESET}")
    print(f" {'ID':^4} | {'Tempo (min)':^13} | {'Pizzas':^10} | {'Relação (min/pizza)':^20}")
    print(f"{Cor.CIANO}{'─' * 65}{Cor.RESET}")
    for p in pedidos:
        razao = p['tempo'] / p['pizzas']
        print(f" #{p['id']:<3} | {p['tempo']:>9} min  | {p['pizzas']:>7} pz | {razao:>15.2f} min/pz")
    print(f"{Cor.CIANO}{'─' * 65}{Cor.RESET}")
    print(f"• {Cor.NEGRITO}Capacidade da Mochila (P):{Cor.RESET} {P} pizzas")
    print(f"• {Cor.NEGRITO}Total de Pedidos (N):{Cor.RESET}      {len(pedidos)} pedidos")
    print(f"• {Cor.NEGRITO}Demanda Total:{Cor.RESET}             {demanda_total_pizzas} pizzas (Capacidade é {P} pizzas)")
    print(f"• {Cor.NEGRITO}Tempo Bruto Somado:{Cor.RESET}        {tempo_bruto_total} min (Se pudesse levar todos)")
    print(f"{Cor.CIANO}{'─' * 65}{Cor.RESET}\n")


def imprimir_matriz_formatada(dp, pedidos, P, destaque_i=None, destaque_w=None):
    """Imprime a matriz DP completa alinhada com destaque de células se fornecido."""
    N = len(pedidos)
    print(f"\n{Cor.NEGRITO}📊 MATRIZ DE PROGRAMAÇÃO DINÂMICA DP[i][w]:{Cor.RESET}")
    print(f"{Cor.DIM}(Linhas 'i' = pedidos considerados | Colunas 'w' = capacidade da moto de 0 a {P}){Cor.RESET}\n")

    # Cabeçalho das colunas w=0 .. P
    cabecalho = f"{'Linha / Pedido':<20} |"
    for w in range(P + 1):
        cabecalho += f" {w:^3} |"
    print(f"{Cor.AZUL}{cabecalho}{Cor.RESET}")
    print(f"{Cor.AZUL}{'─' * len(cabecalho)}{Cor.RESET}")

    for i in range(N + 1):
        if i == 0:
            rotulo = "Base 0 (0 pz)"
        else:
            ped = pedidos[i - 1]
            rotulo = f"P{ped['id']} ({ped['tempo']}m,{ped['pizzas']}pz)"

        linha_str = f"{rotulo:<20} |"
        for w in range(P + 1):
            val = dp[i][w]
            val_txt = f"{val:^3}"

            # Destaques visuais
            if i == destaque_i and w == destaque_w:
                val_txt = f"{Cor.BG_VERDE}{Cor.BRANCO}{val_txt}{Cor.RESET}"
            elif i == destaque_i and destaque_w is not None and w < destaque_w:
                val_txt = f"{Cor.VERDE}{val_txt}{Cor.RESET}"
            linha_str += f" {val_txt} |"

        print(linha_str)
    print(f"{Cor.AZUL}{'─' * len(cabecalho)}{Cor.RESET}\n")


def construir_matriz_dp(pedidos, P, passo_a_passo=False):
    """
    Constrói a matriz de Programação Dinâmica DP[N+1][P+1].
    Se passo_a_passo=True, exibe o cálculo detalhado de cada célula com substituição.
    """
    N = len(pedidos)
    dp = [[0] * (P + 1) for _ in range(N + 1)]

    t_inicio = time.perf_counter()

    for i in range(1, N + 1):
        ped = pedidos[i - 1]
        t_i = ped["tempo"]
        p_i = ped["pizzas"]

        for w in range(1, P + 1):
            val_cima = dp[i - 1][w]

            if p_i > w:
                # CASO 1: O pedido não cabe na mochila
                dp[i][w] = val_cima
                ramo = "CASO 1 (NÃO CABE)"
                condicao = f"p_{i} ({p_i} pz) > w ({w} pz)"
                formula_txt = f"DP[{i-1}][{w}] = {val_cima} min"
                decisao_txt = f"{Cor.VERMELHO}DEIXAR O PEDIDO{Cor.RESET} (excede a capacidade residual)"
            else:
                # CASO 2: O pedido cabe na mochila
                w_rest = w - p_i
                val_rest = dp[i - 1][w_rest]
                val_levar = val_rest + t_i

                if val_levar > val_cima:
                    dp[i][w] = val_levar
                    decisao_txt = f"{Cor.VERDE}LEVAR O PEDIDO{Cor.RESET} (ganho maior: {val_levar}m > {val_cima}m)"
                else:
                    dp[i][w] = val_cima
                    decisao_txt = f"{Cor.AMARELO}DEIXAR O PEDIDO{Cor.RESET} (manter anterior é melhor ou igual: {val_cima}m >= {val_levar}m)"

                ramo = "CASO 2 (CABE NA BAG)"
                condicao = f"p_{i} ({p_i} pz) <= w ({w} pz)"
                formula_txt = f"max( Cima={val_cima}m, Levar={val_rest}+{t_i}={val_levar}m ) = {dp[i][w]} min"

            if passo_a_passo:
                print(f"{Cor.CIANO}{'─' * 70}{Cor.RESET}")
                print(f"{Cor.NEGRITO}🔍 CÉLULA DP[{i}][{w}] - Pedido #{i} ({t_i}m, {p_i}pz) | Mochila: {w} pizzas{Cor.RESET}")
                print(f"• {Cor.MAGENTA}Ramo Ativo da Recorrência:{Cor.RESET} {Cor.NEGRITO}{ramo}{Cor.RESET}")
                print(f"• {Cor.BRANCO}Condição:{Cor.RESET} {condicao}")
                print(f"• {Cor.AMARELO}Substituição Numérica:{Cor.RESET} {formula_txt}")
                print(f"• {Cor.VERDE}Decisão Local:{Cor.RESET} {decisao_txt}")
                print(f"{Cor.CIANO}{'─' * 70}{Cor.RESET}")
                tecla = input("Pressione [Enter] para a próxima célula (ou digite 't' para concluir todas): ").strip().lower()
                if tecla == 't':
                    passo_a_passo = False

    t_fim = time.perf_counter()
    tempo_execucao_ms = (t_fim - t_inicio) * 1000

    return dp, tempo_execucao_ms


def executar_backtracking_passo_a_passo(dp, pedidos, P):
    """
    Executa a auditoria de reconstrução da solução ótima (Backtracking)
    de trás para frente (de N até 1), permitindo avanço passo a passo interativo.
    """
    N = len(pedidos)
    print(f"\n{Cor.MAGENTA}{'═' * 78}{Cor.RESET}")
    print(f"{Cor.NEGRITO}{Cor.BRANCO} 🔄 FASE DE RECONSTRUÇÃO DA SOLUÇÃO ÓTIMA (BACKTRACKING INTERATIVO){Cor.RESET}")
    print(f" {Cor.DIM}Partindo da célula ótima global DP[{N}][{P}] = {dp[N][P]} min até o Pedido #1{Cor.RESET}")
    print(f"{Cor.MAGENTA}{'═' * 78}{Cor.RESET}\n")

    print(f"{Cor.NEGRITO}Regra de Decisão do Backtracking:{Cor.RESET}")
    print(f"  • Se {Cor.VERDE}DP[i][w] != DP[i-1][w]{Cor.RESET} ⟹ {Cor.VERDE}O Pedido #i FOI LEVADO NA BAG!{Cor.RESET} (subtrai p_i pizzas de w)")
    print(f"  • Se {Cor.AMARELO}DP[i][w] == DP[i-1][w]{Cor.RESET} ⟹ {Cor.AMARELO}O Pedido #i FOI DESCARTADO!{Cor.RESET} (mantém w inalterado)\n")

    w_atual = P
    pedidos_escolhidos = []
    passo_num = 1
    modo_continuo = False

    for i in range(N, 0, -1):
        ped = pedidos[i - 1]
        cur_v = dp[i][w_atual]
        cima_v = dp[i - 1][w_atual]
        foi_levado = (cur_v != cima_v)

        print(f"{Cor.MAGENTA}{'─' * 75}{Cor.RESET}")
        print(f"{Cor.NEGRITO}PASSO #{passo_num} DE {N} | Auditando Pedido #{ped['id']} ({ped['tempo']}m, {ped['pizzas']} pizzas) | Bag Atual: {w_atual} pz{Cor.RESET}")
        print(f"{Cor.MAGENTA}{'─' * 75}{Cor.RESET}")

        if foi_levado:
            w_depois = w_atual - ped['pizzas']
            ganho_rest = dp[i - 1][w_depois]
            pedidos_escolhidos.append(ped)

            print(f"• {Cor.NEGRITO}Comparação:{Cor.RESET} DP[{i}][{w_atual}] ({cur_v}m) {Cor.VERDE}≠{Cor.RESET} DP[{i-1}][{w_atual}] ({cima_v}m) ⟹ {Cor.VERDE}{Cor.NEGRITO}VALORES DIFERENTES!{Cor.RESET}")
            print(f"• {Cor.NEGRITO}Decisão:{Cor.RESET}    {Cor.BG_VERDE}{Cor.BRANCO} ✅ O PEDIDO #{ped['id']} FOI OBRIGATORIAMENTE LEVADO! {Cor.RESET}")
            print(f"\n• {Cor.AMARELO}{Cor.NEGRITO}POR QUE ESCOLHEU ESTE PEDIDO?{Cor.RESET}")
            print(f"  Sem o Pedido #{ped['id']}, o melhor tempo com capacidade {w_atual} pizzas era apenas {cima_v} min (DP[{i-1}][{w_atual}]).")
            print(f"  Ao levar o Pedido #{ped['id']} ({ped['tempo']} min, {ped['pizzas']} pizzas), somamos o seu tempo com a melhor")
            print(f"  solução para o espaço restante ({w_depois} pizzas ⟹ DP[{i-1}][{w_depois}] = {ganho_rest} min):")
            print(f"  {Cor.VERDE}{ganho_rest} min + {ped['tempo']} min = {cur_v} min{Cor.RESET}, superando com folga os {cima_v} min anteriores!")
            print(f"\n• {Cor.NEGRITO}Atualização da Mochila:{Cor.RESET} Subtrai {ped['pizzas']} pizzas:")
            print(f"  {Cor.CIANO}w = {w_atual} - {ped['pizzas']} = {w_depois} pizzas restantes{Cor.RESET} ⟹ Sobe para Pedido #{i-1} com w={w_depois}")

            w_atual = w_depois
        else:
            w_depois = w_atual
            print(f"• {Cor.NEGRITO}Comparação:{Cor.RESET} DP[{i}][{w_atual}] ({cur_v}m) {Cor.AMARELO}=={Cor.RESET} DP[{i-1}][{w_atual}] ({cima_v}m) ⟹ {Cor.AMARELO}{Cor.NEGRITO}VALORES IDÊNTICOS!{Cor.RESET}")
            print(f"• {Cor.NEGRITO}Decisão:{Cor.RESET}    {Cor.VERMELHO}❌ O PEDIDO #{ped['id']} FOI DESCARTADO!{Cor.RESET}")
            print(f"\n• {Cor.AMARELO}{Cor.NEGRITO}POR QUE DESCARTOU ESTE PEDIDO?{Cor.RESET}")
            print(f"  Incluir o Pedido #{ped['id']} ({ped['tempo']}m, {ped['pizzas']} pizzas) não superaria os {cima_v} min já assegurados")
            print(f"  pelos pedidos anteriores para essa capacidade de {w_atual} pizzas. O ganho não compensaria a perda de espaço.")
            print(f"\n• {Cor.NEGRITO}Atualização da Mochila:{Cor.RESET} Capacidade mantida inalterada:")
            print(f"  {Cor.CIANO}w = {w_atual} pizzas{Cor.RESET} ⟹ Sobe para Pedido #{i-1} mantendo w={w_atual}")

        print(f"{Cor.MAGENTA}{'─' * 75}{Cor.RESET}")
        passo_num += 1

        if not modo_continuo and i > 1:
            tecla = input(f"\n{Cor.NEGRITO}Pressione [Enter] para auditar o próximo pedido (ou digite 't' para concluir): {Cor.RESET}").strip().lower()
            if tecla == 't':
                modo_continuo = True
            print()

    # Inverte para ordem cronológica
    pedidos_escolhidos.reverse()
    return pedidos_escolhidos


def exibir_decisao_final(dp, pedidos, P, escolhidos, tempo_execucao_ms):
    """Exibe o painel de resultados e métricas finais formatado com destaque visual."""
    N = len(pedidos)
    tempo_otimo = dp[N][P]
    pizzas_usadas = sum(p['pizzas'] for p in escolhidos)
    vagas_sobrando = P - pizzas_usadas
    pct_ocupacao = (pizzas_usadas / P) * 100
    ids_escolhidos = [p['id'] for p in escolhidos]
    tempo_bruto_total = sum(p['tempo'] for p in pedidos)

    print(f"\n{Cor.VERDE}{'═' * 78}{Cor.RESET}")
    print(f"{Cor.NEGRITO}{Cor.BRANCO} 🏆 DECISÃO FINAL: PLANO DE ENTREGA OTIMIZADO PARA JOSÉ (MOTOBOY){Cor.RESET}")
    print(f"{Cor.VERDE}{'═' * 78}{Cor.RESET}")

    print(f"\n {Cor.NEGRITO}MÉTRICAS PRINCIPAIS:{Cor.RESET}")
    print(f" • {Cor.VERDE}{Cor.NEGRITO}Tempo Total Máximo de Trabalho:{Cor.RESET} {Cor.BRANCO}{Cor.BG_VERDE} {tempo_otimo} minutos {Cor.RESET}")
    print(f" • {Cor.CIANO}{Cor.NEGRITO}Ocupação da Mochila (Bag):{Cor.RESET}      {pizzas_usadas} de {P} pizzas ({pct_ocupacao:.1f}% da capacidade preenchida)")
    print(f" • {Cor.AMARELO}Espaço Ocioso restante:{Cor.RESET}          {vagas_sobrando} pizza(s) sobrando na bolsa")
    print(f" • {Cor.MAGENTA}Pedidos Selecionados:{Cor.RESET}            {len(escolhidos)} de {N} pedidos totais")
    print(f" • {Cor.DIM}Tempo de Processamento da DP:{Cor.RESET}    {tempo_execucao_ms:.4f} milissegundos")

    print(f"\n{Cor.CIANO}{'─' * 78}{Cor.RESET}")
    print(f"{Cor.NEGRITO}📋 STATUS DETALHADO DE CADA PEDIDO DA PIZZARIA:{Cor.RESET}")
    print(f"{Cor.CIANO}{'─' * 78}{Cor.RESET}")

    for p in pedidos:
        if p['id'] in ids_escolhidos:
            tag = f"{Cor.BG_VERDE}{Cor.BRANCO} ✅ LEVAR NA MOTO {Cor.RESET}"
            detalhe = f"{Cor.VERDE}Pedido #{p['id']}: Demora {p['tempo']:>2} min | Ocupa {p['pizzas']:>2} pizzas{Cor.RESET}"
        else:
            tag = f"{Cor.BG_ESCURO}{Cor.BRANCO} ❌ DEIXAR (OUTRO) {Cor.RESET}"
            detalhe = f"{Cor.DIM}Pedido #{p['id']}: Demora {p['tempo']:>2} min | Ocupa {p['pizzas']:>2} pizzas{Cor.RESET}"

        print(f" {tag} ➔ {detalhe}")

    print(f"{Cor.CIANO}{'─' * 78}{Cor.RESET}")

    print(f"\n{Cor.NEGRITO}💡 FORMATO OFICIAL BEECROWD 1286:{Cor.RESET}")
    print(f"  {Cor.VERDE}{tempo_otimo} min.{Cor.RESET}")
    print(f"{Cor.VERDE}{'═' * 78}{Cor.RESET}\n")


def loop_principal():
    """Controla o ciclo de vida interativo do simulador."""
    while True:
        imprimir_banner()
        P, pedidos = menu_configuracao_inicial()
        exibir_tabela_pedidos(pedidos, P)

        # Pergunta como o usuário deseja ver a construção da matriz
        print(f"{Cor.NEGRITO}📐 ESCOLHA O MODO DE CONSTRUÇÃO DA MATRIZ DP:{Cor.RESET}")
        print(f"  {Cor.VERDE}[1]{Cor.RESET} Calcular Imediatamente (Rápido - Exibe a Matriz Completa Pronta)")
        print(f"  {Cor.AMARELO}[2]{Cor.RESET} Demonstração Didática Célula a Célula (Com fórmula de recorrência)")

        modo_matriz = input(f"\nSelecione o modo [1 ou 2] (Padrão: 1): ").strip()
        passo_a_passo_matriz = (modo_matriz == "2")

        dp, tempo_ms = construir_matriz_dp(pedidos, P, passo_a_passo=passo_a_passo_matriz)
        imprimir_matriz_formatada(dp, pedidos, P)

        # Execução do Backtracking interativo
        print(f"{Cor.NEGRITO}Deseja acompanhar a reconstrução da decisão (Backtracking) passo a passo?{Cor.RESET}")
        bt_opcao = input("Pressione [Enter] para SIM (ou 'n' para ir direto ao resultado final): ").strip().lower()

        if bt_opcao != 'n':
            escolhidos = executar_backtracking_passo_a_passo(dp, pedidos, P)
        else:
            # Backtracking silencioso
            w_atual = P
            escolhidos = []
            for i in range(len(pedidos), 0, -1):
                if dp[i][w_atual] != dp[i - 1][w_atual]:
                    escolhidos.append(pedidos[i - 1])
                    w_atual -= pedidos[i - 1]['pizzas']
            escolhidos.reverse()

        exibir_decisao_final(dp, pedidos, P, escolhidos, tempo_ms)

        novo_teste = input(f"\n{Cor.NEGRITO}Deseja realizar uma nova simulação? (s/n): {Cor.RESET}").strip().lower()
        if novo_teste != 's':
            print(f"\n{Cor.AMARELO}Simulador finalizado. Excelente apresentação na UFRPE!{Cor.RESET}\n")
            break


if __name__ == "__main__":
    try:
        loop_principal()
    except KeyboardInterrupt:
        print(f"\n\n{Cor.AMARELO}Execução interrompida pelo usuário. Até logo!{Cor.RESET}\n")
