import streamlit as st
import pandas as pd
from PIL import Image
import openai

# ---------------------------
# Configuração da página
# ---------------------------
st.set_page_config(page_title="LucroCerto FX", page_icon="💹", layout="centered")

# ---------------------------
# Chave da API da OpenAI
# ---------------------------
openai.api_key = st.secrets.get("OPENAI_API_KEY", None)

# ---------------------------
# Layout principal
# ---------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: gold;'>Assistente Forex com IA</h1>
    <p style='text-align: center; color: white;'>
    Este é o seu assistente inteligente para ajudar no Forex em tempo real.
    </p>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Entrada de pergunta
# ---------------------------
user_input = st.text_input("Digite sua pergunta:", placeholder="Qual a melhor entrada para EUR/USD agora?")

if st.button("Consultar IA"):
    if openai.api_key and user_input.strip():
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um trader profissional especialista em Forex scalping."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=200,
            temperature=0.7
        )
        st.success(response.choices[0].message.content)
    else:
        st.warning("⚠️ Configure sua chave da OpenAI em `st.secrets['OPENAI_API_KEY']` para ativar esta função.")

# ---------------------------
# Upload de imagem (print gráfico)
# ---------------------------
st.markdown("### 📤 Envie um print do gráfico da IQ Option")
uploaded_file = st.file_uploader("Drag and drop file here", type=["png", "jpg", "jpeg"])

# ---------------------------
# Caixa de Detalhes + Assistente IA
# ---------------------------
st.markdown("### 📝 Detalhe aqui sua análise ou observações")
user_text = st.text_area("Assistente:", placeholder="Digite sua análise, observações ou peça dicas inteligentes...")

# ---------------------------
# Exemplo de tabela de sinais
# ---------------------------
data = {
    "Horário": ["10:00:05", "10:05:10", "10:10:20"],
    "Ação": ["Buy", "Sell", "Buy"],
    "Par": ["EUR/USD", "GBP/USD", "USD/JPY"],
    "Probabilidade": ["92%", "90%", "95%"]
}
df = pd.DataFrame(data)

st.markdown("### 📊 Sinais de Scalping (Exemplo)")
st.dataframe(df, use_container_width=True)

# ---------------------------
# IA gera dicas inteligentes
# ---------------------------
if openai.api_key:
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

    response = openai.chat.completions.create(
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
