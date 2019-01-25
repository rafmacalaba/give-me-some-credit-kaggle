# Project for Optimized Ensembling/Stacking of different models

Original/Newbie Approach can be found in a kaggle public kernel: https://www.kaggle.com/leafar/give-me-some-credit

Models used:

Neural Nets: sklearn's MLPClassifier & Keras
XGBoost: XGBClassifier
LightGBM: LGBClassifier
LogisticRegression
RandomForestClassifier

5 Different models used for diversity:
Weak learners:
LogisticRegression
Neural Nets: (underfitting)

Strong learners:
XGBoost - best
LGB
RF
## Competition page

[Give Me Some Credit: Improve on the state of the art in credit scoring by predicting the probability that somebody will experience financial distress in the next two years.]
https://www.kaggle.com/c/GiveMeSomeCredit

Raw data can be located at the provided link under Data tab

or download via kaggle API using:
kaggle competitions download -c GiveMeSomeCredit

# HOW TO USE:
1. install requirements.txt (pip install -r requirements.txt)
2. download the dataset in the link from kaggle or use kaggle API
3. run Data Processor Original Dataset.ipynb
4. run Credit_Full Bayesian Model Training and Predictions.ipynb
5. output logs can be found in output.logs

# CREDITS
pipeline reference https://github.com/avsolatorio/world-bank-pover-t-tests-solution which was originally written in python 2. so I made changes to be used it in python 3.

Thanks to Aivin Solatorio https://github.com/avsolatorio for answering questions regarding the overall process.
