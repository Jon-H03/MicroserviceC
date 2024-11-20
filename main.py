from flask import Flask, jsonify
from datetime import datetime


app = Flask(__name__)


@app.route('/datetime', methods=['GET'])
def get_datetime():

    now = datetime.now()

    date_time = now.strftime("Generated on %Y-%m-%d at %H:%M:%S")

    # Return the formatted date and time
    return jsonify({"date_time": date_time}), 200


if __name__ == '__main__':
    app.run(port=5002)
