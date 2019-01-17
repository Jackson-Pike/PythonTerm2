# Task 1
# [ ] print ft_bones list
# [ ] delete "cuboid" from ft_bones
# [ ] reprint list
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
            "intermediate cuneiform", "medial cuneiform"]
print(ft_bones)
del ft_bones[2]
print(ft_bones)

# ------------------------ Task 2 --------------------
# [ ] print ft_bones list
# [ ] delete "cuboid" from ft_bones
# [ ] delete "navicular" from list
# [ ] reprint list
# [ ] check for deletion of "cuboid" and "navicular"
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
            "intermediate cuneiform", "medial cuneiform"]
del ft_bones[2]
del ft_bones[2]
print(ft_bones)

# --------------------------- Task 3 -------------------------
# [ ] pop() and print the first and last items from the ft_bones list
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
            "intermediate cuneiform", "medial cuneiform"]
print("First:", ft_bones.pop(0), "| Last: ", ft_bones.pop())
# [ ] print the remaining list
print("Remaining List: ", ft_bones)

# --------------------------- Task 4 Part 1 -------------------------
# [ ] complete the Register Input task above
purchase_amounts = []

while True:
    usr_add = input("Enter price of item: ")
    if usr_add.lower() != "done" or usr_add.lower() != "d":
        purchase_amounts.append(usr_add)
    else:
        break
# --------------------------- Task 4 Part 2 ------------------------------
# [ ] complete the Register Total task above
subtotal = 0

while purchase_amount:
    fl_val = float(purchase_amounts.pop())
    subtotal += fl_val
print(subtotal)


