__author__ = 'Penghao Wang'
from numpy import *
from math import *
import csv
#load data in traindata
#load label in the trainlabel
traindata = loadtxt('training.csv',usecols=range(9),dtype=int)
trainlabel = loadtxt('training.csv',usecols=(range(9,10)),dtype=int)
d=traindata[0]

#print(d[0])
#print(trainlabel)


#calculate entropy
def calculateEntropy(label):
    entropy = 0
    size = label.size
    count = {}
    for currentLabel in label:
        if currentLabel not in count.keys():
            count[currentLabel] = 0
        count[currentLabel] += 1

    for key in count:
        pxi = float(count[key])/size
        entropy -= pxi*log(pxi,2)

    return entropy

x=calculateEntropy(trainlabel)
print(x)

m= [label for label in trainlabel]
featValues = [datasets[8] for datasets in traindata]
uniqueFeatValues = set(featValues)
mylist = list(uniqueFeatValues)
#print(len(featValues))
#print(featValues)
print(mylist[1])



#split the dataset 
def splitdata(data,splitfeature_index,splitvalue):
    index_less = []
    index_more = []

    #arg = mean(data[splitfeature_index],axis=0) # I use arg here because I will calculate imformation gain of less or greater than the average
    #print(arg)
    for index in range(len(data)):
        d = data[index]
        if d[splitfeature_index] < splitvalue:
            index_less.append(index)
        else:
            index_more.append(index)
    return index_less,index_more
idx_less,idx_greater = splitdata(traindata,0,5)
#print(idx_less)
#print(idx_greater)
#select the best data feature to split the datasets by using information gain

def chooseSplitNode(data,label):
    n_fea = len(data[0])

    n = len(label)
    #print(data)
    base_entropy = calculateEntropy(label)
    best_gain = 0
    for fea_i in range(n_fea): #calculate entropy under each splitting feature
        cur_entropy = 0
        featValues = [datasets[fea_i] for datasets in traindata]
        uniqueFeatValues = list(set(featValues))
        print(uniqueFeatValues)
        #print(uniqueFeatValues)
        for i in uniqueFeatValues:
            cur_entropy = 0
            idxset_less,idxset_greater = splitdata(data,fea_i,i)
            #print(idxset_less)
            prob_less = float(len(idxset_less))/n
            prob_greater = float(len(idxset_greater))/n

        #entropy(value|X) = \sum{p(xi)*entropy(value|X=xi)}
            cur_entropy += prob_less*calculateEntropy(label[idxset_less])
            cur_entropy += prob_greater * calculateEntropy(label[idxset_greater])

            info_gain = base_entropy - cur_entropy #notice gain is before minus after
            print (info_gain)
            if(info_gain>best_gain):
                best_gain = info_gain
                best_idx = fea_i
                splitFeatures = i
    print(best_gain)
    print(best_idx)
    print(splitFeatures)
    return best_idx,splitFeatures




chooseSplitNode(traindata,trainlabel)



#m= [label for label in trainlabel]
#featValues = [datasets[6] for datasets in traindata]
#uniqueFeatValues = set(featValues)
#print(len(featValues))
#print(featValues)

#print(uniqueFeatValues)



