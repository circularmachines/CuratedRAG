import time
import os
import glob

import openai
openai.api_key = os.getenv("OPENAI_TOKEN")

def chatgpt(messages):
    
    response = openai.ChatCompletion.create(
        #model="gpt-3.5-turbo",
        model="gpt-4",
        temperature=0.3,
        messages=messages)
  
    return response['choices'][0]["message"]

def get_note(q,s):
    path="vault/"+s+".md"
    with open(path, 'r') as f:
        data = f.readlines()
        
    out="Query: "+q+"\n"

    out+=s+":\n"
    
    for d in data:
        out+=d

    return out

def ask(query):
    
    system_prompt="""
You will be given a question, and a text from an Obsidian.md note.
Your job is to request links from the obsidian note to learn more about the subject in order to answer the question, links are inside [[double brackets]]
Please don't request links more than once, since it will not give you any new information. 
Respond in one of the follow ways:
[[one single link]]
or, if you are ready to answer the query;
Answer: ..."""
    
    messages=[  {"role": "system", "content": system_prompt},
                {"role": "assistant", "content": "[[index]]"},
                {"role": "user", "content": get_note(query,"index")}]
    
    while True:
        mess=chatgpt(messages)
        
        if "Answer:" in mess["content"]:
            messages.append(mess)
            write_file(messages)
            break
    
        stripped=mess["content"].strip("[]")
        
        try:
            note=get_note(query,stripped)
            messages.append(mess)
            messages.append({"role": "user", "content": note})
            write_file(messages)
        except:
            None    

def write_file(messages):
    global latest_file

    md=""
    for m in messages:

        if m["role"]=="assistant":
            if "[[" in m["content"]:
                md+="#### "+m["content"]+"\n"
            if "Answer:" in m["content"]:
                md+="## Answer\n"
                md+=m["content"][8:]+"\n"
                print(m["content"][8:])
        if m["role"]=="user":
            md+="\n".join(m["content"].split("\n")[2:])+"\n"
            
    
    with open(latest_file, 'w') as f:
        f.write(md.replace("#run","run"))
        


def get_latest_modified_file(path):

    # Find all .md files in the specified path
    files = glob.glob(os.path.join(path, "*.md"))
    
    # If no .md files found, return None
    if not files:
        return None
    
    # Get the latest modified file
    latest_file = max(files, key=os.path.getmtime)

    with open(latest_file, 'r') as f:
        data = f.read()
  
    return latest_file,data

print("running...")

while True:
    latest_file, data = get_latest_modified_file('vault/queries')
    
    if "#run" in data:
        open(latest_file, 'w').close()
        file_name=os.path.normpath(latest_file).split(os.path.sep)[-1]
        query=os.path.normpath(latest_file).split(os.path.sep)[-1][:-3].replace("‽","?")
        print(query)
        ask(query)

    time.sleep(1)
