#PROCESSO SELETIVO GRIS/2020
#NOME: LEONARDO ANDRADE
#Cryptopals Set 1 - Challenge 2 

"""Objetivo: Criar uma funcao faca XOR entre duas strings hexadecimais e resulte numa nova string hexadecimal."""

#function -main() - funcao principal para organizacao

def main():

    hex_string1 = '1c0111001f010100061a024b53535009181c'
    hex_string2 = '686974207468652062756c6c277320657965'
    
    bin_hex1 = hexToBin(hex_string1)
    bin_hex2 = hexToBin(hex_string2)
    bin_xor = xor(bin_hex1,bin_hex2)
    result_hex = binToHex(bin_xor)


    print(bin_hex1,'\n')
    print(bin_hex2,'\n')
    print(bin_xor,'\n')
    print(result_hex,'\n')

#function - hexToBin() - primeiro criamos uma funcao que decodifica hexadecimal para binario

def hexToBin(hex_string):

    lista_hex = []

    #formaremos uma lista onde cada elemento dela sera um caracter da string
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

#function - xor() - executa o operador XOR entre os binarios

def xor(bin_string1,bin_string2):
    
    bin_xor = ''
    
    for pos in range (0,len(bin_string1)):

        if (bin_string1[pos] == bin_string2[pos]):
            bin_xor += '0'

        else:
            bin_xor += '1'
   
    return bin_xor

#function - binToHex() - codifica uma string binario para hexadecimal

def binToHex(bin_string):
    
    hex_string = ''
    pos_ini = 0
    pos_fin = len(bin_string)

    while True:

        #Para codificar em hexadecimal, contaremos os bits de 4 em 4. Para tanto faremos um slice.
        binHex_str = bin_string[pos_ini:(pos_ini+4)]

        #Valor do binario em hexadecimal
        valor_hex = str(hex(int(binHex_str,2))[2:])
        hex_string += valor_hex 

        #incremento da variavel posicao inicial para percorrermos 4 bits em 4 bits
        pos_ini += 4

        if (pos_ini == pos_fin):

            #Como nossa string e perfeitamente divisivel por 4, e possivel concluir que essa comparacao pode finalizar o loop com sucesso 
            break

    return hex_string

#######################################################EXECUTANDO O PROGRAMA############################################################

#function -main() - funcao principal para organizacao

def main():

    hex_string1 = '1c0111001f010100061a024b53535009181c'
    hex_string2 = '686974207468652062756c6c277320657965'

    print('String 1: ',hex_string1,'\n')
    print('String 2: ',hex_string2,'\n')
    
    bin_hex1 = hexToBin(hex_string1)  #De hexadecimal para binario
    bin_hex2 = hexToBin(hex_string2)  #De hexadecimal para binario
    bin_xor = xor(bin_hex1,bin_hex2)  #XOR entre as strings binario
    result_hex = binToHex(bin_xor)    #Resultado do XOR em hexadecimal


    print('Resultado hexadecimal do XOR entre as duas: ',result_hex,'\n')

main()
