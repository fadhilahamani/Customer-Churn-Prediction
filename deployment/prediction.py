import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import joblib

def run():
    # Load Model
    with open('preprocessor.pkl', 'rb') as file_1:
        preprocessor = joblib.load(file_1)
    model = load_model('churn_model.h5')

    # Membuat Title
    st.title('Customer Churn Prediction')

    # Membuat sub header
    st.subheader('This Form is For Predict The Category of Customer Churn')
    st.markdown('---')
    # Membuat form
    with st.form(key='form_paramters'):
        col1, col2, = st.columns(2)
        with col1:
            customer = st.text_input('customerID')
            gender = st.selectbox('gender', ('Male', 'Female'), index=0)
            senior = st.selectbox('SeniorCitizen', ('No', 'Yes'), index=0)
            partner = st.selectbox('Partner', ('No', 'Yes'), index=0)
            dependents = st.selectbox('Dependents', ('No', 'Yes'), index=0)
            tenure = st.number_input('tenure', min_value=0, max_value=100, value=0)
            phone = st.selectbox('PhoneService', ('No', 'Yes'), index=0)
            lines = st.selectbox('MultipleLines', ('No', 'Yes'), index=0)
            internet = st.selectbox('InternetService', ('DSL', 'Fiber Optic', 'No'), index=0)
            security = st.selectbox('OnlineSecurity', ('No', 'Yes'), index=0)
        with col2:
            backup = st.selectbox('OnlineBackup', ('No', 'Yes'), index=0)
            protection = st.selectbox('DeviceProtection', ('No', 'Yes'), index=0)
            support= st.selectbox('TechSupport', ('No', 'Yes'), index=0)
            tv = st.selectbox('StreamingTV', ('No', 'Yes'), index=0)
            movies = st.selectbox('StreamingMovies', ('No', 'Yes'), index=0)
            contract = st.selectbox('Contract', ('Month-to-month', 'One year', 'Two year'), index=0)
            billing = st.selectbox('PaperlessBilling', ('No', 'Yes'), index=0)
            payment = st.selectbox('PaymentMethod', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'), index=0)
            monthly = st.number_input('MonthlyCharges', min_value=0.0, max_value=1000.0, value=0.0, format="%.1f")
            total = st.number_input('TotalCharges', min_value=0.0, max_value=10000.0, value=0.0, format="%.1f")
        st.markdown('---')
        
        submitted = st.form_submit_button('Predict')

        data_inf = {
            'customerID': customer,
            'gender': gender,
            'SeniorCitizen': senior,
            'Partner': partner,
            'Dependents': dependents,
            'tenure': tenure,
            'PhoneService': phone,
            'MultipleLines': lines,
            'InternetService': internet,
            'OnlineSecurity': security,
            'OnlineBackup': backup,
            'DeviceProtection': protection,
            'TechSupport': support,
            'StreamingTV': tv,
            'StreamingMovies': movies,
            'Contract': contract,
            'PaperlessBilling': billing,
            'PaymentMethod': payment,
            'MonthlyCharges': monthly,
            'TotalCharges': total
        }

        data_inf = pd.DataFrame([data_inf])
    
        if submitted:
            # Feature Encoding dan Feature Scaling untuk data inference
            data_inf_final = preprocessor.transform(data_inf)

            y_pred_inf = model.predict(data_inf_final)
            
            # Mengubah hasil prediksi sesuai dengan kategori kelas
            y_pred = []
            for val in y_pred_inf:
                if val >= 0.5:
                    y_pred.append('Yes')
                    st.write('## Churn')
                else:
                    y_pred.append('No')
                    st.write('## No Churn')
            y_pred[:10]
        
if __name__ == '__main__':
    run()