from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name': 'JavaScript'}, {'name': 'Python'}, {'name': 'HTML'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works'})

@app.route('/lang/<string:name>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/lang', methods=['GET', 'POST', 'PUT', 'DELETE'])
def lang(name=''):
    langs = [language for language in languages if language['name'] == name]
    if langs:
        if request.method == 'GET':
            return jsonify({'language':langs[0]})
        elif request.method == 'PUT':
                langs[0]['name'] = request.json['name']
                return jsonify({'language':langs[0]})
        elif request.method == 'DELETE':
                languages.remove(langs[0])
                return jsonify({'languages': languages})
    elif request.method == 'POST':
        language = {'name': request.json['name']}
        languages.append(language)
        return jsonify({'languages': languages})
    else:
        return jsonify({'languages': languages})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
