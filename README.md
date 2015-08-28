# Baguette Du Fromage

Patou, Michel and Gérard enlight your meal with their proposals!

![screenshot](https://raw.githubusercontent.com/Kloadut/baguetteDuFromage/master/screenshot.png)

## Usage

Either:
* Run `baguettedufromage.py` as a python2 script
* Or install python-bottle, launch `web.py` and go to http://localhost:8767/

## How does it work ?

BaguetteDuFromage is a learning bot that records the choices you validate (or not) when you run `baguettedufromage.py`. This way, it calculates a score based on its recorded matching of ingredients.

![screenshot2](https://raw.githubusercontent.com/Kloadut/baguetteDuFromage/master/screenshot2.png)

So the more you 'feed' the bot, the better the meal proposals will actually be. :+1:

**Note:** The ingredients are stored in `ingredients.pkl` as a python pickle, along with a weight (in order to avoid bad ingredient mix in the first place).
