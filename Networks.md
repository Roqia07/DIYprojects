 **IP address** (Internet Protocol address) 
 
 is a unique numerical label assigned to each device connected to a network that uses the Internet Protocol for communication. 
 it consists of two main parts: 1- Network address 2- Host address
 
 **IPv4 (Internet Protocol Version 4)**
 
 uses a 32-bit address with four octets each ranging from 0 to 255
 Example IPv4 addresses: 192.168.1.1 (Common router address)
 
 **Subnetting**
 
 It uses a subnet mask to determine which part of the IP is the network and which is the host.
Example:
- IP Address: 192.168.1.10
- Subnet Mask: 255.255.255.0
- Network address: 192.168.1.0
- Host Range: 192.168.1.1 - 192.168.1.254
- Broadcast: 192.168.1.255
  
**Private IP Addresses (Used in Local Networks)**
Private IPs are used within local networks and are not routable on the internet.
Private Range	Subnet Mask
- 10.0.0.0 – 10.255.255.255	255.0.0.0
- 172.16.0.0 – 172.31.255.255	255.240.0.0
- 192.168.0.0 – 192.168.255.255	255.255.0.0
  
Example:
- Router IP: 192.168.1.1
- Device on the network: 192.168.1.100

**Public IP Addresses (Used on the Internet)**
Public IPs are unique globally and assigned by ISPs (Internet Service Providers).

Example:
8.8.8.8 (Google DNS)

**NAT (Network Address Translation)**
NAT allows multiple devices on a local network to share a single public IP address.The router translates private IPs into a public IP when communicating with the internet.

Example Scenario:
- Router Public IP: 203.0.113.10
- Devices with Private IPs:
- 192.168.1.2
- 192.168.1.3

