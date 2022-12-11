#!/usr/bin/env python

import iptables

# Create a new firewall
firewall = iptables.easy.Firewall()

# Allow incoming connections on port 80 (HTTP)
firewall.accept("tcp", dport=80)

# Allow incoming connections on port 443 (HTTPS)
firewall.accept("tcp", dport=443)

# Allow incoming connections on port 25 (SMTP)
firewall.accept("tcp", dport=25)

# Allow incoming connections on port 53 (DNS)
firewall.accept("tcp", dport=53)

# Allow incoming connections on port 22 (SSH) from a specific IP address
firewall.accept("tcp", dport=22, src="1.2.3.4")

# Block incoming connections on port 22 (SSH) from all other IP addresses
firewall.drop("tcp", dport=22)

# Apply the firewall rules
firewall.apply()
