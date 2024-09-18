# H1-code

H1-code is a command line tool to level up codebases to `H1` (high) quality. It processes files in a specified directory, creates backups, and applies AI-based improvements to enhance code quality.

## Installation
Recommended: Install using `pipx`:
```bash
pipx install git+https://github.com/matan-h/h1-code
```

Install using pip:

```bash
pip install git+https://github.com/matan-h/h1-code
```
<PyPI coming soon>

## Simple Example
```bash
h1-code <folder> <file-extension>
```

For example:

```bash
h1-code ./src dart
```
This command processes all Dart files in the `./src` directory, creates a backup, and applies AI-based improvements using the default model and API.

By default, it assumes the name of the language (as used in Markdown code blocks) is the same as the file extension, in other languages, such as python and JavaScript, you need to specify the language name using `-n <name>` (e.g., `h1-code src py -n python`)

### OpenAI
by default it assumes you have an [Ollama](https://github.com/ollama/ollama) server, with the model of `llama3.1`.
You can change the model using `--model` option, the URL (for example, to ClosedAI) with `--base_url` option, and api-key using `--api_key`.


## Backup Folders

- By default, H1-code creates sequential backup folders (e.g., `folder.h2-backup.0`, `folder.h2-backup.1`, etc.).
- Use the `--single-backup` flag to keep only one backup folder (e.g., `folder.h2-backup`).

## Dependencies

H1-code depends on:

* [OpenAI python SDK](https://github.com/openai/openai-python) - for sending prompts into any OpenAI compatible server (such as ollama)
* [rich](https://github.com/Textualize/rich) - for rich console output and progressbar

## Contribute

If you encounter issues or have suggestions, please open a [GitHub issue](https://github.com/matan-h/h1-code/issues).

If you find `H1-code` useful, consider supporting the project:

<a href="https://www.buymeacoffee.com/matanh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-blue.png" alt="Buy Me A Coffee" height="47" width="200"></a>