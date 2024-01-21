"""
Flags (Bandeira) - Marca um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condição = True
passou_no_if = None

if condição:
   passou_no_if = True
   print('Falça algo')
else:
  print('Não faça algo')

if passou_no_if is None:
  print('Não passou no if')

if passou_no_if is not None:
  print('passou na if')