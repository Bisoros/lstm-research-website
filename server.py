from flask import Flask, send_from_directory, request
import os

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
            app.logger.error(arr)
            return "false"
        np.savetxt(os.path.dirname(os.path.abspath(__file__)) + '/data/' + token_hex(16) + '.csv', np.array(arr), delimiter=',', fmt='%.0f')
    except Exception as e:
        app.logger.error(e)
        return "false"

    return "true"


if __name__ == '__main__':
    app.run(debug=True)
