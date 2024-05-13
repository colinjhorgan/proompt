# Proompt: Easy AI Proompting

**Proompt**
*Verb*<br>
The act of sending a prompt off to an LLM in the hopes that it will solve your problem instead of you having to do any real work.<br><br>
*Why should I learn to code when I can proompt?* <br><br>

Proompt is a Python library that helps you program using AI models hosted via the Groq API. This library defines a very primitive user interface that I like when I do my work. I am currently only maintaining this library for my own purposes, if there are strong ideas for improvement or big issues that I don't catch I will respond to PRs and Issues.

## Why Proompt?
I don't really like the big services for proompting AI models like GitHub copilot or AWS codewhisper because 1. I think they don't provide enough control to users about what to pass to your AI model, 2. They also force you to proompt in the same window as your code which I think is weird, and 3. They box you into using only a single LLM. This library addresses all of these problems as I'll quickly show below.

## Get Started with Proompt
### Groq API
The first thing you will need is an API key from Groq. Set this api key in the following way:
```bash
export GROQ_API_KEY=<insert-key-here>
```
### Install Proompt
Install proompt via pip with the following command:
```python
pip install https://github.com/colinjhorgan/proompt.git
```
I recommend aliasing proompt to something shorter like "llm" with the following:
```bash
alias llm="proompt"
```

### Creating a User Buffer
The concept of a user buffer is very simple. This is just a file that the user writes their prompt into that get sents to a specified model via the Groq API. The default name of the file that Proompt looks for is ask.md. Run the following commands to send your first request via proompt:
```bash
$ echo "Say Hello" >> ask.md
$ proompt
```
proompt will then automatically pull the contents of ask.md, create a request for the Groq API, and send that request. To inspect the response, simply open up ask.md or refresh the file if you have it open. <br><br>
You can specify which file to use as a user buffer with the --buffer or -f argument, ex:
```bash
$ proompt -f prompt.md
```
Using multiple buffers can be nice if you intend to have multiple conversations with LLMs going in parallel.

### Specifying Models
Proompt supports many of the models hosted on Groq. To specify the model to send your proompt to use the --model or -m argument. Ex:
```bash
$ proompt -m llama-8b
```
Here is the table of models supported by Proompt
| Model Name | Groq Model ID |
| --- | --- |
| llama-70b | llama3-70b-8192 |
| llama-8b | llama3-8b-8192 |
| mixtral | mixtral-8x7b-32768 |
| gemma | gemma-7b-it |


## More Details
### Configure Proompt

Proompt uses a `.proompt` file in your current directory to customize Proompt's behavior. Here's an example `.proompt` file:
```toml
default_model = "llama-70b"
default_buffer = "ask.md"
default_system_prompt = ""
```
This file is created automatically the first time you call `proompt`. You can update it with the setter arguments shown in `proompt --help`.

### Passing Files to the User Buffer
Proompt does string formatting almost similar to Jinja2. If you enclose the name of a file (relative to your current directory) in double braces, Proompt will automatically replace this decoration with the file contents at runtime. For example if I have a file called hello.py which looks like this:
```python
print("Hello world!")
```
and my ask.md file looks like this:
```markdown
What does this code do?
{{hello.py}}
```
then the LLM will recieve this:
```markdown
What does this code do?
print("Hello world!")
```
I really like this because it gives the user complete control over the context you send in your prompt. A really cool use case is to scrape documentation HTML via `curl` and then pass that to the LLM in this way. Usually you get a good answer! (Unless you use gemma, no one likes gemma)

### How to Use Proompt Good?
I do all my work in Neovim. I have a file called ask.md which I write my prompts into and then call the `proompt` command to send the prompt to the LLM I want. I can then quickly refresh the file with a `:e` and viola we have the response in a format which is easy to manipulate. This is good enough for me. If you use a different code editor in which quickly switching between files (or refreshing files) is tedious, then proompt probably isn't for you - which is cool. There's plenty of other libraries out there!
