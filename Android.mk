MY_PATH := vendor/magisk
MAGISK_OUT := $(PRODUCT_OUT)/obj/MAGISK

MAGISK_ZIP := $(MAGISK_OUT)/magisk.zip
MAGISKUNZIPPED := $(MAGISK_OUT)/magisk

$(MAGISK_ZIP): $(MY_PATH)/magisk.zip
	cp $< $@

$(MAGISKUNZIPPED): $(MAGISK_ZIP)
	export ANDROID_BUILD_TOP=$$(pwd) && mkdir -p $(MAGISKUNZIPPED) && cd $(MAGISKUNZIPPED) && python3 $$ANDROID_BUILD_TOP/$(MY_PATH)/unpack.py
