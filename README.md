# crossrun

Run code in multiple programming languages directly from Python.

## Installation

```bash
pip install git+https://github.com/Inferno-God1001/crossrun.git
```

## Supported Languages

| Language   | Command used |
|------------|-------------|
| bash       | bash        |
| ruby       | ruby        |
| python     | python      |
| javascript | node        |

## Usage

```python
from crossrun import set_code

# Run bash
output = set_code('bash', 'echo "Hello from bash"')
print(output)

# Run python
output = set_code('python', 'print("Hello from Python")')
print(output)

# Run javascript
output = set_code('javascript', 'console.log("Hello from JS")')
print(output)

# Run ruby
output = set_code('ruby', 'puts "Hello from Ruby"')
print(output)
```

## Special Syntax

crossrun supports a custom escaping syntax for quotes and braces:

| Syntax  | Replaced with |
|---------|--------------|
| `-,`    | `'`          |
| `-,,`   | `"`          |
| `*-,`   | `'''`        |
| `<;`    | `{`          |
| `;>`    | `}`          |

## License

MIT
