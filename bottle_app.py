#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import error, route, run, default_app, debug, static_file
from bottle import request, redirect
from songs import songs
from datetime import datetime

import hash_password # This code has taken from link below.
# https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py

comments = []


@route('/submit', method="POST")
def submit():
    password = request.forms.get('password')

    if hash_password.create_hash(password) == 'b493d48364afe44d11c0165cf470a4164d1e2609911ef998be868d46ade3de4e':

        # comment_text = request.forms.get('commentText')  returns byte string
        # Use this code instead of one above since it returns utf-8
        # encoded string rather that byte string like the code above does
        comment_text = request.forms.commentText # return utf-8 encoded string

        print('comment text = ' , comment_text)

        if comment_text != '':

            comment = {'commentText': comment_text, 'time': datetime.now()}

            if request.forms.anonymous == 'yes' or request.forms.username == '':
                comment['username'] = 'Anonymous'
            else:
                comment['username'] = request.forms.username
                # this code returns byte string so it is disabled
                # comment['username'] = request.forms.get('username')
            comments.insert(0, comment)
            print(request.forms.commentText677)
    redirect('/songs.html')


### TESTING FORM STUFF
@route('/')  # Code on the left equals to => route('/', 'GET', index)
def index():
    return static_file('index.html', root='./static')


@route('/<page_name>')
def return_page(page_name):
    if page_name == 'songs.html':
        return songs(comments)
    else:
        return static_file(page_name, root='./static')


@route('/css/<filepath>')
def css_static(filepath):
    return static_file(filepath, root='./static/css')


@route('/img/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/img')


@route('/favicon.ico')
def server_static():
    return static_file('favicon.ico', root='./static/')


@error(404)
def error404(error):
    return "OOPS" + str(error)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
    run()
