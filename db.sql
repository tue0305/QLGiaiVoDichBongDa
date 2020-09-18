CREATE DATABASE  IF NOT EXISTS `football_league` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `football_league`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: football_league
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `banthang`
--

DROP TABLE IF EXISTS `banthang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `banthang` (
  `maBT` int NOT NULL AUTO_INCREMENT,
  `thoiDiem` float NOT NULL,
  `maTD` int NOT NULL,
  `maCT` int NOT NULL,
  `maLoaiBT` int NOT NULL,
  PRIMARY KEY (`maBT`),
  KEY `maTD` (`maTD`),
  KEY `maCT` (`maCT`),
  KEY `maLoaiBT` (`maLoaiBT`),
  CONSTRAINT `banthang_ibfk_1` FOREIGN KEY (`maTD`) REFERENCES `trandau` (`maTD`),
  CONSTRAINT `banthang_ibfk_2` FOREIGN KEY (`maCT`) REFERENCES `cauthu` (`maCT`),
  CONSTRAINT `banthang_ibfk_3` FOREIGN KEY (`maLoaiBT`) REFERENCES `loaibanthang` (`maLoaiBT`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banthang`
--

LOCK TABLES `banthang` WRITE;
/*!40000 ALTER TABLE `banthang` DISABLE KEYS */;
/*!40000 ALTER TABLE `banthang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cauthu`
--

DROP TABLE IF EXISTS `cauthu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cauthu` (
  `maCT` int NOT NULL AUTO_INCREMENT,
  `tenCT` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ngaySinh` date NOT NULL,
  `ghiChu` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `avatar` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `maLoaiCT` int NOT NULL,
  `maDB` int NOT NULL,
  PRIMARY KEY (`maCT`),
  KEY `maLoaiCT` (`maLoaiCT`),
  KEY `maDB` (`maDB`),
  CONSTRAINT `cauthu_ibfk_1` FOREIGN KEY (`maLoaiCT`) REFERENCES `loaicauthu` (`maLoaiCT`),
  CONSTRAINT `cauthu_ibfk_2` FOREIGN KEY (`maDB`) REFERENCES `doibong` (`maDB`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cauthu`
--

LOCK TABLES `cauthu` WRITE;
/*!40000 ALTER TABLE `cauthu` DISABLE KEYS */;
INSERT INTO `cauthu` VALUES (2,'nguyễn văn độ','2020-09-24',NULL,'https://znews-photo.zadn.vn/w660/Uploaded/kbd_bcvi/2019_11_23/5d828d976f24eb1a752053b5_thumb.jpg',2,1);
/*!40000 ALTER TABLE `cauthu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doibong`
--

DROP TABLE IF EXISTS `doibong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doibong` (
  `maDB` int NOT NULL AUTO_INCREMENT,
  `tenDB` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `sanNha` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `soLuongCauThu` int NOT NULL,
  `avatar` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`maDB`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doibong`
--

LOCK TABLES `doibong` WRITE;
/*!40000 ALTER TABLE `doibong` DISABLE KEYS */;
INSERT INTO `doibong` VALUES (1,'how are you','nút đồ',11,'https://zshop.vn/images/link/63/1045.jpg?t=1474958283'),(2,'bình dương','hàng mã',12,'https://www.elle.vn/wp-content/uploads/2017/07/25/hinh-anh-dep-1.jpg'),(3,'sai gon','aa',11,'https://img3.thuthuatphanmem.vn/uploads/2019/10/01/mau-logo-bong-da-don-gian_103806674.png'),(4,'bình phước','âa',11,'https://upload.wikimedia.org/wikipedia/vi/4/41/Logolich.jpg'),(5,'hải phòng','bb',11,'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTTSHhizOvoXK9OE_fLvvHxK4_U8A1mBao4qg&usqp=CAU');
/*!40000 ALTER TABLE `doibong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `giaidau`
--

DROP TABLE IF EXISTS `giaidau`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `giaidau` (
  `maGD` int NOT NULL AUTO_INCREMENT,
  `tenGD` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ngayBatDau` date NOT NULL,
  `ngayKetThuc` date NOT NULL,
  `avatar` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`maGD`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `giaidau`
--

LOCK TABLES `giaidau` WRITE;
/*!40000 ALTER TABLE `giaidau` DISABLE KEYS */;
INSERT INTO `giaidau` VALUES (1,'vô địch quốc gia','2020-09-16','2020-09-30','https://img3.thuthuatphanmem.vn/uploads/2019/10/01/hinh-logo-bong-da_103805580.jpg');
/*!40000 ALTER TABLE `giaidau` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loaibanthang`
--

DROP TABLE IF EXISTS `loaibanthang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loaibanthang` (
  `maLoaiBT` int NOT NULL AUTO_INCREMENT,
  `tenLoaiBT` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`maLoaiBT`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaibanthang`
--

LOCK TABLES `loaibanthang` WRITE;
/*!40000 ALTER TABLE `loaibanthang` DISABLE KEYS */;
INSERT INTO `loaibanthang` VALUES (1,'A'),(2,'B'),(3,'C');
/*!40000 ALTER TABLE `loaibanthang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loaicauthu`
--

DROP TABLE IF EXISTS `loaicauthu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loaicauthu` (
  `maLoaiCT` int NOT NULL AUTO_INCREMENT,
  `tenLoaiCT` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`maLoaiCT`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaicauthu`
--

LOCK TABLES `loaicauthu` WRITE;
/*!40000 ALTER TABLE `loaicauthu` DISABLE KEYS */;
INSERT INTO `loaicauthu` VALUES (2,'ngoài nước'),(3,'trong nước');
/*!40000 ALTER TABLE `loaicauthu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quydinh`
--

DROP TABLE IF EXISTS `quydinh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quydinh` (
  `maQD` int NOT NULL AUTO_INCREMENT,
  `tuoiToiThieu` int NOT NULL,
  `tuoiToiDa` int NOT NULL,
  `soCauThuToiThieu` int NOT NULL,
  `soCauThuToiDa` int NOT NULL,
  `soCauThuNuocNgoaiToiDa` int NOT NULL,
  `thoiDiemGhiBanToiDa` int NOT NULL,
  `diemSoThang` int NOT NULL,
  `diemSoThua` int NOT NULL,
  `diemSoHoa` int NOT NULL,
  `thuTuUuTienXepHang` int NOT NULL,
  PRIMARY KEY (`maQD`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quydinh`
--

LOCK TABLES `quydinh` WRITE;
/*!40000 ALTER TABLE `quydinh` DISABLE KEYS */;
INSERT INTO `quydinh` VALUES (1,16,40,15,22,3,96,3,0,1,0);
/*!40000 ALTER TABLE `quydinh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trandau`
--

DROP TABLE IF EXISTS `trandau`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trandau` (
  `maTD` int NOT NULL AUTO_INCREMENT,
  `ngayThiDau` date NOT NULL,
  `gioThiDau` float NOT NULL,
  `sanThiDau` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tranDau` int NOT NULL,
  `tranDau1` int NOT NULL,
  `maVD` int NOT NULL,
  `maGD` int NOT NULL,
  PRIMARY KEY (`maTD`),
  KEY `tranDau` (`tranDau`),
  KEY `tranDau1` (`tranDau1`),
  KEY `maVD` (`maVD`),
  KEY `maGD` (`maGD`),
  CONSTRAINT `trandau_ibfk_1` FOREIGN KEY (`tranDau`) REFERENCES `doibong` (`maDB`),
  CONSTRAINT `trandau_ibfk_2` FOREIGN KEY (`tranDau1`) REFERENCES `doibong` (`maDB`),
  CONSTRAINT `trandau_ibfk_3` FOREIGN KEY (`maVD`) REFERENCES `vongdau` (`maVD`),
  CONSTRAINT `trandau_ibfk_4` FOREIGN KEY (`maGD`) REFERENCES `giaidau` (`maGD`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trandau`
--

LOCK TABLES `trandau` WRITE;
/*!40000 ALTER TABLE `trandau` DISABLE KEYS */;
INSERT INTO `trandau` VALUES (1,'2020-09-24',11,'mĩ',1,2,1,1);
/*!40000 ALTER TABLE `trandau` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `userName` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `passWord` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `birthDate` date DEFAULT NULL,
  `address` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `role` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `user_chk_1` CHECK ((`active` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','admin','c4ca4238a0b923820dcc509a6f75849b','ad@gmail.com',NULL,NULL,'Admin',1),(7,'vip','vip','202cb962ac59075b964b07152d234b70','vip@gmail.com',NULL,NULL,'Admin',1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vongdau`
--

DROP TABLE IF EXISTS `vongdau`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vongdau` (
  `maVD` int NOT NULL AUTO_INCREMENT,
  `tenVD` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`maVD`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vongdau`
--

LOCK TABLES `vongdau` WRITE;
/*!40000 ALTER TABLE `vongdau` DISABLE KEYS */;
INSERT INTO `vongdau` VALUES (1,'vòng loại'),(4,'vòng chung kết'),(5,'bình phước'),(7,'bình phước');
/*!40000 ALTER TABLE `vongdau` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-18 21:17:16
