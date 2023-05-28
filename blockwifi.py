import nmap

# create an nmap scanner object
scanner = nmap.PortScanner()

# scan the local network
scanner.scan(hosts='2.2.80.19/24', arguments='-n -sP -PE -PA21,23,80,3389')

# display the connected devices
for host in scanner.all_hosts():
    # print the host's IP address and hostname (if available)
    print(f'Host: {host} ({scanner[host].hostname()})')
    
    # print the host's state (up or down)
    print(f'State: {scanner[host].state()}')
    
    # iterate over each protocol found on the host (e.g. tcp, udp)
    for proto in scanner[host].all_protocols():
        # print the protocol type
        print(f'Protocol: {proto}')
        
        # iterate over each port found on the host for this protocol
        lport = scanner[host][proto].keys()
        for port in lport:
            # print the port number and its state (open or closed)
            print(f'Port: {port}\tState: {scanner[host][proto][port]["state"]}')
