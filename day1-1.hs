import Data.List 
sortedPairwiseDistance :: [Int] -> [Int] -> Int
sortedPairwiseDistance xs ys = sum $ map absolutDistance $ zip (sort xs) (sort ys)

absolutDistance :: (Int,Int) ->  Int
absolutDistance (x,y) = abs (x-y)
