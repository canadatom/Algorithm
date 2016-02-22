def add_digits(num)
    return num if num < 10
    a = num / 10
    b = num % 10
    add_digits(a + b)
end

puts add_digits(38)