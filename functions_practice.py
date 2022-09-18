def hello():
    print("Hello!!")


def pack(fname):
    print(fname + " Miller")

pack("Avery")
pack("Hannah")
pack("Arnold")

def eat_lunch(food):
    if len(food) == 0:
        print("No food today.")
    else:
        for i in range(len(food)):
            if i == 0:
                print(f"First I eat {food[0]}")
            else:
                print(f"Next I eat {food[i]}")

hello()
print(pack)
eat_lunch([])
eat_lunch(["Burrito"])
eat_lunch(["candy","hotdog","Nachos","fries"])