You can add the ```export``` statement to your shell profile script (```~/.bashrc```, ```~/.bash_profile```, ```~/.zshrc```, etc.):
```sh
echo 'export OPENAI_TOKEN="your_secret_token_here"' &gt;&gt; ~/.bashrc
```

Don't forget to source the profile script or reopen the terminal to apply the changes:
```sh
source ~/.bashrc
```
