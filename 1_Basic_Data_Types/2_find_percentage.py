if __name__ == '__main__':
    n = int(input())    
    #   dict for name: [scores] pairs
    #   [scores] is a list of 3 int values  
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input() # query means request, here enter a name and return the avg value
    
    # code below
    avg = 0
    if query_name in student_marks:
        scores_list = student_marks[query_name]     # get the student's 3 scores
        avg = sum(scores_list) / len(scores_list)   # use sum() and len() to find the avg, 
        #   here [score] == [2 3 4] len() == 3
        #   avg = (2+3+4) / 3 = 9 / 3 = 3         
        print("%.2f" % avg) # this one is asking for a float with 2 decimal places, so print("%.2f" % avg)
        
        #   or
        #   print("%.4f" % avg) # this one is asking for a float with 2 decimal places, so print("%.4f" % avg)
    
