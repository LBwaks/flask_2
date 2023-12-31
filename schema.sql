DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Quizes;
DROP TABLE IF EXISTS Results;

CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
CREATE TABLE Students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL
    

    -- FOREIGN KEY (user_id) REFERENCES user (id)
);
CREATE TABLE Quizes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- user_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    questions TEXT NOT NULL,
    date_given DATE NOT NULL
    -- complete BOOLEAN NOT NULL DEFAULT FALSE,

    -- FOREIGN KEY (user_id) REFERENCES user (id)
);
CREATE TABLE Results(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    quiz_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    -- complete BOOLEAN NOT NULL DEFAULT FALSE,

    FOREIGN KEY (student_id) REFERENCES Students (id),
    FOREIGN KEY (quiz_id) REFERENCES Quizes (id)
);