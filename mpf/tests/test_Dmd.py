from mpf.tests.MpfBcpTestCase import MpfBcpTestCase


class TestDmd(MpfBcpTestCase):

    def getConfigFile(self):
        return self._testMethodName + ".yaml"

    def getMachinePath(self):
        return 'tests/machine_files/dmd/'

    def testDmd(self):
        self.machine.dmds.test_dmd.update(b'12345')
        self.assertEqual(b'12345', self.machine.dmds.test_dmd.hw_device.data)

        self._bcp_client.receive_queue.put_nowait(("dmd_frame", {"name": "test_dmd", "rawbytes": b'1337'}))
        self.machine_run()

        self.assertEqual(b'1337', self.machine.dmds.test_dmd.hw_device.data)

    def testRgbDmd(self):
        self.machine.rgb_dmds.test_dmd.update(b'12345')
        self.assertEqual(b'12345', self.machine.rgb_dmds.test_dmd.hw_device.data)

        self._bcp_client.receive_queue.put_nowait(("rgb_dmd_frame", {"name": "test_dmd", "rawbytes": b'1337'}))
        self.machine_run()

        self.assertEqual(b'1337', self.machine.rgb_dmds.test_dmd.hw_device.data)
