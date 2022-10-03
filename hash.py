import hashlib
import pathlib

for path in pathlib.Path("imagen").iterdir():
    if path.is_file():
        with open(path, 'rb') as f:
            md5 = hashlib.md5(f.read())
            if ("e5ed313192776744b9b93b1320b5e268"== md5.hexdigest()):
                print(str(path))
                print(md5.hexdigest())
                print("La imagen con ese hash es:" + str(path))