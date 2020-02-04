"""
This is the config file to manage contracts documentation
Can override specific devices here e.g. if you need to hide a device
"""

# Location of contracts repo
git_url = "https://github.com/balena-io/contracts.git"

# Where to store the cloned repo
repo_dir = "./contracts"

# Link to device base
device_base = "https://github.com/balena-io-library/base-images/tree/master/balena-base-images/device-base/"

# Link to language base
lang_base = "https://github.com/balena-io-library/base-images/tree/master/balena-base-images/"

# Link to DockerHub base
docker_base = "https://hub.docker.com/r/balenalib/"

# Link to base images
image_base = "{{ $names.base_images.lib }}/"

# Base images repo
github_repo = "{{ $links.githubBaseImages }}"

# Excluded device list
exclude = ["nitrogen8mm-dwe", "m2pcie-tx2"]

# Map arch headers to a nicer output format
headers = {
    "aarch64": "aarch64",
    "amd64": "amd64",
    "armv5e": "armv5e",
    "armv7hf": "ARMv7hf",
    "i386": "i386",
    "i386-nlp": "i386-nlp",
    "rpi": "ARMv6hf"
}
