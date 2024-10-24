class Animal:
    def __init__(self,Nombre ,Tipo ):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.hambre = 0
        self.Sed = 0
    
    def alimentar(self):
        self.hambre = self.hambre -1

    def dar_agua(self):
        self.Sed = self.Sed -1
    
    def estado(self):
        #vCad = 'Hambre: {self.hambre} Sed:{self.Sed}'
        vCad = 'Hambre:' 
        vCad += str(self.hambre)
        vCad += 'Sed:' 
        vCad += str(self.Sed)

        return vCad


class Carnivoro(Animal):
    def __init__(self,Nombre ,Tipo):
        Animal.__init__(self,Nombre,Tipo)


class Alimento:
    def __init__(self, Tipo,Cantidad : int):
        self.Tipo = Tipo
        self.Cantidad = Cantidad

    def usar(self,Cantidad):
        if not isinstance(Cantidad,int):
            raise TypeError('La Cantidad debe ser un entero')
        self.Cantidad -=Cantidad
    
    def es_alimento_adecuado(cls, tipo_animal):
        pass
    
    def estado(self):
        vCad = 'Cantidad'
        vCad += str(self.Cantidad)
        return vCad

class AlimentoCarne(Alimento):
    def __init__(self, Tipo,Cantidad):
        Alimento.Tipo = Tipo
        Alimento.Cantidad = Cantidad
    

            

Chuletas = AlimentoCarne('cerdo',100)
Chuletas.usar(50)
print(Chuletas.estado())

Animal1= Carnivoro('Leon','Carnivoro')

Animal1.alimentar()

print(Animal1.estado())
print(Animal1.estado())

    