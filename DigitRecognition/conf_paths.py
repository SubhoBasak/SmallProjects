import os
import random

icon_num = random.randint(1, 4)

__FILE_DIR__ = os.path.dirname(__file__).replace('\\', '/')

__CLASSIFIER__ = os.path.join(__FILE_DIR__, 'classifier/forest_clf.pkl').replace('\\', '/')

__ICON__ = os.path.join(__FILE_DIR__, 'img_png/icons/icon_'+str(icon_num)+'.png').replace('\\', '/')
