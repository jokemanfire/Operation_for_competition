import socket
import threading
import re

timeout = 0.5
hosts = []
ports = ["22", "80", "33"]
class hosts_port_scan(object):

    def __init__(self, hosts, ports):
        self.hosts = hosts
        self.ports = ports

    def host_port_creat(self, port, host):
        socket.setdefaulttimeout(timeout)#设置超时时间
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((str(host), port))
            f = s.recv(1024)
            self.information_write(f, port, host)
        except:
            #链接错误，写入错误日志
            print("connect error")
            logfile = open("log.txt", "a")
            logfile.write(str(host)+":" + str(port) +"connect error \n")
            logfile.close()

    def host_port_scan(self):
        for host in self.hosts:
            for port in self.ports:
                #实现多线程
                try:
                    threads = threading.Thread(target=self.host_port_creat, args=(port, host))
                    threads.start()
                except:
                    print("threads start error")

    def information_write(self, information, port, host):
        self.information = information
        try:
            fdict = open("test", "a")
            self.information = host + ":" + str(port) + "----" + self.information.decode("utf-8")
            fdict.write(self.information)
            fdict.close()
        except:
            #文件打开失败，写入错误日志
            print("file open filed")
            logfile = open("log.txt", "a")
            logfile.write("file open error \n")
            logfile.close()



def ports_deal():
    #对写入的ports变量进行格式判断
    global ports
    ports_new = []
    if isinstance(ports, list) is True:
        for m in ports:
            if isinstance(m, str) is True:
                compare = re.match(r"(\d+)-(\d+)", m)
                if compare is None:
                    m = int(m)
                    ports_new.append(m)
                else:
                    ports = list()
                    for i in range(int(compare.group(1)), int(compare.group(2))+1):
                        ports.append(i)
                    return 1
        ports = ports_new
    else:
        return 3



def main():
    #主函数
    hosts = ["45.77.27.155"]
    #print(ports_deal())
    #print(ports)
    scans = hosts_port_scan(hosts,ports)
    scans.host_port_scan()

if __name__ == "__main__":
    main()
