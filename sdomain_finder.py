import requests
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style
from tqdm import tqdm
import sys

# Default wordlist embedded in the script
DEFAULT_WORDLIST = [
    "www", "mail", "ftp", "test", "dev", "admin", "blog", "api",
    "staging", "shop", "webmail", "portal", "beta", "secure"
]

def request(url, protocol):
    try:
        full_url = f"{protocol}://{url}"
        result = requests.get(full_url, timeout=5)
        if result.status_code == 200:
            print(f"{Fore.GREEN}[+] Subdomain discovered ----> {full_url}{Style.RESET_ALL}")
            return full_url
    except requests.exceptions.RequestException:
        pass
    return None

def main():
    parser = argparse.ArgumentParser(description="Subdomain Enumeration Tool")
    parser.add_argument("target", help="Target domain (e.g., example.com)")
    parser.add_argument("-w", "--wordlist", help="Path to a custom wordlist")
    parser.add_argument("-o", "--output", help="File to save discovered subdomains", default="subdomains.txt")
    parser.add_argument("-t", "--threads", help="Number of threads", type=int, default=10)
    parser.add_argument("--timeout", help="Request timeout in seconds", type=int, default=5)

    args = parser.parse_args()

    # Use embedded wordlist if no custom wordlist is provided
    if args.wordlist:
        try:
            with open(args.wordlist, "r") as wordlist_file:
                wordlist = [line.strip() for line in wordlist_file]
        except FileNotFoundError:
            print(f"{Fore.RED}[-] Wordlist file not found: {args.wordlist}{Style.RESET_ALL}")
            return
    else:
        print(f"{Fore.YELLOW}[!] No custom wordlist provided. Using the default embedded wordlist.{Style.RESET_ALL}")
        wordlist = DEFAULT_WORDLIST

    discovered_subdomains = []

    try:
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            futures = []
            for word in wordlist:
                subdomain = f"{word}.{args.target}"
                futures.append(executor.submit(request, subdomain, "https"))
                futures.append(executor.submit(request, subdomain, "http"))

            for future in tqdm(as_completed(futures), desc="Scanning", total=len(futures)):
                result = future.result()
                if result:
                    discovered_subdomains.append(result)

        if discovered_subdomains:
            with open(args.output, "w") as outfile:
                outfile.write("\n".join(discovered_subdomains))
            print(f"{Fore.BLUE}[+] Results saved to {args.output}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[-] No subdomains discovered.{Style.RESET_ALL}")

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Scan interrupted by user. Exiting gracefully...{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[-] An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
