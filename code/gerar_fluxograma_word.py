"""
Gera o documento Word exclusivo contendo o FLUXOGRAMA DE DECISÃO da otimização O(P).
Inclui o Diagrama Gráfico de Alta Resolução (300 DPI) perfeitamente espaçado e sem sobreposições,
além dos Blocos Editáveis em formato de tabela Word.
Autor: José Albérico Rocha da Silva (autor)
UFRPE 2026.2 - Projeto e Análise de Algoritmos | Profª Jeane Melo
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def desenhar_fluxograma_imagem(caminho_imagem):
    """
    Desenha o fluxograma gráfico profissional em alta resolução (300 DPI),
    com layout vertical expandido (altura 160) garantindo espaçamento perfeito
    e zero sobreposição entre os blocos finais.
    """
    fig, ax = plt.subplots(figsize=(11, 16.5), dpi=300)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 160)
    ax.axis('off')

    def box(x, y, w, h, text, bg, border, fontsize=9.5, bold=True):
        rect = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle="round,pad=1.2,rounding_size=2.5",
            facecolor=bg, edgecolor=border, linewidth=2, zorder=3
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', color='white',
                fontsize=fontsize, fontweight='bold' if bold else 'normal',
                fontfamily='sans-serif', zorder=4)

    def diamond(x, y, w, h, text, bg, border, fontsize=9):
        pts = [[x, y + h/2], [x + w/2, y], [x, y - h/2], [x - w/2, y]]
        poly = patches.Polygon(pts, facecolor=bg, edgecolor=border, linewidth=2.5, zorder=3)
        ax.add_patch(poly)
        ax.text(x, y, text, ha='center', va='center', color='white',
                fontsize=fontsize, fontweight='bold', fontfamily='sans-serif', zorder=4)

    def arrow(x1, y1, x2, y2, label="", label_color="#38bdf8", offset_x=3, offset_y=0):
        ax.annotate(
            '', xy=(x2, y2), xytext=(x1, y1),
            arrowprops=dict(facecolor='#38bdf8', edgecolor='#38bdf8', width=2, headwidth=8, headlength=8),
            zorder=2
        )
        if label:
            ax.text((x1 + x2)/2 + offset_x, (y1 + y2)/2 + offset_y, label,
                    color=label_color, fontsize=8.5, fontweight='bold', fontfamily='sans-serif', zorder=5)

    def line(x1, y1, x2, y2, color='#38bdf8', width=2):
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=width, zorder=2)

    # -------------------------------------------------------------
    # 1. INÍCIO
    # -------------------------------------------------------------
    box(50, 151, 62, 6.5, "INICIO: resolver_caso(n, max_pizzas, pedidos)", "#0284c7", "#38bdf8", fontsize=10)
    arrow(50, 147.5, 50, 141)

    # -------------------------------------------------------------
    # 2. ALOCAÇÃO DO VETOR 1D
    # -------------------------------------------------------------
    box(50, 137, 66, 7.5, "1. Alocar Vetor 1D em Memoria:\ndp = [0] * (max_pizzas + 1)  [Espaco O(P)]", "#1e293b", "#64748b", fontsize=9.5)
    arrow(50, 133, 50, 127)

    # -------------------------------------------------------------
    # 3. LAÇO EXTERNO (PEDIDOS)
    # -------------------------------------------------------------
    diamond(50, 120, 54, 13, "2. LACO EXTERNO:\nHa mais pedidos na lista?", "#1e3a8a", "#60a5fa", fontsize=9.5)

    # Ramo SIM (Processar próximo pedido)
    arrow(50, 113.5, 50, 107.5, "SIM", "#34d399", offset_x=3)

    # Ramo NÃO (Fim de todos os pedidos -> Canal externo direito para o retorno final)
    arrow(77, 120, 90, 120, "NAO", "#94a3b8", offset_y=2.5, offset_x=-1)
    line(90, 120, 90, 25, color='#94a3b8')
    arrow(90, 25, 74, 25, label_color='#94a3b8')

    # -------------------------------------------------------------
    # 4. EXTRAÇÃO DO PEDIDO ATUAL E INÍCIO DA VARREDURA
    # -------------------------------------------------------------
    box(50, 103, 68, 7.5, "3. Pedido Atual (tempo, pizzas):\nInicializa w = max_pizzas (Varredura Reversa)", "#0f766e", "#2dd4bf", fontsize=9.5)
    arrow(50, 99, 50, 93.5)

    # -------------------------------------------------------------
    # 5. LAÇO INTERNO: VERIFICAÇÃO DE CAPACIDADE
    # -------------------------------------------------------------
    diamond(50, 87, 48, 12, "w >= pizzas?\n(Cabe na bag restante?)", "#7c2d12", "#fb923c", fontsize=9.5)

    # Ramo SIM (Cabe na mochila -> Analisa decisão de Bellman)
    arrow(50, 81, 50, 75, "SIM", "#34d399", offset_x=3)

    # Ramo NÃO (w < pizzas -> Fim da varredura deste pedido -> Canal esquerdo externo para próximo pedido)
    arrow(26, 87, 10, 87, "NAO", "#f87171", offset_y=2.5, offset_x=-1)
    line(10, 87, 10, 120, color='#f87171')
    arrow(10, 120, 23, 120)

    # -------------------------------------------------------------
    # 6. NÓ DE DECISÃO DE BELLMAN
    # -------------------------------------------------------------
    diamond(50, 68, 56, 12.5, "4. DECISAO DE BELLMAN:\ndp[w - pizzas] + tempo > dp[w]?", "#4338ca", "#a5b4fc", fontsize=9)

    # Ramo SIM (Vence Levar o Pedido)
    arrow(22, 68, 22, 58, "SIM (Levar)", "#34d399", offset_x=-14, offset_y=-5)
    box(22, 53, 38, 7.5, "[SIM] dp[w] = dp[w - pizzas] + tempo\n(Ganha o tempo deste pedido)", "#064e3b", "#34d399", fontsize=8.5)

    # Ramo NÃO (Vence Manter Decisão Anterior)
    arrow(78, 68, 78, 58, "NAO (Manter)", "#f87171", offset_x=2, offset_y=-5)
    box(78, 53, 38, 7.5, "[NAO] dp[w] permanece inalterado\n(Solucao previa ja e melhor)", "#450a0a", "#f87171", fontsize=8.5)

    # Confluência para o decremento de w
    arrow(22, 49, 39, 43)
    arrow(78, 49, 61, 43)

    # -------------------------------------------------------------
    # 7. BLOCO DE DECREMENTO (w = w - 1)
    # -------------------------------------------------------------
    box(50, 40, 44, 6, "Decrementa: w = w - 1", "#334155", "#94a3b8", fontsize=9)

    # Retorno do laço interno (Canal intermediário esquerdo x=18)
    line(28, 40, 18, 40, color='#38bdf8')
    line(18, 40, 18, 87, color='#38bdf8')
    arrow(18, 87, 26, 87)

    # -------------------------------------------------------------
    # 8. BLOCO DE RETORNO DA SOLUÇÃO ÓTIMA (Perfeitamente isolado e visível)
    # -------------------------------------------------------------
    box(50, 25, 46, 7.5, "5. RETORNO DA SOLUCAO OTIMA:\nreturn dp[max_pizzas]", "#065f46", "#34d399", fontsize=10)

    # Seta para o Fim
    arrow(50, 21, 50, 14.5)

    # -------------------------------------------------------------
    # 9. FIM DO ALGORITMO
    # -------------------------------------------------------------
    box(50, 11, 32, 5.5, "FIM DO ALGORITMO", "#0284c7", "#38bdf8", fontsize=9.5)

    plt.tight_layout()
    plt.savefig(caminho_imagem, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Imagem do fluxograma salva com sucesso em: {caminho_imagem}")

def gerar_docx_exclusivo_fluxograma(caminho_docx, caminho_imagem):
    doc = docx.Document()

    # Margens padrão ABNT / Apresentação
    for s in doc.sections:
        s.top_margin = Inches(2.5 / 2.54)
        s.bottom_margin = Inches(2.0 / 2.54)
        s.left_margin = Inches(2.5 / 2.54)
        s.right_margin = Inches(2.0 / 2.54)

    cor_azul = RGBColor(30, 58, 138)
    cor_cinza = RGBColor(71, 85, 105)

    # 1. Cabeçalho Principal
    p_tit = doc.add_paragraph()
    p_tit.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tit.paragraph_format.space_before = Pt(0)
    p_tit.paragraph_format.space_after = Pt(4)
    r_tit = p_tit.add_run("FLUXOGRAMA DE TOMADA DE DECISÃO: OTIMIZAÇÃO O(P)")
    r_tit.font.name = "Arial"
    r_tit.font.size = Pt(16)
    r_tit.font.bold = True
    r_tit.font.color.rgb = cor_azul

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("Problema do Motoboy (BeeCrowd 1286) — Programação Dinâmica In-Place\nUFRPE 2026.2 | Disciplina: PAA | Profª. Drª. Jeane Melo\nAutor: José Albérico Rocha da Silva (albericolx@gmail.com)")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(10)
    r_sub.font.color.rgb = cor_cinza

    # 2. Imagem Gráfica de Alta Resolução Embutida
    if os.path.exists(caminho_imagem):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(6)
        doc.add_picture(caminho_imagem, width=Inches(6.2))

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(16)
        r_cap = p_cap.add_run("Figura 1. Fluxograma de blocos do algoritmo in-place O(P) com varredura reversa.")
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(9.5)
        r_cap.font.bold = True
        r_cap.font.color.rgb = cor_cinza

    # Quebra de página para o detalhamento editável dos blocos
    doc.add_page_break()

    # 3. Título da Seção de Blocos Editáveis
    p_sec = doc.add_paragraph()
    p_sec.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_sec.paragraph_format.space_before = Pt(8)
    p_sec.paragraph_format.space_after = Pt(10)
    r_sec = p_sec.add_run("DETALHAMENTO EDITÁVEL DOS BLOCOS DO FLUXOGRAMA")
    r_sec.font.name = "Arial"
    r_sec.font.size = Pt(13)
    r_sec.font.bold = True
    r_sec.font.color.rgb = cor_azul

    blocos = [
        ("BLOCO 1: INÍCIO E ALOCAÇÃO 1D", "0284C7",
         "• Comando: dp = [0] * (max_pizzas + 1)\n"
         "• Função: Aloca um único vetor unidimensional de dimensão P + 1 inicializado com zeros.\n"
         "• Memória: O(P) em memória contígua (apenas 31 inteiros para P = 30 pizzas)."),

        ("BLOCO 2: LAÇO EXTERNO (PEDIDOS)", "1E3A8A",
         "• Comando: for tempo, pizzas in pedidos:\n"
         "• Função: Percorre sequencialmente cada pedido i da pizzaria de 1 até N.\n"
         "• Se todos os pedidos foram processados: avança diretamente para o Bloco 6 (Retorno da Solução Ótima)."),

        ("BLOCO 3: LAÇO INTERNO (VARREDURA REVERSA)", "D97706",
         "• Comando: for w in range(max_pizzas, pizzas - 1, -1):\n"
         "• Função: Varre as capacidades da mochila da direita para a esquerda (w = P até pizzas).\n"
         "★ Regra de Ouro Didática: Esta varredura DEVE ser decrescente para garantir que cada pedido seja usado no máximo 1 única vez (propriedade 0-1)."),

        ("BLOCO 4: NÓ DE DECISÃO DE BELLMAN", "4F46E5",
         "• Condição: if dp[w - pizzas] + tempo > dp[w]:\n"
         "  ├── RAMO SIM (Vence Levar): dp[w] = dp[w - pizzas] + tempo (atualiza o ganho in-place).\n"
         "  └── RAMO NÃO (Vence Manter): dp[w] permanece inalterado (a solução anterior já é ótima)."),

        ("BLOCO 5: DECREMENTO DA CAPACIDADE", "64748B",
         "• Comando: w = w - 1 (Continua até w atingir pizzas - 1).\n"
         "• Em seguida, retorna ao Bloco 2 para analisar o próximo pedido da lista."),

        ("BLOCO 6: RETORNO DA SOLUÇÃO ÓTIMA", "059669",
         "• Comando: return dp[max_pizzas]\n"
         "• Função: A última posição do vetor dp[P] contém o tempo máximo absoluto de entrega.\n"
         "• Complexidade Final: Tempo O(N · P) | Espaço O(P) | Juiz BeeCrowd: Accepted (0.095s).")
    ]

    table = doc.add_table(rows=len(blocos), cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    for idx, (titulo, cor_hex, texto) in enumerate(blocos):
        cell = table.rows[idx].cells[0]
        set_cell_background(cell, "F8FAFC")
        set_cell_margins(cell, 80, 80, 140, 140)

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)

        r_t = p.add_run(f"▼ {titulo}\n")
        r_t.font.name = "Arial"
        r_t.font.size = Pt(10.5)
        r_t.font.bold = True
        r_int = int(cor_hex[0:2], 16)
        g_int = int(cor_hex[2:4], 16)
        b_int = int(cor_hex[4:6], 16)
        r_t.font.color.rgb = RGBColor(r_int, g_int, b_int)

        r_desc = p.add_run(texto)
        r_desc.font.name = "Times New Roman"
        r_desc.font.size = Pt(10)

    doc.save(caminho_docx)
    print(f"Documento Word exclusivo do fluxograma salvo com sucesso em: {caminho_docx}")

if __name__ == "__main__":
    base_dir = r"C:\Users\Windows 10\OneDrive\Documentos\UFRPE\2026.2\Projeto e Análise de Algorítimos\Projeto VA_02\Motoboy"
    img_path = os.path.join(base_dir, "docs", "fluxograma_otimizacao_1d.png")
    docx_path = os.path.join(base_dir, "docs", "fluxograma_word_otimizacao_1d.docx")

    desenhar_fluxograma_imagem(img_path)
    gerar_docx_exclusivo_fluxograma(docx_path, img_path)
