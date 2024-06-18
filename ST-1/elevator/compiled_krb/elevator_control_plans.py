# elevator_control_plans.py

pyke_version = '1.1.1'
compiler_version = 1

def open_to_enter_action(context, current_floor,where_to,where_waiting):
  print(f"Pessoa a espera no piso {current_floor} com o elevador no piso {current_floor} com a porta fechada")

def open_to_leave_action(context, current_floor,where_to,where_waiting):
  print(f"Pessoa dentro do elevador no piso {current_floor} com o elevador no piso {current_floor} com a porta fechada")

def wait_to_enter_action(context, current_floor,where_to,where_waiting):
  print(f"Pessoa a espera no piso {current_floor} com o elevador no piso {current_floor} com a porta aberta")

def wait_to_leave_action(context, current_floor,where_to,where_waiting):
  print(f"Pessoa dentro do elevador no piso {current_floor} com o elevador no piso {current_floor} com a porta aberta")

def wait_nobody_action(context, current_floor,where_to,where_waiting):
  print("Ninguem dentro do elevador e ninguem a espera")

def up_waiting_action(context, current_floor,where_to,where_waiting):
  print(f"Ninguem dentro do elevador, pessoa a espera no piso {where_waiting}, elevador no piso {current_floor} com a porta fechada")

def up_action(context, current_floor,where_to,where_waiting):
  print(f"Pessoa dentro do elevador no piso {current_floor}, com piso destino {where_to} e elevador com porta fechada")

def down_waiting_action(context, current_floor,where_to,where_waiting):
  print(f"Ninguem dentro do elevador, pessoa a espera no piso {where_waiting}, elevador no piso {current_floor} com a porta fechada")

def down_action(context, current_floor,where_to,where_waiting):
  print(f"Pessoa dentro do elevador no piso {current_floor}, com piso destino {where_to} e elevador com porta fechada")

def close_to_destiny_action(context, current_floor,where_to,where_waiting):
  print(f"Pessoa dentro do elevador no piso {current_floor} e a porta esta aberta")

def close_action(context, current_floor,where_to,where_waiting):
  print(f"Ninguem dentro do elevador, elevador no piso {current_floor} com a porta aberta e pessoa ha espera no piso {where_waiting}")

def close_nobody_action(context, current_floor,where_to,where_waiting):
  print(f"Ninguem dentro do elevador, nao ha ninguem ha espera e o elevador tem a porta aberta")


Krb_filename = '../elevator_control.krb'
