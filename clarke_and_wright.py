import numpy as np
from operator import itemgetter

distance_matrix=np.array([[0,28,31,20,25,34],[0,0,21,29,26,20],[0,0,0,38,20,32],[0,0,0,0,30,27],[0,0,0,0,0,25],[0,0,0,0,0,0]])
#calculate savings

list_i_j_saving=[]
i=1
while i<len(distance_matrix)-1:
    j=i+1
    while j<len(distance_matrix):
        saving=distance_matrix[0][i]+distance_matrix[0][j]-distance_matrix[i][j]
        list_i_j_saving.append([i+1,j+1,saving])
        j+=1
    i+=1   
list_i_j_saving=sorted(list_i_j_saving, key=itemgetter(2), reverse=True)
print(list_i_j_saving)

routing=[1,list_i_j_saving[0][0],list_i_j_saving[0][1],1]
print(routing)
index=1
while True:
    if len(routing)==len(distance_matrix)+1:
        break
    if index==len(list_i_j_saving):
        break
    if list_i_j_saving[index][0]==routing[1] and (list_i_j_saving[index][1] not in routing):
        routing.insert(1,list_i_j_saving[index][1])
        index +=1
        print(f'here 1 {index}')
        continue
    if list_i_j_saving[index][0]==routing[-2] and (list_i_j_saving[index][1] not in routing):
        routing.insert(-1,list_i_j_saving[index][1])
        index +=1
        print(f'here 2 {index}')
        continue
    if list_i_j_saving[index][1]==routing[1] and (list_i_j_saving[index][0] not in routing):
        routing.insert(1,list_i_j_saving[index][0])
        index +=1
        print(f'here 3 {index}')
        continue
    if list_i_j_saving[index][1]==routing[-2] and (list_i_j_saving[index][0] not in routing):
        routing.insert(-1,list_i_j_saving[index][0])
        index +=1
        print(f'here 4 {index}')
        continue
    index+=1
    
print(routing)
 