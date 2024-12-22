![ByerWall Banner](https://i.imgur.com/dksZAIj.png)

# ByerWall

![GitHub release (latest by date)](https://img.shields.io/github/v/release/nebulaone-org/byerwall?label=Latest%20Release)
![GitHub issues](https://img.shields.io/github/issues/nebulaone-org/byerwall?label=Issues)
![GitHub](https://img.shields.io/github/license/nebulaone-org/byerwall?label=License)
![GitHub stars](https://img.shields.io/github/stars/nebulaone-org/byerwall?label=Stars)
![GitHub forks](https://img.shields.io/github/forks/nebulaone-org/byerwall?label=Forks)

**ByerWall** is a simple and intuitive GUI-based tool designed to assist in bypassing CGNAT by generating configuration files for [**FRP (Fast Reverse Proxy)**](https://github.com/fatedier/frp) and running the FRP client.

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

## Use Case
Why and what is this for? After switching my ISP, I found out I couldn't play games I used to love to play! This meant I couldn't host ARMA 3 Servers, Satisfactory Servers, or anything that typically requires "UPnP", this is because my new ISP integrated CGNAT, meaning we were not assigned a Private IP, therefore we couldn't play certain games. Nowadays, this can happen alot as some ISPs will not assign Public IPv4 due to the shortage, so the best way to circumnavigate this fiasco is via a reverse proxy. By far the easiest out there is [FastReverseProxy](https://github.com/fatedier/frp) by [fatedier](https://github.com/fatedier). Luckily, I managed to get this to work and solve my issue after reading the documentation, however some people may not have this patience, so I bundled it into a nice, lightweight UI!

## What is the Server IP / Server Port?
Unfortunately, you will need to have a server running FastReverseProxy Server, this may be a hassle, however it is by no means expensive! [DigitalOcean](https://digitalocean.com/) offers a plan for a server for $3/month, other alternatives include AWS or by using a public server from the below database, however using a public server will mean that the port you intend to use may not be available, and you may have to use a different port.

## Public Use Servers
| Server Name           | Server Address   | Server Port |
|------------------------|------------------|-------------|
| Byerwall Public Node 1 | 159.65.51.32     | 7000        |

The availabilty of ports are limited, and common ports such as 25565, 22, 80, 443, are probably already taken. Do not complain when they don't work, these should only be used when you need a quick fix and not for production. Once this server is at 70% capacity I'll add more, if you have a server you'd like to contribute then open an issue.
