from datetime import datetime, timezone, timedelta
import wave
import pyaudio
import pygame
from mutagen.mp3 import MP3
import os
import datetime
import pymssql
from aip import AipSpeech#这是百度的aip包,
import pygame
from mutagen.mp3 import MP3
import os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen,QStandardItemModel, QStandardItem,  QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5 import QtCore, QtWidgets
import base64
import hashlib
import time
import requests
import json
import sys
#对后台窗口截图
import win32gui, win32ui, win32con
from ctypes import windll
import cv2
import numpy
global start_voice,stop_voice
global flag_last_music_name
global flag_wake_up
global flag_last_music_name
flag_last_music_name=0
global flag_music_playing,flag_play_command
flag_music_playing=0#初始状态未占用
flag_play_command=0#表示允许播放
flag_wake_up=True
flag_last_music_name=0
start_voice=True
stop_voice=False
print('软件启动中....')
#这个数据库和手写识别没有关系，仅仅就是保存日常的记录数据，毕竟这是我的笔记本，可以语音手写录入的那种
server = 'SC-201903271457'
user = 'sa'
password = 'sqlserver_li'
database = 'aibinghaus'
conn = pymssql.connect(server, user, password, database)
cur1 = conn.cursor()
#用于播放音乐的函数，放入音乐路径就成
def pc_play_music(n):
    print("开始播放音乐")
    audio = MP3(n)
    pygame.mixer.init()
    path = n
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    for i in range(0,int(audio.info.length)+1 ):
        global flag_play_command
        if i==int(audio.info.length)or flag_play_command == 1:  # 表示有应用请求音频或者已经播放完
            pygame.mixer.music.stop()
            pygame.quit()
            flag_play_command=0
            break
        else:
            time.sleep(1)
    print("播放完成")
#用于停止音乐的函数，只要放置标志位就行了，会让播放的音乐停止播放
def stop_voice_info():
    global flag_play_command
    flag_play_command=1
#用于将文字转化成语音的函数，链接的是百度api,可以研究一下
def play_sentence(myword):
    global flag_last_music_name
    flag_last_music_name = flag_last_music_name+1
    if myword:
        lan = myword#百度的账户，语音生成的，文字转语音
        APP_ID = ''  # 引号之间填写之前在ai平台上获得的参数
        API_KEY = ''  # 如上
        SECRET_KEY = ' '  # 如上
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        result = client.synthesis(lan, 'zh', 1, {'vol': 10, 'per': 4, 'spd': 3, 'pit': 2})
        '''
        固定值zh。语言选择,目前只有中英文混合模式，填写固定值zh
        客户端类型选择，web端填写固定值1
        spd语速，取值0-15，默认为5中语速(选填)
        pit音调，取值0-15，默认为5中语调（选填）
        vol音量，取值0-15，默认为5中音量（选填）
        per发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
        '''
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        name_music = str(flag_last_music_name)
        last_name_music = str(flag_last_music_name - 1)
        path = './mymusic/%s.mp3' % (name_music)
        last_path = './mymusic/%s.mp3' % (last_name_music)
        if not isinstance(result, dict):
            with open(path, 'wb') as f:
                f.write(result)
        pc_play_music(path)
        if (flag_last_music_name > 2):
            try:
                os.remove(last_path)
            except:
                print("没有发现应该删除的音频")
        #我的意思是音乐播放完就删除，要不然一直生成语音文件，谁受得了
#这个是我给自己写的闹钟程序，可以设定时间让他触发。达到延时就触发
def delay_time_sleep():
    while(1):
        str_time = ex.lineEdit_delay_m.text()
        if str_time:
            minute_set = int(str_time)
            print("开始休息了")
            global flag_wake_up
            if flag_wake_up:
                play_sentence("休息设置已经取消")
                break
            else:
                print("休息主循环开启")
            born_seconds=minute_set*60
            print("要延时",born_seconds)
            while(born_seconds):
                if flag_wake_up:
                    print("休息内循环关闭")
                    break
                else:
                    born_seconds-=1
                    time.sleep(1)
                    print("时间还剩",born_seconds)
                if born_seconds==0:
                    word_say="%d分钟的休息已经到时，休息吧，我的主人"%(minute_set)
                    play_sentence(word_say)
