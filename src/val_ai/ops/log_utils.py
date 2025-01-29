import logging
import textwrap

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)-8s] %(module)s->%(funcName)s:%(lineno)d :: %(message)s',
                    # handlers=[logging.FileHandler("my_log.log", mode='w'),
                    #           logging.StreamHandler()]
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