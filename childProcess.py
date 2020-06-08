"""
Name = Mert Can
Surname  = Denli
Python3.6
Implementation of os and multiprocessing modules in python.

"""

import uuid
from multiprocessing import *
import os
import requests
import hashlib


def downloadFile(url, liste, file_name=None, ):
    r = requests.get(url, allow_redirects=True)
    file = file_name if file_name else str(uuid.uuid4())
    open(file, 'wb').write(r.content)
    print("{} downloaded.".format(file_name))
    liste.append(file_name)


def getHash(file):
    hashingAlg = hashlib.sha256()
    with open(file, "rb") as f:#Reads file in binary mode .
        pic = f.read()
        hashingAlg.update(pic)#Sends files to hashing algorithm.
        a = hashingAlg.hexdigest()#Creates a new hexadecimal number to identify file's contents.
        return a


def checkDups(hashSet):
    _size = len(hashset)
    repeated = []
    for i in range(_size):
        k = i + 1

        for j in range(k, _size):  # CHECK duplicates.

            if hashset[i] == hashset[j] and hashset[i] not in repeated:
                repeated.append(liste[i])
    return repeated


if __name__ == '__main__':
    liste = []
    urls = [
        "http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
        "https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
        "http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]



    a = os.fork()  # Starts new process with process ıd 0.
    if a == 0:
        print("I am a child process with ID = {}".format(a))
        co = 0
        for url in urls:
            co = co + 1
            downloadFile(url, liste, file_name="File{}".format(co))

    try:  # Prevent orphan process situation using wait.
        os.wait()

        # Waits for completion of a child process.
    except ChildProcessError:  # if process not a child rasises error.
        print("Files downloaded")

    with Pool(processes=4) as pool:  # Use pool of workers to execute gethash function
        hashset = pool.map(getHash, liste)
        pool.close()

    repeated = checkDups(hashset)

    if a == 0:
        for i in repeated:
            print("{} is a duplicate.".format(i))


