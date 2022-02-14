import os

os.system('''(
echo show databases;
) | mysql -u root --password=123456
''')

