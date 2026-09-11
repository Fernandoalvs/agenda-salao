import streamlit as st
import json
import os
from datetime import datetime

ARQUIVO_DADOS = "agenda_salao.json"
SENHA_SALAO = "1234"


def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return {}, 1, []
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados_salvos = json.load(arquivo)

            agendamentos_brutos = dados_salvos.get("agendamentos", dados_salvos)
            bloqueados = dados_salvos.get("bloqueados", [])

            agendamentos_convertidos = {}
            maior_id = 0
            for k, v in agendamentos_brutos.items():
                id_num = int(k)
                agendamentos_convertidos[id_num] = v
                if id_num > maior_id:
                    maior_id = id_num
            return agendamentos_convertidos, maior_id + 1, bloqueados
    except:
        return {}, 1, []


def salvar_dados(agendamentos, bloqueados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        estrutura_dados = {
            "agendamentos": agendamentos,
            "bloqueados": bloqueados
        }
        json.dump(estrutura_dados, arquivo, indent=4, ensure_ascii=False)


agendamentos, proximo_id, bloqueados = carregar_dados()

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
            nome_limpo = nome.strip().upper()
            bloqueados_limpos = [b.strip().upper() for b in bloqueados]

            if nome_limpo in bloqueados_limpos:
                st.error(
                    "⚠️ Desculpe, não há horários disponíveis para este cadastro no momento. Por favor, entre em contato diretamente com o salão.")
            else:
                agendamentos[proximo_id] = {
                    "cliente": nome,
                    "servico": servico,
                    "data": str(data.strftime('%d/%m/%Y')),
                    "horario": str(horario.strftime('%H:%M'))
                }
                salvar_dados(agendamentos, bloqueados)

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

        st.subheader("🚫 Gerenciar Lista de Bloqueio")
        col1, col2 = st.columns([2, 1])

        with col1:
            nome_bloquear = st.text_input("Nome completo da pessoa a bloquear:", placeholder="Ex: Maria Souza")
        with col2:
            st.write("##")  # Apenas um espaço visual
            if st.button("Bloquear Cliente ✖️"):
                if nome_bloquear and nome_bloquear not in bloqueados:
                    bloqueados.append(nome_bloquear)
                    salvar_dados(agendamentos, bloqueados)
                    st.success(f"Cliente '{nome_bloquear}' bloqueada!")
                    st.rerun()

        if bloqueados:
            st.write("**Clientes Bloqueadas Atualmente:**")
            for pessoa in bloqueados:
                col_nome, col_btn = st.columns([3, 1])
                col_nome.write(f"• {pessoa}")
                if col_btn.button("Desbloquear", key=f"desbloquear_{pessoa}"):
                    bloqueados.remove(pessoa)
                    salvar_dados(agendamentos, bloqueados)
                    st.rerun()

        st.write("---")
        st.subheader("📋 Próximos Agendamentos")

        if not agendamentos:
            st.info("Nenhum agendamento realizado ainda. 📋")
        else:
            for id_agenda, dados in list(agendamentos.items()):
                with st.container(border=True):
                    st.write(f"**ID:** {id_agenda} | **Cliente:** {dados['cliente']}")
                    st.write(f"**Serviço:** {dados['servico']} | **Dia:** {dados['data']} às {dados['horario']}")

                    if st.button(f"Cancelar ID {id_agenda}", key=f"btn_{id_agenda}"):
                        del agendamentos[id_agenda]
                        salvar_dados(agendamentos, bloqueados)
                        st.rerun()
    elif senha_digitada != "":
        st.error("⚠️ Senha incorreta! Acesso negado.")
