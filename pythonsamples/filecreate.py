#! usr/bin/python

try:
    fo = open("sample.txt","wb");
    print("name of the file", fo.name);
    print("is closed", fo.closed);
    print("opening mode", fo.mode);
    fo.write(b"Python is great language");
except Exception as ex:
    print("Exception {0}" .format(ex))
finally:
    fo.close()
