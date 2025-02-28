- description : JIRA / CodeBeamer / Gerrit등의 개발 시스템을 사용하는 사용자들의 performance가 어떻게 되는지를 check하기 위한 project (MOUSE)
- tag : mouse , performance , check
- date : 2025-01-01


# Mouse
## [Common]
- use CSV & JSON as input / output interface between processes (python) : http://tiger02.lge.com:18080/proxy?fmt=svg&src=http://tiger02.lge.com/cheoljoo.lee/code/mouse/total.md
## [LDAP]
- LDAP (everytime)
    - lge_ldap_jira_member.py : get ldap information based on input-unit.csv
    	- LDAP server connection : http://mod.lge.com/hub/cheoljoo.lee/ldap/-/blob/main/lge_ldap_jira_member.py#L18-55
    	- usage : http://mod.lge.com/hub/cheoljoo.lee/ldap/-/blob/main/lge_ldap_jira_member.py#L173
## [GITLAB : mod.lge.com/hub]
- MOUSE (daily/weekly)
    - mod-project.py : get projects name from mod.lge.com/hub (gitlab) (parallelization)
    	- basic restapi get 'http://mod.lge.com/hub/api/v4/projects' : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/mod-project.py#L68-104
    	- parallelization : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/mod-project.py#L274-319
    - mod-fork.py  : remove forked project (parallelization)
    	- get forked project : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/mod-fork.py#L233
    - mod-chosen.py : choose proper project with related to ours. (parallelization)
    	- compare with date (updated date) : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/mod-chosen.py#L244-251
    	- get commit to find proper committer (we need to find team member) : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/mod-chosen.py#L254-278
    - mod-chosen-commit.py : get commit data (parallelization)
    	- get commit data : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/mod-chosen-commit.py#L245-303
    - make-vlm-comment.py : make data for comment in vlm in related to JIRA# in commit
    	- make a list of commit : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/make-vlm-comment.py#L323-345
    - vlm-add-comment.py : write comment in vlm
    	- save the table whether this commit was already existed.   if it is not commented, add commit in jira ticket based on commit message. [VLM:___] : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/vlm-add-comment.py#L107-121
## [GIT]
- SLDD-Tiger (daily)
    - sldd/sldd-clone.py : clone vgit & do 'git log' & do 'git show' and parse it -> get data in related to sldd (parallelization)
    	- pprint : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/sldd-tiger/sldd-clone.py#L50-156
    	- get 'git show and git log' for each project : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/sldd-tiger/sldd-clone.py#L177-197
    	- pasrse log and show with state diagram : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/sldd-tiger/sldd-clone.py#L209-233
    - sldd/make-vlm-comment-sldd-tiger.py : make data for comment in vlm in related to JIRA# in commit of sldd file
    - sldd/vlm-add-comment.py : write comment in vlm
## [JIRA]
- UPDATE COMMENT
    - update_comments/CSearchVlm.py : reporter != assignee and need to update  (now : single , need parallelization)
    	- find 'reporter != assignee and need to update' in unresolved : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/update_comments/CSearchVlm.py#L134-136
    	- check date : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blame/master/update_comments/CSearchVlm.py#L394-402
    - update_comments/make-vlm-update-comment.py : vlm update
- Weekly Report (daily) -> simple case to do [1. get jira / 2. get info / 3. do something with info]
    - ddpi/CJQLAdvanced.py -dirname=wrjson/data -fileprefix="wr" -alltickets -updateduration=-7d : gather recent 7 days jira tickets in TIGER project (parallelization)
    	- commonly we can use this file to get jira issues with JQL
    	- jql has string limit. check members # : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CJQLAdvanced.py#L139-149
    	- jira query (get all fields each jira ticket) : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CJQLAdvanced.py#L149-160
    	- parallelized jira query : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CJQLAdvanced.py#L319-352
    - ddpi/CAnalysisVlm.py --inputdir=wrjson/data --inputfileprefix="wr-first" --outputfileprefix=update : commonly we can use this file to analyze jira issues (parallelization)
    	- show the result
    	- analyze all file with input prefix in input directory , then write analyzed info into the same input directory with output prefix
    	- get gerrit commit owner : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CAnalysisVlm.py#L1127-1155
    	- check points in jira issue:
    		- changelog history/reopen/pingpong/emtion/assignees ... : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CAnalysisVlm.py#L282
    	- comments string for specific cases / comment body parsing : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CAnalysisVlm.py#L1157
    - ddpi/CWeeklyReport.py --inputdir=wrjson/data --inputfileprefix=update : get <wr>..</wr> report / make html
    	- convert string for html : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CWeeklyReport.py#L218-227
    	- for with sort : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CWeeklyReport.py#L277-290
