import streamlit as st
from datetime import datetime
import urllib.parse

# 📱 INSIRA O NÚMERO DE WHATSAPP DA SUA IRMÃ AQUI (Com o DDD e sem espaços ou traços)
# Exemplo: "5511999999999" (O 55 é o código do Brasil, obrigatório!)
NUMERO_WHATSAPP = "5511915167912"

# --- CONFIGURAÇÃO DA PÁGINA WEB ---
st.set_page_config(page_title="Solicitar Horário", page_icon="💇‍♀️", layout="centered")

st.title("💇‍♀️ Pré-Agendamento Online - Studio Jeh Beaute")
st.write("Escolha o seu serviço e horário preferidos para enviar a sua solicitação diretamente para o nosso WhatsApp!")
st.write("---")

st.header("Preencha os dados abaixo:")

# Caixas de preenchimento do site que atualizam em tempo real
nome = st.text_input("Qual o seu nome?", placeholder="Digite seu nome completo")
servico = st.selectbox("Escolha o serviço:", ["Corte Feminino", "Corte Masculino", "Manicure", "Pedicure", "Escova/Escova Progressiva"])
data = st.date_input("Escolha o dia desejado:", min_value=datetime.today(), format="DD/MM/YYYY")
horario = st.time_input("Escolha o horário desejado:")

st.write("##") # Espaço visual

# Formata a data e hora para o padrão brasileiro de leitura
data_formatada = data.strftime('%d/%m/%Y')
horario_formatado = horario.strftime('%H:%M')

# Se o nome já foi digitado, geramos a mensagem personalizada em tempo real
if nome:
    mensagem = (
        f"Olá! Me chamo *{nome}* e gostaria de solicitar um agendamento no salão:\n\n"
        f"💇‍♀️ *Serviço:* {servico}\n"
        f"📅 *Dia:* {data_formatada}\n"
        f"⏰ *Horário:* {horario_formatado}\n\n"
        f"Está disponível?"
    )
else:
    # Mensagem padrão caso o nome esteja em branco
    mensagem = f"Olá! Gostaria de solicitar um agendamento para {servico} no dia {data_formatada} às {horario_formatado}. Está disponível?"

# Transforma o texto em códigos que a internet entende
mensagem_codificada = urllib.parse.quote(mensagem)

# Monta o link definitivo do WhatsApp
link_whatsapp = f"https://whatsapp.com{NUMERO_WHATSAPP}&text={mensagem_codificada}"

# Exibe o botão direto. O navegador NUNCA bloqueia este botão porque ele é um link puro!
st.link_button("🟢 ENVIAR SOLICITAÇÃO NO WHATSAPP", link_whatsapp, type="primary", use_container_width=True)

if not nome:
    st.info("💡 Dica: Digite seu nome acima para que a mensagem já vá personalizada com os seus dados!")
