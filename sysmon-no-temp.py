#!/usr/bin/env python
import sys, os ,datetime, time, psutil, getopt
version = "1.0.1"

cpu_perc = psutil.cpu_percent(interval=1, percpu=True) #test for number of cores


if len(cpu_perc) == 4:
                
        #
        mem_perc = 0 #init var
        swap_perc = 0 #init var
        mbytes_sent = 0 #init var
        mbytes_recv = 0 #init var
        cpu_perc = 0 #init var
        swap = 0 #init var
        mem = 0 #init var
        net = 0 #init var


        cpu1_list = []
        cpu2_list = []
        cpu3_list = []
        cpu4_list = []
        swap_list = []
        mem_list = []
        mbytes_sent_list = []
        mbytes_recv_list = []
        #
        def rtcheck(seconds):
                try:
                        seconds = int(seconds)
                        return seconds
                except ValueError:
                        return -1


        def getavg(l):
                out = 0
                for a in range(0,len(l)):
                        out = out+l[a]
                out = float(out) / len(l)
                return out
                        
        def gethigh(l):
                out = 0
                for a in range(0,len(l)):
                        if l[a] > out:
                                out = l[a]
                return out
                
        def getlow(l):
                out = 0
                h = gethigh(l)
                for a in range(0, len(l)):
                        if l[a] < h:
                                out = l[a]
                return out
                                
        def disp(degree,minutes,seconds):
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
                #print "CPU Temperature: " , temp, "'C"
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

        def main():
                global version
                avg = 0
                ver = 0
                run = 0
                help = 0
                check = 0
                runtime = 5
                degree = 0
                seccount = 0
                seclast = 0
                minutes = 0
                temp = 21
                tsum = 0
                ticker = 0
                exitmsg = ""
                
                print "sysmon" , version

                if ver == 1:
                        sys.exit()
                if help == 1:
                        usageinfo(check, run, exitmsg)
                if run == 1:
                        runtime = rtcheck(runtime)
                        if runtime < 1:
                                help = 1
                                exitmsg = "Seconds must be defined as an integer greater than zero."
                                usageinfo()

             
                bseconds = int(time.time())
                
                if avg == 0:
                        print("Press Ctrl+C to exit")
                
                try :
                  while True:
                         
                         #
                         disp(degree,minutes,seconds)
                         
                         cpu1_list.append(float(cpu_perc[0]))
                         cpu2_list.append(float(cpu_perc[1]))
                         cpu3_list.append(float(cpu_perc[2]))
                         cpu4_list.append(float(cpu_perc[3]))
                         
                         swap_list.append(swap_perc)
                         mem_list.append(mem_perc)
                         
                         mbytes_sent_list.append(mbytes_sent)
                         mbytes_recv_list.append(mbytes_recv)
                         
                         
                         	
                         time.sleep(1)
                         sys.stdout.flush()
                #When Ctrl-C is pressed, show summary data
                
                except KeyboardInterrupt :
                        pass
                        
                                
                #add this info for cpu, ram
                avg_cpu1_perc = getavg(cpu1_list) #get averages and print them
                avg_cpu2_perc = getavg(cpu2_list)
                avg_cpu3_perc = getavg(cpu3_list)
                avg_cpu4_perc = getavg(cpu4_list)
                avg_mem_perc = getavg(mem_list)
                avg_swap_perc = getavg(swap_list)
                
                high_cpu1_perc = gethigh(cpu1_list) #get highs and print them
                high_cpu2_perc = gethigh(cpu2_list)
                high_cpu3_perc = gethigh(cpu3_list)
                high_cpu4_perc = gethigh(cpu4_list)
                high_mem_perc = gethigh(mem_list)
                high_swap_perc = gethigh(swap_list)
                
                low_cpu1_perc = getlow(cpu1_list) #get lows and print them
                low_cpu2_perc = getlow(cpu2_list)
                low_cpu3_perc = getlow(cpu3_list)
                low_cpu4_perc = getlow(cpu4_list)
                low_mem_perc = getlow(mem_list)
                low_swap_perc = getlow(swap_list)
                
                #print "\n\nAverage CPU temperature was",tavg,"degrees Celsius"
                print "Average CPU1 percent was",avg_cpu1_perc,"%"
                print "Average CPU2 percent was",avg_cpu2_perc,"%"
                print "Average CPU3 percent was",avg_cpu3_perc,"%"
                print "Average CPU4 percent was",avg_cpu4_perc,"%"
                print "Average RAM percent was",avg_mem_perc,"%"	
                print "Average SWAP percent was",avg_swap_perc,"%\n"	
                
                #print "Highest CPU temperature was",tmax,"degrees Celsius"	
                print "Highest CPU1 percent was",high_cpu1_perc,"%"
                print "Highest CPU2 percent was",high_cpu2_perc,"%"
                print "Highest CPU3 percent was",high_cpu3_perc,"%"
                print "Highest CPU4 percent was",high_cpu4_perc,"%"
                print "Highest RAM percent was",high_mem_perc,"%"	
                print "Highest SWAP percent was",high_swap_perc,"%\n"	
                
                #print "Lowest CPU temperature was",tmin,"degrees Celsius"
                print "Lowest CPU1 percent was",low_cpu1_perc,"%"
                print "Lowest CPU2 percent was",low_cpu2_perc,"%"
                print "Lowest CPU3 percent was",low_cpu3_perc,"%"
                print "Lowest CPU4 percent was",low_cpu4_perc,"%"
                print "Lowest RAM percent was",low_mem_perc,"%"	
                print "Lowest SWAP percent was",low_swap_perc,"%\n"	
                
                
                
                if avg == 1:
                        return 0
                elif os.path.exists("/var/log/sysmon.log") == True:		
                        tod = datetime.datetime.now()
                        syslog = open ( "/var/log/sysmon.log" , "a" )
                        syslog.write ("---------------\n")
                        #syslog.write ("\nAverage CPU temperature was ")
                        #syslog.write (str(tavg))
                        #syslog.write (" degrees Celsius\n")
                        syslog.write ("\nAverage CPU1 percent was ")
                        syslog.write (str(avg_cpu1_perc))	
                        syslog.write ("\nAverage CPU2 percent was ")
                        syslog.write (str(avg_cpu2_perc))
                        syslog.write ("\nAverage CPU3 percent was ")
                        syslog.write (str(avg_cpu3_perc))
                        syslog.write ("\nAverage CPU4 percent was ")
                        syslog.write (str(avg_cpu4_perc))
                        syslog.write ("\nAverage RAM percent was ")
                        syslog.write (str(avg_mem_perc))
                        syslog.write ("\nAverage SWAP percent was ")
                        syslog.write (str(avg_swap_perc))
                        
                        #syslog.write ("\nHighest CPU temperature was ")
                        #syslog.write (str(tmax))
                        #syslog.write (" degrees Celsius\n")
                        syslog.write ("\nHighest CPU1 percent was ")
                        syslog.write (str(high_cpu1_perc))	
                        syslog.write ("\nHighest CPU2 percent was ")
                        syslog.write (str(high_cpu2_perc))
                        syslog.write ("\nHighest CPU3 percent was ")
                        syslog.write (str(high_cpu3_perc))
                        syslog.write ("\nHighest CPU4 percent was ")
                        syslog.write (str(high_cpu4_perc))
                        syslog.write ("\nHighest RAM percent was ")
                        syslog.write (str(high_mem_perc))
                        syslog.write ("\nHighest SWAP percent was ")
                        syslog.write (str(high_swap_perc))
                        
                        #syslog.write ("\nLowest CPU temperature was ")
                        #syslog.write (str(tmin))
                       # syslog.write (" degrees Celsius\n")
                        syslog.write ("\nLowest CPU1 percent was ")
                        syslog.write (str(low_cpu1_perc))	
                        syslog.write ("\nLowest CPU2 percent was ")
                        syslog.write (str(low_cpu2_perc))
                        syslog.write ("\nLowest CPU3 percent was ")
                        syslog.write (str(low_cpu3_perc))
                        syslog.write ("\nLowest CPU4 percent was ")
                        syslog.write (str(low_cpu4_perc))
                        syslog.write ("\nLowest RAM percent was ")
                        syslog.write (str(low_mem_perc))
                        syslog.write ("\nLowest SWAP percent was ")
                        syslog.write (str(low_swap_perc))
                        
                        syslog.write ("\n\nDATE/TIME: ")
                        syslog.write (str(tod))
                        syslog.write ("\n\n---------------\n")
                        print("Log has been updated")
                        
                else:
                        print("Could not locate log file.  Please re-install.")
                        return 1
                        
