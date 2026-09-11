import streamlit as st
import json
import os
from datetime import datetime

ARQUIVO_DADOS = "agenda_salao.json"
SENHA_SALAO = "1234"


def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return {}, 1
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados_salvos = json.load(arquivo)
            agendamentos_convertidos = {}
            maior_id = 0
            for k, v in dados_salvos.items():
                id_num = int(k)
                agendamentos_convertidos[id_num] = v
                if id_num > maior_id:
                    maior_id = id_num
            return agendamentos_convertidos, maior_id + 1
    except:
        return {}, 1


def salvar_dados(agendamentos):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(agendamentos, arquivo, indent=4, ensure_ascii=False)


agendamentos, proximo_id = carregar_dados()

st.set_page_config(page_title="Agenda do Salão", page_icon="💇‍♀️", layout="centered")

st.title("💇‍♀️ Agendamento Online - Studio Jeh Beaute")
st.write("Escolha o seu serviço e reserve o seu horário de forma rápida!")

aba_cliente, aba_salao = st.tabs(["➕ Marcar Horário", "📋 Visualizar Agenda (Salão)"])

with aba_cliente:
    st.header("Faça o seu agendamento")

    if "mensagem_sucesso" in st.session_state:
        st.success(st.session_state["mensagem_sucesso"])
        del st.session_state["mensagem_sucesso"]

    nome = st.text_input("Qual o seu nome?")
    servico = st.selectbox("Escolha o serviço:",
                           ["Corte Feminino", "Corte Masculino", "Manicure", "Pedicure", "Escova/Escova Progressiva"])

    data = st.date_input("Escolha o dia:", min_value=datetime.today(), format="DD/MM/YYYY")
    horario = st.time_input("Escolha o horário:")

    if st.button("Confirmar Agendamento ✨"):
        if nome:
            agendamentos[proximo_id] = {
                "cliente": nome,
                "servico": servico,
                "data": str(data.strftime('%d/%m/%Y')),
                "horario": str(horario.strftime('%H:%M'))
            }
            salvar_dados(agendamentos)

            st.session_state[
                "mensagem_sucesso"] = f"🎉 Perfeito, {nome}! Seu horário para {servico} em {data.strftime('%d/%m/%Y')} às {horario.strftime('%H:%M')} foi reservado!"
            st.rerun()
        else:
            st.error("⚠️ Por favor, digite o seu nome antes de confirmar.")

with aba_salao:
    st.header("Área Restrita do Salão")

    senha_digitada = st.text_input("Digite a senha do salão para acessar a agenda:", type="password")

    if senha_digitada == SENHA_SALAO:
        st.write("---")

        if not agendamentos:
            st.info("Nenhum agendamento realizado ainda. 📋")
        else:
            for id_agenda, dados in list(agendamentos.items()):
                with st.container(border=True):
                    st.write(f"**ID:** {id_agenda} | **Cliente:** {dados['cliente']}")
                    st.write(f"**Serviço:** {dados['servico']} | **Dia:** {dados['data']} às {dados['horario']}")

                    if st.button(f"Cancelar ID {id_agenda}", key=f"btn_{id_agenda}"):
                        del agendamentos[id_agenda]
                        salvar_dados(agendamentos)
                        st.rerun()
    elif senha_digitada != "":
        st.error("⚠️ Senha incorreta! Acesso negado.")
