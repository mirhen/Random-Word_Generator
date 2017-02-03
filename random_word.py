from flask import Flask, render_template
from flask import request, redirect
import random
app = Flask(__name__)
word = 'yo'
@app.route('/')

# def random_word():
        # with open('/usr/share/dict/words') as textfile:
        #     content = textfile.readlines()
        # # you may also want to remove whitespace characters like `\n` at the end of each line
        # content = [x.strip() for x in content]
        #
        # rand_index = random.randint(0, len(content) - 1)
        # return content[rand_index]

def hello_world():
    author = "Me"
    name = "You"

    return render_template('index.html',word=word)

@app.route('/', methods = ['POST'])
def signup():
    with open('/usr/share/dict/words') as textfile:
        content = textfile.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]

        rand_index = random.randint(0, len(content) - 1)
    word = content[rand_index]
    print 'signup button pressed'

    return render_template('index.html',word=word)

if __name__ == "__main__":
    app.run()
