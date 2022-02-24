import json

def update_user_details(user_id , mobile):

    with open("passengerlist.json" , 'r+') as fp1:
        content = json.load(fp1)
        for ele in range(len(content)):

            if(content[ele]['user_id'] == user_id):
                content[ele]["mobile_no"] = mobile
                
        fp1.seek(0)
        fp1.truncate()
        json.dump(content , fp1 , indent = 4)
    return 1