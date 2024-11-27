from netmiko import ConnectHandler

# Conexión al router Mikrotik
mikrotik = {
    "device_type": "mikrotik_routeros",
    "host": "192.168.88.1",  
    "username": "admin",     
    "password": "admin",
}

# Comandos de configuración
commands = [
    "/ip address add address=192.168.1.1/24 interface=ether2",
    "/ip dns set servers=8.8.8.8 allow-remote-requests=yes",
    "/ip address add address=192.168.2.1/24 interface=ether3",
    "/ip pool add name=dhcp_pool ranges=192.168.2.2-192.168.2.254",
    "/ip dhcp-server add address-pool=dhcp_pool interface=ether3 name=dhcp1",
    "/ip dhcp-server network add address=192.168.2.0/24 gateway=192.168.2.1",
    "/ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade",
    "/ip service enable ssh",
]

# Conectar y enviar comandos
try:
    print("Conectando al router...")
    net_connect = ConnectHandler(**mikrotik)
    print("Conexión exitosa.")

    for command in commands:
        print(f"Ejecutando: {command}")
        net_connect.send_command(command)

    print("Configuraciones aplicadas correctamente.")
    net_connect.disconnect()

except Exception as e:
    print(f"Error: {e}")
