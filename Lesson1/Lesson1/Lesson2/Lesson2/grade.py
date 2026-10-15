prelim = float(input("Prelim grade: "))
midterm = float(input("Midterm grade: "))
final = float(input("Final grade: "))

average = (prelim + midterm + final) / 3
print("Average:", round(average, 2))

if average >= 75:
    print("Status: Passed")
else:
    print("Status: Failed")
