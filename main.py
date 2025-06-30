from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def receive_command():
    data = request.json
    command = data.get("text")
    print("Received command:", command)
    # Here you would run your LLM + LangGraph
    return jsonify({"status": "received", "command": command})


@app.route('/', methods=['GET'])
def health():
    print("All ok")
    # Here you would run your LLM + LangGraph
    return jsonify({"status": "working"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # 👈 Use Render's assigned port
    app.run(host='0.0.0.0', port=port)        # 👈 Must bind to 0.0.0.0
