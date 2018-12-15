#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import error, route, run, default_app, debug, static_file
import indexHTML

def htmlify(title, text):
    page = """
        some html shit
        
        """
    return page


@route('/')  # Code on the left equals to => route('/', 'GET', index)
def index():
    return indexHTML.get_index()


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
    return "OOPS"
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
