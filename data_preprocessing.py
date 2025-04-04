import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from io import StringIO
# Load the dataset
df = pd.read_csv(StringIO(urlopen('https://raw.githubusercontent.com/xPritam07/Practical_codes/refs/heads/master/wine.csv').read().decode('utf-8')))
print(df.head())


x=df.iloc[:, :-1].values
y=df.iloc[:, -1].values
print(x)
print(y)

df['Wine'].fillna(df['Wine'].mean())

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# Create the ColumnTransformer
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])],remainder='passthrough')
x=np.array(ct.fit_transform(x))
print(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train)
print(x_test)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
print(x_train)
print(x_test)