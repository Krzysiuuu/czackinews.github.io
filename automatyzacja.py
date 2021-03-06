a = open("articles/abc.txt")

file = str(a.read())

lines = file.split('\n')

key_words = ['subtitle: ', 'title: ',
             'date: ', 'tags: ', 'introduction: ']

bebechy_artykulu = {}

for line in lines:
    for key_word in key_words:
        if key_word in line:
            fixed_line = line.replace(key_word, '')
            bebechy_artykulu[key_word] = fixed_line
            file = file.replace(line, '')
            break

file = file.replace('\n', '')
bebechy_artykulu['article: '] = file

print(bebechy_artykulu)


article_template = """
<html>
	<head>
		<title>{title}</title>
		<meta charset="UTF-8" lang="pl">
		<link rel="stylesheet" type="text/css" href="main.css">
        <link rel="shortcut icon" href="icon.png">
        <meta property="og: image" content="images/a3c1a.jpg">
	</head>
	<body>
		<ul>
            <div id="my_links">
                <a href="index.html"><div class="title"><li class="title"><img src="images/logo_transparent.png" id="logo_transparent"/></li></div></a>
                <div id="menu_option">
                <a href="najnowsze.html"><li>Najnowsze</li></a>
                <a href="czacki.html"><li>Życie Czackiewicza</li></a>
                <a href="polska_i_swiat.html"><li>Polska i świat</li></a>
                <a href="nauka_i_technologia.html"><li>Nauka i Technologia</li></a>
                <a href="rozrywka.html"><li>Rozrywka</li></a>
                <a href="sport.html"><li>Sport</li></a>
                </div>
            </div>
		</ul>
        <a id="scroll" onclick="myFunction()" href="javascript:void(0);"><img src="scroll.png" id="scroll_picture"/></a>
        
        <img src="images/easter-a.jpg" alt="newspaper" id="main_newspaper" padding="0px"></img>
		    <div id="welcome">
                <h1 id="main_text_white" color="white">{title}</h1>
                <h2 id="second_text_white">{subtitle}</h2>
            </div>
        
        <!--
        <div id="author">
            <img src="authors/hubert.jpg" id="author_photo" style="vertical-align: middle;">
            <div id="author_text">
                <p id="about_author">O autorze</p>
                <h3 id="author_name">KR</h3>
                <p id="author_description">
                    Znany influencer, filantrop, biznesmen, geniusz, przywódca, złoty medalista, 
                    prawnik, pszczelarz, kartograf, prezenter, dziennikarz, coach, trener, czarodziej, winiarz, rolnik, 
                    bóg i masażysta. Interesuje się wędkarstwem. Szlachetnie urodzony.
                </p>
            </div>
        -->
            
        </div>
        <div id="main_part">
            <p id="textabc">
                <div id=tyt_art>
                <strong>{introduction}</strong><br><br></div>
<div id=artykuł>
    
{article} <br><br>
            </p></div>
        
        </div>
        </div>

        <footer>
            <p id="footer">&copy Czacki News 2020</p>
        </footer>
	</body>
</html>
"""

article_finished = article_template.format(title=bebechy_artykulu['title: '],
                        subtitle=bebechy_artykulu['subtitle: '],
                        introduction=bebechy_artykulu['introduction: '],
                        article=bebechy_artykulu['article: '])


print('\n')
print('\n')
print('\n')
print(article_finished)

article_file = open('bebech.html', 'wb')
article_file.write(article_finished.encode())
article_file.close()
a.close()
