# module_package_import
this is a Python module and package import example.

假定如下文件结构：
![在这里插入图片描述]
之所以设置了一个相对复杂的文件结构，是为了接下来做各种测试验证各种导入模式。
以下所有涉及的测试和文件结构，都已上传 - github -，有需要的朋友可以整个clone下来实践下整个代码。
由于逻辑上有点复杂，以下测试需要一定的时间进行研究。

概念1：包package是文件夹, 模块module是.py文件

概念2：绝对导入和相对导入(又分为隐式相对导入和显式相对导入)

    绝对导入：基于完整路径导入模块(.py文件)，比如`from pa.sub import deep`
    相对导入-显式：基于相对路径符号导入模块，比如在spam.py中写入`from . import grok`
    相对导入-隐式：不采用相对路径符号而以默认相对关系导入，比如在spam.py中写入`import grok`

    这三种方式中，python规则不推荐用隐式相对导入，因为没有路径说明，很可能直接导入了一个跟系统文件重名的模块文件，导致覆盖系统文件，比如import string，这就会覆盖string文件。
    相对导入中，.代表本级文件夹，…代表上一级文件夹，比如在deep.py文件中，可以写`from .. import grok`，其中…代表的就是pa.sub文件夹的路径，而在spam.py文件中可以写`from . import isolate`，其中.代表的就是pa文件夹
    而绝对导入中，每个新的文件夹导入本质上就是导入该文件夹下的`__init__`文件，

概念3：python永远基于`__main__`函数作为入口，能够导入同层和下层的package和module的名称，绝不可能导入更上一层的package/module。
这里需要说明，一个.py文件有两种加载方式，一种是作为script运行或者在IDE中直接run file，另一种是作为module被import，两种方式完全不同的影响__main__函数入口。当作为script运行时，该文件的自有名称就会被__main__替代掉，而当作为module被import时，该文件的名称就是路径+文件名，两种方式都可以通过print(name)来查看。比如bar.py文件，通常作为module被主程序导入，他的__name__属性就是pb.bar，而如果坚持要运行bar.py，则他的__name__属性就会被覆盖成__main__来运行作为入口。

接下来看实例：
实例1：train.py作为主函数运行
在train.py运行后输出见右边，具体解释下每个输出。
![在这里插入图片描述]

    首先输出`this is train.py: _ _main__` ，这句输出是通过train.py中打印__name__得到，说明__name__ = __main__
    然后输出`this is pa __init__: pa`，这句输出是通过在pa文件夹下__init__文件中事先写了一句print打印__init__文件的__name__属性得到，说明from pa import spam这句会先执行pa下的__init__文件，然后才执行spam.py，且__init__文件的名称就是pa
    然后输出`this is spam.py: pa.spam` ，这句输出是spam文件打印自己的__name__属性，如下，也证明此时spam的__name__属性是由包名+文件名的组合
    然后输出`this is grok.py: pa.grok`，这句输出是spam文件调用grok模块后grok文件的输出
![在这里插入图片描述]
    然后输出`this is pb __init__: pb`，这条是在grok.py文件中调用pb.bar，其中pb的__init__文件的print输出。
    然后输出`this is bar.py: pb.bar`，这条是bar.py本身print __name__的输出
    然后输出`this is sub __init__ pa.sub`，这条是bar.py内进行的相对导入`from pa.sub import deep`，先执行pa的__init__，然后执行deep本身的打印
    然后输出`this is deep:pa.sub.deep`，就是deep.py本身的print __name__
    最后输出`this is isolate2: pa.isolate2`，这是deep.py 执行的相对二级调用`from .. import isolate2`

以上详细的代码输入可以查看github上的源码：通过实验，可以完整验证绝对导入/相对导入/导入执行过程/__main__函数命名方式，希望能够帮到你解惑。
