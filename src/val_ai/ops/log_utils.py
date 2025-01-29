import sys
import logging
import textwrap

DEBUG_FILE = 'debug_ttg.log'
sys.stdout = open(DEBUG_FILE, 'a')
sys.stderr = open(DEBUG_FILE, 'a')

# file_handler = logging.FileHandler(filename='debug_ttg.log')
# stdout_handler = logging.StreamHandler(stream=sys.stdout)
# handlers = [file_handler, stdout_handler]

logging.basicConfig(level=logging.DEBUG, stream = sys.stdout,
                    format='[%(levelname)-8s] %(module)s->%(funcName)s:%(lineno)d :: %(message)s',
                    # handlers= handlers
                    )
logger = logging.getLogger("ttg")

def txt_banner(text,width=100,display=True,symbol="-"):
    text = text.upper()
    lines = textwrap.wrap(text,break_long_words=False, width = width)
    content = "\n".join( line.center(width) for line in lines )
    txt = ""
    txt +=symbol.center(width,symbol) + "\n"
    txt +=content + "\n"
    txt +=symbol.center(width,symbol) + "\n"
    if display:  print(txt)
    else: return txt