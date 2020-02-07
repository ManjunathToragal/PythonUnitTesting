import json

File_txt = input("Enter file name with path : ") #"Text_file.txt"

File_txt = open(File_txt)

My_list = [json.loads(i.strip()) for i in File_txt]

Lenght = len(My_list)

print(Lenght)

Total_test_time = int(input("Enter Test Sensor Test time  : "))

Acceler_Data    = int(input("Enter Accelerometer Data per sec  : "))

Temp_Bat        = int(input("Enter Temp and Battery  Data per min  : "))


class Asen:
    def __init__(self):

        self.Accle_count = 0
        self.Temp_count  = 0
        self.Batt_count  = 0
        self.Dis_conn    = 0
        self.Num_disconn = 0
        self.loss_time   = 0
        self.flag        = 0

    def Find(self, My_data):
        for i in range(len(My_data)):
            if(My_data[i]["PID"]=="0"):
                self.Accle_count +=1

            elif(My_data[i]["PID"]=="1"):
                self.Temp_count +=1

            elif(My_data[i]["PID"]=="2"):
                self.Batt_count +=1

            elif(My_data[i]["PID"]=="998"):
                self.Num_disconn +=1
                if self.flag == 0:
                    self.Dis_conn = My_data[i]["TS"]
                    self.flag = 1

            elif(My_data[i]["PID"]=="999" and self.flag==1):
                self.loss_time= self.loss_time+((My_data[i]["TS"] - self.Dis_conn)/1000)
                self.flag=0

        return [int(self.Accle_count),int(self.loss_time),int(self.Temp_count),int(self.Batt_count),int(self.Num_disconn)]

        

#ins = Asen()
#data = ins.Find(My_list)

data =Asen().Find(My_list)
print("Data from given txt file",data)


def Ideal_data(Class_data,Total_test_time ):

    for i in range(len(Class_data)):
        if i==1:
            Actual_test_time = int(Total_test_time) - data[1]

    Ideal_Accle_data = Actual_test_time * 5

    Ideal_Temp_data  = Actual_test_time / 60

    Ideal_Batt_data  = Actual_test_time /60

    return [int(Actual_test_time) ,int(Ideal_Accle_data),int(Ideal_Temp_data) ,int(Ideal_Batt_data)]


data_Actual = Ideal_data(data,Total_test_time)
print("Data from User and text file parameter calculation",data_Actual)


Accle_loss = 100 - ((data[0]/data_Actual[1]) * 100)

print("Accle_loss : ", Accle_loss )

Temp_loss  = 100 - ((data[2] / data_Actual[2] ) * 100)

print("Temp_loss : ",Temp_loss)

Batt_loss  = 100 - ((data[3] / data_Actual[3]) * 100)

print("Batt_loss : ",Batt_loss)
    

