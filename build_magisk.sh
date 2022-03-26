/usr/bin/python3 -m venv $MAGISK_OUT/venv
. $MAGISK_OUT/venv/bin/activate
cd $ANDROID_BUILD_TOP/vendor/magisk/src
./build.py -r -o $MAGISK_OUT/main_obj all
