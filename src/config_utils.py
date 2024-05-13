import os
import tomli
import tomli_w

def check_and_create_config_file():
    """
    Check if .proompt file exists, create it with defaults if not.
    """
    config_file = '.proompt'
    if not os.path.exists(config_file):
        with open(config_file, 'wb') as f:
            default_config = {
                'default_model': 'llama-70b',
                'default_buffer': 'ask.md',
                'default_system_prompt': ''
            }
            tomli_w.dump(default_config, f)

def set_default_model(model: str):
    """
    Set default model in .proompt file.
    """
    config_file = '.proompt'
    with open(config_file, 'rb+') as f:
        config = tomli.load(f)
        config['default_model'] = model
        f.seek(0)
        tomli_w.dump(config, f)
        f.truncate()

def set_default_buffer(buffer: str):
    """
    Set default user buffer in .proompt file.
    """
    config_file = '.proompt'
    with open(config_file, 'rb+') as f:
        config = tomli.load(f)
        config['default_buffer'] = buffer
        f.seek(0)
        tomli_w.dump(config, f)
        f.truncate()

def set_default_system_prompt(prompt: str):
    """
    Set default system prompt in .proompt file.
    """
    config_file = '.proompt'
    with open(config_file, 'rb+') as f:
        config = tomli.load(f)
        config['default_system_prompt'] = prompt
        f.seek(0)
        tomli_w.dump(config, f)
        f.truncate()

def get_config_defaults():
    """
    Get default values from .proompt file.
    """
    check_and_create_config_file()
    config_file = '.proompt'
    with open(config_file, 'rb') as f:
        config = tomli.load(f)
        return {
            'default_model': config.get('default_model'),
            'default_buffer': config.get('default_buffer'),
            'default_system_prompt': config.get('default_system_prompt')
        }
