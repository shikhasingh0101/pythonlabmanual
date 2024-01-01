# main.py
# from  cars import BMW, AUDI, NISSAN

# bmw_car = BMW.BMW("X5")
# audi_car = AUDI.AUDI("A3")
# nissan_car = NISSAN.NISSAN("Altima")

# bmw_car.display_model()
# bmw_car.start_engine()

# audi_car.display_model()
# audi_car.start_engine()

# nissan_car.display_model()
# nissan_car.start_engine()
from BMW import BMW  
from AUDI import AUDI
from NISSAN import  NISSAN  

bmw = BMW("M3", "blue") 
audi = AUDI("A5", 354)
nissan = NISSAN("Sentra", "hybrid")


bmw.start_engine()
bmw.display_model()
audi.start_engine()
audi.display_model()
nissan.start_engine()
nissan.display_model()
