f = open("leitura.txt", "r")

string_total = list(f.read())


flag = 0

#flag 0 == aspas fechadas
#flag 1 == aspas abertas

count = 0

string_tratada = list()

string_tratada = string_total.copy()

for c in string_total:
    if (c == '"') and (flag == 1):
        flag = 0

    elif(c == '"') and (flag == 0):
        flag = 1

    elif(c == ",") and (flag == 0):

        string_tratada[count] = ";"
    
    elif(c != ','):
        
        string_tratada[count] = c

    count += 1

string_final = ""

for i in range(len(string_total)):
    string_final += string_tratada[i]


print(string_final)