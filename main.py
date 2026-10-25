import sys

def main():

        
    words = {'hi': 0, 'hello': 1, 'good': 2, 'morning': 3, 'bye': 4, 'see': 5, 'you': 6, 'goodbye': 7, 'how': 8, 'are': 9, 'what': 10, 'is': 11, 'this': 12, 'ok': 13}
    word_ids = {}


    for word, word_id in words.items():         
        word_ids[word_id] = word


    training_data = [
        { "text": "hi", "label": "greeting" },
        { "text": "hello", "label": "greeting" },
        { "text": "good morning", "label": "greeting" },
        
        { "text": "bye", "label": "goodbye" },
        { "text": "see you", "label": "goodbye" },
        { "text": "goodbye", "label": "goodbye" },
        
        { "text": "how are you", "label": "question" },
        { "text": "what is this", "label": "question" },
        { "text": "are you ok", "label": "question" },
    ]


    print("Vocabulary:", words)
    print("Words count:", len(words))
    while True:
        print()

    
        # # # for i in range(len(training_data)):
        # # #     print(training_data[i]["text"])
        # # # word_id = words["morning"]

        answer = input("You: ")

        if answer == "exit":
            print("Exiting...")
            sys.exit(0)

        # # #   You:
        # # #
        # # #   You: hi
        # # #   Word IDs: [0]
        # # #   Vector: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # # # 
        # # #   You: good morning
        # # #   Word IDs: [2, 3]
        # # #   Vector: [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # # #
        # # #   You: how are you
        # # #   Word IDs: [8, 9, 6]
        # # #   Vector: [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0]
        # # #
        # # #
        # # #   for i in range(len(answer.split())):
        # # #       word_ids += [0]
        # # #
        # # #   for j in range(len(word_ids)):
        # # #       for i in range(len(words)):
        # # #           if answer.split()[j] == words[i]:
        # # #               word_ids[j] += words.index(words[i])+1

        
        answered_word_ids = []
        # print("len answer.split()", len(answer.split()))
        # print("len(word_ids)", len(word_ids))
        for j in range(len(answer.split())):
            for i in range(len(word_ids)):
        # # #         if()
                    answered_word_ids



        for i in range(len(answer.split())):
            answered_word_ids += [0]

               
            # word_ids[word_id] = word
        empty = [0] * len(word_ids)

        for j in range(len(answered_word_ids)):
            for word, word_id in words.items():
                # print(words[i])
                # print(answer.split()[j], "==", word)
                # if /* answer.split()[j] */ == words[i]:
                    # answered_word_ids[j] += word_id+1
                if answer.split()[j] == word:
                    # print("fuck id:",word_id)
                    # print('ну сука он же должен был прибавить тебя ебённый в рот не нахуй?_1:', word_id)
                    empty[word_id] += 1
                    # print("fuck:",empty)

        
        # print("answered_word_ids",answered_word_ids)
        empty_2 = [0] * len(answered_word_ids)

        for i in range(len(answered_word_ids)):
            answered_word_ids[i] = answered_word_ids.index(answered_word_ids[i])
            # print("--------------------------------------------",answered_word_ids[i], answered_word_ids.index(answered_word_ids[i]))

        # print("--------------------",answered_word_ids)

        # for j in range(len(answered_word_ids)):
        #     for word, word_id in words.items():
        #         # print(words[i])
        #         print(answer.split()[j], "==", word)
        #         # if /* answer.split()[j] */ == words[i]:
        #             # answered_word_ids[j] += word_id+1
        #         if answer.split()[j] == word:
        #             print("fuck id:",word_id)
        #             empty_2[word_id] += 1
        #             print("fuck:",empty_2)





        # print(answered_word_ids)

        empty_3 = [] 

        for i in range(len(answer.split())):
            empty_3 += [0]

        # print("empty_3",empty_3)

        



        for j in range(len(answered_word_ids)):
            for word, word_id in words.items():
                # print(words[i])
                # print(answer.split()[j], "==", word)
                # if /* answer.split()[j] */ == words[i]:
                    # answered_word_ids[j] += word_id+1
                if answer.split()[j] == word:
                    # print("fuck id:",word_id)
                    # print(j, word_id)
                    empty_3[j] += word_id
                    # if not word_id >= len(empty_3):
                    #     print("ALLO NAXUI GDE TI SUKA&&&&&",word_id)
                    #     empty_3[word_id] += word_id

        # for word, word_id in words.items():
        #     # print(word_id, ">=", len(empty_3))
        #     if not word_id >= len(empty_3):
        #         word_ids[word_id] = word
        #         # print(answer.split()[i], "==", word)
        #         # print('Слово:', word)
        #         print('ну сука он же должен был прибавить тебя ебённый в рот не нахуй?_2:', word_id-1)
        #         # print('---')
        #         empty_3[word_id] += word_id





                
        print("Word IDs:", empty_3)
        
        print("Vector:", empty)

        # # # for j in range(len(answered_word_ids)):
        # # #     for i in range(len(word_ids)):
        # # #         if answer.split()[j] == word_ids[i]:
        # # #             answered_word_ids[j] += word

        # for i in range(len(word_ids)):
        #     print(word_ids[i])

        
        for i in range(len(answer.split())):
            answer.split()[i]
        # for word, word_id in words.items():
        #     # for hi
        #     if answer.split()[i] == word:
        #         # empty[word_id] += 1
        #         print(answer.split()[i], "==", word)
                # print('Слово:', word)
                # print('Номер:', word_id)
                # print('---')

        # print(empty)
        # print(answered_word_ids)
        # # # print("Word IDs:", answered_word_ids)






        # words = [ "hi", "hello", "bye", "see you" ]
        # empty = []
        # matrix_xz = [0] * 14
        # training_data = [
        #     { "text": "hi", "label": "greeting" },
        #     { "text": "hello", "label": "greeting" },
        #     { "text": "good morning", "label": "greeting" },
            
        #     { "text": "bye", "label": "goodbye" },
        #     { "text": "see you", "label": "goodbye" },
        #     { "text": "goodbye", "label": "goodbye" },
            
        #     { "text": "how are you", "label": "question" },
        #     { "text": "what is this", "label": "question" },
        #     { "text": "are you ok", "label": "question" },
        # ]

        

        # for j in range(len(empty_3)):
        #     for i in range(len(words)):
        #         if answer.split()[j] == words[i]:
        #             empty_3[j] += words.index(words[i])+1

        

        # print(len(answer.split()))
        # for j in range(len(words)):
        #     for i in range(len(answer.split())):
        #         if answer.split()[i] == words[j]:
        #             matrix_xz[j] += 1
        #         # elif answer.split()[i] == words[1]:
        #         #     matrix_xz[1] += 1
        #         # elif answer.split()[i] == words[2]:
        #         #     matrix_xz[2] += 1
        
        # print("Vector:", matrix_xz)

        # for i in range(len(training_data)):
        #     print("Text:", training_data[i]["text"], "|", "Label:", training_data[i]["label"])

        # print()

if __name__ == '__main__':
    main()