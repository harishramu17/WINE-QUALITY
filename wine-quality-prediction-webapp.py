import streamlit as st
import pickle
import numpy as np


loaded_model=pickle.load(open("C:/Users/mdjit/OneDrive/Desktop/devlop/Wine-Quality-Prediction/trained_model .sav",'rb'))

def wine_quality_prediction(input_data):

    input_arr=np.array(input_data)
    inputs_array=input_arr.reshape(1,-1)
    inputs_array
    if (loaded_model.predict(inputs_array))==1:
        return " QUALITY OF WINE IS FIXED ACIDITY "
    elif(loaded_model.predict(inputs_array))==2:
        return " QUALITY OF WINE IS VOLATILE ACIDITY "
    elif(loaded_model.predict(inputs_array))==3:
        return " QUALITY OF WINE IS CITRIC ACID "
    elif(loaded_model.predict(inputs_array))==4:
        return " QUALITY OF WINE IS RESIDUAL SUGAR "
    elif(loaded_model.predict(inputs_array))==5:
        return " QUALITY OF WINE IS CHLORIDES"
    elif(loaded_model.predict(inputs_array))==6:
        return " QUALITY OF WINE IS FREE SULFUR DIOXIDE "
    elif(loaded_model.predict(inputs_array))==7:
        return " QUALITY OF WINE IS TOTAL SULPHUR DIOXIDE "
    elif(loaded_model.predict(inputs_array))==8:
        return " QUALITY OF WINE IS DENSITY "
    elif(loaded_model.predict(inputs_array))==9:
        return " QUALITY OF WINE IS pH"
    elif(loaded_model.predict(inputs_array))==10:
        return " QUALITY OF WINE IS SULPHATES"
    elif(loaded_model.predict(inputs_array))==11:
        return " QUALITY OF WINE IS ALCOHOL "
    else:
        return "IT IS BEST QUALITY OF WINE"
    


    
def main():

    st.title("WINE QUALITY PREDICTION")

    fixed_acidity =st.number_input("FIXED ACIDITY OF WINE")
    volatile_acidity=st.number_input("VOLATILE ACIDITY")
    citric_acid=st.number_input("CITRIC ACID")
    chlorides=st.number_input("CHLORIDES")
    total_sulfhur_dioxide=st.number_input("TOTAL SULPHUR DIOXIDE")
    density=st.number_input("DENSITY")
    sulphates=st.number_input("SULPHATES")
    alcohol=st.number_input("ALCOHOL")







    diagnosis=""


    if st.button("Wine Quality Test Result"):
        diagnosis = wine_quality_prediction([fixed_acidity,volatile_acidity,citric_acid,chlorides,total_sulfhur_dioxide,density,sulphates,alcohol])
        
    st.success(diagnosis)


if __name__ == '__main__':
    main()

