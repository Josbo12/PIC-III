import subprocess


command1 = ["grep 'cpu' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'"]
p1 = subprocess.Popen(command1, stdout=subprocess.PIPE, shell=True)
(output1, err1) = p1.communicate()

command2 = ["free -m"]
p2 = subprocess.Popen(command2, stdout=subprocess.PIPE, shell=True)
(output2, err2) = p2.communicate()
mem = output2.split(" ")
mem = [val for val in mem if val != '']
print mem

print "CPU usage: " + "%.2f" % float(output1) + "%"
print "MEM usage: " + "%.2f" % ((float(mem[7])/float(mem[6]))*100) + "%"
