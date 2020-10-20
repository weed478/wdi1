Aₙ₊₁(Aₙ::Int64)::Int64 = (Aₙ % 2) * (3Aₙ + 1) + (1 - Aₙ % 2) * Aₙ ÷ 2

function getnforseries(a₀::Int64)::Int64
    aₙ = a₀
    n = 0
    while aₙ != 1
        aₙ = Aₙ₊₁(aₙ)
        n += 1
    end
    n
end

function main(target::Integer)
    maxpool::AbstractVector{Tuple{Int64, Int64}} = Array{Tuple{Int64, Int64}}(undef, Threads.nthreads())

    # target = 2^20
    perthread = target ÷ Threads.nthreads()

    Threads.@threads for t ∈ 1:Threads.nthreads()
        bestₐ = 1
        bestₙ = 0
        start = (t - 1) * perthread + 2
        for a ∈ start:start + perthread
            n = getnforseries(a)
            if n > bestₙ
                bestₙ = n
                bestₐ = a
            end
        end
        maxpool[t] = (bestₐ, bestₙ)
    end
    maxₙ = maximum(p->p[2], maxpool)
    maxᵢ = findall(p->p[2]==maxₙ, maxpool)
    for i ∈ maxᵢ
        best = maxpool[i]
        println("a = $(best[1]) n = $(best[2])")
    end
end
