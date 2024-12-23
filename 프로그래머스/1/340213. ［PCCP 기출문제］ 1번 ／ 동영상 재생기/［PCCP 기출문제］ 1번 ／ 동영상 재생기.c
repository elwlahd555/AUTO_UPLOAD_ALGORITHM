#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// commands_len은 배열 commands의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* video_len, const char* pos, const char* op_start, const char* op_end, const char* commands[], size_t commands_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(10);
    memset(answer, '\0', 10);
    int video_len_second=0;
    int now_second=0;
    int op_start_second=0;
    int op_end_second=0;
    char* temp = (char*)malloc(10);
    video_len_second+=((int)video_len[0]-48)*600;
    video_len_second+=((int)video_len[1]-48)*60;
    video_len_second+=((int)video_len[3]-48)*10;
    video_len_second+=((int)video_len[4]-48);
    
    now_second+=((int)pos[0]-48)*600;
    now_second+=((int)pos[1]-48)*60;
    now_second+=((int)pos[3]-48)*10;
    now_second+=((int)pos[4]-48);
    
    op_start_second+=((int)op_start[0]-48)*600;
    op_start_second+=((int)op_start[1]-48)*60;
    op_start_second+=((int)op_start[3]-48)*10;
    op_start_second+=((int)op_start[4]-48);
    
    op_end_second+=((int)op_end[0]-48)*600;
    op_end_second+=((int)op_end[1]-48)*60;
    op_end_second+=((int)op_end[3]-48)*10;
    op_end_second+=((int)op_end[4]-48);

    for(int i=0; i<commands_len; i++){

        if(op_start_second<=now_second && now_second<=op_end_second){
            now_second=op_end_second;
        }
        if(strcmp(commands[i],"next")==0){
            now_second+=10;
            if(now_second>video_len_second){
                now_second=video_len_second;
            }
        }else if(strcmp(commands[i],"prev")==0){
            now_second-=10;
            if(now_second<0){
                now_second=0;
            }
        }
    }
    if(op_start_second<=now_second && now_second<=op_end_second){
        now_second=op_end_second;
    }

    if(now_second/60<10){
        strcat(answer,"0");
    }
    sprintf(temp, "%d", now_second/60);
    strcat(answer,temp);
    strcat(answer,":");
    sprintf(temp, "%d", now_second%60);
    if(now_second%60<10){
        strcat(answer,"0");
    }
    strcat(answer,temp);
    return answer;
}