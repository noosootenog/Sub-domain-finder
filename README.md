# Sub-domain Finder

## Features
- Fast and efficient sub-domain enumeration.
- Supports multiple DNS resolution methods.
- Supports API integration for advanced sub-domain discovery.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- A running instance of [Python](https://www.python.org/downloads/) (version 3.6 or higher).
- Network access to DNS services.

## Installation
To install the Sub-domain Finder, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/noosootenog/Sub-domain-finder.git
   cd Sub-domain-finder
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```


## Project Structure
The project structure is as follows:
```
├── result/
│   └── found_subdomains.txt
├── source/
│   ├── function/
│   │   ├── create_gui.py
│   │   ├── find_subdomains.py
│   │   ├── load_wordlist.py
│   │   ├── perform_scan.py
│   │   └── start_scan.py
│   └── main.py
├── LICENSE
├── README.md
├── requirements.txt
└── wordlist.txt

```

## How it Works
Sub-domain Finder utilizes a combination of DNS lookups and common sub-domain naming conventions to find potential sub-domains quickly. It leverages popular APIs for more comprehensive results.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
