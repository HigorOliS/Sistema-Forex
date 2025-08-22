st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/HigorOliS/Sistema-Forex/main/IMG_3894.jpeg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        position: relative;
    }}
    /* Camada escura sobre a imagem */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(0,0,0,0.75); /* 75% preto por cima */
        z-index: 0;
    }}
    /* Garante que o conteúdo fica acima da camada escura */
    .block-container {{
        position: relative;
        z-index: 1;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
