import socket

domain = input("Enter Domain Name or IP Address:- ")

try:
    ip = socket.gethostbyname(domain)
    print(f"\n=========================\n{domain} = {ip}\n=========================")

    print("\nScanning Ports...")
    print("              port nunmber       stutes")
    for port in range(1,65535):
        check = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        check.settimeout(0.3)

        result = check.connect_ex((ip, port))

        if result == 0:
            
            print(f"[+] Port        {port}              OPEN")
       

        check.close()

except socket.gaierror:
    print("Invalid Domain Name or IP Address")