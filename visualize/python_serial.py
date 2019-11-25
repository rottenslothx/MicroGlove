import settings
import serial
import re
import winsound
import time
import threading
import logging
import multiprocessing as mp

ser = serial.Serial(settings.SERIAL_PORT, 57600)
print("connected to: " + ser.portstr)
line_temp = ""


def read_all_filtered_out():
    global ser
    line_temp = ""
    attributes = []
    datalist = [{
                    "result": 0,
                    "id": 0,
                    "delta_time":0,
                    "angle_x":0,
                    "angle_y":0,
                    "angle_z":0
                },{
                    "result": 0,
                    "id": 0,
                    "delta_time":0,
                    "angle_x":0,
                    "angle_y":0,
                    "angle_z":0
                },{
                    "result": 0,
                    "id": 0,
                    "delta_time":0,
                    "angle_x":0,
                    "angle_y":0,
                    "angle_z":0
                },{
                    "result": 0,
                    "id": 0,
                    "delta_time":0,
                    "angle_x":0,
                    "angle_y":0,
                    "angle_z":0
                }]
    while len(attributes) < 6:
        for line in ser.read():
            # print(chr(line)+"("+str(line)+")",end='')
            # print(chr(line),end='')
            if line == 0xa :
                temp_attributes = line_temp.split(":")
                attributes = []
                for attribute in temp_attributes:
                    for sub_attribute in attribute.split("#"):
                        attributes.append(sub_attribute)
                if len(attributes) < 6 :
                    print(line_temp)
                    #clear if no collect char from a 1st char or not collect all data
                    line_temp = ""
                    break
                if attributes[0] != "Index" and attributes[2] != "DEL" \
                    and attributes[4] != "FIL":
                    #clear if no collect char from a 1st char or not collect all data
                    line_temp = "" 
                    break
                    pass
                angle = attributes[5].split(',')
                if len(angle) < 3 :
                    break
                data = {
                    "result": 0,
                    "id": attributes[1],
                    "delta_time":attributes[3],
                    "angle_x":angle[0],
                    "angle_y":angle[1],
                    "angle_z":angle[2]
                }
                datalist[int(attributes[1])]=data
                # print(attributes)
                print(data)
                print()
                line_temp = ""
            else :
                line_temp+=chr(line)
    return data
def terminate():
    global ser 
    ser.close()


