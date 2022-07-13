from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


printRed = lambda t: print(f"\033[31m{t}\033[0m")

class User(BaseModel):
    id: int
    name: str = "张三"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []  # 列表中的元素要是int类型，或者可以直接转换成int类型


external_data = {
    "id": "123",
    "signup_ts": "2022-12-22 12:22",
    "friends": [1, 2, "3"]
}

user = User(**external_data)


printRed("----------你好啊----------")
print(user.dict())
print(user.copy())  # 浅拷贝
print(user.json())
print(user.schema())
print(user.schema_json())

# User.parse_obj()  # 从一个对象解析模型类
# User.parse_raw()  # 从字符串解析模型类
# User.parse_file()  # 从一个文件解析模型类
User.construct(**external_data)  # 不校验数据，直接创建模型类


