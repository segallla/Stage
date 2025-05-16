GEOCODE_DATA = {
    "44933 Fern Ave, Lancaster, CA 93534": {
        "lat": 34.6944,
        "lon": -118.1750,
        "geocoder": "stub"
    },
    "456 Elm St, Compton, CA 90220": {
        "lat": 33.8950,
        "lon": -118.2230,
        "geocoder": "stub"
    },
    "5300 Sheila St, Commerce, CA 90040": {
        "lat": 34.0006,
        "lon": -118.1521,
        "geocoder": "stub",
    },
}

PARCEL_DATA = {
    "44933 Fern Ave, Lancaster, CA 93534": {
        "APN": "3153-015-959",
        "parcel_area_acres": 1.4,
        "parcel_area_sqft": 60984,
    },
    "456 Elm St, Compton, CA 90220": None,
    "5300 Sheila St, Commerce, CA 90040": {
        "APN": "5248-001-026",
        "parcel_area_acres": 2.0,
        "parcel_area_sqft": 87120,
    },
}

CIRCUIT_DATA = {
    "44933 Fern Ave, Lancaster, CA 93534": {
        "circuit_id": "CIRCUIT-XYZ",
        "circuit_voltage_kV": 12,
        "substation_name": "Lancaster",
        "circuit_distance_m": 50,
    },
    "456 Elm St, Compton, CA 90220": {
        "circuit_id": "COMPTON-4KV-1",
        "circuit_voltage_kV": 4,
        "substation_name": "Compton",
        "circuit_distance_m": 100,
    },
    "5300 Sheila St, Commerce, CA 90040": {
        "circuit_id": "CIRCUIT-COMMERCE",
        "circuit_voltage_kV": 16,
        "substation_name": "Commerce",
        "circuit_distance_m": 30,
    },
}

SUBSTATION_DATA = {
    "Lancaster": {
        "system_name": "Antelope Valley",
        "deficiency_year": None,
        "status": "No projected capacity shortfall (next 5 years)",
    },
    "Compton": {
        "system_name": "South Bay",
        "deficiency_year": 2025,
        "status": "Capacity-constrained (deficiency by 2025)",
    },
    "Commerce": {
        "system_name": "Los Angeles",
        "deficiency_year": None,
        "status": "No projected capacity shortfall (next 5 years)",
    },
}
