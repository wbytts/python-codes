txtFile = open('rank.txt','r')
line = txtFile.readline()
oldTime = int(line)
txtFile.close()

newTime = 35
if newTime < oldTime:
    txtFile = open('rank.txt', 'w')
    txtFile.write(str(newTime))
    txtFile.close()