import re
import subprocess

# Ping the loopback address (127.0.0.1) to make sure it's up
loopback_ping = subprocess.run(["ping", "-n", "1", "127.0.0.1"], capture_output=True)
if loopback_ping.returncode == 0:
    print("Loopback ping successful!")
else:
    print("Loopback ping failed")
    print("Something wrong on local device")

# Run the ipconfig command and capture its output
output = subprocess.check_output("ipconfig").decode()

# Use regular expressions to extract the IPv4 address from the output
ipv4_regex = r"IPv4 Address\. . . . . . . . . . . : ([\d\.]+)"
match = re.search(ipv4_regex, output)
if match:
    ip_address = match.group(1)
else:
    print("Could not find IPv4 address in output")
    exit()

# Ping the IPv4 address and measure round trip time
ipv4_ping = subprocess.run(["ping", "-n", "1", ip_address], capture_output=True)

# Check the return code to see if the ping was successful
if ipv4_ping.returncode == 0:
    print(f"Ping to {ip_address} successful!")
    # Extract the round trip time from the output using regular expressions
    time_regex = r"Average = (\d+)ms"
    match = re.search(time_regex, ipv4_ping.stdout.decode())
    if match:
        round_trip_time = match.group(1)
        print(f"Round trip time to {ip_address}: {round_trip_time}ms")
    else:
        print("Could not find round trip time in output")
else:
    print(f"Ping to {ip_address} failed")
    print("Check router/modem")

# Ping Google's DNS server (8.8.8.8) to make sure we have internet connectivity
google_ping = subprocess.run(["ping", "-n", "1", "8.8.8.8"], capture_output=True)
if google_ping.returncode == 0:
    print("Google ping successful!")
    # Extract the round trip time from the output using regular expressions
    time_regex = r"Average = (\d+)ms"
    match = re.search(time_regex, google_ping.stdout.decode())
    if match:
        round_trip_time = match.group(1)
        print(f"Round trip time to Google: {round_trip_time}ms")
    else:
        print("Could not find round trip time in output")
else:
    print("Google ping failed")

# Ping Twitch.tv to measure round trip time
twitch_ping = subprocess.run(["ping", "-n", "1", "twitch.tv"], capture_output=True)

# Check the return code to see if the ping was successful
if twitch_ping.returncode == 0:
    print("Twitch ping successful!")
    # Extract the round trip time from the output using regular expressions
    time_regex = r"Average = (\d+)ms"
    match = re.search(time_regex, twitch_ping.stdout.decode())
    if match:
        round_trip_time = match.group(1)
        print(f"Round trip time to Twitch: {round_trip_time}ms")
    else:
        print("Could not find round trip time in output")
else:
    print("Twitch ping failed")

# Ping Steampowered.com to measure round trip time
steam_ping = subprocess.run(["ping", "-n", "1", "steampowered.com"], capture_output=True)

# Check the return code to see if the ping was successful
if steam_ping.returncode == 0:
    print("Steam ping successful!")
    # Extract the round trip time from the output using regular expressions
    time_regex = r"Average = (\d+)ms"
    match = re.search(time_regex, steam_ping.stdout.decode())
    if match:
        round_trip_time = match.group(1)
        print(f"Round trip time to Steam: {round_trip_time}ms")
    else:
        print("Could not find round trip time in output")
else:
    print("Steam ping failed")

# Wait for user input before exiting
input("Press Enter to exit...")
