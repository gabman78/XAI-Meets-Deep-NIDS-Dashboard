import streamlit as st
import base64

def pulsanti_stilizzati():
    st.markdown(
        """
        <style>
        .stButton>button {
            border: none;
            width: 250px;
            height: 180px;
            border-radius: 20px;
            font-size: 40px !important;
            font-weight: 1200 !important;
            color: #2484A1;
            background-color: #ffffff10;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            cursor: pointer;
            margin: 20px auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            line-height: 1.4;
            text-align: center;
        }

        .stButton>button:hover {
            transform: scale(1.05);
            background-color: #ffffff20;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def aggiungi_sfondo(image_path: str):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )



def logo_home():
    # Centrare immagine usando le colonne
    col1, col2, col3 = st.columns([2, 4, 1])
    with col2:
        st.image("images/logo.png", width=300)

    
