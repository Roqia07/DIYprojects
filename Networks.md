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

///////////////////////////////////////////////////////////////////////////////////////////////////////
# hosts
- hosts are split into clients and servers:
**clients**: initiate requests
**Hosts**: respond to the request

- when a client requests access to a host (website) it sends 2 ip addresses the src(client ip address) Dst(destination: server) and vice versa

/////////////////////////////////////////////////////////////////////////////////////////////////////////
# repeater
 between 2 devices 
- regenerate signals to be sent across great distances

# hub 
repeater bur for multi-ports 

- hub duplicates the signal and sends it to multiple devices at the same time

**!!!everyone recieves everyone else's data**

# bridge

2 sets of hosts connected by a hub with a bridge in the middle between hub connected hosts
- bridge only have **2** ports one  for each hub connected devices
-  if i want to communicate between 2 devices at the same hub then the data is also sent to the bridge and it knows that it is not meant to go to the other hub then it would prevent it and the same goes for the other hub unless i want to send the data to the other hub then the bridge will allow it and all the data are sent to all the devices on the other side.

# switch
- combination of hubs and bridges 
- like hubs: many devices are connected to each other
- like bridges : knows which host connected to each port

- **the switch knows which hosts on each port so if a device in a network only wants to communicate with another one then it can be easily sent to its port without the message being sent to other devices**


- **multiple devices can communicate with each other at the same time**

- !! all these device share the same ip address space (192.168.1.XX)
- all these devices are within the same network

# Router
- facilitate communication between different networks ( if i ahve several switches for example)

* connects the devices to the internet

* provides security to different networks

- creates the heriarchy of IP addresses

## routing table
- contains all the netweorks a router knows about (all different switches and the internet)
## Gateway 
- the router have differnt IP address for each network
- **the Gateway** is the hosts' way out of the local network

### conclusion
Switch	|Router
--------|---------
 The resource is shared among multiple devices with the help of a single LAN using a network switch.       |Data is moved between two or more computers with the help of a router.
Network switches uses data frames.   |Routers use data packets.
Switches only work in a Wired network connection.     |Router works with both wired and wifi networks.
Switches use MAC Addresses for transferring data to the proper destination.         |Routers use IP Addresses for the same work.


![Hub](https://resource.fs.com/mall/generalImg/PDplb4k8HoCGONxCEn7cmedwnjg.gif)
*Figure 1: Network Hub*

![Bridge](https://www.landisgyr.com/webfoo/wp-content/uploads/2019/12/Network-Bridge-Front.jpg?width=300)
*Figure 2: Network bridge*
![hubWithBridge](https://i.postimg.cc/j5fZFmkt/Advantages-and-Disadvantages-of-Network-Bridge.jpg?width=300)
*Figure 3: hub bridge network*
![Switch](https://www.cisco.com/c/dam/assets/swa/img/anchor-info/what-is-network-switching-628x353.png?width=300)
*Figure 3: Network switch*
![Router](https://api-rayashop.freetls.fastly.net/media/catalog/product/cache/4e49ac3a70c0b98a165f3fa6633ffee1/f/0/f0ozphn_3whznflofg9xumnj_1.jpeg?width=300)
*Figure 4: Router 3ady*
