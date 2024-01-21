if __name__ == '__main__':
    name_score = []
    count = int(input("Enter count: "))
    
    for _ in range(count):
        name = input("Enter name: ")
        score = float(input("Enter score: "))
        name_score.append([name, score])
    
    
    unique_scores = set(score for _, score in name_score)
    
    if len(unique_scores) < 2:
        print("There is no second maximum score.")
    else:
        
        max_score = max(unique_scores)
        
        
        second_max_score = max(score for _, score in name_score if score != max_score)
        
      
        names_second_max_score = sorted([name for name, score in name_score if score == second_max_score])
        
        print(f"Max Score: {max_score}")
        print(f"Second Max Score: {second_max_score}")
        print(f"Names with Second Max Score (Alphabetically): {', '.join(names_second_max_score)}")
