file = open("shopping_list.txt", "w")
print("enter 5 shopping items:")
for i in range(5):
    item = input(f"item {i+1}:")
    file.write(item+"\n")
file.close()


print("\n---- Shopping List----")
file = open("shopping_list.txt","r")
print(file.read())
file.close()

file = open("Shopping_list.txt","a")

print("add2 more shopping items:")
for i in range(2):
    item = input(f"New Item {i + 1}: ")
    file.write(item + "\n")

file.close()


print("\n--- Updated Shopping List ---")
file = open("shopping_list.txt", "r")

for line in file:
    print(line.strip())

file.close()

print("\nThank you for using My Shopping List Manager!")