data_list = []

def readData ():
    data_file = open("data.txt", "r")
    for line in data_file:
        line = line.split()
        obj = []
        obj.append(float(line[0]))
        obj.append(float(line[1]))
        data_list.append(obj)
    data_file.close()

def writeData (cluster, file_name="cluster.txt"):
    cluster_file = open(file_name, "w")
    for obj in cluster:
        string = ""
        for i in obj:
            string += str(i) + " "
        string += '\n'
        cluster_file.write(string)
    return
