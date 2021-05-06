def ping_pong(lst, win):
    res = ['Ping!', 'Pong!'] * len(lst)
    return res if win else res[:-1]

print(ping_pong(["Ping!"], True))
print(ping_pong(["Ping!", "Ping!"], False)) 
print(ping_pong(["Ping!", "Ping!", "Ping!"], True)) 