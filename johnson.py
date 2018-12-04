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
        self.direccional=bool(direccional)
        self.diccionario={}
        self.aristas=[]
        self.cola=[]
    def Bellman_Ford_Johnson(self,origen):
        vec=[ float('inf') for i in range(len(self.vec_nodo))]
        vec[self.diccionario[origen]]=0
        for i in range(len(self.vec_nodo)-1):
            for arista in self.aristas:
                nodo1=arista.get_Inicio().contenido
                nodo2=arista.get_Final().contenido
                if vec[self.diccionario[nodo2]]>vec[self.diccionario[nodo1]]+arista.peso:
                    vec[self.diccionario[nodo2]]=vec[self.diccionario[nodo1]]+arista.peso
        return vec
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
    def Dijsktra(self,grafo,origen):
        inicio=grafo.diccionario[origen]
        distancia=[float('inf') for i in range(len(grafo.vec_nodo))]
        distancia_formal=[float('inf') for i in range(len(grafo.vec_nodo))]
        distancia[inicio]=0
        distancia_formal[inicio]=0
        padre=[-1 for i in range(len(grafo.vec_nodo))]
        self.cola+=[(inicio,distancia[inicio])]
        while len(self.cola)>0:
            self.Ordenar_Dupla()
            v_actual_=self.cola.pop(0)
            v_actual=v_actual_[0]
            for arista in grafo.vec_nodo[v_actual].vec_arista:
                if distancia[grafo.diccionario[arista.get_Final().contenido]]>distancia[v_actual]+arista.peso:
                    distancia[grafo.diccionario[arista.get_Final().contenido]]=distancia[v_actual]+arista.peso
                    padre[grafo.diccionario[arista.get_Final().contenido]]=v_actual
                    self.cola+=[(grafo.diccionario[arista.get_Final().contenido],distancia[grafo.diccionario[arista.get_Final().contenido]])]
                    distancia_formal[grafo.diccionario[arista.get_Final().contenido]]=distancia_formal[v_actual]+self.vec_nodo[v_actual].get_Arista(arista.get_Final().contenido).peso
        return distancia_formal
    def Algoritmo_Johnson(self):
        self.Añadir_Nodos(Nodo('Q'))
        self.diccionario['Q']=len(self.vec_nodo)-1
        for i in range(len(self.vec_nodo)):
            self.Insertar_Aristas('Q',self.vec_nodo[i].contenido,0,'Paso2')
        vec_bellman=self.Bellman_Ford_Johnson('Q')
        grafo2=Grafo("G_Aux",self.direccional)
        for i in range(len(self.vec_nodo)-1):
            grafo2.Añadir_Nodos(Nodo(self.vec_nodo[i].contenido))
        grafo2.diccionario=self.diccionario
        for i in self.aristas:
            if i.nombre!="Paso2":
                peso=i.peso+vec_bellman[self.diccionario[i.get_Inicio().contenido]]-vec_bellman[self.diccionario[i.get_Final().contenido]]
                grafo2.Insertar_Aristas(i.get_Inicio().contenido,i.get_Final().contenido,peso,str(i.nombre))
        matriz_final=[]
        for i in range(len(grafo2.vec_nodo)):
            matriz_final+=[self.Dijsktra(grafo2,grafo2.vec_nodo[i].contenido)]
        print(matriz_final)
    def get_nodo(self,nombre):
        for i in self.vec_nodo:
            if i.contenido==nombre:
                return i
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
                    print("Ya existe conexion")
            else:
                if inicio.Validar_Arista(Inicio,Objetivo)==False and final.Validar_Arista(Objetivo,Inicio)==False:
                    arista_directa1=Arista(inicio,final,Peso,Nombre)
                    arista_directa2=Arista(final,inicio,Peso,Nombre)
                    inicio.Añadir_Arista(arista_directa1)
                    final.Añadir_Arista(arista_directa2)
                    self.aristas+=[arista_directa1,arista_directa2]
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
            
def Crear_Grafo(file_name):
    file=open(file_name,"r")
    linea1=file.readline().split(",")
    name=linea1[0]
    direccional=linea1[1]
    grafo=Grafo(name,int(direccional.split("\n")[0]))
    grafo.Ingresar_Datos(file_name)
    grafo.Algoritmo_Johnson()
    
a=time.time()
Crear_Grafo("Johnson.txt")
b=time.time()
print(b-a)
        
                
        
       
            
            
            
        
        
