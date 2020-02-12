
# Example1

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(list(zipped))
# [(1, 'a'), (2, 'b'), (3, 'c')]

# Example2
floats = [4.0, 5.0, 6.0]
zipped = zip(integers, letters, floats)
print(list(zipped))
# [(1, 'a', 4.0), (2, 'b', 5.0), (3, 'c', 6.0)]

# Pass argument of unequal length
print(list(zip(range(5), range(100))))
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]


# if you don't want to ignore the extra values, if 2 values of longest thn use fill value
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zip_longest(numbers, letters, longest, fillvalue=None)
# [(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), (None, None, 3), (None, None, 4)]


# loop over multiple iterator at the same time
# O(N*M) (number of iterators * minimum size of iterator)
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print(f'Letter: {l}')
    print(f'Number: {n}')

