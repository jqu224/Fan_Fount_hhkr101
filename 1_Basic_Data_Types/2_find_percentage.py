if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # code below
    avg = 0
    if query_name in student_marks:
        scores_list = student_marks[query_name]
        avg = sum(scores_list)/len(scores_list)
        print("%.2f" % avg)
