
import json

with open('data.json') as f:
   data = json.load(f)


print("Dirección IP:", data["ip"])
print("Sistema operativo:", data["so"])


primer_version = data["version"][0]
print("Versión:", primer_version)
print("Hostname:", data["hostname"])
print("CPU:", data["cpu"])