#语音的记录文件，用于录音用的
def record_voice(time_long):
    DATA_CHUNK=1024
    FORMAT_VOICE=pyaudio.paInt16
    CHANNELS_SINGLE=1
    DATA_RATE=16000
    MY_SECONDES=time_long
    MY_FILENAME="D:/temp_record_voice.wav"
    my_pyaudio=pyaudio.PyAudio()
    stream=my_pyaudio.open(format=FORMAT_VOICE,channels=CHANNELS_SINGLE,rate=DATA_RATE,input=True,frames_per_buffer=DATA_CHUNK)
    print("录音开始了")
    voice_data_chunk=[]
    display_second = 0
    now_time = datetime.datetime.now()
    for i in range(0, int(DATA_RATE / DATA_CHUNK * MY_SECONDES)):
        global start_voice
        if start_voice:
            next_time = datetime.datetime.now()
            temp_time = next_time - now_time
            if (temp_time.total_seconds() - 1 > 0):
                now_time = datetime.datetime.now()
                display_second = display_second + 1
                str_second=str(display_second) + "秒"
                ex.second_level.setText(str_second)
            data = stream.read(DATA_CHUNK)
            voice_data_chunk.append(data)
        else:
            break
    stream.stop_stream()
    stream.close()
    my_pyaudio.terminate()
    voice_file=wave.open(MY_FILENAME,"wb")
    voice_file.setnchannels(CHANNELS_SINGLE)
    voice_file.setsampwidth(my_pyaudio.get_sample_size(FORMAT_VOICE))
    voice_file.setframerate(DATA_RATE)
    voice_file.writeframes(b''.join(voice_data_chunk))
    voice_file.close()
    print("录音结束")
    global stop_voice
    stop_voice=True
#识别录音文件，将语音转化为文字。
def get_text():
    global start_voice
    global stop_voice
    start_voice=False
    while(1):
        if stop_voice:#百度的语音转文字，账户自己注册一个去
            APP_ID = ''
            API_KEY = ''
            SECRET_KEY = ''
            client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
            get_voice_file = open("D:/temp_record_voice.wav", "rb")
            voice_text = get_voice_file.read()
            # try:
            result = client.asr(voice_text, 'wav', 16000, {'dev_pid': '1936', })
            start_voice = True
            stop_voice = False
            if result['err_no'] == 0:
                return result['result'][0]
            else:
                return "识别错误"
        else:
            time.sleep(1)
            print("正在识别")
def thread_music_play(myword):
    global say_things
    say_things=myword
    ex.start_work5()
#手写识别的线程。
class WorkThread_recongnize_hand(QThread):
    sinOut_hand = pyqtSignal(str)
    def __init__(self, obj):
        super(WorkThread_recongnize_hand, self).__init__()
        self.obj = obj
    def run(self):
        ex.pushButton_hand_word.setEnabled(False)
        save_hand()
        hand_word=start_hand()
        self.sinOut_hand.emit(hand_word)
#根据句柄去截图
def save_hand():
    # 获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow("Qt5QWindowIcon", "墨宝无双")  # 窗口的类名可以用Visual Studio的SPY++工具获取
    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
    width = right - left
    height = bot - top
    # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(hWnd)
    # 创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    # 创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # 将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    # 保存bitmap到内存设备描述表
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

    # 如果要截图到打印设备：
    ###最后一个int参数：0-保存整个窗口，1-只保存客户区。如果PrintWindow成功函数返回值为1
    result = windll.user32.PrintWindow(hWnd, saveDC.GetSafeHdc(), 0)
    print(result)  # PrintWindow成功则输出1

    # 保存图像
    ##方法一：windows api保存
    ###保存bitmap到文件
    saveBitMap.SaveBitmapFile(saveDC, "C:\\Users\\Administrator\\Desktop\\hand_writing.bmp")
    print("保存成功")
