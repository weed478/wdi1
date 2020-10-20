function fib(x::Integer)
    a = 1
    b = 1

    while a < x
        println(a)
        b = a + b
        a = b - a
    end
end

fib(1000000)
