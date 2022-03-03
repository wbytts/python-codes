from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio import start_server

# 输入框
input_res = input("please input your name:")
print('browser input is:', input_res)

# 密码框
pwd_res = input("please input your password:",type=PASSWORD)
print('password:', pwd_res)

# 下拉框
select_res = select("please select your city:",['北京','西安','成都'])
print('your city is:',select_res)

# checkbox
checkbox_res = checkbox("please confirm the checkbox:",options=['agree','disagree'])
print('checkbox:', checkbox_res)

# 文本框
text_res = textarea("please input what you want to say:",rows=3,placeholder='...')
print('what you said is:',text_res)

# 文件上传
upload_res = file_upload("please upload what you want to upload:",accept="image/*")

with open(upload_res.get('filename'),mode='wb') as f: # 因为读取的图片内容是二进制，所以要以wb模式打开
    f.write(upload_res.get('content'))
print('what you uploaded is:',upload_res.get('filename'))

# 滑动条

sld = slider('这是滑动条',help_text='请滑动选择')  # 缺点是不能显示当前滑动的值
toast('提交成功')
print(sld)

# 单选选项

radio_res = radio(
    '这是单选',
    options=['西安','北京','成都']
    )
print(radio_res)

# 更新输入项

Country2City={
    'China':['西安','北京','成都'],
    'USA': ['纽约', '芝加哥', '佛罗里达'],
}

countries = list(Country2City.keys())

update_res = input_group(
    "国家和城市联动",
    [
        # 当国家发生变化的时候，onchange触发input_update方法去更新name=city的选项，更新内容为Country2City[c]，c代表国家的选项值
        select('国家',options=countries,name='country',onchange=lambda c: input_update('city',options=Country2City[c])),
        select('城市',options=Country2City[countries[0]],name='city')
    ]
)

print(update_res)
