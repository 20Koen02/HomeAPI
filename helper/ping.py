import platform  # For getting the operating system name
import subprocess  # For executing a shell command


def ping(ip):
    """
    Ping the specified host
    :param ip: IP Address to be pinged
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', ip]

    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
