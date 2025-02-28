- description : C / C++ 코드에서    fork 한  process 를  pid 으로  kill 할 때   자식 process 까지  다 죽도록 만들려면,어떻게 할 수 있을까요?
- tag : c , c++ , waitpid , zombie
- date : 2024-01-01

- C / C++ 코드에서    fork 한  process 를  pid 으로  kill 할 때   자식 process 까지  다 죽도록 만들려면,어떻게 할 수 있을까요?
    - 이전에   직접 실험으로 보여 주신거 중에 pipe 해서 실행하고    마지막 command가  종료 될 때    다  같이 종료됨
    - endless_log_show  xxx  cmd  |   log_search_tool  xxxx xxx 
    - log_search_tool 이   exit 할때   endless_log_show  도 같이 종료 되는 거 보여  주셔서  문의 드립니다.
    - 이것을 C / C++ 코드에서 어떻게  같이 kill 하게  동작 할 수 있을 런지요?

- https://codetravel.tistory.com/42
- https://cboard.cprogramming.com/c-programming/138057-waitpid-non-blocking-fork.html


```cpp
else {
    printf("The pid of the child is: %d\n", pid);
    int waittime = 0;
    int Stat;
    do {
        wpid = waitpid(pid, &Stat, WNOHANG);
        if (wpid == 0) {
            if (waittime < timeout) {
                printf("Parent waiting %d second(s).\n", waittime);
                sleep(1);
                waittime ++;
            }
            else {
                printf("Killing child process\n");
                kill(pid, SIGKILL); 
            }
        }
    } while (wpid == 0 && waittime <= timeout);
 
    if (WIFEXITED(Stat)) {
        printf("Child exited, status=%d\n", WEXITSTATUS(Stat));
    }
    else if (WIFSIGNALED(Stat)) {
        printf("Child %d was terminated with a status of: %d \n", pid, WTERMSIG(Stat));
    }
}
```