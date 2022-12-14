#tutto è pubblico --> non c'è il private come in Java = no getter e no setter

class IPaddress():
    def __init__(self,ip_stringa):  #analogo del this. in java --> qualunque metodo richiede il (self, ...)
        self.ip_notazione_dec = ip_stringa
        self.ip_notazione_bin = None
        self.ip_binario = None
        
    def ipBroad(self, sb ="/24"):
        num = int(sb[1:])
        sub_bin = ""
        sub_bin = "0"*num + 1 * (32-num)
        for w in range(0, 32):
            if(a % 8 == 0):
                temp = temp + "."
            else:
                pass
            if(self.ip_notazione_bin[w] == "0" and sub_bin[w] == "0"):
                temp 
        
    def binTOdec(self):
        pass
        


    def decTObin(self):
       lista_str = self.toList()
       biN=""
       for elemento in lista_str:
           temp = bin(elemento)[2:]
           temp = "0"*(8 - len(temp))+ temp
           biN += temp+"."
           self.ip_binario += temp
    self.ip_notazione_bin = biN[:-1]
   
    def toListBIN(self):
        lista_stringhe = self.ip_notazione_bin.split('.')
        return [bin(gruppo) for gruppo in lista_stringheBIN]
    
    def toList(self):
        lista_stringhe = self.ip_notazione_dec.split('.')
        return [int(gruppo) for gruppo in lista_stringhe]
    
def main():
    indirizzoIP = IPaddress("192.168.0.123")
    print(indirizzoIP.ip_notazione_dec)
    print(indirizzoIP.toList())
    indirizzoIP.decTObin()
    
    
if __name__ == '__main__':
    main()