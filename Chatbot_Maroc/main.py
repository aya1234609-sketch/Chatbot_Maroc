import base64
import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Quiz - Unité Territoriale du Maroc", page_icon="🇲🇦", layout="centered")

# Fonction pour encoder l'image locale en base64 (الخلفية)
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

img_base64 = get_base64_image("background.png")

if img_base64:
    bg_style = f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(15, 12, 41, 0.4), rgba(48, 43, 99, 0.4)), url("data:image/png;base64,{img_base64}") !important;
        background-size: cover !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)
else:
    bg_style = """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

# بداية محتوى التطبيق الخاص بك
st.title("🇲🇦 الوحدة الترابية للمغرب : تاريخ، سيادة وتنمية")
st.markdown("---")
st.write("Espace interactif de présentation - Lycée Arrachad")
