import os
import subprocess

TOOLS = {
    "1": ("Suricata", "sudo apt update && sudo apt install -y suricata", "suricata -h"),
    "2": ("RITA", "sudo apt update && sudo apt install -y snapd && sudo snap install rita", "rita --help"),
    "3": ("Cuckoo Sandbox", "sudo apt update && sudo apt install -y cuckoo", "cuckoo --help"),
    "4": ("Wireshark", "sudo apt update && sudo apt install -y wireshark", "wireshark -h"),
    "5": ("Zui", "sudo apt update && sudo apt install -y npm && sudo npm install -g zui", "zui -h"),
    "6": ("Zeek", "sudo apt update && sudo apt install -y zeek", "zeek --help"),
    "7": ("NetworkMiner & Mono", "sudo apt update && sudo apt install -y mono-complete && wget -q -O networkminer.zip https://www.netresec.com/?download=NetworkMiner && unzip networkminer.zip -d /opt/networkminer && rm networkminer.zip", "mono /opt/networkminer/NetworkMiner.exe"),
    "8": ("nfdump", "sudo apt update && sudo apt install -y nfdump", "nfdump -h"),
    "9": ("PassiveDNS", "sudo apt update && sudo apt install -y passivedns", "passivedns -h"),
    "10": ("Volatility", "sudo apt update && sudo apt install -y volatility", "volatility -h"),
}

INSTALL_PATHS = {
    "Suricata": "/usr/bin/suricata",
    "RITA": "/snap/bin/rita",
    "Cuckoo Sandbox": "/usr/bin/cuckoo",
    "Wireshark": "/usr/bin/wireshark",
    "Zui": "/usr/bin/zui",
    "Zeek": "/usr/bin/zeek",
    "NetworkMiner": "/opt/networkminer/NetworkMiner.exe",
    "nfdump": "/usr/bin/nfdump",
    "PassiveDNS": "/usr/bin/passivedns",
    "Volatility": "/usr/bin/volatility",
}

def is_installed(tool_path):
    """Check if the tool is already installed."""
    return os.path.exists(tool_path)

def install_tool(name, command):
    """Install the specified tool using the provided command."""
    print(f"\nInstalling {name}...")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"{name} installed successfully!\n")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to install {name}.\n")

def show_help():
    """Display help information for the tools."""
    print("\nAvailable Tools and How to Use Them:")
    for key, (name, _, usage) in TOOLS.items():
        print(f"- {name}: Run \"{usage}\" for help.")

    print("\nThis script will install the following tools:")
    for key, (name, _, _) in TOOLS.items():
        print(f"- {name}")

def main():
    """Main menu for tool installation."""
    while True:
        print("\nAvailable Tools:")
        for key, (name, _, _) in TOOLS.items():
            print(f"{key}. {name}")
        print("A. Install all tools")
        print("H. Show help")
        print("Q. Quit")

        choice = input("\nEnter your choice: ").strip().upper()

        if choice == "Q":
            print("Exiting...")
            break

        elif choice == "A":
            for key, (name, command, _) in TOOLS.items():
                if is_installed(INSTALL_PATHS[name]):
                    print(f"{name} is already installed.")
                else:
                    install_tool(name, command)

        elif choice == "H":
            show_help()

        elif choice in TOOLS:
            name, command, _ = TOOLS[choice]
            if is_installed(INSTALL_PATHS[name]):
                print(f"{name} is already installed.")
            else:
                install_tool(name, command)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
