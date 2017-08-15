import unittest

from snapstack import Plan, Setup, Step

class SnapstackTest(unittest.TestCase):

    def test_snapstack(self):
        '''
        _test_snapstack_

        Run a basic smoke test, utilizing our snapstack testing harness.

        '''
        cinder = Step(
            snap='cinder',
            script_loc='./tests/',
            scripts=['cinder.sh'],
            files=[
                'etc/snap-cinder/cinder/cinder/cinder.conf.d/database.conf',
                'etc/snap-cinder/cinder/cinder/cinder.conf.d/keystone.conf',
                'etc/snap-cinder/cinder/cinder/cinder.conf.d/lvm.conf',
                'etc/snap-cinder/cinder/cinder/cinder.conf.d/rabbitmq.conf',
                'etc/snap-cinder/tgt/conf.d/cinder_tgt.conf'
            ],
            snap_store=False)

        plan = Plan(tests=[cinder])
        plan.run()
