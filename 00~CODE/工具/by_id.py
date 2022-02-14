import uuid

def get_uuid4():
    return uuid.uuid4().__str__().replace('-', '')


