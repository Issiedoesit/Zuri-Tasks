# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


import string
print(' ')
print("Welcome to Anagrammer. We accept input of any two words and determine if they are anagrams")
print(' ')
print('Please note that all punctuations and capital letters in your entry are cleaned and do not count in our program')
print(' ')
while True:

    def find_anagram(word_entry, anagram):
        print(' ')
        word_entry = input('Enter your first word: ')
        anagram = input('Enter your second word: ')
        word_one = word_entry.lower()
        word_two = anagram.lower()
        word_one = ''.join(str(word_one).split(' '))
        word_two = ''.join(str(word_two).split(' '))
        #print(word_one)
        #print(word_two)

        words = word_one
        new_words_one = []
        for word in words:
            for letter in word:
                if letter in string.punctuation:
                    word = word.replace(letter,"")   
            new_words_one.append(word)

        #print(new_words_one)

        words = word_two
        new_words_two = []
        for word in words:
            for letter in word:
                if letter in string.punctuation:
                        word = word.replace(letter,"")   
            new_words_two.append(word)
        #print(new_words_two)

        word_one_joined = ''.join(new_words_one)
        word_two_joined = ''.join(new_words_two)
        word_one_sort = sorted(word_one_joined)
        word_two_sort = sorted(word_two_joined)
      
        #print(word_one_sort)
        #print(word_two_sort)

        print(' ')
        print('Running Anagrammer on \" {} \" and \" {} \"'.format(word_entry, anagram))
        print(' ')
        print('Clean-up on entry returned: Word [{}] and Word to compare[{}]'.format(word_one_joined, word_two_joined))
        

        if word_one_sort == word_two_sort:
            return True 
            
          
        else:
            return False
            
    
    anagrammer = find_anagram((), ())
    print(' ')
    print(anagrammer)
    print(' ')
    cont_d = input('Continue? Enter Y for Yes or N for No: ')
    if cont_d == 'Y':
        print(' ')
        print('Calling Anagrammer again')
        continue
    elif cont_d == 'N':
        print('')
        print('Bye Bye and see you again')
        break

i want to push
