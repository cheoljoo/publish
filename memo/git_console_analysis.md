
- description : git blame을 다루는 법
- tag : git, blame
- date : 2024-01-01

----------------------------------

# git blame for csv file
- we should find csv row. so we need to process comma delimiter.
  - count "
  - if we meet \n and count is odd , then it is row end of csv file
  - if we meet \n and count is even , then it is inside of contents of field in csv file
- getting information
  ```json
    {
        'csvdata' : {
            'date' : {     # writing date
                'TRDK': {
                    '[git_repository]' :  {
                      '[filename]' : {   # filename
                          '[csv_line_number]': {    # csv line number
                              'date' : today's date,
                              'classification' : TRDK,
                              'git' : git_repository,
                              'branch' : branch_name,
                              'fn' : filename,
                              'lncsv' : csv_line_number
                              'lnfile' : [] ,   # file line list
                              'committer' : ...,
                              'SHA' : ... ,     # commit SHA  
                              'time' : ... , # commit time
                              'value' : {
                                  field : value
                              },
                              'runResult' : boolean   # only for expected_log_scenario
                          },
                          ...
                      }
                    }
                },
                'TDSK' : {
                    # it is same with TRDK
                }
            }
            ...
        },
        'info' : {
            ...
            ...
        }

    }
  ```
  - filename  (fn)
  - line number in excel (lncsv)
  - line number in file (lnfile)
  - value of each field (value { field : value , ...})
  - committer (committer)
  - commit SHA (SHA)
  - commit time (time)

- Todo
  - change process map
  - add filename and csv_line_number to compare the result in result_logscenario.json (ALOGA/gatherExpected.py)
    - gatherExpected.py : add filename and csv_line_number in taf_expected_log_scenario.csv
  - json file size : create file each date (ALOGA/getExpectedGitBlame.py)
    - we can merge files if we need
  - gather each file  (ALOGA/historyCopy.py)
  - how to get the difference between date's datum (ALOGA/historyCopy.py)
    - data size
  - getting information will get the result from result_logscenario.json (ALOGA/historyCopy.py)
    - make the history json for finalResult and fail evidence
  - copy aloga.html for backup and find the result ... (ALOGA/historyCopy.py)

## Design Change because of bitbake
- ALOGA/getExpectedGitBlame.py generates each gitblame-~~~.json in STORE directory
	- not one json file
	- ALOGA/data_git_store directory
  	- ALOGA/data_git_store/expected_log_msg_*.csv
    - ALOGA/data_git_store/expected_log_scenario_*.csv
    - ALOGA/data_git_store/gitblame_expected_log_msg_*.json
    - ALOGA/data_git_store/gitblame_expected_log_scenario_*.json
- ALOGA/gatherExpected.py will merge into one file ( ALOGA/taf_git_blame_scenario.json ) from ALOGA/data_git_store/gitblame_expected_log_scenario_*.json
- ALOGA/logScenarioAnalyzer.py merged this gitblame result in ALOGA/result_logscenario.json
- ALOGA/htmlScenario.py will show additional information
- ALOGA/historyCopy.py will stack the current information into historyALOGA.json.
  - historyALOGA.json should be in unremovable place.  generally we cloned from git when we run it. so historyALOGA.json should be out of cloned directory.

