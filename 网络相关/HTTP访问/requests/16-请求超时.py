import requests

"""
可以告诉 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应。
基本上所有的生产代码都应该使用这一参数。如果不使用，你的程序可能会永远失去响应
"""
