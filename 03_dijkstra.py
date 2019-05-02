import math     #importiamo libreria math per l'infinito

graph = [
    [0,3,0,4],      #matrice di adiacenza con 4 nodi pesati
    [3,0,1,5],
    [0,1,0,2],
    [4,5,2,0]]

source = 0
nodeNumber = len(graph)     #lunghezza del grafo = numero di liste = numero di nodi = 4

labelList = [math.inf for i in range(nodeNumber)]       #tutti i nodi del grafo hanno distanza infinito per ora
labelList[source] = 0       #distanza da source a se stesso = 0 -> [0,infinito,infinito,infinito]

unexploredNodes = [i for i in range(nodeNumber)]        #nodi da esplorare

#si parte dal nodo sorgente perchè ha sempre la label più piccola di tutti = 0
while len(unexploredNodes)>0:
    
    print(unexploredNodes)

    minLabel = min([labelList[node] for node in unexploredNodes])       #minLabel = il valore minimo di quelli che ci sono nella lista dei nodi non esplorati, al primo giro è 0 cioè quella di source

    for i in unexploredNodes:
        if labelList[i] == minLabel:
            currentNode = i
        else:
            break

    print(currentNode)
    unexploredNodes.remove(currentNode)     #togliere il nodo esplorato dalla lista dei nodi non esplorati (gli passiamo l'indice del nodo corrente)

    for neighbourNode,weight in enumerate(graph[currentNode]):      #cicliamo sulla riga del current node del grafo
        if weight>0:
            distance = labelList[currentNode]+weight        #distance = distanza del nodo corrente + il peso
            if(distance<labelList[neighbourNode]):      #se la distanza < del peso del nodo vicino
                labelList[neighbourNode]=distance       #distanza del nodo vicino = distance

print(labelList)  
