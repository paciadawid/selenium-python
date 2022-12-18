a_int = 1  # no max value
a_float = 1.0

a_string = "button=['test']"
a_string2 = 'button=["test"]'
print(a_string[2])

a_list = [0, 0, 0, 1, 2]  # ordered, mutable, not unique
a_list[0] = 100
a_list.append(5)
print(a_list[0])

a_tuple = (0, 0, 1, 2)  # ordered, immutable, not unique
# a_tuple[0] = 100

a_dict = {  # unordered, mutable, unique keys
    "colour": "white",
    "shape": "ball",
    1: 0
}
print(a_dict["colour"])

a_set = {0, 1, 2, 0}  # unordered, mutable, unique
print(a_set)

a_bool = True  # False if 0, "", [], (), {}, None

if a_bool:
    print("True")
else:
    print("False")

a_none = None

pajton = {
    "animal": "cat",
    "age": 4,
    "weight": 4.5,
    "colours": ("white", "black", "grey"),
    "toys": ["ball", "mouse"],
    "if_alive": True
}

print("My cat is " + str(pajton["age"]) + " years old")
print("My cat is {} years old".format(pajton["age"]))
print(f"My cat is {pajton['age']} years old")
