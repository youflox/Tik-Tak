from flask import Flask, render_template, request, make_response, jsonify, session

app = Flask(__name__)

app.secret_key = 'a3fc4b5b2c78c53a36910465305d1686456'

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/Nanda')
def home():
    session.pop('posted_da', None)
    return render_template('home.html')

@app.route('/Ratna')
def test():
    session.pop('getter', None)
    return render_template('test.html')


@app.route('/post', methods=['GET','POST'])
def resp():

    if request.method == 'POST':
        req = request.get_json()
        print(req)
        session['posted_da'] = req
        res = make_response(jsonify({'msg':'received'}), 200)
        return res

    if request.method == 'GET':
        if 'posted_da' in session:
            data = session['posted_da']
            return make_response(jsonify({'data': data}), 200)
        else:
            return 'null'

@app.route('/getter', methods=['GET','POST'])
def getter():

    if request.method == 'POST':
        req = request.get_json()
        print(req)
        session['getter'] = req
        res = make_response(jsonify({'msg':'sent'}), 200)
        return res

    if request.method == 'GET':
        if 'getter' in session:
            return make_response(jsonify({'data': session['getter']}), 200)
        else:
            return 'null'



if __name__ == '__main__':
    app.run(debug=True)
