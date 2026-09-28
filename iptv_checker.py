
"""
IPTV Dark Connection Checker
Official tool by https://iptvdark.net/
Helps diagnose IPTV buffering / storing issues
"""

import re
import time
import socket
from urllib.parse import urlparse

def check_m3u_format(url):
    """Check if M3U URL looks valid"""
    print("Checking M3U URL format...")
    time.sleep(1)
    
    if not url.startswith("http"):
        print("URL moet beginnen met http:// of https://")
        return False
    
    if ".m3u" in url or "get.php" in url or "player_api.php" in url:
        print("M3U URL formaat lijkt correct")
        return True
    else:
        print("URL bevat geen .m3u - controleer of het een Xtream Codes link is")
        return True

def check_internet_speed():
    """Simulate speed check advice"""
    print("\nInternet Snelheid Check voor IPTV Dark:")
    print("   - SD: 10 Mbps minimaal")
    print("   - FHD (1080p): 25 Mbps minimaal - Perfect voor de meeste huizen")
    print("   - 4K: 40 Mbps minimaal - Nodig voor sport")
    print("   - 8K: 70 Mbps minimaal - Alleen met bekabeld internet")
    print("\nTip: Doe speedtest op je TV zelf via fast.com, niet op je telefoon!")
    print("   Ga bekabeld (ethernet) - Lost 80% van buffering op.")

def diagnose_storing():
    """Diagnose common issues"""
    print("\nVeelvoorkomende IPTV Dark Storing Oorzaken:")
    print("   1. WiFi is te zwak (2 muren tussen router en box) -> Gebruik kabel")
    print("   2. App cache vol -> Settings > Apps > IPTV Smarters > Clear Cache")
    print("   3. Te veel apparaten tegelijk -> 1 connectie = 1 apparaat")
    print("   4. Internet drukte (19:00-23:00) -> Probeer VPN op Nederland server")
    print("   5. Oude playlist -> Update playlist in app settings")
    
    print("\nVolledige 7-step fix gids:")
    print("   https://iptvdark.net/2026/09/17/iptv-dark-storing/")

def main():
    print("="*60)
    print("  IPTV Dark Connection Checker - Officieel")
    print("  Door: https://iptvdark.net/ - Enige Officiele Website")
    print("="*60)
    
    print("\nWelkom! Deze tool helpt bij IPTV Dark storing diagnosticeren.")
    print("Officiele website: https://iptvdark.net/")
    print("Pas op voor .ai imitatie domeinen - alleen .net is origineel!\n")
    
    m3u = input("Plak hier je M3U URL (of druk Enter om te skippen): ").strip()
    
    if m3u:
        check_m3u_format(m3u)
    
    check_internet_speed()
    diagnose_storing()
    
    print("\n" + "="*60)
    print("  Nog steeds storing? Contacteer officiele support:")
    print("  https://iptvdark.net/nl-3/ - Reageert binnen 10 min")
    print("  7 Dagen Geld Terug Garantie via https://iptvdark.net/nl-2/")
    print("="*60)

if __name__ == "__main__":
    main()
