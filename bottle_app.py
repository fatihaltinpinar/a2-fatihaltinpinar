#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import error, route, run, default_app, debug, static_file
import indexHTML
from bottle import post, request
import hash_password

def htmlify(title, text):
    page = """
        some html shit
        
        """
    return page

### TESTING FORM STUFF
comments = []

def login():
    page =  '''
   <form action="/login" method="post">
            Comment: <input name="comment" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
    </form>
    <ul>
    '''
    for comment in comments:
        page = page + '<li>' + comment + '</li>'
    page = page + '</ul>'
    return page


@route('/login', method="POST")
def do_login():
    comment = str(request.forms.get('comment'))
    password = request.forms.get('password')
    if hash_password.create_hash(password) == 'b493d48364afe44d11c0sadaa4164d1e2609911ef998be868d46ade3de4e':
        comments.insert(0, comment)
        return login()
    else:
        return login()

### TESTING FORM STUFF
@route('/')  # Code on the left equals to => route('/', 'GET', index)
def index():
    return login()
    # return indexHTML.get_index()


@route('/<page_name>')
def return_page(page_name):
    return static_file(page_name, root='./oldHTMLfiles/')


@route('/css/<filepath>')
def css_static(filepath):
    return static_file(filepath, root='./css')


@route('/img/<filename>')
def server_static(filename):
    return static_file(filename, root='./img')


@route('/favicon.ico')
def server_static():
    return static_file('favicon.ico', root='.')


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