if __name__ == '__main__':
    mode = 0
    finger = [0,0,0]
    one = 0
    two = 0
    three = 0
    four = [0,0,0]
    five = 0
    six = 0
    seven = 0
    cal1 = 0
    cal2 = 0
    cal3 = 0
    cal4 = 0
    cal5 = 0
    cal6 = 0
    cal7 = 0
    count = 1
    datalist = [{
                    "result": 0,
                    "id": 0,
                    "delta_time":0,
                    "angle_x":0,
                    "angle_y":0,
                    "angle_z":0
                },{
                    "result": 0,
                    "id": 0,
                    "delta_time":0,
                    "angle_x":0,
                    "angle_y":0,
                    "angle_z":0
                },{
                    "result": 0,
                    "id": 0,
                    "delta_time":0,
                    "angle_x":0,
                    "angle_y":0,
                    "angle_z":0
                },{
                    "result": 0,
                    "id": 0,
                    "delta_time":0,
                    "angle_x":0,
                    "angle_y":0,
                    "angle_z":0
                }]
    while True:
        for line in ser.read():
            # print(chr(line)+"("+str(line)+")",end='')
            # print(chr(line),end='')
            if line == 0xa :
                temp_attributes = line_temp.split(":")
                attributes = []
                for attribute in temp_attributes:
                    for sub_attribute in attribute.split("#"):
                        attributes.append(sub_attribute)
                if len(attributes) < 6 :
                    print(line_temp)
                    if int(attributes[1]) < 2000:
                        mode = 0
                    else:
                        mode = 1
                    #clear if no collect char from a 1st char or not collect all data
                    line_temp = ""
                    break
                if attributes[0] != "Index" and attributes[2] != "DEL" and attributes[4] != "FIL":
                    #clear if no collect char from a 1st char or not collect all data
                    line_temp = "" 
                    break
                    pass
                angle = attributes[5].split(',')
                if len(angle) < 3 :
                    break
                data = {
                    "result": 0,
                    "id": attributes[1],
                    "delta_time":attributes[3],
                    "angle_x":angle[0],
                    "angle_y":angle[1],
                    "angle_z":angle[2]
                }
                datalist[int(attributes[1])]=data
                if count == 1:
                    print("Calibrate!")
                    time.sleep(3)
                    count+=1
                if count < 500:
                    if int(datalist[0]["id"]) == 0:
                        cal1 += float(datalist[0]["angle_y"])
                        one = (cal1/count) + 40
                    if int(datalist[1]["id"]) == 1:
                        cal2 += float(datalist[1]["angle_y"])
                        two = (cal2/count) + 20
                    if int(datalist[2]["id"]) == 2:
                        cal3 += float(datalist[2]["angle_y"])
                        three = (cal3/count) + 25
                    if int(datalist[3]["id"]) == 3:
                        cal4 += float(datalist[3]["angle_y"])
                        four[0] = (cal4/count)
                    count+=1
                    print(one,' ',two,' ',three,)
                elif count == 500:
                    print("wait for next calibrate!")
                    time.sleep(3)
                    count+=1
                elif count > 500 and count < 1000:
                    if int(datalist[3]["id"]) == 3:
                        cal4 += float(datalist[3]["angle_y"])
                        four[1] = (cal4/count)
                    if int(datalist[0]["id"]) == 0:
                        cal5 += float(datalist[0]["angle_y"])
                        five = (cal5/count) + 40
                    if int(datalist[1]["id"]) == 1:
                        cal6 += float(datalist[1]["angle_y"])
                        six = (cal6/count) + 20
                    if int(datalist[2]["id"]) == 2:
                        cal7 += float(datalist[2]["angle_y"])
                        seven = (cal7/count) + 25
                    count+=1
                    print(five,' ',six,' ',seven)
                elif count == 1000:
                    print("Sucess!")
                    count+=1
                    time.sleep(3)
                four[2] = ((four[0]+four[1])/2) + 20
                print(one,' ',two,' ',three,' ',four[2],' ',five,' ',six,' ',seven)

                # print(attributes)
                if mode == 0:
                    if float(datalist[3]["angle_y"]) < four[2] and int(datalist[3]["id"]) == 3:
                        #print("in")
                        if finger[0] == 0 and float(datalist[0]["angle_y"]) > one and int(datalist[0]["id"]) == 0:
                            print('1')
                            with open("./finger1.txt", "w") as f:
                                f.write("100")
                            finger[0] = 1
                        elif float(datalist[0]["angle_y"]) < one and int(datalist[0]["id"]) == 0:
                            with open("./finger1.txt", "w") as f:
                                f.write("000")
                            finger[0] = 0

                        if finger[1] == 0 and float(datalist[1]["angle_y"]) > two and int(datalist[1]["id"]) == 1:
                            print('2')
                            with open("./finger2.txt", "w") as f:
                                f.write("100")
                            finger[1] = 1
                        elif float(datalist[1]["angle_y"]) < two and int(datalist[1]["id"]) == 1:
                            with open("./finger2.txt", "w") as f:
                                f.write("000")
                            finger[1] = 0

                        if finger[2] == 0 and float(datalist[2]["angle_y"]) > three and int(datalist[2]["id"]) == 2:
                            print('3')
                            with open("./finger3.txt", "w") as f:
                                f.write("100")
                            finger[2] = 1
                        elif float(datalist[2]["angle_y"]) < three and int(datalist[2]["id"]) == 2:
                            with open("./finger3.txt", "w") as f:
                                f.write("000")
                            finger[2] = 0
                    if float(datalist[3]["angle_y"]) > four[2] and int(datalist[3]["id"]) == 3:
                        if finger[0] == 0 and float(datalist[0]["angle_y"]) > five and int(datalist[0]["id"]) == 0:
                            print('1')
                            with open("./finger1.txt", "w") as f:
                                f.write("110")
                            finger[0] = 1
                        elif float(datalist[0]["angle_y"]) < five and int(datalist[0]["id"]) == 0:
                            with open("./finger1.txt", "w") as f:
                                f.write("010")
                            finger[0] = 0

                        if finger[1] == 0 and float(datalist[1]["angle_y"]) > six and int(datalist[1]["id"]) == 1:
                            print('2')
                            with open("./finger2.txt", "w") as f:
                                f.write("110")
                            finger[1] = 1
                        elif float(datalist[1]["angle_y"]) < six and int(datalist[1]["id"]) == 1:
                            with open("./finger2.txt", "w") as f:
                                f.write("010")
                            finger[1] = 0

                        if finger[2] == 0 and float(datalist[2]["angle_y"]) > seven and int(datalist[2]["id"]) == 2:
                            print('3')
                            with open("./finger3.txt", "w") as f:
                                f.write("110")
                            finger[2] = 1
                        elif float(datalist[2]["angle_y"]) < seven and int(datalist[2]["id"]) == 2:
                            with open("./finger3.txt", "w") as f:
                                f.write("010")
                            finger[2] = 0
                elif mode == 1:
                    if float(datalist[3]["angle_y"]) < four[2] and int(datalist[3]["id"]) == 3:
                        print("in")
                        if finger[0] == 0 and float(datalist[0]["angle_y"]) > one and int(datalist[0]["id"]) == 0:
                            print('1')
                            with open("./finger1.txt", "w") as f:
                                f.write("101")
                            finger[0] = 1
                        elif float(datalist[0]["angle_y"]) < one and int(datalist[0]["id"]) == 0:
                            with open("./finger1.txt", "w") as f:
                                f.write("001")
                            finger[0] = 0

                        if finger[1] == 0 and float(datalist[1]["angle_y"]) > two and int(datalist[1]["id"]) == 1:
                            print('2')
                            with open("./finger2.txt", "w") as f:
                                f.write("101")
                            finger[1] = 1
                        elif float(datalist[1]["angle_y"]) < two and int(datalist[1]["id"]) == 1:
                            with open("./finger2.txt", "w") as f:
                                f.write("001")
                            finger[1] = 0

                        if finger[2] == 0 and float(datalist[2]["angle_y"]) > three and int(datalist[2]["id"]) == 2:
                            print('3')
                            with open("./finger3.txt", "w") as f:
                                f.write("101")
                            finger[2] = 1
                        elif float(datalist[2]["angle_y"]) < three and int(datalist[2]["id"]) == 2:
                            with open("./finger3.txt", "w") as f:
                                f.write("001")
                            finger[2] = 0
                    if float(datalist[3]["angle_y"]) > four[2] and int(datalist[3]["id"]) == 3:
                        if finger[0] == 0 and float(datalist[0]["angle_y"]) > five and int(datalist[0]["id"]) == 0:
                            print('1')
                            with open("./finger1.txt", "w") as f:
                                f.write("111")
                            finger[0] = 1
                        elif float(datalist[0]["angle_y"]) < five and int(datalist[0]["id"]) == 0:
                            with open("./finger1.txt", "w") as f:
                                f.write("011")
                            finger[0] = 0

                        if finger[1] == 0 and float(datalist[1]["angle_y"]) > six and int(datalist[1]["id"]) == 1:
                            print('2')
                            with open("./finger2.txt", "w") as f:
                                f.write("111")
                            finger[1] = 1
                        elif float(datalist[1]["angle_y"]) < six and int(datalist[1]["id"]) == 1:
                            with open("./finger2.txt", "w") as f:
                                f.write("011")
                            finger[1] = 0

                        if finger[2] == 0 and float(datalist[2]["angle_y"]) > seven and int(datalist[2]["id"]) == 2:
                            print('3')
                            with open("./finger3.txt", "w") as f:
                                f.write("111")
                            finger[2] = 1
                        elif float(datalist[2]["angle_y"]) < seven and int(datalist[2]["id"]) == 2:
                            with open("./finger3.txt", "w") as f:
                                f.write("011")
                            finger[2] = 0
                print(data)
                #print()
                line_temp = ""
            else :
                line_temp+=chr(line)
    ser.close()