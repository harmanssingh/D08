dict1={"Daniel": "blue","SomeoneOne":"blue","SomeoneTwo0": "red"}

def reverse_lookup(dict_,value):
    lst=()
    for keys1 in dict_:
        if value == dict_[keys1]:
            lst+=(keys1,)
    return lst
