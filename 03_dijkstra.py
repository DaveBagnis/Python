import math

graph = [[0, 1, 4, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 2, 0, 0],
         [4, 0, 0, 5, 0, 0, 0, 0],
         [0, 0, 5, 0, 1, 3, 0, 0],
         [0, 0, 0, 1, 0, 0, 2, 3],
         [0, 2, 0, 3, 0, 0, 0, 0],
         [0, 0, 0, 0, 2, 0, 0, 4],
         [0, 0, 0, 0, 3, 0, 4, 0]]

labelList = [math.inf] * len(graph)  # inizializzazione delle label (moltiplico per il numero di nodi per le righe)
labelList[0] = 0  # distanza dal nodo sorgente = 0

unexploredNode = [0, 1, 2, 3, 4, 5, 6, 7]  # nodi da esplorare

tempLabel = 0

while len(unexploredNode) > 0:
    print(labelList)
    # scelgo il nodo con label minore(k)
    tempList = [math.inf] * len(graph)
    for i in unexploredNode:
        tempList[i] = labelList[i]  # valore della labelList[i]

    minimun = min(tempList)  # trovo il minimo

    if (minimun == math.inf):  # controllo per uscire dal ciclo
        break

    indexMin = tempList.index(minimun)  # prendo l'indice del valore minimo
    tempLabel += labelList[indexMin]  # sommo per sapere il percorso fatto finora

    for j in unexploredNode:  # ciclo for con ricerca dei nodi collegati a k per indici non ancora esplorati
        if (graph[indexMin][j] != 0):  # verifico che sia collegato e che non sia se stesso
            if (labelList[j] > tempLabel + graph[indexMin][j]):
                labelList[j] = tempLabel + graph[indexMin][
                    j]  # per ogni nuovo nodo sommo (valore label(k)+peso arco di quel nodo) il valore della sua label e controllo se sono minori così sostituisco sennò niente

    unexploredNode.remove(indexMin)  # rimuovo l'indice visitato    