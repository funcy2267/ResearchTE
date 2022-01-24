# About
**ResearchTE** automates researching by generating document with answers to given questions.\
Supports getting results from:
- Google
- DuckDuckGo (with images)
- Wikipedia
# Requirements
- Python3
- Windows PowerShell
# Configuration
Run `configure.bat` to configure requirements.
# Usage
Create a text file in *plans/* directory with your document plan.\
Run `main.py` and enter name of this file.
## Creating plan
Example:
- `lang_code;en-US` - Set **search language** to **English**
- `ggl;BIOS definition` - Search **Google** for "**BIOS definition**"
- `ddg;Mainboard` - Search **DuckDuckGo** for "**Mainboard**"
- `ddgimg;Sunflower;3` - Search **DuckDuckGo** for **3 images** with "**Sunflower**"
- `wiki;European Union;2` - Search **Wikipedia** for **2 paragraphs** about "**European Union**"