elif len(cpu_perc) == 2:
                
        #
        mem_perc = 0 #init var
        swap_perc = 0 #init var
        mbytes_sent = 0 #init var
        mbytes_recv = 0 #init var
        cpu_perc = 0 #init var
        swap = 0 #init var
        mem = 0 #init var
        net = 0 #init var


        cpu1_list = []
        cpu2_list = []
        swap_list = []
        mem_list = []
        mbytes_sent_list = []
        mbytes_recv_list = []
        #
        def rtcheck(seconds):
                try:
                        seconds = int(seconds)
                        return seconds
                except ValueError:
                        return -1


        def getavg(l):
                out = 0
                for a in range(0,len(l)):
                        out = out+l[a]
                out = float(out) / len(l)
                return out
                        
        def gethigh(l):
                out = 0
                for a in range(0,len(l)):
                        if l[a] > out:
                                out = l[a]
                return out
                
        def getlow(l):
                out = 0
                h = gethigh(l)
                for a in range(0, len(l)):
                        if l[a] < h:
                                out = l[a]
                return out
                                
        def disp(degree,minutes,seconds):
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
                #print "CPU Temperature: " , temp, "'C"
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

        def main():
                global version
                avg = 0
                ver = 0
                run = 0
                help = 0
                check = 0
                runtime = 5
                degree = 0
                seccount = 0
                seclast = 0
                minutes = 0
                temp = 21
                tsum = 0
                ticker = 0
                exitmsg = ""
                
                print "sysmon" , version

                if ver == 1:
                        sys.exit()
                if help == 1:
                        usageinfo(check, run, exitmsg)
                if run == 1:
                        runtime = rtcheck(runtime)
                        if runtime < 1:
                                help = 1
                                exitmsg = "Seconds must be defined as an integer greater than zero."
                                usageinfo()

                bseconds = int(time.time())
                
                if avg == 0:
                        print("Press Ctrl+C to exit")
                
                try :
                  while True:
                
                         disp(degree,minutes,seconds)
                         
                         cpu1_list.append(float(cpu_perc[0]))
                         cpu2_list.append(float(cpu_perc[1]))
                                                  
                         swap_list.append(swap_perc)
                         mem_list.append(mem_perc)
                         
                         mbytes_sent_list.append(mbytes_sent)
                         mbytes_recv_list.append(mbytes_recv)
                         
                         
                         
                         time.sleep(1)
                         sys.stdout.flush()
                #When Ctrl-C is pressed, show summary data
                
                except KeyboardInterrupt :
                        pass
                        
                
                
                #add this info for cpu, ram
                avg_cpu1_perc = getavg(cpu1_list) #get averages and print them
                avg_cpu2_perc = getavg(cpu2_list)
                avg_mem_perc = getavg(mem_list)
                avg_swap_perc = getavg(swap_list)
                
                high_cpu1_perc = gethigh(cpu1_list) #get highs and print them
                high_cpu2_perc = gethigh(cpu2_list)
                high_mem_perc = gethigh(mem_list)
                high_swap_perc = gethigh(swap_list)
                
                low_cpu1_perc = getlow(cpu1_list) #get lows and print them
                low_cpu2_perc = getlow(cpu2_list)
                low_mem_perc = getlow(mem_list)
                low_swap_perc = getlow(swap_list)
                
                
                print "Average CPU1 percent was",avg_cpu1_perc,"%"
                print "Average CPU2 percent was",avg_cpu2_perc,"%"
                print "Average RAM percent was",avg_mem_perc,"%"	
                print "Average SWAP percent was",avg_swap_perc,"%\n"	
                
                
                print "Highest CPU1 percent was",high_cpu1_perc,"%"
                print "Highest CPU2 percent was",high_cpu2_perc,"%"
                print "Highest RAM percent was",high_mem_perc,"%"	
                print "Highest SWAP percent was",high_swap_perc,"%\n"	
                
                
                print "Lowest CPU1 percent was",low_cpu1_perc,"%"
                print "Lowest CPU2 percent was",low_cpu2_perc,"%"
                print "Lowest RAM percent was",low_mem_perc,"%"	
                print "Lowest SWAP percent was",low_swap_perc,"%\n"	
                
                
                
                if avg == 1:
                        return 0
                elif os.path.exists("/var/log/sysmon.log") == True:		
                        tod = datetime.datetime.now()
                        syslog = open ( "/var/log/sysmon.log" , "a" )
                        syslog.write ("---------------\n")
                        
                        syslog.write ("\nAverage CPU1 percent was ")
                        syslog.write (str(avg_cpu1_perc))	
                        syslog.write ("\nAverage CPU2 percent was ")
                        syslog.write (str(avg_cpu2_perc))
                        
                        syslog.write ("\nAverage RAM percent was ")
                        syslog.write (str(avg_mem_perc))
                        syslog.write ("\nAverage SWAP percent was ")
                        syslog.write (str(avg_swap_perc))
                        
                        
                        syslog.write ("\nHighest CPU1 percent was ")
                        syslog.write (str(high_cpu1_perc))	
                        syslog.write ("\nHighest CPU2 percent was ")
                        syslog.write (str(high_cpu2_perc))
                        
                        syslog.write ("\nHighest RAM percent was ")
                        syslog.write (str(high_mem_perc))
                        syslog.write ("\nHighest SWAP percent was ")
                        syslog.write (str(high_swap_perc))
                        
                        
                        syslog.write ("\nLowest CPU1 percent was ")
                        syslog.write (str(low_cpu1_perc))	
                        syslog.write ("\nLowest CPU2 percent was ")
                        syslog.write (str(low_cpu2_perc))
                        
                        syslog.write ("\nLowest RAM percent was ")
                        syslog.write (str(low_mem_perc))
                        syslog.write ("\nLowest SWAP percent was ")
                        syslog.write (str(low_swap_perc))
                        
                        syslog.write ("\n\nDATE/TIME: ")
                        syslog.write (str(tod))
                        syslog.write ("\n\n---------------\n")
                        print("Log has been updated")
                        
                else:
                        print("Could not locate log file.  Please re-install.")
                        return 1
                        
