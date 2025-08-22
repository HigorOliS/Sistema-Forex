import streamlit as st
import pandas as pd
from PIL import Image

# ---------------------------
# Configuração da página
# ---------------------------
st.set_page_config(
    page_title="LucroCerto FX",
    page_icon="💹",
    layout="wide",
)

# ---------------------------
# Estilo da página com imagem de fundo
# ---------------------------
page_bg = """
<style>
.stApp {
    background: url("https://raw.githubusercontent.com/HigorOliS/Sistema-Forex/main/IMG_3894.jpeg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #FFD700;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0.6);
}
[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.8);
}
.block-container {
    background: rgba(0,0,0,0.7);
    padding: 2rem;
    border-radius: 10px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------------------------
# Cabeçalho
# ---------------------------
st.title("💹 LucroCerto FX")
st.markdown("### 🚀 Scalping de Alta Precisão em Forex")

# ---------------------------
# Upload e observações
# ---------------------------
uploaded_file = st.file_uploader("📤 Envie um print do gráfico da IQ Option")
user_text = st.text_area("✍️ Detalhe aqui sua análise ou observações")

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📊 Seu gráfico enviado", use_column_width=True)

if user_text:
    st.subheader("📝 Observações do Usuário")
    st.write(user_text)

# ---------------------------
# Botão para gerar sinais
# ---------------------------
if st.button("🚀 Gerar Sinais"):
    # Dados de exemplo (futuramente integrados à IA)
    data = {
        "Horário": ["10:01:05", "10:03:15", "10:05:20"],
        "Par": ["EUR/USD", "USD/JPY", "GBP/USD"],
        "Ação": ["Comprar", "Vender", "Comprar"],
        "Acerto (%)": [92, 88, 95]
    }

    df = pd.DataFrame(data)

    # Função para colorir colunas
    def highlight_actions(val):
        if val == "Comprar":
            return "color: lime; font-weight: bold"
        elif val == "Vender":
            return "color: red; font-weight: bold"
        return ""

    styled_df = df.style.map(highlight_actions, subset=["Ação"])
    st.subheader("📊 Sinais Gerados")
    st.dataframe(styled_df, use_container_width=True)
