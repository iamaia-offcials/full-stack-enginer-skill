# Case Study: eSIM Digital Connectivity Store

Architecture for high-velocity instant connectivity purchases and automated provisioning.

## Business Context & User Intent

- **Primary Conversion Action:** Select country, choose data volume, complete instant Apple/Google Pay, install eSIM via QR.
- **Core Friction Point:** Fear of compatibility issues, confusing GB/day calculations, complex APN setup.

## Section Sequence & Architectural Blueprint

1. **Instant Destination Search Hero:**
   - Autocomplete search input: "Where are you going?" with instant country flags.
   - Trust badge: "Instant activation in 190+ countries | No physical SIM required".

2. **Popular Region & Country Grid:**
   - Direct cards for top tourist regions (USA, Europe 33 Countries, Japan, Turkey, Thailand).

3. **Plan Configurator Widget:**
   - Toggle: Data-only vs Data + Calls.
   - Stepper: 1 GB (7 days), 3 GB (15 days), 5 GB (30 days), 10 GB (30 days), Unlimited.
   - Explicit feature checklist: Hotspot supported, operates on local Tier-1 5G networks.

4. **3-Step Setup Explainer:**
   - 1. Buy plan → 2. Scan QR code from email → 3. Turn on roaming upon landing.

5. **Device Compatibility Dropdown:**
   - Searchable device list verifying iPhone, Samsung, Pixel compatibility.
