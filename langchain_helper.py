from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import streamlit as st
import openai
import os

# Configurar la clave API de OpenAI utilizando st.secrets
openai_api_key = st.secrets["openai_api_key"]
openai.api_key = openai_api_key


# Inicializar 'llm' fuera de cualquier bloque de funciones para que sea global
try:
    llm = OpenAI(temperature=0.6)
except Exception as e:
    st.error(f"Error al inicializar OpenAI: {e}")
    llm = None  # Define llm como None en caso de error

def generate_restaurant_name_and_items(cuisine):
    if llm is None:
        # Manejar el caso donde llm no está definido correctamente
        st.error("Error: El modelo de lenguaje no ha sido inicializado correctamente.")
        return




def generate_restaurant_name_and_items(cuisine): 
# Chain 1: Restaurant Name    
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name fot this"
    )
    
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

# Chain 2: Restaurant Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest some menu items for {restaurant_name}. Return it as a comma separated string"""
    ) 

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

# Chain 3: Sequential Chain
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_items"]
    )


    response = chain({'cuisine': cuisine})

    return response


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))

 
    