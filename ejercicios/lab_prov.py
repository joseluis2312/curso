from typing import List, Tuple
from functools import reduce

class generate_sales_report:
    """
       Genera el reporte

    """
    def __init__(self,store_name:str, date:str, sales_data: List[Tuple[str, float, int]], include_tax: bool,currency:str) -> float:
        """
       Inicializa el objeto almacenando todos los parametros 
        
        """
        self.List = list
        self.sales_data = sales_data
        self.include_tax = include_tax
        self.store_name =store_name
        self.date =date
        self.currency = currency
    def funcion_Total_Importe_Item(self,registro:Tuple[str, float, int],ConTasa:bool ):
        vTax = 0
        if ConTasa ==True:
          vTax = 10

        FCalculo = (lambda r:r[1] * r[2]* ((100 + vTax)/100) )
        pepe = FCalculo(registro)
        return FCalculo(registro)
    def funcion_Total_Importe_Items(self, ConTasa:bool ):
        vTotalC = reduce(lambda x,y: x+y, [self.funcion_Total_Importe_Item(z,ConTasa) for z in self.sales_data])
        return vTotalC
    # Función para contar el total de artículos
    def count_total_items(self) -> int:
        vListaCount = [x[2] for x in self.sales_data]
        vCount = reduce(lambda x,y: x+y, [z for z in vListaCount])
        return vCount

    def calculate_average_price(self) -> float:
        vTotal = self.funcion_Total_Importe_Items(False)
        vNum = self.count_total_items()
        vMedia = vTotal/vNum
        return vMedia

    def ejecutar(self):
        #vTotalC = reduce(lambda x,y: x+y, [z[1] * z[2] for z in sales_data])
        vCad =''
        vCad +='Informe de Ventas de Gadget Store\n'
        vCad +='Fecha: ' + self.date + '\n'

#Artículo Más Barato: Speaker a EUR99.99
#Artículo Más Caro: Drone a EUR1599.99
        vTotalC = self.funcion_Total_Importe_Items(self.include_tax)

        vMedia = self.calculate_average_price()


        vCad +='Total de Ventas: ' + self.currency + str(vTotalC) + '\n'
        vCad +='Precio Promedio: ' + self.currency + str( round( vMedia,2)) + '\n'
        vCad +='Total de Artículos Vendidos: ' + self.currency + str(self.count_total_items()) + '\n'

        print(vCad)
    #def calculate_total_sales(sales_data: List[Tuple[str, float, int]], include_tax: bool) -> float:
    #    vTotalC = reduce(lambda x,y: x+y, [z[1] * z[2] for z in sales_data])

    #def __init__(self,sales_data: List[Tuple[str, float, int]], include_tax: bool) -> float:        

vSales = [
    ("Phone", 499.99, 10), 
    ("Tablet", 299.99, 5), 
    ("Laptop", 899.99, 3),
    ("Smart Watch", 199.99, 15),
    ("Headphones", 149.99, 20),
    ("Camera", 499.99, 2),
    ("Drone", 1599.99, 1),
    ("Speaker", 99.99, 7),
]

vOBJSales = generate_sales_report("Gadget Store","2023-09-15",vSales,True,"USD")

vF = vOBJSales.funcion_Total_Importe_Item
vAux=vF(["Phone", 499.99, 10],False)
vAux=(["Phone", 499.99, 10])
vOBJSales.ejecutar()
vAux = vOBJSales.count_total_items()
print(vAux)