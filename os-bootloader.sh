#!/bin/bash

echo "os bootloader"
echo "os kernel"
echo "os device drivers"
echo "os file system"
echo "os process manager"
echo "os memory manager"
echo "os input/output system"
echo "os network stack"
echo "os security manager"
#create bootloader please
echo "bootloader is created"
#create kernel please
echo "kernel is created"
args=(
    --kernel=kernel
    --device-drivers=device-drivers
    --file-system=file-system
    --process-manager=process-manager
    --memory-manager=memory-manager
    --input-output-system=input-output-system
    --network-stack=network-stack
    --security-manager=security-manager
    --os=os
    --BootLoader=BootLoader
)
qemu-system-x86_64 "${args[@]}"