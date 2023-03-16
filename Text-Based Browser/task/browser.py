from collections import deque
import os
import requests
import sys


def save_file(path, name, content):
    with open(os.path.join(path, name.split('.')[0]), 'wt', encoding='utf-8') as f:
        f.write(content)


def read_file(path, name):
    with open(os.path.join(path, name), 'rt', encoding='utf-8') as f:
        print(f.read())


def main():
    stack = deque()
    temp = None
    directory = sys.argv[1]
    if not os.access(directory, os.F_OK):
        os.mkdir(directory)
    while True:
        option = input()
        if option == 'exit':
            break
        elif option == 'back':
            if stack:
                print(stack.pop())
        elif option in os.listdir(directory):
            read_file(directory, option)
        elif '.' in option:
            r = requests.get(option if option.startswith('https://') else 'https://' + option)
            print(r.text)
            if temp:
                stack.append(temp)
            temp = r.text
            save_file(directory, option, r.text)
        else:
            print('Error: Invalid URL')


if __name__ == '__main__':
    main()
