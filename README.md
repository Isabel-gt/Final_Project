![image](https://user-images.githubusercontent.com/111452227/217908785-8b81c481-f065-4008-8b1f-779e353147df.jpeg)









# Using Health Indicators to Predict Diabetes

Technologies:  Python 3.9.12 | Javascript | HTML | Form & Postman | Flask | Tableau | Matplotlib | hvplot | SQLite3 | Google Collab

## Table of contents

Introduction

Method & Model

Exploratory Analysis

Future Analysis

Set Backs

Limitations

Conclusion

Next Steps

References

## Introduction

According to the CDC, the number of people who have diabetes in America is the highest it has ever been. People with diabetes have a deficiency in how their body makes or uses insulin.  Insulin is a important hormone that regulates glucose.  Without proper insulin regulation, patients can succomb to serious complications such as heart disease, vision loss, lower-limb amputation and kidney disease.  It is essential that healthcare providers have the tools to screen patients for prediabetes or diabetes.  The predictions can assist clinicians formulate a   In this project, we intend to use supervised machine learning (classification)to predict diabetes, prediabetes or no diabetes. 

## Method

We used the Diabetes Health Indicators Dataset from 2015 provided by Kaggle. The dataset was obtained by surveying hundreds of thousands of Americans for diabetes or prediabetes predictors with The Behavioral Risk Factor Surveillance System (BRFSS).  We decided to explore 10 of the 22 variables for our prediction; education, age, high BP, gender, BMI, cholesterol check, no doctor because of cost, stroke, smoker, physical activity.

Some of the questions that we explored were age, health history, physical activity and socioeconomic factors.  The data that we chose did not require extensive clean-up such as dropping NaN or columns therefore we were able to proceed in creating the model.  

Before we were able to work with the dataset, we had to label the categories in some of the columns.  If you look at the education categories, those were translated from 1-6 to school levels of education; elementary, middle school, high school, and college education.  

It was felt that a supervised machine learning was the best approach to classify and predict diabetes.  We used the tensorflow deep learning module. To compare for accuracy, we used the random forest method for this prediction.  We then began to build the webpage using HTML, Javascript, and Flask. 

We chose a template from Start Bootstrap and worked on editing and customizing it. We built 2 databases using sqlite, one with all the data and one with only 10 features. We used python in vs code and jupyter notebook to build, and train the models and for vizualization charts as well. Finally, we built flask routes to the html, the database and the machine learning model in order to facilitate testing and demostration.

 ### Database

During the completion of the Diabetes Prediction project, a goal was to create a database based on a dataset from the website Kaggle. This dataset was   downloaded as a CSV file called diabetes.csv. The database was created using Python in two different files. In the first file, an empty table named diabetesTable3 was made using sqlite3. This table contained the features and the target column names. In the second Python file, the data from the diabetes.csv file was loaded into the table, which results in the complete database; this is then stored under the name diabetes3.db. 

<img width="695" alt="3 (1)" src="https://user-images.githubusercontent.com/111452227/220824728-c38a8ae0-aa86-416b-95b0-2db52956fdb1.png">


### HTML and Flask

Another objective was to build an app route using Flask to access the database. Before creating this route, another team member made a file named index.html that included all the front-end web development. This file has many elements that allow users to see all the general information about the project as well as the visualizations. This HTML file shows text boxes where can fill in their information to determine whether they may or may not have diabetes.

To access the database, a button was included in the index.html file. This button leads to another HTML file called database.html. This file contains a heading called “Database”, as well as another button that takes the user back to the home page. The connection between the database.html and the diabetes3.db database was done in a Python file. In this file Flask was imported, then an app route and a function were made. A few methods were used inside this function such as connect, cursor, execute, and fetch all. Finally, the database was rendered in the database.html using the method render template. 

Finally, one more goal that needed to be reached was to create a third HTML file that would display the results of the diabetes prediction. The HTML file was called test. This ended up being a limitation since this objective was not reached due to the difficulty of connecting the route from the Flask app to the third HTML.

<img width="960" alt="image" src="https://user-images.githubusercontent.com/111452227/220792388-df812ddf-a648-420b-8750-5decc54f9da5.png">


### Machine Learning

The diabetes prediction project using TensorFlow deep learning module and logistic regression is an approach to predict the onset of diabetes in patients. The project uses a dataset of demographic and health-related features, such as age, BMI, blood pressure, and physical activity etc, to train a machine learning model.

The first step in the project is to preprocess the dataset by normalizing the features, splitting the data into training and test sets, and converting the labels to binary values. Then, the logistic regression model is built using TensorFlow's high-level API, Keras. The model consists of an input layer, a dense layer with sigmoid activation function, and an output layer.
The next step is to train the model using the training dataset and evaluate its performance on the test dataset. The performance metrics used to evaluate the model include accuracy, precision, recall, and F1 score. Once the model is trained and evaluated, it can be used to predict the onset of diabetes in new patients.

The project also utilizes a deep learning approach using TensorFlow's deep neural network (DNN) module. The DNN model consists of multiple layers of interconnected neurons that use nonlinear activation functions to learn complex relationships between the features and labels.
The DNN model is trained using the same preprocessed dataset and evaluated using the same performance metrics. The project compares the performance of the logistic regression and DNN models and shows that the DNN model outperforms the logistic regression model in terms of accuracy and F1 score.
In conclusion, the diabetes prediction project using TensorFlow deep learning module and logistic regression is an effective approach to predict the onset of diabetes in patients using demographic and health-related features. The project demonstrates the advantages of using a deep learning approach over traditional logistic regression, highlighting the importance of choosing the right machine learning model for a given task

<img width="616" alt="image" src="https://user-images.githubusercontent.com/111452227/220824949-1aaf01e1-d1ef-4488-a829-10d19e7ad19e.png">

In conclusion, the diabetes prediction project using TensorFlow deep learning module and logistic regression is an effective approach to predict the onset of diabetes in patients using demographic and health-related features. The project demonstrates the advantages of using a deep learning approach over traditional logistic regression, highlighting the importance of choosing the right machine learning model for a given task
  
## Analysis

Accuracy = 86%
Outcomes:  0= No diabetes, 1= diabetes or prediabetes

<img width="538" alt="image" src="https://user-images.githubusercontent.com/111452227/220826340-aed57cd0-69ea-4184-b0d0-38f861b76736.png">

![image](https://user-images.githubusercontent.com/111452227/220792974-342680a3-3b14-4f56-99a6-d6bd79b6fd19.png)

Heat Map (22 variables)

<img width="597" alt="image" src="https://user-images.githubusercontent.com/111452227/220826003-2872b747-21c0-448c-8aea-148670cff81e.png">

Heat Map (10 variables)

![image](https://user-images.githubusercontent.com/111452227/220793032-5b9c1e38-3add-44fc-95d4-3e1473e868aa.png)

High Blood Pressure, Cholesterol Check, Stroke

<img width="927" alt="HBP_CC_Stroke" src="https://user-images.githubusercontent.com/111452227/220823826-871b2bab-778c-4ad4-a3ad-86f32aa09e28.png">

Gender

<img width="506" alt="image" src="https://user-images.githubusercontent.com/111452227/220825778-820894fe-118a-4f47-bcc9-1cde9796dc97.png">

No Doctor Visit Due to Cost

<img width="369" alt="image" src="https://user-images.githubusercontent.com/111452227/220825633-85a26753-2128-46a4-92f7-7d405bc84f69.png">

Physical Activity vs BMI

<img width="808" alt="github_doctor" src="https://user-images.githubusercontent.com/111452227/220824397-216d7531-7794-47eb-9355-322d3b247278.png">



Age

<img width="749" alt="image" src="https://user-images.githubusercontent.com/111452227/220825690-8b5fc36e-9140-40fd-b53a-4b10537583f0.png">

Education

<img width="792" alt="image" src="https://user-images.githubusercontent.com/111452227/220825732-ae7fae37-239f-4cf1-b32a-61150d4a5e31.png">

## Future Analysis

1. Explore income analysis

<img width="881" alt="github_income" src="https://user-images.githubusercontent.com/111452227/220823544-3d29c5c6-231e-4792-b4c8-9d61fba2fdf3.png">

Heart Disease or Heart Attack

<img width="905" alt="github_hd" src="https://user-images.githubusercontent.com/111452227/220823387-46bfce48-923a-42b3-8c9e-27f7acd0b6c4.png">

Difficulty Walking

![image](https://user-images.githubusercontent.com/111452227/220824169-34114e7c-0e3d-456c-957f-b6c109154d96.png)


## Set backs

Connecting Flask with the database

Limited knowledge of the functions to make machine model connections with HTML and random forest

Deciding which of the 22 variables had the most significance. 


## Limitations

Time constraint did not allow to explore the deep learning method and random forest models because it required in depth exploration on making the comparisons.

Heat map and comparing/correlating the 22 variables. 

Uncoding the binary code.

Working with several binary variables limited chart functions, i.e., 1 or 0.

Imbalanced sample.  Diabetes sample was a lot less than the No Diabetes sample.


## Conclusion

Our group utilized a variety of technologies to create a diabetes prediction tool for a healthcare setting or individual use. 
We found that some health indicators have a greater influence in determining whether someone is at risk for diabetes.  
Developer and teamwork skills were demonstrated while creating a database and an HTML using Flask.
We used a deep learning method involving TensorFlow and logistic regression to validate the data and both showed an accuracy score of 86%.  
Data analysis was performed to understand the underlying indicators that lead to developing pre-diabetes or diabetes. 
Setbacks creating the models, HTML pages, and analysis were addressed through trial and error and with the guidance of teacher assistants.

## Next Steps

To explore other health indicators such as difficulty walking, nutritional intake such fruits and vegetables. 

Additional analysis on heart disease, income, and alcohol consumption.  

Future use of our deep learning and logistic classification models to triage centers in emergency rooms. 

## References

 GitHub | Stack Overflow |Scikitlearn |Numpy & python documentation | Pubmed | CDC







