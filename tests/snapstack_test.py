import unittest

from snapstack import Plan, Setup, Step

class SnapstackTest(unittest.TestCase):

    def test_snapstack(self):
        '''
        _test_snapstack_

        Run a basic smoke test, utilizing our snapstack testing harness.

        '''
        # snapstack already installs cinder. Override the 'cinder'
        # step with a locally built snap. neutron, nova, etc. will still
        # be installed as normal from the store.
        setup = Setup()
        setup.add_steps(('cinder', Step(
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
            snap_store=False)))

        # Execute the snapstack tests
        plan = Plan(base_setup=setup.steps())
        plan.run()
