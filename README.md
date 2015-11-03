# Vera-_ECCS
Some rule using Vera++ for checking Coding standard. Rule can found at "./untitled/rules/"

Rule need to do:

- 1.8.b.iii: The const keyword shall be used whenever appropriate to define fields in structs and unions that should not be modified (e.g., in a struct overlay for memory-mapped I/O peripheral registers)

3.1.c    : Each of the binary operators +, -, *, /, %, <, <=, >, >=, ==, !=, <<, >>, &, |, ^, &&, and || shall always be preceded and followed by one space.

3.1.e    : The pointer operators * and & shall be written with white space on each side within declarations but otherwise without a space on the operand side.

+ 3.1.h    : The left and right brackets of the array subscript operator ([ and ]) shall always be without surrounding spaces.

+ 3.1.k    : Each comma separating function parameters shall always be followed by one space.

+ 3.1.m    : Each semicolon shall follow the statement it terminates without a preceding space.

3.3.c    : Each source file shall have a blank line at the end.

+ 5.1.b    : All new structures, unions, and enumerations shall be named via a typedef.

- 6.1.g    : Underscores shall be used to separate words in procedure names.

- 6.3.a    : Parameterized macros shall not be used if an inline function can be written to accomplish the same task.

6.3.b.i  : If parameterized macros are used, Surround the entire macro body with parentheses.

6.3.b.ii : If parameterized macros are used, Surround each use of a parameter with parentheses.

7.1.m    : The names of all integer variables containing “effectively Boolean” information (i.e., 0 vs. nonzero) shall begin with the letter ‘b’ and phrased as the question they answer. For example, b_done_yet or gb_is_buffer_full.

8.4.b    : Except for a single loop counter initialization in the first clause of a for statement, assignments shall not be made in any loop’s controlling expression.

+ 8.5.a    : The keywords goto, continue, and break shall not be used to create unconditional jumps.

Embedded C Coding Standard (2008) - Michael Barr
