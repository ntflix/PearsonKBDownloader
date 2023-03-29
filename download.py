import os
import threading

URLS_FILE = "pearson_knowledge_base.txt"  # each article on newline

OUTPUT_DIR = "/Users/uwebefe/Downloads/knowledgebase"  # e.g. /Users/felix/Downloads/knowledgebase

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

urls: list[str] = [x.replace("\n", "") for x in open(URLS_FILE).readlines()]

for url in urls:
    escapedChromePath = CHROME_PATH.replace(" ", "\\ ")
    command = (
        f"""{escapedChromePath} --headless --virtual-time-budget=50000 --timeout=50000 """
        """--run-all-compositor-stages-before-draw --disable-gpu """
        """--user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36\" """
        f"""--dump-dom '{url}' > '{OUTPUT_DIR}/{url.replace('/', '-')}.html' &"""
    )
    # print(command)
    # os.system(command)
    t = threading.Thread(target=os.system, args=[command])
    t.start()
