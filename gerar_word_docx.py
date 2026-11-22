# ===============================================================================
# Script para gerar o arquivo Word (.docx) formatado segundo as normas da ABNT
# Autor: José Albérico Rocha da Silva
# UFRPE - Projeto e Análise de Algoritmos (PAA)
# ===============================================================================

import os
import zipfile

def criar_docx_abnt(caminho_saida):
    """
    Cria um arquivo .docx nativo do Microsoft Word em conformidade com a ABNT
    utilizando a estrutura pura de OpenXML (sem dependência de bibliotecas externas).
    """
    document_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <!-- TITULO DO ARTIGO -->
    <w:p>
      <w:pPr>
        <w:jc w:val="center"/>
        <w:spacing w:before="240" w:after="240" w:line="360" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>
          <w:b/>
          <w:sz w:val="28"/>
        </w:rPr>
        <w:t>RESOLUÇÃO OTIMIZADA DO PROBLEMA DO MOTOBOY (BEECROWD 1286) VIA PROGRAMAÇÃO DINÂMICA: ESTUDO DE CASO DA MOCHILA BINÁRIA</w:t>
      </w:r>
    </w:p>

    <!-- AUTOR E AFILIACAO -->
    <w:p>
      <w:pPr>
        <w:jc w:val="center"/>
        <w:spacing w:after="120" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>
          <w:b/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>José Albérico Rocha da Silva</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr>
        <w:jc w:val="center"/>
        <w:spacing w:after="360" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>
          <w:sz w:val="20"/>
        </w:rPr>
        <w:t>Departamento de Computação – Universidade Federal Rural de Pernambuco (UFRPE)</w:t>
      </w:r>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>
          <w:sz w:val="20"/>
        </w:rPr>
        <w:br/>
        <w:t>Disciplina: Projeto e Análise de Algoritmos (PAA) – 2026.2 | Docente: Profª. Drª. Jeane Melo</w:t>
      </w:r>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>
          <w:sz w:val="20"/>
        </w:rPr>
        <w:br/>
        <w:t>Tema: Tema 6 – BeeCrowd Problema 1286: Motoboy</w:t>
      </w:r>
    </w:p>

    <!-- RESUMO -->
    <w:p>
      <w:pPr>
        <w:jc w:val="both"/>
        <w:spacing w:after="120" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>
          <w:b/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>RESUMO</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr>
        <w:jc w:val="both"/>
        <w:spacing w:after="120" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Este artigo apresenta a formulação teórica, a modelagem matemática e a implementação computacional orientada à resolução do problema 1286 (Motoboy) da plataforma BeeCrowd, fundamentando-se nas normas da ABNT para redação científica. O problema modela a tomada de decisão logística de um entregador que visa maximizar o tempo total de trabalho em entregas diárias, condicionado a uma restrição volumétrica de capacidade de transporte de pizzas. Demonstra-se a redução formal deste cenário ao Problema da Mochila Binária (0-1 Knapsack Problem), NP-completo. Avalia-se a inaptidão de heurísticas gulosas e da busca por força bruta, justificando a adoção do paradigma de Programação Dinâmica (Bottom-Up). O algoritmo foi implementado em linguagem Python 3, incorporando a dedução da equação de Bellman e otimização de espaço em memória para complexidade O(P) por meio de varredura decrescente. São fornecidas provas de complexidade assintótica temporal O(N * P), rastreamento analítico elemento a elemento da matriz de estados, recuperação de solução ótima por retrocesso (backtracking), comprovação de aceite experimental no juiz eletrônico e a declaração de integridade acadêmica referente à Portaria nº 2.664/2026 do CNPq.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr>
        <w:jc w:val="both"/>
        <w:spacing w:after="240" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>
          <w:b/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Palavras-chave: </w:t>
      </w:r>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Projeto e análise de algoritmos. Programação dinâmica. Problema da mochila binária. BeeCrowd 1286. Normas ABNT. Python 3.</w:t>
      </w:r>
    </w:p>

    <!-- 1 INTRODUÇÃO -->
    <w:p>
      <w:pPr>
        <w:spacing w:before="240" w:after="120" w:line="360" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>
          <w:b/>
          <w:sz w:val="24"/>
        </w:rPr>
        <w:t>1 INTRODUÇÃO E CONTEXTUALIZAÇÃO DO PROBLEMA</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr>
        <w:jc w:val="both"/>
        <w:ind w:firstLine="720"/>
        <w:spacing w:after="120" w:line="360" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr>
        <w:t>No problema 1286 do BeeCrowd (Motoboy), somos apresentados ao cenário operacional de José, entregador de uma pizzaria que recebe diariamente uma listagem com N pedidos. Cada pedido i possui duas grandezas determinísticas: o tempo de entrega t_i (em minutos), correspondendo ao ganho, e a quantidade de pizzas demandadas p_i, representando a ocupação física. A motocicleta dispõe de uma capacidade máxima de transporte P pizzas. Cada pedido só pode ser atendido de forma integral ou completamente recusado (não é permitida partição). O objetivo consiste em selecionar o subconjunto de pedidos que maximize o tempo total de entregas sem ultrapassar a capacidade P.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr>
        <w:jc w:val="both"/>
        <w:ind w:firstLine="720"/>
        <w:spacing w:after="120" w:line="360" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr>
        <w:t>As aplicações dessa modelagem no mundo real incluem: logística de carregamento de veículos de entrega com restrição de cubagem, alocação de tarefas em máquinas virtuais sob restrição de memória e núcleos de processamento, e seleção ótima de portfólio de investimentos financeiros com orçamento de capital limitado.</w:t>
      </w:r>
    </w:p>

    <!-- 2 MODELAGEM MATEMATICA -->
    <w:p>
      <w:pPr><w:spacing w:before="240" w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="24"/></w:rPr><w:t>2 MODELAGEM MATEMÁTICA DO PROBLEMA</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="both"/><w:ind w:firstLine="720"/><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr><w:t>O problema em estudo mapeia-se de forma isomórfica ao Problema da Mochila Binária (0-1 Knapsack Problem). Seja S = {1, 2, ..., N} o conjunto de pedidos indexados. Para cada pedido i, definem-se o ganho t_i &gt; 0, o peso p_i &gt; 0 e a variável binária x_i em {0, 1}, onde x_i = 1 indica aceite do pedido e x_i = 0 indica recusa.</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="center"/><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:i/><w:sz w:val="24"/></w:rPr><w:t>Maximizar Z = ∑ (t_i · x_i),  sujeito a: ∑ (p_i · x_i) ≤ P,  com x_i ∈ {0, 1}</w:t></w:r>
    </w:p>

    <!-- 3 ANALISE DA TECNICA -->
    <w:p>
      <w:pPr><w:spacing w:before="240" w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="24"/></w:rPr><w:t>3 ANÁLISE DA TÉCNICA: PROGRAMAÇÃO DINÂMICA</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="both"/><w:ind w:firstLine="720"/><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr><w:t>A busca exaustiva (força bruta) incorre em custo exponencial O(2^N). Heurísticas gulosas (como ordenar pela razão t_i / p_i) falham devido à indivisibilidade dos pedidos, gerando capacidade ociosa residual. A Programação Dinâmica resolve essa questão ao satisfazer duas propriedades essenciais: Subestrutura Ótima e Subproblemas Sobrepostos.</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="both"/><w:ind w:firstLine="720"/><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr><w:t>Cada célula DP[i][w] armazena o tempo máximo de entrega considerando os primeiros i pedidos para uma capacidade hipotética w. Os casos base são estritamente nulos: DP[0][w] = 0 (com zero pedidos não há minutos acumulados) e DP[i][0] = 0 (com capacidade zero nenhuma pizza é transportada). A transição de estados de Bellman é governada por:</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="center"/><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr><w:t>DP[i][w] = DP[i-1][w], se p_i &gt; w</w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr><w:br/><w:t>DP[i][w] = max( DP[i-1][w], t_i + DP[i-1][w - p_i] ), se p_i ≤ w</w:t></w:r>
    </w:p>

    <!-- 4 IMPLEMENTACAO COMPUTACIONAL -->
    <w:p>
      <w:pPr><w:spacing w:before="240" w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="24"/></w:rPr><w:t>4 IMPLEMENTAÇÃO COMPUTACIONAL EM PYTHON 3 E DECISÕES DE PROJETO</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="both"/><w:ind w:firstLine="720"/><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr><w:t>Para otimização de memória, a matriz bidimensional (N+1) x (P+1) foi compactada em um único vetor unidimensional de dimensão P+1. O detalhe crítico de engenharia consiste em iterar a capacidade w em ordem decrescente (de P até p_i), garantindo que cada pedido só seja considerado no máximo uma vez por viagem. A leitura rápida é assegurada por sys.stdin.read().split().</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="both"/><w:ind w:firstLine="720"/><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr><w:t>A reconstrução da solução ótima é realizada por retrocesso (Backtracking): partindo da célula final DP[N][P], se DP[i][w] != DP[i-1][w], o pedido i foi obrigatoriamente incluído, decrementando a capacidade w = w - p_i.</w:t></w:r>
    </w:p>

    <!-- 5 COMPLEXIDADE ASSINTOTICA -->
    <w:p>
      <w:pPr><w:spacing w:before="240" w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="24"/></w:rPr><w:t>5 ANÁLISE DE COMPLEXIDADE ASSINTÓTICA</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="both"/><w:ind w:firstLine="720"/><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr><w:t>A complexidade temporal assintótica é Theta(N * P). Por ser proporcional ao valor numérico da capacidade P, é classificada teoricamente como pseudo-polinomial. Para os limites do BeeCrowd (N ≤ 20, P ≤ 30), o algoritmo executa no máximo 600 operações elementares, processadas em menos de 0,001 segundos. A complexidade espacial na versão otimizada é O(P), consumindo apenas 31 inteiros na memória RAM.</w:t></w:r>
    </w:p>

    <!-- 6 RESULTADOS EXPERIMENTAIS -->
    <w:p>
      <w:pPr><w:spacing w:before="240" w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="24"/></w:rPr><w:t>6 RESULTADOS EXPERIMENTAIS E VALIDAÇÃO NO BEECROWD</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="both"/><w:ind w:firstLine="720"/><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr><w:t>No Caso de Teste 1 oficial (N=4, P=10 pizzas; Pedido 1: 20m, 5p; Pedido 2: 70m, 7p; Pedido 3: 15m, 2p; Pedido 4: 25m, 3p), a célula final DP[4][10] atinge 95 minutos. O backtracking recupera os Pedidos #2 e #4, totalizando exatamente 10 pizzas (100% de aproveitamento do baú).</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="both"/><w:ind w:firstLine="720"/><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr><w:t>O algoritmo foi submetido oficialmente ao juiz eletrônico BeeCrowd sob a linguagem Python 3.9:</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:ind w:left="720"/><w:spacing w:after="60" w:line="280" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>• Número da Submissão: # 50429092</w:t></w:r><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:br/><w:t>• Problema: 1286 - Motoboy</w:t></w:r><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:br/><w:t>• Status / Veredito: Accepted</w:t></w:r><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:br/><w:t>• Tempo de Execução: 0.095 segundos (limite permitido: 1.000s)</w:t></w:r><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:br/><w:t>• Tamanho do Código: 2,49 KB</w:t></w:r><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:br/><w:t>• Data e Horário: 07/11/2026 às 10:23:03</w:t></w:r>
    </w:p>

    <!-- 7 CONSIDERACOES FINAIS -->
    <w:p>
      <w:pPr><w:spacing w:before="240" w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="24"/></w:rPr><w:t>7 CONSIDERAÇÕES FINAIS</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="both"/><w:ind w:firstLine="720"/><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="24"/></w:rPr><w:t>O projeto demonstrou a superioridade da Programação Dinâmica sobre algoritmos gulosos e força bruta para a Mochila 0-1, alcançando solução ótima global em tempo pseudo-polinomial com consumo de memória mínimo. O domínio da equação de recorrência e do procedimento de retrocesso consolidam os objetivos formativos da disciplina de Projeto e Análise de Algoritmos.</w:t></w:r>
    </w:p>

    <!-- DECLARACAO CNPQ -->
    <w:p>
      <w:pPr><w:spacing w:before="240" w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="24"/></w:rPr><w:t>DECLARAÇÃO DE USO DE INTELIGÊNCIA ARTIFICIAL GENERATIVA (PORTARIA Nº 2.664/2026 – CNPQ)</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="both"/><w:ind w:firstLine="720"/><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>Em cumprimento ao Artigo 9º da Portaria nº 2.664/2026 do CNPq, declara-se que a ferramenta Google Antigravity / Gemini 3.8 Flash foi utilizada como suporte auxiliar nas etapas de concepção teórica, estruturação da redação segundo normas da ABNT e conferência analítica da complexidade assintótica. A implementação, testes, depuração e validação experimental foram executados e são de integral responsabilidade autoral do discente José Albérico Rocha da Silva.</w:t></w:r>
    </w:p>

    <!-- REFERENCIAS -->
    <w:p>
      <w:pPr><w:spacing w:before="240" w:after="120" w:line="360" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="24"/></w:rPr><w:t>REFERÊNCIAS (CONFORME NORMA ABNT NBR 6023:2018)</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:after="120" w:line="240" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS (ABNT). </w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="22"/></w:rPr><w:t>NBR 6022</w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>: informação e documentação: artigo em publicação periódica técnica e/ou científica: apresentação. Rio de Janeiro: ABNT, 2018.</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:after="120" w:line="240" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>BEECROWD. </w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="22"/></w:rPr><w:t>Problema 1286: Motoboy</w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>. BeeCrowd Academic Online Judge, 2026. Disponível em: https://judge.beecrowd.com/pt/problems/view/1286. Acesso em: 07 nov. 2026.</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:after="120" w:line="240" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>BELLMAN, Richard. The theory of dynamic programming. </w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="22"/></w:rPr><w:t>Bulletin of the American Mathematical Society</w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>, Providence, v. 60, n. 6, p. 503-515, 1954.</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:after="120" w:line="240" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>CONSELHO NACIONAL DE DESENVOLVIMENTO CIENTÍFICO E TECNOLÓGICO (CNPq). </w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="22"/></w:rPr><w:t>Portaria nº 2.664, de 6 de março de 2026</w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>: Diretrizes para uso de Inteligência Artificial Generativa em atividades de pesquisa e submissão acadêmica. Brasília: Ministério da Ciência, Tecnologia e Inovação, 2026.</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:after="120" w:line="240" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>CORMEN, Thomas H. et al. </w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="22"/></w:rPr><w:t>Algoritmos: teoria e prática</w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>. 3. ed. Rio de Janeiro: Elsevier, 2012.</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:after="120" w:line="240" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>KARP, Richard M. Reducibility among combinatorial problems. </w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:i/><w:sz w:val="22"/></w:rPr><w:t>In</w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>: MILLER, Raymond E.; THATCHER, James W. (ed.). </w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="22"/></w:rPr><w:t>Complexity of Computer Computations</w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>. New York: Plenum Press, 1972. p. 85-103.</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:after="120" w:line="240" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>KLEINBERG, Jon; TARDOS, Éva. </w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="22"/></w:rPr><w:t>Algorithm design</w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>. Boston: Pearson/Addison-Wesley, 2006.</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:after="120" w:line="240" w:lineRule="auto"/></w:pPr>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>SOCIEDADE BRASILEIRA DE COMPUTAÇÃO (SBC). </w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="22"/></w:rPr><w:t>Instruções para autores de artigos da SBC</w:t></w:r>
      <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/></w:rPr><w:t>. Porto Alegre: SBC, 2024.</w:t></w:r>
    </w:p>

    <!-- CONFIGURACOES DA PAGINA (MARGENS ABNT: Superior 3cm, Esquerda 3cm, Direita 2cm, Inferior 2cm) -->
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1701" w:right="1134" w:bottom="1134" w:left="1701" w:header="720" w:footer="720" w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>
"""

    content_types_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""

    rels_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

    with zipfile.ZipFile(caminho_saida, 'w', compression=zipfile.ZIP_DEFLATED) as docx:
        docx.writestr('[Content_Types].xml', content_types_xml)
        docx.writestr('_rels/.rels', rels_xml)
        docx.writestr('word/document.xml', document_xml)

    print(f"Arquivo Word (.docx) criado com sucesso em: {caminho_saida}")

if __name__ == "__main__":
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    destino = os.path.join(diretorio_atual, "artigo_abnt_tema6_motoboy.docx")
    criar_docx_abnt(destino)
