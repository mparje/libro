import streamlit as st
import openai

# Configuramos el diseño de la página
st.set_page_config(layout="wide")

# Configuramos la clave de la API de OpenAI
api_key = st.sidebar.text_input("Ingrese su clave de API de OpenAI", type="password")

if not api_key:
    st.warning("Por favor, ingrese una clave de API válida para continuar.")
else:
    openai.api_key = api_key
    # Continuar con el resto del código que utiliza la clave de API

# Agregamos un título al principio
st.title('Generador de Capítulos de Libro')

# Agregamos información de instrucciones en la columna izquierda
st.sidebar.title('Instrucciones')
st.sidebar.write('1. Ingrese su clave de OpenAI. Si no tiene una, obténgala en https://platform.openai.com/account/api-keys')
st.sidebar.write('2. Proporcione una pequeña introducción o contexto para su libro.')
st.sidebar.write('3. Haga clic en Generar Capítulo para crear contenido para su libro.')

# Pedimos al usuario que ingrese una introducción
introduccion = st.text_area("Introducción o Contexto para el Libro")

# Agregamos un botón para generar un capítulo
if st.button('Generar Capítulo'):
    if introduccion:
        # Generamos un capítulo usando la API de GPT-3
        prompt = f"Genera un capítulo para el libro. Introducción: {introduccion}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1000,
            n=1,
            stop=None,
            timeout=30
        )
        capitulo_generado = response.choices[0].text.strip()

        # Mostramos el capítulo generado
        st.subheader("Capítulo Generado")
        st.write(capitulo_generado)
    else:
        st.warning("Por favor, proporcione una introducción antes de generar un capítulo.")
