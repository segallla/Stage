from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List

from .data import GEOCODE_DATA, PARCEL_DATA, CIRCUIT_DATA, SUBSTATION_DATA


def geocode(address: str) -> Dict[str, Any]:
    data = GEOCODE_DATA.get(address)
    if not data:
        raise ValueError(f"Address not found: {address}")
    return {
        "input": address,
        **data,
    }


def parcel_lookup(address: str) -> Optional[Dict[str, Any]]:
    return PARCEL_DATA.get(address)


def polygon_fetch(lat: float, lon: float, area_acres: float) -> Dict[str, Any]:
    side = (area_acres * 4046.86) ** 0.5  # meters approx
    delta_deg = side / 111320  # rough deg per meter
    return {
        "method": "approximated",
        "area_sqft": area_acres * 43560,
        "geometry_type": "Polygon",
        "coordinates_sample": [
            [lat + delta_deg / 2, lon - delta_deg / 2],
            [lat + delta_deg / 2, lon + delta_deg / 2],
            [lat - delta_deg / 2, lon + delta_deg / 2],
            [lat - delta_deg / 2, lon - delta_deg / 2],
        ],
    }


def circuit_intersection(address: str) -> Dict[str, Any]:
    data = CIRCUIT_DATA.get(address)
    if not data:
        raise ValueError(f"Circuit data not found for {address}")
    return data


def substation_data(substation_name: str) -> Dict[str, Any]:
    data = SUBSTATION_DATA.get(substation_name)
    if not data:
        raise ValueError(f"Substation data not found: {substation_name}")
    return {"substation_name": substation_name, **data}


def interconnection_feasibility(circuit_info: Dict[str, Any], sub_info: Dict[str, Any]) -> Dict[str, Any]:
    voltage = circuit_info["circuit_voltage_kV"]
    deficiency = sub_info["deficiency_year"]
    if voltage >= 12 and deficiency is None:
        feasible = True
        recommended_max_mw = 5
    else:
        feasible = False
        recommended_max_mw = 0.5
    notes = (
        "Sufficient capacity for up to ~5 MW without major upgrades"
        if feasible
        else "Very limited DER capacity remaining without upgrades"
    )
    return {
        "feasible": feasible,
        "notes": notes,
        "recommended_max_MW": recommended_max_mw,
    }


def optimal_bess_config(feasibility: Dict[str, Any]) -> Dict[str, Any]:
    if feasibility["feasible"]:
        power = 4.9
    else:
        power = 0.5
    duration = 4
    return {
        "power_MW": power,
        "duration_hr": duration,
        "energy_MWh": power * duration,
        "configuration_notes": (
            "4-hr duration; under 5 MW for streamlined interconnection"
            if feasibility["feasible"]
            else "Small 0.5 MW/2 MWh to avoid major upgrades"
        ),
    }


def analyze_address(address: str) -> Dict[str, Any]:
    result = {"address": address}

    # STEP1
    geo = geocode(address)
    result["STEP1_GEOCODING"] = geo

    # STEP2
    parcel = parcel_lookup(address)
    if parcel:
        result["STEP2_PARCEL_LOOKUP"] = parcel
        area = parcel["parcel_area_acres"]
    else:
        result["STEP2_PARCEL_LOOKUP"] = {"APN": None, "error": "Parcel not found in data"}
        area = 0.5

    # STEP3
    result["STEP3_POLYGON_FETCH"] = polygon_fetch(geo["lat"], geo["lon"], area)

    # STEP4
    circuit = circuit_intersection(address)
    result["STEP4_CIRCUIT_INTERSECTION"] = circuit

    # STEP5
    sub = substation_data(circuit["substation_name"])
    result["STEP5_SUBSTATION_DATA"] = sub

    # STEP6
    feas = interconnection_feasibility(circuit, sub)
    result["STEP6_INTERCONNECTION_FEASIBILITY"] = feas

    # STEP7
    result["STEP7_OPTIMAL_BESS_CONFIG"] = optimal_bess_config(feas)

    # STEP8 map placeholder
    result["STEP8_MAP_VISUALIZATION"] = {
        "map_image": "N/A",
        "legend": {
            "blue_polygon": "Parcel boundary",
            "red_line": "Distribution circuit",
            "black_x": "Site location",
        },
    }

    return result


def analyze_addresses(addresses: List[str]) -> List[Dict[str, Any]]:
    return [analyze_address(addr) for addr in addresses]
