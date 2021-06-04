# from _typeshed import FileDescriptor
import os
import sys
import json
import time
import js2py


base = "Data"
question_words = ["what","why","who","is","when","how","are", "?", "can", "please", "if", "do"]
questions = []
responses = []

twitter_questions = []
twitter_final = []

duplicate_instagram_questions = []
instagram_questions = []
instagram_lists = []
info = []
count = 0


base = "Data"

def get_folders():
    
    tmp = []

    
    for dir, folder, files in os.walk(base):
    
        try:

            if len(folder) != 0 and sys.argv[1] in dir.lower():
    
                tmp.append(f"{dir}/{folder}")
    
        except IndexError as e:
            
            get_help(e)
            exit()
    return tmp


def get_help(error):
    
    if IndexError:
        print("Missing parameter python3 main.py [FOLDER]")


def print_request(requested):
    
    if len(requested) == 0:
        print("The requested resource is empty or not found")
    else:
        for i in requested:
            print(i)

def read_instagram(type_of_file, base_dir,i):

    try:
        filename = base_dir+"/"+i[0]
        with open(filename,"r") as f:

            message = json.load(f)
            
            if message['messages'][0]['sender_name'] != "WeThinkCode_":
                for i in question_words:
                    if i in message['messages'][0]['content']:
                        
                        duplicate_instagram_questions.append(message['messages'][0]['content'])
                        
                        for j in duplicate_instagram_questions:
                            if j not in instagram_questions:
                                instagram_questions.append(j)                   
                
    except (json.decoder.JSONDecodeError, UnicodeDecodeError, KeyError):
        pass
    
                    
def read_instagram_resource(base_dir,type_of_file,i):
    '''
    reads the differrent directories
    '''
    global count

    if type_of_file == "instagram json":
        read_instagram(type_of_file, base_dir, i)


def instagram_messages_inbox():
    
    resource = "Data/instagram/messages/inbox/"
    

    for dir, folder, files in os.walk(resource):
        
        if len(files) != 0:
            
            read_instagram_resource(dir,"instagram json", files)


def read_twitter(type_of_file, base_dir, i):
    # print(i)

    
    try:
        filename = base_dir+"/"+i[0]
        with open(filename,"r") as f:
            data = f.read()
            jsonData = js2py.eval_js(f'{data}')
            
            for j in jsonData:
                for key, value in j.items():

                    if value['messages'][0]['messageCreate']['senderId'] != "2977649117":
                        for word in question_words:
                            
                            if word in value['messages'][0]['messageCreate']['text']:
                                # twitter_questions.append(value['messages'][0]['messageCreate']['text'])
                                print(value['messages'][0]['messageCreate']['text'])

    except (json.decoder.JSONDecodeError, UnicodeDecodeError, KeyError):
        pass
        

    # pass
    

def read_twitter_resource(base_dir,type_of_file,i):
    
    if type_of_file == "twitter js":
        read_twitter(type_of_file, base_dir, i)

        # pass
    
    
    
def twitter_messages_inbox():
    
    resource = "Data/twitter/twitter-2021-05-26-17480c63da92aaa2744379d2492a6129c4432411f2f50759e4037730274b70cb/data"
    
    for dir, folder, files in os.walk(resource):
        
        if len(files) != 0:
            
            read_twitter_resource(dir, "twitter js", files)
            # print(files)
            # exit()
    
    
    
def get_help(error):
    
    if IndexError:
        print("Missing parameter python3 main.py [FOLDER]")
    

def main():
    
    requested_folders = get_folders()
    instagram_messages_inbox()
    twitter_messages_inbox()


main()
    
