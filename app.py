from flask import Flask, Response, send_file
import os

app = Flask(__name__)

@app.route('/v4/', methods=['GET'])
def get_angelchip():
    file_path = 'angelchip.bin'

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            data = f.read()

        headers = {
            'Content-Type': 'text/html; charset=UTF-8',
            'X-Powered-By': 'PHP/8.0.23',
            'Cache-Control': 'no-store, no-cache, must-revalidate',
            'Pragma': 'no-cache',
            'Vary': 'Accept-Encoding,User-Agent'
        }

        return Response(data, headers=headers)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)
