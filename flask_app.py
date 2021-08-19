import traceback

from flask import Flask, request, jsonify
from flask_cors import CORS

from decoder import decode_did

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def entry():
    try:
        decode_did(request.get_json())
    except BaseException as e:
        print(traceback.format_exc())
        return jsonify({'message': str(e)}), 400
    else:
        return jsonify({'message': 'Successfully verified user'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
