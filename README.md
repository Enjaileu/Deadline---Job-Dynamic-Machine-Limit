# Deadline - Dynamic machine limit
## Context
Script developped for the Artfx Montpellier renderfarm. 
## Purpose
The purpose of this script is to **prevent a heavy render from monopolizing the renderfarm for too long**. The strategy adopted is to spread the rendering out over time by regularly recalculating a machine limit. The script is designed to be used as a pre-task and post-task script. 
## How to use
![ArtfxDynamicMachineLimitParameters](https://github.com/Enjaileu/Deadline_Dynamic_Machine_Limit/assets/95125285/acb6f520-fc90-4615-8d66-593e3cad6544)

The event serves as an interface for setting script parameters. In Deadline, go to Tools>Configure Event Plugins.
1. Users who can use the script.
2. The percentage of the workers the job is authorized to use.
   
![script_explain](https://github.com/Enjaileu/Deadline_Dynamic_Machine_Limit/assets/95125285/7f266734-fafc-421b-93d1-e944ebfdc69d)

In our example, if the farm has 450 workers available and the percentage is 30%, the job's machine limit is set to 135.
