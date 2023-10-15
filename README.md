# Ciper: Efficient CIDR/Subnet Resolver and Domain Name Fetcher

Ciper is a powerful Python tool designed to simplify the retrieval of network information. It efficiently resolves CIDR (Classless Inter-Domain Routing) or subnet information provided by the user into network IPs. One of its key features is its ability to identify valid IP addresses and fetch corresponding domain names associated with those IPs. With built-in efficient concurrency, Ciper provides lightning-fast output, ensuring rapid and accurate results for all your network needs.

## Features

- **Efficient Concurrency**: Ciper leverages built-in concurrency to deliver rapid results, enhancing your productivity.
- **Single IPs or Bulk Processing**: Resolve single IPs or process bulk data from files containing CIDR/subnets, making it versatile for various use cases.
- **Easy Installation**: Ciper can be easily installed using `pip` and is compatible with all major operating systems.
- **OS Independent**: Enjoy the flexibility of running Ciper on any operating system without worrying about compatibility issues.
- **Output Customization**: Save output with a specified filename or let Ciper handle it automatically if a filename is not provided.

## Required Python version

Python 3.11.5


## Installation

Method 1:

```bash
pip install ciper
```

Method 2:
```
git clone https://github.com/sanjai-AK47/Ciper.git
cd Ciper
pip install .
```


## Usage

### Resolving CIDR/Subnet to IPs and Fetching Domain Names

```bash
ciper -h
usage: ciper [-h] [-s SINGLE] [-f FILENAME] [-c CONCURRENT] [-v] [-o OUTPUT]

[INFO]: CIPER Tool dig deep and found domains of the target organisation

options:
  -h, --help            show this help message and exit
  -s SINGLE, --single SINGLE
                        [INFO]: A single range of ip address with CIDR notation (eg:127.0.0.q/24)
  -f FILENAME, --filename FILENAME
                        [INFO]: File that contains range of ipaddress with CIDR notation
  -c CONCURRENT, --concurrent CONCURRENT
                        [INFO]: Conncurrent features for level up the process with multiple process
  -v, --verbose         [INFO]: Show the found domains from the cidr notations
  -o OUTPUT, --output OUTPUT
                        [INFO]: save the found domain from the network

```

### Resolving Single IP Address

```bash
ciper -s 66.242.48.0/22  -o test.txt  --verbose

```

- `-s` or `--single` : Specifies a single Cidr/subnet to resolve.
- `f` or `--filename`: Specifies a filename contains  Cidr/subnet to resolve
- 
![Screenshot from 2023-10-15 21-48-17](https://github.com/sanjai-AK47/Ciper/assets/119435129/9597a1dd-9293-4038-994d-66ac27b66ee8)



## Author

Hey Guys I'm [D.Sanjai Kumar](https://github.com/sanjai-AK47) a web application pentester and bug bounty hunter and Im also an open source tool developer
for CyberSecurity community to develope the community into Open Source I develope tools for all of us and also checkout my other Tools in my repositories
which will be very usefull for bug hunters ,  penetration tester and Ethical hackers check it out here the others tools called [Subdominator](https://github.com/sanjai-AK47/Subdominator) for subdomain enumeration
through passive and OSINT and [GoogleDorker](https://github.com/sanjai-AK47/GoogleDorker) which CLI based google dorking tool and to save the dorking tools and make the work more easy and efficiently

## GitHub Repository

[GitHub Repository](https://github.com/sanjai-AK/Ciper)

For more information and detailed usage instructions, please refer to the [official documentation](https://github.com/sanjai-AK/Ciper).

## Suuport:
Thanks in advance to all users that supporting me to develop these tools and I need your support. Just show your support and love through giving a ⭐ to my tools and remember
sharing is caring so also share to other members of our community to build a Open source community for all ❤️.

