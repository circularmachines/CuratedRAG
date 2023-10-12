#### [[index]]
Curated RAG is a simple [[prototype]] that showcases how to use [[Obsidian]] to create [[LLM]] driven [[chatbot]] instances. The plan is to make an [[open source]] [[project]] out of it

The idea is based on an [[Iterative process]]

Check out [[Quick Start]] for information of how to use it

There is a [[python app]] running in the background accessing the md files in the [[vault]]


#### [[python app]]
app.py is a simple python program with the following tasks:

* Monitoring the [[queries folder]] for the [[run command]]
* Getting the [[query]] from the [[file name]]
* Interfacing with the [[Chat API]] for [[retrieval]] and [[response]]
* Writing to the [[query file]]

check [[install]] for information about installation


#### [[install]]
make sure you have python 3.x.x installed (not sure what's required) #todo

clone project and 

```bash
git clone [repository URL]
cd CuratedRAG
```

Install openai

```bash
pip install openai
```

Set [[environment variables]]

## Answer
The python library you need is openai.
