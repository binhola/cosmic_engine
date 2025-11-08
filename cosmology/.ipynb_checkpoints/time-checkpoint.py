from constants.units import CosmicUnits
from scipy.integrate import quad
import numpy as np

class CosmicTime:
    def __init__(self, universe):
        self.uni = universe

    def age_of_universe(self, z=0, unit='gyr'):
        """Age of universe at redshift z"""
        def integrand(z_prime):
            return 1 / ((1 + z_prime) * self.uni.H(z_prime))
        
        # H in s⁻¹ for proper unit conversion
        H0_si = self.uni.H0 * 1000 / CosmicUnits.MPC_TO_M
        result, _ = quad(integrand, z, np.inf)
        age_sec = result / H0_si
        
        if unit.lower() == 'gyr':
            return CosmicUnits.sec_to_gyr(age_sec)
        elif unit.lower() == 'sec':
            return age_sec
        else:
            raise ValueError("Unit must be 'gyr' or 'sec'")