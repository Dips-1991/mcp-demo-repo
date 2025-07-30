import flask 

def main():
    app = flask.Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello from pythonprograms!"

    app.run()

if __name__ == "__main__":
    main()
