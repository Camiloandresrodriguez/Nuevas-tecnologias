ingreso_mensual =2500000
gastos_mensuales = 4000000

if ingreso_mensual > 2000000:
    if ingreso_mensual - gastos_mensuales < 0:
        print('estas arruinado')
    elif ingreso_mensual-gastos_mensuales > 800000:
        print('aun alcanza para los demas gastos, pero debes tener cuidado de o gastar mas ')
    else:
        print('estas gastando de mas, tienes que reeplantear tud gastos.')
        
elif ingreso_mensual >= 2500000:
    print('es equilibrado a lo que ganas')
    
elif ingreso_mensual >= 2000000:
    print('estas bien en colombia')
    
else:
    print('no te alcanza para subsistir')