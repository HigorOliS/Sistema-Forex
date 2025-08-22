import streamlit as st
import pandas as pd

st.set_page_config(page_title="LucroCerto FX", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(
            rgba(0, 0, 0, 0.7),
            rgba(0, 0, 0, 0.7)
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

if st.button("💡 Gerar Análise"):
    data = {
        "Par": ["EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "AUD/USD"],
        "Horário": ["10:32:15", "06:15:45", "22:47:30", "04:12:59", "21:03:12"],
        "Ação": ["Comprar", "Vender", "Comprar", "Vender", "Comprar"],
        "Probabilidade (%)": [92, 89, 94, 90, 91]
    }
    df = pd.DataFrame(data)

    # Função para aplicar cor dinamicamente
    def color_action(val):
        if val == "Comprar":
            return "color: green; font-weight: bold;"
        elif val == "Vender":
            return "color: red; font-weight: bold;"
        return ""

    # Aplicar estilos dinamicamente
    styled_df = df.style.applymap(color_action, subset=["Ação"])

    st.markdown("## 📈 Resultados da Análise")
    st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)

    st.markdown("## 💡 Dicas de Horários")
    st.write("""
    - **EUR/USD** → Mais preciso entre **10:00 e 12:00 (GMT-3)**.
    - **GBP/USD** → Movimentos fortes entre **05:30 e 07:00**.
    - **USD/JPY** → Boa volatilidade entre **22:00 e 23:30**.
    - **AUD/USD** → Melhor liquidez às **21:00 (abertura Sydney)**.
    - **USD/CHF** → Melhor momento entre **04:00 e 05:00**.
    """)
