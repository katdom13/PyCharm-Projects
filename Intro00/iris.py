import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

print("Iris Sample")

iris = load_iris()
testIndices = [0,50,100]

#get training data

train_features = np.delete(iris.data, testIndices, axis=0)
train_labels = np.delete(iris.target, testIndices)

#get test data

test_features = iris.data[testIndices]
test_labels = iris.target[testIndices]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_features, train_labels)

print(test_labels)
print(clf.predict(test_features))

