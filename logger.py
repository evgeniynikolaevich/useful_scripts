import logging
import sys
import os
file_name = os.path.splitext("/path/to/some/file.txt")[0]

logging.basicConfig(filename = "reports_{}.log".format(filename),level = logging.DEBUG,format='%(asctime)s %(message)s')
logging.info("this info")
logging.warning("this warning")
logging.debug("this debug")

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)
#this is
print = logging.info
