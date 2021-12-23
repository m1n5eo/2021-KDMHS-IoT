from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p>
        <a href="/first">Go First</a>
        <a href="/second">Go Second</a>
    '''

@app.route("/first")
def first():
    return '''
        <p>First Page</p>
        <a href="/">Go Home</a>
    '''

@app.route("/second")
def second():
    return '''
        <p>Second Page</p>
        <a href="/">Go Home</a>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0")