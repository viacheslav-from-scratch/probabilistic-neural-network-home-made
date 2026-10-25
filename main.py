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
        answer = input("You: ")

        if answer == "exit":
            print("Exiting...")
            sys.exit(0)
        
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

        empty_3 = [] 

        for i in range(len(answer.split())):
            empty_3 += [0]

        for j in range(len(answered_word_ids)):
            for word, word_id in words.items():
                if answer.split()[j] == word:
                    empty_3[j] += word_id
                
        print("Word IDs:", empty_3)
        
        print("Vector:", empty)
        
        for i in range(len(answer.split())):
            answer.split()[i]

if __name__ == '__main__':
    main()