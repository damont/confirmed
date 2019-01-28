#!/usr/bin/python3
from flask import Flask
from confirmed import *
import random

app=Flask(__name__)
random.seed()

@app.route('/')
def home():
    return structure_json_formatted_output(get_article_list(get_headlines()))

@app.route('/stories/<int:story_id>')
def retrieve_stories(story_id):
    return get_stories(story_id)

@app.route('/urlcheck/<string:url>')
def check_url(url):
    if random.randint(1, 10) > 5:
        return url + ' confirmed'
    else:
        return url + ' condemned'

if __name__ == "__main__":
    app.run()

