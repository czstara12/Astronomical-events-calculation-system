from dataGateWay import *
from model import *

cof = CelestialObjectForm()
cof.show_all_objects()
cof.add_object()
cof.show_all_objects()

aef = AstronomicalEventForm()
aef.show_all_events()
aef.add_event()
aef.show_all_events()

aof = AstronomicalObservationForm()
aof.show_all_observation()
aof.add_observation(id=None, observation_date='2023-12-08', location='太空观测站',)
aof.add_observation()
aof.show_all_observation()
