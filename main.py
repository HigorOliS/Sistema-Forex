import streamlit as st

st.set_page_config(page_title="LucroCerto FX", page_icon="💰", layout="wide")

st.title("💰 LucroCerto FX - Scalping IA")
st.markdown("### Sistema automatizado com IA para alta precisão em Forex")

# Exemplo de tabela
import pandas as pd

data = {
    "Horário": ["09:15:32", "09:16:45", "09:17:10"],
    "Ação": ["Comprar", "Vender", "Comprar"],
    "Probabilidade (%)": [92, 95, 90]
}

df = pd.DataFrame(data)

st.table(df)

st.info("🚀 Dados apenas para demonstração. Versão Beta.")
