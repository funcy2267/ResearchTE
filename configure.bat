set ProjectPath=%cd%
powershell mkdir .\bin
powershell mkdir .\out
powershell mkdir .\plans
pip3 install -r .\requirements.txt
cd %tmp%
powershell curl https://github.com/jgm/pandoc/releases/download/2.14.1/pandoc-2.14.1-windows-x86_64.zip -o .\pandoc-2.14.1-windows-x86_64.zip
powershell tar -xf .\pandoc-2.14.1-windows-x86_64.zip pandoc-2.14.1/pandoc.exe
powershell mv .\pandoc-2.14.1\pandoc.exe %ProjectPath%\bin
powershell rm .\pandoc-2.14.1-windows-x86_64.zip
powershell rmdir -Recurse .\pandoc-2.14.1