a=0
b=1
for i in range(1,11):
    a+=b
    b+=1
    print(a)
"""
BEGIN
    SET a = 0
    SET b = 1
    FOR i FROM 1 TO 10 DO
        a = a + b
        b = b + 1
        PRINT a
    END FOR
END
"""
