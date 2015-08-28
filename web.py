#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pickle
import random
import baguettedufromage
from bottle import route, run, template, static_file

@route('/')
@route('/<score_required:int>')
def index(score_required=baguettedufromage.SCORE_REQUIRED):
    score = 0
    score_required = int(score_required)

    while score < score_required:
        ingredients = baguettedufromage.choose_ingredients()
        score = baguettedufromage.calculate_score(ingredients)

    if score > score_required*1.3:
        name = 'Gérard'
        image = '03.jpg'
    elif score > score_required*1.1:
        name = 'Michel'
        image = '02.jpg'
    else:
        name = 'Patou'
        image = '01.jpg'

    return template('index.tpl', ingredients=ingredients, name=name, image=image)

@route('/assets/:filename#.*#')
def send_static(filename):
        return static_file(filename, root='./assets/')

run(host='localhost', port=8767)


