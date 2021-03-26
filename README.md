### Steps to create client application with PYQT & QT_Designer

#### 1) Create ui file with QT_Designer

#### 2) Install PYQT from https://riverbankcomputing.com/software/pyqt/download

`pip install PyQt5` or `pip install PyQt6`

#### 3) Can use pyuic6 or (pyuic5) file.ui

##### this command compile ui file to python file on command board

`pyuic5 clientUI.ui`

#### 4) Can use pyuic6 or (pyuic5) file.ui -o pythonFile.py

##### this command compile iu file to python file and set logout to file

`pyuic5 clientUI.ui -o clientUI.py`

#### 5) Create python file: messenger.py

##### this file import clientUI.py main object(app UI)
