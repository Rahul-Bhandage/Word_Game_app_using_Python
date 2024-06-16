import csv

def read_words(filename):
    levels = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Ignore empty lines
                level, word = line.strip().split(',')
                if level not in levels:
                    levels[level] = []
                levels[level].append(word)
    return levels

def generate_csv(words_by_level):
    with open('words.csv', 'w', newline='') as csvfile:
        fieldnames = ['Level 1', 'Level 2', 'Level 3']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(len(words_by_level['1'])):
            writer.writerow({
                'Level 1': words_by_level['1'][i],
                'Level 2': words_by_level['2'][i],
                'Level 3': words_by_level['3'][i],
            })

words_by_level = read_words('words.txt')
generate_csv(words_by_level)
print("CSV file 'words.csv' generated successfully!")
