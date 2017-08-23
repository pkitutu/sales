# About the app - Sales App
The Sales App is an application to help track sales for different products that also tracked by the system. 
It is developed using Django, a python framework based on the Model-View-Controller (MVC)architecture complete with unit tests

## Libraries used

### Front end (JavaScript/CSS)

* tisa-admin
* bootstrap
* datatables
* jquery

### Back end (Python)

* Django
* bootstrap
* djangorestframework

## How to set up
### Pre-requisites

* python2.7 //minimum requirement
* mysql-server
* nginx //web server for production
* browser

### Initial setup

* $ cd sales
* $ pip install -r requirements.txt // install dependent libraries
* $ cd sales
* $ cp local_settings.example.py local_settings.py // edit this to input your database connection options
* $ python manage.py migrate
* $ python manage.py createsuperuser // create a super user inputting the necessary details
* $ python manage.py loaddata testdata.json


### Run tests
* $ python manage.py test // 2 tests should return OK

### Launch app in dev mode
* $ python manage.py runserver
Go to the browser and launch app via http://localhost:8000 and login
Access system administration page via http://localhost:8000/admin 

### Production mode on Linux (Ubuntu) with nginx

* $ sudo pip install virtualenv virtualenvwrapper
* $ echo "export WORKON_HOME=~/Env" >> ~/.bashrc
* $ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc


* $ source ~/.bashrc

* $ mkvirtualenv sales #Creates VM and activates it;; use deactivate to get out and workon vl_vm to go back on

* $ git clone git@github.com:pkitutu/sales.git

* $ cd sales/sales/

* $ pip install -r requirements.txt
* $ python manage.py collectstatic

* $ sudo pip install uwsgi
* $ sudo apt-get install nginx

* $ sudo mkdir -p /etc/uwsgi/sites
* $ cd /etc/uwsgi/sites

* #Create the config files, be sure to replace user with your user name
* $ sudo vi sales.ini

		[uwsgi]
		project = sales
		base = /home/user

		chdir = %(base)/%(project)
		home = %(base)/Env/%(project)
		module = %(project).wsgi:application

		master = true
		processes = 5
		buffer-size = 65535

		socket = %(base)/%(project)/%(project).sock
		chmod-socket = 664
		vacuum = true

* $ sudo vi /etc/init/uwsgi.conf

		description "uWSGI application server in Emperor mode"

		start on runlevel [2345]
		stop on runlevel [!2345]

		setuid user
		setgid www-data

		exec /usr/local/bin/uwsgi --emperor /etc/uwsgi/sites



* $ sudo vi /etc/nginx/sites-available/sales

		server {
		    listen 80;

		    location = /favicon.ico { access_log off; log_not_found off; }
		    location /static/ {
		        root /home/user/sales;
		    }

		    location / {
		        include         uwsgi_params;
		        uwsgi_pass      unix:/home/user/sales/sales.sock;
		    }
		}


* $ sudo ln -s /etc/nginx/sites-available/sales /etc/nginx/sites-enabled

* $ sudo service nginx configtest
* $ sudo service nginx restart
* $ sudo service uwsgi start

* #Acess on the ip and port provided in the browser

## Access the latest
git clone git@github.com:pkitutu/sales.git