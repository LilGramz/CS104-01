numberOfTests = 0
score = 0
total = 0
average = 0.0
scorecount = 0

numberOfTests = int(input("please enter the number of tests you want to average: "))

#Make this stuff repeat untill scorecount = numberOfTests
score = int(input("please enter a score: "))
scorecount = scorecount + 1
total = total + score

average = total/scorecount
print("the average is ",average)

