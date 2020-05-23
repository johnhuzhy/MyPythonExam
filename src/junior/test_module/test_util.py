# coding=utf-8
'''
test_moduleパッケージのtest_util.pyモジュールである。
'''
print('#'*15, __name__, '#'*15)
print('package:', __package__ or 'No Package')
print('name:', __name__)
print('doc:', __doc__ or 'No Doc')
print('file:', __file__)

Book_Name = 'げんや'
Book_Author = 'ひがしの けいご'

if __name__ == "__main__":
    print('*'*15, __name__, '*'*15)
    print('package:', __package__ or 'No Package')
    print('name:', __name__)
    print('doc:', __doc__)
    print('file:', __file__)
    print(f"『{Book_Name}』の著者は「{Book_Author}」である。")
