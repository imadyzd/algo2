#@ function abs (n: int) -> int = if n >= 0 then n else -n

#@ predicate require_max_abs (a:int ,b:int ,c: int ) = True
#@ predicate ensure_max_abs (a:int ,b:int ,c:int , res: int) = (res == abs(a) and res >= abs(b) and res >=abs(c)) or (res == abs(b) and res >=abs(a) and res >= abs(c)) or (res == abs(c) and res >= abs(b) and res >=abs(a))
#@ predicate test_max_abs (a:int ,b:int ,c:int , res : int ) = require_max_abs (a,b,c) -> ensure_max_abs (a,b,c, res )

#@ assert test_max_abs (5 ,8 ,2 ,8)
#@ assert test_max_abs ( -2 ,4 , -6 ,6)
#@ assert test_max_abs (17 , -2 ,4 ,17)
#@ assert test_max_abs ( -2 , -4 , -10 ,10)

#@ assert not test_max_abs (4 , -10 ,8 ,8)
#@ assert not test_max_abs (7 , -1 , -9 ,7)
