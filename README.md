# NetProbe

A simple Python-based network testing tool for portscan, ping, and DNS lookup.

## NetProbe - Network Testing Tool

NetProbe is a lightweight Python-based network testing tool designed for beginners in cybersecurity and OSINT. It provides essential functionalities like host discovery, port scanning, and DNS resolution.

---

## Features

* Host availability check (Ping)
* Common port scanning
* DNS lookup
* Input validation
* Cross-platform support (Windows & Linux)

---

## Installation

```bash
git clone https://github.com/Udeshna-labs/netprobe.git
cd netprobe
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

Then enter a target domain or IP address.

---

## Project Structure

```
netprobe/
├── main.py                 # Main entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── netprobe/              # Package directory
    ├── __init__.py        # Package initialization
    ├── ping.py            # Host availability check
    ├── scanner.py         # Port scanning
    ├── dns_lookup.py      # DNS resolution
    └── utils.py           # Utility functions
```

---

## Disclaimer

This tool is intended for educational purposes only.

* Use only on systems you own or have explicit permission to test.
* Unauthorized scanning may be illegal.

---

## Contributing

Pull requests are welcome! Feel free to improve features, fix bugs, or enhance documentation.

---

## Star the Repo

If you found this useful, consider giving it a star ⭐

---

Created by Udeshna
