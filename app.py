from flask import Flask, render_template, request, send_file, jsonify
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address
import sqlite3
import os

app = Flask(__name__, static_folder='static', static_url_path='')
# limiter = Limiter(
#     app,
#     key_func=get_remote_address,
#     default_limits=["200 per day", "50 per hour"]
# )


@app.route('/tracker_for_me')
def tracker_for_me():
    filename = '1px.png'
    ip_addr = "\""+request.remote_addr+"\""
    user_agent = "\"" + request.user_agent.string + "\""
    referrer = request.referrer
    print('IP Address : {}, User Agent : {}, Referrer : {}'.format(ip_addr, user_agent, referrer))
    attrs = (ip_addr, user_agent, referrer)
    cs.execute("INSERT INTO user (ip_addr, user_agent, referrer) VALUES (?, ?, ?)", attrs)
    conn.commit()
    return send_file(filename, mimetype='image/png')


@app.route('/tracker_list_for_me')
def tracker_list_for_me():
    cs.execute("SELECT * from user order by id desc limit 100")
    json_array = []
    for row in cs:
        json_array.append({
            "id" : row[0],
            "ip_addr" : row[1],
            "user_agent" : row[2],
            "referrer" : row[3]
        })
    return render_template('tracker_list.html', datas=json_array)


@app.route('/')
def show_main():
    return render_template('index.html')


def get_connect_db_path():
    path = os.path.dirname(os.path.realpath(__file__))
    connect_log_path = path + "/connect_log.db"
    return connect_log_path


def init_db():
    conn = sqlite3.connect(get_connect_db_path(), check_same_thread=False)
    cs = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, ip_addr TEXT, user_agent TEXT, referrer TEXT)"
    cs.execute(query)
    return cs, conn


if __name__ == '__main__':
    cs, conn = init_db()
    app.run(host='0.0.0.0', port=82)
