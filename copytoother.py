import logging
import sys
import os
import shutil

logger = logging.getLogger()
# logger object

logger.setLevel(logging.INFO)
# setting level

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s',
                              '%m-%d-%Y %H:%M:%S')
# applying format to log file

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('copy.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


class CopyData:
    def __init__(self, folder, extensions, destFolder):
        self.folder = os.path.abspath(folder)
        self.extensions = extensions
        self.destFolder = os.path.abspath(destFolder)

    def selectiveCopy(self):
        try:
            msg = f"Looking in{self.folder} for files with extensions of{','.join(self.extensions)}"
            logger.info(msg)
            for foldername, subfolders, filenames in os.walk(self.folder):
                count = 0
                for filename in filenames:
                    name, extension = os.path.splitext(filename)
                    if extension in self.extensions:
                        fileAbsPath = foldername + os.path.sep + filename
                        msg1 = f" Copying {fileAbsPath} to {self.destFolder}"
                        logger.info(msg1)
                        # print('Coping', fileAbsPath, 'to', self.destFolder)
                        shutil.copy(fileAbsPath, self.destFolder)
                        count = count + 1
            msg3 = f"No of files are copied {count}"
            logger.info(msg3)

        except Exception as e:
            logger.exception(e)


c = CopyData('sourceFolder', ['.pdf', '.xlsx', 'docx'], 'selectiveFolder')
c.selectiveCopy()
