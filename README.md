#Setup Guide

##Prerequisites

1. virtualenv
1. virtualenvwrapper

##Install procedure

1. Clone repo into project directory

		$ cd ~/work
		$ git clone git@github.com:edgecaselabs/pyUpCheck.git
		$ cd ~/work/pyUpCheck

1. Make virtual env
	
		$ mkvirtualenv pyUpCheck
		$ workon pyUpCheck
		

1. Install	requirements

		$ pip install -r requirements.txt
	
1. Start flask server

		$ cd ~/work/pyUpCheck/webapp
		$ python run.py
		
1. Browse website at [http://localhost:5000](http://localhost:5000)

