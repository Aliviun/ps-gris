//PROCESSO SELETIVO GRIS-2020
//NOME: LEONARDO ANDRADE
//TAG: PORTSCANNER EM GO

"""O objetivo desta TAG de Go era criar um scanner de portas TCP/UDP para verificar 
   o status de cada uma delas, se estao abertas ou fechadas."""

//Antes de tudo preciso deixar minha explicacao quanto ao codigo.\\
//Infelizmente precisei sair nas ultimas 2h do get de Go e nao peguei a explicacao sobre a tag\\
//Precisei ficar 4 dias fora e so consegui o dia 26/02 para fazer o portscanner\\
//Esse codigo eu peguei no site https://ispycode.com/GO/Network/Port-Scanner\\
//Nao fui eu quem o elaborou, envio ele com os comentarios sobre o que entendi\\


package main

import (
	//O pacote  "net" contem funcoes uteis para tentativas de se conectar a determinadas portas
	"net"
	//O pacote "fmt" contem funcoes para formatacao de texto
	"fmt"
	//O pacote "strconv" nos sera util para convertermos valores int e string
	"strconv"
)

func main() { //Definicao da funcao main()

	//"for" que percorre todos os numeros identificadores das portas existentes
	//Comeca no 1 e finaliza em 65534, incrementando de 1 em 1
	for i := 1; i < 65535; i++ {

	//A variavel "port" recebe o valor da porta formatado de int64 para base decimal
	port := strconv.FormatInt(int64(i), 10)

	//Aqui fazemos uma tentativa de conexao com a porta pelo localhost
	//conn: conexao, err: error
	conn, err := net.Dial("tcp", "127.0.0.1:" + port)

	//Caso nao ocorra nenhum tipo de erro (nil = no error, nesse exemplo)
	if err == nil {

	fmt.Println("Port",i, "open")

	//Fechamento da porta aberta
	conn.Close()
      }
   }
}
