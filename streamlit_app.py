import langchain_helper
import streamlit as st
import base64
import json


# Función para cargar las traducciones
def load_translations(language_code):
    with open(f"texts_{language_code}.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Selección del idioma
language = st.sidebar.selectbox("Language", ["English", "Español", "Deutsch"])
language_code = {"English": "en", "Español": "es", "Deutsch": "de"}
texts = load_translations(language_code[language])

# Interfaz de usuario
st.title(texts["title"])

cuisine = st.sidebar.selectbox(texts["select_cuisine"], ("Spain", "United States", "Chinese", "Indian", "Italian", "Japanese", "Mexican", "Thai"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    
    # Eliminar saltos de línea del nombre del restaurante
    restaurant_name = response['restaurant_name'].replace('\n', ' ').strip()

    full_header = texts["response_header"] + restaurant_name
    st.header(full_header)

    menu_items = response['menu_items'].strip().split(",")
    st.write(texts["menu_items_header"])
    for item in menu_items:
        st.write("- " + item)


    # Función para obtener la representación en base64 de una imagen
def get_image_base64(path):
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/svg+xml;base64,{encoded}"

# Obtén la representación en base64 de tus imágenes
github_icon_base64 = get_image_base64("./assets/github.svg")
linkedin_icon_base64 = get_image_base64("./assets/linkedin.svg")

# URLs de tus perfiles
github_url = "https://github.com/limbpuma"
linkedin_url = "https://www.linkedin.com/in/limber-martinez-developer/"

# Usar st.markdown para agregar enlaces con imágenes codificadas en base64
st.markdown(f"""
    <div style="text-align: center; display: flex; justify-content: center; align-items: center; gap: 20px;">
        <a href="{github_url}" target="_blank">
            <img src="{github_icon_base64}" alt="GitHub" style="width: 20px; height: 20px;">
        </a>
        <a href="{linkedin_url}" target="_blank">
            <img src="{linkedin_icon_base64}" alt="LinkedIn" style="width: 20px; height: 20px;">
        </a>
    </div>
""", unsafe_allow_html=True)
# Mensaje "Hecho con Python, Langchain y Streamlit"
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p>Made with ❤️ en Python, Langchain y Streamlit</p>
    </div>
""", unsafe_allow_html=True)