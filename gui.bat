
:start
cls

python -m venv venv
call "venv\scripts\activate"
call pip install -r requirements.txt
call playwright install 
python gui.py


pause
exit
