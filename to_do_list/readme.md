To run the app you will need to have python 3.4 interpreter, pip and virtualenv (optional, but advised) installed.

If you want to work on virtualenv then run following commands in shell:
>>> mkvirtualenv planner
>>> workon planner


In order to run the app you first need to install needed modules (Django).
>>> pip install requirements.txt

Now go to the main project directory (the one containing file 'manage.py') and run in shell:
>>> python manage.py runserver 
or if you want to set port number to a specific value:
>>> python manage.py runserver <port_number>

To use app go to 127.0.0.1:<port_number> in your browser.
