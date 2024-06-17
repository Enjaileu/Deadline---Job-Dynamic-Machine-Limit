from __future__ import absolute_import
from Deadline.Scripting import MonitorUtils, RepositoryUtils, ClientUtils
import os

def __main__(*args):
    ##### author : angele.sionneau@artfx.fr
    ##### This script should be used as a post or pre task script
    ##### When executed, it count the number of workers that are active in the renderfarm. The job's Machine Limit is set to a certain percentage of this count.
    ##### The users that can use this script must be set to the event "ArtfxDynamicMachineLimit" parameters in "Configure Events"
    deadlinePlugin = args[0]
    job = deadlinePlugin.GetJob()

    # execute the script only if the job user is allowed to use it
    if is_user_allowed(job.JobUserName):

        # get all workers infos
        infos = RepositoryUtils.GetSlaveInfoSettings(invalidateCache=True)
        worker_enable_count = 0
        for worker_infos in infos:
            print(worker_infos)
            # if the worker is not offline and if it is enable, it is counted
            if worker_infos.Settings.SlaveEnabled:
                if "Offline" not in str(worker_infos.Info):
                    worker_enable_count += 1
        
        # get the percentage of workers wanted
        percent_wanted = float(RepositoryUtils.GetEventPluginConfig("ArtfxDynamicMachineLimit").GetConfigEntry("PercentWorkers"))
        worker_count_allowed = int((percent_wanted/100)*worker_enable_count)
        print(f"Machine limit du job set a {worker_count_allowed}")

        # set the machine limit
        RepositoryUtils.SetMachineLimitMaximum(job.JobId, worker_count_allowed)

def is_user_allowed(name):
    users_allowed = RepositoryUtils.GetEventPluginConfig("ArtfxDynamicMachineLimit").GetConfigEntry("Users").split(';')
    return name in users_allowed

