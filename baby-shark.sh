#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi
 
#TCP=$(cat /proc/net/tcp | grep "[0-9]: ")
#UDP=$(cat /proc/net/udp | grep "[0-9]: ")
#SOCKETS=$(ls -l $(find /proc/*/fd/ -type l 2>/dev/null) 2>/dev/null | grep socket)
 
#functions for further use
parse_ipv4()
{
    echo "$((16#${1:6:2})).$((16#${1:4:2})).$((16#${1:2:2})).$((16#${1:0:2}))"
}
 
parse_port()
{
    echo "$((16#$1))"
}
 
lookup_socket()
{
    inode=$1
    matches=$(echo "$SOCKETS" | grep "socket:\[$inode\]")
    pid=$(echo "$matches" | sed 's/.*\/proc\/\(.*\)\/fd\/.*/\1/')
    echo $pid
}
 
get_program()
{
    ps=$(ps --no-headers -f $1)
    a=($ps)
    program=${a[8]}
    echo $program
}
 
 
#sinner
while true
do
     
     
    MOREFSUN="$(netstat -antulpn | grep "tcp" | cut -d ":" -f 2 | awk '{print $1}')";
 
    for val in $MOREFSUN;
 
do
 
processname="$(lsof  -i tcp:${val} | cut -d "/" -f 2 | awk '{print $1}')";
pid="$(lsof -i tcp:${val} | tail -n +2 | awk '{print $2}')"
  
if [[ $processname != *"wexond"* ]];then
         
         
if [[ $processname == *"nc"* ]]; then
  echo "--------------------------------------------NETCAT threat!!!------------------------";
 
  echo "NETCAT THREAT!";
  echo "----------------------------------------------------------------------------------";
  echo "-------port:$val";

  lsof -i tcp:${val} | awk 'NR!=1 {print $2}' | xargs kill
  sleep 3;
         
elif [[ $processname == *"netcat"* ]]; then
  echo "--------------------------------------------NETCAT threat!!!------------------------";
  lsof -i tcp:$val
  echo "NETCAT THREAT!";
  echo "----------------------------------------------------------------------------------";
  echo "-------port:$val";
  #mpg123  netcat.mp3
  lsof -i tcp:${val} | awk 'NR!=1 {print $2}' | xargs kill
  sleep 3;
elif [[ $processname == *"php"* ]]; then
  echo "--------------------------------------------php revshell!!!------------------------";
  #mpg123 php.mp3
  echo "PHP REVSHELL THREAT!";
  lsof -i tcp:$val
  echo "----------------------------------------------------------------------------------";
  echo "-------port:$val";
  lsof -i tcp:${val} | awk 'NR!=1 {print $2}' | xargs kill
 
  sleep 3;
elif [[ $processname == *"dnsmasq"* ]]; then
  echo "--------------------------------------------";
  lsof -i tcp:$val
  echo "Process name:$processname";
  echo "-------port:$val";
  echo "----------------------------------------------------------------------------------";
 
 
 
 
    sleep 3;  
elif [[ $processname == *"ruby"* ]]; then
  echo "--------------------------------------------";
  lsof -i tcp:$val
  echo "Process name:$processname";
  echo "-------port:$val";
  echo "----------------------------------------------------------------------------------";
  #mpg123 meterpreter.mp3
  lsof -i tcp:${val} | awk 'NR!=1 {print $2}' | xargs kill
  #fuser -k -n tcp $val;
  #fuser -k -n udp $val;  
  sleep 3;  
 
else
 
     

   echo "--------------------------------------------";
     
  if [[ $val == *"80"* ]]; then
    lsof -i tcp:$val
        echo "I've let it go";
        return
   
   elif [[ $val == *"443"* ]];then
    lsof -i tcp:$val
        echo "I've let it go";
        return
   
   elif [[ $val == *"3306"* ]];then
    echo "I've let it go";
        lsof -i tcp:$val
        return
   elif [[ $val == *"22"* ]];then
    echo "I've let it go";
        lsof -i tcp:$val
          
   else   
  lsof -i tcp:$val;
if [[ $processname == *"gram"* ]]; then
  echo "--------------------------------------------";
  lsof -i tcp:$val
  echo "Process name:$processname";
  echo "-------port:$val";
  echo "---------------------I've let it go-------------------------------------------------------------";
elif [[ $processname == *"wind"* ]]; then
  echo "--------------------------------------------";
  lsof -i tcp:$val
  echo "Process name:$processname";
  echo "-------port:$val";
  echo "----------------------------------------------------------------------------------";
elif [[ $processname == *"obfs4"* ]]; then
  echo "--------------------------------------------";
  lsof -i tcp:$val
  echo "Process name:$processname";
  echo "-------port:$val";
  echo "----------------------------------------------------------------------------------";
else
  echo "----pid:$pid"
  kill $pid
  fuser -k -n tcp $val;
  fuser -k -n udp $val;
   
  echo "port kapandi";
#  timeout 19 tcpdump -vi wlan0
fi
fi
fi
 
    fi  
done
 
 
done
