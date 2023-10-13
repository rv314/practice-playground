
'''
Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.

'''
overall_scores = list()
scores = list()
low_names = list()
second_min = None
            
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #score = "{:.2f}".format(score)
        
        ind_score = []
        ind_score.append(name)
        ind_score.append(score)
        scores.append(score)
        overall_scores.append(ind_score)
        
    second_min = sorted(set(scores))[1]
            
    for i in range(len(overall_scores)):
        if overall_scores[i][1] == second_min:
            low_names.append(overall_scores[i][0])
    
    low_names = sorted(low_names)

    for names in low_names:
        print(names)


# # In[259]:


# # seperate code for printing out names of low scorers
# for i in range(len(overall_scores) - 1):
#     if overall_scores[i][1] <= overall_scores[i + 1][1]:
#         low_names.append(overall_scores[i][0])

# low_names = sorted(low_names)
# for names in low_names:
#     print(names)

# scores = list
# for k, v in temp_dict.items():
#     overall_1.append([k])
#     scores.append(v)
    

# for i in range(len(overall_1)):
#     overall_1[i].append(temp_dict.get(overall_1[i][0]))

# for k, v in temp_dict.items():
#     ind_score.append(k)
#     ind_score.append(v) 
#     overall_1.append([ind_score])
#     #ind_score.clear()
#         #i += 1
#         low_scores = list()
# for i in range(len(overall_scores) - 1):
#     if overall_scores[i][1] <= overall_scores[i + 1][1]:
#         low_scores.append(overall_scores[i][1])
# print(low_scores)