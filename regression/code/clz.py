import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
class Clazif:
    
    def __init__(self):
        pass
    
    def train(self, data):
        self.data = data
        
        dataset = pd.read_csv(self.data)
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, -1].values
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
        
        
        self.sc = StandardScaler()
        X_train = self.sc.fit_transform(X_train)
        X_test = self.sc.transform(X_test)
        
        # Training the Logistic Regression model on the Training set
        self.classifier = LogisticRegression(random_state = 0)
        self.classifier.fit(X_train, y_train)
        
        # Predicting the Test set results
        y_pred = self.classifier.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        return (acc)