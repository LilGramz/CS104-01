numberOfTests = 0
score = 0
total = 0
average = 0.0
scorecount = 0

numberOfTests = int(input("please enter the number of tests you want to average: "))

#Make this stuff repeat untill scorecount = numberOfTests
while scorecount < numberOfTests:
    score = int(input("please enter a score: "))

    #Scorecount is 0 bu increases by 1 each time a number is imputed by user
    scorecount = scorecount + 1

    #total is zero but increases each time  anumber is imputed by the user
    total += score

    #when the number of scores= the initial number imputed the loop ends
    if scorecount == numberOftest:
        break
    
average = total/scorecount
print("the average is ",average)

