import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image


# Load the model
model=pickle.load(open("C:/Users/ssbgt/OneDrive/Masaüstü/BUSSINES/DATA RELATED/DATA ANALYTICS/PROJECTS/Indians-Diabetes-Classification/diabetes.sav","rb"))

img=Image.open("C:/Users/ssbgt/OneDrive/Masaüstü/BUSSINES/DATA RELATED/DATA ANALYTICS/PROJECTS/Indians-Diabetes-Classification/img.jpg")

def predict_diabetes(input_data):

    # Changing input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # Reshape the array as we are predicting for one instance
    std_data = input_data_as_numpy_array.reshape(1, -1)
    # Standardize the input data
    prediction = model.predict(std_data)
    print(prediction)
    if prediction[0] == 0:
        return "The person is not diabetic"
    else:
        return "The person is diabetic"


def main():
    
    # title:
    st.title("Diabetes Prediction app")
    
    #subheader:
    st.subheader("Diabetes Prediction based on the given features")
    
    #text
    st.text("Goal of this app is to predict whether a person is diabetic or not based on the given features") 
    
    # adding image files:
    st.image(img, caption='diabetes')  
    
    # using html-css codes: 
    st.markdown("""
<style>
body {
    background-color: #F5F5F5;
    font-family: 'Arial', sans-serif;
}

img {
    align:center; 
    border:10;
    border-color:cyan;
    border-style:dashed;
}

h1 {
    color: #006D77;
    text-align: center;
}

h2 {
    color: #006D77;
}


button {
    background-color: #006D77;
    color: white;
}

button:hover {
    background-color: #005161;
}
</style>
""", unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; color: cyan;'>Enter the required details</h3>", unsafe_allow_html=True)
    
    # write: you can use it for eveything
    
    st.write("Please enter the required details in the sidebar")
    
    # input data:
    Pregnancies = st.sidebar.slider("Pregnancies",0,17,1)
    Age = st.sidebar.slider("Age",12,99,1)
    Glucose = st.text_input("Glucose")
    BloodPressure = st.text_input("BloodPressure")
    SkinThickness = st.text_input("SkinThickness")
    Insulin = st.text_input("Insulin")
    Bmi = st.text_input("BMI")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
    
    
    # prediction code:
    
    diag=""
    
    # button:
    if st.button("Diabetes Test Result"):
        diag=predict_diabetes([Pregnancies, Glucose, BloodPressure,
                               SkinThickness, Insulin, Bmi,
                               DiabetesPedigreeFunction, Age])
    
    # success of prediction
    st.success(diag)
    
if __name__ == "__main__":
    main()