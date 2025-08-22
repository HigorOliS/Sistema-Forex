import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

# ---------------------------
# Configuração da página
# ---------------------------
st.set_page_config(
    page_title="LucroCerto FX",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Estilo customizado (preto/dourado)
# ---------------------------
st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: #FFD700;
        }
        .stButton>button {
            background-color: #FFD700;
            color: #000000;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Função placeholder de IA para calcular acerto
# ---------------------------
def calcular_acerto(candle_image=None):
    return 90  # Exemplo fixo

# ---------------------------
# Função para colorir Comprar/Vender
# ---------------------------
def color_action(val):
    color = 'green' if val == "Comprar" else 'red'
    return f'background-color: {color}; color: black; font-weight: bold'

# ---------------------------
# Cabeçalho
# ---------------------------
st.title("📊 LucroCerto FX - Scalping")
st.subheader("Tabela de sinais com Acerto (%)")

# ---------------------------
# Upload e observações do usuário
# ---------------------------
st.subheader("📤 Envie seu gráfico ou observações")
uploaded_file = st.file_uploader("📤 Envie um print do gráfico da IQ Option")
user_text = st.text_area("✍️ Detalhe aqui sua análise ou observações")

if uploaded_file:
    user_image = Image.open(uploaded_file)
    st.image(user_image, caption="📊 Seu gráfico enviado", use_column_width=True)

if user_text:
    st.subheader("📝 Observações do Usuário")
    st.write(user_text)

# ---------------------------
# Candle do GitHub
# ---------------------------
st.subheader("📈 Candle Analisado")
url = "https://raw.githubusercontent.com/HigorOliS/Sistema-Forex/main/IMG_3894.jpeg"
response = requests.get(url)
image = Image.open(BytesIO(response.content))
st.image(image, caption="Candle Analisado", use_column_width=True)

# ---------------------------
# Botão para gerar sinais
# ---------------------------
if st.button("🚀 Gerar Sinais"):
    # Lista de sinais de exemplo; futuramente pode vir de API
    sinais_base = [
        {"Horário": "08:00:00", "Par": "EUR/USD", "Ação": "Comprar"},
        {"Horário": "08:15:00", "Par": "USD/JPY", "Ação": "Vender"},
        {"Horário": "08:30:00", "Par": "GBP/USD", "Ação": "Comprar"}
    ]

    df = pd.DataFrame(sinais_base)
    # Calcular Acerto (%)
    df["Acerto (%)"] = df["Par"].apply(lambda x: calcular_acerto(None))

    # Aplicar estilo
    styled_df = df.style.applymap(color_action, subset=['Ação']) \
                        .set_properties(**{'color': '#FFD700', 'background-color': '#000000'})

    # Mostrar tabela
    st.subheader("📊 Sinais Gerados")
    st.dataframe(styled_df)
