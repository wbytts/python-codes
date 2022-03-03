import shelve

sdb = shelve.open("F:/temp/shelve-storage/demo.shelve")
sdb['alist'] = [1, 2, 3, 4, 5]


