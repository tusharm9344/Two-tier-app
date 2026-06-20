import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DB URL comes from environment variable (set in docker-compose)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@app.route('/notes', methods=['POST'])
def add_note():
    content = request.form.get('content')
    if content:
        note = Note(content=content)
        db.session.add(note)
        db.session.commit()
    return ('', 204)

@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return ('', 204)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # creates tables on startup
    app.run(host='0.0.0.0', port=5000, debug=True)
