django-projectgroup-settings-iterator
=====================================

usefull where all django projects are deployed in the same manner.
Iterates over django projects and run commands accordind command_settings
in each of the project. If exists. 

Allows to control periodic (cron) calls of commands through simple setting
file within each django project.

Example of settings file:
	
	HOURLY = {
	    'update_rsscontent': (),
	    'bodyPaint': ()
	}
	
	MONTHLY = {
	    'processRecurring': (2, ),
	}
	
Syntax:
python processor.py <desired part in conf file>

Example:
python processor.py HOURLY
	
this example will run all commands defined in HOURLY dictionary
from the example setting module, i.e update_rsscontent and bodyPaint. 
