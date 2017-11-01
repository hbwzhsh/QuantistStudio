# _*_ coding:utf-8 _*_
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dataset = loadtxt("pima-indians-diabetes.data", delimiter=",")

X = dataset[:,0:8]
Y = dataset[:,8]

seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
#print(X_train, X_test, y_train, y_test)

model = XGBClassifier()
model.fit(X_train,X_test)

y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]

accuracy = accuracy_score(y_test,predictions)
print("Accuracy:%.2f%%"%(accuracy*100.0))


print("game over")