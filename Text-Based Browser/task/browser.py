from bs4 import BeautifulSoup
from collections import deque
from colorama import Fore
import os
import re
import requests
import sys


class Browser:
    def __init__(self):
        self.stack = deque()
        self.previous = None
        self.directory = sys.argv[1]
        if not os.access(self.directory, os.F_OK):
            os.mkdir(self.directory)

    def save_file(self, name, content):
        with open(os.path.join(self.directory, name.split('.')[0]), 'wt', encoding='utf-8') as f:
            f.write(content)

    def read_file(self, name):
        with open(os.path.join(self.directory, name), 'rt', encoding='utf-8') as f:
            print(f.read())

    def get_webpage(self, url):
        try:
            r = requests.get(url if url.startswith('https://') else 'https://' + url)
        except requests.exceptions.ConnectionError:
            print('Error: Invalid URL')
        else:
            soup = BeautifulSoup(r.content, 'html.parser')
            content = '\n'.join([Fore.BLUE + x.text.strip() + Fore.RESET if x.has_attr('href') else x.text.strip() for x in
                                 soup.find_all(['p', 'a', re.compile(r'^h\d')])])
            print(content)
            if self.previous:
                self.stack.append(self.previous)
            self.previous = content
            self.save_file(url, content)

    def menu(self):
        while True:
            option = input()
            if option == 'exit':
                break
            elif option == 'back':
                if self.stack:
                    print(self.stack.pop())
            elif option in os.listdir(self.directory):
                self.read_file(option)
            else:
                self.get_webpage(option)


def main():
    browser = Browser()
    browser.menu()


if __name__ == '__main__':
    main()
