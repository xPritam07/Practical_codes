from urllib.request import urlopen

import pandas as pd
import io
df=pd.read_csv(io.StringIO((urlopen('https://raw.githubusercontent.com/xPritam07/Practical_codes/refs/heads/master/iris.csv').read().decode('utf-8'))))
print(df.head())

from sklearn.preprocessing import LabelEncoder, StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
le=LabelEncoder()
df['species']=le.fit_transform(df['species'])
print(df.head())

corr_mat=df.corr()

sns.heatmap(corr_mat,annot=True,fmt='g')
plt.show()

import numpy as np
x=np.array([[1,2,3],[3,4,5],[6,7,9]])
sc=StandardScaler()

scaled_x=sc.fit_transform(x)

cov_mat=np.cov(scaled_x)
print(cov_mat)

eigval,eigvec=np.linalg.eig(x)
print(eigval)
print(eigvec)