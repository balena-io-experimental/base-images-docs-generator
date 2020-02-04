#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Outputs the contents for this page https://www.balena.io/docs/reference/base-images/base-images-ref/
"""

import json
import os
import config as cfg
import helpers

repo = helpers.init_repo()

devices = helpers.get_devices()

# ---------------------------------------------------
# OS support by arch
# ---------------------------------------------------

arches = helpers.get_arches()
oses = helpers.get_oses()

architectures = {}

for arch in arches:

    # Add on the case were nothing is specified
    architectures[arch] = [""]

    for o in oses:
        with open(cfg.repo_dir + f"/contracts/sw.os/{o}/contract.json", 'r') as f:
            data = f.read()

            # Is this OS supported?
            if arch in data:
                architectures[arch].append(o)

# ---------------------------------------------------
# Language support
# ---------------------------------------------------
langs = helpers.get_langs()

# ---------------------------------------------------
# OS support
# this takes the available os and gets the tags dynamically
# ---------------------------------------------------

operating_systems = {}

for o in oses:
    if o != "resinos":
        operating_systems[o] = []

# ---------------------------------------------------
# Incompatible
# Langs and arches
# ---------------------------------------------------

incompatible = {}

for l in langs:

    incompatible[l] = []

    with open(cfg.repo_dir + f"/contracts/sw.stack/{l}/contract.json", 'r') as f:
        data = f.read()

        for arch in arches:
            if arch not in data:
                incompatible[l].append(arch)

# Prepend the empty case
langs.insert(0, "")

# ---------------------------------------------------
# Setup variants of OS
# ---------------------------------------------------

for o in operating_systems:

    # Need to update dict with tags
    with open(cfg.repo_dir + f"/contracts/sw.os/{o}/contract.json", 'r') as f:
        data = json.load(f)

        operating_systems[o] = ["latest"]

        for v in data["variants"][:1]:
            for d in v["variants"]:
                operating_systems[o].append((d["version"]))

# ---------------------------------------------------
# Get all the devices from the device contract
# ---------------------------------------------------

listings = []

for device in devices:

    # Manual override for certain devices
    if device in cfg.exclude:
        continue

    if os.path.isdir(cfg.repo_dir + f"/contracts/hw.device-type/{device}"):

        with open(cfg.repo_dir + f"/contracts/hw.device-type/{device}/contract.json",
                  'r') as f:

            contract = json.load(f)

            output = {
                "id": contract['slug'],
                "name": contract['name'],
                "arch": contract['data']['arch'],
                "distro": architectures.get(contract['data']['arch'])
            }

            listings.append(output)

# ---------------------------------------------------
# Output the page
# ---------------------------------------------------

print(
    "---\ntitle: Base Image List\nexcerpt: List of available base images and tags\n---\n<!-- Auto Generated by contracts -->"
)

# Output per architecture
for arch in sorted(architectures):
    print(f"\n\n### {cfg.headers[arch]}:")

    # Use a list comprehension to filter by device arch
    device_arch = [v for v in listings if v["arch"] == arch]

    for d in device_arch:

        # Print device headers
        print(f"\n\n##### {d['name']}\n\n")
        print("| Image | Links | Available Tag |")
        print("|:-----------|:------------|:------------|")

        # Now loop through each OS - will sort Debian later
        device_id = [v for v in listings if v["id"] == d['id']]

        for l in device_id:
            # Loop through the distro
            for o in l["distro"]:

                # Loop through the langs
                for l in langs:

                    # Base image name
                    base_image_link = cfg.image_base + d['id']
                    if o:
                        base_image_link = base_image_link + "-" + o
                    if l:
                        base_image_link = base_image_link + "-" + l

                    # Docker Hub
                    docker_hub_link = cfg.docker_base + d['id']
                    if o:
                        docker_hub_link = docker_hub_link + "-" + o
                    if l:
                        docker_hub_link = docker_hub_link + "-" + l

                    # GitHub
                    # This changes if we are at a device base or are in a language, the OS doesn't matter

                    if not l:
                        github_link = cfg.device_base + d['id']
                    else:
                        github_link = cfg.lang_base + l + "/" + d['id']

                    # Tags
                    if not l:

                        # If no OS provided we default to Debian
                        if not o:
                            o = "debian"

                        tags = ", ".join(operating_systems[o])
                    else:
                        tags = "For available image tags, refer [here](" + docker_hub_link + "/tags)"

                    # Finally just check that this isn't incompatible
                    if l in incompatible:
                        if d["arch"] in incompatible[l]:
                            # Incompatible
                            pass
                        else:
                            print(
                                f"| {base_image_link} | [Docker Hub]({docker_hub_link}), [GitHub]({github_link}) | {tags} |"
                            )
                    else:
                        print(
                            f"| {base_image_link} | [Docker Hub]({docker_hub_link}), [GitHub]({github_link}) | {tags} |"
                        )
