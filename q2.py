import matplotlib.pyplot as plt

def graphSnowfall(t):
    """retrieves data from a text file t and displays the snowfall information in a bar chart."""
    # count for each column
    snowfallRanges = {
        '0-10': 0,
        '11-20': 0,
        '21-30': 0,
        '31-40': 0,
        '41-50': 0
    }

    # processing text file
    with open(t, 'r') as file:
        for line in file:
            snowfall = int(line.strip())
            if snowfall <= 10:
                snowfallRanges['0-10'] += 1
            elif snowfall <= 20:
                snowfallRanges['11-20'] += 1
            elif snowfall <= 30:
                snowfallRanges['21-30'] += 1
            elif snowfall <= 40:
                snowfallRanges['31-40'] += 1
            else:
                snowfallRanges['41-50'] += 1


    ranges = list(snowfallRanges.keys())
    counts = list(snowfallRanges.values())

    # adding labels, displaying chart, etc.
    plt.bar(ranges, counts, color='blue')
    plt.xlabel('Snowfall Range (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation')
    plt.show()

# example
graphSnowfall('q2_data.txt')
