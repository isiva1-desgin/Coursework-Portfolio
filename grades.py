
examGrades = [ 83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80]
dayboth = [ 'Trent', 'Jake', 'Mahmoud', 'Alex', 'Sam', 'Percy']
dayOnce =  ['Caleb', 'Jessica', 'Zayne', 'Mary']

numStudents = len(examGrades)
highestG = max(examGrades)
lowestG = min(examGrades)

classAverage = (sum(examGrades))/ len(examGrades)
numAttend = len(dayboth) + len(dayOnce)

print(f"{numStudents} Students took the exam.")
print(f"The highest grade was a {highestG}")
print(f"The lowest grade was a {lowestG}")
print(f"The average grade for the exam was a {classAverage:.1f}")
print()

print(f"{numAttend} students attended the class.")
print(f"{dayboth} attended both class days.")
print(f"{dayOnce} attended one class day.")