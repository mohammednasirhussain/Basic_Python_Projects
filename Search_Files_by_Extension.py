from pathlib import Path 
path = Path(r"c:\\Users\\mmaistry\\OneDrive - CoreLogic Solutions, LLC\\Documents\\") 
files = list(path.rglob("*.py")) 
print(files)
