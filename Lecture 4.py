#import a dataset

from sklearn import datasets
iris = datasets.load_iris()

x = iris.data
y = iris.target 

from sklearn.cross_validation import train_test_split

x_train ,x_test,y_train,y_test = train_test_split(x,y,test_size = .5 )

# # using DecisionTreeClassifier
# from sklearn import tree
# my_classifier = tree.DecisionTreeClassifier()

# using KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()



my_classifier = my_classifier.fit(x_train,y_train)


# way 1 to check the accuracy score 
print my_classifier.score(x_test,y_test)


# way 2 to check the accuracy score 
predictions = my_classifier.predict(x_test)
from sklearn.metrics import accuracy_score
print accuracy_score(y_test,predictions)

