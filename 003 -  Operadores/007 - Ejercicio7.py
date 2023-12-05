# Puede asistir al juego de su hijo

vacaciones = True
diaDescanso = True

def padreAsistira(vacaciones: bool, descanso: bool):
  if (vacaciones or descanso):
    print("Puede asistir al juego de su hijo.")
  else:
    print("No puede asistir al juego de su hijo.")

padreAsistira(vacaciones, diaDescanso)