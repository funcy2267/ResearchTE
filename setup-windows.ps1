$ProjectPath = Get-Location
mkdir bin
mkdir output
mkdir plans
$TempDir = [System.IO.Path]::GetTempPath()
cd $TempDir
curl https://github.com/jgm/pandoc/releases/download/2.14.1/pandoc-2.14.1-windows-x86_64.zip -o .\pandoc-2.14.1-windows-x86_64.zip
tar -xf .\pandoc-2.14.1-windows-x86_64.zip pandoc-2.14.1/pandoc.exe
mv .\pandoc-2.14.1\pandoc.exe $ProjectPath\bin
rm .\pandoc-2.14.1-windows-x86_64.zip
rmdir -Recurse .\pandoc-2.14.1
