from random import randrange
d = {}
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    split_words = words.split(' ')
    for i in range(len(split_words)-1):
        if split_words[i] in d:
            d[split_words[i]].append(split_words[i+1])
        else:
            d[split_words[i]] = [split_words[i+1]]


# TODO: construct 5 random sentences
# Your code here
def construct_random(s):
    new = s.split(' ')
    for i in range(len(new)):
        if new[i] in d:
            new[i] = d[new[i]][randrange(len(d[new[i]]))]
    new_str = ' '.join(new[:-1]).replace('\n', ' ')
    print(new_str)


construct_random('What, you were thirsty, were you?')
construct_random(
    'Now for number three: you unwound every bit of the worsted while I wasn\'t looking!')
construct_random(
    'That\'s three faults, Kitty, and you\'ve not been punished for any of them yet.')
construct_random(
    'Kitty, can you play chess?')
construct_random('And I do so wish it was true!')
