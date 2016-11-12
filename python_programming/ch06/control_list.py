A = ['blue', 'yellow', 'red']
B = ['red', 'green', 'blue']

new_pairs = [(a, b) for a in A for b in B if a != b]
print(new_pairs)
print(len(new_pairs))
