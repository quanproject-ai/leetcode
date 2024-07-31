-- problem 178: https://leetcode.com/problems/rank-scores/
SELECT
    S1.score,
    COUNT(S2.score) AS rank
FROM
    Scores S1, (select distinct score from Scores) S2
WHERE 
    S1.score <= S2.score
GROUP BY S1.id
Order by S1.score desc
-- #1 get all distinct scores
-- #2 count the total occurences as a distinct value to use as a ranking system
-- #3 Comparing with S2 table with the condition that S2 score beats S1 score:
    -- when an S1 score is beaten by S2 score, the total numbers of scores are coutned and are assigned as rank
    -- we group by S1.id is to show each score
-- Note: when you select two tables without a join statement, SQL performs a cartesian product where it combines
    -- every rows of 1st table and 2nd table together. It will contains all columns from both table.


-- Another solution
SELECT 
Score, 
convert(Rank,SIGNED) AS Rank 
FROM
    (SELECT 
    Score, 
    @rank:=CASE 
    WHEN Score=@previous THEN @rank -- if the current score is equal to previous, rank remain the same
    ELSE @rank+1 
    END AS Rank, 
    @previous:=Score -- update the current score to the variable @previous
    FROM Scores,
        (SELECT @previous:=-1,@rank:=0) AS initial
    ORDER BY Score DESC) A;  
-- @rank:= : this is user-defined math