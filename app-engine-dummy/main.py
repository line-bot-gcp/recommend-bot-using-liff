# https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/appengine/standard_python3/hello_world/main.py
# [START gae_python37_app]

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
