def solution(players, m, k):
    result = 0
    capa = m
    servers = [] 
    n = 0
    for p in players:
        if p >= capa:
            need = p // m - len(servers)
            servers += [k] * need
            result += need
        for i in range(len(servers)):
            servers[i] -= 1
        servers = [ s for s in servers if s != 0 ]
        capa = (len(servers) + 1) * m
    return result