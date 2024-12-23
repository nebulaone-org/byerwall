![Byerwall Banner](https://i.imgur.com/dksZAIj.png)

# Byerwall

![GitHub release (latest by date)](https://img.shields.io/github/v/release/nebulaone-org/byerwall?label=Latest%20Release)
![GitHub issues](https://img.shields.io/github/issues/nebulaone-org/byerwall?label=Issues)
![GitHub](https://img.shields.io/github/license/nebulaone-org/byerwall?label=License)
![GitHub stars](https://img.shields.io/github/stars/nebulaone-org/byerwall?label=Stars)
![GitHub forks](https://img.shields.io/github/forks/nebulaone-org/byerwall?label=Forks)

**Byerwall** is a simple and intuitive GUI-based tool designed to assist in bypassing CGNAT by generating configuration files for [**FRP (Fast Reverse Proxy)**](https://github.com/fatedier/frp) and running the FRP client.

Features:
- Create custom proxy entries with options for TCP, UDP, or both protocols.
- Add from popular predefined entries (e.g., RDP, Minecraft, HTTP, HTTPS).
- Generate configuration files with ease.
- One-click "Generate & Run" to execute the FRP client with the generated configuration.
- Lightweight and easy to use, powered by Python and Tkinter.

To Do (Hopefully Coming Soon!):
- Cross-Platform Support: Ensure compatibility with macOS and Linux for broader user adoption.
- Better Theming: I literally threw this together in a day, I went for function over style!
- Intercept UPnP Packets and automatically forward for games.

# How to install/use!
## Windows
Windows installation is easy, grab the latest .zip file from the [releases](https://github.com/nebulaone-org/byerwall/releases/) page, unzip and run the executable file, this will open the GUI and you're set to go!
### Server
To run a server on Windows for the Reverse Proxy, it is impractical, however, you can install the full FRP stack [here](https://github.com/fatedier/frp/releases/download/v0.61.1/frp_0.61.1_windows_amd64.zip) and run the server.

## Linux
Linux has two methods, the CLI method and the UI method.
### CLI
**1)** Get the latest CLI Binaries
```bash
wget https://github.com/nebulaone-org/byerwall/releases/download/v0.0.1-alpha/byerwall
```
**2)** Move the CLI Binaries to your PATH (optional)
```bash
sudo mv byerwall /usr/local/bin
```
**3)** Run Byerwall with the ports/server you want
```bash
byerwall 159.65.51.32:7000 25565:25565 25566:25566 --run # If in PATH
./byerwall 159.65.51.32:7000 25565:25565 25566:25566 --run # If in Directory
```
### GUI
**1)** Get the latest GUI Binaries
```bash
wget https://github.com/nebulaone-org/byerwall/releases/download/v0.0.1-alpha/byerwall-ui
```
**2)** Move the GUI Binaries to your PATH (optional)
```bash
sudo mv byerwall-ui /usr/local/bin
```
**3)** Run Byerwall with the ports/server you want
```bash
byerwall-ui
./byerwall-ui
```
### Server
Running the server on linux is incredibly simple! Simply follow the instructions/commands below (this may vary depending on distro, however very slightly, and if you know your distro well, you'll know what to do!)
```bash
wget https://github.com/nebulaone-org/byerwall/releases/download/v0.0.1-alpha/byerwall-server-linux.zip
unzip byerwall-server-linux.zip
chmod +x byerwall-server.sh
./byerwall-server.sh
```


## Use Case
Why and what is this for? After switching my ISP, I found out I couldn't play games I used to love to play! This meant I couldn't host ARMA 3 Servers, Satisfactory Servers, or anything that typically requires "UPnP", this is because my new ISP integrated CGNAT, meaning we were not assigned a Private IP, therefore we couldn't play certain games. Nowadays, this can happen alot as some ISPs will not assign Public IPv4 due to the shortage, so the best way to circumnavigate this fiasco is via a reverse proxy. By far the easiest out there is [FastReverseProxy](https://github.com/fatedier/frp) by [fatedier](https://github.com/fatedier). Luckily, I managed to get this to work and solve my issue after reading the documentation, however some people may not have this patience, so I bundled it into a nice, lightweight UI!

![Graph](https://i.imgur.com/0kD48q4.png)

## What is the Server IP / Server Port?
Unfortunately, you will need to have a server running FastReverseProxy Server, this may be a hassle, however it is by no means expensive! [DigitalOcean](https://digitalocean.com/) offers a plan for a server for $3/month, other alternatives include AWS or by using a public server from the below database, however using a public server will mean that the port you intend to use may not be available, and you may have to use a different port.

## Public Use Servers
| Server Name           | Server Address   | Server Port |
|------------------------|------------------|-------------|
| Byerwall Public Node 1 | 159.65.51.32     | 7000        |

The availabilty of ports are limited, and common ports such as 25565, 22, 80, 443, are probably already taken. Do not complain when they don't work, these should only be used when you need a quick fix and not for production. Once this server is at 70% capacity I'll add more, if you have a server you'd like to contribute then open an issue.
