a=0
for i in range(1,11):
    a+=i
    i+=1
    print(a)
"""
BEGIN
    SET a = 0
    SET b = 1
    FOR i FROM 1 TO 11 DO
        a = a + b
        b = b + 1
        PRINT a
    END FOR
END
"""