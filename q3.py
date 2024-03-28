def wordCount(t):
    """
    retrives data in test file t and returns dictionary where the keys are unique words in the files and the corresponding
    values are lists of line numbers where the words are found in the text
    """
    word_dict = {}

    # process text file
    with open(t, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            words = line.split()
            for word in words:
                word = word.strip('.,!?').lower()
                if word not in word_dict:
                    word_dict[word] = [line_num]
                else:
                    if line_num not in word_dict[word]:
                        word_dict[word].append(line_num)

    return word_dict

# example:
word_occurrences = wordCount('q3_data.txt')
for word, line_numbers in word_occurrences.items():
    print(f'{word}: {line_numbers}')
