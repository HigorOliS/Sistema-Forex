import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="LucroCerto FX", layout="centered", page_icon="💰")

# Definições de estilo (tema preto e dourado)
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #FFD700;
    }
    .stButton button {
        background-color: #FFD700;
        color: #000000;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .logo {
        text-align: center;
        margin-top: 100px;
        margin-bottom: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializa session_state
if "show_results" not in st.session_state:
    st.session_state.show_results = False

# Funções auxiliares
def gerar_sinais():
    # Aqui depois vamos conectar à IA real
    dados = {
        "Par": ["EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "AUD/USD"],
        "Horário": ["10:32:15", "06:15:45", "22:47:30", "04:12:59", "21:03:12"],
        "Ação": ["Buy", "Sell", "Buy", "Sell", "Buy"],
        "Probabilidade (%)": [92, 89, 94, 90, 91]
    }
    return pd.DataFrame(dados)

def dicas_horarios():
    st.markdown("""
    ### 💡 Dicas de Horários
    - **EUR/USD** → Mais preciso entre **10:00 e 12:00** (GMT-3).  
    - **GBP/USD** → Movimentos fortes entre **05:30 e 07:00**.  
    - **USD/JPY** → Boa volatilidade entre **22:00 e 23:30**.  
    - **AUD/USD** → Melhor liquidez às **21:00** (abertura Sydney).  
    - **USD/CHF** → Melhor momento entre **04:00 e 06:00**.  
    """)

# Tela inicial
if not st.session_state.show_results:
    st.markdown('<div class="logo"><h1>💰 LucroCerto FX</h1></div>', unsafe_allow_html=True)
    if st.button("Buscar Sinais"):
        st.session_state.show_results = True
        st.rerun()

# Tela de resultados
else:
    st.title("📊 Resultados da Análise")
    tabela = gerar_sinais()
    st.table(tabela)

    if st.button("🔄 Nova Busca"):
        st.session_state.show_results = False
        st.rerun()

    dicas_horarios()
