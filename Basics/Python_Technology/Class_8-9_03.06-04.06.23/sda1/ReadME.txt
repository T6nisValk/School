cmd >> python -m compileall -b "filename.py" 
 >> compiles the python file to .pyc

cmd >> uncompyle6 "filename.pyc" > "newfilename.py"
 >> uncompiles the .pyc file to readable .py