#Mac Id: yiny29
#student number: 001335114
#requirement: When one traffic light is green the other must always be red
#why test necessary: The point of this test is to make sure the two lights are never the same to ensure no traffic conflict and collision. The test is sufficient because it focuses on the status of the lights
# and its simple enough to test the output 

from Assignment5.stubs_assignment5 import TrafficLightSystem


def test_passes():
    light = TrafficLightSystem()#an instance of the traffic lights is created with initial values, a traffic light consist of a light on main road, a light on side road and each direction has a pedestrian signal 
    light.runTraffic()
    if light.mainRoadLight == 'red':
        assert light.sideRoadLight == 'green',"When one traffic light is green the other must always be red"
    elif light.sideRoadLight == 'red':
        assert light.mainRoadLight =='green',"When one traffic light is green the other must always be red"