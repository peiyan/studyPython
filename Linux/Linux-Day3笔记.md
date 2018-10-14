### 一、上堂回顾

> 1.目录结构
>
> ​	/；根目录
>
> ​	/home:存放普通用户
>
> ​	/etc:存放系统配置的文件【用户信息，用户密码，root密码等】
>
> ​	/root:存放超级管理员
>
> ​	/tmp:临时目录，存放临时文件
>
> 2.常用命令
>
> ​	文件管理：
>
> ​	ls:列出指定目录下的所有的信息
>
> ​		-a:包括隐藏文件
>
> ​		-l:权限，大小，文件属性等全部列出来
>
> ​		ls -a -l ----->ls -al ----->ll
>
> ​	pwd:查看当前的工作目录
>
> ​	cat:查看文件的内容
>
> ​		cat  finename
>
> ​	cd：切换工作目录
>
> ​		cd  指定的路径【相对路径，绝对路径】
>
> ​		cd  ..      退回上一级目录
>
> ​		cd  ../..
>
> ​		cd  .    当前路径
>
> ​	mv：移动，重命名
>
> ​		mv   源文件   目标文件   ：重命名
>
> ​		mv   源文件   目标目录 ：移动
>
> ​	cp:复制
>
> ​		cp  源文件   目标目录：
>
> ​		cp 源目录   目标目录：
>
> ​	mkdir:创建目录       -p
>
> ​	touch:创建空白文件
>
> ​	rmdir:删除空目录
>
> ​	rm:删除目录和文件
>
> ​		-r:
>
> ​		-rf:强制性删除
>
> ​	ln:建立链接文件
>
> ​		软连接：ln -s   源文件  链接
>
> ​		硬链接：ln  源文件  链接
>
> ​	grep:检索
>
> ​	find:按照条件查找文件
>
> ​	tee:输入

### 二、常用命令

#### 1.文件管理

> 20>sed      流编辑器，一次处理一行内容，主要用来自动编辑一个或多个文件
>
> ```
> 格式：[-nefr] [动作] [文件]
>
> 选项：
> -e<script>或--expression=<script>：以选项中的指定的script来处理输入的文本文件；
> -f<script文件>或--file=<script文件>：以选项中指定的script文件来处理输入的文本文件；
> -h或--help：显示帮助；
> -n或--quiet或——silent：仅显示script处理后的结果；
> -V或--version：显示版本信息。
>
> 参数：
> 文件：指定待处理的文本文件列表。
>
> 命令：
> a\ 在当前行下面插入文本。
> i\ 在当前行上面插入文本。
> c\ 把选定的行改为新的文本。
> d 删除，删除选择的行。
> D 删除模板块的第一行。
> s 替换指定字符
> h 拷贝模板块的内容到内存中的缓冲区。
> H 追加模板块的内容到内存中的缓冲区。
> g 获得内存缓冲区的内容，并替代当前模板块中的文本。
> G 获得内存缓冲区的内容，并追加到当前模板块文本的后面。
> l 列表不能打印字符的清单。
> n 读取下一个输入行，用下一个命令处理新的行而不是用第一个命令。
> N 追加下一个输入行到模板块后面并在二者间嵌入一个新行，改变当前行号码。
> p 打印模板块的行。
> P(大写) 打印模板块的第一行。
> q 退出Sed。
> b lable 分支到脚本中带有标记的地方，如果分支不存在则分支到脚本的末尾。
> r file 从file中读行。
> t label if分支，从最后一行开始，条件一旦满足或者T，t命令，将导致分支到带有标号的命令处，或者到脚本的末尾。
> T label 错误分支，从最后一行开始，一旦发生错误或者T，t命令，将导致分支到带有标号的命令处，或者到脚本的末尾。
> w file 写并追加模板块到file末尾。  
> W file 写并追加模板块的第一行到file末尾。  
> ! 表示后面的命令对所有没有被选定的行发生作用。  
> = 打印当前行号码。  
> # 把注释扩展到下一个换行符以前。  
>
> sed替换标记
> g 表示行内全面替换。  
> p 表示打印行。  
> w 表示把行写入一个文件。  
> x 表示互换模板块中的文本和缓冲区中的文本。  
> y 表示把一个字符翻译为另外的字符（但是不用于正则表达式）
> \1 子串匹配标记
> & 已匹配字符串标记
>
> sed元字符集
> ^ 匹配行开始，如：/^sed/匹配所有以sed开头的行。
> $ 匹配行结束，如：/sed$/匹配所有以sed结尾的行。
> . 匹配一个非换行符的任意字符，如：/s.d/匹配s后接一个任意字符，最后是d。
> * 匹配0个或多个字符，如：/*sed/匹配所有模板是一个或多个空格后紧跟sed的行。
> [] 匹配一个指定范围内的字符，如/[ss]ed/匹配sed和Sed。  
> [^] 匹配一个不在指定范围内的字符，如：/[^A-RT-Z]ed/匹配不包含A-R和T-Z的一个字母开头，紧跟ed的行。
> \(..\) 匹配子串，保存匹配的字符，如s/\(love\)able/\1rs，loveable被替换成lovers。
> & 保存搜索字符用来替换其他字符，如s/love/**&**/，love这成**love**。
> \< 匹配单词的开始，如:/\<love/匹配包含以love开头的单词的行。
> \> 匹配单词的结束，如/love\>/匹配包含以love结尾的单词的行。
> x\{m\} 重复字符x，m次，如：/0\{5\}/匹配包含5个0的行。
> x\{m,\} 重复字符x，至少m次，如：/0\{5,\}/匹配至少有5个0的行。
> x\{m,n\} 重复字符x，至少m次，不多于n次，如：/0\{5,10\}/匹配5~10个0的行。
> ```

