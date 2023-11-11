from flask import Flask, request

app = Flask(__name__)
counter = 0

@app.route('/', methods=['GET', 'POST'])
def counter_service():
    global counter

    if request.method == 'POST':
        counter += 1
        return "POST Request Registerd!!!!"

    return f"Counter: {counter}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
