# 🚀 Credit Risk Analysis Project 📊💳

Welcome to the **Credit Risk Analysis** project! This repository contains a comprehensive analysis and classification of credit risks using various machine learning techniques. Dive in to explore how we transform raw data into actionable insights. 🎉

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

## 🤖 Models Used
We experimented with several models to find the best predictor:
- **Support Vector Classifier (SVC)**
- **Decision Tree Classifier**
- **Random Forest Classifier**
- **Gaussian Naive Bayes**

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
