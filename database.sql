-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: expenses
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

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
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `aname` varchar(55) NOT NULL,
  `description` text NOT NULL,
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (1,'Papa Dew','Father of Dew\'s Family','2019-08-02 04:35:32'),(2,'Mama Dew','Mother of Dew\'s Family','2019-08-02 04:56:52'),(3,'Brother Dew','Brother of Dew\'s Family','2019-08-02 04:56:30');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `cname` varchar(55) CHARACTER SET utf8 NOT NULL,
  `description` text NOT NULL,
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Personal','Personal private expenses','2019-08-02 04:57:58'),(2,'House','Housing expenses','2019-08-02 04:57:58'),(3,'Food','Daily food expenses','2019-08-02 05:00:07'),(4,'Transport','Transportation expenses','2019-08-02 05:00:07'),(5,'Clothing','Clothing expenses','2019-08-02 05:00:07'),(6,'Fun','Entertainment expenses (such as movie, musical, theme park)','2019-08-02 05:00:07'),(7,'Family','Family expenses','2019-08-02 05:00:07'),(8,'Misc','For everything else','2019-08-02 05:00:07'),(9,'Income','Monthly income','2019-08-02 05:00:35');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mode`
--

DROP TABLE IF EXISTS `mode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mode` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `mname` varchar(55) NOT NULL,
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mode`
--

LOCK TABLES `mode` WRITE;
/*!40000 ALTER TABLE `mode` DISABLE KEYS */;
INSERT INTO `mode` VALUES (1,'Cash','2019-08-02 05:02:32'),(2,'Debit Card','2019-08-02 05:02:32'),(3,'Credit Card','2019-08-02 05:02:32'),(4,'Mobile (PayNow/Paylah)','2019-08-02 05:02:32'),(5,'Bank','2019-08-05 03:29:46'),(6,'Others','2019-08-26 08:38:17');
/*!40000 ALTER TABLE `mode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tname` varchar(30) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (1,'FairPrice '),(2,'Sheng Siong'),(3,'Giant'),(4,'Capitaland'),(5,'Insurance'),(6,'Taxi'),(7,'Restaurant'),(8,'Phone Bill'),(9,'Utilities Bill'),(10,'Grocery'),(11,'Airfare'),(12,'Hotel'),(13,'School'),(14,'Stationary');
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` text CHARACTER SET utf8 NOT NULL,
  `debit` decimal(11,2) DEFAULT '0.00',
  `credit` decimal(11,2) DEFAULT '0.00',
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `accountid` int(11) NOT NULL,
  `categoriesid` int(11) NOT NULL,
  `modeid` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accountid` (`accountid`),
  KEY `categoriesid` (`categoriesid`),
  KEY `modeid` (`modeid`),
  CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`accountid`) REFERENCES `account` (`id`),
  CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`categoriesid`) REFERENCES `categories` (`id`),
  CONSTRAINT `transaction_ibfk_3` FOREIGN KEY (`modeid`) REFERENCES `mode` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (1,'Code Institute : Income of the month July 2019',3500.00,0.00,'2019-08-22 07:41:18',1,9,1),(2,'SIM HQ Income of the Month : July 2019',3500.00,0.00,'2019-08-05 04:13:11',2,9,5),(3,'Taxi Taxi',0.00,40.00,'2019-08-23 05:56:58',1,4,3),(13,'Lunch Money for Brother\'s Dew school',0.00,40.00,'2019-08-20 08:15:28',1,3,1),(14,'RWS Day trip',0.00,154.00,'2019-08-20 08:17:02',2,7,3),(15,'New backpack',0.00,0.00,'2019-08-26 07:39:22',1,1,1),(16,'Test tag 1',0.00,10.00,'2019-08-27 06:24:42',1,1,1),(17,'test tag 2',0.00,20.00,'2019-08-27 06:24:58',1,1,1),(18,'test 1 + 2 ',0.00,0.00,'2019-08-27 06:55:37',2,7,3);
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactiontag`
--

DROP TABLE IF EXISTS `transactiontag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transactiontag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `transactionid` int(11) DEFAULT NULL,
  `tagid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `transactionid` (`transactionid`),
  KEY `tagid` (`tagid`),
  CONSTRAINT `transactiontag_ibfk_1` FOREIGN KEY (`transactionid`) REFERENCES `transaction` (`id`),
  CONSTRAINT `transactiontag_ibfk_2` FOREIGN KEY (`tagid`) REFERENCES `tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactiontag`
--

LOCK TABLES `transactiontag` WRITE;
/*!40000 ALTER TABLE `transactiontag` DISABLE KEYS */;
INSERT INTO `transactiontag` VALUES (6,16,1),(7,17,2),(8,18,1),(9,18,2),(10,3,4),(11,3,6);
/*!40000 ALTER TABLE `transactiontag` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-28  3:14:41
