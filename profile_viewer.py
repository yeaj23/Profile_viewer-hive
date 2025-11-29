import streamlit as st
from beem import Hive
from beem.account import Account
import json

# conectar a un nodo de hive
h = Hive(node=["https://api.hive.blog"])

st.write("# Account Hive")

def get_account_info(username):
    # Crear una instancia de Accaount
    account = Account(username, blockchain_instance=h)

    # Obtener la metadata de la cuenta
    account_profile = json.loads(account["posting_json_metadata"])

    # Obtener la foto de perfil de la cuenta
    account_photo = account_profile["profile"]["profile_image"]

    return account, account_profile, account_photo


col1, col2 = st.columns([3,1])
col3, col4 = st.columns([2,3])

with col1:
    # Obtener informacion de la cuenta
    username = st.text_input("Name")

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    search_button = st.button(label="Search", type="primary", use_container_width=True)

# Ejecutar la funcion cuando se hace clic en el boton
if search_button and username:

    # Obtener informacion de la cuenta
    account, account_profile, account_photo = get_account_info(username)

    # Mostrar la foto de perfil de la cuenta
    st.image(account_photo, width=250)

    # Mostrar la informacion de cuenta
    st.write(account)

    # Mostrar la informacion de la cuenta
    with col3:
        st.write(f"Name: {account['name']}")

    with col4:
        st.write(f"Memo key: {account['memo_key']}")

get_account_info("joheredia21")