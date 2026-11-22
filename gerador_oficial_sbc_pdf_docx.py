"""
Gerador Oficial do Artigo SBC em PDF e DOCX (Word)
Disciplina: Projeto e Análise de Algoritmos (PAA) - UFRPE 2026.2
Professora: Dra. Jeane Melo
Autor: José Albérico Rocha da Silva (autor)
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT

# Bibliotecas Word
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

def gerar_pdf(destino_pdf, imagem_print):
    # Margens SBC: Superior 3.5cm, Inferior 2.5cm, Esquerda 3.0cm, Direita 3.0cm
    doc = SimpleDocTemplate(
        destino_pdf,
        pagesize=A4,
        leftMargin=3.0 * cm,
        rightMargin=3.0 * cm,
        topMargin=3.5 * cm,
        bottomMargin=2.5 * cm
    )

    styles = getSampleStyleSheet()

    # Estilos SBC
    style_title = ParagraphStyle(
        'SBCTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=15,
        leading=18,
        alignment=TA_CENTER,
        spaceAfter=10
    )

    style_author = ParagraphStyle(
        'SBCAuthor',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=11.5,
        leading=13,
        alignment=TA_CENTER,
        spaceAfter=4
    )

    style_address = ParagraphStyle(
        'SBCAddress',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9.5,
        leading=11.5,
        alignment=TA_CENTER,
        spaceAfter=3
    )

    style_email = ParagraphStyle(
        'SBCEmail',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=9.5,
        leading=11.5,
        alignment=TA_CENTER,
        spaceAfter=14
    )

    style_abstract = ParagraphStyle(
        'SBCAbstract',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9.5,
        leading=12,
        alignment=TA_JUSTIFY,
        leftIndent=0.8 * cm,
        rightIndent=0.8 * cm,
        spaceBefore=4,
        spaceAfter=8
    )

    style_h1 = ParagraphStyle(
        'SBCH1',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=12,
        leading=14,
        alignment=TA_LEFT,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    style_h2 = ParagraphStyle(
        'SBCH2',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=11,
        leading=13,
        alignment=TA_LEFT,
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    )

    style_p = ParagraphStyle(
        'SBCParagraph',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10.5,
        leading=13,
        alignment=TA_JUSTIFY,
        firstLineIndent=1.27 * cm,
        spaceBefore=0,
        spaceAfter=3
    )

    style_p_noindent = ParagraphStyle(
        'SBCParagraphNoIndent',
        parent=style_p,
        firstLineIndent=0
    )

    style_caption = ParagraphStyle(
        'SBCCaption',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        alignment=TA_CENTER,
        spaceBefore=3,
        spaceAfter=5
    )

    style_code = ParagraphStyle(
        'SBCCode',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10,
        alignment=TA_LEFT,
        leftIndent=0.5 * cm,
        spaceBefore=3,
        spaceAfter=4
    )

    style_ref = ParagraphStyle(
        'SBCReference',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9,
        leading=11,
        alignment=TA_JUSTIFY,
        leftIndent=0.5 * cm,
        firstLineIndent=-0.5 * cm,
        spaceBefore=2,
        spaceAfter=3
    )

    story = []

    # Título
    story.append(Paragraph("Resolução Otimizada do Problema do Motoboy (BeeCrowd 1286) via Programação Dinâmica: Estudo de Caso da Mochila Binária", style_title))
    
    # Autor
    story.append(Paragraph("José Albérico Rocha da Silva", style_author))
    story.append(Paragraph("Departamento de Computação – Universidade Federal Rural de Pernambuco (UFRPE)<br/>Segunda Verificação de Aprendizagem – Projeto e Análise de Algoritmos (PAA) – 2026.2<br/>Docente: Profª. Drª. Jeane Melo | Tema 6: BeeCrowd Problema 1286: Motoboy", style_address))
    story.append(Paragraph("albericolx@gmail.com", style_email))

    # Abstract e Resumo
    story.append(Paragraph("<b>Abstract.</b> <i>This paper presents the modeling and computational solution for problem 1286 (Motoboy) from the BeeCrowd platform, following the Brazilian Computer Society (SBC) template. The problem models the operational logistics of a delivery courier aiming to maximize delivery working time under a strict motorcycle carry capacity. We establish the reduction of this scenario to the classical 0-1 Knapsack Problem (NP-complete). A thorough theoretical review of the knapsack algorithm is provided, detailing its mechanics and justifying why greedy and brute-force methods fail. The historical origins of Dynamic Programming—conceived by Richard Bellman at RAND Corporation during the Cold War—and the Principle of Optimality are explored. Everyday real-world applications in GPS navigation, courier delivery, bioinformatics, cloud resource scheduling, and text correction are analyzed. The algorithm was coded in Python 3 with O(P) space optimization, incorporating step-by-step backtracking reconstruction, online judge acceptance verification (Accepted), and full compliance with CNPq Ordinance No. 2,664/2026.</i>", style_abstract))

    story.append(Paragraph("<b>Resumo.</b> <i>Este artigo descreve a modelagem matemática e a resolução computacional do problema 1286 (Motoboy) da plataforma BeeCrowd, em estrita conformidade com o padrão da SBC e normas ABNT. O desafio modela a decisão logística de um entregador de pizzas que busca maximizar seu tempo total de trabalho diário sob restrição volumétrica de capacidade no baú da moto. Demonstra-se que o problema mapeia-se de forma isomórfica à Mochila Binária 0-1 (NP-completo). Apresenta-se uma sólida revisão teórica do algoritmo da mochila, explicando seu funcionamento e por que ele deve ser empregado neste projeto perante o fracasso de heurísticas gulosas e da busca por força bruta. Contextualiza-se a história da Programação Dinâmica criada por Richard Bellman na RAND Corporation durante a Guerra Fria e seu Princípio da Otimidade, seguida por aplicações contemporâneas no cotidiano (GPS, delivery, bioinformática, computação em nuvem e corretores ortográficos). O código foi implementado em Python 3 com otimização espacial em O(P), rastreamento de matriz, recuperação ótima por retrocesso (backtracking), comprovação de aceite (Accepted) no BeeCrowd e declaração da Portaria nº 2.664/2026 do CNPq.</i>", style_abstract))

    # 1. Introdução
    story.append(Paragraph("1. Introdução e Contextualização do Problema", style_h1))
    story.append(Paragraph("No problema 1286 do BeeCrowd (<i>Motoboy</i>), somos apresentados a José, entregador de uma conceituada pizzaria que recebe diariamente uma listagem contendo <i>N</i> pedidos de clientes (1 &le; <i>N</i> &le; 20). Cada pedido <i>i</i> possui duas grandezas determinísticas associadas: o tempo de entrega <i>t<sub>i</sub></i> &gt; 0 (em minutos), correspondendo ao benefício/ganho obtido por José ao realizar aquela rota, e a quantidade de pizzas demandadas <i>p<sub>i</sub></i> &gt; 0, que representa a ocupação física no baú de sua motocicleta.", style_p_noindent))
    story.append(Paragraph("A motocicleta dispõe de uma capacidade máxima de transporte de <i>P</i> pizzas simultâneas (1 &le; <i>P</i> &le; 30). Devido às restrições contratuais e à integridade dos produtos, cada pedido <i>i</i> só pode ser atendido de forma integral ou completamente recusado (não é permitida a partição de encomendas). O objetivo consiste em selecionar o subconjunto de pedidos que maximize o tempo total de entregas sem ultrapassar a capacidade <i>P</i> do baú.", style_p))

    # 2. Revisão Teórica: Algoritmo da Mochila
    story.append(Paragraph("2. Revisão Teórica: O Algoritmo da Mochila (Knapsack Problem)", style_h1))
    story.append(Paragraph("O <b>Problema da Mochila (Knapsack Problem)</b>, formalizado por George Dantzig (1957) e classificado por Richard Karp (1972) como um dos 21 problemas fundamentais <b>NP-completos</b>, modela o dilema da alocação ótima de recursos escassos sob restrições físicas ou orçamentárias. Na variante da <i>Mochila Binária 0-1</i>, dispõe-se de uma capacidade máxima <i>W</i> e um conjunto de itens com valores <i>v<sub>i</sub></i> e pesos <i>w<sub>i</sub></i>. Cada item deve ser aceito integralmente (<i>x<sub>i</sub></i> = 1) ou descartado (<i>x<sub>i</sub></i> = 0):", style_p_noindent))
    story.append(Paragraph("<b>Maximizar</b> <i>Z</i> = &sum;<sub>i=1</sub><sup>N</sup> (<i>t<sub>i</sub></i> &middot; <i>x<sub>i</sub></i>) &emsp; <b>sujeito a:</b> &sum;<sub>i=1</sub><sup>N</sup> (<i>p<sub>i</sub></i> &middot; <i>x<sub>i</sub></i>) &le; <i>P</i>, &emsp; com <i>x<sub>i</sub></i> &isin; {0, 1}", ParagraphStyle('Formula', parent=style_p_noindent, alignment=TA_CENTER, fontName='Times-Italic', spaceBefore=4, spaceAfter=4)))
    story.append(Paragraph("<b>Por que devemos usar a Mochila 0-1 neste projeto?</b> Existe uma equivalência isomórfica exata entre o problema do motoboy e a mochila clássica: a capacidade <i>W</i> corresponde ao baú de <i>P</i> pizzas; o peso <i>w<sub>i</sub></i> à quantidade de pizzas <i>p<sub>i</sub></i>; o valor <i>v<sub>i</sub></i> ao tempo de entrega <i>t<sub>i</sub></i>; e a decisão binária <i>x<sub>i</sub></i> &isin; {0, 1} à indivisibilidade dos pedidos (uma pizzaria não fatia um pedido entre motoboys). Essa modelagem é indispensável, pois reflete rigorosamente a física do problema.", style_p))

    # 3. Breve Histórico da Programação Dinâmica
    story.append(Paragraph("3. Breve Histórico da Programação Dinâmica", style_h1))
    story.append(Paragraph("A técnica de <b>Programação Dinâmica (PD)</b> foi criada na década de 1950 pelo matemático norte-americano <b>Richard Bellman</b> enquanto atuava na <b>RAND Corporation</b>, principal centro de pesquisa estratégica da Força Aérea dos Estados Unidos durante o auge da Guerra Fria. Bellman estudava processos sequenciais de tomada de decisão em múltiplos estágios.", style_p_noindent))
    story.append(Paragraph("Em sua autobiografia (Bellman 1984), o autor revelou a curiosa motivação para a escolha do nome: o Secretário de Defesa da época, Charles Wilson, tinha aversão à pesquisa básica e desdém pela matemática pura, cortando verbas rotuladas como 'pesquisa'. Para proteger o financiamento contra o Pentágono, Bellman adotou <i>'Programação'</i> (que no jargão militar da época significava planejamento logístico tabular, como em cronogramas) e <i>'Dinâmica'</i> (decisões que evoluem no tempo), formulando um título pomposo e incontestável perante os burocratas do governo.", style_p))
    story.append(Paragraph("O pilar da técnica é o célebre <b>Princípio da Otimidade de Bellman (1957)</b>: <i>'uma política ótima tem a propriedade de que, quaisquer que sejam o estado inicial e as decisões iniciais, as decisões restantes devem constituir uma política ótima com relação ao estado resultante da primeira decisão'</i>. Isso permite resolver subproblemas locais sobrepostos e compor a solução global de forma ascendente (<i>bottom-up</i>).", style_p))

    # 4. Exemplos no Cotidiano
    story.append(Paragraph("4. Aplicações Práticas da Programação Dinâmica no Cotidiano", style_h1))
    story.append(Paragraph("A Programação Dinâmica opera nos bastidores das tecnologias digitais que utilizamos diariamente:", style_p_noindent))
    story.append(Paragraph("&bull; <b>GPS e Roteirização de Trânsito (Waze, Google Maps):</b> Algoritmos como Bellman-Ford e a subestrutura de Dijkstra decompõem viagens em cruzamentos viários intermediários, encontrando a rota de menor tempo sem reavaliar bilhões de trajetos a cada oscilação no tráfego.", style_p_noindent))
    story.append(Paragraph("&bull; <b>Logística Urbana e Delivery (iFood, Rappi, Amazon):</b> Otimização de rotas veiculares (VRP) e empacotamento de encomendas em baús e frotas de entrega sob restrições volumétricas e horários rígidos.", style_p_noindent))
    story.append(Paragraph("&bull; <b>Correção Ortográfica e Comparação de Códigos (Smartphones, Git Diff):</b> A <i>Distância de Edição de Levenshtein</i> calcula o número mínimo de inserções, remoções e trocas para corrigir palavras digitadas incorretamente, enquanto o algoritmo <i>LCS (Maior Subsequência Comum)</i> detecta diferenças entre commits de software.", style_p_noindent))
    story.append(Paragraph("&bull; <b>Bioinformática e Genética (Needleman-Wunsch e Smith-Waterman):</b> Alinhamento de cadeias de nucleotídeos de DNA e RNA em matrizes de PD para mapear mutações genéticas e parentesco evolutivo entre espécies.", style_p_noindent))
    story.append(Paragraph("&bull; <b>Computação em Nuvem (AWS, Google Cloud):</b> Empacotamento ótimo de máquinas virtuais e contêineres Docker em servidores físicos sob limites de CPU e memória RAM (<i>Bin Packing</i>), reduzindo servidores ociosos e energia.", style_p_noindent))
    story.append(Paragraph("&bull; <b>Reconhecimento de Voz (Siri, Alexa):</b> O algoritmo <i>Dynamic Time Warping (DTW)</i> alinha sinais de áudio com velocidades de fala distintas para reconhecer comandos vocais com alta precisão.", style_p_noindent))

    # 5. A Técnica e a Dedução
    story.append(Paragraph("5. Dedução da Equação de Bellman e Falha de Heurísticas", style_h1))
    story.append(Paragraph("A busca exaustiva por força bruta testa todos os 2<sup><i>N</i></sup> subconjuntos, incorrendo em custo exponencial <i>O</i>(2<sup><i>N</i></sup>) impraticável para instâncias moderadas (Cormen et al. 2012). Abordagens gulosas baseadas na razão ganho/custo (<i>t<sub>i</sub></i> / <i>p<sub>i</sub></i>) falham na Mochila 0-1 devido à indivisibilidade dos itens. <i>Exemplo didático:</i> para capacidade <i>P</i> = 10 e pedidos com razão idêntica 10 min/pizza (Pedido A: 60 min, 6 piz; Pedido B: 50 min, 5 piz; Pedido C: 50 min, 5 piz), a heurística escolhe o Pedido A e para (sobram 4 pizzas), totalizando 60 min. A escolha ótima global consiste em levar os Pedidos B e C, somando 10 pizzas e alcançando 100 min (66,7% superior).", style_p_noindent))
    story.append(Paragraph("Seja <i>DP</i>[<i>i</i>][<i>w</i>] o tempo máximo alcançável considerando os primeiros <i>i</i> pedidos com capacidade parcial de <i>w</i> pizzas. <b>Casos Base:</b> <i>DP</i>[0][<i>w</i>] = 0 (zero pedidos geram zero minutos) e <i>DP</i>[<i>i</i>][0] = 0 (mochila de zero vagas transporta zero pizzas).", style_p))
    story.append(Paragraph("<b>Transição de Bellman:</b><br/>"
                           "&bull; Se <i>p<sub>i</sub></i> &gt; <i>w</i> (não cabe): <i>DP</i>[<i>i</i>][<i>w</i>] = <i>DP</i>[<i>i</i>-1][<i>w</i>]<br/>"
                           "&bull; Se <i>p<sub>i</sub></i> &le; <i>w</i> (cabe): <i>DP</i>[<i>i</i>][<i>w</i>] = max( <i>DP</i>[<i>i</i>-1][<i>w</i>], <i>t<sub>i</sub></i> + <i>DP</i>[<i>i</i>-1][<i>w</i> - <i>p<sub>i</sub></i>] )", style_p))

    # Tabela 1
    story.append(Paragraph("Tabela 1. Matriz completa de Programação Dinâmica DP[i][w] para N=4 e P=10", style_caption))
    tabela_dados = [
        ['i \\ w', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['0 (base)', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['1 (20m, 5p)', '0', '0', '0', '0', '0', '20', '20', '20', '20', '20', '20'],
        ['2 (70m, 7p)', '0', '0', '0', '0', '0', '20', '20', '70', '70', '70', '70'],
        ['3 (15m, 2p)', '0', '0', '15', '15', '15', '20', '20', '70', '70', '85', '85'],
        ['4 (25m, 3p)', '0', '0', '15', '25', '25', '40', '40', '70', '70', '85', '95']
    ]
    tabela_pdf = Table(tabela_dados, colWidths=[2.2*cm] + [1.1*cm]*11)
    tabela_pdf.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,0), (0,-1), 'Times-Bold'),
        ('FONTNAME', (11,5), (11,5), 'Times-Bold'),
        ('TEXTCOLOR', (11,5), (11,5), colors.darkblue),
    ]))
    story.append(tabela_pdf)

    story.append(Paragraph("<b>Decisão Ótima por Retrocesso (Backtracking):</b> Partindo de <i>DP</i>[4][10] = 95:<br/>"
                           "1. <i>DP</i>[4][10] &ne; <i>DP</i>[3][10] (95 &ne; 85) &rArr; <b>Pedido #4 Selecionado!</b> (Sobram 10 &minus; 3 = 7 pizzas).<br/>"
                           "2. <i>DP</i>[3][7] = <i>DP</i>[2][7] (70 = 70) &rArr; <b>Pedido #3 Descartado!</b> (Sobram 7 pizzas).<br/>"
                           "3. <i>DP</i>[2][7] &ne; <i>DP</i>[1][7] (70 &ne; 20) &rArr; <b>Pedido #2 Selecionado!</b> (Sobram 7 &minus; 7 = 0 pizzas).<br/>"
                           "4. Capacidade esgotada. Conjunto ótimo: <b>{Pedido #2, Pedido #4}</b>, somando 95 minutos e 10 pizzas (100% de aproveitamento do baú).", style_p_noindent))

    # 6. Implementação Computacional
    story.append(Paragraph("6. Implementação Computacional e Complexidade", style_h1))
    story.append(Paragraph("Para a submissão de alto desempenho, reduziu-se a matriz a um único vetor unidimensional de tamanho <i>P</i>+1, iterando as capacidades em <b>ordem decrescente</b> (de <i>P</i> descendo até <i>p<sub>i</sub></i>) para assegurar a propriedade da mochila 0-1:", style_p_noindent))
    
    codigo_str = (
        "def resolver_caso(n, max_pizzas, pedidos):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;dp = [0] * (max_pizzas + 1)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;for tempo, pizzas in pedidos:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for w in range(max_pizzas, pizzas - 1, -1):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if dp[w - pizzas] + tempo &gt; dp[w]:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dp[w] = dp[w - pizzas] + tempo<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;return dp[max_pizzas]"
    )
    story.append(Paragraph(codigo_str, style_code))

    story.append(Paragraph("<b>Complexidade Assintótica:</b> O algoritmo possui complexidade temporal <b>&Theta;(<i>N</i> &middot; <i>P</i>)</b> (pseudo-polinomial). Para os limites do BeeCrowd (<i>N</i> &le; 20, <i>P</i> &le; 30), executam-se no máximo 600 operações elementares (&lt; 0.001 s). A complexidade espacial é de estritamente <b><i>O</i>(<i>P</i>)</b> na versão otimizada (apenas 31 posições de memória RAM).", style_p_noindent))

    story.append(Paragraph("<b>Simulador Web Interativo e Auditoria de Backtracking:</b> Como contribuição educacional para a disciplina de PAA, foi desenvolvido um simulador interativo em ambiente Web (HTML5/CSS3/JavaScript puro, arquivo <code>simulador_visual_motoboy.html</code>). A aplicação enquadra em tela única a configuração dinâmica de parâmetros (capacidade <i>P</i>, quantidade <i>N</i>, tempos e pizzas), a exibição do preenchimento da matriz com iluminação dos ramos de Bellman e a auditoria passo a passo do retrocesso (<i>backtracking</i>), apresentando justificativas textuais de negócio para a escolha ou descarte de cada pedido. O código-fonte e o simulador interativo encontram-se disponíveis publicamente para replicação acadêmica em: &lt;https://github.com/albericolx/PAA_2026_2_Projeto&gt;.", style_p_noindent))

    # 7. Resultados Experimentais
    story.append(Paragraph("7. Resultados Experimentais e Validação no BeeCrowd", style_h1))
    story.append(Paragraph("O código-fonte foi submetido na plataforma BeeCrowd sob a linguagem Python 3.9, obtendo o veredito oficial <b>Accepted</b> com tempo de execução de <b>0.095s</b> (limite: 1.000s) e tamanho de 2,49 KB sob a Submissão # 50429092, realizada em 07/11/2026 às 10:23:03. A Figura 1 comprova o aceite oficial emitido pelo juiz eletrônico:", style_p_noindent))

    if os.path.exists(imagem_print):
        img = Image(imagem_print, width=13.5*cm, height=5.6*cm)
        story.append(KeepTogether([
            Spacer(1, 2),
            img,
            Paragraph("Figura 1. Tela de aceite (Accepted) do Problema 1286 (Motoboy) emitida pelo juiz eletrônico do BeeCrowd.", style_caption)
        ]))

    # 8. Considerações Finais
    story.append(Paragraph("8. Considerações Finais", style_h1))
    story.append(Paragraph("A Programação Dinâmica confirmou-se como a abordagem exata e eficiente para o Problema da Mochila 0-1, contornando a complexidade exponencial da força bruta e a falibilidade das abordagens gulosas. O legado histórico de Richard Bellman continua indispensável no projeto de algoritmos contemporâneos.", style_p_noindent))

    # Declaração CNPq
    story.append(Paragraph("Declaração de Uso de IA Generativa (Portaria nº 2.664/2026 – CNPq)", style_h1))
    story.append(Paragraph("Em cumprimento ao Artigo 9º da Portaria nº 2.664/2026 do CNPq, declara-se que a ferramenta Google Antigravity / Gemini 3.8 Flash foi empregada como suporte auxiliar na concepção teórica, estruturação do artigo conforme o template SBC e revisão analítica da complexidade assintótica. A implementação computacional, testes, depuração e validação experimental foram executados e são de integral responsabilidade autoral do discente <b>José Albérico Rocha da Silva</b>.", style_p_noindent))

    # Referências
    story.append(Paragraph("References", style_h1))
    refs = [
        "BeeCrowd (2026) “Problema 1286: Motoboy”, BeeCrowd Academic Online Judge, Disponível em: &lt;https://judge.beecrowd.com/pt/problems/view/1286&gt;, Acesso em: 07 nov. 2026.",
        "Bellman, R. (1954) “The theory of dynamic programming”, <i>Bulletin of the American Mathematical Society</i>, v. 60, n. 6, p. 503-515.",
        "Bellman, R. (1957) <i>Dynamic Programming</i>, Princeton, NJ: Princeton University Press.",
        "Bellman, R. (1984) <i>Eye of the Hurricane: An Autobiography</i>, Singapore: World Scientific Publishing.",
        "CNPq (2026) “Portaria nº 2.664, de 6 de março de 2026: Diretrizes para uso de Inteligência Artificial Generativa em atividades de pesquisa e submissão acadêmica”, Brasília: MCTI/CNPq.",
        "Cormen, T. H., Leiserson, C. E., Rivest, R. L. e Stein, C. (2012) <i>Algoritmos: teoria e prática</i>, 3ª edição, Rio de Janeiro: Elsevier.",
        "Dantzig, G. B. (1957) “Discrete-variable extremum problems”, <i>Operations Research</i>, v. 5, n. 2, p. 266-277.",
        "Karp, R. M. (1972) “Reducibility among combinatorial problems”, In: Miller, R. E., Thatcher, J. W. (Ed.), <i>Complexity of Computer Computations</i>, New York: Plenum Press, p. 85-103.",
        "Kleinberg, J. e Tardos, É. (2006) <i>Algorithm design</i>, Boston: Pearson/Addison-Wesley.",
        "SBC (2024) “Instructions for Authors of SBC Conferences Papers and Abstracts”, Sociedade Brasileira de Computação, Porto Alegre."
    ]
    for r in refs:
        story.append(Paragraph(r, style_ref))

    doc.build(story)
    print(f"PDF Oficial SBC gerado com sucesso em: {destino_pdf}")

def gerar_docx(destino_docx, imagem_print):
    doc = docx.Document()
    
    # Margens SBC: 3.5cm topo, 2.5cm rodapé, 3.0cm esquerda/direita
    for s in doc.sections:
        s.top_margin = Inches(3.5 / 2.54)
        s.bottom_margin = Inches(2.5 / 2.54)
        s.left_margin = Inches(3.0 / 2.54)
        s.right_margin = Inches(3.0 / 2.54)

    # Título (16pt Bold, centralizado)
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_t = p_title.add_run("Resolução Otimizada do Problema do Motoboy (BeeCrowd 1286) via Programação Dinâmica: Estudo de Caso da Mochila Binária")
    run_t.font.name = "Times New Roman"
    run_t.font.size = Pt(16)
    run_t.font.bold = True
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(10)

    # Autor (12pt Bold, centralizado)
    p_author = doc.add_paragraph()
    p_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_a = p_author.add_run("José Albérico Rocha da Silva")
    run_a.font.name = "Times New Roman"
    run_a.font.size = Pt(12)
    run_a.font.bold = True

    # Filiação (10pt, centralizado)
    p_aff = doc.add_paragraph()
    p_aff.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_aff = p_aff.add_run("Departamento de Computação – Universidade Federal Rural de Pernambuco (UFRPE)\nSegunda Verificação de Aprendizagem – Projeto e Análise de Algoritmos (PAA) – 2026.2\nDocente: Profª. Drª. Jeane Melo | Tema 6: BeeCrowd Problema 1286: Motoboy")
    run_aff.font.name = "Times New Roman"
    run_aff.font.size = Pt(10)

    # Email (10pt Courier New)
    p_mail = doc.add_paragraph()
    p_mail.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_m = p_mail.add_run("albericolx@gmail.com")
    run_m.font.name = "Courier New"
    run_m.font.size = Pt(10)
    p_mail.paragraph_format.space_after = Pt(14)

    # Abstract
    p_abs = doc.add_paragraph()
    p_abs.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_abs.paragraph_format.left_indent = Inches(0.8 / 2.54)
    p_abs.paragraph_format.right_indent = Inches(0.8 / 2.54)
    p_abs.paragraph_format.space_after = Pt(8)
    r_abs_t = p_abs.add_run("Abstract. ")
    r_abs_t.font.name = "Times New Roman"
    r_abs_t.font.size = Pt(10)
    r_abs_t.font.bold = True
    r_abs = p_abs.add_run("This paper presents the modeling and computational solution for problem 1286 (Motoboy) from the BeeCrowd platform, following the SBC template. The problem models a courier seeking to maximize delivery working time under a strict motorcycle carry capacity. We establish the reduction to the classical 0-1 Knapsack Problem (NP-complete). A thorough theoretical review of the knapsack algorithm is provided, explaining why greedy and brute-force methods fail. The historical origins of Dynamic Programming—conceived by Richard Bellman at RAND Corporation during the Cold War—and the Principle of Optimality are explored. Real-world applications in GPS navigation, logistics delivery, bioinformatics, cloud computing, and spell checking are discussed. The solution was coded in Python 3 with O(P) space optimization, backtracking reconstruction, online judge acceptance verification (Accepted), and compliance with CNPq Ordinance No. 2,664/2026.")
    r_abs.font.name = "Times New Roman"
    r_abs.font.size = Pt(10)
    r_abs.font.italic = True

    # Resumo
    p_res = doc.add_paragraph()
    p_res.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_res.paragraph_format.left_indent = Inches(0.8 / 2.54)
    p_res.paragraph_format.right_indent = Inches(0.8 / 2.54)
    p_res.paragraph_format.space_after = Pt(12)
    r_res_t = p_res.add_run("Resumo. ")
    r_res_t.font.name = "Times New Roman"
    r_res_t.font.size = Pt(10)
    r_res_t.font.bold = True
    r_res = p_res.add_run("Este artigo descreve a modelagem matemática e a resolução computacional do problema 1286 (Motoboy) da plataforma BeeCrowd, em conformidade com o padrão da SBC e normas ABNT. O desafio modela a decisão logística de um entregador de pizzas que busca maximizar seu tempo de trabalho diário sob restrição volumétrica de capacidade no baú da moto. Demonstra-se que o problema mapeia-se de forma isomórfica à Mochila Binária 0-1 (NP-completo). Apresenta-se uma sólida revisão teórica do algoritmo da mochila, explicando seu funcionamento e por que ele deve ser empregado neste projeto perante o fracasso de heurísticas gulosas e da busca por força bruta. Contextualiza-se a história da Programação Dinâmica criada por Richard Bellman na RAND Corporation durante a Guerra Fria e seu Princípio da Otimidade, seguida por aplicações contemporâneas no cotidiano (GPS, delivery, bioinformática, computação em nuvem e corretores ortográficos). O código foi implementado em Python 3 com otimização espacial em O(P), rastreamento de matriz, recuperação por retrocesso (backtracking), comprovação de aceite (Accepted) no BeeCrowd e declaração da Portaria nº 2.664/2026 do CNPq.")
    r_res.font.name = "Times New Roman"
    r_res.font.size = Pt(10)
    r_res.font.italic = True

    def add_h1(texto):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(texto)
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)
        r.font.bold = True
        return p

    def add_p(texto, indent=True):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if indent:
            p.paragraph_format.first_line_indent = Inches(1.27 / 2.54)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(texto)
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)
        return p

    # Seções no Word
    add_h1("1. Introdução e Contextualização do Problema")
    add_p("No problema 1286 do BeeCrowd (Motoboy), somos apresentados a José, entregador de uma conceituada pizzaria que recebe diariamente uma listagem contendo N pedidos de clientes (1 <= N <= 20). Cada pedido i possui duas grandezas determinísticas associadas: o tempo de entrega t_i > 0 (em minutos), correspondendo ao benefício/ganho obtido por José ao realizar aquela rota, e a quantidade de pizzas demandadas p_i > 0, que representa a ocupação física no baú de sua motocicleta.", indent=False)
    add_p("A motocicleta dispõe de uma capacidade máxima de transporte de P pizzas simultâneas (1 <= P <= 30). Devido às restrições contratuais e à integridade dos produtos, cada pedido i só pode ser atendido de forma integral ou completamente recusado (não é permitida a partição de encomendas). O objetivo consiste em selecionar o subconjunto de pedidos que maximize o tempo total de entregas sem ultrapassar a capacidade P do baú.")

    add_h1("2. Revisão Teórica: O Algoritmo da Mochila (Knapsack Problem)")
    add_p("O Problema da Mochila (Knapsack Problem), formalizado por George Dantzig (1957) e classificado por Richard Karp (1972) como um dos 21 problemas fundamentais NP-completos, modela o dilema da alocação ótima de recursos escassos sob restrições físicas ou orçamentárias. Na variante da Mochila Binária 0-1, dispõe-se de uma capacidade máxima W e um conjunto de itens com valores v_i e pesos w_i. Cada item deve ser aceito integralmente (x_i = 1) ou descartado (x_i = 0):", indent=False)
    add_p("Maximizar Z = sum(t_i * x_i) sujeito a: sum(p_i * x_i) <= P, com x_i pertencente a {0, 1}.", indent=False)
    add_p("Por que devemos usar a Mochila 0-1 neste projeto? Existe uma equivalência isomórfica perfeita entre o problema do motoboy e a mochila clássica: a capacidade W corresponde ao baú de P pizzas; o peso w_i à quantidade de pizzas p_i; o valor v_i ao tempo de entrega t_i; e a decisão binária x_i em {0, 1} à indivisibilidade dos pedidos (uma pizzaria não fatia um pedido entre motoboys). Essa modelagem é indispensável, pois reflete com exatidão a física do problema.")

    add_h1("3. Breve Histórico da Programação Dinâmica")
    add_p("A técnica de Programação Dinâmica (PD) foi concebida no início da década de 1950 pelo matemático norte-americano Richard Bellman enquanto atuava como pesquisador na RAND Corporation, principal centro de consultoria científica da Força Aérea dos EUA durante o auge da Guerra Fria. Bellman estudava processos sequenciais de tomada de decisão em múltiplos estágios.", indent=False)
    add_p("Em sua autobiografia, Bellman (1984) relatou a curiosa motivação para a escolha do termo: o Secretário de Defesa da época, Charles Wilson, tinha extrema aversão à pesquisa acadêmica básica e ao trabalho de matemáticos puros, cortando verbas rotuladas como 'pesquisa'. Para proteger o financiamento contra o Pentágono, Bellman adotou 'Programação' (planejamento operacional e confecção de cronogramas tabulares) e 'Dinâmica' (decisões que variam no tempo), criando um título pomposo e incontestável perante os burocratas do governo.")
    add_p("O pilar da técnica é o Princípio da Otimidade de Bellman (1957): 'uma política ótima tem a propriedade de que, quaisquer que sejam o estado inicial e as decisões iniciais, as decisões restantes devem constituir uma política ótima com relação ao estado resultante da primeira decisão'. Isso possibilita resolver subproblemas locais sobrepostos e compor a solução global de forma ascendente (bottom-up).")

    add_h1("4. Aplicações Práticas da Programação Dinâmica no Cotidiano")
    add_p("A Programação Dinâmica opera nos bastidores das tecnologias digitais que utilizamos diariamente:", indent=False)
    add_p("• GPS e Roteirização de Trânsito (Waze, Google Maps): Algoritmos como Bellman-Ford e a subestrutura de Dijkstra decompõem viagens em cruzamentos viários intermediários, encontrando a rota de menor tempo sem reavaliar bilhões de trajetos a cada oscilação no tráfego.", indent=False)
    add_p("• Logística Urbana e Delivery (iFood, Rappi, Amazon): Otimização de rotas veiculares (VRP) e empacotamento de encomendas em baús e frotas de entrega sob restrições volumétricas e horários rígidos.", indent=False)
    add_p("• Correção Ortográfica e Comparação de Códigos (Smartphones, Git Diff): A Distância de Edição de Levenshtein calcula o número mínimo de inserções, remoções e trocas para corrigir palavras digitadas incorretamente, enquanto o algoritmo LCS detecta diferenças entre commits de código.", indent=False)
    add_p("• Bioinformática e Genética (Needleman-Wunsch e Smith-Waterman): Alinhamento de cadeias de nucleotídeos de DNA e RNA em matrizes de PD para mapear mutações genéticas e parentesco evolutivo entre espécies.", indent=False)
    add_p("• Computação em Nuvem (AWS, Google Cloud): Empacotamento ótimo de máquinas virtuais e contêineres Docker em servidores físicos sob limites de CPU e memória RAM (Bin Packing), reduzindo servidores ociosos e consumo energético.", indent=False)
    add_p("• Reconhecimento de Voz (Siri, Alexa): O algoritmo Dynamic Time Warping (DTW) alinha sinais de áudio com velocidades de fala distintas para reconhecer comandos vocais com alta precisão.", indent=False)

    add_h1("5. Dedução da Equação de Bellman e Falha de Heurísticas")
    add_p("A busca exaustiva por força bruta testa todos os 2^N subconjuntos, incorrendo em custo exponencial O(2^N) impraticável para instâncias moderadas. Abordagens gulosas baseadas na razão ganho/custo (t_i / p_i) falham na Mochila 0-1 devido à indivisibilidade dos itens. Contraexemplo didático: para capacidade P = 10 e pedidos com razão idêntica 10 min/pizza (Pedido A: 60 min, 6 piz; Pedido B: 50 min, 5 piz; Pedido C: 50 min, 5 piz), a heurística escolhe o Pedido A e para (sobram 4 pizzas), totalizando 60 min. A escolha ótima global consiste em levar os Pedidos B e C, somando 10 pizzas e alcançando 100 min (66,7% superior).", indent=False)
    add_p("Transição de Bellman:")
    add_p("• Se p_i > w (não cabe): DP[i][w] = DP[i-1][w]")
    add_p("• Se p_i <= w (cabe): DP[i][w] = max( DP[i-1][w], t_i + DP[i-1][w - p_i] )")

    # Tabela 1
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cap = p_cap.add_run("Tabela 1. Matriz completa de Programação Dinâmica DP[i][w] para N=4 e P=10")
    r_cap.font.name = "Arial"
    r_cap.font.size = Pt(9.5)
    r_cap.font.bold = True

    table = doc.add_table(rows=6, cols=12)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    t_data = [
        ['i \\ w', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['0 (base)', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['1 (20m, 5p)', '0', '0', '0', '0', '0', '20', '20', '20', '20', '20', '20'],
        ['2 (70m, 7p)', '0', '0', '0', '0', '0', '20', '20', '70', '70', '70', '70'],
        ['3 (15m, 2p)', '0', '0', '15', '15', '15', '20', '20', '70', '70', '85', '85'],
        ['4 (25m, 3p)', '0', '0', '15', '25', '25', '40', '40', '70', '70', '85', '95']
    ]

    for r_idx, row_values in enumerate(t_data):
        row = table.rows[r_idx]
        for c_idx, val in enumerate(row_values):
            cell = row.cells[c_idx]
            cell.text = val
            p_cell = cell.paragraphs[0]
            p_cell.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run_cell = p_cell.runs[0]
            run_cell.font.name = "Times New Roman"
            run_cell.font.size = Pt(8.5)
            if r_idx == 0 or c_idx == 0:
                run_cell.font.bold = True
            if r_idx == 5 and c_idx == 11:
                run_cell.font.bold = True
                run_cell.font.color.rgb = RGBColor(0, 0, 150)

    p_bt = doc.add_paragraph()
    p_bt.paragraph_format.space_before = Pt(6)
    p_bt.paragraph_format.space_after = Pt(6)
    r_bt = p_bt.add_run("Decisão Ótima por Retrocesso (Backtracking): Partindo de DP[4][10] = 95 min, identificam-se os pedidos aceitos comparando com a linha superior. O conjunto selecionado é {Pedido #2, Pedido #4}, somando 95 min e exatamente 10 pizzas (100% de ocupação do baú).")
    r_bt.font.name = "Times New Roman"
    r_bt.font.size = Pt(10)

    add_h1("6. Implementação Computacional e Complexidade Assintótica")
    add_p("Para a submissão de alto desempenho, reduziu-se a matriz a um único vetor unidimensional de tamanho P+1, iterando as capacidades em ordem decrescente (de P descendo até p_i). A complexidade temporal é Theta(N * P) (pseudo-polinomial), executando no máximo 600 operações elementares (< 0.001s). A complexidade espacial é de estritamente O(P) (apenas 31 inteiros em memória).", indent=False)
    add_p("Simulador Visual Web e Auditoria de Backtracking: Como contribuição didática e suporte às demonstrações práticas na UFRPE, foi desenvolvida uma aplicação interativa em ambiente Web (HTML5/CSS3/JavaScript puro, arquivo simulador_visual_motoboy.html). A ferramenta enquadra em tela única a configuração dinâmica de parâmetros (capacidade P, quantidade N, tempos e pizzas), o preenchimento da matriz com destaque dos ramos da equação de Bellman e a auditoria passo a passo do retrocesso (backtracking), justificando textualmente cada decisão tomada. O código-fonte e o simulador interativo estão acessíveis em: <https://github.com/albericolx/PAA_2026_2_Projeto>.", indent=False)

    add_h1("7. Resultados Experimentais e Validação no BeeCrowd")
    add_p("O código-fonte foi submetido na plataforma BeeCrowd sob a linguagem Python 3.9, obtendo o veredito oficial Accepted com tempo de execução de 0.095s sob a Submissão # 50429092, realizada em 07/11/2026 às 10:23:03. A Figura 1 comprova o aceite oficial emitido pelo juiz eletrônico:", indent=False)

    if os.path.exists(imagem_print):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(2)
        doc.add_picture(imagem_print, width=Inches(5.4))
        
        p_cap_fig = doc.add_paragraph()
        p_cap_fig.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap_fig.paragraph_format.space_after = Pt(8)
        r_cap_fig = p_cap_fig.add_run("Figura 1. Tela de aceite (Accepted) do Problema 1286 (Motoboy) emitida pelo juiz eletrônico do BeeCrowd.")
        r_cap_fig.font.name = "Arial"
        r_cap_fig.font.size = Pt(9)
        r_cap_fig.font.bold = True

    add_h1("8. Considerações Finais")
    add_p("A Programação Dinâmica confirmou-se como a abordagem exata e eficiente para o Problema da Mochila 0-1, contornando a complexidade exponencial da força bruta e a falibilidade das abordagens gulosas. O legado histórico de Richard Bellman continua indispensável no projeto de algoritmos contemporâneos.", indent=False)

    add_h1("Declaração de Uso de IA Generativa (Portaria nº 2.664/2026 – CNPq)")
    add_p("Em cumprimento ao Artigo 9º da Portaria nº 2.664/2026 do CNPq, declara-se que a ferramenta Google Antigravity / Gemini 3.8 Flash foi empregada como suporte auxiliar na concepção teórica, estruturação do artigo conforme o template SBC e revisão analítica da complexidade assintótica. A implementação computacional, testes, depuração e validação experimental foram executados e são de integral responsabilidade autoral do discente José Albérico Rocha da Silva.", indent=False)

    add_h1("References")
    refs_doc = [
        "BeeCrowd (2026) “Problema 1286: Motoboy”, BeeCrowd Academic Online Judge, Disponível em: <https://judge.beecrowd.com/pt/problems/view/1286>, Acesso em: 07 nov. 2026.",
        "Bellman, R. (1954) “The theory of dynamic programming”, Bulletin of the American Mathematical Society, v. 60, n. 6, p. 503-515.",
        "Bellman, R. (1957) Dynamic Programming, Princeton, NJ: Princeton University Press.",
        "Bellman, R. (1984) Eye of the Hurricane: An Autobiography, Singapore: World Scientific Publishing.",
        "CNPq (2026) “Portaria nº 2.664, de 6 de março de 2026: Diretrizes para uso de Inteligência Artificial Generativa em atividades de pesquisa e submissão acadêmica”, Brasília: MCTI/CNPq.",
        "Cormen, T. H., Leiserson, C. E., Rivest, R. L. e Stein, C. (2012) Algoritmos: teoria e prática, 3ª edição, Rio de Janeiro: Elsevier.",
        "Dantzig, G. B. (1957) “Discrete-variable extremum problems”, Operations Research, v. 5, n. 2, p. 266-277.",
        "Karp, R. M. (1972) “Reducibility among combinatorial problems”, In: Miller, R. E., Thatcher, J. W. (Ed.), Complexity of Computer Computations, New York: Plenum Press, p. 85-103.",
        "Kleinberg, J. e Tardos, É. (2006) Algorithm design, Boston: Pearson/Addison-Wesley.",
        "SBC (2024) “Instructions for Authors of SBC Conferences Papers and Abstracts”, Sociedade Brasileira de Computação, Porto Alegre."
    ]

    for ref in refs_doc:
        p_ref = doc.add_paragraph()
        p_ref.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_ref.paragraph_format.left_indent = Inches(0.5 / 2.54)
        p_ref.paragraph_format.first_line_indent = Inches(-0.5 / 2.54)
        p_ref.paragraph_format.space_after = Pt(3)
        r_ref = p_ref.add_run(ref)
        r_ref.font.name = "Times New Roman"
        r_ref.font.size = Pt(9.5)

    doc.save(destino_docx)
    print(f"DOCX Oficial SBC gerado com sucesso em: {destino_docx}")

if __name__ == "__main__":
    base_dir = r"C:\Users\Windows 10\OneDrive\Documentos\UFRPE\2026.2\Projeto e Análise de Algorítimos\Projeto VA_02\Motoboy"
    destino_pdf = os.path.join(base_dir, "artigo_sbc_tema6_motoboy.pdf")
    destino_docx = os.path.join(base_dir, "artigo_sbc_tema6_motoboy.docx")
    imagem_print = os.path.join(base_dir, "print_aceite_beecrowd_1286.png")

    gerar_pdf(destino_pdf, imagem_print)
    gerar_docx(destino_docx, imagem_print)
