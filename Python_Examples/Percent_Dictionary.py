/*
Sample Input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output

56.00
Explanation

Marks for Malika are {52,56,60}  whose average is 56
*/





if __name__ == '__main__':
    n = int(input())
    total = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks = (student_marks[query_name])
    for i in range(len(query_marks)):
        total += query_marks[i]
    print("%.2f" % (total/len(query_marks)))