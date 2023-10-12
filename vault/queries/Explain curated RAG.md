#### [[index]]
Curated RAG is a simple [[prototype]] that showcases how to use [[Obsidian]] to create [[LLM]] driven [[chatbot]] instances. The plan is to make an [[open source]] [[project]] out of it

The idea is based on an [[Iterative process]]

Check out [[Quick Start]] for information of how to use it

There is a [[python app]] running in the background accessing the md files in the [[vault]]

#### [[prototype]]
The project is not designed to be a proper open-source collaborative project right now. If the interest is high it might become one.

Make sure to [[contact circularmachines]] if you want this project to succeed
#### [[Obsidian]]
  
Obsidian is a popular note-taking and knowledge management application that utilizes markdown for note creation and editing. It is renowned for its unique approach to note-taking, which emphasizes linking between notes to create a personal knowledge graph. Users create notes, which can then be interlinked through wiki-style links, allowing the formation of a network of information.
(From ChatGPT)
#### [[LLM]]
Large Language Models. What ChatGPT and similar chatbots are based on.
#### [[chatbot]]
A chatbot based on [[LLM]] such as [[ChatGPT]] or [[Llama]]


#### [[open source]]
I love open source for reasons I will come back to #todo
#### [[project]]
It's not a real project yet, but when it is, the documentation and project planning will be inside this [[obsidian]] [[vault]]. It's all very [[meta]]

Check out the [[roadmap]] that hopefully leads to the [[vision]]
#### [[Iterative process]]

The suggested iterative way of working:

1. Add relevant [[queries]] that you want your [[chatbot]] to be able to [[respond]] to
2. Add [[knowledge]] needed to [[respond]] to [[queries]]
3. Evaluate [[chatbot]] performance
4. Update [[notes]] in [[vault]] to help [[chatbot]] [[access]] the correct [[knowledge]]
#### [[Quick Start]]
Install [[requirements]]

Set [[environment variables]]

run [[python app]]

open [[Obsidian]] and select the "db" folder as the [[vault]]
in the [[queries folder]] create a new note, recommended to make a copy of the [[-copy me‽]] note

rename the note to your [[query]]

add the tag run anywhere in the note


#### [[python app]]
app.py is a simple python program with the following tasks:

* Monitoring the [[queries folder]] for the [[run command]]
* Getting the [[query]] from the [[file name]]
* Interfacing with the [[Chat API]] for [[retrieval]] and [[response]]
* Writing to the [[query file]]
* 
#### [[vault]]
A collection of notes in Obsidian. Basically a folder on your computer accessed by Obsidian and the [[python app]]
## Answer
Curated RAG is a prototype project that uses Obsidian, a note-taking and knowledge management application, to create Large Language Model (LLM) driven chatbot instances. It's an iterative process where relevant queries are added for the chatbot to respond to, knowledge is added to respond to these queries, the chatbot's performance is evaluated, and notes in the Obsidian vault are updated to help the chatbot access the correct knowledge. A Python app runs in the background, monitoring the queries folder for the run command, getting the query from the file name, interfacing with the Chat API for retrieval and response, and writing to the query file. The project is not yet open-source, but there are plans to make it so if there is enough interest.
