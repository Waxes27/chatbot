import os
import sys
import json

base = "Data"
question_words = ["what","why","who","is","when","how","are", "?"]
count = 0


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
    '''
        prints the requested directories
    '''
        if len(requested) == 0:
            print("The requested resource is empty or not found")
        else:
            for i in requested:
                print(i)

def read_instagram(type_of_file, base_dir,i):
    questions = []
    responses = []


    try:
        filename = base_dir+"/"+i[0]
        with open(filename,"r") as f:
            message = json.load(f)
            if message['messages'][0]['sender_name'] != "WeThinkCode_":
                for i in question_words:
                    if i in message['messages'][0]['content']:
                        print(message['messages'][0]['content'])
                        print("\n\n\n")
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
    





def main():

    requested_folders = get_folders()
    print_request(requested_folders)

    # instagram_messages_inbox()
    
    


main()
