#!/bin/python3
'''
Created by Theodore Cowan (http://theodore.me)

This script will crawl through all builds in teamcity and execute do_something().  Modify the do_something function to gain your desired affect.
'''

import requests, json

teamcity_url = "teamcity.domain.com"
teamcity_user = "username"
teamcity_pass = "password"


def do_something(id, name, paused, description, projectName, projectId, href, webUrl):
    '''
    Edit this function with your desired affect

      "id": "Crm_Build"
      "name": "Build"
      "paused": true
      "description": "Build artifact"
      "projectName": "CRM"
      "projectId": "Crm"
      "href": "/app/rest/buildTypes/id:Crm_Build"
      "webUrl": "https://teamcity.domain.com/viewType.html?buildTypeId=Crm_Build"


    Example: Find all builds with a parameter value.

    ..code:: python

      find = "ASDFD42F532SFLSDFJI4"

      headers = {'Accept': 'application/json'}
      build = requests.get('https://'+teamcity_url+href, headers=headers, auth=(teamcity_user, teamcity_pass), timeout=5)
      try:
          build.raise_for_status()
      except:
          print("Failed to get {0}\n{1}".format(id, settings.text))
  
      build = json.loads(build.text)
  
      for parameter in build['parameters']['property']:
          if parameter.get('value') == find:
              print("FOUND {0} in build {1}".format(find, id))
    '''
    print("Did nothing.  Replace this with something useful.\n")

         
def crawl():
    '''
    crawler function
    '''

    headers = {'Accept': 'application/json'}
    #Get list of project builds
    builds = requests.get('https://'+teamcity_url+'/app/rest/buildTypes', headers=headers, auth=(teamcity_user, teamcity_pass), timeout=5)

    try:
        builds.raise_for_status()
    except:
        raise Exception ("{}\nGet builds request failed.".format(builds.text))

    builds = json.loads(builds.text)
    print("Crawling {} builds".format(builds['count']))
    for n, build in enumerate(builds['buildType']):
        do_something(build['id'], build['name'], build.get('paused', 'undefined'), build.get('description', 'undefined'), build['projectName'], build['projectId'], build['href'], build['webUrl'])

crawl()
print("done")
