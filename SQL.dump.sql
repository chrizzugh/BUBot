-- SQLite
SELECT id, question, answer, final_answer
FROM BUbotApp_questionsandanswers;

UPDATE BUbotApp_questionsandanswers
SET answer = "dr. aris j. ordoñez is the director of information & communication technology office.",
    final_answer = "Dr. Aris J. Ordoñez is the Director of Information & Communication Technology Office."
WHERE
    id = 99 
ORDER column_or_expression
LIMIT row_count OFFSET offset;

SELECT FINAL_ANSWER FROM BUbotApp_questionsandanswers WHERE ID=99;


UPDATE BUbotApp_questionsandanswers
SET answer = "there are the groups open for membership: bu magayon dance troupe, teatro bueño, bungcul singers, bu kuerdas (rondalla), bugkos ginikanan - indigenous music ensemble, gamelan and university marching band.",
    final_answer = "There are the groups open for membership: BU Magayon DANCE TROUPE, TEATRO BUeño, BUNGCUL Singers, BU KUERDAS (Rondalla), BUGKOS Ginikanan - indigenous music ensemble, gamelan and UNIVERSITY MARCHING BAND."
WHERE
    id = 543; 

UPDATE BUbotApp_questionsandanswers
SET question="Mr. Salvador M. Abiño."
WHERE
    id = 254; 

ALTER TABLE BUbotApp_questionsandanswers
  ADD static BOOLEAN NOT NULL;

UPDATE BUbotApp_questionsandanswers SET DYNAMIC = 1 WHERE id = 1; 