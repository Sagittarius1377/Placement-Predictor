#  Placement Predictor

An end-to-end Machine Learning project that predicts whether a student is likely to be placed based on academic performance and skill metrics.

This project demonstrates how a data science model can be transformed into a **production-ready application** using modular architecture and containerization.

---

##  Overview

The system takes student-related inputs (such as academic scores, skills, etc.) and predicts placement probability using a lightweight probabilistic model.

It is designed with **real-world deployment practices**, including:

* Model serialization
* API-based inference
* Frontend-backend separation
* Docker containerization

---

## 🏗️ Architecture

```
User → Frontend (Streamlit) → Backend API → ML Model → Prediction
```

### Components:

* **Frontend (`frontend.py`)**

  * Built using Streamlit
  * Collects user input
  * Displays prediction results

* **Backend (`backend.py`)**

  * Handles inference logic
  * Loads precomputed model parameters
  * Returns prediction via API

* **Machine Learning Model**

  * PCA (Dimensionality Reduction)
  * Gaussian Naive Bayes (Probabilistic Model)

---

## 📂 Project Structure

```text
├── .gitignore
├── __init__.py
├── backend.py
├── frontend.py
├── config.py
├── ds-project-1.ipynb
├── college_student_placement_dataset.csv
├── eigen_vectors.npy
├── likelihood_distribution_params.pkl
├── requirements.txt
├── start-backend-frontend.sh
├── Dockerfile
```

---

## ⚙️ Features

* ✅ End-to-end ML pipeline
* ✅ Lightweight inference using saved parameters
* ✅ Interactive UI (Streamlit)
* ✅ Backend API integration
* ✅ Dockerized application
* ✅ Modular and scalable structure

---

    ## 🐳 Run with Docker (Without Docker Compose)

### Step 1: Clone the repository

```bash
git clone https://github.com/Sagittarius1377/Placement-Predictor.git
cd Placement-Predictor
```

---

### Step 2: Build Docker Images

```bash
# Build backend image
docker build -t placement-backend -f Docker_Files/backend-dockerfile .

# Build frontend image
docker build -t placement-frontend -f Docker_Files/frontend-dockerfile .
```

---

### Step 3: Run Containers

```bash
# Run backend container
docker run -d -p 5000:5000 placement-backend

# Run frontend container
docker run -d -p 8501:8501 placement-frontend
```

---

### Step 4: Open in Browser

Frontend:

```
http://localhost:8501
```

---

## 💻 Run Locally (Without Docker)

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 2: Run application

```bash
chmod +x start-backend-frontend.sh
./start-backend-frontend.sh
```

---

### Step 3: Open in Browser

```
http://localhost:8501
```

---

## 📊 Machine Learning Workflow

### 1. Data Preprocessing

* Cleaned and prepared dataset
* Handled features and structure

### 2. Dimensionality Reduction

* Applied PCA
* Stored transformation in `eigen_vectors.npy`

### 3. Model Training

* Used Gaussian Naive Bayes
* Saved parameters in `likelihood_distribution_params.pkl`

### 4. Inference Optimization

* Avoided loading heavy models
* Used mathematical parameters directly → faster predictions

---

## 🛠️ Tech Stack

* **Programming:** Python, Bash
* **ML Libraries:** NumPy, Pandas, Scikit-learn
* **Frontend:** Streamlit
* **Deployment:** Docker

---

## ✨ Key Highlights

* Transitioned from notebook → production application
* Efficient model serving using serialized parameters
* Clean separation of frontend and backend
* Containerized for reproducibility and scalability

---



