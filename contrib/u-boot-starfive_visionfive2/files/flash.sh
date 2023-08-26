#!/bin/sh

DEVICE=$1
UBPATH=$2

[ -n "$DEVICE" -a -n "$UBPATH" ] || exit 32
[ -b "$DEVICE" ] || exit 33
[ -r "${UBPATH}/u-boot-spl.bin.normal.out" ] || exit 34

case "${UBPATH}" in
/dev/mtd*) # QSPI
    # TODO: add support for flashing SPI (via install-u-boot /dev/mtd?).
    # needs mtd-tools packaged + creation of visionfive2_fw_payload.img
    # for flashing look at /proc/mtd for
    # mtd0: 00040000 00001000 "spl"
    # mtd2: 00300000 00001000 "uboot"
    # and:
    # flashcp -v u-boot-spl.bin.normal.out /dev/mtd0
    # flashcp -v visionfive2_fw_payload.img /dev/mtd2
    #[ -r "${UBPATH}/u-boot.itb" ] || exit 34
    #mkimage -f visionfive2-uboot-fit-image.its -A riscv -O u-boot -T firmware visionfive2_fw_payload.img
    :
    ;;
*) # NVMe/eMMC/microSD
    [ -r "${UBPATH}/u-boot.itb" ] || exit 34
    dd if="${UBPATH}/u-boot-spl.bin.normal.out" of="${DEVICE}" seek=4096 conv=notrunc,fsync || exit 35
    dd if="${UBPATH}/u-boot.itb" of="${DEVICE}" seek=8192 conv=notrunc,fsync || exit 35
    ;;
esac
