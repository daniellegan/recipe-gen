import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = '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'
# after replacing thee ingredients, write the right instrunctions based on the replaced ingredients.

template = """
###
Convert the recipe to fit the user preferance based on his diet list.
The desired format:
ingredients: <line_separated_list_of_ingredients_names>
constructor: -||-
###

###
Beloow is a list with the diet preferance and the recipe:
Diet:{diet},
Recipe:{recipe}
###

YOUR ANSWER:
"""
# if using few shot prompting:
###
# Below is an example:
# Diet list: vegan, gluten free.
# Recipe: 1.5 cup milk, 100g butter, 1 cup wheet.
# Therefor your answer will be: 1.5 cup soy-milk, 100g vegan butter like Naturina, 1 cup gluten free wheet. 
###

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

