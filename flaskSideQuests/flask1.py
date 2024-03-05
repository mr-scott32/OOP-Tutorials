from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

class DogForm(FlaskForm):
    breed = SelectField('Select Dog Breed', choices=[('Labrador Retriever', 'Labrador Retriever'),
                                                     ('German Shepherd', 'German Shepherd'),
                                                     ('Golden Retriever', 'Golden Retriever'),
                                                     ('Bulldog', 'Bulldog'),
                                                     ('Beagle', 'Beagle')],
    validators=[DataRequired()])
    bark_button = SubmitField('Bark')
    cancel_button = SubmitField('Cancel')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DogForm()
    if form.validate_on_submit():
        if form.bark_button.data:
            breed = form.breed.data
            flash(f"The {breed} says Woof!")
        elif form.cancel_button.data:
            flash("Barking canceled.")
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
