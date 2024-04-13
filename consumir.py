import requests

def obtener_info_maquina():
    try:
       
        url = "http://127.0.0.1:5000/machine-info"

        
        response = requests.get(url)

       
        if response.status_code == 200:
            data = response.json()
            hostname = data.get("hostname")
            ip_address = data.get("ip_address")

            if hostname and ip_address:
                print(f"Nombre de host (hostname): {hostname}")
                print(f"Dirección IP: {ip_address}")
            else:
                print("No se pudo obtener información completa.")
        else:
            print(f"Error al obtener datos (código de estado {response.status_code}).")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    obtener_info_maquina()
