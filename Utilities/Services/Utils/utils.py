
import yaml, json, sys
import pandas as pd


def list():
    name_list = []
    alpha = 'a'
    for i in range(0, 13):
        name_list.append(alpha)
        alpha = chr(ord(alpha) + 2) 
    print ("List after allowed alphabets : " + str(name_list))
    return name_list

def convert_to_yaml(data):
    return sys.stdout.write(yaml.dump(data.json()))


def convert_to_table_data(data):
    val2 = data.json()
    return pd.DataFrame(val2, columns=["status", "type", "deleted", "_id", "_v", "text", "user", "source"]).set_index('text', drop=True)

if __name__ == "__main__":
    list()
    convert_to_yaml()
    convert_to_table_data()