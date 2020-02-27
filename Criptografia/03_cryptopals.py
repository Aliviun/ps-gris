#PROCESSO SELETIVO GRIS/2020
#NOME: LEONARDO ANDRADE
#Cryptopals Set 1 - Challenge 3 

"""Objetivo: Decriptar uma mensagem gerada a partir de um XOR entre uma chave desconhecida e uma string hexadecimal"""

#function - hexToBin() - primeiro criamos uma funcao que decodifica hexadecimal para binario

def hexToBin(hex_string='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'):

    lista_hex = []

    #formaremos uma lista onde cada elemento dela sera um caracter da string hexadecimal
    for char in hex_string:
        lista_hex += char

    #Convertendo de hexa para binario...
    
    bin_string = ''

    #primeiro "for" que sinaliza um elemento numa posicao
    for pos in range (0,len(lista_hex)):

        #"for" que compara com os primeiros 10 naturais
        for cont_1 in range (0,10):

            if lista_hex[pos] == str(cont_1):
                valor_num = lista_hex[pos]
                
                #a semelhanca sendo verificada, transformaremos o valor em binario
                #O 16 e para definirmos a escala hexadecimal
                #zfill() definira o numero de bits
                
                bin_string += bin(int(valor_num, 16))[2:].zfill(4)
                break

        char=['a','b','c','d','e','f']

        #"for" para as letras de "a" a "f"
        for cont_2 in char:
          if lista_hex[pos] == cont_2:
                valor_alfa = lista_hex[pos]

                #comparacao sendo true, transformaremos o valor em binario
                bin_string += bin(int(valor_alfa, 16))[2:].zfill(4)

                break

    return bin_string

#function - binToAscii() - Recebe uma string em binario e decodifica usando a tabela ASCII

def binToAscii(list_bin):
    
    message = ''
    
    #Aqui esta nossa tabela ascii com valores validos
    tab_ascii={'!':33,'"':34,'#':35,'$':36,'%':37,'&':38,"'":39,'(':40,')':41,'*':42,'+':43,',':44,'-':45,'.':46,'/':47,'0':48,'1':49,'2':50,'3':51,'4':52,'5':53,'6':54,'7':55,'8':56,'9':57,':':58,';':59,'<':60,'=':61,'>':62,'?':63,'@':64,'A':65,'B':66,'C':67,'D':68,'E':69,'F':70,'G':71,'H':72,'I':73,'J':74,'K':75,'L':76,'M':77,'N':78,'O':79,'P':80,'Q':81,'R':82,'S':83,'T':84,'U':85,'V':86,'W':87,'X':88,'Y':89,'Z':90,'[':91,'\\':92,']':93,'^':94,'_':95,'`':96,'a':97,'b':98,'c':99,'d':100,'e':101,'f':102,'g':103,'h':104,'i':105,'j':106,'k':107,'l':108,'m':109,'n':110,'o':111,'p':112,'q':113,'r':114,'s':115,'t':116,'u':117,'v':118,'w':119,'x':120,'y':121,'z':122,'{':123,'|':124,'}':125,'~':126}
    
    for index in range (0,len(list_bin)):
        decimal_ascii = int(list_bin[index],2)

        for key in tab_ascii:
            
            if decimal_ascii == tab_ascii[key]:
                message += key

    return message

#function - xor() - executa o operador XOR entre os binarios

def xor(possivel_chave,lista_bin):

    bin_xor = ''

    for pos_lista in range(0,len(lista_bin)):
        for pos_str in range (0,8):
            
            if (lista_bin[pos_lista][pos_str] == possivel_chave[pos_str]):
                bin_xor += '0'

            else:
                bin_xor += '1'

    return bin_xor

#function - listar_bytes() - recebe uma string binario e retorna uma lista separando byte a byte

def listar_bytes(string_bin):

    lista_bin = []
    pos_ini = 0
    pos_fin = len(string_bin)

    while True:

        #Para separarmos os bytes, contaremos os bits de 8 em 8. Para tanto faremos um slice.
        elem_byte = string_bin[pos_ini:(pos_ini+8)]

        lista_bin += [elem_byte]

        #incremento da variavel posicao inicial para percorrermos 8 bits em 8 bits
        pos_ini += 8

        if (pos_ini == pos_fin):

            #Como nossa string e perfeitamente divisivel por 8, e possivel concluir que essa comparacao pode finalizar o loop com sucesso 
            break

    return lista_bin

#function - verificador() - verifica os caracteres nao muito utilizados na escrita inglesa

def verificador(message):

    result = False

    charac_ilegiv = ['"','#','$','%','&','(',')','*','+','/','@','`',']','\\','[','^','~','_','{','}','<','>','=','|',';']

    for carac in message:
        for char in charac_ilegiv:

            if carac == char:
                result = True
                break
                 
        if result == True:
            break

    return result


#function - main() - funcao principal para organizacao do programa

def main():
    
    #Transformando a string hexa para binario, e depois fazemos uma lista de bytes
    string_bin = hexToBin()
    bytes_list = listar_bytes(string_bin)
    
    #Tentando as chaves possiveis da tabela ASCII
    for ascii_decimal in range (33,127):
        poss_chaveBin = str(bin(ascii_decimal)[2:].zfill(8))
        
        #Fazemos o XOR da chave com cada elemento da lista de bytes, o resultado tambem colocaremos numa lista organizada
        bin_xor = xor(poss_chaveBin,bytes_list)
        list_xor = listar_bytes(bin_xor)
        
        #Decodificamos a mensagem em binario para ASCII
        message = binToAscii(list_xor)
        
        inelegivel = verificador(message)
        if inelegivel == False:
            print('Essa pode ser sua mensagem: ',message,'\n')

main()
