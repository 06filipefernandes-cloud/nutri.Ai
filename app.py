import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- CONFIGURAÇÃO INICIAL ---
st.set_page_config(page_title="NutriIA Body Scan", layout="centered")

# --- BARREIRA DE PAGAMENTO (SENHA) ---
PASSWORD_CORRETO = "DIETA2025" # Mude para a senha que você quiser

st.title("🍎 NutriIA: Análise de Biotipo")
st.write("Bem-vindo! Para acessar sua análise exclusiva, insira o código recebido após a compra.")

senha_usuario = st.text_input("Digite sua Chave de Acesso:", type="password")

if senha_usuario == PASSWORD_CORRETO:
    st.success("Acesso Liberado!")
    
    # --- CONFIGURAR IA ---
    # Substitua 'SUA_CHAVE_AQUI' pela chave que você pegou no Passo 1
    genai.configure(api_key="AIzaSyCQF4wnkHbHDmp0dg3m2SD51ZGtIJtCOas")
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.subheader("📸 Passo 1: Envie sua foto")
    img_file = st.file_uploader("Escolha uma foto de corpo inteiro (frente)", type=['jpg', 'png', 'jpeg'])

    if img_file is not None:
        img = Image.open(img_file)
        st.image(img, caption="Foto carregada", use_column_width=True)
        
        if st.button("Gerar Minha Dieta e Treino"):
            with st.spinner("IA analisando seu biotipo... aguarde."):
                # O PROMPT PARA A IA
                prompt = """
                Analise visualmente esta imagem e identifique o somatotipo (Ectomorfo, Mesomorfo ou Endomorfo).
                Com base nisso, sugira:
                1. Uma estimativa de macros (proteínas, carbo, gorduras).
                2. Um exemplo de dieta de 1 dia.
                3. Um foco de treino (ex: hipertrofia ou queima de gordura).
                AVISO: Adicione no início que isto é uma simulação de IA e não substitui um médico.
                """
                response = model.generate_content([prompt, img])
                st.markdown("### 📋 Seu Plano IA Personalizado:")
                st.write(response.text)
else:
    if senha_usuario != "":
        st.error("Senha incorreta. Adquira seu acesso no site oficial.")
    st.info("Ainda não tem acesso? [Clique aqui para comprar seu acesso]")
