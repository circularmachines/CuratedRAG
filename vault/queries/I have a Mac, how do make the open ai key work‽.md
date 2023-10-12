#### [[index]]
Curated RAG is a simple [[prototype]] that showcases how to use [[Obsidian]] to create [[LLM]] driven [[chatbot]] instances. The plan is to make an [[open source]] [[project]] out of it

The idea is based on an [[Iterative process]]

Check out [[Quick Start]] for information of how to use it

There is a [[python app]] running in the background accessing the md files in the [[vault]]


#### [[Quick Start]]

1. [[install]] CuratedRAG
2. run [[python app]]
3. open [[Obsidian]] and select the "db" folder as the [[vault]]
4. in the [[queries folder]] create a new note, recommended to make a copy of the [[-copy me‽]] note
5. rename the note to your [[query]]
6. add the tag run anywhere in the note


#### [[install]]
make sure you have python 3.x.x installed (not sure what's required) #todo

clone project and 

```bash
git clone https://github.com/circularmachines/CuratedRAG.git
cd CuratedRAG
```

Install openai

```bash
pip install openai
```

Set [[environment variables]]

#### [[environment variables]]
The ```os.getenv("OPENAI_TOKEN")``` function call retrieves the value of the environment variable named ```OPENAI_TOKEN```. To use this functionality, you need to set the environment variable beforehand. 

[[set environment variables temporarily on Linux or Mac]]
[[set environment variables temporarily on Windows]]
[[set environment variables persistently on Linux or Mac]]
[[set environment variables persistently on Windows]]
#### [[set environment variables persistently on Linux or Mac]]
You can add the ```export``` statement to your shell profile script (```~/.bashrc```, ```~/.bash_profile```, ```~/.zshrc```, etc.):
```sh
echo 'export OPENAI_TOKEN="your_secret_token_here"' &gt;&gt; ~/.bashrc
```

Don't forget to source the profile script or reopen the terminal to apply the changes:
```sh
source ~/.bashrc
```

## Answer
To make the OpenAI key work on your Mac, you need to set it as an environment variable. You can do this by adding the export statement to your shell profile script. Here are the steps:

1. Open the terminal.
2. Type the following command: `echo 'export OPENAI_TOKEN="your_secret_token_here"' >> ~/.bashrc`. Replace "your_secret_token_here" with your actual OpenAI key.
3. To apply the changes, source the profile script by typing: `source ~/.bashrc`.

Now, your OpenAI key is set as an environment variable and can be accessed by the application.
