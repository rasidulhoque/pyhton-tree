import sklearn
from sklearn import tree

features=[[2,100],[6,25],[1,300],[1,1000],[4,1000]]
label={1,2,1,1,2,2}
clf=clf.flt(features,label)
printf(clf.predict([[1,140]]))