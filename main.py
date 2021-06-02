import os
import sys
import json

base = "Data"
question_words = ["what","why","who","is","when","how","are", "?", "can", "please", "if", "do"]
questions = []
responses = []

duplicate_instagram_questions = []
instagram_questions = []
instagram_lists = []
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
                        
                        # print(message['messages'][0]['content'])
                        # print("\n\n\n")
                        duplicate_instagram_questions.append(message['messages'][0]['content'])
                        
                        
                        for j in duplicate_instagram_questions:
                            if j not in instagram_questions:
                                instagram_questions.append(j)
                            # instagram_lists.append(instagram_questions)
            
            
                        
                
    except (json.decoder.JSONDecodeError, UnicodeDecodeError, KeyError):
        pass
 
                    
def read_resource(base_dir,type_of_file,i):
    
    global count

    if type_of_file == "instagram json":
        read_instagram(type_of_file, base_dir, i)
    
            


def instagram_messages_inbox():
    
    resource = "Data/instagram/messages/inbox/"
    

    for dir, folder, files in os.walk(resource):
        
        if len(files) != 0:
            
            read_resource(dir,"instagram json", files)
    
    
def twitter_messages_inbox():
    pass
    
    
def get_help(error):
    
    if IndexError:
        print("Missing parameter python3 main.py [FOLDER]")
    

def main():
    
    requested_folders = get_folders()
    instagram_messages_inbox()

    # print(requested_folders)


main()
# set(instagram_questions):
    
