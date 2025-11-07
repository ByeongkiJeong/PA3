# PA3: Secure Python Built-in Wrapper Agent

This is an example project that helps external agents, such as LLMs, execute code and answer queries in a restricted environment by securely wrapping Python's built-in functions.

## Key Ideas

- **Secure Wrapping**: The `wrapped_builtins.py` file wraps standard Python built-in functions like `print()` and `len()` into functions with a `w_` prefix (e.g., `w_print`, `w_len`). Decorators are used to preserve the original function signatures, making it easy for the agent to understand and use the functions.
- **Restricted Environment**: The `ChatAgent` in `pa3_initial.py` can only use the functions passed as the `tools` parameter. This allows for selective exposure of functions, excluding potentially dangerous ones like `eval` or `exec`.

## File Structure

- `pa3_initial.py`: The main script that initializes and runs the `ChatAgent`.
- `wrapped_builtins.py`: Wraps built-in functions and manages the list of functions (`wrapped_builtins`) provided to the agent.
- `README.md`: The project's documentation in Korean.
- `README_EN.md`: The project's documentation in English.
- `.gitignore`: A list of files to be ignored by Git.

## Requirements

- Python 3.8+
- `python-dotenv`: Used to load environment variables from a `.env` file.
- `openai`: Interacts with the OpenAI API.
- `agent-framework`: An AI agent framework from Microsoft. For more details, see the [official GitHub repository](https://github.com/microsoft/agent-framework).

**Dependency Installation (Virtual Environment Recommended):**
```bash
# Create and activate a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies from requirements.txt
# Note: agent-framework may require a pre-release version.
pip install -r requirements.txt --pre
```

## Configuration

OpenAI API information is required to run the project. Create a `.env` file in the root directory and set the environment variables as shown below.

```env
# .env file example
OPENAI_MODEL_NAME="gpt-4o"
OPENAI_API_KEY="sk-..."
OPENAI_ENDPOINT="https://api.openai.com/v1"
```

## Usage

Once the environment variables are set, you can run the agent from the terminal in the following ways.

**1. Pass a query directly as an argument**
```bash
python pa3_initial.py "1 + 1"
```

**2. Run in interactive mode**
```bash
python pa3_initial.py
# Query: 0.043 - 0.001
```

**3. Pass input via a pipe (`|`)**
```bash
echo "2 * 3" | python pa3_initial.py
```

`pa3_initial.py` creates a `ChatAgent` and calls the `run()` function to process the query. The result is displayed on the standard output with a `Response:` prefix.

## Extension Method

To add a new function to `wrapped_builtins`:

1.  Define a new `w_<name>` function in the `wrapped_builtins.py` file using the `@wrap_builtin` decorator.
2.  Add the created function to the `wrapped_builtins` list.
3.  Modify `pa3_initial.py` to pass the function name or the entire list to the `tools` parameter.

> **⚠️ Security Warning**
> Exposing functions that can execute arbitrary code, such as `eval` or `exec`, to the agent can pose a serious security risk. The current code includes `w_eval`, so it must be disabled or used with caution in a real production environment.

## Author

Byeongki Jeong

## License

This project is licensed under the MIT License.

**MIT License**

Copyright (c) 2025 Byeongki Jeong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