#根据截图去识别手写笔迹
def start_hand():
    """
      手写文字识别WebAPI接口调用示例接口文档(必看):https://doc.xfyun.cn/rest_api/%E6%89%8B%E5%86%99%E6%96%87%E5%AD%97%E8%AF%86%E5%88%AB.html
      图片属性：jpg/png/bmp,最短边至少15px，最长边最大4096px,编码后大小不超过4M,识别文字语种：中英文
      webapi OCR服务参考帖子(必看)：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=39111&highlight=OCR
      (Very Important)创建完webapi应用添加服务之后一定要设置ip白名单，找到控制台--我的应用--设置ip白名单，如何设置参考：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=41891
      错误码链接：https://www.xfyun.cn/document/error-code (code返回错误码时必看)
      @author iflytek
    """
    # OCR手写文字识别接口地址
    URL = "http://webapi.xfyun.cn/v1/service/v1/ocr/handwriting"
    # 应用APPID(必须为webapi类型应用,并开通手写文字识别服务,参考帖子如何创建一个webapi应用：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=36481)
    APPID = ""#讯飞的手写识别接口，账户自己注册去
    # 接口密钥(webapi类型应用开通手写文字识别后，控制台--我的应用---手写文字识别---相应服务的apikey)
    API_KEY = ""

    def getHeader():
        curTime = str(int(time.time()))
        param = "{\"language\":\"" + language + "\",\"location\":\"" + location + "\"}"
        paramBase64 = base64.b64encode(param.encode('utf-8'))

        m2 = hashlib.md5()
        str1 = API_KEY + curTime + str(paramBase64, 'utf-8')
        m2.update(str1.encode('utf-8'))
        checkSum = m2.hexdigest()
        # 组装http请求头
        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': APPID,
            'X-CheckSum': checkSum,
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        return header

    def getBody(filepath):
        with open(filepath, 'rb') as f:
            imgfile = f.read()
        data = {'image': str(base64.b64encode(imgfile), 'utf-8')}
        return data

    # 语种设置
    language = "cn|en"
    # 是否返回文本位置信息
    location = "true"
    # 图片上传接口地址
    picFilePath = "C:\\Users\\Administrator\\Desktop\\hand_writing.bmp"
    # headers=getHeader(language, location)
    r = requests.post(URL, headers=getHeader(), data=getBody(picFilePath))
    # print(r)
    print(r.content.decode())
    a = json.loads(r.content.decode())
    print(a)
    ww = a['data']['block'][0]['line']
    hand_word=''
    for i in ww:
        hand_word=hand_word+i['word'][0]['content']+'\n'
    print(hand_word)
    return hand_word
class WorkThread_play_sentence(QThread):
    def __init__(self, obj):
        super(WorkThread_play_sentence, self).__init__()
        self.obj = obj
    def run(self):
        global say_things
        play_sentence(say_things)
class WorkThread_start_voice(QThread):
    sinOut1= pyqtSignal(str)
    def __init__(self, obj):
        super(WorkThread_start_voice, self).__init__()
        self.obj = obj
    def run(self):
        ex.open_voice.setEnabled(False)
        record_voice(600)

        self.sinOut1.emit('1')
class WorkThread_recongnize_voice(QThread):
    sinOut2= pyqtSignal(str)
    def __init__(self, obj):
        super(WorkThread_recongnize_voice, self).__init__()
        self.obj = obj
    def run(self):
        info_text=get_text()
        self.sinOut2.emit(info_text)
        ex.open_voice.setEnabled(True)
class WorkThread_delay_sleep(QThread):
    sinOut4= pyqtSignal(str)
    def __init__(self, obj):
        super(WorkThread_delay_sleep, self).__init__()
        self.obj = obj
    def run(self):
        delay_time_sleep()
        # self.sinOut4.emit(info_text)
class WorkThread_play_voice(QThread):
    sinOut3= pyqtSignal(str)
    def __init__(self, obj):
        super(WorkThread_play_voice, self).__init__()
        self.obj = obj
    def run(self):
        ex.text_voice.setEnabled(False)
        voice_text=ex.textEdit_text.toPlainText()
        play_sentence(voice_text)
        ex.text_voice.setEnabled(True)
        self.sinOut3.emit('1')
def select_all_info_base_time(flag_info):
    search_sql = "select * from record_thoughts where time like '%s'" % (flag_info)
    cur1.execute(search_sql)
    all_info = cur1.fetchall()
    return all_info
def select_get_text(flag_info):
        flag_info = '%' + flag_info + '%'
        search_sql = "select * from record_thoughts where thoughts like '%s' or time like '%s'" % (flag_info, flag_info)
        cur1.execute(search_sql)
        all_info = cur1.fetchall()
        count_list = len(all_info)
        if all_info:
            head_info = "想法数据%d条，思维要比行动更快，思维要比行动扩展的更厉害，思维应当有足够的深度" % (len(all_info)) + "\n"
            ex.textEdit_text.insertPlainText(head_info)
            count = 0
            for i in all_info:
                thought_info = "想法信息:" + i[0]
                time_info = "时间信息:" + i[1]
                should_info = thought_info + "\n" + time_info + "\n" + "••★••" * 10 + "\n"
                ex.textEdit_text.insertPlainText(should_info)
                data_time_list = QStandardItem(i[1])
                ex.model.setItem(count, 0, data_time_list)
                count += 1
            ex.tableView_part.setModel(ex.model)
        else:
            ex.textEdit_text.insertPlainText("\n没有寻找到数据")
