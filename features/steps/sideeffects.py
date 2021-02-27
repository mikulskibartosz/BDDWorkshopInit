from behave import *
from unittest.mock import MagicMock


class SecurityCameras:
    def count_people_in_the_building(self):
        pass


class PowerOutlet():
    def shut_off(self):
        pass

    def device(self):
        return "whatever" #MagicMock(return_value="bla bla")


class DoorLock:
    def __init__(self, notification_listeners):
        self.notification_listeners = notification_listeners

    def lock(self):
        for listener in self.notification_listeners:
            listener.notify_door_locked()


class SmartHome:
    def __init__(self, cameras, power_outlets):
        self.cameras = cameras
        self.power_outlets = power_outlets

    def notify_door_locked(self):
        if self.cameras.count_people_in_the_building() == 0:
            for power_outlet in self.power_outlets:
                if power_outlet.device() != 'fridge':
                    power_outlet.shut_off()


@given(u'3 power outlets')
def step_impl(context):
    context.generic_power_outlets = []

    for _ in range(3):
        power_outlet = PowerOutlet()
        power_outlet.shut_off = MagicMock()
        context.generic_power_outlets.append(power_outlet)


@given(u'one power outlet powering a fridge')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given one power outlet powering a fridge')


@given(u'there are no people in the building')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given there are no people in the building')


@when(u'the door is locked')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the door is locked')


@then(u'shut off all power outlets')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then shut off all power outlets')


@then(u'keep the fridge running')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then keep the fridge running')
