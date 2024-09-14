n = String.to_integer(File.read!("input.txt"))

File.write!("output.txt", Enum.join(
  for i <- 0..(n-1), do: String.duplicate(" ", n-i-1) <> String.duplicate("*", 2*i+1) <> "\n"
) <> Enum.join(
  for i <- (n-2)..0, do: String.duplicate(" ", n-i-1) <> String.duplicate("*", 2*i+1) <> "\n"
))
