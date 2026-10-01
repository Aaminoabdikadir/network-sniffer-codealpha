import socket
import struct
import csv
from datetime import datetime

# Reverse DNS Lookup (IP -> Hostname)
def get_domain_name(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return "Unknown / Local"

def start_sniffer():
    # Qabso IP-ga local-ka ah ee komputarka
    host = socket.gethostbyname(socket.gethostname())
    
    # Abuur Raw Socket
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    conn.bind((host, 0))
    conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print(f"[*] Sniffer-ka horumarsan wuxuu ka shaqaynayaa: {host}")
    
    file_name = f"sniffer_advanced_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Timestamp", "Protocol", "Source IP", "Source Domain", "Destination IP", "Destination Domain"])
        
        try:
            while True:
                raw_data, addr = conn.recvfrom(65535)
                ip_header = raw_data[0:20]
                iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
                
                protocol_num = iph[6]
                src_ip = socket.inet_ntoa(iph[8])
                dest_ip = socket.inet_ntoa(iph[9])
                
                protocol_map = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
                protocol = protocol_map.get(protocol_num, 'OTHER')
                
                # Kaliya marka uu yahay TCP ama UDP raadi Domain Name
                src_domain = get_domain_name(src_ip) if protocol in ['TCP', 'UDP'] else "N/A"
                dest_domain = get_domain_name(dest_ip) if protocol in ['TCP', 'UDP'] else "N/A"
                
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{timestamp}] {protocol} | {src_ip} ({src_domain}) -> {dest_ip} ({dest_domain})")
                
                writer.writerow([timestamp, protocol, src_ip, src_domain, dest_ip, dest_domain])
                
        except KeyboardInterrupt:
            print("\n[*] Sniffer-ka waa la joojiyay.")
        finally:
            # SIO_RCVALL demi (2 arguments oo kaliya ayaan siinaynaa)
            conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == "__main__":
    start_sniffer()