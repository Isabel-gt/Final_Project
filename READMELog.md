
# Logistic Regression Model

The logistic regression model was chosen as a supervised machine learning model to predict a binary outcome of positive diagnosis for diabetes(1) or negative diagnosis for diabetes(0).  

The data was split 75/25 into training and testing data. The model was instantiated, the training data was fit into the model and a prediction was run on the testing data.

The model returned an accuracy score of 85.9287%. A confusion matrix was lay out and a classification report was printed with recall score and f1 score. 

￼<Screenshot 2023-02-23 at 2.58.15 PM.png>

Once the model was ready. We use the joblib and pickle dump method to store the model and transfer it into a flask python file.
￼
<Screenshot 2023-02-23 at 3.03.04 PM.png>

Flask was used to connect the model to a sample testing form on the html webpage.

We use several tutorials and module notes as well as flask documentation page to build routes to the html home page, testing page, database and results page.

<Screenshot 2023-02-23 at 3.18.32 PM.png>

There were many errors and set backs to this process but they were overcame and we learned a lot about troubleshooting the coding process.

The bootstrap html template was extensively edited to match the project desired outcome and gave us an opportunity to practice and extend html and css knowledge.

## Troubleshooting technical difficulties

. Import errors
. Version mismatch errors
. Matrix shape errors
. Attribute errors
. Value errors

## Solving Technical errors

. Google console
. Postman 
. Stack Overflow 
. Stack exchange 
. Towards Data Science 
. Libraries documentations
. Support Services( Instructor, TAs, Tutors)

### Features reference:

BMI: 12 -98
Education: 1-6
Age: 1-13  [ (1-3),(4-6),(7-9),(10-12),(13+)]

## References

<https://www.geeksforgeeks.org/how-to-do-train-test-split-using-sklearn-in-python/?ref=gcse>

<https://pythonprogramming.net/practical-flask-introduction>

<https://towardsdatascience.com/end-to-end-data-science-example-predicting-diabetes-with-logistic-regression-db9bc88b4d16>

<https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html>

<https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#>

<https://datascience.stackexchange.com/questions/25673/attributeerror-numpy-ndarray-object-has-no-attribute-predict/25676>

<https://www.kaggle.com/questions-and-answers/192852>

<https://stats.stackexchange.com/questions/29781/when-conducting-multiple-regression-when-should-you-center-your-predictor-varia>

<https://stackoverflow.com/questions/31421413/how-to-compute-precision-recall-accuracy-and-f1-score-for-the-multiclass-case>

<https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support>

<https://www.kaggle.com/code/alexteboul/diabetes-health-indicators-dataset-notebook/notebook>

<https://www.ge.com/news/reports/software-please-doctors-looking-ai-speed-diagnosis>

<https://www.stockvault.net/free-photos/medical+ai?pg=&ci=&or=&dt=&li=>

<https://www.stockvault.net/free-photos/medical+ai/?p=2>
