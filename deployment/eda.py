import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run():
    # Membuat Title
    st.title('Exploratory Data Analysis (EDA)')

    # Membuat sub header
    st.subheader('EDA for Analysis Dataset Telco Customer Churn')

    # Membuat deskripsi
    st.write('This page is made by *Fadhilah Amani*')

    # Membuat Garis Lurus
    st.markdown('---')

    # Magic Syntax
    '''
    This page contains Exploratory Data Analysis of Customer in Telecommunication Company.
    The dataset's source is from kaggle.com.
    '''
    
    # Show dataframe
    data = pd.read_csv('h8dsft_Milestone1P2_fadhilah_amani_alam_aulia.csv')
    st.dataframe(data)

    # Mengubah tipe data 'TotalCharges' dari object menjadi numerik
    data.TotalCharges = pd.to_numeric(data.TotalCharges, errors='coerce')

    # Membuat histogram berdasarkan input user
    st.write('### Histogram Chart')
    opt = st.selectbox('Select Columns : ', ('tenure', 'MonthlyCharges', 'TotalCharges'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[opt], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat BarPlot
    st.write('### Bar Chart For Total Customer Churn')
    fig = plt.figure(figsize = (13,5))
    ax = sns.countplot(x='Churn', data=data)
    ax.bar_label(ax.containers[0])
    st.pyplot(fig)

    # Mengubah tipe data 'SeniorCitizen' menjadi object
    data.SeniorCitizen.replace(0, 'No', inplace=True)
    data.SeniorCitizen.replace(1, 'Yes', inplace=True)
    data = data.astype({"SeniorCitizen": object})

    # Mengubah nilai 'No Phone Service' dan 'No Internet Service' menjadi 'No
    data.replace('No internet service', 'No', inplace = True)
    data.replace('No phone service', 'No', inplace = True)

    st.write('### Bar Chart Based On Categories')
    opt1 = st.selectbox('Select Columns : ', ('gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'))
    fig = plt.figure(figsize = (13,5))
    ax = sns.countplot(x=data[opt1], data=data)
    ax.bar_label(ax.containers[0])
    st.pyplot(fig)

if __name__ == '__main__':
    run()