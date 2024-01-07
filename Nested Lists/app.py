students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41]]

scores = [student[1] for student in students]
max_score = max(scores)

scores = [score for score in scores if score != max_score]
second_max_score = max(scores)

students_with_second_highest = [student[0] for student in students if student[1] == second_max_score]
students_with_second_highest.sort()

print("Second highest score:", second_max_score)
print("Student(s) with the second highest score:")
for student in students_with_second_highest:
    print(student)



    
  
    

    
    



    
   
    






# for name,score in students.items():
    