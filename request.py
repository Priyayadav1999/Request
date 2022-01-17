import requests
import json
import os

url="http://saral.navgurukul.org/api/courses"
k=requests.get(url)
a=json.loads(k.text)

list=[]
dict1={"courses":list }
for i in range(len(a["availableCourses"])):
    if os.path.exists("courses.json")==True:
        with open("courses.json") as file:
            k=json.load(file)
            p=a["availableCourses"][i]
            course=a["availableCourses"][i]["name"]
            course_id=a["availableCourses"][i]["id"]
            print(i+1,"  ",course, " ",course_id)
            l=k["courses"]
            l.append(p)
            dict1["courses"]=l
            z=open("courses.json","w")
            json.dump(dict1,z,indent=4)
            z.close()
    else:
        new_dict=a["availableCourses"][i]
        list.append(new_dict)
        x=open("courses.json","w")
        json.dump(dict1,x,indent=4)
        x.close()

user=int(input("enter serial number of course you want to choose :-"))

new=open("courses.json")
new_1=json.loads(new.read())
c=0
id_1=0
for j in new_1["courses"]:
    c+=1
    if user==c:
        url2 = "https://saral.navgurukul.org/api/courses/"+j["id"]+"/exercises"
        data=requests.get(url2)
        data_1=json.loads(data.text)
        id_1=j["id"]
        # print(j["id"])
        # print(data_1)
        with open("id.json","w") as co_id:
            json.dump(data_1,co_id,indent=4)
            c1=1
            for m in range(len(data_1["data"])):
                print(c1, " " , data_1["data"][m]["name"])
                c1+=1
# print(id_1)
user2=int(input("enter serial number for slug of exercises = "))

num=0
for n in data_1["data"]:
    num+=1
    if num==user2:
        url3="http://saral.navgurukul.org/api/courses/"+id_1+" /exercise/getBySlug?slug="+n["slug"]
        slug_data=requests.get(url3)
        slug_data_1=json.loads(slug_data.text)
        print(slug_data_1["content"])
        # with open("slug.json","w") as file_slug:
        #     json.dump(slug_data_1,file_slug,indent=4)

 