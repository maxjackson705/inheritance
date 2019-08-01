class parent:
    def __init__(self):
        print("In parent constructor")

    def abc(self):
        print("Method abc")


class childclass(parent):
    pass


c = childclass()
c.abc()
