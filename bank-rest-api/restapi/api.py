from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
import os
import sqlite3
import pandas as pd

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/')
def index():
    return 'Server is UP and RUNNING!!'

#LOCAL VARIABLE TO STORE USER'S CRED
user_cred_storage_list = [
    {"userName": "admin", "password":"admin", "userProfile": "Bank Account Executive"},
]

class userValidation(Resource):
    
    #GET REQUEST
    #def get(self):

    def post(self):
        if (request.data):
            some_json = request.get_json()
            userName = some_json["userName"]
            password = some_json["password"]
            userProfile = some_json["profile"]["prName"]
            '''print(userName)print(password)print(userProfile)'''

            #QUERY FOR VALIDATION
            con = connect()
            #df_match = pd.read_sql_query("SELECT * FROM login;", con)
            #print(df_match.userName.iloc)
            con.row_factory = lambda cursor, row: row[0]
            c = con.cursor()
            u_names = c.execute('SELECT userName FROM login').fetchall()
            u_pass = c.execute('SELECT password FROM login').fetchall()
            u_profiles = c.execute('SELECT prName FROM login').fetchall()
            #print(u_names)
            #print(u_pass)
            #print(u_profiles)


            '''for i in range(len(u_names)):
                if u_names[i] == userName and u_pass[i] == password and u_profiles[i] == userProfile:
                    return 200
            else:
                return 404'''


            if userName in u_names:
                u_id = u_names.index(userName)
                if password == u_pass[u_id] and userProfile == u_profiles[u_id]:
                    return 200
                else:
                    return 404
            else:
                return 404
            '''for user in user_cred_storage_list:
                if user['userName'] == userName and user['password'] == password and user['userProfile'] == userProfile:
                    return 200
            else:
                return 404
            '''

api.add_resource(userValidation, '/user')


def connect():
    BASE_DIR = os.path.dirname(os.getcwd())
    #db_path = os.path.join(BASE_DIR, "db.db")
    #db_path = 'E:\\TCS_Projects\\bank-rest-api\\restapi\\' + 'db.db'
    db_path = 'E:\\TCS_Projects\\database\\' + 'db.db'
    print(db_path)
    con = sqlite3.connect(db_path)
    #cur = con.cursor()
    #df_match = pd.read_sql_query("SELECT * FROM login;", con)
    #print(df_match)
    return con


if __name__ == '__main__':
    print("Server is Up and Running!")
    app.run(debug=True)