# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:36:06 2021

@author: andre
"""

## Import pandas package
import pandas as pd

## Import T-test package
from scipy.stats import ttest_ind

## Create the dataframe
diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

## Retrieve the list of column names from dataset
list(diabetes)

### Question 1: Is there a difference between sex (M:F) and the number of days in hospital?
## Creating variables
Male = diabetes[diabetes['gender']=='Male']
Female = diabetes[diabetes['gender']=='Female']


## Question 1 T-test
ttest_ind(Male['time_in_hospital'], Female['time_in_hospital'])

## T-test Results 1
## statistic=9.542637042242887, pvalue=1.4217299655114968e-21

### Conclusion 1
## The p-value is less than 0.05. This indicates there is a significant difference between males and females for the number of days in the hospital.

### Question 2: Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?
## Creating variables
Caucasian = diabetes[diabetes['race'] == 'Caucasian'] 
African_American = diabetes[diabetes['race'] == 'AfricanAmerican']

## Question 2 T-test
ttest_ind(Caucasian['time_in_hospital'], African_American ['time_in_hospital'])

## T-test Results 2
## statistic=-5.0610017032095325, pvalue=4.178330085585203e-07

### Conclusion 2
## The p-value is less than 0.05. This indicates there is a significant difference between Caucasians and African Americans for the number of days in the hospital.

### Question 3: Is there a difference between RACE (Asian and African American) and the number of lab procedures performed?
## Creating variable
Asian = diabetes[diabetes['race']=='Asian']

## Question 3 T-test
ttest_ind(Asian['num_lab_procedures'], African_American['num_lab_procedures'])

## T-test Results 3
## statistic=-3.9788715315360292, pvalue=6.948907528800307e-05

### Conclusion 3
## The p-value is less than 0.05. This indicates there is a significant difference between Asians and African Americans for number of lab procedures performed.