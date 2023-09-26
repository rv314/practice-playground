'''
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''

def result(query):
    average = float(sum(student_marks.get(query)) / len(student_marks.get(query)))
    average = "{:.2f}".format(average)
    return average

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = str(input())
    
    results = result(query_name)
    print(results)