#PROCESSO SELETIVO GRIS/2020
#NOME: LEONARDO ANDRADE
#Cryptopals Set 1 - Challenge 1 

"""Objetivo: Criar uma funcao que converte uma string hex para base64."""

#function - hexToBin() - primeiro criamos uma funcao que decodifica hexadecimal para binario

def hexToBin(hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'):
    
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
    
    #Perceba que fomos concatenando as strings ao nosso "bin_string" a cada 4 bits

    #Agora vamos pegar nossa string em binario e codifica-la para base64
    base64_string = ''
    pos_ini = 0
    pos_fin = len(bin_string)
    
    #tabela base64
    tab_bs64={'A': 0, 'Q': 16, 'g': 32, 'w': 48,
              'B': 1, 'R': 17, 'h': 33, 'x': 49,
              'C': 2, 'S': 18, 'i': 34, 'y': 50,
              'D': 3, 'T': 19, 'j': 35, 'z': 51,
              'E': 4, 'U': 20, 'k': 36, '0': 52,
              'F': 5, 'V': 21, 'l': 37, '1': 53,
              'G': 6, 'W': 22, 'm': 38, '2': 54,
              'H': 7, 'X': 23, 'n': 39, '3': 55,
              'I': 8, 'Y': 24, 'o': 40, '4': 56,
              'J': 9, 'Z': 25, 'p': 41, '5': 57,
              'K': 10, 'a': 26, 'q': 42, '6': 58,
              'L': 11, 'b': 27, 'r': 43, '7': 59,
              'M': 12, 'c': 28, 's': 44, '8': 60,
              'N': 13, 'd': 29, 't': 45, '9': 61,
              'O': 14, 'e': 30, 'u': 46, '+': 62,
              'P': 15, 'f': 31, 'v': 47, '/': 63}
    
    while True:
        
        #Para codificar em base64, contaremos os bits de 6 em 6. Para tanto faremos um slice.
        bin64_str = bin_string[pos_ini:(pos_ini+6)]
        
        #Valor do binario em decimal, nesse caso em base64
        valor_b64 = str(int(bin64_str,2))

        for key in tab_bs64:
            
            if (str(tab_bs64[key]) == valor_b64):
                
                #Fazendo a comparacao do valor da string com o do dicionario, sendo true, adicionaremos a chave ao nosso codigo b64
                base64_string += key
        
        #incremento da variavel posicao inicial para pularmos 6 bits em 6 bits
        pos_ini += 6
        
        if (pos_ini == pos_fin):
            
            #Como nossa string nao necessita de padding, e possivel concluir que essa comparacao pode finalizar o loop com sucesso 
            break

    return base64_string

#####################################################EXECUTANDO O PROGRAMA######################################################

string_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print('A string em hexadecimal: ',string_hex)
print('A string em base64: ',hexToBin(),'\n')
