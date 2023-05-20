import boto3
import json
import string
import botocore.exceptions
import botocore.errorfactory
import lens
import sys

DEFAULT_WLNAME = "A2CC_template_workload"

client = boto3.client('wellarchitected')

# gen workload if not exists, else get
def get_workload(lenses=['wellarchitected'], wlname=DEFAULT_WLNAME, gen=True):
    # get the workload list
    b = 0
    wllist = None
    try:
        response = client.list_workloads()
        wllist = response['WorkloadSummaries']
        b = len(wllist)
    except:
        pass
    
    a = 0
    wlid = ""

    # if the current account has workloads, look for the template workload
    if b > 0:
        for s in wllist:
            if s['WorkloadName'] == wlname:
                wlid = s['WorkloadId']
                break
            else:
                a = a+1
    
    if wlid == "" and gen == True:
        # create a workload
        try:
            response = client.create_workload(WorkloadName=wlname,Description="A2CC WAPP workload", Environment='PRODUCTION', AwsRegions=["us-east-1"], ReviewOwner="support@a2ccloud.com", Lenses=lenses, ClientRequestToken=wlname)
            wlid = response['WorkloadId']
        except Exception as e:
            print("Error creating template workload.")
            raise e

    
    return wlid
