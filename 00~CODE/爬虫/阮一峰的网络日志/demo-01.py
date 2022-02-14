import requests

start_time = '/2003/12/'

time_list = [f'/{year}/{month}/' for year in range(2003, 2021+1) for month in range(1, 12+1)]
base_url = 'https://www.ruanyifeng.com/blog'

print(time_list)

