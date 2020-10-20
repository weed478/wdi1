function is_ideal(number::Unsigned)::Bool
    if number == 1
        return false
    end

    factor_sum = 1
    x = 2
    while x*x < number
        div, mod = divrem(number, x)
        if mod == 0
            factor_sum += x
            if x != div
                factor_sum += div
            end
        end
        x += 1
    end

    return factor_sum == number
end

function main()
    for i::Unsigned in 1:1000000
        if is_ideal(i)
            println("$i jest wspaniałe")
        end
    end
end
