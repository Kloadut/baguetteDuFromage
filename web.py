#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pickle
import uuid
import baguettedufromage
import bottle

MAX_SCORE_REQUIRED = 60

def display_meal( \
        score_required=baguettedufromage.SCORE_REQUIRED, \
        score=1, ingredients=None, uid=None, answer=None):

    if score > score_required * 2:
        name = 'Gérard'
        image = '03.jpg'
    elif score > score_required * 1.3:
        name = 'Michel'
        image = '02.jpg'
    else:
        name = 'Patou'
        image = '01.jpg'

    return bottle.template('index.tpl', ingredients=ingredients, name=name, image=image, uid=uid, score=score, answer=answer)


def store_meal(ingredients, score, uid, answer=None):
    try:
        history = pickle.load(open('history.pkl'))
    except IOError:
        history = []

    history.append((ingredients, answer, score, uid))
    try:
        pickle.dump(history, open('history.pkl', 'wb'))
    except: pass


@bottle.route('/assets/:filename#.*#')
def send_static(filename):
        return bottle.static_file(filename, root='./assets/')


@bottle.route('/')
def index():
    uid = str(uuid.uuid4()).replace('-', '')[0:8]

    args = bottle.request.query.decode()
    if 'score' in args:
        bottle.redirect('/meal/%s?score=%s' % (uid, args['score']))
    else:
        bottle.redirect('/meal/%s' % uid)


@bottle.route('/meal/<uid:re:[a-z0-9]+>')
def get_meal(uid):
    ingredients = None

    if len(uid) > 8 :
        uid = str(uuid.uuid4()).replace('-', '')[0:8]
        bottle.redirect('/meal/%s' % uid)

    try:
        history = pickle.load(open('history.pkl'))
    except IOError:
        history = []

    for meal in history:
        try:
            if uid == meal[3]:
                ingredients = meal[0]
                score = meal[2]
        except IndexError:
            pass

    args = bottle.request.query.decode()
    if 'answer' in args and args['answer'] in ['yes', 'no', 'almost']:
        answer = args['answer']
    else:
        answer = None

    score_required = baguettedufromage.SCORE_REQUIRED

    if 'score' in args:
        try:
            if int(args['score']) <= MAX_SCORE_REQUIRED:
                score_required = int(args['score'])
        except TypeError: pass
        
        try:
            score_required = int(args['score'])
        except TypeError:
            score_required = 0
    else:
        score_required = baguettedufromage.SCORE_REQUIRED
      
    if ingredients is None:
        score = 0
        while score < score_required:
            ingredients = baguettedufromage.choose_ingredients()
            score = baguettedufromage.calculate_score(ingredients)

        store_meal(ingredients, score, uid)

    elif answer is not None:
        store_meal(ingredients, score, uid, answer)

    return display_meal(score_required, score, ingredients, uid, answer)


bottle.run(host='localhost', port=8767)
