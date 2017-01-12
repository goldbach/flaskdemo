import flask
import socket

application = flask.Flask(__name__)

@application.route('/')
def index():
  return "Hello HFLY  - served from %s!" % socket.gethostname()
  
if __name__ == "__main__":
    application.run()
    
