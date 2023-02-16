# ****** Infinite Iterators******** (Part 1)

# from itertools import count


# def count_example(start, step):
#     counter = count(start, step)

#     for c in counter:
#         print(c)

#         if c == 100:
#             break


# count_example(10, 5)


# ******* Infinite Iterators******** (Part 1)

# from itertools import repeat


# def repeat_example(element, max_repeats):
#     repeater = repeat(element, max_repeats)

#     for val in repeater:
#         print(val)


# repeat_example("hello", 10)


# *******Infinite Iterators************ (Part 1)

# from itertools import cycle


# def cycle_example(elements):
#     i = 0
#     cycler = cycle(elements)

#     while i < 100:
#         print(next(cycler), end=" ")
#         i += 1


# cycle_example("ABCDEF")


# *********Terminating Iterators********* (Part 2)

# from itertools import accumulate


# def accumulate_example(elements):
#     running_sum = accumulate(elements)
#     print(list(running_sum))


# accumulate_example([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# *********Terminating Iterators********* (Part 2)

# from itertools import chain (A)


# def chain_example(elements1, elements2):
#     chained = chain(elements1, elements2)
#     print(list(chained))


# chain_example("ABC", "DEF")


# from itertools import chain  (B)


# def chain_from_iterable_example(iterable):  #Flattens the list
#     chained = chain.from_iterable(iterable)
#     print(list(chained))


# chain_from_iterable_example([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# *********Terminating Iterators********* (Part 2)


# from itertools import compress


# def compress_example(data, selectors):
#     compressed = compress(data, selectors)
#     print(list(compressed))


# compress_example([["a", "b", "c"], [1, 2, 3], [1, 0, 1], [True, False, True]])


# from itertools import pairwise


# def pairwise_example(iterable):
#     paired = pairwise(iterable)
#     print(list(paired))


# pairwise_example([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# from itertools import pairwise


# *********Combinatoric Iterators********* (Part 3)

# from itertools import product


# def product_example(iterable1, iterable2):
#     result = product(iterable1, iterable2)
#     print(list(result))


# product_example([1, 2, 3], ["a", "b", "c"])


# from itertools import permutations


# def permutations_example(iterable, size):
#     result = permutations(iterable, size)
#     print(list(result))


# permutations_example("ABCD", 2)


from itertools import combinations


def combinations_example(iterable, size):
    result = combinations(iterable, size)
    print(list(result))


combinations_example("ABCD", 2)


# https://docs.python.org/3/library/itertools.html
