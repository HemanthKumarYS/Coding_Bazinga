'''
Created on 10-Oct-2017

@author: Young Star Hemanth
'''

'''
Sorting the list in ascending order
'''
list_num = [2,1,2,3,1,3, 682,2,9198,19,88,19,1,61,1,8,18,18,35,168,1,81,6,68,168,1,681,81,81,86]

#===============================================================================
# for i in range(len(list_num)):
#     for j in range(len(list_num)-1):
#         if list_num[j] > list_num[j+1]:
#             list_num[j], list_num[j+1] = list_num[j+1], list_num[j]
#             
# print (list_num)
#===============================================================================

'''
Sorting the list in descending order
'''

for i in range(len(list_num)):
    for j in range(len(list_num)-1):
        if list_num[j] < list_num[j+1]:
            list_num[j], list_num[j+1] = list_num[j+1], list_num[j]
            
print (list_num)