## [GERRIT]
- GERRIT (yearly report)
    - commit-review/main.py : parallelized commit review check / can get all information for this gerrit commit (parallelization)
    	- twice connection : 1. get commits from project -> 2 get detail from each commit : http://mod.lge.com/hub/yoosang.won/commit-review-checker/-/blob/main/main.py#L333-361
    		- 1. get commits from project : http://mod.lge.com/hub/yoosang.won/commit-review-checker/-/blob/main/main.py#L135
    		- 2. get change detail : http://mod.lge.com/hub/yoosang.won/commit-review-checker/-/blob/main/main.py#L35
    	- reference : this project considers 3 gerrit server (na/eu/as) : http://mod.lge.com/hub/cheoljoo.lee/new_commit_review_violation_checker/-/blob/main/group/CGerritReviewViolation.py
    		- python argument parse : http://mod.lge.com/hub/cheoljoo.lee/new_commit_review_violation_checker/-/blob/main/group/CGerritReviewViolation.py
    		- crontab : 5 5 * * *  /bin/bash /home/cheoljoo.lee/code/crontab/new_commit_review_violation_checker/group/b.sh  -> (make all)
## [JIRA&CodeBeamer]
- DDPI dailyTodo (daily report)
    - ddpi/CCodeBeamerGet.py --step=unresolved : get all CodeBeamer unresolved ticket with related to members
    	- you need the permission to access CB restapi
    	- we have several cb server : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CCodeBeamerGet.py#L302-309
    	- library : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/getcbrest.py
    - ddpi/CAnalysisCb.py --finaldir="cb" : analyze codeBeamer
    	- make output with the format of jira analysis (CAnalysisVlm.py)
    - ddpi/CJQLAdvanced.py : get unresolved jira ticket  : new method
    - ddpi/CAnalysisVlm.py --inputdir=update : analyze stored JIRA ticket (parallelization)
    	- make comments after analyzing jira ticket fiedls for overdue/TooLong : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CAnalysisVlm.py#L919-1004
    	- value set : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CAnalysisVlm.py#L886-902
    - ddpi/CUpdate.py : make history and personal data
    	- personal and organized classification : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CUpdate.py#L77-83
    - ddpi/CHtml.py : make thml and fatigue data
    	- need all cb / vlm info : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CHtml.py#L2092-2109
    	- create personal and organized html : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CHtml.py#L76
    	- CB table : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CHtml.py#L263-271
    	- JIRA table : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CHtml.py#L273-287
    	- gantt chart : 
    		- http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CHtml.py#L292-295
    		- http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CHtml.py#L842-972
    	- google data stacked chart : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CHtml.py#L311-333
    	- google chart line graph & table : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CHtml.py#L714-836
    - ddpi/CCommentsHTML.py : make html for commented ticket automatically
    - ddpi/vlm-add-comment.py : add comments in ticket which need to update (check whether it needs to update in ddpi/CAnalysisVlm.py)
- DDPI mgmt (weekly report)
    - ddpi/CJQL.py -mgmt : get all JIRA ticket with related to members (parallelization)
    	- query with specific fields : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CJQL.py#L151
    - ddpi/CAnalysisVlm.py -mgmt : analyze stored JIRA ticket (parallelization)
    - ddpi/CPersonal.py -mgmt : get html for each person and organization and scrum
    	- calculate the snapshot from all history data (changelog history) : http://mod.lge.com/hub/cheoljoo.lee/mouse/-/blob/master/ddpi/CPersonal.py#L249-329
- DDPI stat (yearly performance report)
    - ddpi/CCodeBeamerGet.py --step=all : get all CodeBeamer ticket with related to members (parallelization)
    - ddpi/CCodeBeamerSingleItem.py : divide codebeamer data for each user
    - ddpi/CAnalysisCb.py --finaldir="json/finalcb" : analyze codeBeamer
    - ddpi/CJQL.py : get all JIRA ticket with related to members (parallelization)
    - ddpi/CAnalysisVlm.py : analyze stored JIRA ticket (parallelization)
    - ddpi/vlm-reopen.py : check reopen status
    - ddpi/CPersonal.py : make yeraly performance report (html , email)
    	- all score are calculated in here.

# statistical data 를 모델별로 뿌려 달라고 함. - yesterday page에 들어가면 볼수 있음.


