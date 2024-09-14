n = File.read('input.txt').to_i

File.open('output.txt', 'w') do |file|
  n.times {|i|file.puts' '*(n-i-1) + '*'*(2*i+1)}
  (n-1).times {|i|file.puts' ' *(i+1) + '*'*(2*(n-i-2)+1)}
end
