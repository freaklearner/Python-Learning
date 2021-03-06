import sys; sys.path.append(r"/usr/lib/python2.7/dist-packages");
import pandas;
from pandas.tools.plotting import scatter_matrix;
import matplotlib.pyplot as plt;
from sklearn.metrics import classification_report;
from sklearn.metrics import confusion_matrix;
from sklearn.metrics import accuracy_score;
from sklearn.linear_model import LogisticRegression;
from sklearn.tree import DecisionTreeClassifier;
from sklearn.neighbors import KNeighborsClassifier;
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis;
from sklearn.naive_bayes import GaussianNB;
from sklearn.svm import SVC;
import os.path
import csv


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data";
cols = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'];
dataset = pandas.read_csv(url, names=cols);

if not os.path.isfile('files/repoData.txt'):
    f1 = open(r'files/repoData.txt','w+')
    for roc in dataset.to_records():
        st = str(roc[1])+","+str(roc[2])+","+str(roc[3])+","+str(roc[4])+","+str(roc[5])+"\n"
        f1.write(st)
    f1.close()


