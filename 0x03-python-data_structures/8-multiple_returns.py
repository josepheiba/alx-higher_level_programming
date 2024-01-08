#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght == 0:
        return (lenght, None)
    return (lenght, sentence[0])
