# 股票笔记本项目
Authors:
- 前端：Linking
- 后端：AllenKe

# 相关技术
- 前端：html,css,js,vue
- 后端：python,flask

# 前端部署
## nginx部署

```shell
# 从官网下载相关安装包
wget http://nginx.org/download/nginx-1.12.1.tar.gz

## 解压   
tar -zxvf nginx-1.12.1.tar.gz  

## 安装一些依赖包
yum -y install gcc gcc-c++ automake pcre pcre-devel zlib zlib-devel openssl openssl-devel     

# 放入/usr/local/目录下,推荐，当然也可以是别的位置
mv nginx-1.12.1 /usr/local/ 

# 进入解压后的文件价
cd nginx-1.12.1

# 添加用户组
groupadd nginx
# 添加用户名                        
useradd nginx -g nginx -s /sbin/nologin -M 

# 加入tcp模块，https模块和状态监控模块一起编译（需要什么模块根据自己的需求进行编译），并指定用户名，用户组
./configure --with-stream --with-stream_ssl_module --with-http_stub_status_module --user=nginx --group=nginx 
# 编译 安装        
make && make install     
```

# 后端部署
## 启动脚本

```shell
# 在stock_notes目录里面有个启动脚本svrctl.sh

sh svrctl.sh <start_base|start_test|stop|restart|ps>

    - start_base    :   启动基础环境的测试。
    - start_test    :   启动测试环境的测试.
    - stop          :   停止基础环境的测试.
    - ps            :   查看基础环境的程序进程。   
```
