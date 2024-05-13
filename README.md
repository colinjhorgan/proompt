**Proompt: A Library for AI-Assisted Writing**

Proompt is a Python library that helps you generate text based on user input using AI models. It provides a simple configuration file (`~/.proompt`) to customize your writing experience.

**Configure Proompt**

Create a `.proompt` file in your home directory to customize Proompt's behavior. Here's an example file:
```toml
default_model = "llama-70b"
default_buffer = "ask.md"
default_system_prompt = "Please respond to the following prompt:"
```
This file sets the default AI model to `llama-70b`, the default buffer file to `ask.md`, and the default system prompt to "Please respond to the following prompt:".

**Using Proompt**

Proompt provides a command-line interface to generate text based on user input. You can customize the behavior using command-line arguments or by modifying the `.proompt` file.

**Example Usage**

```
$ python proompt.py --model llama-8b --buffer my_buffer.md
```
This command uses the `llama-8b` model and `my_buffer.md` as the buffer file to generate text based on the user input.

**Features**

* Customize default AI model, buffer file, and system prompt using the `.proompt` file.
* Supports multiple AI models (e.g., `llama-70b`, `llama-8b`, `mixtral`, `gemma`).
* Parses user buffer files to include file contents in the generated text.

**Getting Started**

1. Install Proompt using `pip install proompt`.
2. Create a `.proompt` file in your home directory to customize Proompt's behavior.
3. Run `python proompt.py` to generate text based on user input.

**License**

Proompt is licensed under the [Insert License].