def select_info():
    if ex.radioButton_heaven.isChecked():
        # print("天道风雷")
        flag_info=ex.lineEdit_search.text()
        ex.model.clear()
        select_get_text(flag_info)
    else:
        # print("地泽万物")
        flag_info=ex.get_select_content()
        if flag_info:
            select_get_text(flag_info)
def delete_info():
    def delete_get_text(flag_info):
        temp_info=select_all_info_base_time(flag_info)
        if len(temp_info)==0:
            thread_music_play("没有找到id,因此无法删除任何信息")
        else:
            delete_sql = "delete record_thoughts where time like '%s'" % (flag_info)
            cur1.execute(delete_sql)
            conn.commit()
    if ex.radioButton_heaven.isChecked():
        flag_info = ex.lineEdit_search.text()
        delete_get_text(flag_info )
        clear_info()
        ex.textEdit_text.insertPlainText("\n信息已经删除")
    else:
        flag_info=ex.get_select_content()
        if flag_info:
            delete_get_text(flag_info)
            flag_info = ex.lineEdit_search.text()
            ex.model.clear()
            select_get_text(flag_info)
            clear_info()
            ex.textEdit_text.insertPlainText("\n信息已经删除")
def update_info():
    def update_get_text(flag_info):
        temp_info = select_all_info_base_time(flag_info)
        if len(temp_info) == 0:
            thread_music_play("没有找到id,因此无法更新任何信息")
        else:
            thought_info = ex.textEdit_text.toPlainText()
            nowTime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
            update_sql = "update record_thoughts set thoughts = '%s' where  time like '%s'" % (
            thought_info, flag_info)
            cur1.execute(update_sql)
            conn.commit()
            clear_info()

    if ex.radioButton_heaven.isChecked():
        flag_info = ex.lineEdit_search.text()
        update_get_text(flag_info)
    else:
        flag_info=ex.get_select_content()
        if flag_info:
            update_get_text(flag_info)
    flag_info = ex.lineEdit_search.text()
    ex.model.clear()
    select_get_text(flag_info)
    clear_info()
    ex.textEdit_text.insertPlainText("\n信息已经更新")
def insert_info():
    thought_info = ex.textEdit_text.toPlainText()
    nowTime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    insert_sql = "insert record_thoughts values('%s','%s') " % (thought_info, nowTime_str)
    cur1.execute(insert_sql)
    conn.commit()
    clear_info()
    ex.textEdit_text.insertPlainText("\n信息已经添加")
def clear_info():
    ex.textEdit_text.setText("")
#记录手写笔迹的函数
class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        # resize设置宽高，move设置位置
        self.resize(1000, 500)
        self.move(100, 100)
        self.setWindowTitle('墨宝无双')
        # setMouseTracking设置为False，否则不按下鼠标时也会跟踪鼠标事件
        '''
            要想将按住鼠标后移动的轨迹保留在窗体上
            需要一个列表来保存所有移动过的点
        '''
        self.pos_xy = []
    def remove_hand(self):
        self.pos_xy = []

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)

        '''
            首先判断pos_xy列表中是不是至少有两个点了
            然后将pos_xy中第一个点赋值给point_start
            利用中间变量pos_tmp遍历整个pos_xy列表
                point_end = pos_tmp

                判断point_end是否是断点，如果是
                    point_start赋值为断点
                    continue
                判断point_start是否是断点，如果是
                    point_start赋值为point_end
                    continue

                画point_start到point_end之间的线
                point_start = point_end
            这样，不断地将相邻两个点之间画线，就能留下鼠标移动轨迹了
        '''
        if len(self.pos_xy) > 1:
            point_start = self.pos_xy[0]
            for pos_tmp in self.pos_xy:
                point_end = pos_tmp

                if point_end == (-1, -1):
                    point_start = (-1, -1)
                    continue
                if point_start == (-1, -1):
                    point_start = point_end
                    continue

                painter.drawLine(point_start[0], point_start[1], point_end[0], point_end[1])
                point_start = point_end
        painter.end()

    def mouseMoveEvent(self, event):
        '''
            按住鼠标移动事件：将当前点添加到pos_xy列表中
            调用update()函数在这里相当于调用paintEvent()函数
            每次update()时，之前调用的paintEvent()留下的痕迹都会清空
        '''
        # 中间变量pos_tmp提取当前点
        pos_tmp = (event.pos().x(), event.pos().y())
        # pos_tmp添加到self.pos_xy中
        self.pos_xy.append(pos_tmp)

        self.update()

    def mouseReleaseEvent(self, event):
        '''
            重写鼠标按住后松开的事件
            在每次松开后向pos_xy列表中添加一个断点(-1, -1)
            然后在绘画时判断一下是不是断点就行了
            是断点的话就跳过去，不与之前的连续
        '''
        pos_test = (-1, -1)
        self.pos_xy.append(pos_test)

        self.update()

    def start_workthread(self):
        # 创建线程
        self.thread1 = WorkThread_recongnize_hand(obj="1")
        self.thread1.sinOut_hand.connect(self.put_word_win)  # 进程连接回传到GUI的事件
        print("Thread14 id:", id(self.thread1))  # 每执行一次，创建一个子线程对象，互不影响
        # 开始线程
        print("手写文字识别线程已经启动")
        self.thread1.start()
    def put_word_win(self,content):
        if content[0:4]=="墨宝无双":
            ex.textEdit_text.insertPlainText("\n应如是:"+content[5:]+"\n")
        else:
            ex.textEdit_text.insertPlainText("\n应如是:" + content + "\n")
        ex.pushButton_hand_word.setEnabled(True)
        self.remove_hand()
