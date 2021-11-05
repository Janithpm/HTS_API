
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

htsData = {}

htsArgs = reqparse.RequestParser()
htsArgs.add_argument('dateTime', type=str, help='Date and Time', required=True)
htsArgs.add_argument('tempC', type=float,
                     help='Temperature in C', required=True)
htsArgs.add_argument('tempF', type=float,
                     help='Temperature in F', required=True)
htsArgs.add_argument('hum', type=int, help='Humidity', required=True)
htsArgs.add_argument('sm', type=int, help='Soil Moisture', required=True)


def abortIfNotFound(deviceID):
    if deviceID not in htsData:
        abort(404, message="Device not found")


def abortIfFound(deviceID):
    if deviceID in htsData:
        abort(409, message="Device already exists")


class Hts(Resource):
    def get(self, deviceID):

        if deviceID == "all":
            return htsData, 201

        abortIfNotFound(deviceID)

        return htsData[deviceID], 201

    def put(self, deviceID):
        # abortIfFound(deviceID)
        args = htsArgs.parse_args()
        htsData[deviceID] = {
            args['dateTime']: {
                'tempC': args['tempC'],
                'tempF': args['tempF'],
                'hum': args['hum'],
                'sm': args['sm']
            }
        }

        return htsData[deviceID], 201


api.add_resource(Hts, '/hts/<deviceID>')

if __name__ == '__main__':
    app.run(debug=True)
