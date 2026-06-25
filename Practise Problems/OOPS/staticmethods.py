class employee:

    def __init__(self, name , position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager' , 'Cashier', 'Cook', 'janitor']
        return position in valid_positions
    

# print(employee.is_valid_position("Cook"))

obj1 = employee("spongebob", "Cook")

print(obj1.get_info())


