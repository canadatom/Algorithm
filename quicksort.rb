class QuickSort
	def outplace_sort(to_sort)
		return to_sort if to_sort.length <= 1

		pivot = to_sort.pop

		left_arr = []
		right_arr = []

		to_sort.each do |x|
			if x <= pivot 
				left_arr.push(x) 
			else
				right_arr.push(x)
			end
		end
		return outplace_sort(left_arr).push(pivot) + outplace_sort(right_arr)
	end

	def inplace_sort!(to_sort, start, finish)
		if (start < finish)
			p_index = inplace_partition(to_sort, start, finish)
			inplace_sort!(to_sort, start, p_index - 1)
			inplace_sort!(to_sort, p_index + 1, finish)
		end
		return to_sort
	end

	def inplace_partition(to_partition, start, finish)
		pivot = to_partition.first
		p_index = start
		to_partition.each do |x|
			if (x <= pivot)
				x, to_partition[p_index] = to_partition[p_index], x 
				p_index += 1
			end
		end
		to_partition[p_index], to_partition.first = to_partition.first, to_partition[p_index]
		return p_index
	end
end

to_sort = [ 3, 5, 10, 4, 8, 7 ]
qs = QuickSort.new
print qs.outplace_sort(to_sort)
print qs.inplace_sort!(to_sort, 0, to_sort.size - 1)