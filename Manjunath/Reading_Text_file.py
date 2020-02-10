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
        self.Actual_Test_Time = 0
        self.Ideal_Accle_pack = 0
        self.Ideal_Temp_pack  = 0
        self.Ideal_Batt_pack  = 0
        self.Accle_pack_loss  = 0
        self.Temp_pack_loss   = 0
        self.Batt_pack_loss   = 0

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


    def Ideal_data_cal(self, Input_Test_Time , Class_data , Acceler_Data):
        self.Actual_Test_Time = Input_Test_Time - Class_data[1]
       
        self.Ideal_Accle_pack = self.Actual_Test_Time *  Acceler_Data

        self.Ideal_Temp_pack  = self.Actual_Test_Time / 60

        self.Ideal_Batt_pack  = self.Actual_Test_Time / 60

        return [int(self.Ideal_Accle_pack) , int(self.Ideal_Temp_pack) ,int(self.Ideal_Batt_pack),int(self.Actual_Test_Time)]


    def Loss_pack(self,  Find1 , data_cal):

        self.Accle_pack_loss = 100 - ((Find1[0] / data_cal[0]) * 100 )

        self.Temp_pack_loss  = 100 - ((Find1[2] / data_cal[1]) * 100)

        self.Batt_pack_loss  = 100 - ((Find1[3] / data_cal[2]) * 100)

        return [float(self.Accle_pack_loss) , float(self.Temp_pack_loss) , float(self.Batt_pack_loss)]

data =Asen().Find(My_list)
#print("Data from given txt file",data)

data1 = Asen().Ideal_data_cal(Total_test_time , data ,Acceler_Data)
#print("Data from given txt file",data1)

data2 =Asen().Loss_pack(data , data1)
print("Accle_pack_Loss : ",data2[0])
print("Temp_pack_loss : ",data2[1])
print("Batt_pack_loss : ",data2[2])
print("Number of disconnect : ",data[4])


    
