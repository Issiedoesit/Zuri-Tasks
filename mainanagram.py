
import string
print(' ')
print("Welcome to Anagrammer. We accept input of any two words and determine if they are anagrams")
print(' ')
print('Please note that all punctuations and capital letters in your entry are cleaned and do not count in our program.\nIt will return True or False on whether they are anagrams')
print(' ')

#Numbers can be used within anagrams and can be anagrams themselves. 
#To run the program to remove numbers, Uncomment line 41 and 42

while True:

    def find_anagram(word_entry, anagram):
        print(' ')
        word_entry = input('Enter your first word: ')
        anagram = input('Enter your second word: ')
        word_one = word_entry.lower()
        word_two = anagram.lower()
        word_one = ''.join(str(word_one).split(' '))
        word_two = ''.join(str(word_two).split(' '))

        words = word_one
        new_words_one = []
        for word in words:
            for letter in word:
                if letter in string.punctuation:
                    word = word.replace(letter,"")   
            new_words_one.append(word)


        words = word_two
        new_words_two = []
        for word in words:
            for letter in word:
                if letter in string.punctuation:
                        word = word.replace(letter,"")   
            new_words_two.append(word)
       
       
        #new_words_one = ''.join([i for i in new_words_one if not i.isdigit()])
        #new_words_two = ''.join([i for i in new_words_two if not i.isdigit()])

        word_one_joined = ''.join(new_words_one)
        word_two_joined = ''.join(new_words_two)
        word_one_sort = sorted(word_one_joined)
        word_two_sort = sorted(word_two_joined)
      

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

