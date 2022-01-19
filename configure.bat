python .\gen_path.py
powershell mkdir .\bin
powershell mkdir .\out
cd .\scripts
.\download-bin.bat
.\install-modules.bat
cd ..\
powershell New-Item ".\plan.txt" -ItemType File
