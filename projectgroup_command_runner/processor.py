'''
Created on Jan 2, 2012

@author: vencax
'''
import os
import logging
import subprocess
from projectgroup_settings_iterator.settings import Settings


class CommandProcessor(Settings):

    settings_module_name = 'command_settings'

    def __init__(self, desired_config_part):
        self.desired_config_part = desired_config_part
        self.load_config()
        
    def process_specific_settings(self, cfgMod):
        logfile = getattr(cfgMod, 'COMMANDLOGFILE', None)
        level = logging._levelNames[getattr(cfgMod, 'LOGLEVEL', 'WARN')]
        logging.basicConfig(filename=logfile, level=level)

    def process_project_settins(self, proj_sett, proj_path):
        try:
            commandInfo = proj_sett[self.desired_config_part]
            for command, params in commandInfo.items():
                self.runCommand(command, params, proj_path)
        except Exception, e:
            logging.error(e)

    def runCommand(self, commandToRun, params, proj_path):
        """
        Process message as django app in given path.
        """
        python_binary = os.path.join(proj_path, self.path_to_python)
        manage = os.path.join(proj_path, self.path_to_manage, 'manage.py')
        toCall = [python_binary, manage, commandToRun, params]
        logging.debug('calling: %s' % toCall)
        self.call(toCall)

    def call(self, called):
        try:
            retval = subprocess.call(called)
            logging.debug('Retcode: %i' % retval)
        except Exception, e:
            logging.exception(e)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "one param at least"
        sys.exit(-1)
    CommandProcessor(sys.argv[2])