> ```Python
> #1.增加
> #a,追加，a后面可以接字符串，但是注意：新接的字符串会出现在下一行
> yangyang@yangyang-virtualmachine:~$ cd Desktop/
> yangyang@yangyang-virtualmachine:~/Desktop$ ls
> a  a1.txt  a2.txt  a.txt  b.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ vim a1.txt 
> yangyang@yangyang-virtualmachine:~/Desktop$ sed  "/^text/a\pppppp" a1.txt 
> this is a test
> text
> pppppp
> hello
> uuuu
> ppppp
> yangyang@yangyang-virtualmachine:~/Desktop$ sed -i "2a\python1805" a1.txt 
> yangyang@yangyang-virtualmachine:~/Desktop$ vim a1.txt 
>
>
> #i,插入，和a之间的区别在于添加到了匹配到的行的前面
> yangyang@yangyang-virtualmachine:~/Desktop$ sed  "/^text/i\pppppp111" a1.txt 
> this is a test
> pppppp111
> text
> python1805
> hello
> uuuu
> ppppp
>
> #2.删除
> #d,删除，注意：所有d后面不接任何内容
> yangyang@yangyang-virtualmachine:~/Desktop$ sed "3d" a1.txt 
> this is a test
> text
> hello
> uuuu
> ppppp
> yangyang@yangyang-virtualmachine:~/Desktop$ sed "1,3d" a1.txt 
> hello
> uuuu
> ppppp
> yangyang@yangyang-virtualmachine:~/Desktop$ cat a1.txt 
> this is a test
> text
> python1805
> hello
> uuuu
> ppppp
> yangyang@yangyang-virtualmachine:~/Desktop$ sed "1d;3d;5d" a1.txt
> text
> hello
> ppppp
> yangyang@yangyang-virtualmachine:~/Desktop$ cat a1.txt 
> this is a test
> text
> python1805
> hello
> uuuu
> ppppp
>
> #3.替换
> #s 
> yangyang@yangyang-virtualmachine:~/Desktop$ sed "s/text/exam/" a1.txt
> this is a test
> exam
> python1805
> hello
> uuuu
> ppppp
> yangyang@yangyang-virtualmachine:~/Desktop$ cat a1.txt 
> this is a test
> ```

