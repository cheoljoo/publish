- description : TIDL (Tiger Interface Definition Language)을 수행시키는 starting part만 적어둔 것이다.
- tag : TIDL , docker
- date : 2024-01-01

# getting started - 2024Y
- git clone http://mod.lge.com/hub/cheoljoo.lee/TIDL.git

## docker run to get documents
- $ bash docker.sh 1
- remove 227 exit 0  in CGADoxygen/run.sh
```txt
diff --git a/run.sh b/run.sh
index a6b665f..94ffb1a 100755
--- a/run.sh
+++ b/run.sh
@@ -224,7 +224,6 @@ echo "#### build_doxygen makefile ####"
 tput sgr0
 cd build_doxygen; make ; cd ..

-exit 0

 tput setaf 2
 echo "#### build_uml makefile ####"
 ```
- $ bash docker.sh 2
- final result :
  - CGADoxygen/build_perlmod/OUTPUT/sequ.css.html
  - CGADoxygen/build_perlmod/OUTPUT/nece.css.html

## run.sh  without docker
- pip3 install hpp2plantuml
  - change perl to python execution file : it has the same options
- pip3 install MarkdownPP
  - it makes markdown package for document
- minimize use of perl module
  - remove cga2excel.pl  in CGADoxygen/build_perlmod/makefile
  - git diff build_perlmod/makefile
```
diff --git a/build_perlmod/makefile b/build_perlmod/makefile
index 8dc0406..ba196ce 100644
--- a/build_perlmod/makefile
+++ b/build_perlmod/makefile
@@ -25,7 +25,7 @@ all:
        perl ../collab.pl OUTPUT/LLD.html
        perl ../collab.pl OUTPUT/LLD.html.md
        perl ../collab.pl OUTPUT/LLD.css.html
-       perl cga2excel.pl default.GV OUTPUT/LLD.xlsx > c3.log
+        #perl cga2excel.pl default.GV OUTPUT/LLD.xlsx > c3.log
        perl cga2class.pl > class.log

        sh makeBasicDocumentsInOUTPUT.sh
```
- final result:
  - http://tiger02.lge.com/cheoljoo.lee/temp/TIDL/CGADoxygen/build_perlmod/OUTPUT/SDD.html
  - http://lotto645.lge.com:8088/cheoljoo.lee/code/tiger/TIDL/CGADoxygen/build_perlmod/OUTPUT/nece.css.html
  - http://tiger02.lge.com/cheoljoo.lee/code/tiger/TIDL/CGADoxygen/build_perlmod/OUTPUT/SDD.html

