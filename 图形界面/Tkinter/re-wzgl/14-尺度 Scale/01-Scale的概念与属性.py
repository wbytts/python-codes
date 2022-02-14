"""
尺度，Scale，用来产生并选择一个范围内的数字

label：默认没有标签文字，如果是水平的Scale则出现在左上角，如果是垂直的则出现在右上角
length：尺度条长度，默认是100像素
orient：方向，默认是垂直，可选 HORIZONTAL 和 VERTICAL
repeatdelay：按住滑块多久之后才能拖动，单位是毫秒，默认是 300ms
showvalue：正常会显示尺度条的目前值，设置为0则不显示
takefocus：正常的尺度条可以获取焦点，这个设为0则无法获取焦点
tickinterval：尺度条的标记刻度
troughcolor：槽（trough）的颜色

digits：尺度数值，读取时需要使用tk变量类型来读取
variable：设置或取得目前选取的尺度值
from_：尺度条的初始值
to：尺度条范围的末端值
resolution：每次改动的数值
"""
