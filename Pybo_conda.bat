set root=C:\Anaconda3
call %root%\Scripts\activate.bat %root%

call conda env list
call conda activate WebCellCounter
call cd C:\Projects\FlaskWeb

call set FLASK_APP=pybo
call set FLASK_ENV=development

cmd/k