> 21>打包和压缩
>
> 打包：将一大堆的文件或者目录变成一个总的文件
>
> 压缩：将一个较大的文件处理成一个较小的文件
>
> 操作：先打包【tar命令】-----》压缩【gzip命令和bzip2等】
>
> a.tar     可以把一大堆的文件和目录全部打包成一个文件
>
> ```Python
> -A或--catenate：新增文件到已存在的备份文件；
> -B：设置区块大小；-c或--create：建立新的备份文件；
> -C <目录>：这个选项用在解压缩，若要在特定目录解压缩，可以使用这个选项。
> -d：记录文件的差别；
> -x或--extract或--get：从备份文件中还原文件；
> -z或--gzip或--ungzip：通过gzip指令处理备份文件；
> -Z或--compress或--uncompress：通过compress指令处理备份文件；
> -f<备份文件>或--file=<备份文件>：指定备份文件；
> -v或--verbose：显示指令执行过程；
> -r：添加文件到已经压缩的文件；
> -u：添加改变了和现有的文件到已经存在的压缩文件；
> -j：支持bzip2解压文件；
> -v：显示操作过程；
> -l：文件系统边界设置；
> -k：保留原有文件不覆盖；
> -m：保留文件不被覆盖；
> -w：确认压缩文件的正确性；
> -p或--same-permissions：用原来的文件权限还原文件；
> -P或--absolute-names：文件名使用绝对名称，不移除文件名称前的“/”号；
> -N <日期格式> 或 --newer=<日期时间>：只将较指定日期更新的文件保存到备份文件里；
> --exclude=<范本样式>：排除符合范本样式的文件。
>
> 演示命令：
> yangyang@yangyang-virtualmachine:~/Desktop$ ls
> a  a1.txt  a2.txt  a.txt  b.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ tar -cvf log.tar a1.txt
> a1.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ rm -rf log.tar
> yangyang@yangyang-virtualmachine:~/Desktop$ tar -zcvf log.tar.gz a1.txt 
> a1.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ rm  -rf log.tar.gz 
> yangyang@yangyang-virtualmachine:~/Desktop$ tar -jcvf log.tar.bz2 a1.txt
> a1.txt
>
> 总结：
> -cvf:直接打包，但是不压缩
> -zcvf:.tar.gz代表的是使用gzip压缩的包
> -jcvf:.tar.bz2代表的是使用bzip2压缩的包
> ```
>
> b.gzip	 对文件进行压缩和解压缩，压缩之后用“.gz”作为扩展名
>
> ​	还可以和tar命令一起构成Linux操作系统中比较流行的压缩文件格式
>
> ```Python
> -d或--decompress或----uncompress：解开压缩文件；
> -f或——force：强行压缩文件。不理会文件名称或硬连接是否存在以及该文件是否为符号连接；
> -l或——list：列出压缩文件的相关信息；
> -L或——license：显示版本与版权信息；
> -n或--no-name：压缩文件时，不保存原来的文件名称及时间戳记；
> -N或——name：压缩文件时，保存原来的文件名称及时间戳记；
> -q或——quiet：不显示警告信息；
> -r或——recursive：递归处理，将指定目录下的所有文件及子目录一并处理；
> -t或——test：测试压缩文件是否正确无误；
> -v或——verbose：显示指令执行过程；
> -V或——version：显示版本信息；
>
> 演示命令：
> angyang@yangyang-virtualmachine:~$ cd Desktop/
> yangyang@yangyang-virtualmachine:~/Desktop$ gzip *      #全部压缩
> yangyang@yangyang-virtualmachine:~/Desktop$ gzip -dv *	#全部解压
> a1.txt.gz:	  8.3% -- replaced with a1.txt
> a2.txt.gz:	  9.1% -- replaced with a2.txt
> a.gz:	  2.4% -- replaced with a
> a.txt.gz:	  7.1% -- replaced with a.txt
> b.txt.gz:	  0.0% -- replaced with b.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ gzip *
> yangyang@yangyang-virtualmachine:~/Desktop$ gzip -l *      #显示压缩后的信息
>          compressed        uncompressed  ratio uncompressed_name
>                  69                  48   8.3% a1.txt
>                  35                  11   9.1% a2.txt
>                  60                  41   2.4% a
>                  76                  56   7.1% a.txt
>                  26                   0   0.0% b.txt
>                 266                 156 -55.1% (totals)
> yangyang@yangyang-virtualmachine:~/Desktop$ touch text1.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ gzip -r text1.txt 
> yangyang@yangyang-virtualmachine:~/Desktop$ mkdir check
> yangyang@yangyang-virtualmachine:~/Desktop$ cd check/
> yangyang@yangyang-virtualmachine:~/Desktop/check$ touch  a.txt
> yangyang@yangyang-virtualmachine:~/Desktop/check$ touch b.txt
> yangyang@yangyang-virtualmachine:~/Desktop/check$ touch c.txt
> yangyang@yangyang-virtualmachine:~/Desktop/check$ mkdir text
> yangyang@yangyang-virtualmachine:~/Desktop/check$ cd ..
> yangyang@yangyang-virtualmachine:~/Desktop$ gzip -rv check    #递归压缩
> #注意：只是将目录下的文件全部递归压缩，对子目录不做操作
> check/a.txt:	  0.0% -- replaced with check/a.txt.gz
> check/b.txt:	  0.0% -- replaced with check/b.txt.gz
> check/c.txt:	  0.0% -- replaced with check/c.txt.gz
> yangyang@yangyang-virtualmachine:~/Desktop$ gzip -dr check   #递归解压
> yangyang@yangyang-virtualmachine:~/Desktop$ cd check/
> yangyang@yangyang-virtualmachine:~/Desktop/check$ ls
> a.txt  b.txt  c.txt  text
> yangyang@yangyang-virtualmachine:~/Desktop/check$ cd ..
> yangyang@yangyang-virtualmachine:~/Desktop$ gzip -dv *
> a1.txt.gz:	  8.3% -- replaced with a1.txt
> a2.txt.gz:	  9.1% -- replaced with a2.txt
> a.gz:	  2.4% -- replaced with a
> a.txt.gz:	  7.1% -- replaced with a.txt
> b.txt.gz:	  0.0% -- replaced with b.txt
> gzip: check is a directory -- ignored
> text1.txt.gz:	  0.0% -- replaced with text1.txt
> ```

#### 2.vi和vim编辑器

