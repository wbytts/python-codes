choices = {
    'A': lambda: print('A'),
    'B': lambda: print('B'),
    'C': lambda: print('C'),
    'D': lambda: print('D'),
    'E': lambda: print('E'),
}

choices.get('B', lambda: print('default'))()

# =================================================================
key = 'B'
{
    'A': (lambda: print('A')),
    'B': (lambda: print('B')),
    'C': (lambda: print('C')),
}[key]()
