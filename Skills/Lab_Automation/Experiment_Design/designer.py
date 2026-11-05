# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

from typing import List, Dict

# Experiment Designer
# Focus: Thermo Fisher / Lab Automation Partnership
# Capabilities: Generates high-level robot commands from scientific intent.

class ExperimentDesigner:
    def __init__(self):
        self.supported_robots = ["Opentrons_OT2", "Tecan_Fluent"]

    def design_experiment(self, intent: str, parameters: Dict) -> Dict:
        """
        Translates scientific intent (e.g., 'Make a pH gradient') into robot steps.
        """
        print(f"Designing experiment for: {intent}")
        
        protocol = {
            "metadata": {
                "name": intent,
                "robot": parameters.get("robot", "Opentrons_OT2")
            },
            "labware": self._select_labware(parameters),
            "steps": []
        }

        if "gradient" in intent.lower():
            protocol["steps"] = self._generate_gradient_steps(parameters)
        elif "pcr" in intent.lower():
            protocol["steps"] = self._generate_pcr_steps(parameters)
        
        return protocol

    def _select_labware(self, params: Dict) -> Dict:
        # Simplified selection logic
        return {
            "source_plate": "corning_96_wellplate_360ul_flat",
            "destination_plate": "nest_96_wellplate_100ul_pcr_full_skirt",
            "tiprack": "opentrons_96_tiprack_300ul"
        }

    def _generate_gradient_steps(self, params: Dict) -> List[Dict]:
        steps = []
        start_conc = params.get("start_conc", 10)
        end_conc = params.get("end_conc", 100)
        wells = params.get("wells", 12)
        
        step_size = (end_conc - start_conc) / (wells - 1)
        
        for i in range(wells):
            current_conc = start_conc + (i * step_size)
            steps.append({
                "action": "transfer",
                "source": "A1", # Reservoir
                "dest": f"A{i+1}",
                "volume": 50, # Mock volume logic
                "mix_after": True,
                "comment": f"Creating concentration {current_conc:.2f} mM"
            })
        return steps

    def _generate_pcr_steps(self, params: Dict) -> List[Dict]:
        return [{"action": "distribute_mastermix", "volume": 20}]

if __name__ == "__main__":
    designer = ExperimentDesigner()
    
    # User Intent: Create a drug concentration gradient
    experiment_params = {
        "robot": "Opentrons_OT2",
        "start_conc": 0,
        "end_conc": 50,
        "wells": 8
    }
    
    protocol = designer.design_experiment("Drug Concentration Gradient", experiment_params)
    
    import json
    print(json.dumps(protocol, indent=2))

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
