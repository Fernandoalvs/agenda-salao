import streamlit as st
from datetime import datetime
import urllib.parse

# 📱 NÚMERO DE WHATSAPP DO STUDIO ATUALIZADO
NUMERO_WHATSAPP = "5511966092902"

# --- CONFIGURAÇÃO DA PÁGINA WEB ---
st.set_page_config(page_title="Studio Jeh Beauté", page_icon="💇‍♀️", layout="centered")

# --- DESIGN: PALETA OFICIAL + BLINDAGEM COMPLETA DE LETRAS CLARAS (CSS) ---
VISUAL_STUDIO = """
    <style>
    /* 1. Força o fundo de fora do site a ser o Dourado Acetinado */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #CDBBA7 !important; 
        background-image: none !important;
    }

    /* 2. Container Central Pérola (Off-white) */
    .block-container {
        background-color: #FAF6F0 !important; 
        padding: 45px !important;
        border-radius: 16px;
        box-shadow: 0px 15px 35px rgba(44, 30, 24, 0.25);
        margin-top: 40px;
    }

    /* 3. Forçando as cores dos títulos para o Marrom Escuro do logotipo */
    h1, h2, h3, .stMarkdown p, span, p strong {
        color: #2C1E18 !important;
        font-family: 'Playfair Display', 'Didot', 'Georgia', serif !important;
    }

    /* Legenda secundária */
    p.subtitulo {
        color: #5C4A42 !important;
        text-align: center;
        font-size: 15px;
    }

    /* Estilização dos rótulos dos campos (Labels) */
    label, .stWidgetFormLabel p {
        color: #2C1E18 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }

    /* 🔒 CORREÇÃO CIRÚRGICA: Força a cor das letras DENTRO de absolutamente todas as caixas para BRANCO */
    input, select, 
    div[data-baseweb="select"] *, 
    div[data-baseweb="input"] input, 
    .stTextInput input,
    div[data-testid="stDateInput"] input,
    div[data-testid="stTimeInput"] input {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }

    /* Garante que o texto de exemplo (placeholder) fique em cinza claro */
    input::placeholder {
        color: #CCCCCC !important;
        opacity: 1 !important;
    }

    /* Esconde elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(VISUAL_STUDIO, unsafe_allow_html=True)

# --- CONTEÚDO DO SITE ---
st.markdown("<h1 style='text-align: center; letter-spacing: 2px;'>STUDIO JEH BEAUTÉ</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo'>Pré-Agendamento Online de Serviços Exclusivos</p>", unsafe_allow_html=True)
st.write("---")

st.markdown("<h3 style='font-size: 18px; margin-bottom: 15px;'>✨ Insira seus dados para a solicitação:</h3>",
            unsafe_allow_html=True)

# Organizando os campos lado a lado em duas colunas
col1, col2 = st.columns(2)

with col1:
    nome = st.text_input("👤 Seu nome completo:", placeholder="Digite aqui...")
    data = st.date_input("📅 Escolha o dia:", min_value=datetime.today(), format="DD/MM/YYYY")

with col2:
    servico = st.selectbox("💇‍♀️ Escolha o serviço:",
                           ["Corte Feminino", "Manicure", "Pedicure", "Escova/Escova Progressiva"])
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

# --- BOTÃO "AGENDAR AGORA" EM NUDE ROSÉ ---
botao_html = f"""
    <div style="text-align: center; margin-top: 15px;">
        <a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #E6D5CC; color: #2C1E18; padding: 16px 30px; font-size: 16px; font-weight: bold; font-family: 'Playfair Display', serif; letter-spacing: 2px; border-radius: 8px; display: inline-block; box-shadow: 0px 4px 15px rgba(44, 30, 24, 0.15); width: 100%; transition: 0.3s;">
                AGENDAR AGORA
            </div>
        </a>
    </div>
"""
st.markdown(botao_html, unsafe_allow_html=True)

st.write("##")
st.markdown(
    "<p style='font-size: 13px; color: #5C4A42; text-align: center;'>💡 <i>Ao clicar no botão, sua solicitação será enviada formatada diretamente para o nosso atendimento via WhatsApp.</i></p>",
    unsafe_allow_html=True)
