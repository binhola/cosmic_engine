class CosmicUnits:
    """Handle unit conversions for cosmology"""
    # Distance conversions
    MPC_TO_KM = 3.08567758128e19
    MPC_TO_M = 3.08567758128e22
    KM_TO_MPC = 1 / MPC_TO_KM
    
    # Time conversions
    YEAR_TO_SEC = 365.25 * 24 * 3600
    GYR_TO_SEC = 1e9 * YEAR_TO_SEC
    
    # Energy and mass
    MSUN_TO_KG = 1.989e30
    
    # Class methods for conversions
    @classmethod
    def mpc_to_km(cls, distance_mpc):
        return distance_mpc * cls.MPC_TO_KM
    
    @classmethod
    def km_to_mpc(cls, distance_km):
        return distance_km * cls.KM_TO_MPC
    
    @classmethod
    def sec_to_gyr(cls, time_sec):
        return time_sec / cls.GYR_TO_SEC
    
    @classmethod
    def kg_to_msun(cls, mass_kg):
        return mass_kg / cls.MSUN_TO_KG