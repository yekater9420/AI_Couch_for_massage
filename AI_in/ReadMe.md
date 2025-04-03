# AI_Couch_for massage

##**# Part I: Why we do it?**

Nothing, _Just for fun._

***
##**# Part II: Requirements**

Configuring the project environment is simple. 

###Firstly, you need to install Python 3.9 or higher. Then, you need to install the following packages:

###Secondly，Just run the following command in the project directory:

`pip install -r requirements.txt`

###Thirdly，Download the Ali SDK as _alibabacloud-nls-python-sdk-dev.zip_ in the project。
Unzip it and then open it in its _root directory_ and enter the following instructions

`pip install -r requirements.txt`

If u do that whitout any error, the SDK has been installed successfully.

###Fourthly，You need to register an Ali account and get AccessKeyID and AccessKeySecret. These are taught on Alibaba's official website.
[Alibaba's official website](https://www.aliyun.com/)

When u have got that, you need to configure them as system variables for privacy protection.

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

###Fifthly，You need to download the _ffmpeg_  and unzip it in the project directory.

####If your operating system is _linux_:
Install ffmpeg: Different Linux distributions have different commands for installing ffmpeg.

_Ubuntu/Debia_:

`sudo apt-get update`

`sudo apt-get install ffmpeg`

_CentOS/RHEL_:

`sudo yum install epel-release`

`sudo yum install ffmpeg ffmpeg-devel`

Verify installation: After the installation is complete, you can verify that ffmpeg and ffprobe were successfully installed by entering the following command into the terminal:

`ffmpeg -version`

`ffprobe -version`

Modify the code: In the code, you do not need to specify the PATH to the executable file as you do on Windows systems, because Linux systems look for the executable file from the environment variable path.

###If you do all of them successfully, Congratulations to you!The environment is ready to go.

***

**# Part III: Project Structure**

***

**# Part IV: How to use it?**

