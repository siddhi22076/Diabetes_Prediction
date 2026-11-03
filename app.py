import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="AI Diabetes Prediction",
    page_icon="🩺",
    layout="wide"
)

model = joblib.load("diabetes_model.pkl")

menu = st.sidebar.selectbox(
    "Navigation",
    ["🏠 Home", "🩺 Prediction", "ℹ About"]
)

st.markdown("""
<style>
.main{
    background-color:#0E1117;
}
.stButton>button{
    width:100%;
    background:#00B4D8;
    color:white;
    border-radius:10px;
    height:3em;
    font-size:18px;
}
h1{
    color:#00B4D8;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

if menu == "🏠 Home":

    st.title("🩺 AI Diabetes Prediction System")

    col1,col2,col3 = st.columns([1,2,1])
    with col2:
     st.image(
          "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1200",width=500
        )

    st.markdown("""
    ## Welcome

    This application predicts whether a patient is at risk of diabetes using Machine Learning.

    ### Features
    ✅ Fast Prediction

    ✅ Random Forest Algorithm

    ✅ Easy to Use

    ✅ High Accuracy
    """)

elif menu == "🩺 Prediction":
    # Title
    st.title("🩺 Diabetes Prediction System")
    st.write("Enter the patient's health details below.")

    # Input fields
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)

    glucose = st.number_input("Glucose", min_value=0, max_value=300, value=120)

    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)

    skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)

    insulin = st.number_input("Insulin", min_value=0, max_value=900, value=79)

    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)

    diabetes_pedigree = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.5
    )

    age = st.number_input("Age", min_value=1, max_value=120, value=30)

    # Prediction button
    if st.button("Predict"):

        input_data = pd.DataFrame({
            "Pregnancies": [pregnancies],
            "Glucose": [glucose],
            "BloodPressure": [blood_pressure],
            "SkinThickness": [skin_thickness],
            "Insulin": [insulin],
            "BMI": [bmi],
            "DiabetesPedigreeFunction": [diabetes_pedigree],
            "Age": [age]
        })

        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)

        st.subheader("Prediction Result")

        if prediction[0] == 1:
            st.error("⚠️ High Risk of Diabetes")
        else:
            st.success("✅ Low Risk of Diabetes")

        st.progress(float(probability[0][1]))    

        st.write(f"**Risk Score:** {probability[0][1]*100:.2f}%")

elif menu == "ℹ About":

    st.title("About Project")

    st.write("""
    **Project Name**

    AI Based Diabetes Prediction System

    **Algorithm**
    - Random Forest Classifier

    **Language**
    - Python

    **Framework**
    - Streamlit

    **Dataset**
    - Pima Indians Diabetes Dataset

    **Developer**
    - Siddhi Burbure
    """)

    st.markdown("---")
st.caption("Developed by Siddhi Burbure | BCA Final Year")