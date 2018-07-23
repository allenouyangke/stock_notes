2#!/bin/bash
# -------------------------------------------------------------------------------
# Script_name: 	svrctl.sh
# Revision: 	1.0
# Date: 		2018/07/14
# Author: 		AllenKe
# Email: 		allenouyangke@icloud.com
# Description:	用于启动stock_notes项目。
#               sh scrctl.sh <start_base|start_test|stop|restart|ps>
# -------------------------------------------------------------------------------

start_base(){
    PNUM=`ps -ef | grep stock_notes.py | grep -v grep | wc -l`
    if [[ ${PNUM} != 0 ]];then
        echo "The process had been start, Please check! "
        exit 1
    fi
    # /usr/bin/nohup /root/.pyenv/shims/python /export/stock_notes/stock_notes.py runserver -h 0.0.0.0 -p 8888 &
    # 已将单个文件的开发方式改成了工程文件的形式，主要通过蓝图连接启动文件和app文件里的各个模块
    /usr/bin/nohup /root/.pyenv/shims/python /export/stock_notes/stock_notes_pro.py runserver -h 0.0.0.0 -p 8888 &
}

start_test(){
    PNUM=`ps -ef | grep stock_notes_test.py | grep -v grep | wc -l`
    if [[ ${PNUM} != 0 ]];then
        echo "The test process had been start, Please check! "
        exit 1
    fi
    /usr/bin/nohup /root/.pyenv/shims/python /export/stock_notes/test/stock_notes_test.py runserver -h 0.0.0.0 -p 9999 &
}

stop(){
    PNUM=`ps -ef | grep stock_notes.py | grep -v grep | wc -l`
    if [[ ${PNUM} == 0 ]];then
        echo "The processes had not start! "
        exit 1
    fi
    PLIST=`ps -ef | grep stock_notes.py | grep -v grep | awk '{print $2}'`
    for P_ID in ${PLIST[@]}
    do
        kill -9 ${P_ID}
    done
    PNUM=`ps -ef | grep stock_notes.py | grep -v grep | wc -l`
    if [[ ${PNUM} != 0 ]];then
        echo "The processes had not kill， Please check! "
        exit 1
    fi
    echo "The processes had been stop! "
}

restart(){
    echo "5秒后停止进程"
    sleep 5
    stop
    echo "10秒后启动进程"
    sleep 10
    start
}

psprocess(){
    ps -ef | grep stock_notes.py | grep -v grep
}

case $1 in
    start_base) start_base ;;
    start_test) start_test ;;
    stop) stop ;;
    restart) restart ;;
    ps) psprocess ;;
    *) 
    echo "Usge: Please enter the option (start_base|start_test|stop|restart|ps)"
    ;;
esac
