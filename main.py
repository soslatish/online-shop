from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    #isActive = db.Column(db.Bool, default=True)
    text = db.Column(db.Text, nullable = False)
with app.app_context():
    db.create_all()
     
    def __repr__(self):
        return f'Запись: {self.title}'
    
@app.route('/')
def index():
    items= Item.query.all()
    return render_template('index.html',data=items)

@app.route('/about')
def about():
    return render_template('about.html')
 
@app.route('/create', methods=['POST','GET'])
def create():
    if request.method == 'POST' and all(elem in request.form.keys() for elem in ['subb','dess']):
            title=request.form['title']
            price=request.form['price']

            item=Item(title=title, price=price)

            try:
                db.session.add(item) 
                db.session.commit()
                return redirect(url_for('/'), 301)
            except: 
                return "Ошибочка"

    else:
        return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)
    