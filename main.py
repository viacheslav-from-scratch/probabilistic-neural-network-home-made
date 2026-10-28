import sys
import time
import random

def rand_range(min, max):
    max = max / 100
    min = min / 100
    return min, max


def main():
    words = {'hi': 0, 'hello': 1, 'good': 2, 'morning': 3, 'bye': 4, 'see': 5, 'you': 6, 'goodbye': 7, 'how': 8, 'are': 9, 'what': 10, 'is': 11, 'this': 12, 'ok': 13, 'my': 14, 'friend': 15, 'later': 16, 'i': 17, 'am': 18, 'fine': 19, '[end]': 20}
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


    # print("Vocabulary:", words)
    # print("Words count:", len(words))
    # print("Training data:")
    
    # while True:
    #     for i in range(len(training_data)):
    #         print()

    #         answer = training_data[i]["text"]
    #         print("Text:", answer)
            
    #         answered_word_ids = []
    #         for j in range(len(answer.split())):
    #             for i in range(len(word_ids)):
    #                     answered_word_ids

    #         for i in range(len(answer.split())):
    #             answered_word_ids += [0]

    #         empty = [0] * len(word_ids)

    #         for j in range(len(answered_word_ids)):
    #             for word, word_id in words.items():
    #                 if answer.split()[j] == word:
    #                     empty[word_id] += 1

    #         empty_2 = [0] * len(answered_word_ids)

    #         for i in range(len(answered_word_ids)):
    #             answered_word_ids[i] = answered_word_ids.index(answered_word_ids[i])

    #         for i in range(len(training_data)):
    #             if answer == training_data[i]["text"]:
    #                 print("Label:",training_data[i]["label"])
            
    #         print("Vector:", empty)
            
    #         for i in range(len(answer.split())):
    #             answer.split()[i]

    while True:
        print()
        question = input("You: ")
        if question == "exit":
            print("Exiting...")
            sys.exit(0)
        
        # print(len(answer))

        ###empty_3 = []
        ###for i in range(len(answer.split())):
        ###    empty_3 += [0]
        ###for j in range(len(empty_3)):
        ###    for word, word_id in words.items():
        ###        if answer.split()[j] == word:
        ###            empty_3[j] += word_id
        ###        
        ###print("Word IDs:", empty_3)
        ###
        ###empty = []
        ###for i in range(len(word_ids)):
        ###    empty += [0]
        ###for j in range(len(answer.split()[j])-1):
        ###    for word, word_id in words.items():
        ###        if answer.split()[j] == word:
        ###            empty[word_id] += 1
        ###print("Vector:", empty)

        # start logic
        #
        # hi → hello my friend
        # bye → see you later
        # how are you → i am fine
        #
        # if hi
        # Input: hi | Generated: [empty] | Next: hello
        # Input: hi | Generated: hello | Next: my
        # Input: hi | Generated: hello my | Next: friend
        # Input: hi | Generated: hello my friend | Next: [end]
        #
        # if bye
        # Input: bye | Generated: [empty] | Next: see
        # Input: bye | Generated: see | Next: you
        # Input: bye | Generated: see you | Next: later
        # Input: bye | Generated: see you later friend | Next: [end]
        #
        # if how are you
        # Input: how are you | Generated: [empty] | Next: i
        # Input: how are you | Generated: i | Next: am
        # Input: how are you | Generated: i am are | Next: fine
        # Input: how are you | Generated: i am fine | Next: [end]
        # sys.stdout.flush()
        # if "hi" == question and 1.0 >= random.random() >= 0:
        #     answer = "[empty]"
        #     print(answer, end=" ")
        #     if "[empty]" == answer:
        #         answer = "hello"
        #         print(answer, end=" ")
        #         if "hello" == answer:
        #             answer = "my"
        #             print(answer, end=" ")
        #             if "my" == answer:
        #                 answer = "friend"
        #                 print(answer, end=" ")
        #                 if "friend" == answer:
        #                     answer = "[end]"
        #                     print(answer, end=" ")
        # if "bye" == question:
        #     answer = "[empty]"
        #     print(answer, end=" ")
        #     if "[empty]" == answer:
        #         answer = "see"
        #         print(answer, end=" ")
        #         if "see" == answer:
        #             answer = "you"
        #             print(answer, end=" ")
        #             if "you" == answer:
        #                 answer = "later"
        #                 print(answer, end=" ")
        #                 if "later" == answer:
        #                     answer = "[end]"
        #                     print(answer, end=" ")
        # if "how are you" == question:
        #     answer = "[empty]"
        #     print(answer, end=" ")
        #     if "[empty]" == answer:
        #         answer = "i"
        #         print(answer, end=" ")
        #         if "i" == answer:
        #             answer = "am"
        #             print(answer, end=" ")
        #             if "am" == answer:
        #                 answer = "fine"
        #                 print(answer, end=" ")
        #                 if "fine" == answer:
        #                     answer = "[end]"
        #                     print(answer, end=" ")
        
        

        marks = [
            # idx  input          generated   mark
            ( 0,  "hi",          "hello",    9999),
            ( 3,  "hello",       "my",       1000),
            ( 4,  "my",          "friend",   1000),
            ( 5,  "friend",      "[end]",    9999),

            ( 6,  "how are you", "i",        9999),
            ( 8,  "i",           "am",       1000),
            ( 9,  "am",          "fine",     1000),
            (10,  "fine",        "[end]",    9999),

            (11,  "bye",         "see",      9999),
            (13,  "see",         "you",      1000),
            (14,  "you",         "later",    1000),
            (15,  "later",       "[end]",    9999),
        ]

        mark = []
        input_ = []
        generated = []
        idx = []
        prepare_arr = []
        temp = 0
        for item in marks:
            prepare_arr.append(item)

        for item in prepare_arr:
            for i in range(len(item)):
                if i == 3:
                    mark.append(item[i])
                if i == 2:
                    generated.append(item[i])
                if i == 1:
                    input_.append(item[i])
                if i == 0:
                    idx.append(item[i])
                    # print(item[i])


        for j in range(len(mark)-1):
            for i in range(len(mark)-1):
                if mark[i] <= mark[i+1]:
                    temp = mark[i]
                    mark[i] = mark[i+1]
                    mark[i+1] = temp
                    temp = generated[i]
                    generated[i] = generated[i+1]
                    generated[i+1] = temp
                    temp = input_[i]
                    input_[i] = input_[i+1]
                    input_[i+1] = temp
                    temp = idx[i]
                    idx[i] = idx[i+1]
                    idx[i+1] = temp
        
        minimum_mark = mark[len(mark)-1]
        maximum_mark = mark[0]
        # print(minimum_mark)
        # print(maximum_mark)
        




        # for i in range(len(mark)):
        #     print(idx[i], input_[i], generated[i], mark[i])
        count = 0
        precision = 0

        answer = question
        for i in range(len(mark)):
            if answer == input_[i]:
                # print(idx[i], input_[i], generated[i], mark[i])
                count += 1
            if answer == input_[i] and not "[end]" in answer and maximum_mark >= minimum_mark and not "[end]" in answer:
                # print(generated[i], end=' ')
                answer = generated[i]

        # precision
        answer = question
        for i in range(len(mark)):
            if answer == input_[i]:
                precision += mark[i]
                print(idx[i], input_[i], generated[i], mark[i], precision)
            if answer == input_[i] and not "[end]" in answer and maximum_mark >= minimum_mark and not "[end]" in answer:
                # print(generated[i], end=' ')
                answer = generated[i]
        print(count, precision)

        # for i in range(len(mark)):
        #
        #     # if question == input_[i]:
        #         # random.randint(0, n)
        #         # print(idx[i], input_[i], generated[i], mark[i], precision)
        #         # print(idx[i], input_[i], generated[i], mark[i])
        #
        #     # for j in range(len(mark)-1):
        #     #     for i in range(len(mark)-1):
        #     #         if mark[i] <= mark[i+1]:
        #     #             temp = mark[i]
        #     #             mark[i] = mark[i+1]
        #     #             mark[i+1] = temp
        #
        #     # if question == input_[i]:
        #     #     print(idx[i], input_[i], generated[i], mark[i])
        #
        #     # for i in range(len(mark)):
        #     #     print(idx[i], input_[i], generated[i], mark[i])
        #
        #     # print(answer, "==", input_[i])
        #     if answer == input_[i]:
        #         print(generated[i], end=' ')
        #         answer = generated[i]

        answer = question
        for i in range(len(mark)):
            
            if question == input_[i]:
                print(random.randint(0, precision))
                print(idx[i], input_[i], generated[i], mark[i], precision)
                
            # for j in range(len(mark)-1):
            #     for i in range(len(mark)-1):
            #         if mark[i] <= mark[i+1]:
            #             temp = mark[i]
            #             mark[i] = mark[i+1]
            #             mark[i+1] = temp

            # if question == input_[i]:
            #     print(idx[i], input_[i], generated[i], mark[i])

            # for i in range(len(mark)):
            #     print(idx[i], input_[i], generated[i], mark[i])

            # print(answer, "==", input_[i])
            if answer == input_[i]:
                print(generated[i], end=' ')
                answer = generated[i]
            

        # for idx, input_, generated, mark in marks:
        #     if question == input_:
        #         print(generated, end=' ')
        #         question = generated
            

        # presition = random.random()
        # # print(presition)
        # if "hi" == question and 1.0 >= presition >= 0 or "hello" == question and 1.0 >= presition >= 0 or "hey" == question and 1.0 >= presition >= 0:
        #     answer = "[empty]"
        #     print(answer, end=" ")

        #     presition = random.random()
        #     # print(presition)
        #     if "[empty]" == answer and 1.0 >= presition >= 0.66:
        #         answer = "hi"
        #         print(answer, end=" ")
        #     if "[empty]" == answer and 0.66 >= presition >= 0.33:
        #         answer = "hello"
        #         print(answer, end=" ")
        #     if "[empty]" == answer and 0.33 >= presition >= 0:
        #         answer = "hey"
        #         print(answer, end=" ")



        #     presition = random.random()
        #     # print(presition)
        #     if "hi" == answer and 1.0 >= presition >= 0.5 or "hello" == answer and 1.0 >= presition >= 0.5 or "hey" == answer and 1.0 >= presition >= 0.5:
        #         answer = "how"
        #         print(answer, end=" ")
        #     if "hi" == answer and 0.5 >= presition >= 0 or "hello" == answer and 0.5 >= presition >= 0 or "hey" == answer and 0.5 >= presition >= 0:
        #         answer = "what"
        #         print(answer, end=" ")



        #     presition = random.random()
        #     # print(presition)
        #     if "how" == answer and 1.0 >= presition >= 0 or "what" == answer and 1.0 >= presition >= 0:
        #         answer = "can"
        #         print(answer, end=" ")



        #     presition = random.random()
        #     # print(presition)
        #     if "can" == answer and 1.0 >= presition >= 0:
        #         answer = "i"
        #         print(answer, end=" ")



        #     presition = random.random()
        #     # print(presition)
        #     if "i" == answer and 1.0 >= presition >= 0.5:
        #         answer = "help"
        #         print(answer, end=" ")
        #     if "i" == answer and 0.5 >= presition >= 0:
        #         answer = "assist"
        #         print(answer, end=" ")



        #     presition = random.random()
        #     # print(presition)
        #     if "help" == answer and 1.0 >= presition >= 0 or "assist" == answer and 1.0 >= presition >= 0:
        #         answer = "you"
        #         print(answer, end=" ")
            
            

        #     presition = random.random()
        #     # print(presition)
        #     if "you" == answer and 1.0 >= presition >= 0.5:
        #         answer = "today"
        #         print(answer, end=" ")
        #     if "you" == answer and 0.5 >= presition >= 0:
        #         answer = "?"
        #         print(answer, end=" ")



        #     presition = random.random()
        #     # print(presition)
        #     if "today" == answer and 1.0 >= presition >= 0:
        #         answer = "?"
        #         print(answer, end=" ")



        #     presition = random.random()
        #     # print(presition)
        #     if "?" == answer and 1.0 >= presition >= 0:
        #         answer = "[end]"
        #         print(answer, end=" ")
        
        # presition = random.random()
        # if "write me a python code for AI" == question and 1.0 >= presition >= 0 or "python code for AI" == question and 1.0 >= presition >= 0:
        #     answer = "[empty]"
        #     print(answer, end=" ")
        #     presition = random.random()
        #     # print(presition)
        #     if "[empty]" == answer and 1.0 >= presition >= 0:
        #         answer = "\n"
        #         print(answer, end=" ")
        #         if "\n" == answer and 1.0 >= presition >= 0:
        #             answer = "if"
        #             print(answer, end=" ")
        #             if "if" == answer and 1.0 >= presition >= 0:
        #                 answer = "\"anytext\""
        #                 print(answer, end=" ")
        #                 if "\"anytext\"" == answer and 1.0 >= presition >= 0:
        #                     answer = "=="
        #                     print(answer, end=" ")
        #                     if "==" == answer and 1.0 >= presition >= 0:
        #                         answer = "question"
        #                         print(answer, end=" ")
        #                         if "question" == answer and 1.0 >= presition >= 0:
        #                             answer = "and"
        #                             print(answer, end=" ")
        #                             if "and" == answer and 1.0 >= presition >= 0:
        #                                 answer = "1.0"
        #                                 print(answer, end=" ")
        #                                 if "1.0" == answer and 1.0 >= presition >= 0:
        #                                     answer = ">="
        #                                     print(answer, end=" ")
        #                                     if ">=" == answer and 1.0 >= presition >= 0:
        #                                         answer = "presition"
        #                                         print(answer, end=" ")
        #                                         if "presition" == answer and 1.0 >= presition >= 0:
        #                                             answer = ">="
        #                                             print(answer, end=" ")
        #                                             if ">=" == answer and 1.0 >= presition >= 0:
        #                                                 answer = "0"
        #                                                 print(answer, end=" ")
        #                                                 if "0" == answer and 1.0 >= presition >= 0:
        #                                                     answer = ":"
        #                                                     print(answer, end=" ")
        #                                                     if ":" == answer and 1.0 >= presition >= 0:
        #                                                         answer = "\n\t"
        #                                                         print(answer, end=" ")
        #                                                         if "\n\t" == answer and 1.0 >= presition >= 0:
        #                                                             answer = "answer"
        #                                                             print(answer, end=" ")
        #                                                             if "answer" == answer and 1.0 >= presition >= 0:
        #                                                                 answer = "="
        #                                                                 print(answer, end=" ")
        #                                                                 if "=" == answer and 1.0 >= presition >= 0:
        #                                                                     answer = "\"answer\""
        #                                                                     print(answer, end=" ")
        #                                                                     if "\"answer\"" == answer and 1.0 >= presition >= 0:
        #                                                                         answer = "\n\t"
        #                                                                         print(answer, end=" ")
        #                                                                         if "\n\t" == answer and 1.0 >= presition >= 0:
        #                                                                             answer = "print(answer,"
        #                                                                             print(answer, end=" ")
        #                                                                             if "print(answer," == answer and 1.0 >= presition >= 0:
        #                                                                                 answer = "end=\" \")"
        #                                                                                 print(answer, end=" ")
        #                                                                                 if "end=\" \")" == answer and 1.0 >= presition >= 0:
        #                                                                                     answer = "\n"
        #                                                                                     print(answer, end=" ")
        #                                                                                     if "\n" == answer and 1.0 >= presition >= 0 : 
        #                                                                                         answer = "[end]" 
        #                                                                                         print(answer, end=" ") 
        

                        
            
if __name__ == '__main__':
    main()