import sys
import subprocess
from pathlib import Path
import webbrowser as wb

target_file = "path placeholder"

def nirvanaEsterEgg():
    wb.open("https://open.spotify.com/artist/Nirvana")

def download_src_finder(file_path):
    path = Path(file_path).resolve()
    
    if not path.exists():
        return f"Error: '{path}' doesn't exist"

    # Windows
    if sys.platform == "win32":
        flow_path = path.with_name(f"{path.name}:Zone.Identifier")

        if flow_path.exists():
            content = flow_path.read_text(errors="ignore")

            for line in content.splitlines():

                if line.startswith("HostUrl="):
                    return line.split("HostUrl=", 1)[1]
                
            return "file downloaded - HostUrl not reached" 
        
        else:
            return "no download infos found - the file could be created locally"

    # MacOS
    elif sys.platform == "darwin":
        try:
            result = subprocess.run(
                ["xattr", "-p", "com.apple.metadata:kMDItemWhereFroms", str(path)],
                capture_output=True, text=True, check=True
            )

            return result.stdout.strip()
        except subprocess.CalledProcessError:
            return "no download infos found"

    # Linux
    else:
        try:
            
            result = subprocess.run(
                ["getfattr", "--only-values", "-n", "user.xdg.origin.url", str(path)],
                capture_output=True, text=True, check=True
            )

            return result.stdout.strip()
        
        except subprocess.CalledProcessError:
            return "no download infos found"

if __name__ == "__main__":
    source_url = download_src_finder(target_file)
    print(f"download origin: {source_url}")
