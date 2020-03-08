import os
import random

icon_num = random.randint(1, 4)

__FILE_DIR__ = os.path.dirname(__file__).replace('\\', '/')

__CLASSIFIER_1__ = os.path.join(__FILE_DIR__, 'classifier/digit_clf1.pkl').replace('\\', '/')
__CLASSIFIER_2__ = os.path.join(__FILE_DIR__, 'classifier/digit_clf2.pkl').replace('\\', '/')
__SCALER__ = os.path.join(__FILE_DIR__, 'classifier/scaler.pkl').replace('\\', '/')

__ICON__ = os.path.join(__FILE_DIR__, 'img_png/icons/icon_'+str(icon_num)+'.png').replace('\\', '/')