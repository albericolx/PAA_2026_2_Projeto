"""
Script para Gerar o Documento Editável Word (.docx) com o Fluxo e Diagrama de Blocos
da Implementação Otimizada em Espaço O(P) para o Problema do Motoboy (BeeCrowd 1286).
Autor: José Albérico Rocha da Silva
UFRPE 2026.2 - Projeto e Análise de Algoritmos (PAA) | Profª Jeane Melo
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    """Define a cor de fundo de uma célula de tabela em formato hexadecimal."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Define os espaçamentos internos da célula."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def criar_documento_fluxo(caminho_docx):
    doc = docx.Document()

    # Margens ABNT/SBC padrão: 3cm superior/esquerda, 2cm inferior/direita
    for s in doc.sections:
        s.top_margin = Inches(3.0 / 2.54)
        s.bottom_margin = Inches(2.0 / 2.54)
        s.left_margin = Inches(3.0 / 2.54)
        s.right_margin = Inches(2.0 / 2.54)

    # Cores corporativas / acadêmicas
    cor_azul = RGBColor(30, 58, 138)       # #1e3a8a
    cor_verde = RGBColor(6, 95, 70)        # #065f46
    cor_vermelho = RGBColor(185, 28, 28)   # #b91c1c
    cor_cinza = RGBColor(71, 85, 105)      # #475569

    # 1. TÍTULO PRINCIPAL
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(4)
    run_t = p_title.add_run("DIAGRAMA DE BLOCOS E FLUXO DE TOMADA DE DECISÃO:\nIMPLEMENTAÇÃO OTIMIZADA EM ESPAÇO O(P)")
    run_t.font.name = "Arial"
    run_t.font.size = Pt(15)
    run_t.font.bold = True
    run_t.font.color.rgb = cor_azul

    # Subtítulo acadêmico
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(16)
    run_sub = p_sub.add_run("Projeto e Análise de Algoritmos (PAA) — UFRPE 2026.2\nDocente: Profª. Drª. Jeane Melo | Discente: José Albérico Rocha da Silva (autor)\nTema 6: BeeCrowd 1286 — Motoboy (Mochila Binária 0-1)")
    run_sub.font.name = "Times New Roman"
    run_sub.font.size = Pt(10.5)
    run_sub.font.italic = True
    run_sub.font.color.rgb = cor_cinza

    # Função auxiliar para cabeçalhos de seção
    def add_h1(texto):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(texto)
        r.font.name = "Arial"
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = cor_azul
        return p

    def add_h2(texto):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(texto)
        r.font.name = "Arial"
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = cor_verde
        return p

    def add_p(texto, indent=True, bold_prefix=""):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if indent:
            p.paragraph_format.first_line_indent = Inches(1.27 / 2.54)
        p.paragraph_format.space_after = Pt(4)
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.font.name = "Times New Roman"
            rb.font.size = Pt(10.5)
            rb.font.bold = True
        r = p.add_run(texto)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10.5)
        return p

    # -------------------------------------------------------------------------
    # SEÇÃO 1: MOTIVAÇÃO E O CÓDIGO FONTE ANALISADO
    # -------------------------------------------------------------------------
    add_h1("1. O Algoritmo Analisado: Compactação de Matriz 2D para Vetor 1D")
    add_p("Na formulação padrão da Programação Dinâmica para o Problema da Mochila 0-1, utiliza-se uma matriz bidimensional DP[N+1][P+1]. Contudo, uma análise matemática cuidadosa da equação de Bellman revela que, para preencher qualquer célula da linha atual i, o algoritmo consulta exclusivamente a linha imediatamente superior i-1:", bold_prefix="Fundamento Teórico: ")

    p_eq = doc.add_paragraph()
    p_eq.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_eq.paragraph_format.space_before = Pt(4)
    p_eq.paragraph_format.space_after = Pt(6)
    r_eq = p_eq.add_run("DP[i][w] = max( DP[i-1][w],  DP[i-1][w - p_i] + t_i )")
    r_eq.font.name = "Courier New"
    r_eq.font.size = Pt(10.5)
    r_eq.font.bold = True

    add_p("Como nenhuma célula das linhas anteriores (i-2, i-3, ..., 0) volta a ser consultada, é plenamente viável descartar a matriz 2D e reaproveitar um único vetor unidimensional de tamanho P+1. O código de produção implementado para o BeeCrowd 1286 sintetiza essa técnica:")

    # Caixa de Código
    tbl_code = doc.add_table(rows=1, cols=1)
    tbl_code.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_code = tbl_code.rows[0].cells[0]
    set_cell_background(c_code, "0F172A")  # dark blue/slate
    set_cell_margins(c_code, 120, 120, 180, 180)
    
    code_text = (
        "def resolver_caso(n, max_pizzas, pedidos):\n"
        "    # 1. Aloca vetor unidimensional compacto inicializado em zero\n"
        "    dp = [0] * (max_pizzas + 1)\n\n"
        "    # 2. Processa cada pedido sequencialmente (Loop Externo)\n"
        "    for tempo, pizzas in pedidos:\n\n"
        "        # 3. Varredura DECRESCENTE da capacidade (Loop Interno Crítico)\n"
        "        for w in range(max_pizzas, pizzas - 1, -1):\n\n"
        "            # 4. Decisão de Bellman In-Place: Levar vs Manter\n"
        "            if dp[w - pizzas] + tempo > dp[w]:\n"
        "                dp[w] = dp[w - pizzas] + tempo\n\n"
        "    # 5. O valor ótimo global reside na última posição\n"
        "    return dp[max_pizzas]"
    )
    p_c = c_code.paragraphs[0]
    r_c = p_c.add_run(code_text)
    r_c.font.name = "Courier New"
    r_c.font.size = Pt(9)
    r_c.font.color.rgb = RGBColor(226, 232, 240)

    # -------------------------------------------------------------------------
    # SEÇÃO 2: DIAGRAMA DE BLOCOS DO FLUXO DO ALGORITMO
    # -------------------------------------------------------------------------
    add_h1("2. Diagrama de Blocos do Fluxo de Execução")
    add_p("O fluxograma a seguir detalha cada etapa do algoritmo, desde a inicialização dos parâmetros até o retorno do tempo ótimo, evidenciando as estruturas de repetição aninhadas e a bifurcação de decisão:", indent=False)

    # Tabela com as etapas do Fluxograma formatada como Blocos Visuais
    etapas_fluxo = [
        ("BLOCO 1: INÍCIO E ENTRADA DE DADOS",
         "• Recebe N (quantidade de pedidos) e P (capacidade máxima de pizzas).\n• Recebe a listagem de pedidos com seus pares (tempo_i, pizzas_i).\n• Se N == 0: encerra o processamento (critério de parada oficial BeeCrowd).",
         "1E3A8A", "F8FAFC"),
        
        ("BLOCO 2: INICIALIZAÇÃO DO VETOR 1D",
         "• Cria o vetor unidimensional dp de dimensão (P + 1) com zeros:\n  dp = [0, 0, 0, ..., 0]  (onde o índice representa a capacidade w de 0 a P).\n• Consumo de Memória: estritamente O(P) palavras inteiras (ex.: 31 inteiros para P=30).",
         "0284C7", "F8FAFC"),

        ("BLOCO 3: LAÇO EXTERNO — SELEÇÃO DO PEDIDO (i = 1 até N)",
         "• Para cada pedido (tempo, pizzas) presente na lista:\n• Extrai o benefício t_i e o custo de capacidade p_i a serem avaliados nesta rodada.",
         "0D9488", "F8FAFC"),

        ("BLOCO 4: LAÇO INTERNO — VARREDURA DECRESCENTE (w = P descendo até pizzas)",
         "• Inicializa a capacidade w na capacidade máxima da mochila P.\n• Condição de continuidade do laço: enquanto w >= pizzas.\n• Passo de decremento: w = w - 1 a cada iteração.\n★ Ponto Crítico Didático: A iteração DEVE ser decrescente (da direita para a esquerda)!",
         "D97706", "FFFBEB"),

        ("BLOCO 5: NÓ DE DECISÃO DE BELLMAN IN-PLACE",
         "• Avalia a expressão condicional booleana:\n  if dp[w - pizzas] + tempo > dp[w]:\n\n"
         "  [RAMO SIM - VENCE LEVAR O PEDIDO]:\n"
         "  • O valor com o novo pedido supera o valor anterior.\n"
         "  • Atualização in-place: dp[w] = dp[w - pizzas] + tempo.\n\n"
         "  [RAMO NÃO - VENCE MANTER O ANTERIOR]:\n"
         "  • Manter a combinação sem o pedido atual gera resultado melhor ou igual.\n"
         "  • Nenhuma alteração é feita: dp[w] permanece inalterado.",
         "4F46E5", "EEF2FF"),

        ("BLOCO 6: CONTROLE DO LAÇO INTERNO (w)",
         "• w atingiu o valor (pizzas - 1)?\n"
         "  • Se NÃO: repete o Bloco 5 para o próximo w (decrementa).\n"
         "  • Se SIM: concluiu a varredura para este pedido; avança ao Bloco 7.",
         "64748B", "F8FAFC"),

        ("BLOCO 7: CONTROLE DO LAÇO EXTERNO (PEDIDOS)",
         "• Todos os N pedidos foram processados?\n"
         "  • Se NÃO: avança para o próximo pedido da lista (volta ao Bloco 3).\n"
         "  • Se SIM: todos os subproblemas foram resolvidos com sucesso.",
         "64748B", "F8FAFC"),

        ("BLOCO 8: RETORNO DA SOLUÇÃO E FIM",
         "• O resultado ótimo global reside na última célula do vetor: dp[P].\n• Retorna dp[P] (tempo máximo em minutos).\n• Complexidade Temporal: O(N · P) | Complexidade Espacial: O(P).",
         "059669", "ECFDF5")
    ]

    tbl_fluxo = doc.add_table(rows=len(etapas_fluxo), cols=1)
    tbl_fluxo.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_fluxo.autofit = False

    for idx, (titulo_bloco, desc_bloco, cor_header_hex, cor_bg_hex) in enumerate(etapas_fluxo):
        cell = tbl_fluxo.rows[idx].cells[0]
        set_cell_background(cell, cor_bg_hex)
        set_cell_margins(cell, 80, 80, 140, 140)

        p_b = cell.paragraphs[0]
        p_b.paragraph_format.space_before = Pt(2)
        p_b.paragraph_format.space_after = Pt(2)
        r_btit = p_b.add_run(f"▼ {titulo_bloco}\n")
        r_btit.font.name = "Arial"
        r_btit.font.size = Pt(10)
        r_btit.font.bold = True
        
        # Converte hex para RGBColor
        r_int = int(cor_header_hex[0:2], 16)
        g_int = int(cor_header_hex[2:4], 16)
        b_int = int(cor_header_hex[4:6], 16)
        r_btit.font.color.rgb = RGBColor(r_int, g_int, b_int)

        r_bdesc = p_b.add_run(desc_bloco)
        r_bdesc.font.name = "Times New Roman"
        r_bdesc.font.size = Pt(9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # -------------------------------------------------------------------------
    # SEÇÃO 3: POR QUE A ITERAÇÃO DEVE SER DECRESCENTE? (O PONTO CHAVE)
    # -------------------------------------------------------------------------
    add_h1("3. O Mistério Revelado: Por que o Laço de Capacidades DEVE ser Decrescente?")
    add_p("Esta é a pergunta mais frequente em bancas e avaliações de algoritmos: 'Por que o laço interno de w percorre de P até pizzas (decrescente), em vez de percorrer de pizzas até P (crescente)?'.", bold_prefix="O Ponto Central da Explicação: ")
    add_p("A resposta reside na preservação estrita da propriedade binária (0-1), impedindo que um mesmo pedido seja computado duas ou mais vezes na mesma viagem da motocicleta.")

    add_h2("3.1 O Erro Fatal se Fosse Crescente (Varredura Esquerda ➔ Direita):")
    add_p("Suponha que a moto tenha capacidade P = 5 pizzas e a pizzaria receba um único Pedido #1 com tempo = 20 min e pizzas = 2. O vetor começa zerado: dp = [0, 0, 0, 0, 0, 0].", indent=False)
    add_p("Se percorrermos de forma CRESCENTE (w = 2, 3, 4, 5):", indent=False)
    add_p("1. Em w = 2: dp[2] = max(dp[2], dp[2-2] + 20) = max(0, dp[0] + 20) = 20.\n"
          "2. Em w = 4: dp[4] = max(dp[4], dp[4-2] + 20) = max(0, dp[2] + 20) = 20 + 20 = 40!  ❌ ERRO GRAVE!\n"
          "O algoritmo usou o Pedido #1 duas vezes, como se José tivesse levado 4 pizzas do mesmo pedido! Isso violaria a restrição binária 0-1 e transformaria o problema em uma Mochila Ilimitada (Unbounded Knapsack).", indent=True)

    add_h2("3.2 A Precisão Matemática da Varredura DECRESCENTE (Direita ➔ Esquerda):")
    add_p("Ao iterar de forma DECRESCENTE (w = 5 descendo até 2):", indent=False)
    add_p("1. Em w = 5: consulta dp[5-2] = dp[3]. Como dp[3] ainda não foi modificado nesta rodada, ele guarda exatamente o valor do estágio anterior (i-1), que é 0. Logo, dp[5] = 20.\n"
          "2. Em w = 4: consulta dp[4-2] = dp[2], que ainda guarda o valor do estágio anterior (0). Logo, dp[4] = 20.\n"
          "3. Em w = 2: consulta dp[2-2] = dp[0] = 0. Logo, dp[2] = 20.\n"
          "Resultado final do vetor: dp = [0, 0, 20, 20, 20, 20]. Cada pedido é utilizado no máximo UMA ÚNICA VEZ! A propriedade da Mochila 0-1 é preservada com 100% de rigor matemático em uma única dimensão de memória.", indent=True)

    # -------------------------------------------------------------------------
    # SEÇÃO 4: TABELA COMPARATIVA DE ESTADOS DO VETOR 1D (CASO N=4, P=10)
    # -------------------------------------------------------------------------
    add_h1("4. Simulação Numérica do Vetor 1D: Caso Oficial BeeCrowd (N=4, P=10)")
    add_p("A tabela abaixo demonstra a evolução do vetor unidimensional dp[0..10] após a conclusão de cada iteração do laço externo:", indent=False)

    tbl_sim = doc.add_table(rows=6, cols=12)
    tbl_sim.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_sim.autofit = False

    dados_sim = [
        ['Estágio / Capacidade', 'w=0', 'w=1', 'w=2', 'w=3', 'w=4', 'w=5', 'w=6', 'w=7', 'w=8', 'w=9', 'w=10'],
        ['Inicial (Zeros)', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['Após P1 (20m, 5pz)', '0', '0', '0', '0', '0', '20', '20', '20', '20', '20', '20'],
        ['Após P2 (70m, 7pz)', '0', '0', '0', '0', '0', '20', '20', '70', '70', '70', '70'],
        ['Após P3 (15m, 2pz)', '0', '0', '15', '15', '15', '20', '20', '70', '70', '85', '85'],
        ['Após P4 (25m, 3pz)', '0', '0', '15', '25', '25', '40', '40', '70', '70', '85', '95']
    ]

    for r_i, row_v in enumerate(dados_sim):
        row = tbl_sim.rows[r_i]
        for c_i, val in enumerate(row_v):
            cell = row.cells[c_i]
            cell.text = val
            p_ce = cell.paragraphs[0]
            p_ce.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_ce = p_ce.runs[0]
            r_ce.font.name = "Times New Roman"
            r_ce.font.size = Pt(8.5)
            if r_i == 0 or c_i == 0:
                r_ce.font.bold = True
                set_cell_background(cell, "F1F5F9")
            if r_i == 5 and c_i == 11:
                r_ce.font.bold = True
                r_ce.font.color.rgb = RGBColor(6, 95, 70)
                set_cell_background(cell, "D1FAE5")

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # -------------------------------------------------------------------------
    # SEÇÃO 5: COMPARAÇÃO DE COMPLEXIDADE E GANHOS DE ENGENHARIA
    # -------------------------------------------------------------------------
    add_h1("5. Comparativo de Complexidade e Benefícios para Apresentação")

    tbl_comp = doc.add_table(rows=4, cols=3)
    tbl_comp.alignment = WD_TABLE_ALIGNMENT.CENTER

    headers_comp = ["Dimensão de Análise", "Versão Didática (Matriz 2D)", "Versão Produção Otimizada (Vetor 1D)"]
    for c_idx, h in enumerate(headers_comp):
        cell = tbl_comp.rows[0].cells[c_idx]
        cell.text = h
        set_cell_background(cell, "1E3A8A")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.runs[0]
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    dados_comp = [
        ("Complexidade de Memória (Espaço)", "O(N · P) — Armazena (N+1) × (P+1) inteiros", "O(P) — Armazena estritamente (P+1) inteiros"),
        ("Alocação na Instância Oficial (N=20, P=30)", "651 posições inteiras em matriz", "31 posições inteiras em vetor (Economia de 95,2%)"),
        ("Eficiência de Cache e CPU", "Múltiplos saltos de ponteiros em memória para matriz de listas", "Localidade espacial contígua, aproveitando 100% da cache L1/L2")
    ]

    for r_idx, (c1, c2, c3) in enumerate(dados_comp, 1):
        row = tbl_comp.rows[r_idx]
        for c_idx, val in enumerate([c1, c2, c3]):
            cell = row.cells[c_idx]
            cell.text = val
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx == 0 else WD_ALIGN_PARAGRAPH.JUSTIFY
            r = p.runs[0]
            r.font.name = "Times New Roman"
            r.font.size = Pt(9)
            if r_idx % 2 == 1:
                set_cell_background(cell, "F8FAFC")

    doc.add_paragraph().paragraph_format.space_before = Pt(12)

    # Conclusão / Roteiro de Fala
    add_h1("6. Roteiro Sugerido de Explicação na Apresentação Oral")
    add_p("Para brilhar perante a professora Jeane Melo durante a explicação deste slide:", bold_prefix="Dica Didática para a Defesa: ")
    add_p("1. 'Professora, na versão didática utilizamos a matriz 2D para permitir o Backtracking visual. Porém, para a submissão de alta performance no BeeCrowd, compactamos toda a matriz em um único vetor 1D de tamanho P+1.'\n"
          "2. 'A razão matemática é que para preencher a linha atual, só precisamos de células da linha anterior. Então podemos sobrescrever o mesmo vetor.'\n"
          "3. 'O detalhe mais elegante do algoritmo é que o laço da mochila precisa rodar de trás para frente (decrescente). Se rodasse para frente, um pedido seria somado múltiplas vezes como se fosse infinito. Ao rodar de trás para frente, garantimos que cada pedido seja usado no máximo uma única vez, preservando a propriedade da Mochila 0-1.'", indent=True)

    doc.save(caminho_docx)
    print(f"Documento Word editável gerado com sucesso em: {caminho_docx}")

if __name__ == "__main__":
    destino = r"C:\Users\Windows 10\OneDrive\Documentos\UFRPE\2026.2\Projeto e Análise de Algorítimos\Projeto VA_02\Motoboy\docs\fluxo_otimizacao_espacial_1d.docx"
    criar_documento_fluxo(destino)
