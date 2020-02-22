def arkademy(inpt):
    output=""
    if (type(inpt) is not int):
        return print("Input harus angka!")
    
    for k in range(inpt):
        if ((k+1) % 3 == 0) and ((k+1) % 7 == 0):
            output = output + "Arkademy"
        elif ((k+1) % 3 == 0):
            output = output + "Arka"
        elif ((k+1) % 7 == 0):
            output = output + "Demy"
        else:
            output = output + str(k+1)
            
        if ((k+1) != inpt):
            output = output + ", "

    return print(output)
        
inpt = input("Masukkan angka : ")
inpt = int(inpt)
arkademy(inpt)