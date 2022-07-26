import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AfGF5zGEyPOsdmScYe7OT7kl6RSU4E2sEL35kAtTJ4yGjVlRFmC8kmv3d8EbX1rikmJacZuJ5T28VnpE"
        self.client_secret = "EED0xgqLyFoR62vUXx7aCRTcRKqcFC2iN1L0ge4rT3oSk_u4Yd6ZEYLGqtmVnGIBAgM0Qsb2QwtWILnR"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
