_gold = int(253)

print("猜猜我手中有几块金子?")
_answer = int( input("把你的答案写在这里吧:"))

if _answer == _gold:
    print("猜中了,真厉害!我把我手里的金子都给你")
elif _answer >_gold:
    print("哎呀,我手里没有这么多金子,我有这么富吗?")
else :
    print("才这么点?小看我了")
