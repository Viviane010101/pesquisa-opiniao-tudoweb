import streamlit as st

st.set_page_config(
    page_title="Pesquisa de Satisfação - TudoWeb",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Pesquisa de Satisfação")
st.subheader("🌐 TudoWeb")

st.write(
    "Olá! Queremos saber sua opinião sobre o nosso atendimento. "
    "Sua participação é muito importante para nós! 💙"
)

st.divider()

if "respostas" not in st.session_state:
    st.session_state.respostas = []

if "excelente" not in st.session_state:
    st.session_state.excelente = 0

if "bom" not in st.session_state:
    st.session_state.bom = 0

if "ruim" not in st.session_state:
    st.session_state.ruim = 0

st.header("👤 Dados do entrevistado")

nome = st.text_input(
    "📝 Nome",
    placeholder="Digite seu nome"
)

idade = st.number_input(
    "🎂 Idade",
    min_value=1,
    max_value=120,
    step=1
)

opiniao = st.radio(
    "💬 Como você avalia nosso atendimento?",
    [
        "⭐ Excelente",
        "👍 Bom",
        "😞 Ruim"
    ]
)

if st.button("📤 Enviar resposta", use_container_width=True):

    if nome.strip() == "":
        st.warning("⚠️ Por favor, informe seu nome.")

    elif len(st.session_state.respostas) >= 50:
        st.warning("⚠️ A pesquisa já atingiu o limite de 50 entrevistados.")

    else:
        if opiniao == "⭐ Excelente":
            st.session_state.excelente += 1

        elif opiniao == "👍 Bom":
            st.session_state.bom += 1

        elif opiniao == "😞 Ruim":
            st.session_state.ruim += 1

        st.session_state.respostas.append({
            "nome": nome,
            "idade": idade,
            "opiniao": opiniao
        })

        st.success(
            f"✅ Obrigado, {nome}! Sua opinião foi registrada com sucesso."
        )

st.divider()

st.header("📊 Resultado da pesquisa")

total_respostas = (
    st.session_state.excelente
    + st.session_state.bom
    + st.session_state.ruim
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("⭐ Excelente", st.session_state.excelente)

with col2:
    st.metric("👍 Bom", st.session_state.bom)

with col3:
    st.metric("😞 Ruim", st.session_state.ruim)

st.metric("📋 Total de respostas", total_respostas)

if total_respostas >= 50:
    st.success("🎉 A pesquisa atingiu o limite de 50 entrevistados!")

st.divider()

st.info(
    """
    💙 **A TudoWeb agradece sua participação!**

    Sua opinião é muito importante para nós.

    💡 Tem alguma sugestão de melhoria?
    Compartilhe sua ideia com a TudoWeb através
    do nosso canal de atendimento.

    🚀 Sua sugestão pode contribuir para melhorarmos
    cada vez mais nosso atendimento.
    """
)
