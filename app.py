import streamlit as st
import pandas as pd
from PIL import Image

# ---------------------------
# Configuração da página
# ---------------------------
st.set_page_config(page_title="LucroCerto FX", layout="wide")

# Fundo com imagem escurecida
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(
            rgba(0, 0, 0, 0.75),
            rgba(0, 0, 0, 0.75)
        ), url("https://raw.githubusercontent.com/HigorOliS/Sistema-Forex/main/IMG_3894.jpeg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    table {
        background-color: rgba(0,0,0,0.6);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💹 LucroCerto FX")

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
# Botão para gerar análise
# ---------------------------
if st.button("🚀 Gerar Análise"):
    # Dados fictícios de exemplo (simulação)
    data = {
        "Par": ["EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "AUD/USD"],
        "Horário": ["10:32:15", "06:15:45", "22:47:30", "04:12:59", "21:03:12"],
        "Ação": ["Comprar", "Vender", "Comprar", "Vender", "Comprar"],
        "Acerto(%)": [92, 89, 94, 90, 91]
    }
    df = pd.DataFrame(data)

    # Função para aplicar cor automaticamente
    def color_action(val):
        if val == "Comprar":
            return "color: lime; font-weight: bold;"
        elif val == "Vender":
            return "color: red; font-weight: bold;"
        return ""

    styled_df = df.style.applymap(color_action, subset=["Ação"])

    # Mostrar tabela
    st.markdown("## 📈 Resultados da Análise")
    st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)

    # Dicas de horários
    st.markdown("## 💡 Dicas de Horários")
    st.write("""
    - **EUR/USD** → Mais preciso entre **10:00 e 12:00 (GMT-3)**.
    - **GBP/USD** → Movimentos fortes entre **05:30 e 07:00**.
    - **USD/JPY** → Boa volatilidade entre **22:00 e 23:30**.
    - **AUD/USD** → Melhor liquidez às **21:00 (abertura Sydney)**.
    - **USD/CHF** → Melhor momento entre **04:00 e 05:00**.
    """)
