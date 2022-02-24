import json

def add_passengers(name , age , gender , mobile):
    #Statement 1.1 user_id -> (name + age + first 2 digits of mobile no)
    dic = {
    "user_id": name + age + mobile[:2] , 
    "name": name,
    "age": age,
    "gender": gender,
    "mobile_no": mobile
    }

    file = open("passengerlist.json" , 'r+')
    content = json.load(file)
    for ele in range(len(content)):
        if dic['user_id'] == content[ele]["user_id"]:
            file.close()
            return -1
    content.append(dic)
    file.seek(0)
    file.truncate()
    json.dump(add_new_passenger , file , indent = 4)
    file.close()


    # ------------------------------------------------------- #

    file2 = open("train.json" , 'r+')
    train_content = json.load(file2)
    train_content['passenger list'].append(dic['user_id'])
    file2.seek(0)
    file2.truncate()
    json.dump(train_content , file2 , indent = 4)
    file2.close()

    return 1