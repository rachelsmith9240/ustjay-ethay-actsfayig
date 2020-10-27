import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def get_pig_latinized(facts):
    response = requests.post(url="https://hidden-journey-62459.herokuapp.com/piglatinize/",
                             data={'input_text': facts})

    result = str(response.url) + '<br/>' + '-'*200 + '<br/>' + str(response.text)
    
    return result

@app.route('/')
def home():
    return get_pig_latinized(get_fact())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

