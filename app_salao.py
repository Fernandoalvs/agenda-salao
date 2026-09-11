import streamlit as st
from datetime import datetime
import urllib.parse


NUMERO_WHATSAPP = "5511915167912"


st.set_page_config(page_title="Solicitar Horário", page_icon="💇‍♀️", layout="centered")

st.title("💇‍♀️ Pré-Agendamento Online - Studio Jeh Beaute")
st.write("Escolha o seu serviço e horário preferidos para enviar a sua solicitação diretamente para o nosso WhatsApp!")
st.write("---")

st.header("Preencha os dados abaixo:")


nome = st.text_input("Qual o seu nome?")
servico = st.selectbox("Escolha o serviço:",
                       ["Corte Feminino", "Manicure", "Pedicure", "Escova/Escova Progressiva"])
data = st.date_input("Escolha o dia desejado:", min_value=datetime.today(), format="DD/MM/YYYY")
horario = st.time_input("Escolha o horário desejado:")

st.write("##")

if st.button("Solicitar Agendamento via WhatsApp 🟢"):
    if nome:
        data_formatada = data.strftime('%d/%m/%Y')
        horario_formatado = horario.strftime('%H:%M')

        mensagem = (
            f"Olá! Me chamo *{nome}* e gostaria de solicitar um agendamento no salão:\n\n"
            f"💇‍♀️ *Serviço:* {servico}\n"
            f"📅 *Dia:* {data_formatada}\n"
            f"⏰ *Horário:* {horario_formatado}\n\n"
            f"Está disponível?"
        )

        mensagem_codificada = urllib.parse.quote(mensagem)

        link_whatsapp = f"https://whatsapp.com{NUMERO_WHATSAPP}&text={mensagem_codificada}"

        st.success("🎉 Seus dados foram organizados!")

        st.link_button("Clique aqui para enviar no WhatsApp 📲", link_whatsapp, type="primary")
    else:
        st.error("⚠️ Por favor, digite o seu nome antes de prosseguir.")
