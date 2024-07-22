from collections import defaultdict

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

file_path =  'words_alpha.txt'

with open(file_path, 'r', encoding='utf-8') as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]


Cwords  = [3,4,5,6,7,8,9,10] #words between length 3 - 10
for i in range (0,len(Cwords)):
 Cwords[i] = [string for string in lines if len(string) == i+3]



last_res =...  #result of the last input
last_attempt = ...
while 1:

    #user input
    corr= True
    while corr:
     word_length = int(input("Length of the word: "))
     if(word_length >= 3 and word_length <= 10):
      corr= False
     else: 
         print ("unsupported word length")
    guess_ammount = int(input("Number of guesses: "))


    words =  Cwords[word_length -3]

   


    #creating a double array, where each alphabet letter gets the words, its featured in
    sorted_by_letter = alphabet
    for i in range(len(alphabet)):
        tmp = []
        for word in words:
            if alphabet[i] in word:
                tmp.append(word)
        sorted_by_letter[i] = tmp






    def findBestWord(sorted_by_letter1): 
     global last_attempt
     word_occurrences = defaultdict(lambda: {'count': 0, 'total_words': 0})

     # Step 2: Iterate over the double array to populate the dictionary
     for sub_array in sorted_by_letter1:
        seen_words = set()  # Track words seen in this sub-array to avoid counting duplicates within the same array
        for word in sub_array:
            if word not in seen_words:
                word_occurrences[word]['count'] += 1
                word_occurrences[word]['total_words'] += len(sub_array)
                seen_words.add(word)

    # Step 3: Calculate the metric and find the word with the highest value
     max_value = 0
     max_word = None

     for word, data in word_occurrences.items():
        metric = data['count'] * data['total_words']
        if metric > max_value:
            max_value = metric
            max_word = word

    # max_word is the word that appears in the most arrays multiplied by the number of words in those arrays
     print(f"\nThe word with the highest metric is: {max_word} \n\n")
     last_attempt=max_word



    while 1:
        guess_ammount -=1
        findBestWord(sorted_by_letter)
  
        if(guess_ammount == 0):
            break

        print( "Please input the word, replacing the colored letters with numbers.")
        print( "green = 1    yellow = 2")
        last_res= input("Result:   ")

        #filter "sorted_by_letter[]" by the previous result by first removing dark letters
        for i in range(len(sorted_by_letter)): 
            counter =0
            for char in last_res:

                if not char.isdigit():
                  sorted_by_letter[i] = [word for word in sorted_by_letter[i] if char not in word]

                if char == '2':
                  sorted_by_letter[i] = [word for word in sorted_by_letter[i] if last_attempt[counter] in word]  # remove all words without "last_attempt[counter]"
                  sorted_by_letter[i] = [word for word in sorted_by_letter[i] if word[counter] != last_attempt[counter]]  # remove all words with the letter "last_attempt[counter]" at the current searched-for place
                
                if char == '1':
                    sorted_by_letter[i] = [word for word in sorted_by_letter[i] if last_attempt[counter] in word]  # remove all words without "last_attempt[counter]"

                counter +=1
   




