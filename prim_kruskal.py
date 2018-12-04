import random
class Node:
    def __init__(self,name):
        self.n_nodo=name
        self.aristas=[]
    def add_aristas(self,arista):
        self.aristas.append(arista)
class Edge:
    def __init__(self,peso,nodo1,nodo2,edge_name):
        self.peso=peso
        self.conexion=[]
        self.conexion.append(nodo1)
        self.conexion.append(nodo2)
        self.edge_name=edge_name
class UFDS:
    def __init__(self,grafo):
        self.ufds=[]
        self.dicc_nodo={}
        self.grafo=grafo
        self.kruskal=[]
    def generar_ufds(self,vec_nodo):
        for i in range(len(vec_nodo)):
            self.dicc_nodo[vec_nodo[i].n_nodo]=[i]
            self.ufds.append(-1)
    def find(self,i):
        if self.ufds[i]==-1:
            return i
        else:
            return self.find(self.ufds[i])
    def union(self,x,y):
        x1 = self.find(x)
        y2 = self.find(y)
        if x1!=y2:
            self.ufds[x1] = y2
    def generar_kruskal(self,vec_aristas):
        for j in vec_aristas:
            x = self.find(self.dicc_nodo[j.conexion[0]][0])
            y = self.find(self.dicc_nodo[j.conexion[1]][0])
            if x == y:
                continue
            self.union(x,y)
            self.kruskal+=[j.edge_name]
    def reset(self):
        for i in range(len(self.ufds)):
            self.ufds[i]=-1
    def Print_sets(self):
        aux=[]
        dicc_nodo2={}
        dicc_nodo_inv={}
        cont=0
        for key,value in self.dicc_nodo.items():
            
            dicc_nodo_inv[value[0]]=key
        for i in range(len(self.ufds)):
            if self.ufds[i]==-1:
                dicc_nodo2[i]=cont
                aux+=[dicc_nodo_inv[i]]
                cont+=1
        for i in range(len(self.ufds)):
            if self.ufds[i]!=-1:
                aux[dicc_nodo2[self.ufds[i]]]+=dicc_nodo_inv[i]
        print(aux)
                
    