#主界面
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 470)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.open_voice = QtWidgets.QPushButton(self.centralWidget)
        self.open_voice.setGeometry(QtCore.QRect(0, 370, 75, 23))
        self.open_voice.setObjectName("open_voice")
        self.recongnize_voice = QtWidgets.QPushButton(self.centralWidget)
        self.recongnize_voice.setGeometry(QtCore.QRect(160, 370, 75, 23))
        self.recongnize_voice.setObjectName("recongnize_voice")
        self.second_level = QtWidgets.QLabel(self.centralWidget)
        self.second_level.setGeometry(QtCore.QRect(570, 70, 54, 12))
        self.second_level.setObjectName("second_level")
        self.textEdit_text = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_text.setGeometry(QtCore.QRect(0, 40, 551, 301))
        self.textEdit_text.setObjectName("textEdit_text")
        self.text_voice = QtWidgets.QPushButton(self.centralWidget)
        self.text_voice.setGeometry(QtCore.QRect(80, 370, 75, 23))
        self.text_voice.setObjectName("text_voice")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_search = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_search.setGeometry(QtCore.QRect(90, 12, 113, 20))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(240, 370, 75, 23))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_update = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_update.setGeometry(QtCore.QRect(320, 370, 75, 23))
        self.pushButton_update.setObjectName("pushButton_update")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 370, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(470, 370, 75, 23))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 75, 23))
        self.label.setObjectName("label")
        self.lineEdit_time = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_time.setGeometry(QtCore.QRect(370, 12, 113, 20))
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(560, 150, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit_delay_m = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_delay_m.setGeometry(QtCore.QRect(590, 146, 51, 20))
        self.lineEdit_delay_m.setObjectName("lineEdit_delay_m")
        self.pushButton_sleep = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_sleep.setGeometry(QtCore.QRect(570, 190, 75, 23))
        self.pushButton_sleep.setObjectName("pushButton_sleep")
        self.tableView_part = QtWidgets.QTableView(self.centralWidget)
        self.tableView_part.setGeometry(QtCore.QRect(645, 41, 171, 301))
        self.tableView_part.setObjectName("tableView_part")
        self.radioButton_heaven = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_heaven.setGeometry(QtCore.QRect(690, 10, 89, 16))
        self.radioButton_heaven.setObjectName("radioButton_heaven")
        self.radioButton_earth = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_earth.setGeometry(QtCore.QRect(740, 10, 89, 16))
        self.radioButton_earth.setObjectName("radioButton_earth")
        self.pushButton_stop_voice = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_stop_voice.setGeometry(QtCore.QRect(550, 370, 75, 23))
        self.pushButton_stop_voice.setObjectName("pushButton_stop_voice")
        self.pushButton_clear_hand = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_clear_hand.setGeometry(QtCore.QRect(570, 290, 75, 23))
        self.pushButton_clear_hand.setObjectName("pushButton_clear_hand")
        self.pushButton_hand_word = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_hand_word.setGeometry(QtCore.QRect(570, 320, 75, 23))
        self.pushButton_hand_word.setObjectName("pushButton_hand_word")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 831, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_voice.setText(_translate("MainWindow", "开启录音"))
        self.recongnize_voice.setText(_translate("MainWindow", "识别录音"))
        self.second_level.setText(_translate("MainWindow", "读秒"))
        self.text_voice.setText(_translate("MainWindow", "播放文本"))
        self.pushButton.setText(_translate("MainWindow", "查询:"))
        self.pushButton_delete.setText(_translate("MainWindow", "删除"))
        self.pushButton_update.setText(_translate("MainWindow", "修改"))
        self.pushButton_2.setText(_translate("MainWindow", "添加"))
        self.pushButton_clear.setText(_translate("MainWindow", "清空"))
        self.label.setText(_translate("MainWindow", "时间:"))
        self.label_2.setText(_translate("MainWindow", "定时:"))
        self.pushButton_sleep.setText(_translate("MainWindow", "设定休息"))
        self.radioButton_heaven.setText(_translate("MainWindow", "司天"))
        self.radioButton_earth.setText(_translate("MainWindow", "司地"))
        self.pushButton_stop_voice.setText(_translate("MainWindow", "停止播放"))
        self.pushButton_clear_hand.setText(_translate("MainWindow", "擦除重写"))
        self.pushButton_hand_word.setText(_translate("MainWindow", "笔迹识别"))

    def init_ui(self):
        self.model = QStandardItemModel()  # 存储任意结构数据
        nowTime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
        self.lineEdit_time.setText(nowTime_str)
        self.second_level.setText("读秒")
        self.recongnize_voice.setText("识别录音")
        self.open_voice.setText("开启录音")
        self.open_voice.pressed. connect(self.start_work1)
        self.recongnize_voice.pressed.connect(self.start_work2)
        self.text_voice.pressed.connect(self.start_work3)
        self.pushButton.pressed.connect(select_info)
        self.pushButton_delete.pressed.connect(delete_info)
        self.pushButton_update.pressed.connect(update_info)
        self.pushButton_2.pressed.connect(insert_info)
        self.pushButton_clear.pressed.connect(clear_info)
        self.pushButton_sleep.pressed.connect(self.control_sleep_time)
        self.radioButton_heaven.setChecked(True)
        self.pushButton_stop_voice.pressed.connect(self.stop_voice)
        self.tableView_part.setFont(QFont("Times",10,QFont.Black))

    def start_work1(self):
        # 创建线程
        self.thread1 = WorkThread_start_voice(obj="1")
        self.thread1.start()
    def start_work2(self):
        # 创建线程
        self.thread2 = WorkThread_recongnize_voice(obj="2")
        self.thread2.sinOut2.connect(self.show_info)
        self.thread2.start()

    def start_work3(self):
        # 创建线程
        self.thread3 = WorkThread_play_voice(obj="3")
        self.thread3.start()
    def start_work4(self):
        # 创建线程
        self.thread4 = WorkThread_delay_sleep(obj="4")
        self.thread4.start()
    def start_work5(self):
        # 创建线程
        self.thread5= WorkThread_play_sentence(obj="5")
        self.thread5.start()
    def show_info(self,context):
        # self.textEdit_text.setText()
        self.textEdit_text.insertPlainText("\n要多想:"+context+"\n")
    def control_sleep_time(self):
        global flag_wake_up
        if self.pushButton_sleep.text()=="设定休息":
            ex.start_work4()
            self.pushButton_sleep.setText("正在休息")

            flag_wake_up=False
        elif self.pushButton_sleep.text()=="正在休息":
            self.pushButton_sleep.setText("设定休息")

            flag_wake_up=True
    def get_select_content(self):
        r=self.tableView_part.currentIndex().row()
        uer_id = self.model.data(self.model.index(r, 0))
        return uer_id
    def stop_voice(self):
        stop_voice_info()
        ex.text_voice.setEnabled(True)

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QMainWindow()
ex = Ui_MainWindow()
ex.setupUi(w)
ex.init_ui()
hand_test = Example()
hand_test.show()
def delay_init():
    ex.pushButton_clear_hand.clicked.connect(hand_test.remove_hand)
    ex.pushButton_hand_word.clicked.connect(hand_test.start_workthread)
delay_init()
w.show()
while (1):
    QApplication.processEvents()
sys.exit(app.exec_())
