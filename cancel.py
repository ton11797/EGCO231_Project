def Cancel(data):
    booklist = DB.get_room()
    array=[]
    for book in booklist["available-room"]:
        for cancel in data["Data"]:
            if cancel["Room"]==book["Room"]:
                status = False
                for schedule in book["schedule"]:
                    if cancel["Data_Time"]==book["Data_Time"]:
                        if whois(data["cookie_session"])=="admin" or whois(data["cookie_session"])==schedule["Username"]:
                            array.append({"Room":cancel["Room"],"Data_time":cancel["Data_Time"],"status":"success","error":"none"})
                            status = True
                        else:
                            array.append({"Room":cancel["Room"],"Data_time":cancel["Data_Time"],"status":"fail","error":"Permission denied"})
                if status:
                    array.append({"Room":cancel["Room"],"Data_time":cancel["Data_Time"],"status":"fail","error":"Room available"})
    respond = {"Data":array}
    return json.dumps(respond)    