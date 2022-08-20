import psycopg2
from psycopg2 import Error
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

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

    return {"data": response}


if __name__ == '__main__':
    connection = psycopg2.connect(user="vqlnioqfkvocxj", password="20de6fb3a0fd8e652444adbe7273c89429f28c11cc1376e46eb789cfb8474bef",
                                  host="ec2-54-229-217-195.eu-west-1.compute.amazonaws.com", port="5432", database="de9mikemijit5j")
    app.run(host="0.0.0.0", port=3001, debug=True, threaded=True)
