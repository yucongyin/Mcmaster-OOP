#Mac Id: yiny29
#student number: 001335114
#requirement: The walk signal for pedestrians must only allow crossing when the trac light in the same direction is green.
#The two conditional statements are parallel to ensure that both sides' pedestrian signal is tested 

from Assignment5.stubs_assignment5 import TrafficLightSystem


def test_passes():
    light = TrafficLightSystem()#an instance of the traffic lights is created with initial values, a traffic light consist of a light on main road, a light on side road and each direction has a pedestrian signal 
    light.runTraffic(light.mainRoadLight,light.sideRoadLight)
    if light.mainRoadLight.pedestrianSignal == 'green':
        assert light.mainRoadLight == 'green',"The traffic light must be green to allow the same direction pedestrian to cross"
    if light.sideRoadLight.pedestrianSignal == 'green':
        assert light.sideRoadLight =='green',"The traffic light must be green to allow the same direction pedestrian to cross"