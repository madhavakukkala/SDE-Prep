
def  add_sprinkles(func):
    def wrapper():
        print("*You add sprinkles 🧁*")
        func()
    return wrapper


@add_sprinkles
def get_ice_cream():
    print("Here is the Ice cream 🍨")


get_ice_cream()

add_sprinkles(get_ice_cream)