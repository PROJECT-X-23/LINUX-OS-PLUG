import os
import apt # type: ignore
import apt_pkg # type: ignore
import pip
import random




def LinuxOsInstall():
        # Install required packages
    
        # Install required packages
        apt.update()
        #python saga
        apt.install('python3-pip', 'python3-dev')
        apt.install('python3-setuptools')
        apt.install('python3-wheel')
        apt.install('python3-distutils')
        apt.install('python3-distutils-extra')
        apt.install('python3-pyqt5')
        apt.install('python3-pyqt5-sip')
        #end
        apt.install("git")
        apt.install("curl")
        apt.install("wget")
        apt.install("unzip")
        apt.install("zip")
        apt.install("tar")
        apt.install("xz-utils")
        apt.install("xz")
        #install os
        apt.install("qemu")
        apt.install("qemu-system-x86_64")
        apt.install("qemu-system-i386")
        apt.install("qemu-system-alpha")
        apt.install("qemu-system-mips")
        apt.install("qemu-system-mips64")
        apt.install("qemu-system-mips64el")
        apt.install("qemu-system-mipsel")
        apt.install("qemu-system-ppc")
        apt.install("qemu-system-ppc64")
        apt.install("qemu-system-s390x")
        apt.install("qemu-system-sparc")
        apt.install("qemu-system-sparc64")
        apt.install("qemu-system-x86")
        apt.install("qemu-system-x86_64")
        apt.install("wine64")
        #facultative tools
        apt.install("nasm")
        apt.install("gcc")
        apt.install("g++")
        apt.install("clang")
        apt.install("clang++")
        apt.install("clang-format")
        apt.install("clang-tidy")
        apt.install("clang-analyzer")
        apt.install("openjdk-8-jdk")
        apt.install("openjdk-8-jre")
        apt.install("openjdk-11-jdk")
        apt.install("openjdk-11-jre")
        #end
        #check
        if not os.path.exists("/usr/bin/python3"):
                    print("Python3 not found")
                    return False
        if not os.path.exists("/usr/bin/git"):
                    print("Git not found")
                    return False
        #check jdk
        if not os.path.exists("/usr/bin/java"):
                    print("Java not found")
                    return False
        #close
        print("installation complete")
        print("do you want to reboot?")
        print("y/n")
        reboot = input()
        if reboot == "y":
                os.system("sudo reboot now")
        elif reboot == "n":
                print("aniways i will reboot")
                os.system("sudo reboot now")
        else:
                os.system("sudo reboot now")
        

