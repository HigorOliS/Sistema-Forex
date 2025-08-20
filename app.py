import streamlit as st
import pandas as pd

st.set_page_config(page_title="LucroCerto FX", layout="centered")

# =========================
# TELA 1 - Entrada do Usuário
# =========================
if "tela" not in st.session_state:
    st.session_state["tela"] = "inicio"
    st.session_state["comentario_usuario"] = ""

if st.session_state["tela"] == "inicio":
    st.markdown("<h1 style='text-align: center; color: gold;'>💹 LucroCerto FX</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Seu aliado no Forex com IA ⚡</h3>", unsafe_allow_html=True)

    st.write("")
    st.write("")

    # Botão de gerar sinais
    if st.button("🚀 Gerar sinais com IA", use_container_width=True):
        st.session_state["tela"] = "resultado"
        st.rerun()

    st.write("---")

    # Upload do print
    uploaded_file = st.file_uploader("📷 Envie um print do gráfico (opcional)", type=["png", "jpg", "jpeg"])

    # Caixa de texto para otimizar análise
    comentario = st.text_area(
        "📝 Otimize a análise com sua descrição (opcional)",
        placeholder="*Pode detalhar o cenário do gráfico (ex.: tendência, rompimento, suporte/resistência)..."
    )
    if comentario:
        st.session_state["comentario_usuario"] = comentario

# =========================
# TELA 2 - Resultados
# =========================
elif st.session_state["tela"] == "resultado":
    st.markdown("<h2 style='text-align: center;'>📊 Resultados da análise</h2>", unsafe_allow_html=True)

    # Simulação de sinais
    dados = {
        "Par de moedas": ["EUR/USD", "USD/JPY", "GBP/USD", "USD/CHF", "AUD/USD"],
        "Horário sugerido": ["10:30:15", "11:45:30", "13:15:45", "15:20:10", "17:50:05"],
        "Ação": ["Comprar", "Vender", "Comprar", "Vender", "Comprar"],
        "Probabilidade(%)": [92, 96, 94, 90, 91]
    }
    df = pd.DataFrame(dados)

    # Estilizar tabela (verde para comprar, vermelho para vender)
    def colorir_acoes(val):
        if val == "Comprar":
            return "color: green; font-weight: bold;"
        elif val == "Vender":
            return "color: red; font-weight: bold;"
        return ""

    st.dataframe(df.style.applymap(colorir_acoes, subset=["Ação"]), use_container_width=True)

    # Dicas de horários
    st.markdown("### 💡 Dicas de horários ideais")
    st.markdown("""
    - **EUR/USD** → Mais previsível entre **10h e 12h**  
    - **USD/JPY** → Melhor entre **22h e 02h**  
    - **GBP/USD** → Alta volatilidade entre **09h e 11h**  
    - **USD/CHF** → Estável entre **15h e 17h**  
    - **AUD/USD** → Oportunidades entre **20h e 23h**
    """)

    # Comentário do usuário (se houver)
    if st.session_state["comentario_usuario"]:
        st.markdown("### 💡 Comentário da sua análise")
        st.info(st.session_state["comentario_usuario"])

    st.write("---")

    # Botão para nova análise
    if st.button("🔄 Nova análise", use_container_width=True):
        st.session_state["tela"] = "inicio"
        st.session_state["comentario_usuario"] = ""
        st.rerun()
