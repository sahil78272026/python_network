import socket

def scan_ports(host, ports):
    # Create a socket object for each port to check
    results = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((host, port))
            results.append(f"Port {port} is open")
        except:
            pass
        finally:
            s.close()
    print(dir(s))
            
    return results

# Example usage
host = "8.8.8.8"
ports = [10,20,443]
print("Scanning open ports on", host)
results = scan_ports(host, ports)
if len(results) > 0:
    print("Found", len(results), "open ports:")
    for result in results:
        print(result)
else:
    print("No open ports found.")
