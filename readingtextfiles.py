import string


def read_file_content(story):
    with open(story) as f:
        contents = f.read()
        print('')
        print('The text within the file is:')
        print('')
        print(str(contents))
        return contents.split()



text = read_file_content('story.txt')



from collections import Counter



def count_words():
    words = text
    new_words = []
    for word in words:
        for letter in word:
            if letter in string.punctuation:
                word = word.replace(letter,"")   
        new_words.append(word)
    lowered_text = [x.lower() for x in new_words]
    count = Counter(lowered_text)

    return count

print('This is the word count: \n \n' ,count_words())

