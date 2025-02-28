- description : cisco style command line interface에 대한 정보이다. fish project에 구현이 되어져있고, 상세 설명도 잘 되어져있다. C++ version도 구현되어져있다.
- tag : c++ , python , cisco , cli
- date : 2024-01-01


# getting started - 2024Y
- tcmd
  - git clone http://mod.lge.com/hub/Tiger/AutoTest_Cmd
- fish (cisco style cli)
  - git clone https://github.com/cheoljoo/fish

## what i do to add aloga command in tcmd
- tcmd update automatically if we check the new version
  - but , we need not to update.  -> this update will do in ```tiger_common_cmd.sh```
  - ```
    init_tcmd() {

        echo "init_tcmd : but return for test"
        return
    ```
- ```tiger_common_cmd.py```
  - add element in TOP variable
    - 
