txtFile = open('scores.txt', 'r')
totalScore = 0
for i in range(10):
    line = txtFile.readline()
    score = int(line)
    totalScore += score
averageScore = totalScore/10
txtFile.close()
print('平均成绩为：', averageScore)

txtFile = open('averageScore.txt', 'w')
txtFile.write(str(averageScore))
txtFile.close()