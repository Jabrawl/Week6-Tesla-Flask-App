from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from car_inventory.forms import CarForm
from car_inventory.models import Car, db


site = Blueprint('site', __name__, template_folder = 'site_templates')

"""
Note that in the above code, some arguments are specified when creating the 
Blueprint object. The first argument, 'site', is the Blueprint's name, this is used
by Flask's routing mechanism. The second argument, __name__, is the Blueprint's import name,
which Flask uses to locate the Blueprint's resources
"""

@site.route('/')
def home():
    return render_template('index.html')


@site.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
    my_car = CarForm()
    try:
        if request.method == "POST" and my_car.validate_on_submit():
            name = my_car.name.data
            description = my_car.description.data
            price = my_car.price.data
            color = my_car.color.data
            model = my_car.model.data
            year = my_car.year.data
            mileage = my_car.mileage.data
            cost_of_production = my_car.cost_of_production.data
            user_token = current_user.token

            car = Car(name, description, price, color, model, year, mileage, cost_of_production, user_token)

            db.session.add(car)
            db.session.commit()

            return redirect(url_for('site.profile'))

    except:
        raise Exception("Tesla not created, please check your form and try again!")

    user_token = current_user.token

    cars = Car.query.filter_by(user_token = user_token)


    return render_template('profile.html', form = my_car, cars = cars)