> **vi命令**是UNIX操作系统最通用的全屏幕纯文本编辑器。Linux中的vi编辑器叫vim，它是vi的增强版（vi Improved），与vi编辑器完全兼容，而且实现了很多增强功能
>
> vim编辑器工作模式有三种：命令模式，输入模式【编辑模式】，末行模式
>
> 输入模式：可以完成文本文档的编辑操作
>
> 命令模式：可以完成对文本的操作命令
>
> 掌握：掌握三种工作模式之间的任意切换
>
> ```Python
> 进入vi的命令 
>     vim filename :打开或新建文件，并将光标置于第一行首    ******
>     vi +n filename ：打开文件，并将光标置于第n行首 
>     vi + filename ：打开文件，并将光标置于最后一行首
>     vi filename1 filename2   :同时打开多个文件
>       
> 演示命令：
> yangyang@yangyang-virtualmachine:~/Desktop$ vim a1.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ vim +3 a1.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ vim + a1.txt
>
> 插入文本类命令 
>   	i ：在光标前       ******
>   	I ：在当前行首 
>   	a：光标后        ******
>   	A：在当前行尾 
>   	o：在当前行之下新开一行        ******
>   	O：在当前行之上新开一行 
>   	r：替换当前字符 
>   	R：替换当前字符及其后的字符，直至按ESC键 
>   
> 移动光标 #在命令模式下使用
>   	j或下箭头 向下移动一行
>   	k或上箭头 向上移动一行
>   	h或左箭头 左移一个字符
>   	l或右箭头 右移一个字符
>   	w 　　　　右移一个词
>   	W 　　　　右移一个以空格分隔的词 
>   	b 　　　　左移一个词
>   	B 　　　　左移一个以空格分隔的词
>   	0 　　　　移到行首
>   	Ctrl-F　　向前翻页
>   	Ctrl-B　　向后翻页
>   	nG　　　　到第n行  ------》先按下数字，再按下G
>   	G 　　　　到最后一行
>   	gg	     第一行   -----》先按下g，再按下g
>   	n+       光标下移n行 
>   	n-       光标上移n行
>     
> esc:退出输入模式      ******
>
> :set number：在命令模式下，用于在最左端显示行号；
> :set nonumber：在命令模式下，用于在最左端不显示行号；
>
> 保存退出 
>   	:wq		执行存盘退出操作；      #对内容做修改之后使用，保存退出   *****
>     :wq!	#修改之后并且强制保存退出
> 	:w		执行存盘操作；
> 	:w！		执行强制存盘操作；
> 	:q		执行退出vi操作；
> 	:q！		执行强制退出vi操作；     #如果没有任何修改的时候使用  ******
> 	:e文件名	打开并编辑指定名称的文件；
> 	:n!		如果同时打开多个文件，则保存上个文件继续编辑下一个文件；
> 	:f		用于显示当前的文件名、光标所在行的行号以及显示比例；
> 	
> 删除操作【注意：和上面的插入文本类没有关系，进入vim后直接使用】 #在命令模式下使用
>   	x		删除光标处的单个字符 
>   	dd		删除光标所在行 
>   	dw		删除当前字符到单词尾（包括空格）的所有字符 
>   	de		删除当前字符到单词尾（不包括单词尾部的空格）的所有字符 
>   	d$		删除当前字符到行尾的所有字符 
>   	d^		删除当前字符到行首的所有字符 
>   	J		删除光标所在行行尾的换行符，相当于合并当前行和下一行的内容
>   	
> 替换操作
>   	:s/old/new 		将当前行中查找到的第一个字符“old” 串替换为“new”
>   	:#,#s/old/new 	在行号“#,#”范围内替换所有的字符串“old”为“new”
>   	:%s/old/new	    在整个文件范围内替换所有的字符串“old”为“new”
>   	:s/old/new/c 	在替换命令末尾加入c命令，将对每个替换动作提示用户进行确认
>   	
> 撤消操作 【注意：直接在输入模式下使用】
> 	u取消最近一次的操作，并恢复操作结果   *****
> 	#可以多次使用u命令恢复已进行的多步操作 
> 	U取消对当前行进行的所有操作 
> 	Ctrl + r对使用u命令撤销的操作进行恢复 
> ```

#### 3.用户管理

> 用户管理包括用户和组账号的管理
>
> 在Linux系统中，每个系统都必须有一个账号，并且对于不同的系统资源的使用权限
>
> root：超级管理员，通常用于系统的管理和维护，对Linux系统具有不受任何限制的操作权限

> ```
> linux使用文件保存用户信息 
> /etc/passwd 用户账户信息。
> /etc/shadow 安全用户账户信息。
> /etc/group 组账户信息。
> /etc/gshadow 安全组账户信息。
> /etc/default/useradd 账户创建的默认值。
> /etc/skel/ 包含默认文件的目录。
> /etc/login.defs Shadow 密码套件配置。
> ```

> 1>whoami     查看当前系统当前用户的用户名
>
> ```Python
> 演示命令：
> yangyang@yangyang-virtualmachine:/$ su root
> 密码： 
> root@yangyang-virtualmachine:/# whoami
> root
> ```

> 2>who     查看当前所有登录系统的用户信息
>
> ```Python
> -q:只显示用户的登录账号的和登录用户的数量
> -u:显示列标题
>
> 演示命令：
> root@yangyang-virtualmachine:/# su yangyang
> yangyang@yangyang-virtualmachine:/$ who
> yangyang tty7         2018-06-28 08:54 (:0)
> yangyang@yangyang-virtualmachine:/$ who -q
> yangyang
> # 用户数=1
> yangyang@yangyang-virtualmachine:/$ who -u
> yangyang tty7         2018-06-28 08:54 02:42        8992 (:0)
> ```

> 3>exit	退出
>
> 如果切换后的用户，则返回上一个登录的账号
>
> ```Python
> 演示命令：
> yangyang@yangyang-virtualmachine:/$ su root
> 密码： 
> root@yangyang-virtualmachine:/# exit
> exit
> yangyang@yangyang-virtualmachine:/$ su root
> 密码： 
> root@yangyang-virtualmachine:/# su yangyang
> yangyang@yangyang-virtualmachine:/$ su
> 密码： 
> root@yangyang-virtualmachine:/# exit
> exit
> yangyang@yangyang-virtualmachine:/$ su - 
> 密码： 
> root@yangyang-virtualmachine:~# exit
> 注销
> ```

> 4>su	切换用户
>
> 注意：如果不知名用户名，则默认切换到root用户
>
> 用法：
>
> ​	su  用户名
>
> ​	su  -   用户名
>
> ```Python
> 演示命令：
> yangyang@yangyang-virtualmachine:/$ su - root
> 密码： 
> root@yangyang-virtualmachine:~# su - yangyang
> yangyang@yangyang-virtualmachine:~$ pwd
> /home/yangyang
> yangyang@yangyang-virtualmachine:~$ 
> ```

