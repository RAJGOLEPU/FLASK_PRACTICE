from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        return redirect(url_for('greeting', name=name))
    return render_template('index.html')

@app.route('/greeting')
def greeting():
    name = request.args.get('name')
    return render_template('greeting.html', name=name)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
