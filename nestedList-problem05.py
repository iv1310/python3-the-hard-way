"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry



"""

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    # Take the lowest grades and drop it from the list
    lowest = min(score for _, score in students)
    grades = [[name, score] for name, score in students if score > lowest]

    # Take the second lowest grade from the filtered list and store it to another list.
    lowest = min(score for _, score in grades)
    names = [[name, score] for name, score in grades if lowest == score]

    # Then sort it
    names.sort()
    for name, _ in names:
        print(name)
