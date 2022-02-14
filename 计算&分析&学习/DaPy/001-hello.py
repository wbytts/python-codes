import DaPy as dp

datas = dp.DataSet('C:/Users/hp/Desktop/交替登陆/需要删除新vpn/1交替登录.csv') # 初始化数据集

f = datas.readframe() # 数据框方式读取数据
print(f)
