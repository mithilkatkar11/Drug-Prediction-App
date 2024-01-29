import streamlit as st
import pickle
import numpy as np 

st.title("Drug Prediction Systeam")

with open("xgb_classifier.pkl", "rb") as file:
    xgb_model = pickle.load(file)

def Predict_function(Age,Gender,BP,Cholesterol,Na_to_k):
    input_array = np.array([[Age,Gender,BP,Cholesterol,Na_to_k]])
    drug_prediction = xgb_model.predict(input_array)
    return drug_prediction

Age = st.slider("Age", min_value= 1, max_value= 100)
Gender = st.selectbox("Gender", ["Male", "Female"])
BP = st.selectbox("BP",["Low", "Normal", "High"])
Cholesterol = st.selectbox("Cholesterol", ["Normal","High"])
Na_to_k = st.slider("Na_to_k", min_value= 1, max_value= 50)

if not Gender or not BP or not Cholesterol:
    st.wite("Please make a selection for all dropdown menus.")
else:
    Gender = 1 if Gender == "Male" else 0
    BP_mapping = {"High" :0, "Low" :1, "Normal" :2}
    BP = BP_mapping[BP]
    Cholesterol = 1 if Cholesterol == "Normal" else 0

    if st.button("Predict"):
        st.write(f"User values are {Age,Gender,BP,Cholesterol,Na_to_k}")
        prediction = Predict_function(Age,Gender,BP,Cholesterol,Na_to_k)
        drug_dct = {0:"DrugA", 1:"DrugB", 2:"DrugC", 3:"DrugX", 4:"DrugY"}
        st.write(f"\n The Prediction is {drug_dct[prediction[0]]}")


