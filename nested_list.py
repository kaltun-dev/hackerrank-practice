def sort_students(names_scores):
    # Step 1: Extract all scores from the nested list
    scores = []
    for student in names_scores:
        scores.append(student[1])
        
    # Step 2: Remove duplicates and sort scores in ascending order
    sorted_scores = sorted(set(scores))
    
    # Step 3: Get the second lowest score (index 1 in sorted list)
    second_lowest = sorted_scores[1]
    
    # Step 4: Find all students who have the second lowest score
    names_second_lowest = []
    for student in names_scores:
        if student[1] == second_lowest:
            names_second_lowest.append(student[0])
    
    # Step 5: Sort the names alphabetically
    names_second_lowest = sorted(names_second_lowest)
    
    # Step 6: Print each name on a new line
    for name in names_second_lowest:
        print(name)


if __name__ == '__main__':
    
    # Step 1: Initialize empty list to store [name, score]
    names_scores = []
    
    # Step 2: Read number of students and collect input
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        
        # Store each student as [name, score]
        names_scores.append([name, score])
    
    # Step 3: Process and display result
    sort_students(names_scores)