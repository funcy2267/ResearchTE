# About
`ResearchTE` automates researching by generating document with answers to given questions.\
Supports getting results from:
- Google
- DuckDuckGo (with images)
- Wikipedia
# Requirements
- Python 3
# Configuration
### Linux
Install dependencies (Debian):
```
sudo apt update && sudo apt install -y python3 python3-pip pandoc
```
Install required Python modules:
```
pip3 install -r ./requirements.txt
```
Create directories:
```
mkdir output && mkdir plans
```
### Windows
Install Python 3:
```
winget install --id=Python.Python.3 -e
```
Install required Python modules:
```
pip3 install -r .\requirements.txt
```
Run `.\setup-windows.ps1`.
# Usage
Create a text file in `plans` directory with your research plan.\
Run `main.py` and enter name of this file. Word document + markdown file will be saved in `output` folder.
## Creating plan
Example:
- `lang_code;en-US` - Set **search language** to **English**
- `ggl;BIOS definition` - Search **Google** for "**BIOS definition**"
- `ddg;Mainboard` - Search **DuckDuckGo** for "**Mainboard**"
- `ddgimg;Sunflower;3` - Search **DuckDuckGo** for **3 images** with "**Sunflower**"
- `wiki;European Union;2` - Search **Wikipedia** for **2 paragraphs** about "**European Union**"
