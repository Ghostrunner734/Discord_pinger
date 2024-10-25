import socket


# Функция для пинга сервера и получения IP-адреса
def ping_server(server):
    try:
        ip_address = socket.gethostbyname(server)
        return ip_address
    except socket.gaierror:
        return None


# Открываем файл для записи
with open('servers_ips.txt', 'w') as file:
    ip_addresses = []  # Список для хранения найденных IP-адресов
    not_found_servers = set()  # Множество для хранения не найденных серверов

    for i in range(11000):  # от 0000 до 9999
        server_name = f'frankfurt{i:04d}.discord.gg'  #Измените здесь название

        # Пропускаем сервер, если он уже был не найден
        if server_name in not_found_servers:
            continue

        ip = ping_server(server_name)
        if ip:
            ip_addresses.append(ip)  # Добавляем только IP в список
            print(ip)
        else:
            not_found_servers.add(server_name)  # Добавляем не найденный сервер в множество
            print(f'{server_name} - не найден')

    # Записываем все найденные IP-адреса в файл в формате ip, ip, ip
    if ip_addresses:
        file.write(', '.join(ip_addresses) + '\n')
