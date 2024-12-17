worker = [
    {
        "name":"name",
        "phone":"phone",
        "email":"email",
        "post":"post",
        "numberRoom":"numberRoom",
        "skype":"skype"

    }
]


def addWorker(worker):
    name = input("input your name: ")
    phone = input("input your phone: ")
    email = input("input your email: ")
    post = input("input your post: ")
    numberRoom = input("input your numberRoom: ")
    skype = input("input your skype: ")
    worker.append({
        "name":name,
        "phone":phone,
        "email":email,
        "post":post,
        "numberRoom":numberRoom,
        "skype":skype
    })
    showWorker(worker)

def showWorker(worker):
    for item in worker:
        print(item)

def deleteWorker(worker):
    workerName = input("Input the name of the worker to delete: ")
    for item in worker:
        if item["name"] == workerName:
            worker.remove(item)
            print(f"Worker '{workerName}' has been deleted.")
            return
    print(f"Worker '{workerName}' not found.")

def searchWorker(worker):
    workerName = input("Input the name of the worker to search: ")
    for item in worker:
        if item["name"] == workerName:
            print(f"Worker '{workerName}' has been found.")
            print(f"Worker '{item['name']}',{item['phone']},{item['email']}',{item['post']},{item['numberRoom']},{item['skype']}')")
            return

def changeWorker(worker):
    workerName = input("Input the name of the worker to change: ")
    for item in worker:
        if item["name"] == workerName:
            new_name = input("input your new name: ")
            new_phone = input("input your new phone: ")
            new_email = input("input your new email: ")
            new_post = input("input your new post: ")
            new_numberRoom = input("input your new numberRoom: ")
            new_skype = input("input your new skype: ")
            item["name"] = new_name
            item["phone"] = new_phone
            item["email"] = new_email
            item["post"] = new_post
            item["numberRoom"] = new_numberRoom
            item["skype"] = new_skype
            print(f"Worker '{workerName}' has been changed.")
            print(
                f"Worker '{item['name']}',{item['phone']},{item['email']}',{item['post']},{item['numberRoom']},{item['skype']}')")




addWorker(worker)
addWorker(worker)
searchWorker(worker)
changeWorker(worker)
deleteWorker(worker)