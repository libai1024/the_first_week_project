#!/bin/bash
#pycontrol 
echo "------------WELCOME TO PYCONTROL------------"

while :
do
echo "#1：进程数量显示"
echo "#2: 进程停止"
echo "#3: 进程启动"
echo "#4: 进程重启"
echo "#5/q: 退出脚本"
echo "please input a number:"
read num
case $num in
        #1：进程数量显示       
	1)
		
		echo "------------[pycontrol]所有进程如下------------"
		ps -ef|grep "\.py"
		;;
	#2: 进程停止
	2)	
		echo "请输入PID或PIDs:"
		read  PROCESS	
		echo "------------[pycontrol]停止操作进行中------------"		
		if [ $PROCESS -lt 1 ]
		then
			echo "进程停止操作缺少参数 PID "
  			exit 1
		fi
		
		for i in $PROCESS
		do
  			echo "Killed the $i process "
  			kill -15 $i
		done
		echo "*************************ANS****************************"
		ps -ef|grep "\.py"
		;;
	3)
	#3: 进程启动
		echo "输入文件名:"
		read filename
		echo $filename
		nohup python3 -u  $filename > output.log 日志 2>&1 &

		echo "------------[pycontrol]$filename 已启动------------"
		ps -f|grep "\.py"
		;;
	4)
	#4： 进程重启
		
		PROCESS=`ps -f|grep "\.py"|awk '{ print $2}'`	
		F=`ps -ef|grep "\.py"|awk '{ print $10}'`
		PROCESS=($PROCESS)
		F=($F)	
		for(( i=0;i<(${#PROCESS[*]}-1);i++)) 
		do
  		echo "--------------------------Killed the  process [ ${PROCESS[i]} ]"		
		findpid='/proc/'${PROCESS[i]}
	
		ans=`ls -al $findpid|grep "cwd -> "`
		ans=($ans)
		string=${F[i]}
		array=(${string//// }) 
		temp=${array[-1]}		
		abspath=${ans[-1]}'/'$temp
		echo $abspath
		kill -15  ${PROCESS[i]}
	 	nohup python3 -u  $abspath > output.log 日志 2>&1 &
		done

		echo "------------[pycontrol]${PROCESS[i]} - $abspath 已重启------------"
		ps -f|grep "\.py"
		;;
	5)
		exit 1
		;;
	q)
		exit 1 
		;;
esac
done	
