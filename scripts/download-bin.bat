set /p ProjectPath=<..\ProjectPath.txt
cd %tmp%
powershell curl https://github.com/htacg/tidy-html5/releases/download/5.8.0/tidy-5.8.0-win64.zip -o .\tidy-5.8.0-win64.zip
powershell tar -xf .\tidy-5.8.0-win64.zip tidy-5.8.0-win64/bin/tidy.exe
powershell mv .\tidy-5.8.0-win64\bin\tidy.exe %ProjectPath%\bin
powershell rm .\tidy-5.8.0-win64.zip
powershell rmdir -Recurse .\tidy-5.8.0-win64

powershell curl https://github.com/jgm/pandoc/releases/download/2.14.1/pandoc-2.14.1-windows-x86_64.zip -o .\pandoc-2.14.1-windows-x86_64.zip
powershell tar -xf .\pandoc-2.14.1-windows-x86_64.zip pandoc-2.14.1/pandoc.exe
powershell mv .\pandoc-2.14.1\pandoc.exe %ProjectPath%\bin
powershell rm .\pandoc-2.14.1-windows-x86_64.zip
powershell rmdir -Recurse .\pandoc-2.14.1