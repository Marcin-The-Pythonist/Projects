# What data did I use to create this model? 
  I used a Kaggle dataset: https://www.kaggle.com/datasets/kmldas/hr-employee-data-descriptive-analytics/discussion/311494

# What does this model predict?
  Based on values tagged with the '+' sign in the *Data used for training* chapter, the model predicts whether an employee might quit. 

# Data used for training
  The dataset consists of 11 columns: <br>
  Emp_Id(Dropped, irrelevant)	<br>
  satisfaction_level - Ranges from 0 to 100. *+*<br>
  last_evaluation	- Employee performance(Dropped due to high p-value).<br>
  number_project - Number of projects completed(Dropped due to high correlation with time spent at the company).<br>
  average_montly_hours - Average working time per month. *+*<br>
  time_spend_company	- Time spent in the company. *+*<br>
  Work_accident	- Did the employee have an accident in the workplace? *+*<br>
  left - Did this employee quit? (endogenous variable) <br>
  promotion_last_5years	- Was the employee promoted in the last 5 years? *+*<br>
  Department - Dropped(irrelevant, although could be used if finding affiliation rate for each department was needed)<br>
  salary - low, medium, or high. (The model itself takes integers: 
                                1 for low
                                2 for medium
                                3 for high) *+*
# Model's Accuracy
  Accuracy:  70.0 %
  Specificity:  67.0 %
  Sensitivity:  80.0 %
