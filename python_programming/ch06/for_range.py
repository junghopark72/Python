# for_range.py

nest = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]

for x in range(len(nest)):
    for y in range(len(nest[x])):
        print("nest[%d][%d]: %d" % (x, y, nest[x][y]))
