![image](https://user-images.githubusercontent.com/111452227/217908785-8b81c481-f065-4008-8b1f-779e353147df.jpeg)









# Final_Project

### Diabetes Predictions

## Table of contents

Introduction

Method

Technologies

Results

Limitations

Conclusion

References

## Introduction

According to the CDC, the number of people who have diabetes in America is the highest it has ever been. People with diabetes have a deficiency in how their body makes or uses insulin.  Insulin is a important hormone that regulates glucose.  Without proper insulin regulation, patients can succumb to serious complications such as heart disease, vision loss, lower-limb amputation and kidney disease.  It is essential that healthcare providers have the tools to screen patients for prediabetes or diabetes.  The predictions can assist clinicians formulate a   In this project, we intend to use supervised machine learning (classification)to predict diabetes, prediabetes or no diabetes. 

## Method

We used the Diabetes Health Indicators Dataset from 2015 provided by Kaggle. The dataset was obtained by surveying hundreds of thousands of Americans for diabetes or prediabetes predictors with The Behavioral Risk Factor Surveillance System (BRFSS).  We decided to explore 10 of the 22 variables for our prediction. 

Variables:

Education

Age

High BP

Gender

BMI

Cholesterol check

No Doc bc Cost

Stroke

Smoker

Physical Activity



Some of the questions that we explored were age, diet, physical activity and health history.  The data that we chose did not require extensive clean-up such as dropping NaN or columns therefore we were able to proceed in creating the model.  

Diab

Before we were able to work with the dataset, we had to label the categories in some of the columns.  For example.  the income column had 8 

It was felt that a supervised machine learning was the best approach to classify and predict diabetes.  We used the tensorflow deep learning module. To compare for accuracy, we used the random forest method for this prediction.  We then began to build the webpage using HTML, Javascript, and Flask. To be continued...

Demonstrate and expand further the logistic model prediction since we had a higher accuracy... and then use tensorflow and random forest as additional analysis.   



## Technologies

Python 3.9.12

Javascript

HTML

Form & Postman

Flask

Tableau

## Results 

Accuracy = 86%
Outcomes:  0= No diabetes, 1= prediabetes, 2= diabetes

<img width="506" alt="image" src="https://user-images.githubusercontent.com/111452227/219551735-007f4bda-6a51-419e-8e80-566625b1d918.png">



### Charts and Visuals

High Blood Pressure

<img width="622" alt="image" src="https://user-images.githubusercontent.com/111452227/219551777-0a520155-ce31-4c71-a4c2-e4c814d4722a.png">

High Cholesterol

<img width="622" alt="image" src="https://user-images.githubusercontent.com/111452227/219551825-71086f21-017e-458d-a2e2-6b9c06b7df4d.png">



## Set backs

Connecting Flask with the database. 

We cannot expand on tensorflow (limited knowledge of the functions to make machine model connections with HTML) and random forest 

## Limitations

Greta: Time constraint did not allow to explore the deep learning method and randon forest models because it required in depth exploration on making the comparisons.  

Garima:  Heat map and comparing/correlating the 22 variables. Uncoding the binary code.  


Analysis: 

## Conclusions


## Futher Analysis

1. Explore income analysis

<img width="612" alt="image" src="https://user-images.githubusercontent.com/111452227/219551893-af196382-2163-48c5-b83b-474f7c0614ee.png">

2.
3.


## References



