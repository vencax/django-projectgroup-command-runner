'''
Created on May 9, 2012

@author: vencax
'''

import unittest
from projectgroup_settings_iterator.tests import DjangoProjectRootTestCase
from projectgroup_command_runner.processor import CommandProcessor
import os


class TestingCommandProcessor(CommandProcessor):
    def __init__(self, desired_config_part):
        self.runqueue = []
        CommandProcessor.__init__(self, desired_config_part)

    def call(self, called):
        self.runqueue.append(called)


class TestSetting(DjangoProjectRootTestCase):

    testDomains = ('example1.com', 'example2.com')
    settings_module_name = 'command_settings'
    settings_template = '''
HOURLY = {
    'update_rsscontent': (),
    'bodyPaint': ()
}

MONTHLY = {
    'processRecurring': (2, ),
}
# %s
    '''

    def test_all(self):
        cp = TestingCommandProcessor('HOURLY')

        desiredCalled = self._createDesired((
            ('update_rsscontent', ()),
            ('bodyPaint', ())
        ))
        assert sorted(desiredCalled) == sorted(cp.runqueue), \
            'expected:\n%s\nactual:\n%s' % (desiredCalled,
                                            self.server.runqueue)

        cp = TestingCommandProcessor('MONTHLY')

        desiredCalled = self._createDesired((
            ('processRecurring', (2, )),
        ))
        assert sorted(desiredCalled) == sorted(cp.runqueue), \
            'expected:\n%s\nactual:\n%s' % (desiredCalled,
                                            self.server.runqueue)

    def _createDesired(self, commands):
        desiredCalled = []
        for d in self.testDomains:
            pyth = os.path.join(self.projects_root, d, self.path_to_python)
            manage = os.path.join(self.projects_root, d,
                                  self.path_to_manage, 'manage.py')

            for comm, pars in commands:
                desiredCalled.append([pyth, manage, comm, pars])

        return desiredCalled

if __name__ == '__main__':
    unittest.main()
