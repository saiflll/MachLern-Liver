%%writefile.app.py
import pickle
import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Judul Aplikasi
st.title("Aplikasi Prediksi Penyakit Liver")

# Input Data
st.sidebar.header("Input Parameter")
def user_input_features():
    Age = st.sidebar.number_input("Age 20-100", 20, 100, 50)
    Gender = st.sidebar.selectbox("Gender (0 = Female, 1 = Male)", (0, 1))
    Total_Bilirubin = st.sidebar.number_input("Total Bilirubin 0-8", 0.1, 8.0, 1.0)
    Direct_Bilirubin = st.sidebar.number_input("Direct Bilirubin 0-8", 0.1, 8.0, 0.5)
    Alkaline_Phosphotase = st.sidebar.number_input("Alkaline Phosphotase 70-800", 70, 3000, 200)
    Alamine_Aminotransferase = st.sidebar.number_input("Alamine Aminotransferase 100-2000", 10, 2000, 100)
    Aspartate_Aminotransferase = st.sidebar.number_input("Aspartate Aminotransferase 10-3000", 10, 3000, 100)
    Total_Protiens = st.sidebar.number_input("Total Protiens 2-10", 2.0, 10.0, 6.0)
    Albumin = st.sidebar.number_input("Albumin 2-6 ", 2.0, 6.0, 4.0)
    Albumin_and_Globulin_Ratio = st.sidebar.number_input("Albumin and Globulin Ratio 0-3 ", 0.1, 2.5, 1.0)
