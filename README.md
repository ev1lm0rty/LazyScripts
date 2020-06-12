## About
* Some quick and dirty scripts that I use while pentesting a box.
* These are just raw scripts, you can tweak them if u like.

## Scripts
* OneLineRev.py : Create one line reverse shells easily.
* Venom.py : Create msfvenom payloads quickly.

## Usage

### OneLineRev
* Usage   : `python3 OneLineRev.py <IP> <Port> <Type>`
* Types   :  Bash , Perl , Java , NC , Php , Python
* Example : `python3 OneLineRev.py 127.0.0.1 1234 bash`

### Venom
* Usage   : `python3 Venom.py <IP> <Port> <Type>`
* Types:
  * lsb : Linux Shell Bind
  * lmb : Linux Meterpreter Bind
  * lmr : Linux Meterpreter Reverse
  * wsr : Windows Shell Reverse
  * wmr : Windows Meterpreter Reverse
  * wmre : Windows Meterpreter Reverse Encoded
* Example : `python3 Venom.py 127.0.0.1 1234 lmr`
