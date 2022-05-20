def add(*args):
    total = 0
    for i in args:
        total += i
    return total #for문에서 return을 쓸수있다. 그런데 for문은 return만나면 한번쓰고 바로 종료되서 쓰는 의미가없을듯.
    
c = add(1,2,3,4,5,6,7,8,9)
print(c)
