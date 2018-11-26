import time
class Nodo:
    def __init__(self,Contenido):
        self.contenido=Contenido
        self.vec_arista=[]
    def Añadir_Arista(self,arista):
        self.vec_arista+=[arista]
    def Validar_Arista(self,Inicio,Objetivo):
        for i in self.vec_arista:
            if i.get_Inicio().contenido==Inicio and i.get_Final().contenido==Objetivo:
                return True
        return False
    def get_Arista(self,objetivo):
        for i in self.vec_arista:
            if i.get_Final().contenido==objetivo:
                return i
    def Imprimir_Aristas(self):
        for i in self.vec_arista:
            print(i.nombre,self.contenido)
class Arista:
    def __init__(self,Inicio,Objetivo,Peso,Nombre):
        self.vec_nodos=[Inicio,Objetivo]
        self.peso=int(Peso)
        self.nombre=Nombre
    def get_Inicio(self):
        return self.vec_nodos[0]
    def get_Final(self):
        return self.vec_nodos[1]
class Grafo:
    def __init__(self,nombre,direccional):
        self.vec_nodo=[]
        self.nombre=nombre
        self.vec_etapa=[]
        self.direccional=bool(direccional)
        self.diccionario={}
        self.cola=[]
        self.aristas=[]
        self.flujo_maximo=[]
    def get_nodo(self,nombre):
        for i in self.vec_nodo:
            if i.contenido==nombre:
                return i
    def Ordenar_Dupla(self):
        self.quicksort(0,len(self.cola)-1)
    def quicksort(self,inicio,fin):
        if inicio<fin:
            split=self.sub_arrays(inicio,fin)
            self.quicksort(inicio,split-1)
            self.quicksort(split+1,fin)
    def sub_arrays(self,inicio,fin):
        pivot=self.cola[fin][1]
        ptr_principal=inicio
        ptr_secundario=inicio
        while ptr_secundario<fin:
            if self.cola[ptr_secundario][1]<pivot:
                self.cola[ptr_principal],self.cola[ptr_secundario]=self.cola[ptr_secundario],self.cola[ptr_principal]
                ptr_principal+=1
                ptr_secundario+=1
            else:
                ptr_secundario+=1
        self.cola[ptr_principal],self.cola[fin]=self.cola[ptr_secundario],self.cola[ptr_principal]
        return ptr_principal
    def aux_Ford(self,nodo_actual,padre,capacidad_min,k_min):
        if k_min:
            while padre[nodo_actual]!=-1:
                    aux=self.vec_nodo[padre[nodo_actual]].get_Arista(self.vec_nodo[nodo_actual].contenido).peso
                    if capacidad_min>aux:
                        capacidad_min=aux
                    nodo_actual=padre[nodo_actual]
            return capacidad_min
        else:
            while padre[nodo_actual]!=-1:
                self.vec_nodo[padre[nodo_actual]].get_Arista(self.vec_nodo[nodo_actual].contenido).peso-=capacidad_min
                self.vec_nodo[nodo_actual].get_Arista(self.vec_nodo[padre[nodo_actual]].contenido).peso+=capacidad_min
                nodo_actual=padre[nodo_actual]
            return True
            
    def Dijsktra_Fulkerson(self,fuente,sumidero):
        inicio=self.diccionario[fuente]
        distancia=[float('inf') for i in range(len(self.vec_nodo))]
        distancia[inicio]=0
        padre=[-1 for i in range(len(self.vec_nodo))]
        self.cola+=[(inicio,distancia[inicio])]
        while len(self.cola)>0:
            self.Ordenar_Dupla()
            v_actual_=self.cola.pop(0)
            v_actual=v_actual_[0]
            for arista in self.vec_nodo[v_actual].vec_arista:
                if arista.peso>0:
                    if distancia[self.diccionario[arista.get_Final().contenido]]>distancia[v_actual]+arista.peso:
                        distancia[self.diccionario[arista.get_Final().contenido]]=distancia[v_actual]+arista.peso
                        padre[self.diccionario[arista.get_Final().contenido]]=v_actual
                        self.cola+=[(self.diccionario[arista.get_Final().contenido],distancia[v_actual]+arista.peso)]
        if float('inf')!=distancia[self.diccionario[sumidero]]:
            nodo_actual=self.diccionario[sumidero]
            capacidad_min=self.aux_Ford(nodo_actual,padre,float('inf'),True)
            self.flujo_maximo+=[capacidad_min]
            return self.aux_Ford(nodo_actual,padre,capacidad_min,False)
            
        else:
            return False
    def Fulkerson(self,fuente,sumidero):
        while self.Dijsktra_Fulkerson(fuente,sumidero):
            print("Ejecutando Dijsktra")
        fin=self.diccionario[sumidero]
        flujo_maximo=0
        for i in self.flujo_maximo:
            flujo_maximo+=i
        for i in self.vec_nodo[0].vec_arista:
            i.get_Final().get_Arista(self.vec_nodo[0].contenido).peso
        print(flujo_maximo)   
    def Añadir_Nodos(self,Nodo):
        self.vec_nodo+=[Nodo]
    def Insertar_Aristas(self,Inicio,Objetivo,Peso,Nombre):
        inicio=self.get_nodo(Inicio)
        final=self.get_nodo(Objetivo)
        if inicio!=None and final!=None:
            if self.direccional==True:
                if inicio.Validar_Arista(Inicio,Objetivo)==False:
                    arista_directa=Arista(inicio,final,Peso,Nombre)
                    inicio.Añadir_Arista(arista_directa)
                    self.aristas+=[arista_directa]
                else:
                    """print("Ya existe conexion")"""
            else:
                if inicio.Validar_Arista(Inicio,Objetivo)==False and final.Validar_Arista(Objetivo,Inicio)==False:
                    inicio.Añadir_Arista(Arista(inicio,final,Peso,Nombre))
                    final.Añadir_Arista(Arista(final,inicio,Peso,Nombre))
                else:
                    print("Ya existe conexion")
        else:
            print("No existen tales nodos")
    def Ingresar_Datos(self,file_name):
        with open(file_name) as file:
            for i,line in enumerate(file):
                cont=0
                if i==0:
                    continue
                if i==1:
                    for palabra in line.split(","):
                        self.Añadir_Nodos(Nodo(palabra.split("\n")[0]))
                        cont+=1
                    continue
                origen=0
                final=0
                peso=0
                edge_name=0
                for palabra in line.split(","):
                    cont+=1
                    if cont==1:
                        origen=palabra
                    if cont==2:
                        final=palabra
                    if cont==3:
                        peso=palabra
                    if cont==4:
                        edge_name=palabra.split("\n")[0]
                self.Insertar_Aristas(origen,final,peso,edge_name)
            file.close()
        for i in range(len(self.vec_nodo)):
            self.diccionario[self.vec_nodo[i].contenido]=i
        for i in self.aristas:
            self.Insertar_Aristas(i.get_Final().contenido,i.get_Inicio().contenido,"0",i.nombre)
            
def Crear_Grafo(file_name):
    file=open(file_name,"r")
    linea1=file.readline().split(",")
    name=linea1[0]
    direccional=linea1[1]
    grafo=Grafo(name,int(direccional.split("\n")[0]))
    grafo.Ingresar_Datos(file_name)
    grafo.Fulkerson("s","t")
    
a=time.time()
Crear_Grafo("Fulkerson.txt")
b=time.time()
print(b-a)
        
                
        
       
            
            
            
        
        
