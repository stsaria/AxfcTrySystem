import requests, sys, os

savename = ""
subdomains = [
    "pepper",
    "saffron",
    "mars",
    "taurus",
    "aquarius",
    "aries",
    "earth",
    "jupiter",
    "mercury",
    "venus",
    "emerald",
    "sapphire",
    "peridot",
    "opal",
    "ape",
    "gorilla",
    "monkey",
    "chimpanzee",
    "capricomus",
    "pisces",
    "capricornus",
    "gemini",
    "diamond",
    "pearl",
    "aquamarine",
    "fenrir"
]

print("Axfc DL Try System")
path = input("Axfc DL URL : ").split("axfc.net")[-1]
filename = path.split("/")[-1]

os.makedirs("download", exist_ok=True)

for i in subdomains:
    url = "https://"+i+".axfc.net"+path
    print(url, end="")
    try:
        res = requests.get(url)
        res.raise_for_status()
        savename = "download/"+i+"-"+filename
        with open(savename, mode="wb") as f:
            f.write(res.content)
        print(" OK")
    except Exception:
        print(" Error")
        continue
    if os.path.isfile(savename) and not "-all" in sys.argv:
        break

if os.path.isfile(savename):
    print("ファイルがダウンロードできました")
else:
    print("ファイルがダウンロードできませんでした")