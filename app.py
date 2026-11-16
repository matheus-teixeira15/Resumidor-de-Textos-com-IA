
import streamlit as st
from resumidor import resumir_texto

# Configuração da página
st.set_page_config(
    page_title="Resumidor de Texto de IA",
    page_icon="📝",
    layout="centered"
)

# Título
st.title("📝 Resumidor de Texto de IA")

st.write(
    "Insira um texto abaixo e deixe a Inteligência "
    "Artificial gerar um resumo para você."
)

# Campo para inserir o texto
texto = st.text_area(
    "Texto para resumir:",
    height=250,
    placeholder="Cole seu texto aqui..."
)

# Seleção do tamanho do resumo
tamanho = st.selectbox(
    "Escolha o tamanho do resumo:",
    ["Curto", "Médio", "Detalhado"]
)

# Botão para gerar o resumo
if st.button("Gerar resumo", type="primary"):

    if not texto.strip():
        st.warning("Por favor, insira um texto.")

    else:
        try:
            with st.spinner("Gerando resumo..."):
                resumo = resumir_texto(texto, tamanho)

            st.subheader("Resumo gerado:")
            st.write(resumo)

        except Exception as erro:
            st.error(f"Erro ao gerar resumo: {erro}")
