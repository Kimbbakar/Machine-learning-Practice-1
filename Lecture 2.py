from sklearn.datasets import load_iris

import pandas as pd
import numpy as np

iris = load_iris()

print iris.feature_names
print iris.target_names

print iris.data[0] 

test_idx = [0,50,100] 

# Training data 

train_target = np.delete(iris.target,test_idx )
train_data = np.delete(iris.data,test_idx,axis = 0 )


# test data 
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]
 