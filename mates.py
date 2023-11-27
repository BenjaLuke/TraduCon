import math                         
    
def redondea(valor,decimales):     
                                                                                                                 
    valor_final = math.ceil(valor) if valor - int(valor) >= 0.00001 else math.floor(valor)                                                          
    if decimales == 0: return int(valor_final)                                                                                                  
    else: return round(valor,decimales)                                                                                                         