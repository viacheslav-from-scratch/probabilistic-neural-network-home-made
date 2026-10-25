import sys
import numpy as np

def main():
    while True:
            
        words = {'hi': 0, 'hello': 1, 'good': 2, 'morning': 3, 'bye': 4, 'see': 5, 'you': 6, 'goodbye': 7, 'how': 8, 'are': 9, 'what': 10, 'is': 11, 'this': 12, 'ok': 13}
        word_ids = {}

        # items() выдаёт пары: ключ и значение.
        for word, word_id in words.items():
            # Новый словарь: номер становится ключом,
            # а слово — значением.
            word_ids[word_id] = word

        # # # for i in range(len(word_ids)):
        # # #     print(word_ids[i])

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



        # # #   Vocabulary: {'hi': 0, 'hello': 1, 'good': 2, 'morning': 3, 'bye': 4, 'see': 5, 'you': 6, 'goodbye': 7, 'how': 8, 'are': 9, 'what': 10, 'is': 11, 'this': 12, 'ok': 13}
        # # #   Words count: 14


        # for i in range(len(words)):
        print("Vocabulary:", words)
        print("Words count:", len(words))
        print()


        # # for i in range(len(training_data)):
        # #     print(training_data[i]["text"])
            
        # word_id = words["morning"]

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
        # # for j in range(len(answer.split())):
        # #     for i in range(len(word_ids)):
        #         if()
        #             answered_word_ids

        for i in range(len(answer.split())):
            answered_word_ids += [0]

        # for j in range(len(answered_word_ids)):
        #     for i in range(len(word_ids)):
        #         if answer.split()[j] == word_ids[i]:
        #             answered_word_ids[j] += word

        for i in range(len(word_ids)):
            print(word_ids[i])

        i = 0
        for i in range(len(answer.split())):
            print(answer.split()[i])

        for word, word_id in words.items():
            print(answer.split()[i])
            print('Слово:', word)
            print('Номер:', word_id)
            print('---')
            i+=1

        # print(answered_word_ids)
        print("Word IDs:", answered_word_ids)






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

        

        # for i in range(len(answer.split())):
        #     empty += [0]

        # for j in range(len(empty)):
        #     for i in range(len(words)):
        #         if answer.split()[j] == words[i]:
        #             empty[j] += words.index(words[i])+1

        # print("Word IDs:", empty)

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