> 5>useradd       添加用户
>
> 注意：添加普通用户，只能通过root添加
>
> ```Python
> -c 备注 加上备注。并会将此备注文字加在/etc/passwd中的第5项字段中
> -d 用户主文件夹。指定用户登录所进入的目录，并赋予用户对该目录的的完全控制权        
> -e 有效期限。指定帐号的有效期限。格式为YYYY-MM-DD，将存储在/etc/shadow         
> -f 缓冲天数。限定密码过期后多少天，将该用户帐号停用       
> -g 主要组。设置用户所属的主要组  www.cit.cn           *******
> -G 次要组。设置用户所属的次要组，可设置多组         
> -M 强制不创建用户主文件夹         
> -m 强制建立用户主文件夹，并将/etc/skel/当中的文件复制到用户的根目录下      ****  
> -p 密码。输入该帐号的密码         
> -s shell。用户登录所使用的shell         
> -u uid。指定帐号的标志符user id，简称uid
>
>
> 演示命令：
> #第一种方式添加用户
> yangyang@yangyang-virtualmachine:~$ su root
> 密码： 
> root@yangyang-virtualmachine:/home/yangyang# useradd zhangsan    #添加用户
> root@yangyang-virtualmachine:/home/yangyang# su yangyang
> yangyang@yangyang-virtualmachine:~$ ls /home/
> yangyang         #本质没有添加进来
> yangyang@yangyang-virtualmachine:~$ su root
> 密码： 
> root@yangyang-virtualmachine:/home/yangyang# mkdir /home/zhangsan
>   #在home目录下创建一个和用户同名的目录
> root@yangyang-virtualmachine:/home/yangyang# exit
> exit
> yangyang@yangyang-virtualmachine:~$ ls /home/
> yangyang  zhangsan
> yangyang@yangyang-virtualmachine:~$ ls -l /home/
> 总用量 8
> drwxr-xr-x 31 yangyang rock 4096 6月  28 11:13 yangyang
> drwxr-xr-x  2 root     root 4096 6月  28 14:17 zhangsan
> yangyang@yangyang-virtualmachine:~$ sudo chown zhangsan:zhangsan /home/zhangsan				#将新建的用户和新建的用户目录联系起来
> [sudo] yangyang 的密码： 
> yangyang@yangyang-virtualmachine:~$ ls -l /home/
> 总用量 8
> drwxr-xr-x 31 yangyang rock     4096 6月  28 11:13 yangyang
> drwxr-xr-x  2 zhangsan zhangsan 4096 6月  28 14:17 zhangsan
> yangyang@yangyang-virtualmachine:~$ sudo passwd zhangsan
> 输入新的 UNIX 密码： 
> 重新输入新的 UNIX 密码： 
> passwd：已成功更新密码
> yangyang@yangyang-virtualmachine:~$ ls /home/
> yangyang  zhangsan
> yangyang@yangyang-virtualmachine:~$ su - zhangsan
> 密码： 
> $ ls
> $ su yangyang
> 密码： 
> yangyang@yangyang-virtualmachine:/home/zhangsan$ cd ../..
> yangyang@yangyang-virtualmachine:/$ ls -a /home/yangyang/.bash*  #查看配置文件
> /home/yangyang/.bash_history  /home/yangyang/.bashrc
> /home/yangyang/.bash_logout
> yangyang@yangyang-virtualmachine:/$ su - zhangsan
> 密码： 
> $ ls -a /etc/skel/       #查看配置文件
> .  ..  .bash_logout  .bashrc  examples.desktop	.profile
> $ cp /etc/skel/.bash* .     #将查到的文件拷贝到当前目录下
> $ ls -a
> .  ..  .bash_logout  .bashrc
> $ 注销        #按下ctrl+ d注销用户
> yangyang@yangyang-virtualmachine:/$ sudo vim /etc/passwd  #设置用户密码
> yangyang@yangyang-virtualmachine:/$ su - zhangsan
> 密码： 
> zhangsan@yangyang-virtualmachine:~$ su - yangyang
> 密码： 
>
> #第二种方式添加用户
> yangyang@yangyang-virtualmachine:~$ sudo useradd -m -s /bin/bash lisi
> yangyang@yangyang-virtualmachine:~$ ls /home/
> lisi  yangyang  zhangsan
> yangyang@yangyang-virtualmachine:~$ sudo useradd -m xiaoli
> yangyang@yangyang-virtualmachine:~$ ls /home/
> lisi  xiaoli  yangyang  zhangsan
> yangyang@yangyang-virtualmachine:~$ su - zhangsan
> 密码： 
>
> #第三种方式添加用户
> zhangsan@yangyang-virtualmachine:~$ sudo useradd -m hello
> [sudo] zhangsan 的密码： 
> zhangsan 不在 sudoers 文件中。此事将被报告。
> zhangsan@yangyang-virtualmachine:~$ su - root
> 密码： 
> root@yangyang-virtualmachine:~# vim /etc/sudoers
> root@yangyang-virtualmachine:~# 
>
> 问题：按照第一种方式新增的用户和正常用户的使用有区别
> 正常用户：yangyang@yangyang-virtualmachine:~$ su - zhangsan
> 新增的用户：$ ls
>
> 解决方案：需要手动添加配置文件，过程如下：
> yangyang@yangyang-virtualmachine:/$ su - zhangsan
> 密码： 
> $ ls -a /etc/skel/       #查看配置文件
> .  ..  .bash_logout  .bashrc  examples.desktop	.profile
> $ cp /etc/skel/.bash* .     #将查到的文件拷贝到当前目录下
> $ ls -a
> .  ..  .bash_logout  .bashrc
> $ 注销        #按下ctrl+ d注销用户
> yangyang@yangyang-virtualmachine:/$ sudo vim /etc/passwd  #设置用户密码
> yangyang@yangyang-virtualmachine:/$ su - zhangsan
> 密码： 
> zhangsan@yangyang-virtualmachine:~$
> ```
>

