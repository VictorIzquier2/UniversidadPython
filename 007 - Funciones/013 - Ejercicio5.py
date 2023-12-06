def celsius_a_farenheit():
  celsius = float(input('Introduzca la temperatura en grados C: '))
  farenheit: float = (celsius * 1.8) + 32
  print(f"{celsius}ºC son {farenheit}ºF")
  
def farenheit_a_celsius():
  farenheit = float(input('Introduzca la temperatura en grados F: '))
  celsius: float = (farenheit - 32) / 1.8
  print(f"{farenheit}ºF son {celsius}ºC")
  

celsius_a_farenheit()
farenheit_a_celsius()
  