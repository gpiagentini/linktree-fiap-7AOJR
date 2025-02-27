def recebe(hora: str):
    hora = hora.split(":")
    total = 0
    total += int(hora[0]) * 3600
    total += int(hora[1]) * 60
    total += int(hora[2])
    print(total)


recebe('00:10:21')