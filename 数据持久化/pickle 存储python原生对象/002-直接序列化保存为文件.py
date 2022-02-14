import pickle

m = [1, 2, 3, 4, 5]

fw = open('m.pickle', 'wb')
pickle.dump(m, fw)
fw.close()

fr = open('m.pickle', 'rb')
read_m = pickle.load(fr)
fr.close()
print(read_m)
