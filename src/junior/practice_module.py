'''juniorパッケージのpractice_module.pyモジュールである。'''
import test_module as tm
from test_module.test_util import Book_Name,Book_Author,concat

print('#'*15, __name__, '#'*15)
print('package:', __package__ or 'No Package')
print('name:', __name__)
print('doc:', __doc__)
print('file:', __file__)

print('#'*33)
print(tm.sys.path)
print(tm.os.getcwd())

print('#'*33)
print(f"『{Book_Name}』の著者は「{Book_Author}」である。")
c3 = concat("earth", "mars", "venus")
print(c3)
