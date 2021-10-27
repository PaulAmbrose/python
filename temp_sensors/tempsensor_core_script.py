def get_temp(dev_file):
    f = open(dev_file,"r")
    contents = f.readlines()
    f.close()
    index = contents[-1].find("t=")
    if index != -1 :
        temperature = contents[-1][index+2:]
        cels =float(temperature)/1000
        return cels
if __name__ =="__main__":
    temp = get_temp("/sys/bus/w1/devices/28-021317c245aa/w1_slave")
    print(temp)
    