elif len(cpu_perc) == 8:
                
        #
        mem_perc = 0 #init var
        swap_perc = 0 #init var
        mbytes_sent = 0 #init var
        mbytes_recv = 0 #init var
        cpu_perc = 0 #init var
        swap = 0 #init var
        mem = 0 #init var
        net = 0 #init var


        cpu1_list = []
        cpu2_list = []
        cpu3_list = []
        cpu4_list = []
        cpu5_list = []
        cpu6_list = []
        cpu7_list = []
        cpu8_list = []
        swap_list = []
        mem_list = []
        mbytes_sent_list = []
        mbytes_recv_list = []
        #
        def rtcheck(seconds):
                try:
                        seconds = int(seconds)
                        return seconds
                except ValueError:
                        return -1


        def getavg(l):
                out = 0
                for a in range(0,len(l)):
                        out = out+l[a]
                out = float(out) / len(l)
                return out
                        
        def gethigh(l):
                out = 0
                for a in range(0,len(l)):
                        if l[a] > out:
                                out = l[a]
                return out
                
        def getlow(l):
                out = 0
                h = gethigh(l)
                for a in range(0, len(l)):
                        if l[a] < h:
                                out = l[a]
                return out
                                
        def disp(temp,degree,minutes,seconds):
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
                #print "CPU Temperature: " , temp, "'C"
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

        def main():
                global version
                avg = 0
                ver = 0
                run = 0
                help = 0
                check = 0
                runtime = 5
                degree = 0
                seccount = 0
                seclast = 0
                minutes = 0
                temp = 21
                tsum = 0
                ticker = 0
                exitmsg = ""
                
                print "sysmon" , version

                if ver == 1:
                        sys.exit()
                if help == 1:
                        usageinfo(check, run, exitmsg)
                if run == 1:
                        runtime = rtcheck(runtime)
                        if runtime < 1:
                                help = 1
                                exitmsg = "Seconds must be defined as an integer greater than zero."
                                usageinfo()

                prevtemp = 21
                tmax = 0
                tmin = 1000
                bseconds = int(time.time())
                
                if avg == 0:
                        print("Press Ctrl+C to exit")
                
                try :
                  while True:
                         
                         #
                         disp(degree,minutes,seconds)
                         
                         cpu1_list.append(float(cpu_perc[0]))
                         cpu2_list.append(float(cpu_perc[1]))
                         cpu3_list.append(float(cpu_perc[2]))
                         cpu4_list.append(float(cpu_perc[3]))
                         cpu5_list.append(float(cpu_perc[4]))
                         cpu6_list.append(float(cpu_perc[5]))
                         cpu7_list.append(float(cpu_perc[6]))
                         cpu8_list.append(float(cpu_perc[7]))
                         
                         swap_list.append(swap_perc)
                         mem_list.append(mem_perc)
                         
                         mbytes_sent_list.append(mbytes_sent)
                         mbytes_recv_list.append(mbytes_recv)
                         
                         
                          	
                         time.sleep(1)
                         sys.stdout.flush()
                #When Ctrl-C is pressed, show summary data
                
                except KeyboardInterrupt :
                        pass
                        
                tavg = tsum / ticker
                tavg = round(tavg, 1)
                
                #add this info for cpu, ram
                avg_cpu1_perc = getavg(cpu1_list) #get averages and print them
                avg_cpu2_perc = getavg(cpu2_list)
                avg_cpu3_perc = getavg(cpu3_list)
                avg_cpu4_perc = getavg(cpu4_list)
                avg_cpu5_perc = getavg(cpu5_list) #get averages and print them
                avg_cpu6_perc = getavg(cpu6_list)
                avg_cpu7_perc = getavg(cpu7_list)
                avg_cpu8_perc = getavg(cpu8_list)
                avg_mem_perc = getavg(mem_list)
                avg_swap_perc = getavg(swap_list)
                
                high_cpu1_perc = gethigh(cpu1_list) #get highs and print them
                high_cpu2_perc = gethigh(cpu2_list)
                high_cpu3_perc = gethigh(cpu3_list)
                high_cpu4_perc = gethigh(cpu4_list)
                high_cpu5_perc = gethigh(cpu5_list) #get highs and print them
                high_cpu6_perc = gethigh(cpu6_list)
                high_cpu7_perc = gethigh(cpu7_list)
                high_cpu8_perc = gethigh(cpu8_list)                
                high_mem_perc = gethigh(mem_list)
                high_swap_perc = gethigh(swap_list)
                
                low_cpu1_perc = getlow(cpu1_list) #get lows and print them
                low_cpu2_perc = getlow(cpu2_list)
                low_cpu3_perc = getlow(cpu3_list)
                low_cpu4_perc = getlow(cpu4_list)
                low_cpu5_perc = getlow(cpu5_list) #get lows and print them
                low_cpu6_perc = getlow(cpu6_list)
                low_cpu7_perc = getlow(cpu7_list)
                low_cpu8_perc = getlow(cpu8_list)
                low_mem_perc = getlow(mem_list)
                low_swap_perc = getlow(swap_list)
                
                #print "\n\nAverage CPU temperature was",tavg,"degrees Celsius"
                print "Average CPU1 percent was",avg_cpu1_perc,"%"
                print "Average CPU2 percent was",avg_cpu2_perc,"%"
                print "Average CPU3 percent was",avg_cpu3_perc,"%"
                print "Average CPU4 percent was",avg_cpu4_perc,"%"
                print "Average CPU5 percent was",avg_cpu5_perc,"%"
                print "Average CPU6 percent was",avg_cpu6_perc,"%"
                print "Average CPU7 percent was",avg_cpu7_perc,"%"
                print "Average CPU8 percent was",avg_cpu8_perc,"%"
                print "Average RAM percent was",avg_mem_perc,"%"	
                print "Average SWAP percent was",avg_swap_perc,"%\n"	
                
                #print "Highest CPU temperature was",tmax,"degrees Celsius"	
                print "Highest CPU1 percent was",high_cpu1_perc,"%"
                print "Highest CPU2 percent was",high_cpu2_perc,"%"
                print "Highest CPU3 percent was",high_cpu3_perc,"%"
                print "Highest CPU4 percent was",high_cpu4_perc,"%"
                print "Highest CPU5 percent was",high_cpu5_perc,"%"
                print "Highest CPU6 percent was",high_cpu6_perc,"%"
                print "Highest CPU7 percent was",high_cpu7_perc,"%"
                print "Highest CPU8 percent was",high_cpu8_perc,"%"
                print "Highest RAM percent was",high_mem_perc,"%"	
                print "Highest SWAP percent was",high_swap_perc,"%\n"	
                
                #print "Lowest CPU temperature was",tmin,"degrees Celsius"
                print "Lowest CPU1 percent was",low_cpu1_perc,"%"
                print "Lowest CPU2 percent was",low_cpu2_perc,"%"
                print "Lowest CPU3 percent was",low_cpu3_perc,"%"
                print "Lowest CPU4 percent was",low_cpu4_perc,"%"
                print "Lowest CPU5 percent was",low_cpu5_perc,"%"
                print "Lowest CPU6 percent was",low_cpu6_perc,"%"
                print "Lowest CPU7 percent was",low_cpu7_perc,"%"
                print "Lowest CPU8 percent was",low_cpu8_perc,"%"
                print "Lowest RAM percent was",low_mem_perc,"%"	
                print "Lowest SWAP percent was",low_swap_perc,"%\n"	
                
                
                
                if avg == 1:
                        return 0
                elif os.path.exists("/var/log/sysmon.log") == True:		
                        tod = datetime.datetime.now()
                        syslog = open ( "/var/log/sysmon.log" , "a" )
                        syslog.write ("---------------\n")
                        
                        syslog.write ("\nAverage CPU1 percent was ")
                        syslog.write (str(avg_cpu1_perc))	
                        syslog.write ("\nAverage CPU2 percent was ")
                        syslog.write (str(avg_cpu2_perc))
                        syslog.write ("\nAverage CPU3 percent was ")
                        syslog.write (str(avg_cpu3_perc))
                        syslog.write ("\nAverage CPU4 percent was ")
                        syslog.write (str(avg_cpu4_perc))
                        syslog.write ("\nAverage CPU5 percent was ")
                        syslog.write (str(avg_cpu5_perc))	
                        syslog.write ("\nAverage CPU6 percent was ")
                        syslog.write (str(avg_cpu6_perc))
                        syslog.write ("\nAverage CPU7 percent was ")
                        syslog.write (str(avg_cpu7_perc))
                        syslog.write ("\nAverage CPU8 percent was ")
                        syslog.write (str(avg_cpu8_perc))
                        syslog.write ("\nAverage RAM percent was ")
                        syslog.write (str(avg_mem_perc))
                        syslog.write ("\nAverage SWAP percent was ")
                        syslog.write (str(avg_swap_perc))
                        
                        
                        syslog.write ("\nHighest CPU1 percent was ")
                        syslog.write (str(high_cpu1_perc))	
                        syslog.write ("\nHighest CPU2 percent was ")
                        syslog.write (str(high_cpu2_perc))
                        syslog.write ("\nHighest CPU3 percent was ")
                        syslog.write (str(high_cpu3_perc))
                        syslog.write ("\nHighest CPU4 percent was ")
                        syslog.write (str(high_cpu4_perc))
                        syslog.write ("\nHighest CPU5 percent was ")
                        syslog.write (str(high_cpu5_perc))	
                        syslog.write ("\nHighest CPU6 percent was ")
                        syslog.write (str(high_cpu6_perc))
                        syslog.write ("\nHighest CPU7 percent was ")
                        syslog.write (str(high_cpu7_perc))
                        syslog.write ("\nHighest CPU8 percent was ")
                        syslog.write (str(high_cpu8_perc))
                        syslog.write ("\nHighest RAM percent was ")
                        syslog.write (str(high_mem_perc))
                        syslog.write ("\nHighest SWAP percent was ")
                        syslog.write (str(high_swap_perc))
                        
                        
                        syslog.write ("\nLowest CPU1 percent was ")
                        syslog.write (str(low_cpu1_perc))	
                        syslog.write ("\nLowest CPU2 percent was ")
                        syslog.write (str(low_cpu2_perc))
                        syslog.write ("\nLowest CPU3 percent was ")
                        syslog.write (str(low_cpu3_perc))
                        syslog.write ("\nLowest CPU4 percent was ")
                        syslog.write (str(low_cpu4_perc))
                        syslog.write ("\nLowest CPU5 percent was ")
                        syslog.write (str(low_cpu5_perc))	
                        syslog.write ("\nLowest CPU6 percent was ")
                        syslog.write (str(low_cpu6_perc))
                        syslog.write ("\nLowest CPU7 percent was ")
                        syslog.write (str(low_cpu7_perc))
                        syslog.write ("\nLowest CPU8 percent was ")
                        syslog.write (str(low_cpu8_perc))
                        syslog.write ("\nLowest RAM percent was ")
                        syslog.write (str(low_mem_perc))
                        syslog.write ("\nLowest SWAP percent was ")
                        syslog.write (str(low_swap_perc))
                        
                        syslog.write ("\n\nDATE/TIME: ")
                        syslog.write (str(tod))
                        syslog.write ("\n\n---------------\n")
                        print("Log has been updated")
                        
                else:
                        print("Could not locate log file.  Please re-install.")
                        return 1
                        
