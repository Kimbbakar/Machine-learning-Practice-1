from scipy.spatial import distance
import random

#This lecture is about writing classifier by own 

def euc(a,b):
	return distance.euclidean(a,b)

class ScrappyKNN():
	def fit(self,x_train,y_train):
		self.x_train = x_train
		self.y_train = y_train

	def random_predict(self,x_test):
		predictios = [] 
		for row in x_test:
			label = random.choice(self.y_train)
			predictios.append(label)
		return predictios

	def predict(self,x_test):
		predictios = [] 
		for row in x_test:
			label = self.close(row)
			predictios.append(label)
		return predictios

	def close(self, row ):

		dis = 123456789
		idx = 0

		for i in range(0,len(self.x_train ) ):

			if euc(x_train[i],row )<dis :
				dis=euc(x_train[i],row )
				idx = i

		return self.y_train[idx]


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

