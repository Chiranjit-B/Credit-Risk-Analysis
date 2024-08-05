# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/162cDCToxKhzdnpkFs6Nh8AgTMn0v1Hhf
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, Markdown, Latex

sns.set_style('whitegrid')

from sklearn.preprocessing import LabelEncoder
from sklearn import model_selection
from sklearn.cluster import KMeans
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import f1_score

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/Credit Risk Analysis/german_credit_data_with_target.csv")
df.head(10)

df.info()

df.columns

df.isna().sum()

""" PERFORMING EXPLORATORY DATA ANALYSIS """

fig, ax = plt.subplots(1,2,figsize=(15,5))
sns.histplot(df, x='Age', bins=30, hue="Sex", ax=ax[0]).set_title("Age/Sex Distribution");
sns.boxplot(data=df, x="Sex", y="Age", ax=ax[1]).set_title("Age/Sex Distribution");

fig, ax = plt.subplots(1,2,figsize=(15,5))
sns.boxplot(data=df, x='Risk', y='Age', ax=ax[0]).set_title("Age Distribution with Risk");
sns.countplot(data=df, x="Sex", hue="Risk", ax=ax[1]).set_title("Sex Distribution with Risk");

# Define a function to map the job numbers to their descriptions using if-else statements
def job_description_encoder(job_code):
    if job_code == 0:
        return 'unskilled and non-resident'
    elif job_code == 1:
        return 'unskilled and resident'
    elif job_code == 2:
        return 'skilled'
    elif job_code == 3:
        return 'highly skilled'
    else:
        return 'unknown'

# Apply the function to create a new column 'Job Description'
df['Job Description'] = df['Job'].apply(job_description_encoder)

# Display the first few rows to verify the new column
df[['Job', 'Job Description']].head()

fig, ax = plt.subplots(1,2, figsize=(15,5))
sns.countplot(data=df, x="Saving accounts", hue="Risk", ax=ax[0]).set_title("Saving Account Quality Distribution with Risk");
sns.countplot(data=df, x="Checking account", hue="Risk", ax=ax[1]).set_title("Checking Account Quality Distribution with Risk");

fig, ax = plt.subplots(1,2, figsize=(20,5))
sns.countplot(data=df, x="Job Description", hue="Risk", ax=ax[0]).set_title("Job Distribution with Risk");
sns.countplot(data=df, x="Housing", hue="Risk", ax=ax[1]).set_title("Housing Distribution with Risk");

""" PERFORMING DATA PRE-PROCESSING """

# label encode account quality and fill NaN with 0
def H_LabelEncoder(text):
    if text == "free":
        return 0
    elif text == "rent":
        return 1
    elif text == "own":
        return 2

df["Housing"] = df["Housing"].apply(H_LabelEncoder)
print(df['Housing'])

# label encode account quality and fill NaN with 0
def SC_LabelEncoder(text):
    if text == "little":
        return 1
    elif text == "moderate":
        return 2
    elif text == "quite rich":
        return 3
    elif text == "rich":
        return 4
    else:
        return 0

df["Saving accounts"] = df["Saving accounts"].apply(SC_LabelEncoder)
df["Checking account"] = df["Checking account"].apply(SC_LabelEncoder)

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Calculate the correlation matrix
corr = df[['Age', 'Job', 'Housing', 'Saving accounts', 'Checking account', 'Credit amount', 'Duration']].corr()

# Set the size of the heatmap
sns.set(rc={'figure.figsize':(11, 7)})

# Create the heatmap with the corrected mask
sns.heatmap(corr, linewidths=.5, annot=True, cmap="YlGnBu", mask=np.triu(np.ones_like(corr, dtype=bool))) \
    .set_title("Pearson Correlations Heatmap")

# Show the plot
plt.show()

""" Label Encoding Categorical Data """

# use LabelEncoder() to encode other categorical columns:
for col in ["Sex", "Purpose", "Risk"]:
    le = LabelEncoder()
    le.fit(df[col])
    df[col] = le.transform(df[col])

df.drop('Job Description', axis=1, inplace=True)

df.head(10)

"""  TRAIN-TEST SPLIT """

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

y.value_counts()

