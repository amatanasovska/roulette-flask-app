from flask import *
import game
import db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def m():
    return render_template('front.html')


@app.route('/rand', methods=['GET', 'POST'])
def p():
    data = request.get_data().decode("utf-8")
    if data:
        return str(game.Game.play(str(data))) + ' ' + str(game.Game.winning)
    else:
        return "ERROR"


@app.route('/logIn', methods=['GET', 'POST'])
def lgin():
    data = request.get_data().decode("utf-8")
    if data:
        return str(db.Db.logIn(data))
    else:
        return "fail"


@app.route('/reqsignup', methods=['GET', 'POST'])
def reqsignup():
    data = request.get_data().decode("utf-8")
    if data != 'username=&password=':
        return str(db.Db.new_user(data))
    else:
        return "fail"


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/getcreds', methods=['GET', 'POST'])
def getcredits():
    return render_template("getcredits.html")


@app.route('/reqcredits', methods=['GET', 'POST'])
def reqcredits():
    data = request.get_data().decode("utf-8")
    arr = data.split('&')
    if arr[0] != 'credits=' and arr[1] != 'username=':
        return str(db.Db.addCredits(data))
    else:
        return "fail"


if __name__ == "__main__":
    app.run()
