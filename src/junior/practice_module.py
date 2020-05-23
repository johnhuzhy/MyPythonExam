'''
juniorパッケージのpractice_module.pyモジュールである。
'''
import test_module
import test_module.test_util

print('#'*15, __name__, '#'*15)
print('package:', __package__ or 'No Package')
print('name:', __name__)
print('doc:', __doc__)
print('file:', __file__)

print(f"『{test_module.test_util.Book_Name}』の著者は「{test_module.test_util.Book_Author}」である。")
