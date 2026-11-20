import socket
import nmap


def scan_target(target: str, port_range: str = "1-1024", arguments: str = "-sV") -> None:
    """Scan a target host using python-nmap and print open ports."""
    scanner = nmap.PortScanner()

    try:
        resolved_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Error: Could not resolve '{target}'.")
        return

    print(f"\n[*] Target     : {target} ({resolved_ip})")
    print(f"[*] Port Range : {port_range}")
    print(f"[*] Arguments  : {arguments}")
    print("[*] Scanning... please wait.\n")

    try:
        scanner.scan(hosts=resolved_ip, ports=port_range, arguments=arguments)
    except nmap.PortScannerError as exc:
        print(f"[!] Nmap error: {exc}")
        return
    except Exception as exc:
        print(f"[!] Unexpected error: {exc}")
        return

    if resolved_ip not in scanner.all_hosts():
        print("[!] Host appears down or did not respond to scan probes.")
        return

    host_data = scanner[resolved_ip]
    print(f"Host State: {host_data.state().upper()}")

    open_found = False
    for proto in host_data.all_protocols():
        print(f"\nProtocol: {proto.upper()}")
        print(f"{'PORT':<10} {'STATE':<10} {'SERVICE':<18} {'VERSION'}")
        print("-" * 62)

        for port in sorted(host_data[proto].keys()):
            info = host_data[proto][port]
            state = info.get("state", "unknown")
            if state == "open":
                open_found = True
                service = info.get("name", "unknown")
                product = info.get("product", "")
                version = info.get("version", "")
                full_version = f"{product} {version}".strip() or "N/A"
                print(f"{port:<10} {state.upper():<10} {service:<18} {full_version}")

    if not open_found:
        print("\n[-] No open ports found in the specified range.")


def main() -> None:
    target = input("Enter Domain Name or IP Address: ").strip()
    if not target:
        print("[!] Target cannot be empty.")
        return

    port_range = input("Enter Port Range (default 1-1024, or e.g. 22,80,443 / 1-65535): ").strip()
    if not port_range:
        port_range = "1-1024"

    arguments = input("Enter Nmap arguments (default -sV, or e.g. -sS -sV): ").strip()
    if not arguments:
        arguments = "-sV"

    scan_target(target, port_range, arguments)


if __name__ == "__main__":
    main()