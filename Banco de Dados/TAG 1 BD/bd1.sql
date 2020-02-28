CREATE DATABASE  IF NOT EXISTS `psgris` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `psgris`;
-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: psgris
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `candidatos`
--

DROP TABLE IF EXISTS `candidatos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `candidatos` (
  `dre` int(11) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `curso` varchar(30) NOT NULL,
  `area_favorita` varchar(30) DEFAULT NULL,
  `presenca` char(4) NOT NULL,
  PRIMARY KEY (`dre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `candidatos`
--

LOCK TABLES `candidatos` WRITE;
/*!40000 ALTER TABLE `candidatos` DISABLE KEYS */;
INSERT INTO `candidatos` VALUES (117425689,'Fulano de Tal','fulanodetal@poli.ufrj.br','Engenharia Elétrica','Banco de Dados','100%'),(118104124,'Ciclano Silva','ciclano@poli.ufrj.br','Engenharia Civil','Criptografia','60%'),(118127894,'Felipe Barbosa','felipe-barbosa@dcc.ufrj.br','Ciência da Computação','Firewall','70%'),(118658963,'Maria Julia','maria.j@dcc.ufrj.br','Ciência da Computação','Web','90%'),(119105102,'Mariano Gomes','mariano-gomesj@dcc.ufrj.br','Ciência da Computação','Web','80%'),(119574125,'Daniel Soares','soares_daniel@poli.ufrj.br','Engenharia Nuclear','Redes','100%');
/*!40000 ALTER TABLE `candidatos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ouvintes`
--

DROP TABLE IF EXISTS `ouvintes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ouvintes` (
  `nome` varchar(30) NOT NULL,
  `vinculo_ufrj` text NOT NULL,
  `identificacao(CPF/DRE)` varchar(12) NOT NULL,
  `curso` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `como_conheceuGRIS` text NOT NULL,
  PRIMARY KEY (`identificacao(CPF/DRE)`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ouvintes`
--

LOCK TABLES `ouvintes` WRITE;
/*!40000 ALTER TABLE `ouvintes` DISABLE KEYS */;
INSERT INTO `ouvintes` VALUES ('Márcio Santos','Sem vínculo','04415478921','','masantos@gmail.com','Por um membro'),('Sofia Lima','Sem vínculo','05745825801','','lima_sofia@gmail.com','Pesquisa'),('Adalto Melo','Estudante','115487658','Ciência da Computação','melo-adalto@dcc.ufrj.br','Mural'),('Roberto Nunes','Estudante','117256341','Biologia','robnunes@biologia.ufrj.br','Grupo Facebook');
/*!40000 ALTER TABLE `ouvintes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `palestrantes`
--

DROP TABLE IF EXISTS `palestrantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `palestrantes` (
  `id_get` int(2) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `descricao` text NOT NULL,
  `formacao` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `gris_desde` year(4) NOT NULL,
  `situacao_gris` text NOT NULL,
  PRIMARY KEY (`id_get`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `palestrantes`
--

LOCK TABLES `palestrantes` WRITE;
/*!40000 ALTER TABLE `palestrantes` DISABLE KEYS */;
INSERT INTO `palestrantes` VALUES (1,'Esoj','Trabalha no CapGov','Engenharia Eletrônica','esoj@poli.ufrj.br',2018,'Membro'),(2,'Breno','Trabalha no CapGov','Engenharia Eletrônica','brenocss@poli.ufrj.br',2018,'Membro'),(3,'Sidney','Monitor de Criptografia I','Ciência da Computação','sid@dcc.ufrj.br',2019,'Membro'),(4,'Franklin','Diretor GRIS','Ciência da Computação','franklin@dcc.ufrj.br',2019,'Membro'),(5,'Manoel','Analista de Segurança - Globo','Engenharia Eletrônica','mdjunior@poli.ufrj.br',2013,'Colaborador'),(6,'Arthur','Especialista em BD','Ciência da Computação','arthur@dcc.ufrj.br',2015,'Colaborador');
/*!40000 ALTER TABLE `palestrantes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tag` (
  `id_tag` int(2) NOT NULL AUTO_INCREMENT,
  `assunto` varchar(30) NOT NULL,
  `descricao` text NOT NULL,
  `data_entrega` varchar(10) NOT NULL,
  `get_avaliador` int(2) DEFAULT NULL,
  PRIMARY KEY (`id_tag`),
  KEY `get_avaliador` (`get_avaliador`),
  CONSTRAINT `tag_ibfk_1` FOREIGN KEY (`get_avaliador`) REFERENCES `palestrantes` (`id_get`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (1,'Banco de Dados','Criar um Banco de Dados do Processo Seletivo GRIS','29/02/2020',6),(2,'Criptografia','Resolver 3 desafios do Cryptopals','29/02/2020',3),(3,'Perl/Go','Criar um Portscanner em Go','27/02/2020',5),(4,'Ethical Hacking','Redação sobre Ethical Hacking e Hacking Ativismo','07/03/2020',6);
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-28 15:52:09
