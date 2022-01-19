import os
import io

with io.open(".\\ProjectPath.txt", "w", encoding="utf-8") as file:
    file.write(os.getcwd())
    file.close()
