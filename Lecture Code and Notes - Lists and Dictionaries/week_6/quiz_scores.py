quiz_scores = [8, 4, 10, 9, 7]
#quiz_scores[1] = 10
#print(quiz_scores)

quiz = int(input('Which quiz did you retake?'))
index = quiz-1
score = int(input('What was your score on quiz 2?'))

quiz_scores[index] = score

print(quiz_scores)
