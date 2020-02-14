# Output the base images so I don't have to
import json
import config as cfg
import helpers

repo = helpers.init_repo()

langs = helpers.get_langs()
os = helpers.get_oses()
arch = helpers.get_arches()

# Langs
print("-------------------------")
print("LANGUAGES")
print("-------------------------")

for lang in langs:

    print("-------------------------")
    print(lang)
    print("-------------------------")

    with open(cfg.repo_dir + f"/contracts/sw.stack/{lang}/contract.json", 'r') as f:
        data = json.load(f)


    print("Latest: {}".format(data["data"]["latest"]))

    for v in data["variants"]:
        print(v["version"])

    # Need to get supported arch for each lang

# OS
print("-------------------------")
print("OS")
print("-------------------------")
for o in os:

    print("-------------------------")
    print(o)
    print("-------------------------")

    with open(cfg.repo_dir + f"/contracts/sw.os/{o}/contract.json", 'r') as f:
        data = json.load(f)

    print("Latest: {}".format(data["data"]["latest"]))

    for v in data["variants"][:1]:
        for d in v["variants"]:
            print(d["version"])

    # Need to get support arch for each lang