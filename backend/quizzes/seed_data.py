ROUNDS = [
    {
        'round_number': 1,
        'title': 'General Knowledge Basics',
        'description': 'Fundamental GK questions',
        'questions': [
            {
                'text': 'What is the capital of France?',
                'choices': [('London', False), ('Berlin', False), ('Paris', True), ('Madrid', False)],
            },
            {
                'text': 'Which planet is known as the Red Planet?',
                'choices': [('Venus', False), ('Mars', True), ('Jupiter', False), ('Saturn', False)],
            },
            {
                'text': 'What is the largest ocean on Earth?',
                'choices': [('Atlantic Ocean', False), ('Indian Ocean', False), ('Arctic Ocean', False), ('Pacific Ocean', True)],
            },
            {
                'text': 'Who wrote Romeo and Juliet?',
                'choices': [('Charles Dickens', False), ('William Shakespeare', True), ('Jane Austen', False), ('Mark Twain', False)],
            },
            {
                'text': 'What is the chemical symbol for gold?',
                'choices': [('Go', False), ('Au', True), ('Ag', False), ('Gd', False)],
            },
            {
                'text': 'How many continents are there?',
                'choices': [('5', False), ('6', False), ('7', True), ('8', False)],
            },
            {
                'text': 'What is the tallest mountain in the world?',
                'choices': [('K2', False), ('Kangchenjunga', False), ('Mount Everest', True), ('Lhotse', False)],
            },
            {
                'text': 'Which country is known as the Land of the Rising Sun?',
                'choices': [('China', False), ('South Korea', False), ('Japan', True), ('Thailand', False)],
            },
            {
                'text': 'What is the currency of United Kingdom?',
                'choices': [('Euro', False), ('Pound Sterling', True), ('Dollar', False), ('Franc', False)],
            },
            {
                'text': 'Which animal is known as the King of the Jungle?',
                'choices': [('Tiger', False), ('Elephant', False), ('Lion', True), ('Gorilla', False)],
            },
        ],
    },
    {
        'round_number': 2,
        'title': 'Science & Nature',
        'description': 'Explore the wonders of science and the natural world',
        'questions': [
            {
                'text': 'What is the chemical symbol for water?',
                'choices': [('H2O', True), ('CO2', False), ('O2', False), ('NaCl', False)],
            },
            {
                'text': 'Which gas do plants absorb from the atmosphere during photosynthesis?',
                'choices': [('Oxygen', False), ('Carbon dioxide', True), ('Nitrogen', False), ('Hydrogen', False)],
            },
            {
                'text': 'What is the largest organ in the human body?',
                'choices': [('Liver', False), ('Brain', False), ('Skin', True), ('Heart', False)],
            },
            {
                'text': 'Which planet is closest to the Sun?',
                'choices': [('Venus', False), ('Earth', False), ('Mercury', True), ('Mars', False)],
            },
            {
                'text': 'What is the hardest natural substance on Earth?',
                'choices': [('Gold', False), ('Iron', False), ('Diamond', True), ('Quartz', False)],
            },
            {
                'text': 'Which part of a plant is mainly responsible for photosynthesis?',
                'choices': [('Root', False), ('Stem', False), ('Leaf', True), ('Flower', False)],
            },
            {
                'text': 'What force keeps planets in orbit around the Sun?',
                'choices': [('Magnetism', False), ('Gravity', True), ('Friction', False), ('Electricity', False)],
            },
            {
                'text': 'What is the chemical symbol for sodium?',
                'choices': [('So', False), ('Sd', False), ('Na', True), ('S', False)],
            },
            {
                'text': 'Which blood cells help fight infection?',
                'choices': [('Red blood cells', False), ('White blood cells', True), ('Platelets', False), ('Plasma cells', False)],
            },
            {
                'text': 'What is the approximate speed of light?',
                'choices': [('300,000 km/s', True), ('30,000 km/s', False), ('3,000 km/s', False), ('300 km/s', False)],
            },
        ],
    },
    {
        'round_number': 3,
        'title': 'History & Geography',
        'description': 'Journey through world history and discover places across the globe',
        'questions': [
            {
                'text': 'Which ancient civilization built the pyramids of Giza?',
                'choices': [('Romans', False), ('Greeks', False), ('Egyptians', True), ('Persians', False)],
            },
            {
                'text': 'In which year did World War II end?',
                'choices': [('1918', False), ('1939', False), ('1945', True), ('1950', False)],
            },
            {
                'text': 'Which is the longest river in the world?',
                'choices': [('Amazon', False), ('Nile', True), ('Yangtze', False), ('Mississippi', False)],
            },
            {
                'text': 'Which country has the largest land area?',
                'choices': [('China', False), ('Canada', False), ('United States', False), ('Russia', True)],
            },
            {
                'text': 'Who was the first President of the United States?',
                'choices': [('Abraham Lincoln', False), ('George Washington', True), ('Thomas Jefferson', False), ('John Adams', False)],
            },
            {
                'text': 'The Great Wall is located in which country?',
                'choices': [('Japan', False), ('India', False), ('China', True), ('Mongolia', False)],
            },
            {
                'text': 'Julius Caesar was a leader of which ancient civilization?',
                'choices': [('Egypt', False), ('Greece', False), ('Rome', True), ('Persia', False)],
            },
            {
                'text': 'What is the capital of Japan?',
                'choices': [('Beijing', False), ('Seoul', False), ('Bangkok', False), ('Tokyo', True)],
            },
            {
                'text': 'On which continent is the Sahara Desert located?',
                'choices': [('Asia', False), ('Africa', True), ('Australia', False), ('South America', False)],
            },
            {
                'text': 'Who reached the Americas in 1492?',
                'choices': [('Ferdinand Magellan', False), ('Christopher Columbus', True), ('Vasco da Gama', False), ('James Cook', False)],
            },
        ],
    },
    {
        'round_number': 4,
        'title': 'Literature & Language',
        'description': 'Test your knowledge of books, authors, and the English language',
        'questions': [
            {
                'text': 'Who wrote "Pride and Prejudice"?',
                'choices': [('Charlotte Bronte', False), ('Jane Austen', True), ('Emily Dickinson', False), ('Virginia Woolf', False)],
            },
            {
                'text': 'What is the first book in the Harry Potter series?',
                'choices': [("The Philosopher's Stone", True), ('The Chamber of Secrets', False), ('The Prisoner of Azkaban', False), ('The Goblet of Fire', False)],
            },
            {
                'text': 'Who wrote "The Old Man and the Sea"?',
                'choices': [('Mark Twain', False), ('Ernest Hemingway', True), ('F. Scott Fitzgerald', False), ('John Steinbeck', False)],
            },
            {
                'text': 'What is a group of lions called?',
                'choices': [('Herd', False), ('Pack', False), ('Pride', True), ('Flock', False)],
            },
            {
                'text': 'Which part of speech describes an action?',
                'choices': [('Noun', False), ('Adjective', False), ('Verb', True), ('Adverb', False)],
            },
            {
                'text': 'Who wrote the novel "1984"?',
                'choices': [('Aldous Huxley', False), ('George Orwell', True), ('Ray Bradbury', False), ('H. G. Wells', False)],
            },
            {
                'text': 'What is the opposite of the word "ancient"?',
                'choices': [('Old', False), ('Historic', False), ('Modern', True), ('Antique', False)],
            },
            {
                'text': 'Which literary device gives human qualities to non-human things?',
                'choices': [('Simile', False), ('Personification', True), ('Alliteration', False), ('Hyperbole', False)],
            },
            {
                'text': 'What is the plural of "child"?',
                'choices': [('Childs', False), ('Childes', False), ('Children', True), ('Childrens', False)],
            },
            {
                'text': 'Who wrote "The Jungle Book"?',
                'choices': [('Lewis Carroll', False), ('Rudyard Kipling', True), ('J. M. Barrie', False), ('Roald Dahl', False)],
            },
        ],
    },
    {
        'round_number': 5,
        'title': 'Sports & Games',
        'description': 'From football to chess, show off your sporting knowledge',
        'questions': [
            {
                'text': 'How many players from one team are on the field in a football (soccer) match?',
                'choices': [('9', False), ('10', False), ('11', True), ('12', False)],
            },
            {
                'text': 'The Wimbledon tournament is held in which sport?',
                'choices': [('Cricket', False), ('Tennis', True), ('Golf', False), ('Badminton', False)],
            },
            {
                'text': 'How many rings are on the Olympic flag?',
                'choices': [('4', False), ('5', True), ('6', False), ('7', False)],
            },
            {
                'text': 'Which country won the 2011 Cricket World Cup?',
                'choices': [('Australia', False), ('Sri Lanka', False), ('India', True), ('Pakistan', False)],
            },
            {
                'text': 'What is the maximum break in a standard game of snooker?',
                'choices': [('100', False), ('147', True), ('155', False), ('180', False)],
            },
            {
                'text': 'How many points is a touchdown worth in American football?',
                'choices': [('3', False), ('6', True), ('7', False), ('8', False)],
            },
            {
                'text': 'In chess, which piece can move in any direction?',
                'choices': [('Rook', False), ('Bishop', False), ('Knight', False), ('Queen', True)],
            },
            {
                'text': 'Which sport uses a shuttlecock?',
                'choices': [('Squash', False), ('Badminton', True), ('Table tennis', False), ('Tennis', False)],
            },
            {
                'text': 'How many holes are in a standard round of golf?',
                'choices': [('9', False), ('12', False), ('18', True), ('21', False)],
            },
            {
                'text': 'Which athlete is known as "Lightning Bolt"?',
                'choices': [('Carl Lewis', False), ('Usain Bolt', True), ('Michael Johnson', False), ('Tyson Gay', False)],
            },
        ],
    },
    {
        'round_number': 6,
        'title': 'Movies & Entertainment',
        'description': 'Lights, camera, action! Test your film and entertainment trivia',
        'questions': [
            {
                'text': 'Which movie features the character Jack Sparrow?',
                'choices': [('Titanic', False), ('Pirates of the Caribbean', True), ('The Mummy', False), ('Gladiator', False)],
            },
            {
                'text': 'Who directed "Jurassic Park"?',
                'choices': [('James Cameron', False), ('Steven Spielberg', True), ('Christopher Nolan', False), ('George Lucas', False)],
            },
            {
                'text': 'Which animated film features Simba?',
                'choices': [('Aladdin', False), ('Frozen', False), ('The Lion King', True), ('Madagascar', False)],
            },
            {
                'text': 'What is the name of the wizarding school in Harry Potter?',
                'choices': [('Narnia', False), ('Hogwarts', True), ('Xavier Academy', False), ('Beauxbatons', False)],
            },
            {
                'text': 'Which superhero is known as the Dark Knight?',
                'choices': [('Superman', False), ('Spider-Man', False), ('Batman', True), ('Iron Man', False)],
            },
            {
                'text': 'Who played Iron Man in the Marvel films?',
                'choices': [('Chris Evans', False), ('Robert Downey Jr.', True), ('Chris Hemsworth', False), ('Mark Ruffalo', False)],
            },
            {
                'text': 'Which movie series features the Force?',
                'choices': [('Star Trek', False), ('Star Wars', True), ('The Matrix', False), ('Dune', False)],
            },
            {
                'text': 'Which film had the highest worldwide box office gross by 2024?',
                'choices': [('Titanic', False), ('Avatar', True), ('Avengers: Endgame', False), ('The Lion King', False)],
            },
            {
                'text': 'Which actor voices Woody in Toy Story?',
                'choices': [('Tim Allen', False), ('Tom Hanks', True), ('Robin Williams', False), ('John Ratzenberger', False)],
            },
            {
                'text': 'What is the name of the snowman in Frozen?',
                'choices': [('Sven', False), ('Kristoff', False), ('Olaf', True), ('Hans', False)],
            },
        ],
    },
    {
        'round_number': 7,
        'title': 'Technology & Computers',
        'description': 'Put your digital know-how to the test',
        'questions': [
            {
                'text': 'What does CPU stand for?',
                'choices': [('Central Processing Unit', True), ('Computer Personal Unit', False), ('Central Program Utility', False), ('Control Processing Unit', False)],
            },
            {
                'text': 'Which company developed the Windows operating system?',
                'choices': [('Apple', False), ('Google', False), ('Microsoft', True), ('IBM', False)],
            },
            {
                'text': 'What does HTML stand for?',
                'choices': [('HyperText Markup Language', True), ('HighText Machine Language', False), ('HyperTool Multi Language', False), ('Home Tool Markup Language', False)],
            },
            {
                'text': 'Which device is mainly used to input text into a computer?',
                'choices': [('Monitor', False), ('Printer', False), ('Keyboard', True), ('Speaker', False)],
            },
            {
                'text': 'What does "WWW" stand for?',
                'choices': [('World Wide Web', True), ('Web Wide World', False), ('Wide World Web', False), ('World Web Wide', False)],
            },
            {
                'text': 'Which language is mainly used for styling web pages?',
                'choices': [('Python', False), ('CSS', True), ('SQL', False), ('Java', False)],
            },
            {
                'text': 'What is the binary equivalent of the decimal number 5?',
                'choices': [('100', False), ('101', True), ('110', False), ('111', False)],
            },
            {
                'text': 'Who is often called the father of the computer?',
                'choices': [('Alan Turing', False), ('Charles Babbage', True), ('Bill Gates', False), ('John von Neumann', False)],
            },
            {
                'text': 'What does RAM stand for?',
                'choices': [('Read Access Memory', False), ('Random Access Memory', True), ('Rapid Access Module', False), ('Runtime Active Memory', False)],
            },
            {
                'text': 'Which company created the iPhone?',
                'choices': [('Samsung', False), ('Nokia', False), ('Apple', True), ('Sony', False)],
            },
        ],
    },
    {
        'round_number': 8,
        'title': 'Music & Arts',
        'description': 'Discover famous artists, instruments, and musical legends',
        'questions': [
            {
                'text': 'Who painted the Mona Lisa?',
                'choices': [('Vincent van Gogh', False), ('Pablo Picasso', False), ('Leonardo da Vinci', True), ('Michelangelo', False)],
            },
            {
                'text': 'How many strings does a standard guitar have?',
                'choices': [('4', False), ('5', False), ('6', True), ('7', False)],
            },
            {
                'text': 'Which musical instrument has 88 keys?',
                'choices': [('Organ', False), ('Piano', True), ('Accordion', False), ('Harpsichord', False)],
            },
            {
                'text': 'Who composed "The Four Seasons"?',
                'choices': [('Mozart', False), ('Beethoven', False), ('Antonio Vivaldi', True), ('Bach', False)],
            },
            {
                'text': 'Salvador Dali is associated with which art movement?',
                'choices': [('Cubism', False), ('Surrealism', True), ('Impressionism', False), ('Realism', False)],
            },
            {
                'text': 'What is the national instrument of Scotland?',
                'choices': [('Violin', False), ('Flute', False), ('Bagpipes', True), ('Harp', False)],
            },
            {
                'text': 'Who is known as the "King of Pop"?',
                'choices': [('Elvis Presley', False), ('Michael Jackson', True), ('Prince', False), ('Freddie Mercury', False)],
            },
            {
                'text': 'Which artist famously cut off part of his ear?',
                'choices': [('Claude Monet', False), ('Vincent van Gogh', True), ('Paul Cezanne', False), ('Edvard Munch', False)],
            },
            {
                'text': 'How many lines are in a standard musical staff?',
                'choices': [('4', False), ('5', True), ('6', False), ('7', False)],
            },
            {
                'text': 'Which member of The Beatles played bass?',
                'choices': [('John Lennon', False), ('Paul McCartney', True), ('George Harrison', False), ('Ringo Starr', False)],
            },
        ],
    },
    {
        'round_number': 9,
        'title': 'Food & Culture',
        'description': 'A tasty tour of dishes, traditions, and cultures around the world',
        'questions': [
            {
                'text': 'Which country is famous for sushi?',
                'choices': [('Thailand', False), ('Japan', True), ('China', False), ('Korea', False)],
            },
            {
                'text': 'What is the main ingredient in guacamole?',
                'choices': [('Tomato', False), ('Avocado', True), ('Cucumber', False), ('Pepper', False)],
            },
            {
                'text': 'Which spice is the most expensive in the world by weight?',
                'choices': [('Cinnamon', False), ('Vanilla', False), ('Saffron', True), ('Cardamom', False)],
            },
            {
                'text': 'Which Italian dish is made with layers of pasta, meat sauce, and cheese?',
                'choices': [('Risotto', False), ('Lasagna', True), ('Carbonara', False), ('Pizza', False)],
            },
            {
                'text': 'Which fruit is known as the "king of fruits" in Southeast Asia?',
                'choices': [('Mango', False), ('Durian', True), ('Papaya', False), ('Jackfruit', False)],
            },
            {
                'text': 'What is the primary ingredient in bread?',
                'choices': [('Rice', False), ('Flour', True), ('Sugar', False), ('Milk', False)],
            },
            {
                'text': 'Diwali is a major festival celebrated mainly in which country?',
                'choices': [('China', False), ('Japan', False), ('India', True), ('Egypt', False)],
            },
            {
                'text': 'What is the traditional Japanese rice wine called?',
                'choices': [('Soju', False), ('Sake', True), ('Makgeolli', False), ('Shaoxing', False)],
            },
            {
                'text': 'Which vitamin is found in citrus fruits?',
                'choices': [('Vitamin A', False), ('Vitamin B12', False), ('Vitamin C', True), ('Vitamin D', False)],
            },
            {
                'text': 'Which city is famous for the Eiffel Tower and French cuisine?',
                'choices': [('Rome', False), ('Madrid', False), ('Paris', True), ('Berlin', False)],
            },
        ],
    },
    {
        'round_number': 10,
        'title': 'Brain Teasers & Mixed Trivia',
        'description': 'The final challenge: riddles, logic, and mixed trivia',
        'questions': [
            {
                'text': 'What comes next in the sequence: 2, 4, 8, 16, ...?',
                'choices': [('20', False), ('24', False), ('32', True), ('64', False)],
            },
            {
                'text': 'How many months of the year have 28 days?',
                'choices': [('1', False), ('2', False), ('6', False), ('All 12', True)],
            },
            {
                'text': 'If you rearrange the letters of "LISTEN", which word do you get?',
                'choices': [('SILENT', True), ('TINSEL', False), ('ENLIST', False), ('INLETS', False)],
            },
            {
                'text': 'What has keys but cannot open locks?',
                'choices': [('A map', False), ('A piano', True), ('A door', False), ('A safe', False)],
            },
            {
                'text': 'What is half of 2 plus 2?',
                'choices': [('1', False), ('2', False), ('3', True), ('4', False)],
            },
            {
                'text': 'Which is heavier: a kilogram of feathers or a kilogram of iron?',
                'choices': [('Feathers', False), ('Iron', False), ('They weigh the same', True), ('It depends on the weather', False)],
            },
            {
                'text': 'What number does the Roman numeral "IX" represent?',
                'choices': [('4', False), ('6', False), ('9', True), ('11', False)],
            },
            {
                'text': 'What has to be broken before you can use it?',
                'choices': [('A promise', False), ('An egg', True), ('A rule', False), ('A window', False)],
            },
            {
                'text': 'If today is Monday, what day will it be in 3 days?',
                'choices': [('Wednesday', False), ('Thursday', True), ('Friday', False), ('Sunday', False)],
            },
            {
                'text': 'What is the next prime number after 7?',
                'choices': [('8', False), ('9', False), ('10', False), ('11', True)],
            },
        ],
    },
]
