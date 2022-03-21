import numpy as np

T=1
F=0

q_id           = np.array([1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4])
predicted_rank = np.array([0,1,2,3,0,1,2,0,1,2,3,4,0,1,2,3])
truth_relevance= np.array([T,F,T,F,T,T,T,F,F,F,F,F,T,F,F,T]) == 1


q_id_num, q_id_cant= np.unique(q_id, return_counts = True)
qp = np.zeros(len(q_id_num))

for i, num, cant in zip(np.arange(len(q_id_num)), q_id_num, q_id_cant):
  qp [i]= (np.sum((q_id == num) & (truth_relevance)))/cant
  print ('La query id',num,'tiene una precisión', qp[i])

print ('La precisión promedio es', np.mean(qp))