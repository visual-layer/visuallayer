import visuallayer as vl

print(vl.datasets.zoo.list_datasets())

print("Loading pets dataset from zoo")
my_pets = vl.datasets.zoo.load('vl-oxford-iiit-pets')

print("Gettting dataset info")
print(my_pets.info)

print("Gettting dataset report")
print(my_pets.report)

print("Running dataset explore")
my_pets.explore()

print("Exporting to pytorch")
train_dataset = my_pets.export(output_format="pytorch", split="train")
test_dataset = my_pets.export(output_format="pytorch", split="test")

print("Exporting issues")
my_pets.export_issues("./issues-pets.csv")

print("Success")