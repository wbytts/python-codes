import json

class JsonData:

    def __init__(self):
        try:
            f = open('./data.json', 'r')
            s = f.read()
            self.data = json.loads(s)
            f.close()
        except:
            f = open('./data.json', 'w')
            self.data = {}
            s = json.dumps(self.data)
            f.write(s)
            f.close()

    def get_dict(self):
        return self.data

    def save_dict(self):
        f = open('./data.json', 'w')
        # self.data = data
        s = json.dumps(self.data)
        f.write(s)
        f.close()


class WordsBook:

    def __init__(self):
        pass

    @classmethod
    def get_data(cls):
        pass

    @classmethod
    def save_data(self):
        pass


