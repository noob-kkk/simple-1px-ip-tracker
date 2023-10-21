from flask import Flask, render_template, request, send_file, jsonify
import sqlite3
import os
import geoip2.database
from datetime import datetime

# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address


reader = geoip2.database.Reader("./GeoLite2-City.mmdb")
app = Flask(__name__, static_folder="static", static_url_path="")


# # Dependency Error in PI...
# limiter = Limiter(
#     app,
#     key_func=get_remote_address,
#     default_limits=["200 per day", "50 per hour"]
# )


@app.route("/tracker_for_me")
def tracker_for_me():
    filename = "1px.png"
    ip_addr = str(request.environ["HTTP_X_REAL_IP"]) or str(
        request.remote_addr
    )
    try:
        response = reader.city(ip_addr)
        country = response.country.name
        city = response.city.name
    except Exception as e:
        print("error in tracker_for_me : ", e)
    user_agent = str(request.user_agent.string)
    referrer = request.referrer
    try:
        country
    except:
        country = ""
    try:
        city
    except:
        city = ""
    date = datetime.now()
    attrs = (ip_addr, country, city, date, user_agent, referrer)
    cs.execute(
        "INSERT INTO user (ip_addr, country, city, date, user_agent, referrer) VALUES (?, ?, ?, ?, ?, ?)",
        attrs,
    )
    conn.commit()
    return send_file(filename, mimetype="image/png")


@app.route("/tracker_list_for_me")
def tracker_list_for_me():
    cs.execute("SELECT * from user order by id desc limit 500")
    json_array = []
    for row in cs:
        # split_ip_addrs = row[1].split(".")
        # ip_addr = ".".join(split_ip_addrs[0:3]) + ".*"
        ip_addr = row[1]
        # now_kst = row[4].astimezone(timezone('Asia/Seoul'))
        json_array.append(
            {
                "id": row[0],
                "ip_addr": ip_addr,
                "country": row[2],
                "city": row[3],
                "date": row[4],
                "user_agent": row[5],
                "referrer": row[6],
            }
        )
    return render_template("tracker_list.html", datas=json_array)


@app.route("/my_ip")
def my_ip():
    return request.remote_addr


@app.route("/")
def show_main():
    return render_template("index.html")


def get_connect_db_path():
    path = os.path.dirname(os.path.realpath(__file__))
    connect_log_path = path + "/connect_log.db"
    return connect_log_path


def init_db():
    conn = sqlite3.connect(get_connect_db_path(), check_same_thread=False)
    cs = conn.cursor()
    query = (
        "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "ip_addr TEXT, country TEXT, city TEXT, date TEXT, user_agent TEXT, referrer TEXT)"
    )
    cs.execute(query)
    return cs, conn


if __name__ == "__main__":
    cs, conn = init_db()
    app.run(host="0.0.0.0", port=1005)
