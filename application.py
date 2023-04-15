import streamlit as st
import pickle
#from PIL  import Image
import pandas as pd
st.write("bonjour") 

model = pickle.load(open("modelsave.sav","rb"))

#st.dump(model)
#st.button("click")

with st.form("forme1"):
    #name = st.text_input("Name") # prend en entrée une colonne de type objet
    age = st.number_input("Age",min_value=0) #prend en entrée les colonnes de type entier
    income = st.number_input("Income",min_value=0) 
    score= st.number_input("Score",min_value=0) 
    #image = st.file_uploader("Set image") # prend en entrée les donnée de type image
    #pd = st.date_input("BD") # prend en entrée les données de type data
    submit = st.form_submit_button("Submit") # pour soumettre notre formulaire

    if submit:
        data = pd.DataFrame({"Age": [age],"Income": [income],"Score": [score]}, columns=["Age","Income","Score"])
        X = data.values
        Pred = model.predict(X) 
        st.write(f"cette individu appartient a la classe: {Pred}")