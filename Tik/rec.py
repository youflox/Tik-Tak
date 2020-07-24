from flask import Flask, render_template, request,redirect, url_for, make_response, jsonify, session

app = Flask(__name__)

app.secret_key = 'a3fc4b5b2c78c53a36910465305d1686456'

moves = {}

@app.route('/', methods = ['GET','POST'])
def login():
    if request.method == 'Post':
        user = request.form('username')

        opponent_player = request.get_json()

        return redirect(url_for('user', username = user))

@app.route('/<user>')
def player(user):

    # session.pop('posted_da', None)
    return render_template('user.html', username=user)

# @app.route('/<opponent>')
# def opponent_player(opponent):
#     session.pop('getter', None)
#     return render_template('opponent.html')


@app.route('/<username>/post', methods=['POST'])
def user_post(username):
    if request.method == 'POST':
        req = request.get_json()
        moves[username] = req
        print(username,'US REC ',moves[username])
        res = make_response(jsonify({'msg':'received'}), 200)
        return res

@app.route('/<username>/get')
def user_get(username):
    if request.method == 'GET':
        print()
        if username in moves:
            data = moves[username]
            print(username, 'US SEN ', moves[username])
            return make_response(jsonify({'data': data}), 200)
        else:
            return 'null'

@app.route('/<opponent>/post', methods=['POST'])
def opponent_post(opponent):

    if request.method == 'POST':
        req = request.get_json()
        moves[opponent] = req
        print(opponent,'OP REC ',moves[opponent])

        res = make_response(jsonify({'msg':'received'}), 200)
        return res

@app.route('/<opponent>/get')
def opponent_get(opponent):
    if request.method == 'GET':
        if opponent in moves:

            print(opponent, 'OP SEN ', moves[opponent])

            return make_response(jsonify({'data': moves[opponent]}), 200)
        else:
            return 'null'



if __name__ == '__main__':
    app.run(debug=True)
