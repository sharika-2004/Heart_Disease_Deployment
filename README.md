# Heart Disease Prediction using Machine Learning

## Overview

This project demonstrates an end-to-end machine learning deployment pipeline for predicting the risk of heart disease based on clinical parameters. The model is developed using the Heart Disease dataset, exposed through a Flask REST API, version-controlled using GitHub, and deployed as a live web service on Render.

## Dataset

- **Dataset:** Heart Disease Prediction Dataset
- **Source:** https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Joblib
- Gunicorn
- GitHub
- Render

## Machine Learning Model

**Algorithm Used:** Random Forest Classifier

## Model Performance

| Metric | Value |
|--------|--------|
| Accuracy | **98.54%** |

## Project Structure

```text
HeartDiseaseDeployment/
│
├── app.py
├── train_model.py
├── model.pkl
├── heart.csv
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

## Live Deployment

The application has been successfully deployed on Render and is publicly accessible at:

**https://heart-disease-deployment-kl2w.onrender.com/**

## Conclusion

This project successfully demonstrates the complete workflow of deploying a machine learning model from development to production. A Random Forest Classifier was trained using the Heart Disease dataset and achieved an accuracy of **98.54%** on the test data. The trained model was serialized using Joblib and integrated into a Flask REST API capable of receiving patient information in JSON format and returning prediction results. The application was version-controlled using GitHub and deployed on Render as a publicly accessible web service. This project highlights the importance of MLOps practices such as model packaging, version control, API development, and cloud deployment for delivering scalable and reliable machine learning applications.
