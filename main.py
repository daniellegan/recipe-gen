import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = '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'
# after replacing thee ingredients, write the right instrunctions based on the replaced ingredients.

template = """
Below is a regular recipe that a user enterd.
your goal is to convert the recipe to fit the user preferance based on his food diet.

Below is an example:
if hid diet is vegan and he the recepie is Milk 
your answer will be soy-milk

Beloow is a list with his diet preferance and the recipe:
Diet:{diet},
Recipe:{recipe}

YOUR ANSWER:
"""

prompt = PromptTemplate(
    input_variables=["diet", "recipe"],
    template=template,
)

def load_LLM():
    llm = OpenAI(temperature=0)
    return llm

llm = load_LLM()

#python -m streamlit run your_script.py
st.set_page_config(page_title="Recipe Generator", page_icon=":root:")

st.title("Recipe Generator")

col1, col2, col3 = st.columns(3)
with col1:
    diet_choices = st.multiselect('diet', ['vegan','sugar free', 'gluten free', 'dairy free', 'vegeterian'])
with col2:
    url_clicked = st.button('url', key=0)
with col3:
    recipe_clicked = st.button('recipe', key=1)

# url_clicked = st.button('url')
# recipe_clicked = st.button('recipe')

def get_input_button(): 
    if (url_clicked):
        input_text = st.text_input(label="", placeholder="enter url")
    else: 
        # if(recipe_clicked):
        input_text = st.text_area(label="", placeholder="enter recipe")
    return input_text

input_recipe = get_input_button()

if input_recipe:
    prompt_with_values = prompt.format(diet=diet_choices, recipe=input_recipe)
    formatted_recipe = llm(prompt_with_values)
    st.write(formatted_recipe)



# def run_componenet(props):
#     value = component_toolbar_buttons(key='toolbar_buttons', **props)
#     return value

# def handle_event(value):
#     st.write('recived from component', value)

# props = {
#     'buttons': {
#         'url': False,
#         'recipe': False
#     }
# }

# st.column_config(['col', 'col2'])
# handle_event(run_componenet(props))

