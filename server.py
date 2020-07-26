from flask import Flask, send_from_directory, request

import numpy as np
from secrets import token_hex

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return send_from_directory('templates', 'index.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        arr = list(map(int, list(request.get_json())))
        if not all([i == 0 or i == 1 for i in arr]):
            return "false"
        np.savetxt('data/' + token_hex(16) + '.csv', np.array(arr), delimiter=',', fmt='%.0f')
    except:
        return "false"

    return "true"


if __name__ == '__main__':
    app.run(debug=True)
