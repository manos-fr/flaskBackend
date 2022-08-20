import psycopg2
from psycopg2 import Error
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/titles', methods=['GET'])
def get_titles():
    try:
        cursor = connection.cursor()
        with connection:
            cursor.execute(f"SELECT * FROM titles")
            response = cursor.fetchall()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    key_list = ["tconst", "titletype", "originaltitle", "primarytitle",
                "isadult", "startyear", "endyear", "runtimeminutes", "genres"]

    res = []

    for i in range(0, len(response)-1):
        res.append({
            key_list[0]: response[i][0],
            key_list[1]: response[i][1],
            key_list[2]: response[i][2],
            key_list[3]: response[i][3],
            key_list[4]: response[i][4],
            key_list[5]: response[i][5],
            key_list[6]: response[i][6],
            key_list[7]: response[i][7],
            key_list[8]: response[i][8],
        })
    return {'rows': res}


if __name__ == '__main__':
    connection = psycopg2.connect(user="vqlnioqfkvocxj", password="20de6fb3a0fd8e652444adbe7273c89429f28c11cc1376e46eb789cfb8474bef",
                                  host="ec2-54-229-217-195.eu-west-1.compute.amazonaws.com", port="5432", database="de9mikemijit5j")
    app.run(host="0.0.0.0", port=3000, debug=True, threaded=True)
