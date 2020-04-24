import matplotlib
import pandas as pd
import numpy as np
import pandas.util.testing as tm
import seaborn as sns
from jedi.refactoring import inline



""" 1. Define Project class (variables ,constructor and function ) code here in the below space as per the requirement"""
class Project:
    def __init__(self, projectId, projectName, manHours, technologyList):
        self.projectId = projectId
        self.projectName = projectName
        self.manHours = manHours
        self.technologyList = technologyList
        avgProjCost = 0
    def calculateProjCost(self, ratePH):
        projectCost = self.manHours*ratePH
        return projectCost

""" 2. Define Organization class( Variables,Constructor and function) code here in the below space as per requirement """

class Organization:
    def __init__(self, orgName, ProjList):
        self.orgName = orgName
        self.ProjList = ProjList

    def projAvgCostByTechnology(self, projId, rate):
        for value in self.ProjList:
            if value.projectId == projId:
                value.avgProjCost = (value.calculateProjCost(rate)
                /len(value.technologyList))
                return value
        else:
            return None



advertising = pd.read_csv('tvmarketing.csv')
# %matplotlib inline
# sns.pairplot(advertising, x_vars=['TV'], y_vars='Sales', height=7, aspect=0.7, kind='scatter')
X = advertising['TV']
X.head()
y = advertising['Sales']

y.head()
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, random_state= 100)
print(type(X_train))
print(type(X_test))
print(type(y_train))
print(type(y_test))

train_test_split

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

X_train = X_train[:, np.newaxis]
X_test = X_test[:, np.newaxis]

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)