import psutil, os, sys
mem_perc = 0 #init var
swap_perc = 0 #init var
mbytes_sent = 0 #init var
mbytes_recv = 0 #init var
cpu_perc = 0 #init var
swap = 0 #init var
mem = 0 #init var
net = 0 #init var



def disp(degree):
    global cpu_perc
    global swap
    global swap_perc
    global mem
    global mem_perc
    global net
    global mbytes_sent
    global mbytes_recv

    cpu_perc = psutil.cpu_percent(interval=1, percpu=True)
    swap = psutil.swap_memory()
    swap_perc = swap.percent
    mem = psutil.virtual_memory()
    mem_perc = mem.percent
    net = psutil.net_io_counters()
    mbytes_sent = float(net.bytes_sent) / 1048576
    mbytes_recv = float(net.bytes_recv) / 1048576

    os.system('clear') #clear the screen

    print "-"*30
    print "CPU"
    print "-"*30
    print "CPU Temperature: " , degree, "'C"
    for i in range(len(cpu_perc)):
        print "CPU Core", str(i+1),":", str(cpu_perc[i]), "%"

    print "-"*30
    print "MEMORY"
    print "-"*30
    print "RAM: ", mem_perc, "%"
    print "Swap: ", swap_perc, "%"
    print "-"*30
    print "NETWORK"
    print "-"*30
    print "MB sent: ", mbytes_sent
    print "MB received: ", mbytes_recv
    print "-"*30
    print "DISKS"
    print "-"*30

    if len(sys.argv) > 1:
        for disk in range(1, len(sys.argv)):
            tmp = psutil.disk_usage(sys.argv[disk])
            print sys.argv[disk], "\n"
            print "Megabytes total: ",
            print str(float(tmp.total) / 1048576)
            print "Megabytes used: ",
            print str(float(tmp.used) / 1048576)
            print "Megabytes free: ",
            print str(float(tmp.free) / 1048576)
            print "Percentage used: ",
            print tmp.percent, "\n"

def main():
    print("Press Ctrl+C to exit")
    while True:
        temp = open("/sys/class/thermal/thermal_zone0/temp").read().strip().lstrip('temperature :').rstrip(' C')
        temp = float(temp) / 1000
        disp(temp)

main()