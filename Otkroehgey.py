import requests
from bs4 import BeautifulSoup

def get_whois_info(ip_address):
    url = f"https://www.whois.com/whois/{ip_address}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    data = soup.find("div", class_="df-block")
    if data:
        registry_data = data.find("pre", {"id": "registryData"})
        registrar_data = data.find("pre", {"id": "registrarData"})

        whois_info = ""
        if registry_data:
            whois_info += registry_data.get_text() + "\n"
        if registrar_data:
            whois_info += registrar_data.get_text() + "\n"

        headers = data.find_all("div", class_="d-flex")
        for header in headers:
            whois_info += header.get_text() + "\n"

        return whois_info
    else:
        return "Не удалось получить информацию whois для данного IP-адреса."

if __name__ == "__main__":
    ip_address = input("Введите IP-адрес: ")
    whois_info = get_whois_info(ip_address)
    print()
    print(whois_info)