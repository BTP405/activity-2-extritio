def statsDecorator(func):
    def wrapper(numbers):
        print("Numbers read:", numbers)
        print("Count:", len(numbers))
        print("Average:", sum(numbers) / len(numbers))
        print("Maximum:", max(numbers))
        print("-" * 30)
        return func(numbers)
    return wrapper

@statsDecorator
def process_numbers(numbers):
    pass

def printStats(t):
    """
    retrieves data from a text file t and calls a decorator function for each line,
    which prints stats about the numbers in that line
    """
    with open(t, 'r') as file:
        for line in file:
            numbers = [int(num) for num in line.split()]
            process_numbers(numbers)

# example
printStats('q4_data.txt')
