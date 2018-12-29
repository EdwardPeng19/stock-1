# coding=utf-8

user_agents = [
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1;AcooBrowser;.NETCLR1.1.4322;.NETCLR2.0.50727)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0;AcooBrowser;SLCC1;.NETCLR2.0.50727;MediaCenterPC5.0;.NETCLR3.0.04506)",
"Mozilla/4.0(compatible;MSIE7.0;AOL9.5;AOLBuild4337.35;WindowsNT5.1;.NETCLR1.1.4322;.NETCLR2.0.50727)",
"Mozilla/5.0(Windows;U;MSIE9.0;WindowsNT9.0;en-US)",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Win64;x64;Trident/5.0;.NETCLR3.5.30729;.NETCLR3.0.30729;.NETCLR2.0.50727;MediaCenterPC6.0)",
"Mozilla/5.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;WOW64;Trident/4.0;SLCC2;.NETCLR2.0.50727;.NETCLR3.5.30729;.NETCLR3.0.30729;.NETCLR1.0.3705;.NETCLR1.1.4322)",
"Mozilla/4.0(compatible;MSIE7.0b;WindowsNT5.2;.NETCLR1.1.4322;.NETCLR2.0.50727;InfoPath.2;.NETCLR3.0.04506.30)",
"Mozilla/5.0(Windows;U;WindowsNT5.1;zh-CN)AppleWebKit/523.15(KHTML,likeGecko,Safari/419.3)Arora/0.3(Change:287c9dfb30)",
"Mozilla/5.0(X11;U;Linux;en-US)AppleWebKit/527+(KHTML,likeGecko,Safari/419.3)Arora/0.6",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US;rv:1.8.1.2pre)Gecko/20070215K-Ninja/2.1.1",
"Mozilla/5.0(Windows;U;WindowsNT5.1;zh-CN;rv:1.9)Gecko/20080705Firefox/3.0Kapiko/3.0",
"Mozilla/5.0(X11;Linuxi686;U;)Gecko/20070322Kazehakase/0.4.5",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9.0.8)GeckoFedora/1.9.0.8-1.fc10Kazehakase/0.5.6",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_3)AppleWebKit/535.20(KHTML,likeGecko)Chrome/19.0.1036.7Safari/535.20",
"Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;fr)Presto/2.9.168Version/11.52",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.11TaoBrowser/2.0Safari/536.11",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/21.0.1180.71Safari/537.1LBBROWSER",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;WOW64;Trident/5.0;SLCC2;.NETCLR2.0.50727;.NETCLR3.5.30729;.NETCLR3.0.30729;MediaCenterPC6.0;.NET4.0C;.NET4.0E;LBBROWSER)",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1;QQDownload732;.NET4.0C;.NET4.0E;LBBROWSER)",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.84Safari/535.11LBBROWSER",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.1;WOW64;Trident/5.0;SLCC2;.NETCLR2.0.50727;.NETCLR3.5.30729;.NETCLR3.0.30729;MediaCenterPC6.0;.NET4.0C;.NET4.0E)",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;WOW64;Trident/5.0;SLCC2;.NETCLR2.0.50727;.NETCLR3.5.30729;.NETCLR3.0.30729;MediaCenterPC6.0;.NET4.0C;.NET4.0E;QQBrowser/7.0.3698.400)",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1;QQDownload732;.NET4.0C;.NET4.0E)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SV1;QQDownload732;.NET4.0C;.NET4.0E;360SE)",
"Mozilla/5.0(WindowsNT5.1)AppleWebKit/537.1(KHTML,likeGecko)Chrome/21.0.1180.89Safari/537.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/21.0.1180.89Safari/537.1",
"Mozilla/5.0(iPad;U;CPUOS4_2_1likeMacOSX;zh-cn)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8C148Safari/6533.18.5",
"Mozilla/5.0(WindowsNT6.1;Win64;x64;rv:2.0b13pre)Gecko/20110307Firefox/4.0b13pre",
"Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv:16.0)Gecko/20100101Firefox/16.0",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.11(KHTML,likeGecko)Chrome/23.0.1271.64Safari/537.11",
"Mozilla/5.0(X11;U;Linuxx86_64;zh-CN;rv:1.9.2.10)Gecko/20100922Ubuntu/10.10(maverick)Firefox/3.6.10",
"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/58.0.3029.110Safari/537.36",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/22.0.1207.1Safari/537.1",
"Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6",
"Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6",
"Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/19.77.34.5Safari/537.1",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5",
"Mozilla/5.0(WindowsNT6.0)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.36Safari/536.5",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3",
"Mozilla/5.0(WindowsNT5.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",
"Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",
"Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3",
"Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3",
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3",
"Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.0Safari/536.3",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24",
"Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/43.0.2357.132Safari/537.36",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:41.0)Gecko/20100101Firefox/41.0"
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/22.0.1207.1Safari/537.1"
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
"Mozilla/5.0(WindowsNT10.0;WOW64;rv:38.0)Gecko/20100101Firefox/38.0",
"Mozilla/5.0(WindowsNT10.0;WOW64;Trident/7.0;.NET4.0C;.NET4.0E;.NETCLR2.0.50727;.NETCLR3.0.30729;.NETCLR3.5.30729;InfoPath.3;rv:11.0)likeGecko",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)",
"Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
"Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5",
"Mozilla/5.0(iPod;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5",
"Mozilla/5.0(iPad;U;CPUOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5",
"Mozilla/5.0(Linux;U;Android2.3.7;en-us;NexusOneBuild/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"MQQBrowser/26Mozilla/5.0(Linux;U;Android2.3.7;zh-cn;MB200Build/GRJ22;CyanogenMod-7)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Opera/9.80(Android2.3.4;Linux;OperaMobi/build-1107180945;U;en-GB)Presto/2.8.149Version/11.10",
"Mozilla/5.0(Linux;U;Android3.0;en-us;XoomBuild/HRI39)AppleWebKit/534.13(KHTML,likeGecko)Version/4.0Safari/534.13",
"Mozilla/5.0(BlackBerry;U;BlackBerry9800;en)AppleWebKit/534.1+(KHTML,likeGecko)Version/6.0.0.337MobileSafari/534.1+",
"Mozilla/5.0(hp-tablet;Linux;hpwOS/3.0.0;U;en-US)AppleWebKit/534.6(KHTML,likeGecko)wOSBrowser/233.70Safari/534.6TouchPad/1.0",
"Mozilla/5.0(SymbianOS/9.4;Series60/5.0NokiaN97-1/20.0.019;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/525(KHTML,likeGecko)BrowserNG/7.1.18124",
"Mozilla/5.0(compatible;MSIE9.0;WindowsPhoneOS7.5;Trident/5.0;IEMobile/9.0;HTC;Titan)",
"Mozilla/4.0(compatible;MSIE6.0;)Opera/UCWEB7.0.2.37/28/999",
"Mozilla/6.0(iPhone;CPUiPhoneOS8_0likeMacOSX)AppleWebKit/536.26(KHTML,likeGecko)Version/8.0Mobile/10A5376eSafari/8536.25",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
"Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",

]