from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris=load_iris()
x=iris.data
y=iris.target


x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=25, test_size=0.2)
dtc=DecisionTreeClassifier()
dtc.fit(x_train,y_train)

print("Accuracy score is : ",dtc.score(x_test,y_test))