class Graph:
    def __init__(self,nombre,dirigido):
        self.nombre=nombre;
        self.vec_nodo=[]
        self.dirigido=dirigido
        self.arbol_prim=0
        self.ufds=0
        self.vec_aristas=[]
    def quicksort(self):
        self.quicksort_2(0,len(self.vec_aristas)-1)
    def quicksort_2(self,inicio,fin):
        if inicio<fin:
            splitpoint=self.particion(inicio,fin)
            self.quicksort_2(inicio,splitpoint-1)
            self.quicksort_2(splitpoint+1,fin)
    def particion(self,inicio,fin):
        pivot=self.vec_aristas[fin].peso
        puntero_principal=inicio
        puntero_secundario=inicio
        while puntero_secundario<fin:
            if self.vec_aristas[puntero_secundario].peso<pivot:
                self.vec_aristas[puntero_principal],self.vec_aristas[puntero_secundario]=self.vec_aristas[puntero_secundario],self.vec_aristas[puntero_principal]
                puntero_principal+=1
                puntero_secundario+=1
            else:
                puntero_secundario+=1
        self.vec_aristas[puntero_principal],self.vec_aristas[fin]=self.vec_aristas[fin],self.vec_aristas[puntero_principal]
        
        return puntero_principal
    def generate_ufds(self,grafo):
        self.ufds=UFDS(grafo)
        self.ufds.generar_ufds(grafo.vec_nodo)
        self.quicksort()
        self.ufds.generar_kruskal(self.vec_aristas)
        print(str("Kruskal\n"),self.ufds.kruskal)
    def dfs_principal(self,nodo,representantes):
        aux=[]
        for i in representantes:
            aux+=[(self.dfs(nodo,i,[]),i)]
        minimo=aux[0]
        for i in aux:
            if minimo[0]>i[0]:
                minimo=i
        return minimo[1]
    def dfs(self,nodo,representante,visitados):
        if nodo==representante:
            return 0
        else:
            actual=self.arbol_prim.get_node(nodo)
            visitados.append(nodo)
            for aristas in actual.aristas:
                if not aristas.conexion[1] in visitados:
                    a=self.dfs(aristas.conexion[1],representante,visitados)
                    if type(a)==int:
                        return a+int(aristas.peso)

                
            
    def read(self,file_name):
        with open(file_name) as file:
            for i,line in enumerate(file):
                cont=0
                if i<1:
                    for palabra in line.split(","):
                        nodito=Node(palabra.split("\n")[0])
                        self.add_node(nodito)
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
                if origen!="\n":
                    a=Edge(peso,origen,final,edge_name)
                    self.get_node(origen).add_aristas(a)
                    self.vec_aristas.append(a)
                    self.get_node(final).add_aristas(Edge(peso,final,origen,edge_name))
        file.close()
    def add_node(self,nodo):
        self.vec_nodo.append(nodo)
    def get_node(self,nombre_nodo):
        for i in self.vec_nodo:
            if i.n_nodo==nombre_nodo:
                return i
    def imprimir_conexiones(self):
        print(self.nombre)
        for i in self.vec_nodo:
            for arista in i.aristas:
                print(i.n_nodo+str("-> ")+arista.conexion[1]+" "+arista.edge_name)
    def ordenar_aristas(self,vec_aristas):
        for i in range(len(vec_aristas)-1,0,-1):
            for j in range(i):
                if vec_aristas[j].peso>vec_aristas[j+1].peso:
                    vec_aristas[j],vec_aristas[j+1]=vec_aristas[j+1],vec_aristas[j]
                
    def Prim(self,origen):
        no_visitados=[]
        for i in self.vec_nodo:
            no_visitados.append(i.n_nodo)
        vec_aristas=[]
        nodo_actual=origen
        arbol_exp=[]
        while len(no_visitados)>1:
            for arista in self.get_node(nodo_actual).aristas:
                if arista.conexion[1] in no_visitados:
                    vec_aristas.append(arista)
            self.ordenar_aristas(vec_aristas)
            arbol_exp.append(vec_aristas[0])
            no_visitados.remove(nodo_actual)
            nodo_actual=vec_aristas[0].conexion[1]
            vec_aristas.pop(0)
        self.arbol_prim=Graph("Prim",self.dirigido)
        for i in range(6):
            nodito=Node(chr(i+65))
            self.arbol_prim.add_node(nodito)
        for i in arbol_exp:
            self.arbol_prim.get_node(i.conexion[0]).add_aristas(i)
            self.arbol_prim.get_node(i.conexion[1]).add_aristas(Edge(i.peso,i.conexion[1],i.conexion[0],i.edge_name))
    def Clustering(self,k):
        aux=[]
        random.shuffle(self.vec_nodo)
        aux=self.vec_nodo
        representantes=[]
        for i in range(0,k):
            representantes.append(aux[i].n_nodo)
        print(representantes)
        del aux[0:k]
        self.ufds.reset()
        for i in aux:
            elegido=self.dfs_principal(i.n_nodo,representantes)
            print(elegido,i.n_nodo)
            self.ufds.union(self.ufds.dicc_nodo[i.n_nodo][0]
                            ,self.ufds.dicc_nodo[elegido][0])
        print(self.ufds.ufds)
        self.ufds.Print_sets()
        
        
    
grafo=Graph("Grafo",0)
grafo.read("conexiones.txt")
grafo.imprimir_conexiones()
grafo.Prim("A")
print("\n")
grafo.arbol_prim.imprimir_conexiones()
grafo.generate_ufds(grafo)
a=input("Ingrese numero de clusters:")
grafo.Clustering(int(a))




    
