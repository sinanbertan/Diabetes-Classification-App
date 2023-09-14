
# Indians-Diabetes-Classification-EDA-App
- This project focuses on prediction if patient are diabetes or not. The project includes machine learning, exploratory data analysis (EDA), and data visualization techniques to gain insights into the dataset and understand its patterns. The project uses the diabetes.csv dataset, which can be downloaded from Kaggle: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database


# ACKNOWLEDGEMENTS

### DATA CONTENT

* Pregnancies: Number of times pregnant

* Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test

* BloodPressure: Diastolic blood pressure (mm Hg)

* SkinThickness: Triceps skin fold thickness (mm)

* Insulin: 2-Hour serum insulin (mu U/ml)

* BMI: Body mass index (weight in kg/(height in m)^2)

* DiabetesPedigreeFunction: Diabetes pedigree function

* Age: Age (years)

* Outcome: Class variable (0 or 1) 268 of 768 are 1, the others are 0

## Installation
The following tools were used for this analysis:

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scipy
- Sklearn

- To run this project, you will need to have Python 3 installed on your machine. You can install the required libraries by running the following command:


- pip install pandas matplotlib seaborn numpy plotly Sklearn 
## Usage 
- To run the analysis, simply execute the notebook. The script will generate several visualizations that help illustrate analysis of data.
## Roadmap

[1. IMPORTING LIBRARIES](#1)
    
[2. LOADING DATA](#2)  

[3. DATA CONTENT](#3)

[4. EXPLORATORY DATA ANALYSIS](#4)

[5. DATA VISUALIZATION](#5)

[6. OUTLIER DETECTION](#6)

[7. DATA PREPROCESSING](#7)

[8. MODEL TRAINING AND EVALUATING](#8)

[9. FEATURE IMPORTANCE](#9)

[10. AUC-ROC CURVE](#10)

[11. MODEL TUNING](#11)

[12. CONCLUSION](#12)


 The analysis includes visualizations using Matplotlib, Plotly and Seaborn.

## Contributing

- Contributions to this project are welcome. If you notice any errors or have ideas for additional analyses, please feel free to open an issue or submit a pull request.

## Application screenshots:
![img1]()
![img2]()


## Conclusion 

*  After I have done the Exploratory Data Analysis, I have found out that there are outliers in the dataset. I have used the IQR method to fill the outliers with median. And then I have done data visualization to get insight from data. After that I have built Classification models and trained them. After model tuning , I got %78.00 accuracy score from LGBMclassifier.