> 6>userdel        删除用户
>
> ```Python
> userdel -r zhangsan   ：删除普通用户，同时自动删除用户所在的主目录
> userdel zhangsan：只是删除普通用户，不会自动删除用户所在的主目录，需要手动 rm -rf zhangsan
>
> 演示命令：
> yangyang@yangyang-virtualmachine:~$ sudo userdel -r zhangsan
> [sudo] yangyang 的密码： 
> userdel: zhangsan 邮件池 (/var/mail/zhangsan) 未找到
> yangyang@yangyang-virtualmachine:~$ ls /home/
> yangyang
> ```

> 7>passwd    设置密码
>
> 注意：一般配合useradd命令使用，当添加一个新的普通用户时，一般会紧接着设置该用户的密码
>
> ```Python
> 演示命令：
> yangyang@yangyang-virtualmachine:~$ sudo useradd -m abc   #添加用户
> yangyang@yangyang-virtualmachine:~$ sudo passwd abc
> 输入新的 UNIX 密码： 			#需要设置的密码
> 重新输入新的 UNIX 密码： 
> passwd：已成功更新密码
> yangyang@yangyang-virtualmachine:~$ su - abc
> 密码：        #新用户的密码
> abc@yangyang-virtualmachine:~$ 
> ```

> 8>查看用户组
>
> 用户组的作用：将多个用户管理在同一个组下，方便管理，可以让不同的用户享用同种权限
>
> ```Python
> 演示命令：
> yangyang@yangyang-virtualmachine:~$cat /etc/group
> ```

> 9>groupadd 			添加组
>
> ```Python
> 演示命令：
> yangyang@yangyang-virtualmachine:~$ sudo useradd -m python -g python1805
> yangyang@yangyang-virtualmachine:~$ sudo passwd python
> 输入新的 UNIX 密码： 
> 重新输入新的 UNIX 密码： 
> passwd：已成功更新密码
> yangyang@yangyang-virtualmachine:~$ su - python
> 密码： 
> python@yangyang-virtualmachine:~$ ll
> 总用量 32
> drwxr-xr-x 2 python python1805 4096 6月  28 15:23 ./
> drwxr-xr-x 5 root   root       4096 6月  28 15:23 ../
> -rw-r--r-- 1 python python1805  220 9月   1  2015 .bash_logout
> -rw-r--r-- 1 python python1805 3771 9月   1  2015 .bashrc
> -rw-r--r-- 1 python python1805 8980 4月  20  2016 examples.desktop
> -rw-r--r-- 1 python python1805  655 6月  24  2016 .profile
> ```

> 10>usermod     	修改用户的基本信息
>
> ```Python
> -c<备注> 　修改用户帐号的备注文字。 
> -d登入目录> 　修改用户登入时的目录。 
> -e<有效期限> 　修改帐号的有效期限。 
> -f<缓冲天数> 　修改在密码过期后多少天即关闭该帐号。 
> -g<群组> 　修改用户所属的群组。 
> -G<群组> 　修改用户所属的附加群组。 
> -l<帐号名称> 　修改用户帐号名称。 
> -L 　锁定用户密码，使密码无效。 
> -s<shell> 　修改用户登入后所使用的shell。 
> -u<uid> 　修改用户ID。 
> -U 　解除密码锁定。
>
> 演示命令：
> angyang@yangyang-virtualmachine:~$ ls -l /home/
> 总用量 16
> drwxr-xr-x  2 abc      abc        4096 6月  28 14:59 abc
> drwxr-xr-x  2 jack     jack       4096 6月  28 15:30 jack
> drwxr-xr-x  2 python   python1805 4096 6月  28 15:23 python
> drwxr-xr-x 31 yangyang yangyang   4096 6月  28 14:36 yangyang
> yangyang@yangyang-virtualmachine:~$ sudo groupadd tom     #创建用户组
> yangyang@yangyang-virtualmachine:~$ sudo usermod -g jack tom   
> usermod：用户“tom”不存在				#修改用户的用户组
> yangyang@yangyang-virtualmachine:~$ sudo usermod -g tom jack
> yangyang@yangyang-virtualmachine:~$ ls -l /home/
> 总用量 16
> drwxr-xr-x  2 abc      abc        4096 6月  28 14:59 abc
> drwxr-xr-x  2 jack     tom        4096 6月  28 15:30 jack
> drwxr-xr-x  2 python   python1805 4096 6月  28 15:23 python
> drwxr-xr-x 31 yangyang yangyang   4096 6月  28 14:36 yangyang
> yangyang@yangyang-virtualmachine:~$ sudo usermod -l newuser jack #修改用户名
> yangyang@yangyang-virtualmachine:~$ ls -l /home/
> 总用量 16
> drwxr-xr-x  2 abc      abc        4096 6月  28 14:59 abc
> drwxr-xr-x  2 newuser  tom        4096 6月  28 15:30 jack
> drwxr-xr-x  2 python   python1805 4096 6月  28 15:23 python
> ```
>

