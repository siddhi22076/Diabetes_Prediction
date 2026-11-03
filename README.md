# 🩺 Diabetes Prediction System

A machine learning-based web application that predicts the likelihood of diabetes using patient health-related information.

The application uses a trained Random Forest Classification model to analyze medical input parameters and generate a diabetes prediction through a simple and interactive Streamlit interface.

## 🚀 Features

- User-friendly web interface built with Streamlit
- Predict diabetes using health-related input parameters
- Machine Learning model using Random Forest Classifier
- Instant prediction results
- Pre-trained model integration using a `.pkl` file
- Simple and interactive user experience

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Streamlit | Web application interface |
| Scikit-learn | Machine Learning |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Pickle | Model serialization |

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd Diabetes_Prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 🧠 Machine Learning Model

**Algorithm:** Random Forest Classifier

The trained model processes patient health parameters and predicts whether the input data indicates a likelihood of diabetes.

## 🎯 Project Objective

The objective of this project is to explore the practical application of machine learning in healthcare by developing a simple prediction system that demonstrates how patient health data can be used for classification.

## 🔮 Future Enhancements

- Improve model accuracy through hyperparameter tuning
- Add more machine learning algorithms
- Display prediction probability
- Add data visualization and health insights
- Improve the user interface and reporting features

## ⚠️ Disclaimer

This application is developed for educational purposes only. Its predictions are not medical diagnoses and should not replace professional medical advice.

## 👩‍💻 Developer

Developed as a Python and Machine Learning project.

---

⭐ If you find this project useful, consider giving this repository a star!
