# 🌾 Crop Recommendation System using Streamlit

A smart crop recommendation system built using machine learning and deployed with Streamlit. This app helps farmers and agricultural experts identify the most suitable crop to grow based on soil and climate conditions.

---

## 📌 Project Features

- Predicts the best crop using **Naive Bayes** algorithm (chosen after comparing with other models)
- Accepts soil nutrients and weather inputs (N, P, K, Temperature, Humidity, pH, Rainfall)
- Clean and modern **Streamlit web interface**
- Displays recommended crop with an icon and helpful message
- Includes an interactive notebook for model comparison

---

## 📁 Project Structure
```
crop-recommendation/
├── Streamlit.py                # Main Streamlit app file (entry point)
├── Crop_Models.ipynb           # Jupyter notebook comparing ML models
├── Crop_recommendation.csv     # Dataset used for training and testing
├── requirements.txt            # List of required Python packages
├── naive_bayes_crop_model.pkl  # Saved Naive Bayes model (via pickle)
├── label_encoder.pkl           # Saved LabelEncoder for crop names
└── README.md                   # Project documentation
```

---
---
## 🚀 Live Demo

Try the app live here:  
🔗 [Streamlit App Link](https://crop-adviser.streamlit.app/)

---
---
## 🧪 Dataset

- File: `Crop_recommendation.csv`
- Features:
  - `N`, `P`, `K` — Macronutrients in the soil
  - `temperature`, `humidity` — Atmospheric conditions
  - `ph` — Acidity/alkalinity of the soil
  - `rainfall` — Water availability
- Target: `label` (Crop name)

---

## 🧠 Model Used

After evaluating several models in `Crop_Models.ipynb` including:
- Logistic Regression
- Decision Trees
- Random Forest
- KNN
- SVM
- **Naive Bayes ✅ (Chosen for best accuracy & speed)**

---
---
## 🛠️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/crop-recommendation.git
cd crop-recommendation
```

### 2️⃣ Install requirements

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app

```bash
streamlit run Streamlit.py
```

---
---
## 📦 Requirements

All dependencies are listed in `requirements.txt`. Major ones include:

- streamlit
- scikit-learn
- pandas
- numpy
- matplotlib (optional for future upgrades)
---
---

## 📜 License

This project is for educational purposes. Feel free to use and modify it for your use cas
---