> 11>groupdel 			删除组
>
> ```Python
> 演示命令：
> yangyang@yangyang-virtualmachine:~$ sudo groupdel abc
> groupdel：不能移除用户“abc”的主组
> yangyang@yangyang-virtualmachine:~$ sudo groupdel python1805
> groupdel：不能移除用户“python”的主组
> yangyang@yangyang-virtualmachine:~$ sudo groupadd user11   
> yangyang@yangyang-virtualmachine:~$ sudo groupdel user11  #删除没有用户的组
> yangyang@yangyang-virtualmachine:~$ sudo userdel -r abc   #删除对于有用户组
> userdel: user abc is currently used by process 13160 
> yangyang@yangyang-virtualmachine:~$ 注销   #如果用户在使用中则使用ctrl+d注销
> yangyang@yangyang-virtualmachine:~$ sudo userdel -r abc   #注销之后再删除
> userdel: user abc is currently used by process 13160
> yangyang@yangyang-virtualmachine:~$ 注销
> abc@yangyang-virtualmachine:~$ 注销
> yangyang@yangyang-virtualmachine:~$ sudo userdel -r abc
> userdel: abc 邮件池 (/var/mail/abc) 未找到  
> ```

> 12>sudo      让当前用户暂时以管理员的身份root来执行命令

> 13>chmod     修改文件权限
>
> ```Python
> drwxr-xr-x 31 yangyang yangyang   4096 6月  28 14:36 yangyang
>
> #权限的意义
> rwx           			r-x  			 			r-x
> 当前用户的权限			  同组内其他用户的权限		   其他组内用户的权限
> r w x -
> 4 2 1 0
>
> 演示命令：
> #字母法修改文件权限
> yangyang@yangyang-virtualmachine:~/Desktop$ ll
> 总用量 12
> drwxr-xr-x  2 yangyang yangyang 4096 6月  28 15:47 ./
> drwxr-xr-x 31 yangyang yangyang 4096 6月  28 15:47 ../
> -rw-r--r--  1 yangyang rock       20 6月  28 15:47 a.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ chmod u+x a.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ ll
> 总用量 12
> drwxr-xr-x  2 yangyang yangyang 4096 6月  28 15:47 ./
> drwxr-xr-x 31 yangyang yangyang 4096 6月  28 15:47 ../
> -rwxr--r--  1 yangyang rock       20 6月  28 15:47 a.txt*
>   
> #数字法修改文件权限
> yangyang@yangyang-virtualmachine:~/Desktop$ touch b.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ ll
> 总用量 12
> drwxr-xr-x  2 yangyang yangyang 4096 6月  28 15:52 ./
> drwxr-xr-x 31 yangyang yangyang 4096 6月  28 15:47 ../
> -rwxr--r--  1 yangyang rock       20 6月  28 15:47 a.txt*
> -rw-r--r--  1 yangyang rock        0 6月  28 15:52 b.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ chmod 0764 b.txt
> yangyang@yangyang-virtualmachine:~/Desktop$ ll
> 总用量 12
> drwxr-xr-x  2 yangyang yangyang 4096 6月  28 15:52 ./
> drwxr-xr-x 31 yangyang yangyang 4096 6月  28 15:47 ../
> -rwxr--r--  1 yangyang rock       20 6月  28 15:47 a.txt*
> -rwxrw-r--  1 yangyang rock        0 6月  28 15:52 b.txt*
> ```

> 14>chown       修改文件所有者
>
> 格式：chown   新的用户  文件名

> 15>chgrp      修改文件所属组
>
> 格式：chgrp   新的用户  文件名

#### 4.系统管理

> 1>date   显示日期
>
> ```
> 日期格式化
> %Y     year
> %m     month (01..12)
> %d     day of month (e.g., 01)
> %H     hour (00..23)
> %I     hour (01..12)
> %M     minute (00..59)
> %S     second (00..60)
>
> 演示命令：
>
> ```

> 2>cal		显示一个日历
>
> ```
> 演示命令：
> yangyang@yangyang-virtualmachine:~/Desktop$ cal 
>       六月 2018         
> 日 一 二 三 四 五 六  
>                 1  2  
>  3  4  5  6  7  8  9  
> 10 11 12 13 14 15 16  
> 17 18 19 20 21 22 23  
> 24 25 26 27 28 29 30  
> ```

> 3>ps	报告当前系统的进程状态
>
> ```
> 演示命令：
> yangyang@yangyang-virtualmachine:~/Desktop$ ps -u
> USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
> yangyang  13087  0.0  0.3  25248  6124 pts/4    Ss   14:56   0:00 bash
> yangyang  14078  0.0  0.1  39104  3284 pts/4    R+   16:42   0:00 ps -u
> ```
>
> 

