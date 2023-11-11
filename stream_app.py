# https://github.com/wjbmattingly/streamlit_lessons_youtube/blob/main/01_intro_to_streamlit_app.py

import streamlit as st
import requests
from bs4 import BeautifulSoup
import json
import pickle

import scrape


file = open("dic_data.obj",'rb')
dic_data = pickle.load(file)
file.close()


file = open("dic_companywise.obj",'rb')
dic_companywise = pickle.load(file)
file.close()



st.title("Boycott for palestine")
st.header("Details about brands to boycott")
# button1 = st.button("Click Me")
# if button1:
#     st.write("This is some text.")

# st.header("Start of the Checkbox Section")
# like = st.checkbox("Do you like this app?")
# button2 = st.button("Submit")
# if button2:
#     if like:
#         st.write("Thanks. I like it too.")
#     else:
#         st.write("I'm sorry. You have bad tastes.")

# st.header("Start of the Radio Button Section")
# animal = st.radio("What animal is your favorite?", ("Lion", "Tiger", "Bear"))
# button3 = st.button("Submit Animal")
# if button3:
#     st.write(animal)
#     if animal == "Lion":
#         st.write("ROAR!")

categories=list(dic_data.keys())
category = st.selectbox("Choose category.", categories)

print("Chosen category is",category)

companies=dic_data[category]['names']

name = st.selectbox("Companies that we need to boycott.", companies)

print("Chosen company is",name)


company_details = dic_companywise[name]
st.image(company_details["logo"],width=200)

print("Chosen company_details is",company_details)

# st.subheader("Description")
st.text(company_details["description"])


st.text("Reason For Boycott")
st.caption(company_details["reason"])


st.text("Source Of Information")
st.caption(company_details["source"])
st.markdown("""---""")


st.text("Action")
st.caption(company_details["howToBoycott"])



st.text("Alternatives")
st.caption(company_details["alternatives"])
st.markdown("""---""")


button1 = st.button("Update Info")
st.caption("Warning: takes 3 minutes")
if button1:
    print("clicked the button")
    scrape.scrape_web()
    
