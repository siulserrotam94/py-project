#importar opcion aleatoria
import random

#mientras que algun jugador gane

#FUNCION PARA DEFINIR OPCION USER AND COMPUTER
def choose_options():
  #tuple ambito de la funcion
  options_tuple=('PIEDRA','PAPEL','TIJERA')
  user_option = input('PIEDRA,PAPEL, TIJERA=>')
  user_option= user_option.upper()
  #TRANSFORMACION A MINUSCULAS 
  #user_option= user_option.lower()
  #SI no esta Entre
  
  if not user_option in options_tuple:
    print('esa opcion no es no es valida')
    #continue
    #si la funcion no es valida
    return None, None
  #crear opcion aleatoria con la opciones de la tuple
  computer_option=random.choice(options_tuple)
  #transformacion a mayuscula
  computer_option=computer_option.upper()
  print('user option=>', user_option)
  print('computer option=>', computer_option)
  #retonarla
  return user_option,computer_option

#FUNCION DONDE CORRE LAS REGLAS DEL JUEGO
def check_rules(user_option,computer_option,user_wins,computer_wins):
  if user_option == computer_option:
    print('empate!')
  elif user_option == 'PIEDRA':
    if computer_option=='TIJERA':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins+=1
    else:
      print('papel gana a piedra')
      print('computer game!')
      computer_wins+=1
  elif user_option =='PAPEL':
    if computer_option=='PIEDRA':
      print('papel gana a piedra')
      print('user game!')
      user_wins+=1
    else:
      print('tijera gana a papel')
      print('computer game!')
      computer_wins+=1
  elif user_option =='TIJERA':
    if computer_option=='PAPEL':
      print('tijera gana a papel')
      print('user gano!')
      user_wins+=1
    else:
      print('piedra gana a tijera')
      print('computer game!')
      computer_wins+=1
  return  
#FUNCION QUIEN GANA EL JUEGO
def check_wins(user_wins,computer_wins):
  if user_wins==2:
    print('El usuario es el ganador')
  if computer_wins==2:
    print('El computador es el ganador')
#FUNCION JUEGO PRINCIPAL DONDE INDICA EL ROUND Y LOS PUNTOS
def run_game():
  
  computer_wins=0
  user_wins=0
  rounds=1
  while True:
    print('*'*10)
    print('ROUND', rounds)
    print('*'*10)
  
    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1
    #llamar la funcion
    user_option,computer_option =choose_options()    
    user_wins,computer_wins=check_rules(user_option,computer_option,user_wins,computer_wins)
    check_wins(user_wins,computer_wins)

run_game()