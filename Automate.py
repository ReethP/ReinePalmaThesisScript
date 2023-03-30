# import required module
import os
# assign directory
directory = "data"
 
# iterate over files in
# that directory
master_array = []
for i in range(0,1000):
    master_array.append([])

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        # print(f)
        open_file = open(f,errors="ignore")
        counter = 0
        print(f)
        for line in open_file:
            line = line.replace("\n","")
            line = line.replace(" ","")
            line = line.replace("\'","")            
            line = line.replace("\x00","")            
            line = line.replace("\x9d","")            
            line = line.split(",")
            if counter > 4:
                line = list(map(float,line))
            while(len(line) < 4):
                line.append("")
            # print(line)
            # line = list(line)
            # line = line.append(" ")
            # for item in line:
            #     print(type(item))
            master_array[counter].append(line)
            # print(line)
            # print(len(line))
            counter+=1
        open_file.close()

# print(master_array)

exer_file = open("new_exer.csv","w")

for item in master_array:
    # FORMAT MO NALANG TO
    new_item = str(item)
    new_item = new_item.replace("\n","")
    new_item = new_item.replace(" ","")
    new_item = new_item.replace("\'","")
    new_item = new_item.replace("\"","")
    new_item = new_item.replace("[","") 
    new_item = new_item.replace("]","") 
    exer_file.write(str(new_item) + "\n")

exer_file.close()