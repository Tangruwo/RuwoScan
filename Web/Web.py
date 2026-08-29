# 这里是ai写的，就是省心哈，就是核心部分不敢给它，怕看不懂哈

from flask import Flask, render_template, jsonify, request
import json
import os
import webbrowser

app = Flask(__name__)

# 获取当前文件所在目录的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "..", "prompts", "ruwoscan.log")
CMD_FILE = os.path.join(BASE_DIR, "..", "prompts", "ruwoscan.log")


def get_logs(limit=200):
    logs = []
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[-limit:]:
                if line.strip():
                    try:
                        logs.append(json.loads(line))
                    except:
                        pass
    except FileNotFoundError:
        pass
    except Exception as e:
        print(e)
    return logs


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/logs")
def logs():
    return jsonify({"logs": get_logs()})


@app.route("/command", methods=["POST"])
def command():
    cmd = request.get_json().get("command", "")
    if cmd:
        try:
            with open(CMD_FILE, "w", encoding="utf-8") as f:
                f.write(cmd)
        except Exception as e:
            return jsonify({"status": "error", "msg": str(e)})
    return jsonify({"status": "ok"})


@app.route("/clear", methods=["POST"])
def clear():
    try:
        open(LOG_FILE, "w", encoding="utf-8").close()
    except:
        pass
    return jsonify({"status": "ok"})


if __name__ == "__main__":

    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":# 只在主进程中打开浏览器
        webbrowser.open("http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)