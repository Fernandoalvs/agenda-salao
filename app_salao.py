import streamlit as st
import json
import os
from datetime import datetime

ARQUIVO_DADOS = "agenda_salao.json"


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


    nome = st.text_input("Qual o seu nome?")
    servico = st.selectbox("Escolha o serviço:",
                           ["Corte Feminino", "Manicure", "Pedicure", "Escova/Escova Progressiva"])
    data = st.date_input("Escolha o dia:", min_value=datetime.today())
    horario = st.time_input("Escolha o horário:")


    if st.button("Confirmar Agendamento ✨"):
        if nome:

            agendamentos[proximo_id] = {
                "cliente": nome,
                "servico": servico,
                "data": str(data.strftime('%d/%m/%y')),
                "horario": str(horario.strftime('%H:%M'))
            }
            salvar_dados(agendamentos)
            st.success(f"🎉 Perfeito, {nome}! Seu horário para {servico} foi reservado com sucesso!")
        else:
            st.error("⚠️ Por favor, digite o seu nome antes de confirmar.")


with aba_salao:
    st.header("Gerenciar Horários Marcados")

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
