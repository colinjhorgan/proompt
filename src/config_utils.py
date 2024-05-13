import os
import tomli
import tomli_w

def check_and_create_config_file():
    """
    Check if .proompt file exists, create it with defaults if not.
    """
    config_file = '.proompt'
    if not os.path.exists(config_file):
        with open(config_file, 'w') as f:
            default_config = {
                'default_model': 'llama3-70b-8192',
                'default_user_buffer': 'ask.md',
                'default_system_prompt': ''
            }
            toml.dump(default_config, f)

def set_default_model(model: str):
    """
    Set default model in .proompt file.
    """
    config_file = '.proompt'
    with open(config_file, 'r+') as f:
        config = toml.load(f)
        config['default_model'] = model
        f.seek(0)
        toml.dump(config, f)
        f.truncate()

def set_default_user_buffer(buffer: str):
    """
    Set default user buffer in .proompt file.
    """
    config_file = '.proompt'
    with open(config_file, 'r+') as f:
        config = toml.load(f)
        config['default_user_buffer'] = buffer
        f.seek(0)
        toml.dump(config, f)
        f.truncate()

def set_default_system_prompt(prompt: str):
    """
    Set default system prompt in .proompt file.
    """
    config_file = '.proompt'
    with open(config_file, 'r+') as f:
        config = toml.load(f)
        config['default_system_prompt'] = prompt
        f.seek(0)
        toml.dump(config, f)
        f.truncate()

