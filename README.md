# Subdomain Finder Tool

## 🚀 Overview
The Subdomain Finder Tool is a powerful and efficient Python-based tool designed for ethical hackers and cybersecurity professionals.
This tool helps discover subdomains of a given target domain, aiding in reconnaissance and penetration testing.

## ✨ Features
This tool stands out for its simplicity and versatility, offering essential functionalities required in modern reconnaissance workflows.
- **Built-in Default Wordlist**: No need for external wordlists.
- **Multithreading**: Speeds up scanning by running multiple threads simultaneously.
- **Protocol Support**: Handles both HTTP and HTTPS.
- **Output to File**: Saves results in a user-specified file for later analysis.
- **Custom Wordlist Support**: Users can specify their own wordlists for advanced use cases.

## 🔧 Prerequisites
Make sure you have the following installed:
- Python 3.6+
- Required libraries (install via `pip install -r requirements.txt`)

## 📥 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/<your_username>/subdomain-finder.git
   cd subdomain-finder
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📚 Usage
Run the tool using the command:
```bash
python sdomain_finder.py <target> <wordlist> [-o OUTPUT] [-t THREADS] [--timeout TIMEOUT]
```

### Required Arguments:
- `<target>`: The target domain (e.g., `example.com`).
- `<wordlist>`: Path to the wordlist file.

### Optional Arguments:
- `-o OUTPUT`: Save the discovered subdomains to a specified file.
- `-t THREADS`: Number of threads to use (default: 10).
- `--timeout TIMEOUT`: Request timeout in seconds (default: 5).

### Example:
```bash
python sdomain_finder.py google.com wordlist.txt -o results.txt -t 20
```

## 🛠 Built-In Wordlist
The tool includes a small default wordlist to get started quickly. You can modify or expand this wordlist in the `data/wordlist.txt` file.


## 🤝 Contributions
Contributions are welcome! Feel free to open issues or submit pull requests with improvements, bug fixes, or new features.

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## 📧 Contact
Feel free to reach out for suggestions or feedback:
- **Developer**: Lucky Kumar
- **Email**: luckykumar200221@gmail.com
