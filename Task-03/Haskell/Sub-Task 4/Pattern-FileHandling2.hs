main = do
    input <- readFile "input.txt"
    let n = read input :: Int
    let upper = [replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*' | i <- [0..n-1]]
    let lower = [replicate (i + 1) ' ' ++ replicate (2 * (n - i - 2) + 1) '*' | i <- [0..n-2]]
    writeFile "output.txt" (unlines (upper ++ lower))
