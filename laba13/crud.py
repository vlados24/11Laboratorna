from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class PhotographerDevice(db.Model):

    id = db.Column(db.Integer,  nullable=False,  primary_key=True, autoincrement=True)
    weight = db.Column(db.Integer, nullable=False, unique=False)
    size = db.Column(db.Integer, nullable=False, unique=False)

    def __init__(self,
                 weight=0.0,
                 size=0.0):
        self.weight = weight
        self.size = size


class PhotographerDeviceSchema(ma.Schema):

    class Meta:

        fields = ('weight', 'size')


photographerDevice_schema = PhotographerDeviceSchema()

photographerDevices_schema = PhotographerDeviceSchema(many=True)

db.create_all()


@app.route("/photographerDevice", methods=["POST"])
def add_photographerDevice():

    weight = request.json['weight']

    size = request.json['size']

    new_photographerDevice = PhotographerDevice(weight, size)

    db.session.add(new_photographerDevice)

    db.session.commit()

    return photographerDevice_schema.jsonify(new_photographerDevice)


@app.route("/photographerDevice", methods=["GET"])
def get_photographerDevice():
    all_photographerDevices = PhotographerDevice.query.all()
    result = photographerDevices_schema.dump(all_photographerDevices)
    return jsonify(result.data)


@app.route("/photographerDevice/<id>", methods=["GET"])
def photographerDevice_detail(id):

    photographerDevice = PhotographerDevice.query.get(id)

    return photographerDevice_schema.jsonify(photographerDevice)


@app.route("/photographerDevice/<id>", methods=["PUT"])
def photographerDevice_update(id):

    photographerDevice = PhotographerDevice.query.get(id)

    weight = request.json['weight']

    size = request.json['size']

    photographerDevice.weight = weight

    photographerDevice.size = size

    db.session.commit()

    return photographerDevice_schema.jsonify(photographerDevice)


@app.route("/photographerDevice/<id>", methods=["DELETE"])
def photographerDevice_delete(id):
    photographerDevice = PhotographerDevice.query.get(id)
    db.session.delete(photographerDevice)
    db.session.commit()

    return photographerDevice_schema.jsonify(photographerDevice)


if __name__ == '__main__':
    app.debug = True
    app.run()
