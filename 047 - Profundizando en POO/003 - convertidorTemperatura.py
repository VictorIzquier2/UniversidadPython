class ConvertidorTemperatura:
  
  MAX_CELSIUS = 100
  MAX_FAHRENHEIT = 213
  
  @classmethod
  def celsius_fahrenheit(cls, celsius):
    if celsius > cls.MAX_CELSIUS:
      raise ValueError(f'Temperatura demasiado alta: {celsius}ºC')
    return celsius * 9/5 + 32
  
  @classmethod
  def fahrenheit_celsius(cls, fahrenheit):
    if fahrenheit > cls.MAX_FAHRENHEIT:
      raise ValueError(f'Temeperatura demasiado alta: {fahrenheit}ºF')
    return (fahrenheit-32) * 5/9
  
if __name__ == '__main__':
  resultado = ConvertidorTemperatura.celsius_fahrenheit(22)
  print(f'22 C a F: {resultado:.2f}')
  resultado = ConvertidorTemperatura.fahrenheit_celsius(10)
  print(f'10 F a C: {resultado:.2f}')
    