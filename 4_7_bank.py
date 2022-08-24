clients = {}
with open('input.txt', 'r') as file_obj:
    for line in file_obj.readlines():
        oper = line.split()
        action = oper[0]
        if action == 'DEPOSIT':
            if oper[1] not in clients:
                clients[oper[1]] = 0
            clients[oper[1]] += int(oper[2])
        elif action == 'WITHDRAW':
            if oper[1] not in clients:
                clients[oper[1]] = 0
            clients[oper[1]] -= int(oper[2])
        elif action == 'BALANCE':
            if oper[1] not in clients:
                print('ERROR')
            else:
                print(clients[oper[1]])
        elif action == 'TRANSFER':
            if oper[1] not in clients:
                clients[oper[1]] = 0
            if oper[2] not in clients:
                clients[oper[2]] = 0
            clients[oper[1]] -= int(oper[3])
            clients[oper[2]] += int(oper[3])
        elif action == 'INCOME':
            p = int(oper[1])
            for key in clients.keys():
                s = clients[key]
                if s > 0:
                    s += int((s*p)/100)
                    clients[key] = s
# print(clients)


