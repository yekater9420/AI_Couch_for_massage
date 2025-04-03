# AI智能按摩床

##**# Part I: 为什么我们要做它?**

Nothing, _Just for fun._

***
##**# Part II: 环境搭建**

搭建这个项目的环境非常简单：

###首先，您需要安装Python 3.9或更高版本。本项目所使用的为3.11

###第二，在根目录下面运行以下命令：

`pip install -r requirements.txt`

###第三，下载阿里SDK文件，_alibabacloud-nls-python-sdk-dev.zip_，将其解压，并在**根目录**下运行以下命令：

`pip install -r requirements.txt`

如果你做了这个没有报错，这个SDK已经安装完成。

###第四，你需要去阿里云官网注册一个账号，并获取你的AccessKeyID和AccessKeySecret，这些阿里官网上已经很详细了。
[Alibaba's official website](https://www.aliyun.com/)

当你获取到这两个以后，处于个人隐私问题，需要将其配置为环境变量

####If your operating system is _linux_:

Edit the `~/.bashrc` or `~/.zshrc` file (depending on your shell type) :

`nano ~/.bashrc`

Add the following at the end of the file:

`export ALIBABA_CLOUD_ACCESS_KEY_ID=YourAccessKeyID`

`export ALIBABA_CLOUD_ACCESS_KEY_SECRET=YourAccessKeySecret`

Save the file and exit the editor.
To make the configuration work:

`source ~/.bashrc`

####If your operating system is _windows_:
Go to the system properties and click on the "Advanced system settings" button.

Click on the "Environment Variables" button.

Click on the "New" button and add the following:

Name: `ALIBABA_CLOUD_ACCESS_KEY_ID`
Value: `YourAccessKeyID`

Click on the "New" button and add the following:

Name: `ALIBABA_CLOUD_ACCESS_KEY_SECRET`
Value: `YourAccessKeySecret`

Click on the "OK" button to close the dialog boxes.

Restart your computer or open a new command prompt window to apply the changes.


Fifthly，You need to install the "ffmpeg" in this project. 

If you do all of them successfully, Congratulations to you!The environment is ready to go.

***

**# Part III: 项目结构**

***

**# Part IV: 如何使用**

