from pandas import read_csv

#Load dataset 

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

dataset = read_csv(url, names=names)

#shape

print("Dataset shape: ")
print(dataset.shape)

#descriptions

print("Dataset Description")
print(dataset.describe())

#class distribution

print("Class Distribution")
print(dataset.groupby('class').size())
