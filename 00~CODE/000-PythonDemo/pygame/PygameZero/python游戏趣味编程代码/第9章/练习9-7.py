def BMI(height, weight):
    bmi = weight/height/height
    result = ''
    if bmi < 18.5:
        result = '体重过轻'
    elif bmi < 24:
        result = '体重正常'
    elif bmi < 27:
        result = '过重'
    elif bmi < 30:
        result = '轻度肥胖'
    elif bmi < 35:
        result = '中度肥胖'
    else:
        result = '重度肥胖'
    return result

h = float(input('输入身高（米）：'))
w = float(input('输入体重（公斤）：'))
print(BMI(h, w))