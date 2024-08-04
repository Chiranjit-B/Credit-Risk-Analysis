# 🚀 Credit Risk Analysis Project 📊💳

![Project Badge](https://img.shields.io/badge/Project-Credit%20Risk%20Analysis-brightgreen)
![EDA Badge](https://img.shields.io/badge/EDA-Exploratory%20Data%20Analysis-blue)
![Classification Model Badge](https://img.shields.io/badge/Model-Random%20Forest%20Classifier-orange)
![SMOTE Badge](https://img.shields.io/badge/SMOTE-Class%20Imbalance%20Handling-yellow)
![Clustering Badge](https://img.shields.io/badge/Clustering-KMeans%20Clustering-lightblue)
![Hyperparameter Tuning Badge](https://img.shields.io/badge/Hyperparameter%20Tuning-GridSearchCV-red)
![Accuracy Badge](https://img.shields.io/badge/Accuracy-82.5%25-green)

Welcome to the **Credit Risk Analysis** project! This repository contains a comprehensive analysis and classification of credit risks using various machine learning techniques. Dive in to explore how we transform raw data into actionable insights. 🎉

![image](https://github.com/user-attachments/assets/efc49fa7-288d-45c7-8dfb-978538bc03ca)


## 📚 Table of Contents
- [Introduction](#introduction)
- [Data Description](#data-description)
- [Project Workflow](#project-workflow)
- [Models Used](#models-used)
- [Results](#results)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

## 📝 Introduction
Credit risk analysis is crucial for financial institutions to determine the likelihood of a borrower defaulting on a loan. This project uses a dataset with various features to predict whether a loan applicant is a good or bad credit risk. Let's make data-driven decisions! 📈

## 📊 Data Description
The dataset includes the following columns:
- `Age`: Age of the applicant
- `Sex`: Gender of the applicant
- `Job`: Job type
- `Housing`: Housing status
- `Saving accounts`: Saving account status
- `Checking account`: Checking account status
- `Credit amount`: Credit amount requested
- `Duration`: Duration of the loan
- `Purpose`: Purpose of the loan
- `Risk`: Target variable (Good/Bad risk)

## 🔄 Project Workflow
Here's a high-level overview of the steps we took in this project:
1. **Data Preprocessing**: Cleaning and transforming the raw data 📋
2. **Exploratory Data Analysis (EDA)**: Understanding data distribution and relationships 🔍
3. **Cluster Analysis**: Using K-means to identify patterns and groupings within the data 📊
4. **Feature Engineering**: Creating new features from the clusters 🚀
5. **SMOTE Analysis**: Applying Synthetic Minority Over-sampling Technique (SMOTE) to handle class imbalance ⚖️
6. **Model Training**: Training various models to predict credit risk 🤖
7. **Hyperparameter Tuning and Grid Search**: Using GridSearchCV for hyperparameter tuning to find the best model parameters 🔧
8. **Model Evaluation**: Comparing models based on performance metrics 🏅

## ⚖️ SMOTE Analysis
SMOTE (Synthetic Minority Over-sampling Technique) is used to address class imbalance in the dataset. By generating synthetic samples for the minority class, SMOTE helps in improving the model's ability to correctly classify minority instances. In this project, SMOTE is applied to the training data to balance the 'Good' and 'Bad' risk categories.

## 🔧 Hyperparameter Tuning and Grid Search
Hyperparameter tuning is crucial for optimizing model performance. We use GridSearchCV to perform an exhaustive search over a specified parameter grid for each model. This helps in finding the best combination of hyperparameters that maximize the model's accuracy and other performance metrics. For example, we tune the number of estimators and the depth of trees for the Random Forest model.

## 🤖 Models Used
We experimented with several models to find the best predictor:
- **Support Vector Classifier (SVC)**
- **Decision Tree Classifier**
- **Random Forest Classifier**
- **Gaussian Naive Bayes**
- **K-Nearest Neighbors (KNN)**: KNN is a simple and effective classification algorithm that assigns a class to a sample based on the majority class of its k-nearest neighbors. In this project, KNN is used to explore its effectiveness in predicting credit risk.

## 🏆 Results
The Random Forest Classifier emerged as the top performer with the following metrics:
- **Accuracy**: 0.825
- **Precision**: 0.803
- **Recall**: 0.781
- **F1 Score**: 0.792

Detailed performance metrics for each model can be found in the `results` directory.

## 💻 How to Run
Follow these steps to run the project on your local machine:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/credit-risk-analysis.git
    cd credit-risk-analysis
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Jupyter Notebook**:
    ```sh
    jupyter notebook Credit_Risk_Analysis_Code.ipynb
    ```

## 🤝 Contributing
We welcome contributions! Feel free to open issues or submit pull requests. Check out our [contributing guidelines](CONTRIBUTING.md) for more information.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Let's predict and prevent credit risks together! 🚀📊
