import sys
import time

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


    print("Vocabulary:", words)
    print("Words count:", len(words))
    print("Training data:")
    while True:
        for i in range(len(training_data)):
            print()

            answer = training_data[i]["text"]
            print("Text:", answer)
            
            answered_word_ids = []
            for j in range(len(answer.split())):
                for i in range(len(word_ids)):
                        answered_word_ids

            for i in range(len(answer.split())):
                answered_word_ids += [0]

            empty = [0] * len(word_ids)

            for j in range(len(answered_word_ids)):
                for word, word_id in words.items():
                    if answer.split()[j] == word:
                        empty[word_id] += 1

            empty_2 = [0] * len(answered_word_ids)

            for i in range(len(answered_word_ids)):
                answered_word_ids[i] = answered_word_ids.index(answered_word_ids[i])

            for i in range(len(training_data)):
                if answer == training_data[i]["text"]:
                    print("Label:",training_data[i]["label"])
            
            print("Vector:", empty)
            
            for i in range(len(answer.split())):
                answer.split()[i]

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

            if "hi" == question:
                answer = "[empty]"
                print(answer, end=" ")
                sys.stdout.flush()
                time.sleep(0.5)
                if "[empty]" == answer:
                    answer = "hello"
                    print(answer, end=" ")
                    sys.stdout.flush()
                    time.sleep(0.5)
                    if "hello" == answer:
                        answer = "my"
                        print(answer, end=" ")
                        sys.stdout.flush()
                        time.sleep(0.5)
                        if "my" == answer:
                            answer = "friend"
                            print(answer, end=" ")
                            sys.stdout.flush()
                            time.sleep(0.5)
                            if "friend" == answer:
                                answer = "[end]"
                                print(answer, end=" ")
                                sys.stdout.flush()
                                time.sleep(0.5)
            elif "bye" == question:
                answer = "[empty]"
                print(answer, end=" ")
                sys.stdout.flush()
                time.sleep(0.5)
                if "[empty]" == answer:
                    answer = "see"
                    print(answer, end=" ")
                    sys.stdout.flush()
                    time.sleep(0.5)
                    if "see" == answer:
                        answer = "you"
                        print(answer, end=" ")
                        sys.stdout.flush()
                        time.sleep(0.5)
                        if "you" == answer:
                            answer = "later"
                            print(answer, end=" ")
                            sys.stdout.flush()
                            time.sleep(0.5)
                            if "later" == answer:
                                answer = "[end]"
                                print(answer, end=" ")
                                sys.stdout.flush()
                                time.sleep(0.5)
            elif "how are you" == question:
                answer = "[empty]"
                print(answer, end=" ")
                sys.stdout.flush()
                time.sleep(0.5)
                if "[empty]" == answer:
                    answer = "i"
                    print(answer, end=" ")
                    sys.stdout.flush()
                    time.sleep(0.5)
                    if "i" == answer:
                        answer = "am"
                        print(answer, end=" ")
                        sys.stdout.flush()
                        time.sleep(0.5)
                        if "am" == answer:
                            answer = "fine"
                            print(answer, end=" ")
                            sys.stdout.flush()
                            time.sleep(0.5)
                            if "fine" == answer:
                                answer = "[end]"
                                print(answer, end=" ")
                                sys.stdout.flush()
                                time.sleep(0.5)


if __name__ == '__main__':
    main()