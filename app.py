import streamlit as st
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

# ---------------------------
# URL da imagem do GitHub
# ---------------------------
img_url = "https://raw.githubusercontent.com/HigorOliS/Sistema-Forex/main/IMG_3894.jpeg"

# ---------------------------
# Carregando a imagem
# ---------------------------
try:
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    st.image(img, caption="Gráfico carregado do GitHub")
except Exception as e:
    st.error(f"Erro ao carregar a imagem: {e}")

# ---------------------------
# Configuração do background
# ---------------------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{img_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Título e cabeçalhos
# ---------------------------
st.title("💹 LucroCerto FX")
st.header("💡 Otimize sua Análise")

# ---------------------------
# Upload de arquivo e texto
# ---------------------------
uploaded_file = st.file_uploader("📤 Envie um print do gráfico da IQ Option")
user_text = st.text_area("✍️ Detalhe aqui sua análise ou observações")

# ---------------------------
# Botão para gerar análise
# ---------------------------
if st.button("Gerar Análise"):
    # Dados de exemplo
    data = {
        "Par": ["EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "AUD/USD"],
        "Horário": ["10:32:15", "06:15:45", "22:47:30", "04:12:59", "21:03:12"],
        "Ação": [
            '<span style="color:green">Comprar</span>',
            '<span style="color:red">Vender</span>',
            '<span style="color:green">Comprar</span>',
            '<span style="color:red">Vender</span>',
            '<span style="color:green">Comprar</span>'
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
