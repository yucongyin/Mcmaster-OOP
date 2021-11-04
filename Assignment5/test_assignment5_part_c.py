#Mac Id: yiny29
#student number: 001335114
#requirement: The trac light should be green for the main road unless trac has been waiting on the side street for more than
#90s, in which case it should be red and the side street light green until 30s after all trac on the side street has
#cleared.
#The test is necessary because it is required for the side road traffic to travel as well, but has a lower priority than the main road. The test is sufficient because I provided the top level condition
#as well as the lower level condition to make sure both the input and output is accurate


from stubs_assignment5 import TrafficLightSystem

def test_passes():
    light = TrafficLightSystem()#an instance of the traffic lights is created with initial values, a traffic light consist of a light on main road, a light on side road and each direction has a pedestrian signal 
    light.runTraffic(light.mainRoadLight,light.sideRoadLight)
    if light.sideRoadLight.trafficCensor()== true:#The top level condition is the cencor of side road which means there are traffic waiting on side road
        if light.sideRoadLight.censorTimer() < 90:#if they have waited for less than 90, traffic light on main road stays green
            assert light.mainRoadLight.lightColor == 'green',"The traffic waiting on side road has waited less than 90s"
        else:
            assert light.mainRoadLight.lightColor == 'red',"The trac light should be green for the main road unless trac has been waiting on the side street for more than 90s"
            if light.sideRoadLight.trafficCensor == false:
                light.sideRoadLight.setlightTimer(30)
                while light.sideRoadLight.lightTimer > 1:
                    assert light.sideRoadLight.lightColor == 'green',"the side street light green until 30s after all trac on the side street has cleared"
                    light.sideRoadLight.lightTimer =- 1
                #end while
                assert light.sideRoadLight.lightColor == 'red',"the side street light has been green more than 30s after waiting traffic cleared"
            else:
                light.sideRoadLight.lightColor == 'green',"Traffic on side road hasn't cleared yet"
    else:
        assert light.mainRoadLight.lightColor == 'green',"No traffic on the side road waiting"
