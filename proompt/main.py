import os
import re 
import argparse

from groq import Groq

from .config_utils import *

MODEL_LOOKUP = {
    'llama-70b':'llama3-70b-8192',
    'llama-8b':'llama3-8b-8192',
    'mixtral':'mixtral-8x7b-32768',
    'gemma':'gemma-7b-it',
}

def append_to_file(file_name, string_to_append):
    """
    Appends a string to the end of a file.
    
    Parameters:
    file_name (str): The name of the file to append to.
    string_to_append (str): The string to append to the file.
    """
    with open(file_name, 'a') as f:
        f.write('\n'+string_to_append)


def parse_user_buffer(filename):
    """
    Opens a file and returns its contents as a string, ignoring markdown comments.
    
    Parameters:
    filename (str): The name of the file to parse.
    
    Returns:
    str: The contents of the file, ignoring markdown comments.
    """
    with open(filename, 'r') as f:
        lines = [line for line in f.readlines() 
                if not line.lstrip().startswith('<!--')]
    return ''.join(lines)


def format_buffer_contents(string, search_pattern='{{(.*?)}}' ):
    """
    Replaces occurrences of the search pattern in a string with file contents.
    
    Parameters:
    string (str): The string to search and replace in.
    search_pattern (str): The pattern to search for in the string.
    
    Returns:
    str: The string with the search pattern replaced with file contents.
    """
    # Find all occurrences of the search_pattern in the string
    matches = re.findall(search_pattern, string)

    # Iterate through the matches and replace them with their corresponding file contents
    for match in matches:
        print(match)
        file_path = match.strip()
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                file_contents = file.read()
            string = string.replace('{{'+match+'}}', file_contents)
        else:
            print(f"Warning: File not found at path '{file_path}'")

    return string


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--set-system-prompt',
        help='Set default system prompt',
        type=str,
        metavar='',
        required=False,)
    parser.add_argument(
        '--set-default-model',
        help='Set default model',
        type=str,
        metavar='',
        required=False,)
    parser.add_argument(
        '--set-default-buffer',
        help='Set default user buffer',
        type=str,
        metavar='',
        required=False,)
    parser.add_argument(
        '--model',
        '-m',
        help='Model name to use for request',
        type=str,
        metavar='',
        required=False,)
    parser.add_argument(
        '--buffer',
        '-f',
        help='Buffer filename to use for request',
        type=str,
        metavar='',
        required=False,)
    args = parser.parse_args()

    # Setters for configuring the .proompt file
    if args.set_system_prompt:
        set_default_system_prompt(args.set_system_prompt)
        return

    if args.set_default_model:
        set_default_model(args.set_default_model)
        return

    if args.set_default_buffer:
        set_default_buffer(args.set_default_buffer)
        return

    # Get defaults from .proompt and overwrite with args if necessary
    config = get_config_defaults()

    if args.model:
        config['default_model'] = args.model

    if args.buffer:
        config['default_model'] = args.buffer

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    buffer_contents = parse_user_buffer(config['default_buffer'])
    buffer_contents_fmtd = format_buffer_contents(buffer_contents)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": config['default_system_prompt']
            },
            {
                "role": "user",
                "content": buffer_contents_fmtd,
            }
        ],
        model=MODEL_LOOKUP[config['default_model']],
    )

    append_to_file(
        config['default_buffer'],
        chat_completion.choices[0].message.content)

if __name__ == "__main__": 
    main()
