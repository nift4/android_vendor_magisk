MY_PATH := vendor/magisk
MAGISK_OUT := $(PRODUCT_OUT)/obj/MAGISK

$(MAGISK_OUT)/magisk.zip:
	export ANDROID_BUILD_TOP=$$(pwd) MAGISK_OUT=$$(cd $(MAGISK_OUT); pwd) && $${ANDROID_BUILD_TOP}/$(MY_PATH)/build_magisk.sh
