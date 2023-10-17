from random import randint

def randomScores(Scores):
    for n in range(1,11):
        Scores[n] = randint(0,100)

def checkGrade(Scores,grades):
    GRADES = { 80:'A',70:'B',60:'C',50:'D',0:'F'}
    for n, score in Scores.items():
        for key, value in GRADES.items():
            if (score >= key):
                Grades[n] = value
                break

def reportGrade(Scores,Grades):
    print('='*23)
    print("| No. | Score | Grade |")
    print('='*23)
    for n in Scores:
        print(f'| %3d  | %3d |  %s  |'%(n,Scores[n],Grades[n]))
    print('='*23)

#main
Scores = {}
Grades = {}
randomScores(Scores)
checkGrade(Scores,Grades)
reportGrade(Scores,Grades)