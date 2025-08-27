import streamlit as st
import pandas as pd
from PIL import Image
from openai import OpenAI

# ---------------------------
# Configuração da página
# ---------------------------
st.set_page_config(page_title="Assistente Forex com IA", page_icon="📈", layout="wide")

# Conexão com a API da OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------------------------
# Layout Principal (mantido no estilo original)
# ---------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: gold;'>Assistente Forex com IA</h1>
    <p style='text-align: center; color: white;'>
    Este é o seu assistente inteligente para ajudar no Forex em tempo real.
    </p>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Caixa de pergunta principal
# ---------------------------
pergunta = st.text_input("Digite sua pergunta:", "Qual a melhor entrada para EUR/USD agora?")

if st.button("Consultar IA"):
    with st.spinner("Consultando a IA..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um especialista em Forex e scalping. Responda de forma clara, direta e com foco em alta precisão."},
                    {"role": "user", "content": pergunta}
                ]
            )
            resultado = response.choices[0].message.content
            st.markdown(f"✅ **Resposta da IA:**\n\n{resultado}")
        except Exception as e:
            st.error(f"Erro ao consultar IA: {e}")

# ---------------------------
# Upload do gráfico
# ---------------------------
st.markdown("### 📩 Envie um print do gráfico da IQ Option")
uploaded_file = st.file_uploader("Arraste ou selecione o arquivo", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📊 Gráfico enviado", use_column_width=True)

# ---------------------------
# Anotações / Observações
# ---------------------------
st.markdown("### 📝 Detalhe aqui sua análise ou observações")
observacoes = st.text_area("Escreva suas anotações aqui...")

# ---------------------------
# Geração de dicas inteligentes com IA
# ---------------------------
if observacoes:
    with st.spinner("Gerando dicas inteligentes..."):
        try:
            dicas = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um especialista em Forex. Analise as observações do usuário e sugira 3 dicas práticas e estratégicas para melhorar suas entradas no mercado."},
                    {"role": "user", "content": observacoes}
                ]
            )
            st.subheader("💡 Dicas Inteligentes da IA")
            st.markdown(dicas.choices[0].message.content)
        except Exception as e:
            st.error(f"Erro ao gerar dicas: {e}")
