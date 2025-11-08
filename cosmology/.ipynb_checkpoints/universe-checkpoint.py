from constants.units import CosmicUnits
from constants.physical import PhysicalConstants

class Universe:
    """Main Universe class holding cosmological parameters"""
    
    def __init__(self, H0=67.4, Omega_m=0.315, Omega_Lambda=0.685, Omega_rad=9.2e-5):
        # Instance attributes - each universe can have different parameters
        self.H0 = H0  # km/s/Mpc
        self.Omega_m = Omega_m
        self.Omega_Lambda = Omega_Lambda
        self.Omega_rad = Omega_rad
        self.Omega_k = 1 - (Omega_m + Omega_Lambda + Omega_rad)
        self.H0_si = CosmicUnits.km_to_mpc(H0)

        # Import calculators
        from cosmology.distances import DistanceCalculator
        from cosmology.time import CosmicTime
        
        self.distances = DistanceCalculator(self)
        self.time = CosmicTime(self)
    
    # Instance method - needs self to access H0, Omega_m, etc.
    def H(self, z):
        """Hubble parameter at redshift z - needs instance data"""
        a = self.z_to_a(z)
        return self.H0 * ((self.Omega_rad / a**4 + self.Omega_m / a**3 + 
                         self.Omega_k / a**2 + self.Omega_Lambda)**0.5)
    
    # Static method - pure function, no instance/class data needed
    @staticmethod
    def z_to_a(z):
        return 1 / (1 + z)
    
    @staticmethod
    def a_to_z(a):
        return 1 / a - 1