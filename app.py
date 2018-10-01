import redis
from flask import Flask

app = Flask(__name__)
conn = redis.Redis(host='localhost', port=6379)
RES_STR = "appB {} {} times\n"


@app.route('/view', methods=['GET'])
def redis_view():
    times = conn.get('carats')
    return RES_STR.format("view", int(times))

@app.route('/incr', methods=['GET'])
def redis_incr():
    times = conn.incr('carats')
    return RES_STR.format("incr", int(times))

@app.route('/init', methods=['GET'])
def redis_init():
    conn.set('carats', 0)
    times = conn.get('carats')
    return RES_STR.format("init", int(times))

@app.route('/')
def hello():
    word = "Hello World"
    return word

if __name__ == "__main__":
    app.run()
