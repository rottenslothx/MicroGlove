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


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

def read_all_filtered_out():
    global ser
    line_temp = ""
    attributes = []
    data = {}
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

def sound1(name):
    winsound.PlaySound("68441__pinkyfinger__piano-c.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    time.sleep(2)
    
def sound2(name):
    winsound.PlaySound("68442__pinkyfinger__piano-d.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    time.sleep(2)

def sound3(name):
    winsound.PlaySound("68443__pinkyfinger__piano-e.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    time.sleep(2)


if __name__ == '__main__':
    finger = [0,0,0]
    while True:
        for line in ser.read():
            thr_fingerche = threading.Thread(target=sound1, args=(1,))
            thr_fingermid = threading.Thread(target=sound2, args=(1,))
            thr_finger3rd = threading.Thread(target=sound3, args=(1,))
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
                # print(attributes)
                if finger[0] == 0 and float(angle[1]) > 40 and int(attributes[1]) == 1:
                    thr_fingerche.start()
                    finger[0] = 1
                if float(angle[1]) <20 and int(attributes[1]) == 1:
                    finger[0] = 0

                if finger[1] == 0 and float(angle[1]) > 50 and int(attributes[1]) == 2:
                    thr_fingermid.start()
                    finger[1] = 1
                if float(angle[1]) < 20 and int(attributes[1]) == 2:
                    finger[1] = 0

                if finger[2] == 0 and float(angle[1]) > 20 and int(attributes[1]) == 3:
                    thr_finger3rd.start()
                    finger[2] = 1
                if float(angle[1]) < 10 and int(attributes[1]) == 3:
                    finger[2] = 0

                print(data)
                print()
                line_temp = ""
            else :
                line_temp+=chr(line)
    ser.close()