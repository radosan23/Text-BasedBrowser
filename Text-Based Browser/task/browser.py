from collections import deque
import os
import sys

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created "soft" magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

pages = {'bloomberg.com': bloomberg_com, 'nytimes.com': nytimes_com}


def save_file(path, name):
    with open(os.path.join(path, name.split('.')[0]), 'wt') as f:
        f.write(pages[name])


def read_file(path, name):
    with open(os.path.join(path, name), 'rt') as f:
        print(f.read())


def main():
    stack = deque()
    directory = sys.argv[1]
    if not os.access(directory, os.F_OK):
        os.mkdir(directory)
    while True:
        option = input()
        if option == 'exit':
            break
        elif option == 'back':
            if stack:
                stack.pop()
                print(stack.pop())
        elif option in os.listdir(directory):
            read_file(directory, option)
        elif option in pages:
            print(pages[option])
            stack.append(pages[option])
            save_file(directory, option)
        else:
            print('Error: Invalid URL')


if __name__ == '__main__':
    main()
