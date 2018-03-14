'''
Created on 7 mar. 2018

@author: admin
'''

class Usuario:
    '''
    classdocs
    '''


    def __init__(self, Nombre, Apellido, DNI, Telefono, Helbidea):
        
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.DNI = DNI
        self.Telefono = Telefono
        self.Helbidea = Helbidea
        '''
        Constructor
        '''
    def Bistaratu (self):
        print (self.Nombre,self.Apellido)
        
    def BistaratuDNI (self):
        print(self.DNI)
        
    def BistaratuTel(self):
        print(self.Telefono)
        
        
        
            
        
        
            
        
u1=Usuario('Ander','Conchas','65432345X','688666006','') 
u2=Usuario('Unai','','','','') 
u3=Usuario('Jon','','','','') 
u4=Usuario('Tarantula','','','','') 
u1.Bistaratu()
u2.Bistaratu()
u3.Bistaratu()
u4.Bistaratu()
u1.BistaratuDNI()
u1.BistaratuTel()