> 4>kill	删除执行中的程序或工作
>
> ```
> -a：当处理当前进程时，不限制命令名和进程号的对应关系；
> -l <信息编号>：若不加<信息编号>选项，则-l参数会列出全部的信息名称；
> -p：指定kill 命令只打印相关进程的进程号，而不发送任何信号；
> -s <信息名称或编号>：指定要送出的信息；
> -u：指定用户
>
> 演示命令：
> yangyang@yangyang-virtualmachine:~/Desktop$ kill -l
>  1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL	 5) SIGTRAP
>  6) SIGABRT	 7) SIGBUS	 8) SIGFPE	 9) SIGKILL	10) SIGUSR1
> 11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM	15) SIGTERM
> 16) SIGSTKFLT	17) SIGCHLD	18) SIGCONT	19) SIGSTOP	20) SIGTSTP
> 21) SIGTTIN	22) SIGTTOU	23) SIGURG	24) SIGXCPU	25) SIGXFSZ
> 26) SIGVTALRM	27) SIGPROF	28) SIGWINCH	29) SIGIO	30) SIGPWR
> 31) SIGSYS	34) SIGRTMIN	35) SIGRTMIN+1	36) SIGRTMIN+2	37) SIGRTMIN+3
> 38) SIGRTMIN+4	39) SIGRTMIN+5	40) SIGRTMIN+6	41) SIGRTMIN+7	42) SIGRTMIN+8
> 43) SIGRTMIN+9	44) SIGRTMIN+10	45) SIGRTMIN+11	46) SIGRTMIN+12	47) SIGRTMIN+13
> 48) SIGRTMIN+14	49) SIGRTMIN+15	50) SIGRTMAX-14	51) SIGRTMAX-13	52) SIGRTMAX-12
> 53) SIGRTMAX-11	54) SIGRTMAX-10	55) SIGRTMAX-9	56) SIGRTMAX-8	57) SIGRTMAX-7
> 58) SIGRTMAX-6	59) SIGRTMAX-5	60) SIGRTMAX-4	61) SIGRTMAX-3	62) SIGRTMAX-2
> 63) SIGRTMAX-1	64) SIGRTMAX	
> ```

> 5>df      显示磁盘分区上的可使用的磁盘空间
>
> ​	注意：默认的单位为kb
>
> ```
> 演示命令：
> yangyang@yangyang-virtualmachine:~/Desktop$ df 
> df: /mnt/hgfs: 协议错误
> 文件系统          1K-块    已用    可用 已用% 挂载点
> udev             982640       0  982640    0% /dev
> tmpfs            201812    8928  192884    5% /run
> /dev/sda1      16381864 8263340 7263332   54% /
> tmpfs           1009040     280 1008760    1% /dev/shm
> tmpfs              5120       4    5116    1% /run/lock
> tmpfs           1009040       0 1009040    0% /sys/fs/cgroup
> tmpfs            201812      68  201744    1% /run/user/1000
> yangyang@yangyang-virtualmachine:~/Desktop$ df -h
> df: /mnt/hgfs: 协议错误
> 文件系统        容量  已用  可用 已用% 挂载点
> udev            960M     0  960M    0% /dev
> tmpfs           198M  8.8M  189M    5% /run
> /dev/sda1        16G  7.9G  7.0G   54% /
> tmpfs           986M  280K  986M    1% /dev/shm
> tmpfs           5.0M  4.0K  5.0M    1% /run/lock
> tmpfs           986M     0  986M    0% /sys/fs/cgroup
> tmpfs           198M   68K  198M    1% /run/user/1000
> ```

> 6>du  	显示文件的内存大小
>
> 注意：与df命令不同的是du命令是对文件和目录磁盘使用的空间的查看

> 7>free	显示当前系统未使用的和已使用的内存数目，还可以显示被内核使用的内存缓冲区
>
> ```
> 演示命令：
> free -m
>               total        used        free      shared  buff/cache   available
> Mem:           1970        1103         144          15         722         638
> Swap:          4093           5        4088
>
>
> 延时命令：
> total        used        free      shared  buff/cache   available
> Mem:           1970        1103         144          15         722         638
> Swap:          4093           5        4088
>
> 全部		  已使用的      剩余的  共享的    缓存
> total = used + free
>
> ```

> 8>其他
>
> ```
> reboot:重启
> shutdown -h now   :立即关机
> shutdown -r now   :立即重启
> shutdown -h +1    ：1分钟之后重启
> clear   :清屏，作用类似于ctrl+l
>
> init 0: 关机
> init 6: 重启
> ```

> 9>ping   检测网络的连通性
>
> 10>ifconfig  查看网卡信息，ip地址等，相当于windows上的ipconfig
>
> ```
> 演示命令：
> yangyang@yangyang-virtualmachine:~/Desktop$ ifconfig
> ens33     Link encap:以太网  硬件地址 00:0c:29:8c:1e:35  
>           inet 地址:10.36.131.192  广播:10.36.131.255  掩码:255.255.255.0
>           inet6 地址: fe80::2025:7389:1aad:8cc8/64 Scope:Link
>           UP BROADCAST RUNNING MULTICAST  MTU:1500  跃点数:1
>           接收数据包:73625 错误:0 丢弃:0 过载:0 帧数:0
>           发送数据包:29011 错误:0 丢弃:0 过载:0 载波:0
>           碰撞:0 发送队列长度:1000 
>           接收字节:9001772 (9.0 MB)  发送字节:2018148 (2.0 MB)
>
> lo        Link encap:本地环回  
>           inet 地址:127.0.0.1  掩码:255.0.0.0
>           inet6 地址: ::1/128 Scope:Host
>           UP LOOPBACK RUNNING  MTU:65536  跃点数:1
>           接收数据包:42021 错误:0 丢弃:0 过载:0 帧数:0
>           发送数据包:42021 错误:0 丢弃:0 过载:0 载波:0
>           碰撞:0 发送队列长度:1000 
>           接收字节:3381269 (3.3 MB)  发送字节:3381269 (3.3 MB)
> ```
>
> 