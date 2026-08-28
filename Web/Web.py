from flask import Flask, render_template, jsonify, request
import json
import webbrowser

app = Flask(__name__)
LOG_FILE = "../prompts/ruwoscan.log"

def get_logs(limit=100):
    logs = []
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f.readlines()[-limit:]:
                if line.strip():
                    try:
                        logs.append(json.loads(line))
                    except:
                        pass
    except:
        pass
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
        with open("prompts/command.txt", "w", encoding="utf-8") as f:
            f.write(cmd)
    return jsonify({"status": "ok"})

@app.route("/clear", methods=["POST"])
def clear():
    open(LOG_FILE, "w", encoding="utf-8").close()
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    webbrowser.open("127.0.0.1:5000")