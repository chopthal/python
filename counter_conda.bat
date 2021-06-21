set root=C:\Anaconda3
call %root%\Scripts\activate.bat %root%

call conda env list
call conda activate WebCellCounter
call cd C:\Projects\FlaskCC

call set FLASK_APP=counter
call set FLASK_ENV=development

cmd/k
