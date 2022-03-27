import zipfile
out_file = "../magisk.zip"
abi_map={"x64" : ["x86_64", "x86"], "arm64" : ["arm64-v8a", "armeabi-v7a"]}
def extract_as(zip, name, as_name, dir):
    info = zip.getinfo(name)
    info.filename = as_name
    zip.extract(info, dir)

with zipfile.ZipFile(out_file) as zip:
    arch = "arm64"
    extract_as(zip, f"lib/{ abi_map[arch][0] }/libmagisk64.so", "magisk64", arch)
    extract_as(zip, f"lib/{ abi_map[arch][1] }/libmagisk32.so", "magisk32", arch)
    standalone_policy = False
    try:
        zip.getinfo(f"lib/{ abi_map[arch][0] }/libmagiskpolicy.so")
        standalone_policy = True
    except:
        pass
    extract_as(zip, f"lib/{ abi_map[arch][0] }/libmagiskinit.so", "magiskinit", arch)
    if standalone_policy:
        extract_as(zip, f"lib/{ abi_map[arch][0] }/libmagiskpolicy.so", "magiskpolicy", arch)
    else:
        extract_as(zip, f"lib/{ abi_map[arch][0] }/libmagiskinit.so", "magiskpolicy", arch)
    extract_as(zip, f"lib/{ abi_map[arch][0] }/libmagiskboot.so", "magiskboot", arch)
    extract_as(zip, f"lib/{ abi_map[arch][0] }/libbusybox.so", "busybox", arch)
    arch = "x64"
    extract_as(zip, f"lib/{ abi_map[arch][0] }/libmagisk64.so", "magisk64", arch)
    extract_as(zip, f"lib/{ abi_map[arch][1] }/libmagisk32.so", "magisk32", arch)
    standalone_policy = False
    try:
        zip.getinfo(f"lib/{ abi_map[arch][0] }/libmagiskpolicy.so")
        standalone_policy = True
    except:
        pass
    extract_as(zip, f"lib/{ abi_map[arch][0] }/libmagiskinit.so", "magiskinit", arch)
    if standalone_policy:
        extract_as(zip, f"lib/{ abi_map[arch][0] }/libmagiskpolicy.so", "magiskpolicy", arch)
    else:
        extract_as(zip, f"lib/{ abi_map[arch][0] }/libmagiskinit.so", "magiskpolicy", arch)
    extract_as(zip, f"lib/{ abi_map[arch][0] }/libmagiskboot.so", "magiskboot", arch)
    extract_as(zip, f"lib/{ abi_map[arch][0] }/libbusybox.so", "busybox", arch)
    if standalone_policy:
        extract_as(zip, f"lib/{ abi_map['x64'][0] }/libmagiskpolicy.so", "magiskpolicy", ".")
    else:
        extract_as(zip, f"lib/{ abi_map['x64'][0] }/libmagiskinit.so", "magiskpolicy", ".")
    extract_as(zip, f"assets/boot_patch.sh", "boot_patch.sh", "all")
    extract_as(zip, f"assets/util_functions.sh", "util_functions.sh", "all")
