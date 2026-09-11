import streamlit as st
from datetime import datetime
import urllib.parse

# 📱 NÚMERO DE WHATSAPP DO STUDIO
NUMERO_WHATSAPP = "5511966092902"

# --- CONFIGURAÇÃO DA PÁGINA WEB ---
st.set_page_config(page_title="Studio Jeh Beaute", page_icon="💇‍♀️", layout="centered")

# --- LINK DA IMAGEM DE FUNDO PERSONALIZADA ---
# Usamos uma foto em HD de um salão moderno, minimalista e elegante
URL_IMAGEM_FUNDO = "https://unsplash.com"

# --- APLICANDO O DESIGN VISUAL (CSS) ---
VISUAL_CUSTOMIZADO = f"""
    <style>
    /* Aplica a imagem de fundo em toda a tela do site */
    .stApp {{
        background-image: url("{URL_IMAGEM_FUNDO}");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
    }}

    /* Cria o container central com efeito "vidro fosco" para leitura limpa */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.92);
        padding: 40px !important;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.15);
        margin-top: 30px;
    }}

    /* Esconde os menus cinzas padrão do Streamlit */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
"""
st.markdown(VISUAL_CUSTOMIZADO, unsafe_allow_html=True)

# --- CONTEÚDO DO SITE ---
st.markdown("<h1 style='text-align: center; color: #1E1E1E;'>💇‍♀️ Studio Jeh Beaute</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #555555; font-size: 16px;'>Escolha o serviço e horário de sua preferência para atendimento</p>",
    unsafe_allow_html=True)
st.write("---")

st.markdown("<h3 style='color: #1E1E1E;'>✨ Insira seus dados para a solicitação:</h3>", unsafe_allow_html=True)

# Organizando os campos lado a lado
col1, col2 = st.columns(2)

with col1:
    nome = st.text_input("👤 Seu nome completo:", placeholder="Ex: Maria Silva")
    data = st.date_input("📅 Escolha o dia:", min_value=datetime.today(), format="DD/MM/YYYY")

with col2:
    servico = st.selectbox("💇‍♀️ Escolha o serviço:",
                           ["Corte Feminino", "Corte Masculino", "Manicure", "Pedicure", "Escova/Escova Progressiva"])
    horario = st.time_input("⏰ Escolha o horário:")

st.write("##")  # Espaço visual

# --- PROCESSAMENTO DO LINK DO WHATSAPP ---
data_formatada = data.strftime('%d/%m/%Y')
horario_formatado = horario.strftime('%H:%M')

if nome:
    mensagem = (
        f"Olá! Me chamo *{nome}* e gostaria de solicitar um agendamento no salão:\n\n"
        f"💇‍♀️ *Serviço:* {servico}\n"
        f"📅 *Dia:* {data_formatada}\n"
        f"⏰ *Horário:* {horario_formatado}\n\n"
        f"Está disponível?"
    )
else:
    mensagem = f"Olá! Gostaria de solicitar um agendamento para {servico} no dia {data_formatada} às {horario_formatado}. Está disponível?"

mensagem_codificada = urllib.parse.quote(mensagem)
link_whatsapp = f"https://wa.me{NUMERO_WHATSAPP}?text={mensagem_codificada}"

# --- BOTÃO DO WHATSAPP ESTILIZADO EM HTML ---
botao_html = f"""
    <div style="text-align: center; margin-top: 10px;">
        <a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25D366; color: white; padding: 16px 30px; font-size: 18px; font-weight: bold; border-radius: 50px; display: inline-block; box-shadow: 0px 6px 12px rgba(37, 211, 102, 0.3); width: 100%; transition: 0.3s;">
                🟢 ENVIAR SOLICITAÇÃO VIA WHATSAPP
            </div>
        </a>
    </div>
"""
st.markdown(botao_html, unsafe_allow_html=True)

st.write("##")
st.info(
    "💡 **Como funciona?** Ao clicar no botão acima, seu WhatsApp se abrirá com os dados preenchidos. Nossa equipe irá analisar a disponibilidade e te responderá em instantes!")
