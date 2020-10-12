
### value of __name__

* if the script run directly
```
app = Flask('__main__')
```

* if the script being imported as module
```
app = Flask(__name__)
```

### Routing
create endpoints to handle the various requests. Requests from different URLs can be directed to different endpoints in a process called routing.

> route()

To build a route, we need to first define a function, known as a view function, that contains the code for processing the request and generating a response

use the route() decorator to bind a URL to the view function such that the function will be triggered when the URL is visited

route() decorator takes the URL path as parameter, or the part of the URL that follows the domain name

```
@app.route('/')
def home():
    return 'Hello, World!'
```

Multiple URLs can also be bound to the same view function

```
@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'
```

render html

```
@app.route('/)
def home():
    return '<h1>Hello, World!</h1>
```
```
@app.route('/)
def home():
    return '''
    <h1>Hello, World!</h1>
    <p>My first paragraph,</p>
    <a href="/">Back to Home</a>
    '''
```
```
@app.route('/convert/celsius_to_kelvin/<float:celsius>')
def celsius_to_kelvin(celsius):
    return f'{celsius + 273.15}K'
```

use variable rules to allow for dynamic URLs.

```
@app.route('/orders/<user_name>/<int:order_id>')
def orders(user_name, order_id):
    return f'<p>Fetching order #{order_id} for {user_name}.</p>'
```

Note that we can also optionally enforce the type of the variable being accepted using the syntax: **<converter:variable_name>**

|string accepts any text without a slash (default)|
|int|accepts positive integers|
|float|accepts positive floating point values|
|path|like string but also accepts slashers|
|uuid|accepts UUID strings|

