def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def divide(first_term, second_term):
    if second_term == 0:
        raise Exception("Divide by zero")
    else:
        return first_term / second_term
