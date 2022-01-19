# Requirements
- Python 3.x
- Windows PowerShell
# Usage
Before you do anything, run **configure.bat**.  
Edit **plan.txt** for your needs, and run **main.py** to generate a docx document (./out/output.docx).
# Examples
For **plan.txt**:  
`lang_code,pl-PL` - Set search language to polish,  
`1,"bios definicja"` - Search Google for 'bios definicja',  
`2,"płyta główna"` - Search DuckDuckGo for 'płyta główna',  
`3,"ramdac",3` - Search DuckDuckGo for 3 images,  
`4,"pamięć ram",2` - Search Wikipedia for 2 paragraphs about 'pamięć ram'.
