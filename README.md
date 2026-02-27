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

## Usage
To run the Sub-domain Finder, use the following command:
```bash
python finder.py -d <domain_name>
```
Replace `<domain_name>` with the target domain you want to enumerate sub-domains for.

## Project Structure
The project structure is as follows:
```
Sub-domain-finder/
├── finder.py        # Main script to run the tool
├── requirements.txt  # List of dependencies
└── README.md        # Project documentation
```

## How it Works
Sub-domain Finder utilizes a combination of DNS lookups and common sub-domain naming conventions to find potential sub-domains quickly. It leverages popular APIs for more comprehensive results.

## Configuration
You can configure the tool by modifying the `config.json` file. Here, you can set your preferred APIs, DNS servers, and other parameters.

## Output
The tool generates an output file named `results.txt` containing the enumerated sub-domains and their corresponding IP addresses.

## Troubleshooting
If you encounter issues while running the tool:
- Ensure that your internet connection is stable.
- Verify that the target domain is valid and accessible.
- Check if any required APIs are correctly configured in the `config.json` file.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.