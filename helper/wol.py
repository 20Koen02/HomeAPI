import socket
import struct


def wake_up(ip, mac):
    """
    Send Wake On LAN Magic Packet
    :param ip: The machine's IP Address
    :param mac: The machine's MAC Address
    """

    # Remove mac separator [:-\s]
    mac = mac.replace(mac[2], '')

    # Pad the synchronization stream.
    data = ''.join(['FFFFFFFFFFFF', mac * 20])
    send_data = b''

    # Split up the hex values and pack.
    for i in range(0, len(data), 2):
        send_data = b''.join([send_data,
                              struct.pack('B', int(data[i: i + 2], 16))])

    # Broadcast it to the LAN.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(send_data, (ip, 7))
