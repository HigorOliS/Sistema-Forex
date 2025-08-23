import streamlit as st
import pandas as pd
from PIL import Image
import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

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
st.markdown("### 🚀 Forex com IA em Tempo Real")

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
# Chave da OpenAI
# ---------------------------
openai_api_key = st.secrets.get("OPENAI_API_KEY", None)
client = OpenAI(api_key=openai_api_key) if openai_api_key else None

# ---------------------------
# Botão para gerar sinais
# ---------------------------
if st.button("🚀 Gerar Sinais"):
    # Dados de exemplo (depois a IA pode gerar isso também)
    data = {
        "Horário": ["10:01:05", "10:03:15", "10:05:20"],
        "Par": ["EUR/USD", "USD/JPY", "GBP/USD"],
        "Ação": ["Comprar", "Vender", "Comprar"],
        "Acerto (%)": [92, 88, 95]
    }

    df = pd.DataFrame(data, columns=["Horário", "Par", "Ação", "Acerto (%)"])

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

    # ---------------------------
    # Geração de dicas inteligentes via IA
    # ---------------------------
    if client:
        signals_text = df.to_string(index=False)
        user_notes = user_text if user_text else "Nenhuma observação"

        prompt = f"""
        Você é um assistente especializado em Forex.
        O usuário acabou de gerar sinais de scalping.
        Aqui estão os sinais:

        {signals_text}

        Observações do usuário:
        {user_notes}

        Gere 3 a 4 dicas curtas e práticas, em português, personalizadas
        para este cenário. Seja direto e útil, nada genérico.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um trader profissional especialista em Forex scalping."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )

        dicas = response.choices[0].message.content
        st.markdown("---")
        st.subheader("💡 Dicas Inteligentes (IA)")
        st.markdown(dicas)
    else:
        st.warning("⚠️ Configure sua chave da OpenAI em `st.secrets['OPENAI_API_KEY']` para ativar as dicas inteligentes.")
