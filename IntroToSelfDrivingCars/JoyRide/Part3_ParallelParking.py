# Before running any code changes make sure to click the button "Restart Connection" above first.
# Also make sure to click Reset in the simulator to refresh the connection.
# After making any code changes, make sure to click the button "Restart Connection" above first. Then re-run your code cell (Ctrl+Enter).
# You need to wait for the Kernel Ready message.

car_parameters = {"throttle": 0, "steer": 0, "brake": 0}

def control(pos_x, pos_y, time, velocity):
    """ Controls the simulated car"""
    global car_parameters
    
    
    # TODO: Use WASD keys in simulator to gain an intuitive feel of parallel parking.
    # Pay close attention to the time, position, and velocity in the simulator.
    
    # TODO: Use this information to make decisions about how to set your car parameters
    
    # In this example the car will drive forward for three seconds
    # and then backs up until its pos_y is less than 32 then comes to a stop by braking
    if time < 2:
        # 1. Step: Drive forward
        car_parameters['throttle'] = 1
    else:
        # 2. Step: Drive backward
        car_parameters['throttle'] = -1
        if pos_y < 32:
            # 6. Step: Come to stop
            car_parameters['steer'] = 0
            car_parameters['brake'] = 1              
        elif pos_y < 35: 
            # 5. Step: Steer left
            car_parameters['steer'] = -25
        elif pos_y < 37: 
            # 4. Step: Steer straight
            car_parameters['steer'] = 0
        elif pos_y < 41:
            # 3. Step: Steer right
            car_parameters['steer'] = 25
    return car_parameters
    
import src.simulate as sim
sim.run(control)
