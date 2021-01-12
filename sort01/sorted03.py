#!/usr/bin/python3

# create a custom function for sorting
# the fuction take_second will always return
# what is in the second position
# take the second element for sort
def take_second(secondplacewins):
    return secondplacewins[1]

# random list of tuples
puzzle = [(3, "antelope"), ("Alta", " "), ("Research", "banana", 3.14159265359, "pi")]
simpsons = [ ('Moe', "?"), ('Otto', '?'), ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34) ]


# sort list with our custom key take_second
sorted_list = sorted(puzzle, key = take_second)

# print list
print('Sorted list:', sorted_list)
for key, value in simpsons:
    print(key, value)


def byAge(characterbio):
    # isinstance can test if a value is an int, float, str, etc.
    if isinstance(characterbio[1], int):
        return characterbio[1]
    else:
        return 1000  # if a user does not have an age, return 1000
        # which will put them at the end of the list

simpsonsAge = sorted(simpsons, key=byAge)

print('Result of sorted(simpsons, key=byAge): ', simpsonsAge)
