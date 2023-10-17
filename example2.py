def checkGrade(score):
    Grades = { 80:'A',70:'B',60:'C',50:'D',0:'F'}
    for n in Grades:
        if (score >= n):
            return (Grades[n])

done = True
while done:
    score = int(input('Enter your score (-1 to exit) : '))
    if(score != -1):
        grade = checkGrade(score)
        print(f'Your score = %d, got grade = %s'%(score,grade))
    else:
        done = False

print('End Program')