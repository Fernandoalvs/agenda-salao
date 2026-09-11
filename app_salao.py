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

# Caixas de preenchimento do site
nome = st.text_input("Qual o seu nome?", placeholder="Digite seu nome completo")
servico = st.selectbox("Escolha o serviço:", ["Corte Feminino", "Corte Masculino", "Manicure", "Pedicure", "Escova/Escova Progressiva"])
data = st.date_input("Escolha o dia desejado:", min_value=datetime.today(), format="DD/MM/YYYY")
horario = st.time_input("Escolha o horário desejado:")

st.write("##") # Espaço visual

# Formata a data e hora para o padrão brasileiro de leitura
data_formatada = data.strftime('%d/%m/%Y')
horario_formatado = horario.strftime('%H:%M')

# Cria a mensagem
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

# Links alternativos do WhatsApp (usando o wa.me que é mais aceito por celulares)
link_whatsapp = f"https://wa.me{NUMERO_WHATSAPP}?text={mensagem_codificada}"

st.write("### Clique no botão abaixo para enviar:")

# 🚀 A SOLUÇÃO: Criamos um botão visual usando HTML puro. O navegador aceita isso instantaneamente como um link comum!
botao_html = f"""
    <div style="text-align: center;">
        <a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25D366; color: white; padding: 14px 20px; font-size: 16px; font-weight: bold; border-radius: 8px; display: inline-block; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); width: 100%;">
                🟢 ENVIAR SOLICITAÇÃO NO WHATSAPP
            </div>
        </a>
    </div>
"""

# Exibe o botão HTML na tela com segurança
st.markdown(botao_html, unsafe_allow_html=True)
