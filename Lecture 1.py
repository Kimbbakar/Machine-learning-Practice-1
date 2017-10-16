from sklearn import tree
import numpy as np

# label 0 = apple
# label 1 = orange 

features = np.array([ [140,1],[130,1],[150,0],[170,0] ] )
labels = np.array([0,0,1,1])


#decision tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

print clf.feature_importances_

print clf.predict( [ [150,0] ] )