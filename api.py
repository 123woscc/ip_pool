from flask import Flask, g ,jsonify
from db import RedisPool

app = Flask(__name__)
app.secret_key = 'hard key'


def get_conn():
    if not hasattr(g, 'redis_connect'):
        g.redis_connect = RedisPool()
    return g.redis_connect


@app.route('/')
def index():
    return '<h1>Welcome</h1>'


@app.route('/get')
def get_ip():
    conn = get_conn()
    return conn.gets()[0]


@app.route('/pop')
def pop_ip():
    conn = get_conn()
    return conn.pop()


@app.route('/gets/<int:num>')
def get_ips(num):
    conn = get_conn()
    total = conn.size
    if num > total:
        num = total
    return jsonify(ips=conn.gets(total=num))


@app.route('/count')
def get_counts():
    pool = get_conn()
    return str(pool.size)


if __name__ == '__main__':
    app.run(debug=True)
