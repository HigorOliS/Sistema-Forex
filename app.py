import streamlit as st
import pandas as pd
import random

# ==============================
# CONFIGURAÇÃO DA PÁGINA
# ==============================
st.set_page_config(page_title="LucroCerto FX", layout="centered")

# Estilo customizado com CSS
st.markdown("""
    <style>
        .main {
            background-color: #000000;
            color: #FFD700;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            margin-top: 10px;
            margin-bottom: 30px;
        }
        .stButton button {
            background-color: #FFD700;
            color: #000000;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px;
            width: 100%;
        }
        .buy {
            color: #00FF00;
            font-weight: bold;
        }
        .sell {
            color: #FF0000;
            font-weight: bold;
        }
        .section {
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# ==============================
# TELA 1
# ==============================
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.markdown("<div class='title'>💹 LucroCerto FX</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Seu assistente inteligente para Forex</div>", unsafe_allow_html=True)

    # Caixa de texto
    user_input = st.text_area(
        "Otimize sua análise com IA:",
        placeholder="Descreva o cenário do gráfico (ex.: tendência, rompimento, suporte/resistência)",
        height=100
    )

    # Upload do print (opcional)
    uploaded_file = st.file_uploader("Envie um print do gráfico (opcional):", type=["png", "jpg", "jpeg"])

    if st.button("🚀 Gerar Sinais com IA"):
        st.session_state.page = "result"
        st.session_state.user_input = user_input

# ==============================
# TELA 2
# ==============================
elif st.session_state.page == "result":
    st.markdown("<div class='title'>📊 Resultados da Análise</div>", unsafe_allow_html=True)

    # Gerando sinais fictícios
    pares = ["EUR/USD", "USD/JPY", "GBP/USD", "USD/CHF", "AUD/USD"]
    horarios = ["10:32:15", "11:15:47", "14:05:30", "16:45:10", "19:20:05"]
    acoes = ["Comprar", "Vender"]

    data = []
    for par, h in zip(pares, horarios):
        acao = random.choice(acoes)
        prob = random.randint(85, 98)
        data.append([par, h, acao, prob])

    df = pd.DataFrame(data, columns=["Par", "Horário", "Ação", "Probabilidade (%)"])

    # Estilizando tabela
    def color_action(val):
        if val == "Comprar":
            return "color: #00FF00; font-weight: bold;"
        elif val == "Vender":
            return "color: #FF0000; font-weight: bold;"
        return ""

    st.dataframe(df.style.map(color_action, subset=["Ação"]))

    # Dicas
    st.markdown("<div class='section'><h3>💡 Dicas de Horários</h3></div>", unsafe_allow_html=True)
    st.markdown("""
    • EUR/USD → Mais preciso entre 10:00 e 12:00  
    • GBP/USD → Movimentos fortes entre 05:30 e 07:00  
    • USD/JPY → Melhor análise entre 21:00 e 23:00  
    • AUD/USD → Alta liquidez entre 22:00 e 00:00  
    • USD/CHF → Mais previsível entre 09:00 e 11:00  
    """)

    # Comentário do usuário
    if st.session_state.user_input.strip() != "":
        st.markdown("<div class='section'><h3>💡 Comentário da sua Análise</h3></div>", unsafe_allow_html=True)
        st.success(st.session_state.user_input)

    # Botão de reinício
    if st.button("🔄 Nova Análise"):
        st.session_state.page = "home"
