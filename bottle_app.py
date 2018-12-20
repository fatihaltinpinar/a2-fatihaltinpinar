#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import error, route, run, default_app, debug, static_file
from bottle import post, request, redirect


import hash_password # This code has taken from link below.
# https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py


def htmlify(title, text):
    page = """
        some html shit
        
        """
    return page

### TESTING FORM STUFF


comments = []


def login():
    page ='''
    
   <form action="/submit" method="post">
            Username: <input id="usernameBox" name="username" type="text"/> 
            
            <input name="anonymous" id="anonymousBox" type="checkbox" 
            value="Yes"> I want to be anonymous </br>
            
            Comment: <input name="comment" type="text" />   </br>
            Password: <input name="password" type="password" /> </br>
            <input value="Login" type="submit" />
    </form>
    <ul>
    <script>
        var anonymousBox = document.getElementById("anonymousBox");
        var usernameBox = document.getElementById("usernameBox");
        
        anonymousBox.addEventListener( 'change', function() {
            
            if (anonymousBox.checked == true){
                usernameBox.disabled = true;
            }else {
                usernameBox.disabled = false;
            }     
        
        });
               
        
    </script>
    '''
    for comment in comments:
        page = page + '<li>' + comment + '</li>'
    page = page + '</ul>'
    return page


@route('/submit', method="POST")
def do_login():
    form = request.forms.getall()
    print(form)
    comment = str(request.forms.get('comment'))
    password = request.forms.get('password')
    if hash_password.create_hash(password) == 'b493d48364afe44d11c0165cf470a4164d1e2609911ef998be868d46ade3de4e':
        comments.insert(0, comment)
        redirect("/")
    else:
        redirect("/")


### TESTING FORM STUFF
@route('/')  # Code on the left equals to => route('/', 'GET', index)
def index():
    return login()
    # return static_file('index.html', root='./static')


@route('/<page_name>')
def return_page(page_name):
    return static_file(page_name, root='./static')


@route('/css/<filepath>')
def css_static(filepath):
    return static_file(filepath, root='./static/css')


@route('/img/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/img')


@route('/favicon.ico')
def server_static():
    return static_file('favicon.ico', root='.static/')


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
