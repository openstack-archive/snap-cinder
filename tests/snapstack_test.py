import unittest

from snapstack import Plan, Setup, Step

class SnapstackTest(unittest.TestCase):

    def __init__(self):
        self.cinder = Step(
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

        self.cinder_cleanup = Step(
            script_loc='./tests/',
            scripts=['cinder_cleanup.sh'])

        self.plan = Plan(tests=[self.cinder],
                         test_cleanup=[self.cinder_cleanup])

    def test_snapstack(self):
        '''Deploy, run base smoke test, then cleanup and destroy

        Deploys the base OpenStack with cinder built and deployed from
        this snap, utilizing snapstack testing harness. Deployment is
        cleaned up and destroyed after all configuration/test scripts
        are run.
        '''
        self.plan.run()

    def deploy(self):
        '''Deploy and run basic smoke tests

        Deploys the base OpenStack with cinder built and deployed from
        this snap, utilizing snapstack testing harness. Deployment is
        left up after configuration/test scripts are run.
        '''
        self.plan.deploy()

    def destroy(self):
        '''Cleanup and destroy base smoke test deployment

        Cleans up and destroys the deployed OpenStack environment.
        '''
        self.plan.destroy()
