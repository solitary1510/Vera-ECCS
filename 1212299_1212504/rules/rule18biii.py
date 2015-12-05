# coding=utf-8
# Rule 1.8.b.iii: The const keyword shall be used whenever appropriate to define fields in structs
# and unions that should not be modified
# (e.g., in a struct overlay for memory-mapped I/O peripheral registers)

# Luật này có nhiều nhập nhằng. Vì khó có thể biết được thuộc tính nào là những thuộc tính không
# được phép thay đổi như những map về các thanh ghi đọc/ghi......