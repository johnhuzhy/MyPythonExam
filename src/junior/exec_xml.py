import xml.etree.ElementTree as ET
import os

if __name__ == "__main__":
    tree = ET.ElementTree(file="././prop/sample_book.xml")
    root = tree.getroot()
    print("root.tag:", root.tag)
    print('#'*33)
    for child in root:
        print(child.tag, child.attrib)
        for grandson in child:
            print(grandson.tag, ":", grandson.text)
        print('*'*33)

    for ele in tree.iter(tag="Book"):
        print(ele.tag, ele.attrib)
    print('#'*33)

    for ele in tree.iter(tag="Title"):
        print(ele.tag, ele.attrib, ele.text)
    print('#'*33)

    # for ele in tree.iter():
    #     print(ele.tag, ele.attrib, ele.text)
    # print('#'*33)

    for ele in tree.iterfind("Book/Title"):
        print(ele.attrib, ele.text)
    print('#'*33)

    for ele in tree.findall("Book"):
        print(ele.find('Title').attrib, ele.find('Title').text)
    print('#'*33)

    outpath = os.getcwd()
    file = outpath + '././prop/sample_book.xml'

    for price in root.iter("Price"):
        new_price = float(price.text) + 3
        price.text = str(new_price)
        price.set("updated","up")
    tree.write(file)

    # for book in root.findall("Book"):
    #     price = book.find("Price").text
    #     if float(price) > 150.0:
    #         root.remove(book)
    # tree.write(file)

    # ET.SubElement(root,"Book")
    # new_ele = root[2]
    # new_ele.text = "python"
    # tree.write(file)


    