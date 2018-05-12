from sklearn import tree
from os import system

clf = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]

X = [[181, 80, 11], [177, 70, 10], [160, 60, 7], [154, 54, 6], [166, 65, 9],[190, 90, 12], [175, 64, 8],[177, 70, 9], [159, 55, 8], [171, 75, 9], [181, 85, 10]]


Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female','female', 'male', 'male']



clf = clf.fit(X, Y)
system('clear')
i=int(input("Enter Height : "))
j=int(input("Enter Weight : "))
k=int(input("Enter shoe_size: "))


prediction = clf.predict([[i, j, k]])

print(prediction)

