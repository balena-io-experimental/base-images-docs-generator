from git import Repo
import os
import config as cfg
import shutil

# ---------------------------------------------------
# Clone the latest version of the contracts repo
# ---------------------------------------------------


def init_repo():
    if not os.listdir(cfg.repo_dir):
        cloned_repo = Repo.clone_from(url=cfg.git_url, to_path=cfg.repo_dir)
    else:
        shutil.rmtree(cfg.repo_dir)
        cloned_repo = Repo.clone_from(url=cfg.git_url, to_path=cfg.repo_dir)

    return cloned_repo

# ---------------------------------------------------
# Get all device contracts from the hw.device-type folder
# ---------------------------------------------------


def get_devices():
    devices = os.listdir(cfg.repo_dir + "/contracts/hw.device-type")
    devices.sort()
    return devices

# ---------------------------------------------------
# Get all device architectures from the arch.sw folder
# ---------------------------------------------------


def get_arches():
    arches = os.listdir(cfg.repo_dir + "/contracts/arch.sw")
    arches.sort()
    return arches

# ---------------------------------------------------
# Get all OS from the sw.os folder
# ---------------------------------------------------


def get_oses():
    oses = os.listdir(cfg.repo_dir + "/contracts/sw.os")
    oses.remove("resinos")
    oses.sort()
    return oses

# ---------------------------------------------------
# Get all languages from the sw.stack folder
# ---------------------------------------------------


def get_langs():
    langs = os.listdir(cfg.repo_dir + "/contracts/sw.stack")
    return langs
