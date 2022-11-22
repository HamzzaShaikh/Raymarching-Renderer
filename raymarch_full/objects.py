import numpy as np
from utils import normalize, proj

class Material:
    def __init__(self, ambient, diffuse, spectral, spectral_p):
        self.ambient = np.array(ambient)
        self.diffuse = np.array(diffuse)
        self.spectral = np.array(spectral)
        self.spectral_p = spectral_p
        
    def get_ambient_coef(self):
        return self.ambient
    
    def get_diffuse_coef(self):
        return self.diffuse
    
    def get_spectral_coef(self):
        return self.spectral
    
    def get_spectral_p_coef(self):
        return self.spectral_p

class Sphere:
    def __init__(self, position, radius, material):
        self.position = position
        self.radius = radius
        self.material = material
        
    def get_distance(self, location):
        return np.linalg.norm(location-self.position) - self.radius
    
    def get_surface_normal(self, location):
         return normalize(location-self.position)
     
class Plane:
    def __init__(self, position, normal, material):
        self.position = position
        self.normal = normalize(normal)
        self.material = material
        
    def get_distance(self, location):
        return np.linalg.norm(proj((location - self.position), self.normal))
    
    def get_surface_normal(self, location):
        return self.normal