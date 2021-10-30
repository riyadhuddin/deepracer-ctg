def reward_function(params):

    center_variance = params["distance_from_center"] / params["track_width"]

    left_lane = [20,24,25,26,30,80,82,83,84,100, 104, 110, 152,153,154,264,265,266,270,274]#Fill in the waypoints
    
    center_lane = [1,2,6,10, 16, 33,34,39,40, 58, 70,76,88,90,92,94,95,97,111,112,113,114,118,119,120,121,128,129,136,137,138,140,142,144,146, 155, 158,162,166,172,182,197,198,199,200,201,202,205,207,209,212,213,214,215,216,219,220,225,226,230,234,235,236,237,256,257,258,259,260,261,263]#Fill in the waypoints
    
    right_lane = [116,116,117,123,124,125,126,127,168,170,175,179,183,187,190,195]#Fill in the waypoints
    
    fast = [1,2,10,16,40,50,60,70,75,240,250,264,270,272]#Fill in the waypoints
    slow = [17,18,19,20,26,27,35,36,37,38,77,79,80,83,85,87,96,97,98,108,112,115,120,129,142,145,149,159,160,161,162,164,165,167,200,205,210,215,219,220,222,223,224,226,230,234,238,259,261,262,263]#Fill in the waypoints
    
    reward = 21

    if params["all_wheels_on_track"]:
        reward += 10
    else:
        reward -= 10

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10
    if params["closest_waypoints"][1] in fast:
        if params["speed"] == 2 :
            reward += 10
        else:
            reward -= 10
    elif params["closest_waypoints"][1] in slow:
        if params["speed"] == 1 :
            reward += 10
        else:
            reward -= 10
        
    
    return float(reward)