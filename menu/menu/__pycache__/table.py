CREATE TABLE `dynamicmenu_mainmenu` (  `id` bigint(20) NOT NULL,  `menucode` int(11) NOT NULL,  `menuname` varchar(100) NOT NULL,  `menutype` int(11) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
 
CREATE TABLE `dynamicmenu_menulist` (  `id` bigint(20) NOT NULL,  `Menucode` int(11) NOT NULL,  `MenuType` int(11) NOT NULL,  `menuname` varchar(100) NOT NULL,  `submenuname` varchar(100) NOT NULL,  `menulink` varchar(100) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
