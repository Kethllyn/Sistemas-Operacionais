class PRIOd:
    def __init__(self, id, prioridade, tmp_chegada, tmp_concluir):
        self.id = id
        self.tmp_inicial = 0  # Tempo de relógio em que o processo foi executado a primeira vez
        self.prior_est = prioridade
        self.prior_din = self.prior_est
        self.tmp_chegada = tmp_chegada  # Momento em que o processo foi adicionado na lista
        self.tmp_concluir = tmp_concluir  # Tempo de CPU para concluir


def organizar_inicial(data):
    data.sort(key=lambda x: x.prior_din, reverse=True)
    data.sort(key=lambda x: x.tmp_chegada)
    return data


def organizar_prioridade(data):
    data.sort(key=lambda x: x.prior_din, reverse=True)
    return data


def processar(data_ent):
    quantum = 50
    relogio = 0
    fator_envelhecimento = 1
    data_ready = []  # Processos que entraram na lista de execução
    while True:
        print("\r----------------------")
        print("\rTEMPO DE RELÓGIO: ", relogio)
        if len(data_ent) > 0:
            for q in reversed(data_ent):  # Adiciona as tarefas à fila de acordo com o tempo de chegada, le a lista
                # em ordem inversa para evitar problemas de iteração
                if relogio >= q.tmp_chegada:
                    q.tmp_inicial = relogio
                    data_ready.append(q)
                    data_ent.remove(q)
        elif len(data_ent) <= 0 and len(data_ready) <= 0:
            break

        if len(data_ready) > 0:
            organizar_prioridade(data_ready)
            print("\nProcesso sendo executado: ")
            print("ID: ", data_ready[0].id)
            print("Prioridade Dinâmica: ", data_ready[0].prior_din)
            data_ready[0].tmp_concluir -= quantum
            print("Tempo de CPU para concluir o processo: ", data_ready[0].tmp_concluir)

            # Adiciona o fator de envelhecimento
            for x in data_ready:
                x.prior_din += fator_envelhecimento
            data_ready[0].prior_din = data_ready[0].prior_est

            if data_ready[0].tmp_concluir <= 0:  # Ultima execução de uma tarefa
                print("CONCLUIDO")
                del (data_ready[0])
                # time.sleep(1)
            else:
                data_ready.append(data_ready[0])
                del (data_ready[0])
                # time.sleep(1)

            print("\nLista de prioridades dinâmicas")
            for i in data_ready:
                print("ID: ", i.id)
                print("PD: ", i.prior_din)
                print("\r")
        relogio += quantum


data = []
p1 = PRIOd('p1', 3, 300, 200)
data.append(p1)
p2 = PRIOd('p2', 2, 250, 200)
data.append(p2)
p3 = PRIOd('p3', 5, 100, 200)
data.append(p3)
p4 = PRIOd('p4', 8, 200, 200)
data.append(p4)
p5 = PRIOd('p5', 3, 250, 200)
data.append(p5)
p6 = PRIOd('p6', 1, 150, 200)
data.append(p6)
p7 = PRIOd('p7', 1, 100, 200)
data.append(p7)
p8 = PRIOd('p8', 4, 200, 200)
data.append(p8)
p9 = PRIOd('p9', 6, 300, 200)
data.append(p9)
p0 = PRIOd('p0', 1, 200, 200)
data.append(p0)

new_data = organizar_inicial(data)

processar(data)
