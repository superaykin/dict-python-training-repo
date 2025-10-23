# Simulation 13 - Day 4

#declaring a dictionary
ed = {}
print(f"Empty Dictionary: {ed}")

print()
capitals = {"USA":"Washington", "France":"Paris", "India":"New Delhi"}
print(f"Country's Capital: {capitals}")

print()
numNames = {1:"One", 2:"Two", 3:"Three"}
print(f"Number Names: {numNames}")

print(F"index 1 {numNames[1]}")

multiDict = {1 : "test", 2 : { 1 : "new line", 2 : "line 3"}, 3 : "four"}

print(F"{multiDict}")
print(F"MultiDict index 2: {multiDict[2]}")
print(F"MultiDict index 2: {multiDict[2][1]}")

print()
sample = {True:"Ikenn", False:"Wew"}
print(f"Sample: {sample}")
print(F"True Index: {sample[False]}")



#creating a dictionary
empty_dict = {}
initial_dict = {"key":"value", 1:"One", "Fractional":23.12}
print(f"All the Dictionary: {empty_dict}\t{initial_dict}")
copy_key_dict = {*initial_dict}
copy_kv_pair = {**initial_dict}


#using the the get() in accessing the dictionary value
print()
print(capitals.get("France"))
print(capitals.get("India"))
