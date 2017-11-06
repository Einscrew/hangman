#!/usr/bin/env python3

import getpass


def get_key():
    key = getpass.getpass("Enter solution")
    lst = []
    cur = []
    for c in key:
        lst.append(c)
        cur.append(" ")
    return [lst, cur]


def print_forca(cur, life):

    word = ""
    for i in cur:
        word += str(i)

    string = "_"*4+"\n|  " \
             + life[0] + "\n| " + life[1] + life[2] + life[3]\
             + "\t\t"+word+"\n| " + life[4] + " " + life[5] + "\n" + 6*"-"

    print(string)


def main():
    [key, cur] = get_key()
    death = -1
    man = ["o", "/", "|", "\\", "/", "\\"]
    life = [" ", " ", " ", " ", " ", " "]
    while cur != key:
        c = input("Enter your guess.\n")
        correct = 0
        for i in range(len(key)):
            if key[i] == c:
                correct = 1
                cur[i] = key[i]
        if correct == 0:
            death += 1
            if death >= len(man):
                print("YOU LOST")
                break
            life[death] = man[death]

        print_forca(cur, life)


if __name__ == "__main__":
    main()
