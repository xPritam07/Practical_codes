import numpy as np
import seaborn as sns
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)


pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(random_state=42))
])

param_grid = {
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [3, 5, None]
}

grid_search = GridSearchCV(estimator=pipe, cv=5, param_grid=param_grid, scoring='accuracy' )
grid_search.fit(x_train,y_train)

y_pred = grid_search.predict(x_test)

print(classification_report(y_test, y_pred))