"""from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

# Split the data into features (X) and target (y)
X = df.drop('Risk', axis=1)
y = df['Risk']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMote to the training data
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# Display the shape of the original and resampled data
print(f'Original training set shape: {X_train.shape, y_train.shape}')
print(f'Resampled training set shape: {X_train_smote.shape, y_train_smote.shape}')
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

# Define the parameter grid for Grid Search
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30],
    'max_features': ['auto', 'sqrt', 'log2']
}

# Initialize the RandomForestClassifier
rf = RandomForestClassifier(random_state=42)

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2, scoring='accuracy')

# Fit GridSearchCV on the training data
grid_search.fit(X_train_smote, y_train_smote)

# Get the best parameters and best estimator
best_params = grid_search.best_params_
best_rf = grid_search.best_estimator_

# Print the best parameters
print(f'Best parameters found: {best_params}')

# Train the RandomForestClassifier with the best parameters on the full training set
best_rf.fit(X_train_smote, y_train_smote)

# Predict on the test set
y_pred = best_rf.predict(X_test)

# Print classification report
print(classification_report(y_test, y_pred))

from sklearn.metrics import accuracy_score
# Train the RandomForestClassifier with the best parameters on the full training set
best_rf.fit(X_train_smote, y_train_smote)

# Predict on the test set
y_pred = best_rf.predict(X_test)

# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

import xgboost as xgb
from sklearn.model_selection import RandomizedSearchCV

# Define parameter grid for XGBoost
param_grid = {
    'n_estimators': [10, 50, 100, 200, 300,500],
    'learning_rate': [0.01, 0.1, 0.2, 1, 2,5,10,20, 50],
    'max_depth': [5, 10, 20, 50, 100, 200, 250],
    'subsample': [0.7, 0.8, 0.9, 1.0],
    'colsample_bytree': [0.7, 0.8, 0.9, 1.0]
}

# Initialize XGBoost
xgb_model = xgb.XGBClassifier(random_state=42)

# Initialize RandomizedSearchCV
random_search = RandomizedSearchCV(estimator=xgb_model, param_distributions=param_grid, cv=5, n_jobs=-1, verbose=2, scoring='accuracy')

# Fit RandomizedSearchCV on the training data
random_search.fit(X_train_smote, y_train_smote)

# Get the best parameters and best estimator
best_xgb = random_search.best_estimator_

# Predict on the test set
y_pred = best_xgb.predict(X_test)

# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

import xgboost as xgb
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

# Define parameter grid for XGBoost
param_grid = {
    'n_estimators': [10, 50, 100, 200, 300,500],
    'learning_rate': [0.01, 0.1, 0.2, 1, 2,5,10,20, 50],
    'max_depth': [5, 10, 20, 50, 100, 200, 250],
    'subsample': [0.7, 0.8, 0.9, 1.0],
    'colsample_bytree': [0.7, 0.8, 0.9, 1.0]
}

# Initialize XGBoost
xgb_model = xgb.XGBClassifier(random_state=42)

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=xgb_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2, scoring='accuracy')

# Fit GridSearchCV on the training data
grid_search.fit(X_train_smote, y_train_smote)

# Get the best parameters and best estimator
best_params = grid_search.best_params_
best_xgb = grid_search.best_estimator_

# Print the best parameters
print(f'Best parameters found: {best_params}')

# Train the XGBoostClassifier with the best parameters on the full training set
best_xgb.fit(X_train_smote, y_train_smote)

# Predict on the test set
y_pred = best_xgb.predict(X_test)

# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Get the best parameters and best estimator
best_params = grid_search.best_params_
best_xgb = grid_search.best_estimator_

# Print the best parameters
print(f'Best parameters found: {best_params}')

# Train the XGBoostClassifier with the best parameters on the full training set
best_xgb.fit(X_train_smote, y_train_smote)

# Predict on the test set
y_pred = best_xgb.predict(X_test)

# Calculate performance metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label=1, average='binary')
recall = recall_score(y_test, y_pred, pos_label=1, average='binary')
f1 = f1_score(y_test, y_pred, pos_label=1, average='binary')

# Print performance metrics
print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
print(f'Classification Report:\n {classification_report(y_test, y_pred)}')

""" CLUSTERING APPROACH """

cdf = pd.read_csv("/content/drive/MyDrive/Credit Risk Analysis/german_credit_data_with_target.csv")



cdf = df.drop("Risk", axis = 1)
cdf.head(10)

""" finding the best number of clusters for optimum solution b/w 2 and 16 clusters """

inertias = []

for i in range(2,16):
    kmeans = KMeans(n_clusters=i, random_state=0).fit(cdf)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
plt.title('Inertias v.s. N_Clusters')
plt.plot(np.arange(2,16),inertias, marker='o', lw=2);

""" Analysis: The "elbow" in above chart is indicated at 4. The number of clusters chosen should therefore be 4. """

km = KMeans(n_clusters=4, random_state=0)
clusters = km.fit_predict(cdf)
df_clustered = cdf[['Age', 'Job', 'Housing', 'Saving accounts', 'Checking account', 'Credit amount', 'Duration']]
df_clustered["Cluster"] = clusters
sns.pairplot(df_clustered[['Age', 'Job', 'Housing', 'Saving accounts', 'Checking account', 'Credit amount', 'Duration', "Cluster"]], hue="Cluster");

""" BUT SINCE THERE ARE ONLY Categories in output,
i.e : "good" and "bad", therefore we are using 2 cluster classification model """

X, y = df.drop("Risk", axis=1), df["Risk"]
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.20, random_state=0)

max_score = 0
max_k = 0
for k in range(1, 100):
    neigh = KNeighborsClassifier(n_neighbors=k)
    neigh.fit(X_train,y_train)
    score = f1_score(y_test, neigh.predict(X_test))
    if score > max_score:
        max_k = k
        max_score = score

display(Markdown("If use K-Nearest Neighbors Classification, the k should be " + str(max_k) + " to get best prediction, and then the  mean accuracy is " + str(max_score)))

from sklearn import model_selection
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import pandas as pd

# Define models
Models = {
    "SVC": SVC(),
    "DecisionTree": DecisionTreeClassifier(),
    "RandomForest": RandomForestClassifier(),
    "GaussianNaiveBayes": GaussianNB()
}

# Initialize a list to collect results
cv_results_list = []

for key in Models.keys():
    cv_res = model_selection.cross_validate(Models[key], X_train, y_train,
                                             return_train_score=True,
                                             scoring="f1",
                                             cv=5, n_jobs=-1)
    res = {
        'model': key,
        'train_score': cv_res["train_score"].mean(),
        'test_score': cv_res["test_score"].mean(),
        'fit_time': cv_res["fit_time"].mean(),
        'score_time': cv_res["score_time"].mean(),
        }
    cv_results_list.append(res)
    print("CV for model:", key, "done.")

# Convert results list to DataFrame
cv_results = pd.DataFrame(cv_results_list)

cv_results

""" from the above result it is sage to assume that Random Forest is the
best Model for this problem statement considering the dataset"""

rf = Models["RandomForest"].fit(X_train, y_train)
print('f1_score:', f1_score(y_test, rf.predict(X_test)))

