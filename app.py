from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", port=6379)

app = Flask(__name__)


@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<html>" \
           "<head>" \
           "<link rel='icon' type='image/png' href='https://raw.githubusercontent.com/QazyBi/f20/master/favicon-32x32.png'>"\
           "</head>" \
           "<body>" \
           "<img src='https://sun3-10.userapi.com/4-GMANnfOvb3k7HODqwOILCwZi_9xlDPZ60i8w/TfDIEcPqpbc.jpg' style='width:300px; height:400px;'>"\
           "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"\
           "</body>"\
           "</html>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
