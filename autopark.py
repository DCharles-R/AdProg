import numpy as np

class ProximitySensor:

    def __init__(self, distance, max_dist, min_dist, pos_x, pos_y):
        self.distance = distance
        self.max_dist = max_dist
        self.min_dist = min_dist
        self.pos_x = pos_x
        self.pos_y = pos_y

class Camera:

    def __init__(self, resolution, width, height, camera_port):
        self.resolution = resolution
        self.width = width
        self.heigh = height
        self.comm_port = camera_port

class Motor:

    def __init__(self, rpm_velocity, activity, max_velocity, min_velocity):
        self.rpm_velocity = rpm_velocity
        self.activity = activity
        self.max_velocity = max_velocity
        self.min_velocity = min_velocity

class Surroundings:

    def __init__(self, location):
        self.location = location

class Vehicle:

    def __init__(self, length, width, lin_velocity, pos_x, pos_y, angle, side_dist):
        self.length = length
        self.width = width
        self.lin_velocity = lin_velocity
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle_rad = np.radians(angle)
        c, s = np.cos(self.angle_rad), np.sin(self.angle_rad)
        self.rot_mat = np.array((c, -s),(s, c))
        self.front_left_corner = np.matmul(self.rot_mat, np.array(pos_x + length / 2, pos_y + width / 2))
        self.front_right_corner = np.matmul(self.rot_mat,np.array(pos_x + length / 2, pos_y - width / 2))
        self.rear_left_corner = np.matmul(self.rot_mat,np.array(pos_x - length / 2, pos_y + width / 2))
        self.rear_right_corner = np.matmul(self.rot_mat,np.array(pos_x - length / 2, pos_y - width / 2))
        self.absolute_pos = [self.front_left_corner, self.front_right_corner, self.rear_left_corner, self.rear_right_corner]
        self.front_right_sensor_pos = np.matmul(self.rot_mat, np.array(pos_x + length / 4, pos_y - width / 2))
        self.rear_right_sensor_pos = np.matmul(self.rot_mat, np.array(pos_x - length / 4, pos_y - width / 2))
        self.front_sensor = ProximitySensor(side_dist, max_dist=0.5, min_dist=0.2, pos_x=self.front_right_sensor_pos[0], pos_y=self.front_right_sensor_pos[1])
        self.rear_sensor = ProximitySensor(side_dist, max_dist=0.5, min_dist=0.2, pos_x=self.rear_right_sensor_pos[0], pos_y=self.rear_right_sensor_pos[1])