# 1、访问首页地址：http://127.0.0.1:8000/base/





#2、数据库建表语句：
CREATE TABLE `saas` (
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `total` varchar(64) DEFAULT NULL,
  `succ` varchar(64) DEFAULT NULL,
  `fail` varchar(64) DEFAULT NULL,
  `percent` varchar(64) DEFAULT NULL,
  `author` varchar(64) DEFAULT NULL,
  `add_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=137 DEFAULT CHARSET=utf8 COMMENT='电商自动化用例信息表';
