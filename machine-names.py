"""
Output supported machine names and architectures for https://www.balena.io/docs/reference/base-images/devicetypes/

This script allows the user to print to the console a formatted table of machine names
and architectures for all device types with balena contracts https://github.com/balena-io/contracts
"""

import json
import os
import config as cfg
import helpers

repo = helpers.init_repo()

# Get all device contracts from the hw.device-type folder
devices = helpers.get_devices()

output = []

for device in devices:

    if device in cfg.exclude:
        continue

    if os.path.isdir(cfg.repo_dir + f"/contracts/hw.device-type/{device}"):

        with open(cfg.repo_dir + f"/contracts/hw.device-type/{device}/contract.json", 'r') as f:

            contract = json.load(f)

            output.append(contract)

# Sort the output by device name
output = sorted(output, key=lambda k: k['name'])

# Format the output for the documentation
print("Device Name | {{ $names.company.allCaps }}_MACHINE_NAME | {{ $names.company.allCaps }}_ARCH | GitHub")
print("------------ | ------------- | ------------- | -------------")

for o in output:
    print(
        f"| {o['name']} | {o['slug']} | {o['data']['arch']} | [Link]({cfg.github_repo}/{o['slug']}) |")
