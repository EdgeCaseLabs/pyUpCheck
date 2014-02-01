### Settings

DEBUG = True
SENTRY_DSN = None
COMMANDS_FILE = 'commands.txt'


### Imports and Setup
from flask import Flask
from raven import Client
from fabric.api import env, local
import os

class AbortException(Exception):
    pass

app = Flask(__name__)
app.debug = DEBUG
env.abort_exception = AbortException
if SENTRY_DSN:
    client = Client(SENTRY_DSN)
else:
    client = None

### Routes
@app.context_processor
def inject_context():
    return dict(debug=app.debug)

@app.route("/")
def index():

    # Test settings
    if not client:
        return "Your SENTRY_DSN doesn't appear to be set properly.", 500

    try:
        COMMANDS = os.path.join(os.path.abspath(os.path.dirname(__file__)), COMMANDS_FILE)
        f = open(COMMANDS)
    except:
        client.captureException()
        return "Unable to locate your commands file: %s" % COMMANDS, 500
    else:

        for cmd in f.readlines():

            try:
                local('ps -ef | grep "%s" | grep -v grep' % cmd.strip('\n'), capture=True)
            except:
                # record a simple message
                #client.captureMessage('hello world!')
                client.captureException()
                return "ERROR: Bummer. Nothing good.", 500

        return "OK: Everything's peachy!"



if __name__ == "__main__":
    app.run()