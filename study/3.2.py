#3-4
names = ["Jay", "Tom", "Adel"];
print(names)
print(len(names))

#3-5
sickOne = "Tom";
print(sickOne + ' is sick.')
names.remove(sickOne)
print(names)
newOne = "Jerry";
print(newOne + ' is coming')
names.append(newOne)
print(names);
print(names[0] + " will come finally.");
print(names[1] + " will come finally.");
print(names[2] + " will come finally.");

#3-6
print("more people will come!")
names.insert(0, "Mr Left");
print(names);
names.insert(3, "Mr Middle");
print(names);
names.append("Mr right");
print(names);

#3-7
print("But something is EMERGCY, Three people can come!!!")
print(len(names))
names.pop();
names.pop();
names.pop();
names.pop();
print(len(names))
print(names);
print(names[0] + "is lucky!")
print(names[1] + "is lucky!")
names.pop(1)
names.pop(0)
print(names)
print("nobody Left")









