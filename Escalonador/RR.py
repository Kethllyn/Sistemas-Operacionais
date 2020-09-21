class RoundRobin:
    def __init__(self, id, tmp_chegada, tmp_concluir):
        self.id = id
        self.tmp_chegada = tmp_chegada #Momento em que o processo foi adicionado na lista
        self.tmp_concluir = tmp_concluir #Tempo de CPU para concluir
        self.concluido = False


def organizar(data):
    organizado = sorted(data, key=lambda x: x.tmp_chegada)
    return organizado

def processar(new_data):
    quantum = 0.25
    while len(new_data) > 0:
        print("\nProcesso sendo executado: ")
        print("ID: ", new_data[0].id)
        new_data[0].tmp_concluir -= quantum
        print("Tempo de CPU para concluir o processo: ", new_data[0].tmp_concluir)
        if new_data[0].tmp_concluir <= 0:
            print("CONCLUIDO")
            del (new_data[0])
            #time.sleep(1)
        else:
            new_data.append(new_data[0])
            del (new_data[0])
            #time.sleep(1)


data = []
#todos os processos entram como 3ms no tempo pra concluir
p1 = RoundRobin('p1', 300, 3)
data.append(p1)
p2 = RoundRobin('p2', 250, 3)
data.append(p2)
p3 = RoundRobin('p3', 100, 3)
data.append(p3)
p4 = RoundRobin('p4', 200, 3)
data.append(p4)
p5 = RoundRobin('p5', 250, 3)
data.append(p5)
p6 = RoundRobin('p6', 150, 3)
data.append(p6)
p7 = RoundRobin('p7', 100, 3)
data.append(p7)
p8 = RoundRobin('p8', 200, 3)
data.append(p8)
p9 = RoundRobin('p9', 300, 3)
data.append(p9)
p0 = RoundRobin('p0', 200, 3)
data.append(p0)

new_data = organizar(data)

print("\nPROCESSANDO\n")
processar(new_data)
