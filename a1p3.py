#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 <<Insert your name here>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 1 Student Solution
January 2026
Author: Louis Lam
"""


from sys import flags
from a1p1 import encrypt, decrypt

LETTERS = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'


def crack_caesar(ciphertext, val_words):
    best_plain = None
    best_key = None
    best_score = -1

    for key in LETTERS:
        plain = decrypt(ciphertext, key)

        score = 0
        for token in plain.split():
            word = []
            for ch in token:
                if 'A' <= ch <= 'Z':
                    word.append(ch)
            w = ''.join(word)
            if w and w in val_words:
                score += 1

        if score > best_score:
            best_score = score
            best_plain = plain
            best_key = key
        elif score == best_score:
            if best_plain is None or plain < best_plain:
                best_plain = plain
                best_key = key

    return best_plain, best_key


def form_dictionary(text_address='carroll-alice.txt'):
    with open(text_address, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    cleaned = []
    for ch in text.upper():
        if 'A' <= ch <= 'Z':
            cleaned.append(ch)
        else:
            cleaned.append(' ')

    return set(''.join(cleaned).split())



def test():
    assert crack_caesar('TBHZLIB QL TLKABOHXKA', form_dictionary()) == ('WELCOME TO WONDERLAND', 'X')


if __name__ == "__main__" and not flags.interactive:
    test()