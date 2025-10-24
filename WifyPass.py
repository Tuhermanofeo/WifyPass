import subprocess


#Obtiene metadatos
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('/n')

#Extrae nombres de red
profile = []
for i in data:
    if "All User Profile" in i:
        profile.append(i.split(":")[1][1:-1])

for i in profile:
    try: #Metadatos del perfil
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, "key=clear"]).decode('utf-8', errors="backslashreplace").split('/n')
        result = []

        #Extrae contraseña de los metadatos
        for b in results:
            if "Key Content" in b:
                result.append(b.split(":")[1][1:-1])
        #Imprime contraseña
        try:
            print("{:<30}| {:<}".format(i, result[0]))
        except Exception as e:
            print("{:<30}| {:<}".format(i, ""))
    except Exception as e:
        print(print("{:<30}| {:<}".format(i, "¡Error Ocurred!")))