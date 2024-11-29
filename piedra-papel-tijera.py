jugador1 = input("Hola ¡jugador1! , ¿Que eliges?, ¿Piedra, Papel o Tijera?")
jugador2 = input("Hola ¡jugador1! , ¿Que eliges?, ¿Piedra, Papel o Tijera?")

if jugador1 == jugador2:
    print("¡Ha sido un empate!")
elif (jugador1 == "piedra" and jugador2 == "Tijera=") or (jugador1 =="Papel" and jugador2 =="Piedra") or (jugador1 == "Tijera" and jugador2 == "Papel"):
    print("Ha ganado el jugador 1")
else:
    print("Ha ganado el jugador 2")
    