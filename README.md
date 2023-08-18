# SnapGPT

SnaptGPT allows you to automatically generate a ChatGPT response after taking a screenshot of a piece of text.

# Requirements

- Python 3.6+
- macOS 10.15+
- An OpenAI API key

# Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/nekumelon/SnapGPT.git
cd SnapGPT
pip3 install -r requirements.txt
```

Then, create a `.env` file with the following parameters:

```
OPENAI_API_KEY=<Ex: sk-xxxx>
HAS_GPT4=<Ex: True>
KEYBIND=<Ex: command+4>
```

# Usage

Run the `main.py` script with admin privileges to begin:

```bash
sudo python3 main.py
```

After that, you can use the provided keybind in the `.env` file to take a screenshot of a piece of text. The script will then automatically generate a response using ChatGPT and set it as your clipboard.
You can also click on the icon in the menu bar and select "Take Screenshot" to take a screenshot.
