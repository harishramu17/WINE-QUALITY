# Wine Quality Prediction using RandomForestClassifier

![download](https://github.com/harishramu17/WINE-QUALITY/assets/107133605/a0973490-557b-40c3-960c-703d38fb1858)



<h2>Introduction<br></h2>
<p>This project aims to build a Wine Quality Prediction model using the RandomForestClassifier from the scikit-learn library. The model will be trained on a dataset containing various attributes of wine samples, and it will predict the quality of wine as a categorical label (e.g., Fixed acidity,Volatile acidity,Citric acid,Residual sugar,Chlorides,Free sulfur dioxide,Total sulfur dioxide,Density,pH
,Sulphates
,Alcohol).</p>

<h2>Dataset<br></h2>
<p>The dataset used for this project is sourced from UCI Machine Learning Repository. It consists of two datasets, one for red wine samples and another for white wine samples. Each dataset contains several chemical and sensory features of wines and their corresponding quality ratings by wine experts.</p>

<h2>Attributes in the dataset include:<br></h2>

1.Fixed acidity<br>
2.Volatile acidity<br>
3.Citric acid<br>
4.Residual sugar<br>
5.Chlorides<br>
6.Free sulfur dioxide<br>
7.Total sulfur dioxide<br>
8.Density<br>
9.pH<br>
10.Sulphates<br>
11.Alcohol<br>
The target variable is the "Quality" column, which represents the quality rating of the wine.

<h2>Data Preprocessing<br></h2>
Before training the RandomForestClassifier, we preprocess the data to handle missing values, normalize or scale features, and encode the target variable into categorical labels. We also split the data into training and testing sets to evaluate the model's performance.

<h2>Model Training<br></h2>
The RandomForestClassifier is used to train the Wine Quality Prediction model on the preprocessed training data. RandomForest is an ensemble learning method that builds multiple decision trees during training and combines their predictions to make more accurate predictions.

<h2>Evaluation<br></h2>
After training the model, we evaluate its performance on the test data using various metrics, including accuracy, precision, recall, and F1-score. These metrics provide insights into how well the model performs in predicting the wine quality.
