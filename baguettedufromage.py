#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pickle
import random

INTRO = "Votre plat est :"
QUERY = "Cela vous convient-il ? (yes/almost/no) : "
WRONG = "Mauvaise réponse, choisissez 'yes', 'almost' ou 'no' : "

NUMBER_OF_INGREDIENTS = 5
MIN_WEIGHT = 16
MAX_WEIGHT = 20
SCORE_REQUIRED = 30

NO_MINUS_SCORE = 1
ALMOST_SCORE = 1
YES_SCORE = 3

def choose_ingredients():
    ingredients = pickle.load(open('ingredients.pkl'))
    weight = 0
    
    while weight <= MIN_WEIGHT or weight >= MAX_WEIGHT:
        chosen_ingredients = random.sample(ingredients, NUMBER_OF_INGREDIENTS)
        weight = sum([i[1] for i in chosen_ingredients])
    
    def getWeight(ingredient):
        return ingredient[1]
    chosen_ingredients.sort(key=getWeight, reverse=True)

    return [i[0] for i in chosen_ingredients]


def calculate_score(ingredients):
    score = 0

    try:
        history = pickle.load(open('history.pkl'))
    except IOError:
        return score

    matched_ingredients = []
    
    for ingredient_1 in ingredients:
        for ingredient_2 in ingredients:
            if ingredient_1 != ingredient_2 \
            and (ingredient_2, ingredient_1) not in matched_ingredients:
                matched_ingredients.append((ingredient_1, ingredient_2))

                for previous_match in history:
                    if  ingredient_1 in previous_match[0] \
                    and ingredient_2 in previous_match[0]:
                        if previous_match[1] == 'no':
                            score-=NO_MINUS_SCORE
                        elif previous_match[1] == 'almost':
                            score+=ALMOST_SCORE
                        elif previous_match[1] == 'yes':
                            score+=YES_SCORE

    return score


def store_match(match_tuple):
    try:
        history = pickle.load(open('history.pkl'))
    except IOError:
        history = []

    history.append(match_tuple)
    pickle.dump(history, open('history.pkl', 'wb'))


def main():
    score = 0

    while score < SCORE_REQUIRED:
        ingredients = choose_ingredients()
        score = calculate_score(ingredients)

    print
    print INTRO
    print ', '.join(ingredients) + ' (score '+ str(score) +')'

    try:
        answer = raw_input(QUERY)

        while answer not in ['no', 'almost', 'yes']:
            answer = raw_input(WRONG)
    except KeyboardInterrupt:
        return

    store_match((ingredients, answer))
    main()


if __name__ == "__main__":
    main()
