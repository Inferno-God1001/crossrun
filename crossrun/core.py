import subprocess
import os


def set_code(language=None, code=None):
    """
    Execute code in a given programming language.

    Args:
        language (str): The language to run ('bash', 'ruby', 'python', 'javascript').
        code (str): The code to execute.

    Returns:
        str: The output of the executed code, or an error message.
    """
    if not language or not code:
        return 'Language and code are required'

    languages_list = [
        {'language': 'bash',       'extension': '.sh'},
        {'language': 'ruby',       'extension': '.rb'},
        {'language': 'python',     'extension': '.py'},
        {'language': 'javascript', 'extension': '.js', 'delta': 'node'},
    ]

    supported = [item['language'] for item in languages_list]

    if language not in supported:
        return 'Language not found'

    try:
        # Custom quote/brace escaping
        code = code.replace('*-,,', '""""')
        code = code.replace('*-,',  "'''")
        code = code.replace('-,,',  '"')
        code = code.replace('-,',   "'")
        code = code.replace('<;',   '{')
        code = code.replace(';>',   '}')

        lang_item = next(item for item in languages_list if item['language'] == language)
        extension = lang_item['extension']
        command   = lang_item.get('delta', language)
        file_name = language + extension

        with open(file_name, 'w') as f:
            f.write(code)

        result = subprocess.run(
            [command, file_name],
            capture_output=True,
            text=True
        )

        os.remove(file_name)

        return result.stdout if result.stdout else result.stderr

    except Exception as e:
        if os.path.exists(file_name):
            os.remove(file_name)
        return f'Fatal: {e}'
