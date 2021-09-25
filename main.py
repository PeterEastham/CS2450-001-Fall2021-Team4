import sys

from service.file_helper import FileHelper
from view.login_page import main as main
"""
We'll use this as an entry point.
Maybe we use this to figure out the target directory so the
user can run from anywhere?

Something like args[0].split("/")[:-1].join("/")
and pass that to well... another controller XD
File_Path_Controller.start_controller(pathStr)

def start_controller(baseString = "."):
    #singleton
"""

if __name__ == "__main__":
    FileHelper.start_helper(sys.argv[0][:-7])
    main()
