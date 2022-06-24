##    You are in charge of the cake for a child's birthday. You have decided
##    the cake will have one candle for each year of their total age. They
##    will only be able to blow out the tallest of the candles. Count how many
##    candles are tallest.

##### ##### ##### #####

#   Iterative Solution
#   O(n)
#   n is the length of integer_array
#   Solved in one pass over the array
#   Algo:
#       Iterate over the array keeping track of the largest integer found
#       Use a dictionary to keep track of the # of occurrences of each integer
#       Return the count of the largest integer found
#   Key Concepts:
#       Using a dictionary to store key:value pairs
#       Using try/except as a cleaner way to create and increment key:value pairs

def solutionOne(integer_array):

    largest_integer = 0
    integer_count_table = dict()

    for integer in integer_array:

        if integer > largest_integer:
            largest_integer = integer

        try:
            integer_count_table[integer] += 1

        except:
            integer_count_table[integer] = 1

    return integer_count_table[largest_integer]

##### ##### ##### #####
