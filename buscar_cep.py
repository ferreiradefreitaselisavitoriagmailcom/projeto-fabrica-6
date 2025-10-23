import streamlit as st
import buscar_cep as cep


## TÍTULO DA APLICAÇÃO
st.title("CR Entregas 📦")


## LISTA DE OPÇÕES
opcoes = ["Buscar CEP", "Descobrir CEP"]


## BARRA LATERAL
st.sidebar.header("Menu de Opções")
st.sidebar.image("./bmw_correio.png")
escolha = st.sidebar.selectbox("Escolha uma opção:", opcoes)


## LÓGICA DAS OPÇÕES
if escolha == "Buscar CEP":
    st.image("./CR7_busca_cep.png", width=500)
    numero_cep = st.text_input("Digite o CEP que deseja buscar (apenas números):")
    
    if st.button("Buscar CEP"):
        dados = cep.buscar_cep(numero_cep)
        if dados:
            st.success("CEP encontrado com sucesso!")
            st.json(dados)
            # Exibir mapa com a localização do CEP
            st.map({
                "latitude": [ float(dados["lat"]) ],
                "longitude": [ float(dados["lng"]) ] 
            })
        else:
            st.error("CEP não encontrado. Verifique o número e tente novamente.")
elif escolha == "descobrir CEP":
    st.image("./CRT_busca_endereco..png",width=500)
    endereco = st.text_input("digite o endereco completo(rua,numero,cidade,estado):")
    if st.button("descobrir CEP"):
        resultado = cep.descobrir_cep(endereco)
        st.info("a busca do CEP foi realizada.veja o limk abaixo:")
        st.markdown(f"[resultado da busca no google]({resultado})")
