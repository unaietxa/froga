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
        
        
        
u1=Usuario('Ander','Conchas','','','') 
u2=Usuario('Unai','','','','') 
u3=Usuario('Jon','','','','') 
u1.Bistaratu()
u2.Bistaratu()
u3.Bistaratu()