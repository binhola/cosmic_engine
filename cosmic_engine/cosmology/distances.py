# cosmology/distances.py
from cosmic_engine.constants.units import CosmicUnits
from cosmic_engine.constants.physical import PhysicalConstants
import numpy as np
from scipy.integrate import quad

class DistanceCalculator:
    """Handle all distance calculations"""
    
    def __init__(self, universe):
        self.universe = universe  # Reference to parent universe

    def hubble_law(self, distance_mpc):
        return self.universe.H0 * distance_mpc
    
    def comoving_distance(self, z, unit='mpc'):
        def integrand(z_prime):
            return PhysicalConstants.c / self.universe.H(z_prime)
        
        result, _ = quad(integrand, 0, z)

        if unit.lower() == 'mpc':
            return result
        elif unit.lower() == 'km':
            return CosmicUnits.MPC_TO_KM(result)
        else:
            raise ValueError("Unit must be 'mpc' or 'km'")
    
    def angular_distance(self, z, unit='mpc'):
        """Angular diameter distance (Mpc)"""
        d_c = self.comoving_distance(z, unit='mpc')
        result = d_c / (1 + z)
        
        if unit.lower() == 'mpc':
            return result
        elif unit.lower() == 'km':
            return CosmicUnits.mpc_to_km(result)
        else:
            raise ValueError("Unit must be 'mpc' or 'km'")