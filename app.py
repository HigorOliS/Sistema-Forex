import streamlit as st
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

# ---------------------------
# URL da imagem do fundo
# ---------------------------
img_url = "https://raw.githubusercontent.com/HigorOliS/Sistema-Forex/main/IMG_3894.jpeg"

# ---------------------------
# Fundo com overlay escuro
# ---------------------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{img_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        position: relative;
    }}
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(0,0,0,0.85); /* camada preta translúcida */
        z-index: 0;
    }}
    .block-container {{
        position: relative;
        z-index: 1; /* garante que o conteúdo fique acima do overlay */
    }}
    h1, h2, h3 {{
        color: #FFD700 !important; /* dourado */
        text-shadow: 1px 1px 3px black;
    }}
    .stButton button {{
        background-color: #FFD700;
        color: black;
        border-radius: 8px;
        border: none;
        padding: 0.5em 1em;
        font-weight: bold;
        transition: 0.3s;
    }}
    .stButton button:hover {{
        background-color: black;
        color: #FFD700;
        border: 1px solid #FFD700;
    }}
    table {{
        background-color: #111111 !important;
        color: #FFD700 !important;
        border-collapse: collapse;
        width: 100%;
    }}
    th {{
        background-color: #222222 !important;
        color: #FFD700 !important;
        padding: 8px;
    }}
    td {{
        background-color: #000000 !important;
        padding: 8px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Título
# ---------------------------
st.title("💹 LucroCerto FX")
st.header("💡 Otimize sua Análise")

# ---------------------------
# Upload e observações
# ---------------------------
uploaded_file = st.file_uploader("📤 Envie um print do gráfico da IQ Option")
user_text = st.text_area("✍️ Detalhe aqui sua análise ou observações")

# ---------------------------
# Botão para gerar análise
# ---------------------------
if st.button("✨ Gerar Análise"):
    data = {
        "Par": ["EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "AUD/USD"],
        "Horário": ["10:32:15", "06:15:45", "22:47:30", "04:12:59", "21:03:12"],
        "Ação": [
            '<span style="color:#00FF66">Comprar</span>',
            '<span style="color:#FF3333">Vender</span>',
            '<span style="color:#00FF66">Comprar</span>',
            '<span style="color:#FF3333">Vender</span>',
            '<span style="color:#00FF66">Comprar</span>'
        ],
        "Probabilidade (%)": [92, 89, 94, 90, 91]
    }
    
    df = pd.DataFrame(data)

    st.markdown("## 📈 Resultados da Análise")
    st.write(df.to_html(escape=False), unsafe_allow_html=True)

    st.markdown("## 💡 Dicas de Horários")
    st.write("""
    - **EUR/USD** → Mais preciso entre **10:00 e 12:00 (GMT-3)**.
    - **GBP/USD** → Movimentos fortes entre **05:30 e 07:00**.
    - **USD/JPY** → Boa volatilidade entre **22:00 e 23:30**.
    - **AUD/USD** → Melhor liquidez às **21:00 (abertura Sydney)**.
    - **USD/CHF** → Melhor momento entre **04:00 e 05:00**.
    """)
