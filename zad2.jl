function getfibstart(year)
    Σ = -1
    a = -1

    x = 1
    y = 1

    while year > x
        a′ = 0
        while year > x * a′
            a′ += 1

            if (year - x * a′) % y == 0
                b = (year - x * a′) ÷ y
                if Σ < 0 || a′ + b < Σ
                    Σ = a′ + b
                    a = a′
                end
            end
        end
        y = x + y
        x = y - x
    end

    return (a, Σ - a)
end

println(getfibstart(2020))
