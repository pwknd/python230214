#demolist.py

colors = ["red","green","blue","red"]
print(colors)

colors.append("white")
print(colors)
colors.append("black")
print(colors)

colors.insert(1,"yellow")
colors +=["red"]
print(colors)
print(colors.index("red"))
print(colors.count("red"))


colors.remove("red")
print(colors)
colors.extend(["red","pink","white"])
print(colors)
