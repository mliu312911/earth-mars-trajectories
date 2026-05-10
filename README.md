# Earth-to-Mars Trajectory Simulation

I built these simulations during my 10-week NSF REU at RIT in Summer 2025, working under Dr. Michael Richmond. When I started, I had no Python experience and learned by checking out library books. By the end, I was running 2D and 3D models of rocket trajectories from Earth to Mars.

## Overview

Numerical simulation of spacecraft trajectories from Earth to Mars, modeling gravitational effects of the Sun, Earth, and Mars. Compares chemical and ion propulsion systems for propellant efficiency and transit time trade-offs.

## Files

| File | What it runs |
| :--- | :--- |
| `analytic_solar_system_2d.py` | Just Earth and Mars orbiting. No rocket. |
| `euler_chemical_2d.py` | Chemical rocket with two impulsive burns, Hohmann transfer. |
| `euler_ion_single_2d.py` | Single ion engine, low-thrust spiral outward. |
| `euler_ion_multi_2d.py` | Same thing but with N engines for higher thrust. |
| `euler_combined_2d.py` | All three rocket types in one visualization for comparison. |
| `euler_chemical_3d.py` | Chemical rocket in VPython 3D. |
| `euler_ion_3d.py` | Ion thruster in VPython 3D. |

The early files use Euler integration and a lot of repeated code (I was figuring things out as I went).

## Methods

- **Numerical Integration:** Euler's method
- **Propulsion Models:** Impulsive chemical burns, continuous low-thrust ion propulsion with variable mass
- **Visualization:** Python `turtle` (2D), VPython (3D)

## Key Results

- Modeled Hohmann transfers with chemical propulsion
- Simulated spiral trajectories for continuous-thrust ion engines
- Compared propellant mass fractions: ion propulsion requires significantly less fuel at the cost of longer transit times

## Requirements

- Python 3.x
- `turtle` (standard library)
- `vpython` (for 3D models)

## Presentations

This research was presented at:
- **247th American Astronomical Society (AAS) Meeting**, Phoenix, AZ - January 2026 (Oral)
- **RIT Undergraduate Research Symposium**, Rochester, NY - July 2025 (Oral)

## Author

Marcus Liu - NSF REU Fellow, Rochester Institute of Technology, Summer 2025
