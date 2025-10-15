
var1 = 123
var2 = 'Mundo!'

print("Olá", var2, var1)

print("Olá %s %d" %(var2, var1))

"""
Quando o Python foi criado, ele herdou vários formatos de string interpolation do printf do C.
Olha só como funciona:

%s -> string (s vem de string)

%d -> decimal integer (d vem de decimal, não de integer)

%i -> também existe, e significa integer (mas %d é mais usado por tradição do C)

"""
print("Olá {} {}" .format(var2,var1))
print("Olá "+ var2 + " " +str(var1))
print(f"Olá {var2} {var1}")