# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification
import csv

# Displays the inventory.
def display_inventory(inventory):
    for k,v in inventory.items():
        print(v,k)
    print("Total number of items:",sum(inventory.values()))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    added_items_dict = dict()
    for i in added_items:
        added_items_dict[i] = added_items_dict.get(i, 0) + 1
    from collections import Counter
    i= Counter(inventory)
    a_i= Counter(added_items_dict)
    result=(i+a_i)
    inventory.clear()
    inventory.update(dict(result))
    return


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    k_list=[]
    for k,v in inventory.items(): 
        k=str(k)
        k_list.append(k)
    #print(k_list)
    max_key_len=int(len(max(k_list, key=len)))
    #print(max_key_len)
    a=10
    print("\n")
    print("Inventory:")
    print("count".rjust(a," "),"item name".rjust(max_key_len+a," "), sep='')
    print('-'*(max_key_len+2*a))
    if order=='count,asc':
        for k,v in sorted(inventory.items(),key=lambda v:v[1]):
            v=str(v)   
            k=str(k)
            print(v.rjust(a," "), k.rjust(max_key_len+a," "),sep='')
    elif order=='count,desc':
        for k,v in sorted(inventory.items(),key=lambda v:v[1], reverse=True):
            v=str(v)   
            k=str(k)
            print(v.rjust(a," "), k.rjust(max_key_len+a," "),sep='')
    else:
        for k,v in inventory.items():
            v=str(v)   
            k=str(k)
            print(v.rjust(a," "), k.rjust(max_key_len+a," "),sep='')
    print('-'*(max_key_len+2*a))
    print("Total number of items:",sum(inventory.values()))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    import_inv = open(filename)
    inv_Reader = csv.reader(import_inv)
    for row in inv_Reader:
        imp_dict={x:row.count(x) for x in row}
    from collections import Counter
    i= Counter(inventory)
    i_d= Counter(imp_dict)
    inventory.clear()
    inventory.update(dict(i+i_d))
    import_inv.close()
    return


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    newlist = list()
    for k,v in inventory.items():
        newlist2=list()
        newlist2=[k]*v
        newlist.extend(newlist2)
    if filename==None:
        with open('export_inventory.csv','w') as export_inv:
            export_inv_write= csv.writer(export_inv)
            export_inv_write.writerow(newlist)
    else:
        with open(filename,'w') as export_inv:
            export_inv_write=csv.writer(export_inv)
            export_inv_write.writerow(newlist)
    export_inv.close() 