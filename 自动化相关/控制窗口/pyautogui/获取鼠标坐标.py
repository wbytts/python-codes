import pyautogui as pag

try:
    print("按Ctrl+C结束:")
    while True:
        x, y = pag.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except:
    pass
