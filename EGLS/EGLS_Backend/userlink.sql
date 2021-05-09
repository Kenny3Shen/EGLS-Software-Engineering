-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2021-04-15 12:07:41
-- 服务器版本： 5.7.26
-- PHP 版本： 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `userlink`
--

-- --------------------------------------------------------

--
-- 表的结构 `shen_ss`
--

CREATE TABLE `shen_ss` (
  `Title` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `Platform` int(11) NOT NULL,
  `RoomId` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `Definition` int(11) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `shen_ss`
--

INSERT INTO `shen_ss` (`Title`, `Platform`, `RoomId`, `Definition`, `id`) VALUES
('DouYu_99999_Blue-Ray', 0, '99999', 0, 4),
('AcFun_23512715_Blue-Ray', 2, '23512715', 0, 5),
('BiliBili_743689_Blue-Ray', 1, '743689', 0, 8),
('BiliBili_884199_Blue-Ray', 1, '884199', 0, 10),
('BiliBili_22211725_Blue-Ray', 1, '22211725', 0, 11),
('AcFun_17825771_Blue-Ray', 2, '17825771', 0, 13),
('AcFun_17062172_Blue-Ray', 2, '17062172', 0, 14),
('DouYu_22222_Blue-Ray', 0, '22222', 0, 16),
('DouYu_5377721_Blue-Ray', 0, '5377721', 0, 21),
('BiliBili_6_Blue-Ray', 1, '6', 0, 22),
('NanTong', 0, '606118', 0, 23),
('WDNMD', 0, '9418', 0, 29);

--
-- 转储表的索引
--

--
-- 表的索引 `shen_ss`
--
ALTER TABLE `shen_ss`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `shen_ss`
--
ALTER TABLE `shen_ss`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
