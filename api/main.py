import mysql.connector
from mysql.connector import Error
from flask import Flask, request, jsonify
from operator import itemgetter
import json

app = Flask(__name__)

@app.route('/flights/<id>/passengers', methods=['GET'])
def getFlights(id):
    idVuelo = id
    try:
        conn = mysql.connector.connect(host='mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com',
                                        database='airline',
                                        user='bsale_test',
                                        password='bsale_test')

    finally:
        if conn.is_connected():
#Realizar Queries, 1) recibir toda la informacion del vuelo, utilizando el id recibido por link.
            queryFlight = (" SELECT DISTINCT f.takeoff_date_time,f.takeoff_airport,f.landing_date_time, f.landing_airport, f.airplane_id FROM boarding_pass AS bp JOIN passenger AS p ON bp.passenger_id = p.passenger_id JOIN flight AS f ON  bp.flight_id = f.flight_id WHERE bp.flight_id = %s")
            cursor = conn.cursor()
            cursor.execute(queryFlight, (idVuelo,))
            resf = cursor.fetchall()
            #print(resf)
        # 2) Recibir informacion de los pasajeros
            queryPassenger = ("SELECT p.passenger_id, p.dni, p.name, p.age, p.country, bp.boarding_pass_id, bp.purchase_id, bp.seat_id   FROM boarding_pass AS bp JOIN passenger AS p ON p.passenger_id = bp.passenger_id where bp.flight_id = %s")
            cursor.execute(queryPassenger, (idVuelo,))
            
            resp = cursor.fetchall()
            #print(resp[0])
#Construir objeto json entero
            resjson = {}
            #Construir objeto pasajeros
            passArray = []
            passengers = {} 
            #passValues = ["passengerId", "dni", "name", "age", "country","boardingPassId", "seatTypeId", "seatId"]
            i = 0
            while i < len(resp):
                passengers = {} 
                passengers["passengerId"] = resp[i][0]
                passengers["dni"] = resp[i][1]
                passengers["name"] = resp[i][2]
                passengers["age"] = resp[i][3]
                passengers["country"] = resp[i][4]
                passengers["boardingPassId"] = resp[i][5]
                passengers["seatTypeId"] = resp[i][6]
                passengers["seatId"] = resp[i][7]      
                passArray.append(passengers)
                i+=1

            
            #print(passArray)
    #Construir objeto data
            data = {}
            data['flightId'] = resf[0][0]
            data['takeOffTime'] = resf[0][1]
            data['landingDateTime'] = resf[0][2]
            data['landingAirport'] = resf[0][3]
            data['airplaneId'] = resf[0][4]
            data['passengers'] = passArray
    #Construir objeto que contiene data

            resjson["code"] = 200
            resjson["data"] = data 
            json_data = json.dumps(resjson)
            cursor.close()
            conn.close()
            print("Bye bye")
            return(json_data)
            
        elif resf == None:
            return{
                "code": 404,
                "data": {}
            }
        else:
            return{
                "code":400,
                "errors": "could not connect to db"
            }
        


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)