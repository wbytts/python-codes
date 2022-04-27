import pickle
import json

posts = None
with open('posts', 'rb') as f:
    posts = pickle.load(f)

for post in posts:
    with open('./blogs_json/' + post['postid'] + '.json', 'w', encoding='utf8') as f:
        f.write(str(post))
    with open('./articles/' + post['postid'] + '.md', 'w', encoding='utf8') as f:
        f.write(post['description'])