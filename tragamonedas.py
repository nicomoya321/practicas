import random

MAX_LINES= 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
colum = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

def slots_giratorios(rows , colum , symbols):
    todos_symbols =[]
    for symbol , symbol_count in symbols.items():
        for _ in range(symbol_count):
            todos_symbols.append(symbol)
    columns =[[],[],[]]
    for _ in range (colum):
        colum = []
    current_symbols = current_symbols[:]
    for row in range (ROWS):
        value = random.choice(current_symbols)
        current_symbols.remove(value)
        colum.append(value)
        
        columns.append(colum)
    return columns

def print_slot_machine(columns):
    for ROW in range(len(columns[0])):
        for i, colum in enumerate(columns):
            if i != len(columns) - 1:
                print(colum[ROW], end = " |")
            else:
                print(colum[ROW], end =" ")
                
print()

        
        
                   

def depositos():
    monto = input("ingrese numero de lineas que quiere apostar(1 -" + str(MAX_LINES)+")?")
    while True:
        monto = input("cuanto desea ingresar ?")
        if monto.isdigit():
            monto= int(monto)
            if monto > 0:
                break
            else:
                print("ingrese un monto valido")
        else:
            print("ingrese un numero")     
            
    return monto



def numero_de_lineas():
    lineas = input("ingrese numero de lineas que quiere apostar(1 -" + str(MAX_LINES)+")?")
    while True:
        lineas = input("cuanto desea ingresar ?")
        if lineas.isdigit():
            lineas= int(lineas)
            if 1 <= lineas >= MAX_LINES:
                break
            else:
                print("Iingrese un numero valido de lineas")
        else:
            print("ingrese un numero")     
            
    return lineas

def recibir_apuesta():
    monto = input("ingrese numero de lineas que quiere apostar(1 -" + str(MAX_LINES)+")?")
    while True:
        monto = input("cuanto desea ingresar ?")
        if monto.isdigit():
            monto= int(monto)
            if MIN_BET <= monto <= MAX_BET:
                break
            else:
                print(f"el monto debe estar entre ${MIN_BET} - ${MAX_BET}.")
        else:
            print("ingrese un numero")     
            
    return monto




def main():
    balance = depositos()
    lineas = numero_de_lineas()
    
    while True:
        apuesta = recibir_apuesta()
        apuesta_total = apuesta * lineas
        
        if apuesta_total > balance:
            print(f"no tienes saldo para apostar , tu saldo actual es : ${balance}")
        else:
            break

slots= slots_giratorios = (ROWS,colum,symbol_count)
print_slot_machine(slots)

main()