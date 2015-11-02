@echo off
set PATH=%PATH%;".\vera++";".\vera++\bin";
set VERA_ROOT=.\1212299_1212504
vera++ -p full_vera_exam code_need_check.c
PAUSE