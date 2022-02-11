from flask import Flask
from flask_restful import Resource, Api,reqparse,request
import pandas as pd
from datetime import datetime
from threading import Timer
import ast

app = Flask(__name__)
api=Api(app)

#user file
user_path='/RESTAPI Data/Data/users.xlsx'
location_path='/RESTAPI Data/Data/Location.xlsx'
#location file

class users(Resource):
    def get(self):
        data=pd.read_excel(user_path)
        data=data.to_dict()
        return {'data':data},200

    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument ('Location',required=True,type=int)
        parser.add_argument('Name',required=True,type=str)
        parser.add_argument('City', required=True, type=str)
        args=parser.parse_args()

        data=pd.read_excel(user_path)

        if args['UserId'] in data['UserId']:
            return {
                'message': f"{args['UserId']} already Exits"
            },409
        else:
            data=data.append({
                'UserId':str(args['UserId']),
                'Name': args['UserId'],
                'City': args['UserId'],
                'Location': []
            }, ignore_index=True)
            data.to_excel(user_path,index=False)
            return {'data':data.to_dict()},200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('UserId', required=True, type=int)
        args=parser.parse_args()

        data=pd.read_excel(user_path)

        if args['UserId'] in data['UserId']:
            data=data[data['UserId'] !=str(args['UserId'])]
            data.to_excel(user_path,index=False)
            return{'data':data.to_dict()},200
        else:
            return{'message': f"{args['UserId']} does not exit!"
                   },404

class Location(Resource):
    def get(self):
        data=pd.read_excel(location_path)
        return {'data':data.to_dict()},200

#api.com/users
api.add_resource(users,'/RESTAPI Data/Data/users.xlsx')
api.add_resource(Location,'/RESTAPI Data/Data/Location.xlsx')

if __name__ =="__main__":
    app.run(debug=True)

