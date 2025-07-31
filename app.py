import os
from flask import Flask, render_template, request
from encode import compress_json
from decode import decompress_json
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    encode_result = ""
    decode_result = ""
    active_tab = "encode"

    if request.method == 'POST':
        if 'encode_submit' in request.form:
            active_tab = "encode"
            try:
                json_data = json.loads(request.form['encode_input'])
                encode_result = compress_json(json_data)
            except Exception as e:
                encode_result = f"Invalid JSON input: {e}"
        elif 'decode_submit' in request.form:
            active_tab = "decode"
            base64_str = request.form['decode_input']
            decode_result = json.dumps(decompress_json(base64_str), indent=2)

    return render_template("index.html", encode_result=encode_result, decode_result=decode_result, active_tab=active_tab)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
