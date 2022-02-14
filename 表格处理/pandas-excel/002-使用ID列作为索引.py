import pandas as pd

df = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Tim', 'Victor', 'Nick']
})
df = df.set_index('ID')
df.to_excel('files/demo1.xlsx')


