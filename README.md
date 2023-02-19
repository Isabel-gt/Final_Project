![image](https://user-images.githubusercontent.com/111452227/217908785-8b81c481-f065-4008-8b1f-779e353147df.jpeg)









# Using Health Indicators to Predict Diabetes

Technologies:  Python 3.9.12 | Javascript | HTML | Form & Postman | Flask | Tableau

## Table of contents

Introduction

Method

Exploratory Analysis

Results/Model

Set Backs

Limitations

Conclusion

Future Considerations

References

## Introduction

According to the CDC, the number of people who have diabetes in America is the highest it has ever been. People with diabetes have a deficiency in how their body makes or uses insulin.  Insulin is a important hormone that regulates glucose.  Without proper insulin regulation, patients can succomb to serious complications such as heart disease, vision loss, lower-limb amputation and kidney disease.  It is essential that healthcare providers have the tools to screen patients for prediabetes or diabetes.  The predictions can assist clinicians formulate a   In this project, we intend to use supervised machine learning (classification)to predict diabetes, prediabetes or no diabetes. 

## Method

We used the Diabetes Health Indicators Dataset from 2015 provided by Kaggle. The dataset was obtained by surveying hundreds of thousands of Americans for diabetes or prediabetes predictors with The Behavioral Risk Factor Surveillance System (BRFSS).  We decided to explore 10 of the 22 variables for our prediction; education, age, high BP, gender, BMI, cholesterol check, no doctor because of cost, stroke, smoker, physical activity.

Some of the questions that we explored were age, health history, physical activity and socioeconomic factors.  The data that we chose did not require extensive clean-up such as dropping NaN or columns therefore we were able to proceed in creating the model.  

Before we were able to work with the dataset, we had to label the categories in some of the columns.  If you look at the education categories, those were translated from 1-6 to school levels of education; elementary, middle school, high school, and college education.  

It was felt that a supervised machine learning was the best approach to classify and predict diabetes.  We used the tensorflow deep learning module. To compare for accuracy, we used the random forest method for this prediction.  We then began to build the webpage using HTML, Javascript, and Flask. To be continued...

The diabetes prediction project using TensorFlow deep learning module and logistic regression is an approach to predict the onset of diabetes in patients. The project uses a dataset of demographic and health-related features, such as age, BMI, blood pressure, and physical activity etc, to train a machine learning model.

The first step in the project is to preprocess the dataset by normalizing the features, splitting the data into training and test sets, and converting the labels to binary values. Then, the logistic regression model is built using TensorFlow's high-level API, Keras. The model consists of an input layer, a dense layer with sigmoid activation function, and an output layer.
The next step is to train the model using the training dataset and evaluate its performance on the test dataset. The performance metrics used to evaluate the model include accuracy, precision, recall, and F1 score. Once the model is trained and evaluated, it can be used to predict the onset of diabetes in new patients.

The project also utilizes a deep learning approach using TensorFlow's deep neural network (DNN) module. The DNN model consists of multiple layers of interconnected neurons that use nonlinear activation functions to learn complex relationships between the features and labels.
The DNN model is trained using the same preprocessed dataset and evaluated using the same performance metrics. The project compares the performance of the logistic regression and DNN models and shows that the DNN model outperforms the logistic regression model in terms of accuracy and F1 score.
In conclusion, the diabetes prediction project using TensorFlow deep learning module and logistic regression is an effective approach to predict the onset of diabetes in patients using demographic and health-related features. The project demonstrates the advantages of using a deep learning approach over traditional logistic regression, highlighting the importance of choosing the right machine learning model for a given task

...Demonstrate and expand further the logistic model prediction since we had a higher accuracy... and then use tensorflow and random forest as additional analysis.   

## Results 

Accuracy = 86%
Outcomes:  0= No diabetes, 1= diabetes or prediabetes

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

Add: Stack overflow, scikitlearn and numpy documentation pages as sources





