from flask import Blueprint, request, jsonify
from car_inventory.helpers import token_required
from car_inventory.models import db, Car, car_schema, cars_schema


api = Blueprint('api', __name__, url_prefix = '/api')


@api.route('/getdata')
@token_required
def getdata(our_user):
    return {'some': 'value'}

#create drone endpoint
@api.route('/cars', methods = ['POST'])
@token_required
def create_car(our_user):
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    color = request.json['color']
    model = request.json['model']
    year = request.json['year']
    mileage = request.json['mileage']
    cost_of_production = request.json['cost_of_production']
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    car = Car(name, description, price, color, model, year, mileage, cost_of_production, user_token=user_token)

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)

    return jsonify(response)


#Retrieve all drone endpoints
@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(our_user):
    owner = our_user.token
    cars = Car.query.filter_by(user_token= owner).all()
    response = cars_schema.dump(cars)

    return jsonify(response)


#Retrieve One Drone Endpoint
@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(our_user, id):
    owner = our_user.token
    if owner == our_user.token:
        car = Car.query.get(id)
        response = car_schema.dump(car)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Id Required'}), 401
    
#Update Drone Endpoint
@api.route('/cars/<id>', methods = ['PUT','POST'])
@token_required
def update_car(our_user, id):
    car = car.query.get(id)
    car.name = request.json['name']
    car.description = request.json['description']
    car.price = request.json['price']
    car.color = request.json['color']
    car.model = request.json['model']
    car.year = request.json['year']
    car.mileage = request.json['[mileage']
    car.cost_of_production = request.json['cost_of_production']
    car.user_token = our_user.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

#Delete Drone Endpoint
@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_cars(our_user, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)