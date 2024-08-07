def get_file(file,reference):

    with open(file,'r') as f:
        data = f.read()

    with open(reference,'r') as f:
        ref = f.read()

    # Clears white lines.
    data = "\n".join([ll.rstrip() for ll in data.splitlines() if ll.strip()])
    ref = "\n".join([ll.rstrip() for ll in ref.splitlines() if ll.strip()])
    print(ref)

    print(data)

    if ref == data:
        return True
    else:
        return False


if __name__ == '__main__':
    print(get_file("output/xerces/simple.txt","references/simple.xml"))