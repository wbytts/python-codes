
L = ['10.32.119', '10.32.121', '10.32.124', '10.32.106', '10.32.118', '10.32.111', '10.32.110']
ip_list = [f'{s}.{i}' for s in L for i in range(0,24+1)]
print(ip_list)
