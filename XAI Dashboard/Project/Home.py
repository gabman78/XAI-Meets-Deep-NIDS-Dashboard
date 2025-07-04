import streamlit as st
from layout import *
from DBinfo import *
from NetworkAnalysis import *


st.set_page_config(page_title="XAI", layout="centered")
aggiungi_sfondo("images/sfondo.png")

def reset_to_home():
    st.session_state.clear()  # Pulisce tutto lo stato
    st.session_state.page = "home"
    st.rerun()

def go_to(page_name):
    st.session_state.page = page_name




if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    logo_home()
    pulsanti_stilizzati()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🗂️ SDN Database"):
            go_to("DBinfo")
            st.rerun()
    with col2:
        if st.button("🌏DL Network Analysis"):
            go_to("NetworkAnalysis")
            st.rerun()


elif st.session_state.page == "DBinfo":
    pulsanti_stilizzati()

    
    visualizza_dashboard()
    analisi_boxplot()

    if st.button("⬅️ Torna alla Home"):
        go_to("home")
        st.rerun()

elif st.session_state.page == "NetworkAnalysis":
    pulsanti_stilizzati()
    
    main()

    if st.button("⬅️ Torna alla Home"):
        go_to("home")
        st.rerun()