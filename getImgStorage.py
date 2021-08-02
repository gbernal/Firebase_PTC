from firebase import Firebase
import os.path
config = {
    "apiKey": "AIzaSyDC6c2Suia5T0SYvxGC3cKOpBaYrBT98Sw",
    "authDomain": "paperdreams-d55db.firebaseapp.com",
    "databaseURL": "https://paperdreams-d55db.firebaseio.com",
    "projectId": "paperdreams-d55db",
    "storageBucket": "paperdreams-d55db.appspot.com",
    "messagingSenderId": "789122665908",
    "appId": "1:789122665908:web:f39c7077a851df532bf6e1",
    "measurementId": "G-LPXTECLBWC",
    "serviceAccount": "paperdreams-d55db-firebase-adminsdk-lodyy-34a22b1767.json"

}
list =[]
firebase = Firebase(config)
storage = firebase.storage()
files = storage.list_files()
imgDir = 'thumbnaildata'
i = 0
for file in files:
    imgPath = storage.child(file.name).get_url(None)
    urlParts = os.path.split(imgPath)
    #print(urlParts[1].split('%'))
    #Dir = urlParts[1].split('%')
    dir = urlParts[1].replace('%2F', '/')

    cleanDir = dir.split('?')
    checkDir =cleanDir[0].split('/')
    if checkDir[0] == imgDir :
        #print(cleanDir[0].split("/"))
        dir = cleanDir[0].split("/")
        if  dir[1]== '':
            print("In Directory")
        else:
            print("Downloading data")
            storage.child(cleanDir[0]).download('Data/'+checkDir[1])
        #cleanPath  = urlParts[1].replace('%2F','/')
        #cleanPath =  cleanPath.split('?')

        # if img[0] != '2F':
        #
        #     #storage.child(urlParts[1]).download('Data/'+img[0])
        #     i += 1
        #     storage.child(urlParts[1]).download('/Users/gbernal/Documents/GitHub/Firebase_PTC/Data/downloaded %d.png'% i)


#storage.child('thumbnaildata').list_files()
#storage.child("thumbnaildata/part-8c5024f86da70a0e32462de19db44ae4396a3c962627c68401df178599a2a080752bcba2.png").download("/Users/gbernal/Documents/GitHub/Firebase_PTC/Data/downloaded.png")

