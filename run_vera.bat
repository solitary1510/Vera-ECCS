@echo off
set PATH=%PATH%;".\vera++";".\vera++\bin";
set VERA_ROOT=.\1212299_1212504
vera++ --show-rule --profile 1212299_1212504_rules code_need_check.c
PAUSE
