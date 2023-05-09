class Asiento :
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.next = None


class Avion:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def agregar(self, Asiento):
        if(self.head == None):
            tmpAsiento = Asiento
            self.head = tmpAsiento
            self.tail = tmpAsiento
        else:
            tmpAsiento = self.head
            while(tmpAsiento.next != None):
                tmpAsiento = tmpAsiento.next
            tmpAsiento.next = Asiento
            self.tail = Asiento


    def imprimirlista(self):
        tempAsiento = self.head
        while(tempAsiento.next != None):
            print("Asiento es:", tempAsiento.row, " ", tempAsiento.col)
            tempAsiento = tempAsiento.next