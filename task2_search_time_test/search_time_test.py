import random
import time
from linkedbst import LinkedBST


def main():
    with open('words.txt', ) as words:
        words = words.readlines()
    to_find = []
    while len(to_find) < 10000:
        word = random.choice(words)
        if word not in to_find:
            to_find.append(word)

    search_list_test(words, to_find)

    random.shuffle(words)
    tree = LinkedBST()
    for word in words:
        tree.add(word)
    search_tree_test(tree, to_find)

    tree.rebalance()
    search_tree_test(tree, to_find)


def search_list_test(words, to_find):
    start = time.time()
    for word in to_find:
        ind = words.index(word)
    end = time.time()
    print(end - start)


def search_tree_test(tree, to_find):
    start = time.time()
    for word in to_find:
        ind = tree.find(word)
    end = time.time()
    print(end - start)


main()
