import requests
import asiento as a


def BusquedaAsientos(val):
    i = 0    
    queryFlight = "https://bsalesapi.herokuapp.com/flights/"+str(val)+"/passengers"
    resFlight = requests.get(queryFlight)
    boardListCol = []
    boardListRow = []
    print("++++++++++++++++Inicio++++++++++++++++++")
    while i < (len(resFlight.json()["data"]["passengers"])-1):
        pasajero = resFlight.json()["data"]["passengers"][i]
        while(pasajero["seatId"] == None):
            i+=1
            pasajero = resFlight.json()["data"]["passengers"][i]    
        
        boardVal = pasajero["boardingPassId"]
        print(boardVal)
        #boardVal = pasajero["boardingPassId"]    
        querySeats ="https://bsalesapi.herokuapp.com/flights/"+ str(val) +"/seats/"+str(boardVal)
        resSeats = requests.get(querySeats)
        boardListCol.append(resSeats.json()["seatCol"])
        boardListRow.append(resSeats.json()["seatRow"])
        i+=1

    boardList = (boardListCol,boardListRow)
    print("++++++++++++++++Fin++++++++++++++++++")
    return(boardList)

def AvionLista(boardList):
    listaAv = a.Avion()    
    for i in range(0, len(boardList)):
        nodoAsiento = a.Asiento(boardList[0][i], boardList[1][i])
        listaAv.agregar(nodoAsiento)
    return(listaAv)
        





#listaPass = resFlight.json()["data"]["passengers"]
#print(resSeats.json()["seatCol"])
#print(resSeats.json()["seatRow"])