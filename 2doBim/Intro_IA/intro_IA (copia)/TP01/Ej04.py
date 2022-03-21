import numpy as np

truth =      np.array([1,1,0,1,1,1,0,0,0,1]) == 1 
prediction = np.array([1,1,1,1,0,0,1,1,0,0]) == 1
notruth = np.logical_not(truth)
noprediction = np.logical_not(prediction)

TP = np.sum(truth & prediction)
TN = np.sum(notruth & noprediction)
FP = np.sum(notruth & prediction)
FN = np.sum(truth & noprediction)

Precision = TP / (TP + FP)
Recall = TP / (TP + FN)
Accuracy = (TP + TN) / (TP + TN + FP + FN)

print ('Las métricas son:\nPrecisión =', Precision,'\nRecall =', Recall,'\nAccuracy =', Accuracy)