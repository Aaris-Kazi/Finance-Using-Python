from sklearn import svm
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
# clf = svm.SVC(decision_function_shape='ovo')
clf = svm.SVC()
clf.fit(X, Y)
print(clf.predict([[10]]))

dec = clf.decision_function([[1]])
dec.shape[1] # 4 classes: 4*3/2 = 6

clf.decision_function_shape = "ovr"
dec = clf.decision_function([[1]])
dec.shape[1] # 4 classes