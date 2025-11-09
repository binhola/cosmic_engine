from .units import CosmicUnits

class PhysicalConstants:
    """Fundamental physical constants"""
    
    c = 2.99792458e5  # km/s
    G = 6.67430e-11   # m³/kg/s²
    h = 6.62607015e-34  # J·s (Planck constant)
    k_B = 1.380649e-23  # J/K (Boltzmann constant)
    sigma_T = 6.6524587321e-29  # m² (Thomson cross-section)
    
    @classmethod
    def critical_density_H0(cls, H0):
        """Calculate critical density for given H0"""
        H0_si = H0 * 1000 / CosmicUnits.MPC_TO_M  # Convert to s⁻¹
        return 3 * H0_si**2 / (8 * 3.1415926535 * cls.G)