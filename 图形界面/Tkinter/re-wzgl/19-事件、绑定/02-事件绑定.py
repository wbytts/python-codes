"""
widget.bind(event, handler)
event是事件名称，handler是处理函数

鼠标事件：鼠标相对控件的位置会x和y会存入event对象中
    <Button-1>          左键单击
    <Button-2>          中键单击
    <Button-3>          右键单击
    <Button-4>          滑轮上滚
    <Button-5>          滑轮下滚
    <Motion>            鼠标移动
    <B1-Motion>         拖拽，按住左键移动
    <B2-Motion>         拖拽，按住中键移动
    <B3-Motion>         拖拽，按住右键移动
    <ButtonRelease-1>   释放左键
    <ButtonRelease-2>   释放中键
    <ButtonRelease-3>   释放右键
    <Double-Button-1>   双击左键
    <Double-Button-2>   双击中键
    <Double-Button-3>   双击右键
    <Enter>             鼠标进入
    <Leave>             鼠标离开

键盘事件：
    <FocusIn>   键盘焦点进入控件
    <FocusOut>  键盘焦点离开控件
    <Return>    按下Enter键，键盘所有键都可以被绑定，。Cancel BackSpace Tab Shift Ctrl Alt End Esc 。。。首字母大写
    <Key>       按下键盘的某个键。键值会被存储到event对象中
    <Shift-Up>  按住Shift时按下Up
    <Alt-Up>    按住Alt时按下Up
    <Ctrl-Up>   按住Ctrl时按下Up

控件相关事件：
    <Configure> 更改控件的大小和位置，新控件的大小和位置会存入event对象

取消绑定：
    obj.unbind('<xxx>')
"""