elif len(cpu_perc) == 6:
                
        #
        mem_perc = 0 #init var
        swap_perc = 0 #init var
        mbytes_sent = 0 #init var
        mbytes_recv = 0 #init var
        cpu_perc = 0 #init var
        swap = 0 #init var
        mem = 0 #init var
        net = 0 #init var


        cpu1_list = []
        cpu2_list = []
        cpu3_list = []
        cpu4_list = []
        cpu5_list = []
        cpu6_list = []
        swap_list = []
        mem_list = []
        mbytes_sent_list = []
        mbytes_recv_list = []
        #
        def rtcheck(seconds):
                try:
                        seconds = int(seconds)
                        return seconds
                except ValueError:
                        return -1


        def getavg(l):
                out = 0
                for a in range(0,len(l)):
                        out = out+l[a]
                out = float(out) / len(l)
                return out
                        
        def gethigh(l):
                out = 0
                for a in range(0,len(l)):
                        if l[a] > out:
                                out = l[a]
                return out
                
        def getlow(l):
                out = 0
                h = gethigh(l)
                for a in range(0, len(l)):
                        if l[a] < h:
                                out = l[a]
                return out
                                
        def disp(degree,minutes,seconds):
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
                #print "CPU Temperature: " , temp, "'C"
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

        def main():
                global version
                avg = 0
                ver = 0
                run = 0
                help = 0
                check = 0
                runtime = 5
                degree = 0
                seccount = 0
                seclast = 0
                minutes = 0
                temp = 21
                tsum = 0
                ticker = 0
                exitmsg = ""
                
                print "sysmon" , version

                if ver == 1:
                        sys.exit()
                if help == 1:
                        usageinfo(check, run, exitmsg)
                if run == 1:
                        runtime = rtcheck(runtime)
                        if runtime < 1:
                                help = 1
                                exitmsg = "Seconds must be defined as an integer greater than zero."
                                usageinfo()

                
                bseconds = int(time.time())
                
                if avg == 0:
                        print("Press Ctrl+C to exit")
                
                try :
                  while True:
                         
                         #
                         disp(degree,minutes,seconds)
                         
                         cpu1_list.append(float(cpu_perc[0]))
                         cpu2_list.append(float(cpu_perc[1]))
                         cpu3_list.append(float(cpu_perc[2]))
                         cpu4_list.append(float(cpu_perc[3]))
                         cpu5_list.append(float(cpu_perc[4]))
                         cpu6_list.append(float(cpu_perc[5]))
                         
                         
                         swap_list.append(swap_perc)
                         mem_list.append(mem_perc)
                         
                         mbytes_sent_list.append(mbytes_sent)
                         mbytes_recv_list.append(mbytes_recv)
                         
                         
                         
                         time.sleep(1)
                         sys.stdout.flush()
                #When Ctrl-C is pressed, show summary data
                
                except KeyboardInterrupt :
                        pass
                        
                tavg = tsum / ticker
                tavg = round(tavg, 1)
                
                #add this info for cpu, ram
                avg_cpu1_perc = getavg(cpu1_list) #get averages and print them
                avg_cpu2_perc = getavg(cpu2_list)
                avg_cpu3_perc = getavg(cpu3_list)
                avg_cpu4_perc = getavg(cpu4_list)
                avg_cpu5_perc = getavg(cpu5_list) #get averages and print them
                avg_cpu6_perc = getavg(cpu6_list)
                avg_mem_perc = getavg(mem_list)
                avg_swap_perc = getavg(swap_list)
                
                high_cpu1_perc = gethigh(cpu1_list) #get highs and print them
                high_cpu2_perc = gethigh(cpu2_list)
                high_cpu3_perc = gethigh(cpu3_list)
                high_cpu4_perc = gethigh(cpu4_list)
                high_cpu5_perc = gethigh(cpu5_list) #get highs and print them
                high_cpu6_perc = gethigh(cpu6_list)
                high_mem_perc = gethigh(mem_list)
                high_swap_perc = gethigh(swap_list)
                
                low_cpu1_perc = getlow(cpu1_list) #get lows and print them
                low_cpu2_perc = getlow(cpu2_list)
                low_cpu3_perc = getlow(cpu3_list)
                low_cpu4_perc = getlow(cpu4_list)
                low_cpu5_perc = getlow(cpu5_list) #get lows and print them
                low_cpu6_perc = getlow(cpu6_list)
                low_mem_perc = getlow(mem_list)
                low_swap_perc = getlow(swap_list)
                
                #print "\n\nAverage CPU temperature was",tavg,"degrees Celsius"
                print "Average CPU1 percent was",avg_cpu1_perc,"%"
                print "Average CPU2 percent was",avg_cpu2_perc,"%"
                print "Average CPU3 percent was",avg_cpu3_perc,"%"
                print "Average CPU4 percent was",avg_cpu4_perc,"%"
                print "Average CPU5 percent was",avg_cpu5_perc,"%"
                print "Average CPU6 percent was",avg_cpu6_perc,"%"
                
                print "Average RAM percent was",avg_mem_perc,"%"	
                print "Average SWAP percent was",avg_swap_perc,"%\n"	
                
                #print "Highest CPU temperature was",tmax,"degrees Celsius"	
                print "Highest CPU1 percent was",high_cpu1_perc,"%"
                print "Highest CPU2 percent was",high_cpu2_perc,"%"
                print "Highest CPU3 percent was",high_cpu3_perc,"%"
                print "Highest CPU4 percent was",high_cpu4_perc,"%"
                print "Highest CPU5 percent was",high_cpu5_perc,"%"
                print "Highest CPU6 percent was",high_cpu6_perc,"%"
                
                print "Highest RAM percent was",high_mem_perc,"%"	
                print "Highest SWAP percent was",high_swap_perc,"%\n"	
                
                #print "Lowest CPU temperature was",tmin,"degrees Celsius"
                print "Lowest CPU1 percent was",low_cpu1_perc,"%"
                print "Lowest CPU2 percent was",low_cpu2_perc,"%"
                print "Lowest CPU3 percent was",low_cpu3_perc,"%"
                print "Lowest CPU4 percent was",low_cpu4_perc,"%"
                print "Lowest CPU5 percent was",low_cpu5_perc,"%"
                print "Lowest CPU6 percent was",low_cpu6_perc,"%"
                
                print "Lowest RAM percent was",low_mem_perc,"%"	
                print "Lowest SWAP percent was",low_swap_perc,"%\n"	
                
                
                
                if avg == 1:
                        return 0
                elif os.path.exists("/var/log/sysmon.log") == True:		
                        tod = datetime.datetime.now()
                        syslog = open ( "/var/log/sysmon.log" , "a" )
                        syslog.write ("---------------\n")
                        
                        syslog.write ("\nAverage CPU1 percent was ")
                        syslog.write (str(avg_cpu1_perc))	
                        syslog.write ("\nAverage CPU2 percent was ")
                        syslog.write (str(avg_cpu2_perc))
                        syslog.write ("\nAverage CPU3 percent was ")
                        syslog.write (str(avg_cpu3_perc))
                        syslog.write ("\nAverage CPU4 percent was ")
                        syslog.write (str(avg_cpu4_perc))
                        syslog.write ("\nAverage CPU5 percent was ")
                        syslog.write (str(avg_cpu5_perc))	
                        syslog.write ("\nAverage CPU6 percent was ")
                        syslog.write (str(avg_cpu6_perc))
                        syslog.write ("\nAverage CPU7 percent was ")
                        
                        syslog.write ("\nAverage RAM percent was ")
                        syslog.write (str(avg_mem_perc))
                        syslog.write ("\nAverage SWAP percent was ")
                        syslog.write (str(avg_swap_perc))
                        
                        
                        syslog.write ("\nHighest CPU1 percent was ")
                        syslog.write (str(high_cpu1_perc))	
                        syslog.write ("\nHighest CPU2 percent was ")
                        syslog.write (str(high_cpu2_perc))
                        syslog.write ("\nHighest CPU3 percent was ")
                        syslog.write (str(high_cpu3_perc))
                        syslog.write ("\nHighest CPU4 percent was ")
                        syslog.write (str(high_cpu4_perc))
                        syslog.write ("\nHighest CPU5 percent was ")
                        syslog.write (str(high_cpu5_perc))	
                        syslog.write ("\nHighest CPU6 percent was ")
                        syslog.write (str(high_cpu6_perc))
                        
                        syslog.write ("\nHighest RAM percent was ")
                        syslog.write (str(high_mem_perc))
                        syslog.write ("\nHighest SWAP percent was ")
                        syslog.write (str(high_swap_perc))
                        
                        
                        syslog.write ("\nLowest CPU1 percent was ")
                        syslog.write (str(low_cpu1_perc))	
                        syslog.write ("\nLowest CPU2 percent was ")
                        syslog.write (str(low_cpu2_perc))
                        syslog.write ("\nLowest CPU3 percent was ")
                        syslog.write (str(low_cpu3_perc))
                        syslog.write ("\nLowest CPU4 percent was ")
                        syslog.write (str(low_cpu4_perc))
                        syslog.write ("\nLowest CPU5 percent was ")
                        syslog.write (str(low_cpu5_perc))	
                        syslog.write ("\nLowest CPU6 percent was ")
                        syslog.write (str(low_cpu6_perc))
                        
                        syslog.write ("\nLowest RAM percent was ")
                        syslog.write (str(low_mem_perc))
                        syslog.write ("\nLowest SWAP percent was ")
                        syslog.write (str(low_swap_perc))
                        
                        syslog.write ("\n\nDATE/TIME: ")
                        syslog.write (str(tod))
                        syslog.write ("\n\n---------------\n")
                        print("Log has been updated")
                        
                else:
                        print("Could not locate log file.  Please re-install.")
                        return 1

if __name__ == '__main__':
	main()

