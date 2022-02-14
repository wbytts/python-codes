import json

data = {
    'words': [
        {'name': 'apple', 'desc': '苹果'}
    ],
}


def save_data():
    f = open('./data.json', 'w')
    s = json.dumps(data)
    f.write(s)
    f.close()


def get_data():
    f = open('./data.json', 'r')
    s = f.read()
    data = json.loads(s)
    f.close()
    return data



