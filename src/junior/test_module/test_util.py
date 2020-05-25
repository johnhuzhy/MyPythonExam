# coding=utf-8
'''test_moduleパッケージのtest_util.pyモジュールである。'''

print('#'*15, __name__, '#'*15)
print('package:', __package__ or 'No Package')
print('name:', __name__)
print('doc:', __doc__ or 'No Doc')
print('file:', __file__)

Book_Name = 'げんや'
Book_Author = 'ひがしの けいご'


def cheeseshop(kind, *arguments, **keywords):
    '''**仮引数、*任意引数'''
    print("-- Do you hava any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print('-'*33)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ':', keywords[kw])


def concat(*args, sep='/'):
    '''任意引数リスト'''
    return sep.join(args)


if __name__ == "__main__":
    print('*'*15, __name__, '*'*15)
    print('package:', __package__ or 'No Package')
    print('name:', __name__)
    print('doc:', __doc__)
    print('file:', __file__)
    print(f"『{Book_Name}』の著者は「{Book_Author}」である。")
    print('#'*33)
    cheeseshop("Limburger", "It's very runny, sir.",
               "It's really very, very, VERY runny, sir.",
               shopkkeeper="Michael Palin", client="John Cleese", sketch="Cheese Shop Sketch")
    funny = ("Are you kidding me?","God damn it, It's a joke.")
    shopdict = dict(shopkkeeper="Arthas Menethil", client="Kel'Thuzad Naxxramas")
    print('+'*33) 
    cheeseshop("the high elves")
    print('+'*33) 
    cheeseshop("Ranger-General", *funny)
    print('+'*33) 
    cheeseshop("Banshee", **shopdict)
    print('#'*33)           
    c1 = concat("earth", "mars", "venus")
    print(c1)
    c2 = concat("earth", "mars", "venus", sep=".")
    print(c2)
