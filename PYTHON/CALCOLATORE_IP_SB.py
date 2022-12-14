import math
class IPadress():
    def __init__(self,ip_stringa):
        self.ip_notazione_dec = ip_stringa
        self.ip_notazione_bin = None
        self.ip_Broadcast = None
        self.ip_Rete = None
        self.nHostot = None
    
    def ip_subnetting (self, subnet_mask = "/22", sottoreti):
        if(sottoreti > 0):
            num = int(subnet_mask[1:])
            nBit = math.ceil(math.log2(sottoreti))
            num += nBit
            sub_bin = ""
            sub_bin = "0"*num + "1"*(32-num)
            print(f"La subnet mask delle sottoreti è : {num}")
            for i in sottoreti:
                pass
            
        else:
            print("Nessuna sottorete generata :")
            
        
    
    def nHost(self,subnet_mask = "/22"):
        num = int(subnet_mask[1:])
        esp = 32 - num
        nHost = (2**esp)-2
        self.nHostot = nHost
        return self.nHostot
    
    def ip_broadcast(self,subnet_mask = "/22"):
        num = int(subnet_mask[1:])
        sub_bin = ""
        sub_bin = "0"*num + "1"*(32-num)
        temp = ""
        for a in range(0,32):
            if(a % 8 == 0):
                temp =temp + "."
            else:
                pass
            if(self.ip_notazione_bin[a] == "0" and sub_bin[a] == "0"):
                temp = temp + '0'
            else:
                temp = temp + '1'

        self.ip_Broadcast=temp[1:]    
        return self.ip_Broadcast

    def ip_rete(self,subnet_mask = "/22"):
        num = int(subnet_mask[1:])
        sub_bin = ""
        sub_bin = "1"*num + "0"*(32-num)
        temp = ""
        for a in range(0,32):
            if(a % 8 == 0):
                temp =temp + "."
            else:
                pass
            if(self.ip_notazione_bin[a] == "1" and sub_bin[a] == "1"):
                temp = temp + '1'
            else:
                temp = temp + '0'

        self.ip_Rete=temp[1:]
        return self.ip_Rete

    def dec2bin(self):
         lista_bin=self.ip_notazione_dec.split(".")
         lista_grupp = [int(Bin)for Bin in lista_bin]
         s = ""
         self.ip_notazione_bin = ""
         for gruppo in lista_grupp:
            temp= bin(gruppo)[2:]
            temp = "0"*(8-len(temp))+temp
            self.ip_notazione_bin = self.ip_notazione_bin+temp
            s = s +temp + "."
         return s[:-1]

    
def bin2dec(Ip):
    lista_bin_Rete=Ip.split(".")
    d = ""
    for num in lista_bin_Rete:
        temp = int(num,2)
        d = d + str(temp) +"."
    return d[:-1]

def main():
    ip_Utente = input("Indirizzo IP: ")
    subnet_mask = input("Subnet Mask: ")
    sottoreti = int(input("Quante sottoreti vuoi ottenere ? : "))
    indirizzoIP = IPadress(ip_Utente)
    print(f"IP decimale: {indirizzoIP.ip_notazione_dec}")
    print(f"IP binario: {indirizzoIP.dec2bin()}\n")
    print(f"Numero totale di host utilizzabili : {indirizzoIP.nHost(subnet_mask)}")
    print(f"IP broadcast decimale: {bin2dec(indirizzoIP.ip_broadcast(subnet_mask))}")
    print(f"IP rete decimale: {bin2dec(indirizzoIP.ip_rete(subnet_mask))}")
    print(f"")

if __name__ == "__main__":
    main()