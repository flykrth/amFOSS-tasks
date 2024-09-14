main = do
    putStrLn "Enter a number: "
    input <- getLine
    let n = read input :: Int
    putStr $ unlines $ diamond n

diamond :: Int -> [String]
diamond n = upper ++ lower
    where
        upper = [replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*' | i <- [0..n-1]]
        lower = [replicate (i + 1) ' ' ++ replicate (2 * (n - i - 2) + 1) '*' | i <- [0..n-2]]
