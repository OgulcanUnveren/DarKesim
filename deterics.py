import subprocess

filename = '/data/data/com.termux/dar_kesim/detergoogle.py'
filename2=  '/data/data/com.termux/dar_kesim/determinist.py'
#filename3='webapp/run.sh'
while True:
    """However, you should be careful with the '.wait()'"""
    p = subprocess.Popen('python '+filename2, shell=True).wait()
#    p1 = subprocess.Popen('python3 '+filename, shell=True).wait()
    #p2 = subprocess.Popen('bash '+filename3, shell=True).wait()    
    """#if your there is an error from running 'my_python_code_A.py', 
    the while loop will be repeated, 
    otherwise the program will break from the loop"""
    if p != 0:
        continue
    else:
        break
 #   if p1 != 0:
 #       continue
  #  else:
   #     break
 #   if p2 != 0:
  #     continue
  #  else:
   #     break
