import sys
import numpy as np

def main():
    while True:
        words = [ "hi", "hello", "bye", "see you" ]
        empty = []
        matrix_xz = [0, 0, 0]
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

        answer = input("You: ")

        if answer == "exit":
            print("Exiting...")
            sys.exit(0)

        for i in range(len(answer.split())):
            empty += [0]

        for j in range(len(empty)):
            for i in range(len(words)):
                if answer.split()[j] == words[i]:
                    empty[j] += words.index(words[i])+1

        print("Word IDs:", empty)

        for i in range(len(answer.split())):
            if answer.split()[i] == words[0]:
                matrix_xz[0] += 1
            elif answer.split()[i] == words[1]:
                matrix_xz[1] += 1
            elif answer.split()[i] == words[2]:
                matrix_xz[2] += 1
        
        print("Vector:", matrix_xz)

        for i in range(len(training_data)):
            print("Text:", training_data[i]["text"], "|", "Label:", training_data[i]["label"])

        print()

if __name__ == '__main__':
    main()