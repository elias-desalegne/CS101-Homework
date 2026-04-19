def fibonacci(upper_bound):

    the_sequence = [0,1]

    while True:
        number = the_sequence[-1] + the_sequence[-2]
        if number > upper_bound:
            break
        the_sequence.append(number)

    return the_sequence

    pass

print(fibonacci(10))