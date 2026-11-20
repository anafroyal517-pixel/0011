ip = input("IP Address asgeba: ")
first_octet = int(ip.split(".")[0])

if 1 <= first_octet <= 126:
    print("Yegebaw IP Class A new.")
elif first_octet == 127:
    print("Yegebaw IP Loopback (Localhost) new.")
elif 128 <= first_octet <= 191:
    print("Yegebaw IP Class B new.")
elif 192 <= first_octet <= 223:
    print("Yegebaw IP Class C new.")
elif 224 <= first_octet <= 239:
    print("Yegebaw IP Class D (Multicast) new.")
elif 240 <= first_octet <= 255:
    print("Yegebaw IP Class E (Reserved) new.")
else:
    print("Tikikilegna IP ayidelem!")