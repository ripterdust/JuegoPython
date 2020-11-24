from pokemon import Pokemon, showStats, attack
# Primero se pasa la vida y después el poder.
print('Este es un juego de lucha de Pokemones')
pikachu = Pokemon(100, 50, 'Pikachu')
charizard = Pokemon(100, 20, 'Charizard')

contador = 0
# ciclo que va a hacerlos pelear
while pikachu.health > 0 and charizard.health > 0:
   # Esto muestra las estadísticas de los pokemones 
    showStats(pikachu, charizard)
    
    if contador == 0:
        # turno de pikachu
        attack(charizard, pikachu) 
        contador = 1
    else:
        # turno de charizard
        attack(pikachu, charizard)
        contador = 0

    # Imrpimiendo quién ganó
    if pikachu.health <= 0:
        print('Ha ganado Charizard')
    elif charizard.health <= 0:
        print('Ha ganado Pikachu')

print('Gracias por utilizar el programa')
