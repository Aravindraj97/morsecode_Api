# app.py

from flask import Flask, request, jsonify
from morsedict import MORSE_CODE_DICT

app = Flask(__name__)

def convert_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += ' '
    return morse_code.strip()

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    morse_code = convert_to_morse(text)
    return jsonify({'text': text, 'morse_code': morse_code})

if __name__ == '__main__':
    app.run(debug=True)
