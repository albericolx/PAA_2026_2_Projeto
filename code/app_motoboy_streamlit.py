# -*- coding: utf-8 -*-
"""
===============================================================================
Universidade Federal Rural de Pernambuco (UFRPE)
Departamento de Computacao - PAA (Projeto e Analise de Algoritmos)
Professora: Jeane Melo
Projeto VA2 - Tema 6: BeeCrowd 1286 - Motoboy
Tecnica: Programacao Dinamica (Problema da Mochila 0-1)
Linguagem: Python 3 com Streamlit
Autor: Jose Alberico Rocha da Silva (autor)
===============================================================================
Inclui demonstracao passo a passo do BACKTRACKING com a mesma riqueza didatica:
- Comparacao de DP[i][w] != DP[i-1][w];
- Explicacao da deducao logica;
- Atualizacao da capacidade residual da mochila;
- Destaque das celulas e dos pedidos escolhidos.
===============================================================================
"""

import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Simulador Didatico: Motoboy (PAA - UFRPE)",
    page_icon="🍕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilizacao visual compacta para caber em tela unica
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem !important; padding-bottom: 0rem !important;
        padding-left: 1.5rem !important; padding-right: 1.5rem !important;
    }
    header[data-testid="stHeader"] { display: none; }
    
    .titulo-compacto {
        font-size: 20px; font-weight: bold; color: #60a5fa; margin: 0 0 2px 0;
        display: flex; align-items: center; justify-content: space-between;
    }

    .metric-card-lateral {
        background: linear-gradient(135deg, #1e3a8a, #2563eb);
        color: white; padding: 6px 10px; border-radius: 6px; text-align: center;
        margin-top: 8px; margin-bottom: 8px;
    }
    .metric-val-lat { font-size: 20px; font-weight: bold; line-height: 1.1; }
    .metric-lbl-lat { font-size: 9px; opacity: 0.9; text-transform: uppercase; }

    /* Caixa da Recorrencia Compacta */
    .recorrencia-box-compacta {
        background-color: #0b1329; border: 1px solid #334155;
        border-radius: 6px; padding: 6px 12px; margin-bottom: 8px; color: #f8fafc; font-size: 11px;
    }
    .ramo-ativo-c {
        background-color: #1e293b; border-left: 4px solid #f59e0b;
        padding: 4px 10px; border-radius: 4px; margin: 3px 0;
    }
    .ramo-ativo-bt {
        background-color: #1e1b4b; border-left: 4px solid #8b5cf6;
        padding: 6px 12px; border-radius: 4px; margin: 4px 0;
    }
    .ramo-inativo-c { padding: 2px 10px; opacity: 0.35; font-size: 10px; }
    .badge-ramo-c {
        background: #f59e0b; color: #000; padding: 1px 6px; border-radius: 3px;
        font-weight: bold; font-size: 10px;
    }
    .badge-ramo-bt {
        background: #8b5cf6; color: #fff; padding: 1px 6px; border-radius: 3px;
        font-weight: bold; font-size: 10px;
    }

    .detalhe-calculo-compacto {
        background: #020617; border: 1px solid #38bdf8;
        border-radius: 6px; padding: 6px 12px; margin-bottom: 8px;
        font-size: 11px; line-height: 1.45;
    }
    .detalhe-bt-compacto {
        background: #030712; border: 2px solid #8b5cf6;
        border-radius: 6px; padding: 8px 14px; margin-bottom: 8px;
        font-size: 12px; line-height: 1.5; box-shadow: 0 0 10px rgba(139, 92, 246, 0.2);
    }
    .termo-destaque { display: inline-block; padding: 1px 6px; border-radius: 3px; font-weight: bold; font-size: 11px; }
    .termo-cima { background: #065f46; color: #6ee7b7; }
    .termo-resultado { background: #78350f; color: #fde047; font-size: 12px; }

    .card-lat-sim {
        background: linear-gradient(135deg, #065f46, #059669); color: white;
        padding: 5px 8px; border-radius: 5px; margin-bottom: 4px; border: 1px solid #34d399; font-size: 10px;
    }
    .card-lat-nao {
        background: #1e293b; color: #94a3b8; padding: 4px 8px;
        border-radius: 5px; margin-bottom: 4px; border-left: 3px solid #ef4444; font-size: 10px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DADOS DE SESSAO
# -----------------------------------------------------------------------------
if "dados_pedidos" not in st.session_state:
    st.session_state.dados_pedidos = [
        {"Pedido": 1, "Tempo (min)": 20, "Pizzas": 5},
        {"Pedido": 2, "Tempo (min)": 70, "Pizzas": 7},
        {"Pedido": 3, "Tempo (min)": 15, "Pizzas": 2},
        {"Pedido": 4, "Tempo (min)": 25, "Pizzas": 3}
    ]
    st.session_state.capacidade_p = 10

# -----------------------------------------------------------------------------
# BARRA LATERAL UNIFICADA: CONFIGURACAO + DECISAO FINAL
# -----------------------------------------------------------------------------
st.sidebar.markdown("<h3 style='margin:0; padding:0; font-size:16px;'>⚙️ Controle & Decisão</h3>", unsafe_allow_html=True)
st.sidebar.caption("PAA - UFRPE 2026.2 | Profª Jeane Melo | José Albérico")

modo_predefinido = st.sidebar.selectbox(
    "Carregar Cenário:",
    [
        "Personalizado (Digite os valores)",
        "Caso 1 Oficial BeeCrowd (N=4, P=10)",
        "Caso 2 Oficial BeeCrowd (N=2, P=20)",
        "Caso Didático Simples (N=3, P=5)"
    ],
    label_visibility="collapsed"
)

if modo_predefinido == "Caso 1 Oficial BeeCrowd (N=4, P=10)":
    st.session_state.capacidade_p = 10
    st.session_state.dados_pedidos = [
        {"Pedido": 1, "Tempo (min)": 20, "Pizzas": 5},
        {"Pedido": 2, "Tempo (min)": 70, "Pizzas": 7},
        {"Pedido": 3, "Tempo (min)": 15, "Pizzas": 2},
        {"Pedido": 4, "Tempo (min)": 25, "Pizzas": 3}
    ]
elif modo_predefinido == "Caso 2 Oficial BeeCrowd (N=2, P=20)":
    st.session_state.capacidade_p = 20
    st.session_state.dados_pedidos = [
        {"Pedido": 1, "Tempo (min)": 52, "Pizzas": 9},
        {"Pedido": 2, "Tempo (min)": 10, "Pizzas": 12}
    ]
elif modo_predefinido == "Caso Didático Simples (N=3, P=5)":
    st.session_state.capacidade_p = 5
    st.session_state.dados_pedidos = [
        {"Pedido": 1, "Tempo (min)": 12, "Pizzas": 2},
        {"Pedido": 2, "Tempo (min)": 18, "Pizzas": 3},
        {"Pedido": 3, "Tempo (min)": 24, "Pizzas": 4}
    ]

capacidade_mochila = st.sidebar.number_input("Capacidade Máxima da Mochila (P):", 1, 50, st.session_state.capacidade_p, 1)
qtd_pedidos_input = st.sidebar.number_input("Quantidade de Pedidos Desejada (N):", 1, 15, len(st.session_state.dados_pedidos), 1)

while len(st.session_state.dados_pedidos) < qtd_pedidos_input:
    novo_id = len(st.session_state.dados_pedidos) + 1
    modelos_extras = [(15, 2), (30, 4), (22, 3), (40, 5), (18, 2), (25, 3)]
    tpl = modelos_extras[(novo_id - 1) % len(modelos_extras)]
    st.session_state.dados_pedidos.append({"Pedido": novo_id, "Tempo (min)": tpl[0], "Pizzas": tpl[1]})
while len(st.session_state.dados_pedidos) > qtd_pedidos_input:
    st.session_state.dados_pedidos.pop()

df_pedidos = pd.DataFrame(st.session_state.dados_pedidos)
df_editado = st.sidebar.data_editor(
    df_pedidos,
    num_rows="fixed",
    use_container_width=True,
    hide_index=True,
    height=130
)

lista_pedidos = []
for idx, row in df_editado.iterrows():
    try:
        t = int(row["Tempo (min)"])
        p = int(row["Pizzas"])
        lista_pedidos.append((t, p))
    except Exception:
        lista_pedidos.append((10, 2))

num_pedidos = len(lista_pedidos)

# -----------------------------------------------------------------------------
# PROGRAMACAO DINAMICA
# -----------------------------------------------------------------------------
t_inicio = time.perf_counter()
dp_matriz = [[0 for _ in range(capacidade_mochila + 1)] for _ in range(num_pedidos + 1)]
decisoes_celula = [[{"escolha": "BASE", "cima": 0, "levar": 0} for _ in range(capacidade_mochila + 1)] for _ in range(num_pedidos + 1)]

for i in range(1, num_pedidos + 1):
    tempo_atual, pizzas_atual = lista_pedidos[i - 1]
    for w in range(1, capacidade_mochila + 1):
        valor_cima = dp_matriz[i - 1][w]
        if pizzas_atual <= w:
            valor_levar = dp_matriz[i - 1][w - pizzas_atual] + tempo_atual
            if valor_levar > valor_cima:
                dp_matriz[i][w] = valor_levar
                decisoes_celula[i][w] = {"escolha": "LEVAR", "cima": valor_cima, "levar": valor_levar}
            else:
                dp_matriz[i][w] = valor_cima
                decisoes_celula[i][w] = {"escolha": "DEIXAR", "cima": valor_cima, "levar": valor_levar}
        else:
            dp_matriz[i][w] = valor_cima
            decisoes_celula[i][w] = {"escolha": "EXCESSO", "cima": valor_cima, "levar": -1}

t_fim = time.perf_counter()
tempo_ms = (t_fim - t_inicio) * 1000

# Lista de passos do Backtracking pre-calculada
passos_bt = []
w_bt = capacidade_mochila
pedidos_escolhidos_finais = []
for i in range(num_pedidos, 0, -1):
    cur_v = dp_matriz[i][w_bt]
    cima_v = dp_matriz[i - 1][w_bt]
    ped = lista_pedidos[i - 1]
    foi_levado = (cur_v != cima_v)
    if foi_levado:
        w_depois = w_bt - ped[1]
        ganho_rest = dp_matriz[i - 1][w_depois]
        justificativa_texto = (
            f"<b>Por que escolheu o Pedido #{i}?</b> Sem ele, o melhor tempo com capacidade {w_bt} pizzas era {cima_v} min. "
            f"Ao incluir o Pedido #{i} ({ped[0]}m, {ped[1]}pz), somamos seu tempo com a melhor solução para o espaço restante "
            f"({w_depois} pizzas &rarr; DP[{i-1}][{w_depois}] = {ganho_rest}m), obtendo <b>{cur_v} min</b> ({ganho_rest} + {ped[0]}), superando os {cima_v} min!"
        )
    else:
        w_depois = w_bt
        justificativa_texto = (
            f"<b>Por que descartou o Pedido #{i}?</b> A inclusão deste pedido ({ped[0]}m, {ped[1]}pz) não superaria os "
            f"<b>{cima_v} min</b> que já haviam sido garantidos pelos pedidos anteriores para essa mesma capacidade residual de {w_bt} pizzas. "
            f"Logo, a melhor decisão para maximizar o tempo foi deixá-lo de fora."
        )
    passos_bt.append({
        "i": i,
        "w_antes": w_bt,
        "cur_v": cur_v,
        "cima_v": cima_v,
        "tempo": ped[0],
        "pizzas": ped[1],
        "foi_levado": foi_levado,
        "w_depois": w_depois,
        "justificativa": justificativa_texto
    })
    if foi_levado:
        pedidos_escolhidos_finais.append(i)
        w_bt -= ped[1]

pedidos_escolhidos_finais.reverse()
pizzas_utilizadas = sum(lista_pedidos[i - 1][1] for i in pedidos_escolhidos_finais)
tempo_maximo_obtido = dp_matriz[num_pedidos][capacidade_mochila]

# -----------------------------------------------------------------------------
# CONTINUACAO LATERAL: RESULTADO DA DECISAO COMPACTO
# -----------------------------------------------------------------------------
st.sidebar.markdown(f"""
<div class="metric-card-lateral">
    <div class="metric-lbl-lat">Tempo Otimizado</div>
    <div class="metric-val-lat">{tempo_maximo_obtido} min.</div>
    <div style="font-size: 10px;">Mochila: <b>{pizzas_utilizadas} / {capacidade_mochila} pizzas</b></div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<div style='font-size:10px; font-weight:bold; color:#94a3b8; margin-bottom:2px;'>Status dos Pedidos:</div>", unsafe_allow_html=True)
for idx in range(1, num_pedidos + 1):
    t_ped, p_ped = lista_pedidos[idx - 1]
    if idx in pedidos_escolhidos_finais:
        st.sidebar.markdown(f"""
        <div class="card-lat-sim">
            <b>✅ Pedido #{idx} (LEVAR)</b>: {t_ped} min | {p_ped} pz
        </div>
        """, unsafe_allow_html=True)
    else:
        st.sidebar.markdown(f"""
        <div class="card-lat-nao">
            <b>❌ Pedido #{idx} (DEIXAR)</b>: {t_ped} min | {p_ped} pz
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# AREA PRINCIPAL COM ABAS PARA MATRIZ E BACKTRACKING PASSO A PASSO
# -----------------------------------------------------------------------------
st.markdown("""
<div class="titulo-compacto">
    <span>🍕 Simulador Didático: Problema do Motoboy (BeeCrowd 1286)</span>
    <span style="font-size: 12px; background: #1e3a8a; padding: 2px 8px; border-radius: 4px;">Programação Dinâmica</span>
</div>
""", unsafe_allow_html=True)

aba_matriz, aba_bt, aba_todas_matriz = st.tabs([
    "🔍 1. Construção da Matriz Passo a Passo",
    "🔄 2. Retrocesso (Backtracking) Passo a Passo",
    "📋 3. Matriz Completa Finalizada"
])

# -----------------------------------------------------------------------------
# ABA 1: CONSTRUCAO DA MATRIZ PASSO A PASSO
# -----------------------------------------------------------------------------
with aba_matriz:
    total_passos = num_pedidos * capacidade_mochila
    if "passo_atual" not in st.session_state:
        st.session_state.passo_atual = 1
    if st.session_state.passo_atual > total_passos:
        st.session_state.passo_atual = total_passos

    col_b1, col_b2, col_b3, col_b4 = st.columns([1, 1, 1, 3])
    with col_b1:
        if st.button("◀ Voltar Célula", use_container_width=True):
            if st.session_state.passo_atual > 1:
                st.session_state.passo_atual -= 1
    with col_b2:
        if st.button("Avançar Célula ▶", use_container_width=True):
            if st.session_state.passo_atual < total_passos:
                st.session_state.passo_atual += 1
    with col_b3:
        if st.button("⚡ Ir para o Fim", use_container_width=True):
            st.session_state.passo_atual = total_passos
    with col_b4:
        passo_slider = st.slider(
            "Navegador de Células:", 1, total_passos, st.session_state.passo_atual, 1,
            label_visibility="collapsed"
        )
        st.session_state.passo_atual = passo_slider

    idx_lin = 1
    i_alvo, w_alvo = 1, 1
    for i_s in range(1, num_pedidos + 1):
        for w_s in range(1, capacidade_mochila + 1):
            if idx_lin == st.session_state.passo_atual:
                i_alvo, w_alvo = i_s, w_s
                break
            idx_lin += 1
        if idx_lin > st.session_state.passo_atual:
            break

    tempo_p, pizzas_p = lista_pedidos[i_alvo - 1]
    cabe_na_mochila = (pizzas_p <= w_alvo)
    val_cima = dp_matriz[i_alvo - 1][w_alvo]

    col_rec, col_cards_info = st.columns([1.1, 1.3])
    with col_rec:
        if not cabe_na_mochila:
            st.markdown(f"""
            <div class="recorrencia-box-compacta">
                <div style="font-weight: bold; color: #94a3b8; font-size: 10px;">📐 1. FUNÇÃO DE RECORRÊNCIA:</div>
                <div class="ramo-ativo-c">
                    <span class="badge-ramo-c">ATIVO: CASO 1 (NÃO CABE)</span><br>
                    <b>Condição:</b> $p_{{{i_alvo}}} = {pizzas_p} > w = {w_alvo}$ pizzas &implies; <code>DP[i][w] = DP[i-1][w]</code><br>
                    <i>O pedido excede a bag; mantém a melhor solução anterior.</i>
                </div>
                <div class="ramo-inativo-c">Caso 2: $p_i \\le w \\implies \\max(DP[i-1][w], \\; DP[i-1][w-p_i] + t_i)$</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="recorrencia-box-compacta">
                <div style="font-weight: bold; color: #94a3b8; font-size: 10px;">📐 1. FUNÇÃO DE RECORRÊNCIA:</div>
                <div class="ramo-inativo-c">Caso 1: $p_i > w \\implies DP[i-1][w]$</div>
                <div class="ramo-ativo-c">
                    <span class="badge-ramo-c">ATIVO: CASO 2 (CABE NA BAG)</span><br>
                    <b>Condição:</b> $p_{{{i_alvo}}} = {pizzas_p} \\le w = {w_alvo}$ &implies; <code>max( DP[i-1][w], &nbsp; DP[i-1][w - p_i] + t_i )</code><br>
                    <i>Avalia racionalmente: não levar vs levar com espaço restante.</i>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_cards_info:
        c_info1, c_info2, c_info3 = st.columns(3)
        c_info1.info(f"**Item Analisado:**\n\nPedido #{i_alvo} ({tempo_p}m, {pizzas_p}pz)")
        c_info2.warning(f"**Opção 1 (Cima):**\n\n`DP[{i_alvo-1}][{w_alvo}]` = **{val_cima}m**")
        if cabe_na_mochila:
            w_rest = w_alvo - pizzas_p
            val_rest = dp_matriz[i_alvo - 1][w_rest]
            val_levar = val_rest + tempo_p
            c_info3.success(f"**Opção 2 (Levar):**\n\n`DP[{i_alvo-1}][{w_rest}]`+{tempo_p}m = **{val_levar}m**")
        else:
            c_info3.error(f"**Opção 2 (Levar):**\n\nNão cabe ({pizzas_p}pz > {w_alvo})")

    if not cabe_na_mochila:
        st.markdown(f"""
        <div class="detalhe-calculo-compacto">
            <b>2. Substituição no Cálculo de DP[{i_alvo}][{w_alvo}]:</b> &nbsp;
            $p_{{{i_alvo}}} = {pizzas_p} > w = {w_alvo}$ &implies; 
            <code>DP[{i_alvo}][{w_alvo}] = DP[{i_alvo - 1}][{w_alvo}] = </code> <span class="termo-destaque termo-cima">{val_cima} min</span> &implies;
            <b>Resultado:</b> <span class="termo-destaque termo-resultado">{dp_matriz[i_alvo][w_alvo]} min</span> &nbsp;
            (Decisão: <b>DEIXAR O PEDIDO</b> - excede a mochila).
        </div>
        """, unsafe_allow_html=True)
    else:
        vencedor = "LEVAR O PEDIDO" if val_levar > val_cima else "DEIXAR O PEDIDO"
        cor_venc = "#34d399" if val_levar > val_cima else "#f59e0b"
        motivo = "Levar este pedido gera maior ganho global!" if val_levar > val_cima else "Manter a escolha anterior gera maior tempo acumulado."
        st.markdown(f"""
        <div class="detalhe-calculo-compacto">
            <b>2. Substituição no Cálculo de DP[{i_alvo}][{w_alvo}]:</b> &nbsp;
            <code>max( DP[{i_alvo-1}][{w_alvo}] ({val_cima}m), &nbsp; DP[{i_alvo-1}][{w_rest}] + {tempo_p}m ({val_levar}m) )</code> = 
            <span class="termo-destaque termo-resultado">{dp_matriz[i_alvo][w_alvo]} min</span> &nbsp;|&nbsp;
            <b>Decisão:</b> <span style="color: {cor_venc}; font-weight: bold;">{vencedor}</span> ({motivo})
        </div>
        """, unsafe_allow_html=True)

    matriz_atual = [[0 for _ in range(capacidade_mochila + 1)] for _ in range(num_pedidos + 1)]
    idx_cur = 1
    for i_s in range(1, num_pedidos + 1):
        for w_s in range(1, capacidade_mochila + 1):
            if idx_cur <= st.session_state.passo_atual:
                matriz_atual[i_s][w_s] = dp_matriz[i_s][w_s]
            else:
                matriz_atual[i_s][w_s] = "-"
            idx_cur += 1

    colunas_tab = [f"w={w}" for w in range(capacidade_mochila + 1)]
    rotulos_tab = ["Base 0"] + [f"P{i} ({t}m, {p}pz)" for i, (t, p) in enumerate(lista_pedidos, 1)]
    st.dataframe(pd.DataFrame(matriz_atual, index=rotulos_tab, columns=colunas_tab), use_container_width=True, height=170)

# -----------------------------------------------------------------------------
# ABA 2: RETROCESSO (BACKTRACKING) PASSO A PASSO
# -----------------------------------------------------------------------------
with aba_bt:
    st.markdown("""
    <div style="font-size:12px; margin-bottom: 6px;">
        <b>Reconstrução da Solução Ótima (Backtracking):</b> Analisa os pedidos de trás para frente (do Pedido #N até #1) 
        verificando se o valor mudou em relação à linha superior.
    </div>
    """, unsafe_allow_html=True)

    total_passos_bt = len(passos_bt)
    if "passo_bt_atual" not in st.session_state:
        st.session_state.passo_bt_atual = 1

    col_bt1, col_bt2, col_bt3 = st.columns([1, 1, 2])
    with col_bt1:
        if st.button("◀ Passo Anterior (BT)", use_container_width=True):
            if st.session_state.passo_bt_atual > 1:
                st.session_state.passo_bt_atual -= 1
    with col_bt2:
        if st.button("Avançar Backtracking ▶", use_container_width=True):
            if st.session_state.passo_bt_atual < total_passos_bt:
                st.session_state.passo_bt_atual += 1
    with col_bt3:
        st.markdown(f"**Progresso no Backtracking:** Passo **{st.session_state.passo_bt_atual}** de **{total_passos_bt}** pedidos auditados.")

    p_bt = passos_bt[st.session_state.passo_bt_atual - 1]

    # Painel de Regra do Backtracking com o ramo ativo iluminado
    if p_bt["foi_levado"]:
        st.markdown(f"""
        <div class="recorrencia-box-compacta">
            <div style="font-weight: bold; color: #c084fc; font-size: 11px;">🔄 REGRA DE AUDITORIA DO BACKTRACKING:</div>
            <div class="ramo-ativo-bt">
                <span class="badge-ramo-bt">RAMO ATIVO: DP[i][w] != DP[i-1][w]</span><br>
                <b>Condição:</b> Célula atual <code>DP[{p_bt['i']}][{p_bt['w_antes']}] = {p_bt['cur_v']}</code> &ne; Célula superior <code>DP[{p_bt['i']-1}][{p_bt['w_antes']}] = {p_bt['cima_v']}</code><br>
                <b>Conclusão Matemática:</b> O valor aumentou! Logo, <b>O PEDIDO #{p_bt['i']} FOI OBRIGATORIAMENTE LEVADO!</b>
            </div>
            <div class="ramo-inativo-c">Ramo Inativo: Se DP[i][w] == DP[i-1][w] &implies; Descartado (Inativo)</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="recorrencia-box-compacta">
            <div style="font-weight: bold; color: #c084fc; font-size: 11px;">🔄 REGRA DE AUDITORIA DO BACKTRACKING:</div>
            <div class="ramo-inativo-c">Ramo Inativo: Se DP[i][w] != DP[i-1][w] &implies; Levado (Inativo)</div>
            <div class="ramo-ativo-bt">
                <span class="badge-ramo-bt">RAMO ATIVO: DP[i][w] == DP[i-1][w]</span><br>
                <b>Condição:</b> Célula atual <code>DP[{p_bt['i']}][{p_bt['w_antes']}] = {p_bt['cur_v']}</code> == Célula superior <code>DP[{p_bt['i']-1}][{p_bt['w_antes']}] = {p_bt['cima_v']}</code><br>
                <b>Conclusão Matemática:</b> Valores idênticos! O ótimo já existia sem este pedido; logo, <b>O PEDIDO #{p_bt['i']} FOI DESCARTADO!</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Detalhamento do cálculo do Backtracking
    if p_bt["foi_levado"]:
        st.markdown(f"""
        <div class="detalhe-bt-compacto">
            <b>Passo #{st.session_state.passo_bt_atual} | Auditando Pedido #{p_bt['i']} ({p_bt['tempo']}m, {p_bt['pizzas']} pizzas):</b><br>
            • <b>Comparação:</b> <code>DP[{p_bt['i']}][{p_bt['w_antes']}] ({p_bt['cur_v']}m) &ne; DP[{p_bt['i']-1}][{p_bt['w_antes']}] ({p_bt['cima_v']}m)</code> &rarr; <b>DIFERENTES!</b><br>
            • <b>Ação:</b> <span style="color: #34d399; font-weight: bold;">✅ PEDIDO #{p_bt['i']} ESCOLHIDO PARA A MOTO</span>.<br>
            • <b>Por que escolheu?</b> {p_bt['justificativa']}<br>
            • <b>Atualização da Mochila:</b> Consome {p_bt['pizzas']} pizzas: <code>w = {p_bt['w_antes']} - {p_bt['pizzas']} = {p_bt['w_depois']} pizzas</code> &rarr; Sobe para Pedido #{p_bt['i']-1} com {p_bt['w_depois']} pizzas.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="detalhe-bt-compacto">
            <b>Passo #{st.session_state.passo_bt_atual} | Auditando Pedido #{p_bt['i']} ({p_bt['tempo']}m, {p_bt['pizzas']} pizzas):</b><br>
            • <b>Comparação:</b> <code>DP[{p_bt['i']}][{p_bt['w_antes']}] ({p_bt['cur_v']}m) == DP[{p_bt['i']-1}][{p_bt['w_antes']}] ({p_bt['cima_v']}m)</code> &rarr; <b>IGUAIS!</b><br>
            • <b>Ação:</b> <span style="color: #ef4444; font-weight: bold;">❌ PEDIDO #{p_bt['i']} DESCARTADO</span>.<br>
            • <b>Por que descartou?</b> {p_bt['justificativa']}<br>
            • <b>Atualização da Mochila:</b> Mantém <code>w = {p_bt['w_depois']} pizzas</code> &rarr; Sobe para Pedido #{p_bt['i']-1} com {p_bt['w_depois']} pizzas.
        </div>
        """, unsafe_allow_html=True)

    # Exibe a Matriz Completa com destaque das células auditadas
    colunas_todas = [f"w={w}" for w in range(capacidade_mochila + 1)]
    rotulos_todos = ["Base 0"] + [f"P{i} ({t}m, {p}pz)" for i, (t, p) in enumerate(lista_pedidos, 1)]
    st.dataframe(pd.DataFrame(dp_matriz, index=rotulos_todos, columns=colunas_todas), use_container_width=True, height=190)

# -----------------------------------------------------------------------------
# ABA 3: MATRIZ COMPLETA FINALIZADA
# -----------------------------------------------------------------------------
with aba_todas_matriz:
    colunas_todas = [f"w={w}" for w in range(capacidade_mochila + 1)]
    rotulos_todos = ["Base 0"] + [f"P{i} ({t}m, {p}pz)" for i, (t, p) in enumerate(lista_pedidos, 1)]
    st.dataframe(pd.DataFrame(dp_matriz, index=rotulos_todos, columns=colunas_todas), use_container_width=True, height=320)
