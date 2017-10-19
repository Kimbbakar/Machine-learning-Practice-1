import random

#This lecture is about writing classifier by own 


class ScrappyKNN():
	def fit(self,x_train,y_train):
		self.x_train = x_train
		self.y_train = y_train

	def predict(self,x_test):
		predictios = []
		print "**hi"
		for row in x_test:
			label = random.choice(self.y_train)
			predictios.append(label)
		return predictios


#import a dataset

from sklearn import datasets
iris = datasets.load_iris()

x = iris.data
y = iris.target 

from sklearn.cross_validation import train_test_split

x_train ,x_test,y_train,y_test = train_test_split(x,y,test_size = .5 )
 
# using KNeighborsClassifier
my_classifier = ScrappyKNN()


my_classifier.fit(x_train,y_train)

 

predictions = my_classifier.predict(x_test)

# Checking the accuracy 

from sklearn.metrics import accuracy_score
print accuracy_score(y_test,predictions)

