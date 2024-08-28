import apt # type: ignore
import pip
import os
def install_packages(packages):
    for package in packages:
        try:
            apt.cache.Cache()[package].mark_install()
            apt.cache.Cache().commit()
        except Exception as e:
            print(f"Error installing {package}: {e}")

def install_pip_packages(packages):
    for package in packages:
        try:
            pip.main(['install', package])
        except Exception as e:
            print(f"Error installing {package}: {e}")

# Define packages to install
packages = ['ubuntu-desktop', 'ubuntu-restricted-extras', ...]
pip_packages = ['requests', 'pyautogui', ...]

# Install packages
install_packages(packages)
install_pip_packages(pip_packages)

# Reboot the system
print("Rebooting the system...")
os.system("sudo reboot now")