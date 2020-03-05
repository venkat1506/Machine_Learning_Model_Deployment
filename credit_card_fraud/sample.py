import json

input_file = open ('stores-small.json')
json_array = json.load(input_file)
store_list = []

for item in json_array:
    store_details = {"name":None, "city":None}
    store_details['name'] = item['name']
    store_details['city'] = item['city']
    store_list.append(store_details)

print(store_list)



# # print("********************",(sys.argv))

# resultjson={ 'Prediction':'' }
# datasize=len(sys.argv)
# print("Data size@@@@@@@@@@",datasize)

# data1= sys.argv[1]
# # print("data^^^^^^^^^^^",type((data1)))

# arraydata=data1.strip('][').split(', ')

# # arraydata=ast.literal_eval(data1)
# print("arry conversion ",arraydata)


# s=arraydata[0].strip('][').split(', ')
# print("arry conversion ",s)
# print("arry conversion ",type(s))

# json_array = json.load(sys.argv)
# print( "lenth######",json_array)

# for i in datasize:
#     print("%%%%%%%%%%%%",sys.argv[i])
#     CreditId={ 'Id'         :'',
#                 'Prediction':''}
#     # liststr = ast.literal_eval(sys.argv[i])
#     # print("list print##################",liststr)
#     # dataarray = [liststr]

#     # Idval=dataarray[0]
#     # dataarray.remove(dataarray[0])
#     # print("inside for loop",dataarray)
#     # predictionvalue = loaded_model.predict(listdata)
#     # CreditId.Id=Idval
#     # CreditId.predictionvalue
#     # resultjson.Prediction=CreditId

# print(resultjson)


# data=sys.argv[1]
# print("#$%^%^$%^&model data",data.remove(data[0]))
# data1=sys.argv[2]
# list1 = ast.literal_eval(data)
# list2 = ast.literal_eval(data1)
# data_exa=data_exa.append(list1)
# print(data_exa)
# data_exa=data_exa.append(list2)
# result = loaded_model.predict([list1,list2])
# print(result)


# data1=sys.argv[2]
# list2 = ast.literal_eval(data1)
# result1 = loaded_model.predict([list2])
# # print(result1)
# print(result,result1)



# dataframe.append(j)

# print(dataframe)
# data1=myresult[0]
# print("###",i.remove(i[0]))
# ids.append(i[0])
# print(ids)

# for i in range(0, len(j)):
#     j[i] = int(j[i])
# # Printing modified list
# print ("Modified list is : " + str(j))