from plotly.graph_objs import Scatter,Layout
import plotly
import plotly.offline as py
import numpy as np
import plotly.graph_objs as go

#setting offilne
plotly.offline.init_notebook_mode(connected=True)
# 上面几行代码主要是引用一些库，最重要的一点是要把plotly设置为offline模式，


N = 100
random_x = np.linspace(0,1,N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5

#Create traces
trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'markers',
    name = 'markers'
)
trace1 = go.Scatter(
    x = random_x,
    y = random_y1,
    mode = 'lines+markers',
    name = 'lines+markers'
)
trace2 = go.Scatter(
    x = random_x,
    y = random_y2,
    mode = 'lines',
    name = 'lines'
)
data = [trace0,trace1,trace2]
py.iplot(data)

# 随机设置4个参数，x轴的数字和y轴，其中y轴随机3组数据。
# 然后画三种类型的图，trace0是markers，trace1是折线图和markers,trace3是折线图。
# 然后把三种图放在data这个列表里面，调用py.iplot(data)即可。
