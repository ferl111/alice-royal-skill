from flask import Flask, request, jsonify

app = Flask(__name__)

# функция добавления титула
def format_response(text):
    return f"{text}, Ваше Величество"

@app.route("/", methods=["POST"])
def webhook():
    req = request.json
    user_text = req["request"]["original_utterance"].lower()

    # простая логика
    if "привет" in user_text:
        response_text = "Рад вас видеть"
    elif "как дела" in user_text:
        response_text = "Все отлично"
    else:
        response_text = "Я слушаю вас"

    # добавляем титул
    response_text = format_response(response_text)

    return jsonify({
        "response": {
            "text": response_text,
            "end_session": False
        },
        "version": "1.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)