import subprocess

meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

data= meta_data.decode('utf-8', errors="backslashreplace")

data = data.split('\n')
profiles = []

for i in data:
    if "all user profile" in i:

        i = i.split(":")
        i = i[1]
        i = i[1:-1]
        profiles.append(i)

print("{:<30} | {:<}".format("Wi-Fi Name", "Password"))
print("-------------------------")

for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key = clear'])
        results = results.decode('utf-8', errors="blackslashreplace")
        results = results.split("\n")

        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        try:
               print("{:<30} | {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30} | {:<}".format(1, ""))
    except subprocess.CalledProcessError:
        print("Encoding Error Occured")
