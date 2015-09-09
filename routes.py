from flask import Flask, render_template, request, flash
from forms import ContactForm

from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField

app = Flask(__name__) 
app.secret_key = 'development key'

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    class F(Form):
        submit = SubmitField("Submit")
        pass

    field_list = ['foo', 'bar', 'qux']
    for name in field_list:
        setattr(F, name, StringField(name))

    form = F()
    if request.method == 'POST':
        return 'Form posted'
    elif request.method == 'GET':
        return render_template('test.html', form=form, field_names=field_list)


@app.route('/test2', methods=['GET', 'POST'])
def test2():
    form = ContactForm()
    if request.method == 'POST':
        return 'Form posted'
    elif request.method == 'GET':
        return render_template('test2.html', form=form)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
