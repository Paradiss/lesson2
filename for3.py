list_of_scores = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [10, 2, 1, 5, 5, 5, 7]},
    {'school_class': '7g', 'scores': [10, 5, 6, 7]},
    {'school_class': '10', 'scores': [10, 9, 5, 7, 8]}
]
school_mean = 0
class_score = 0
for i in range(len(list_of_scores)):
    for score in list_of_scores[i]['scores']:
        class_score += score  
    school_lass = list_of_scores[i]['school_class']      
    class_mean = class_score/len(list_of_scores[i]['scores'])
    print(f'Средний балл по классу {school_lass} = {class_mean}')
    school_mean += class_mean 
    class_score = 0    
print(f'Средний балл по школе = {school_mean/len(list_of_scores)}')        
