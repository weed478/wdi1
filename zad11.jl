function factorsum(number::Integer)::Integer
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
    factor_sum
end

function main()
    Threads.@threads for i ∈ 1:1000000
        Σ₁ = factorsum(i)
        Σ₂ = factorsum(Σ₁)
        if (Σ₂ == i)
            # println("$i\t$Σ₁")
        end
    end
end
