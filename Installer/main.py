import os
import subprocess

TOOLS = {
    "1": ("Suricata", "sudo apt update && sudo apt install -y suricata", "suricata -h"),
    "2": ("RITA", "wget -q https://github.com/activecm/rita/releases/download/v5.0.8/install-rita-zeek-here.sh && chmod +x install-rita-zeek-here.sh && ./install-rita-zeek-here.sh", "rita --help"),
    "3": ("Cuckoo Sandbox", "pip download cuckoo && pip install *.tar.gz", "cuckoo --help"),
    "4": ("Wireshark", "sudo apt update && sudo apt install -y wireshark", "wireshark -h"),
    "5": ("Zui", "wget -q https://github.com/brimdata/zui/releases/download/v1.18.0/zui_1.18.0_amd64.deb && sudo dpkg -i zui_1.18.0_amd64.deb && rm zui_1.18.0_amd64.deb", "zui -h"),
    "6": ("Zeek", "echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_24.04/ /' | sudo tee /etc/apt/sources.list.d/security:zeek.list && curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_24.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null && sudo apt update && sudo apt install -y zeek", "zeek --help"),
    "7": ("NetworkMiner & Mono", "sudo gpg --homedir /tmp --no-default-keyring --keyring /usr/share/keyrings/mono-official-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && echo 'deb [signed-by=/usr/share/keyrings/mono-official-archive-keyring.gpg] https://download.mono-project.com/repo/ubuntu stable-focal main' | sudo tee /etc/apt/sources.list.d/mono-official-stable.list && sudo apt update && sudo apt install mono-devel -y && apt clean && rm -rf /var/lib/apt/lists/* && wget -q -O networkminer.zip https://www.netresec.com/?download=NetworkMiner && unzip networkminer.zip -d /opt/networkminer && rm networkminer.zip", "mono /opt/networkminer/NetworkMiner.exe"),
    "8": ("nfdump", "sudo apt update && sudo apt install -y nfdump", "nfdump -h"),
    "9": ("PassiveDNS", "sudo apt update && sudo apt install -y passivedns", "passivedns -h"),
    "10": ("Volatility", "sudo apt update && sudo apt install -y volatility", "volatility -h"),
}

INSTALL_PATHS = {
    "Suricata": "/usr/bin/suricata",
    "RITA": "/usr/local/bin/rita",
    "Cuckoo Sandbox": "/usr/local/bin/cuckoo",
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

def install_all_tools():
    """Install all tools sequentially."""
    for key, (name, command, _) in TOOLS.items():
        if is_installed(INSTALL_PATHS[name]):
            print(f"{name} is already installed.")
        else:
            install_tool(name, command)

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

        elif choice == "H":
            show_help()

        elif choice == "A":
            install_all_tools()

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