# sysmon-1.0.1
`sysmon.py` is a program designed to monitor your system.

Install by navigating to the directory you have Setup.py stored in.

Then, type `sudo python Setup.py` in the terminal.
It will not work with python3, as it is written in python2.

To use, type `sysmon` into the command line.

The log is stored at `/var/log/sysmon.log`.
This program will work with your LINUX system provided you have the right hardware. 

## Development
**Note: These examples are written in Python 2.7**

    sudo apt-get install pip
    sudo pip install psutil

Now that we have the modules installed, we can start coding. 

First, create a file called `usage.py`.

    gedit ~/usage.py

Start by importing `psutil`

    import psutil


Then, create a function to monitor the percentage your CPU cores are running at.

<!-- language: python -->

    def cpu_perc(): 

        cpu_perc = psutil.cpu_percent(interval=1, percpu=True) 
        for i in range(len(cpu_perc)):
            print "CPU Core", str(i+1),":", str(cpu_perc[i]), "%"

Let's break that down a bit, shall we?

The first line, `cpu_num = psutil.cpu_percent(interval=1, percpu=True)`, finds the percentage that the cores in your CPU are running at and assigns it to a list called `cpu_perc`.

This loop right here

<!-- language: python -->

    for i in range(len(cpu_num)):
        print "CPU Core", str(i+1),":", str(cpu_perc[i]), "%"
        
is a for loop that prints out the current percentage of each of your CPU cores.

Let's add the RAM usage.

Create a function called `ram_perc`.

<!-- language: python -->

    def ram_perc():
        mem = psutil.virtual_memory()
        mem_perc = mem.percent
        print "RAM: ", mem_perc, "%"
        

`psutil.virtual_memory` gives a data set containing different facts about the RAM in your computer.

Next, you can add some facts about your network.

<!-- language: python -->

    def net():
        net = psutil.net_io_counters()
        mbytes_sent = float(net.bytes_sent) / 1048576
        mbytes_recv = float(net.bytes_recv) / 1048576
        print "MB sent: ", mbytes_sent
        print "MB received: ", mbytes_recv
        
Since `psutil.net_io_counters()` only gives us information about packets sent and received in bytes, some converting was necessary. 

To get some information about swap space, add this function.

<!-- language: python -->

    def swap_perc():
        swap = psutil.swap_memory()
        swap_perc = swap.percent
        
This one is pretty straightforward.

Temperature is kind of hard to do, so you may need to do some research of your own to figure out what will work with your hardware.
You will have to display the contents of a certain file.

Disk usage is a lot easier than temperature. All you need to do is to pass the disk you want to monitor (i.e: `/`) through a certain function.

<!-- language: python -->

    def disks():
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
            

The original output of `psutil.disk_usage` is this,

    >>>psutil.disk_usage('/')
    sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)

but you can also just receive `total`, `used`, `free`, or `percent`.


The completed program: (the aforementioned functions were combined)

<!-- language: python -->

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


The line `temp = open("/sys/class/thermal/thermal_zone0/temp").read().strip().lstrip('temperature :').rstrip(' C')` might not work with your hardware configuration.

Run this program from the command line. Pass the disks you want to monitor as arguments from the command line.

    $ python usage.py /
    
    Press Ctrl+C to exit
    
    ------------------------------
    CPU
    ------------------------------
    CPU Temperature:  39.0 'C
    CPU Core 1 : 4.8 %
    CPU Core 2 : 1.0 %
    CPU Core 3 : 0.0 %
    CPU Core 4 : 4.9 %
    ------------------------------
    MEMORY
    ------------------------------
    RAM:  33.6 %
    Swap:  6.4 %
    ------------------------------
    NETWORK
    ------------------------------
    MB sent:  2.93382358551
    MB received:  17.2131490707
    ------------------------------
    DISKS
    ------------------------------
    / 

    Megabytes total:  13952.484375
    Megabytes used:  8542.6640625
    Megabytes free:  4678.5703125
    Percentage used:  61.2 

    /media/calvin/Data 

    Megabytes total:  326810.996094
    Megabytes used:  57536.953125
    Megabytes free:  269274.042969
    Percentage used:  17.6 

**Disclaimer: none of this is too relevant anymore. I wrote all this in 5th grade and I just uploaded it as a record.**
  [1]: https://github.com/calthecoder/sysmon-1.0.1/archive/master.zip "sysmon"
