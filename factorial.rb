#!/usr/bin/ruby

def fact(n)
  if (n == 0)
    1
  else 
    n * fact(n - 1)
  end
end

puts fact(0)
puts fact(1)
puts fact(2)
puts fact(5)

