from configsimple import config, ConfigSimple, flag


class Component1:
    def __init__(self):
        myconf = ConfigSimple(component="comp1")
        config.add_config(myconf)
        myconf.add_argument("--foo", default="22", type=int, help="The FOO setting!")
        myconf.add_argument("--bar", type=flag)
        myconf.parse_args()
        print("Component1 foo is {}".format(myconf.get("foo")))


class Component2:
    def __init__(self):
        myconf = ConfigSimple(component="comp2")
        config.add_config(myconf)
        myconf.add_argument("--foo", default="xyz", type=str, help="The FOO setting, but a different one!")
        myconf.parse_args()
        print("Component2 foo is {}".format(myconf.get("foo")))


if __name__ == "__main__":
    config.add_argument("--bar", help="The BAR setting")
    config.add_argument("--foo", help="The toplevel FOO setting")
    config.add_argument("--comp", type=int, choices=[1, 2], required=True,  help="Component number")
    config.parse_args()
    print("Toplevel foo is {}".format(config.get("foo")))
    compclass = [Component1, Component2][config.get("comp")-1]
    comp = compclass()
    print("Get the global comp1.foo: {}".format(config.get("comp1.foo")))
    print("Get the global comp2.foo: {}".format(config.get("comp2.foo")))
    print("Get the global comp1.bar: {}".format(config.get("comp1.bar")))


