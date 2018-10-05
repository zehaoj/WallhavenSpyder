#_*_ coding:utf-8 _*_
#__date__='2018-08-27'
#爬取wallhaven上的的图片，支持自定义搜索关键词，自动爬取并该关键词下所有图片并存入本地电脑。
import os
import requests
import time
from progressbar import *
from lxml import etree
from threading import Thread

print('This software is for those who dig high-resolution wallpapers.\nBy inputing the keyword and pages you wanna download, breathtaking(or pantsdropping LOL) pictures will be automatically downloaded to your computer.\nIt will be located where this program located.\nDo enjoy! \n')
print('\n')
print('这个软件是为那些喜欢高像素壁纸的人服务的。通过输入关键词和想下载的页数，你就能将大量的高质量图片下到你的电脑中。默认存储地点是该程序所在地址。')
print('\n')
print('By J.Zehao\n')
print('\n')
print('-h : get help(获取帮助)\n')
print('\n')
print('-t : get tags(获取提示标签)\n')
print('\n')

tf = 1
while(tf == 1):
    keyWord = input(f"{'Please input the keywords that you want to download : '}")
    keyWord = keyWord.lower()
    print('\n')
    if keyWord == '-h':
        print('You can input keyword(tags) to download what you like. \nThen it will show how many images are there available for you to download.\ninput how many pages you wanna download. Normally, there will be 24 pics per page.')
        print('\n')
        print('你可以输入想下载的内容的关键词(标签)。软件将告诉你有多少张图片供下载。输入你想下载的页面数(一个页面有24张)')
        print('\n')
    elif keyWord == '-t':
        print('Here are some exemples: (rank by popularity, * is restricted content)')
        print('\n')
        print('这里是一些标签的例子(按热门度排行，标*的为限制级内容)')
        print('\n')
        print('women (People)')
        print('model (People)')
        print('nature (Nature)')
        print('brunette (People)')
        print('blonde (People)')
        print('landescape (Nature)')
        print('long hair (People)')
        print('anime (Anime&Manga)')
        print('anime girls (Anime&Manga)')
        print('ass (People)*')
        print('digital art (Art&Design)')
        print('women outdoors (People)')
        print('artwork (Art&Design)')
        print('trees (Nature)')
        print('looking at viewer (People)')
        print('boobs (People)*')
        print('video games (Entertainment)')
        print('leaves (Nature)')
        print('nude (People)*')
        print('portrait (Art&Design)')
        print('depth of field (Art&Design)\n')
    else:
        tf = 0

if keyWord == 'landescape':
    keyWord1 = 'id:711'
elif keyWord == 'anime':
   keyWord1 = 'id:1'
elif keyWord == 'ghost in the shell':
   keyWord1 = 'id:2'
elif keyWord == 'hatsune miku':
   keyWord1 = 'id:3'
elif keyWord == 'vocaloid':
   keyWord1 = 'id:4'
elif keyWord == 'anime girls':
   keyWord1 = 'id:5'
elif keyWord == 'destruction':
   keyWord1 = 'id:6'
elif keyWord == 'japan':
   keyWord1 = 'id:7'
elif keyWord == 'city':
   keyWord1 = 'id:10'
elif keyWord == 'interfaces':
   keyWord1 = 'id:11'
elif keyWord == 'cityscape':
   keyWord1 = 'id:13'
elif keyWord == 'science fiction':
   keyWord1 = 'id:14'
elif keyWord == 'futuristic':
   keyWord1 = 'id:15'
elif keyWord == 'city':
   keyWord1 = 'id:17'
elif keyWord == 'subway':
   keyWord1 = 'id:18'
elif keyWord == 'eve online':
   keyWord1 = 'id:19'
elif keyWord == 'river':
   keyWord1 = 'id:20'
elif keyWord == 'firefly':
   keyWord1 = 'id:21'
elif keyWord == 'gandalf':
   keyWord1 = 'id:22'
elif keyWord == 'j. r. r. tolkien':
   keyWord1 = 'id:23'
elif keyWord == 'john howe':
   keyWord1 = 'id:24'
elif keyWord == 'wizard':
   keyWord1 = 'id:27'
elif keyWord == 'the lord of the rings':
   keyWord1 = 'id:28'
elif keyWord == 'the hobbit':
   keyWord1 = 'id:29'
elif keyWord == 'triangle':
   keyWord1 = 'id:30'
elif keyWord == 'gray':
   keyWord1 = 'id:34'
elif keyWord == 'wall-e':
   keyWord1 = 'id:35'
elif keyWord == 'pixar animation studios':
   keyWord1 = 'id:36'
elif keyWord == 'nature':
   keyWord1 = 'id:37'
elif keyWord == 'water':
   keyWord1 = 'id:40'
elif keyWord == 'fish':
   keyWord1 = 'id:41'
elif keyWord == 'cat':
   keyWord1 = 'id:43'
elif keyWord == 'panties':
   keyWord1 = 'id:45'
elif keyWord == 'fire':
   keyWord1 = 'id:46'
elif keyWord == 'earth':
   keyWord1 = 'id:47'
elif keyWord == 'daft punk':
   keyWord1 = 'id:48'
elif keyWord == 'music':
   keyWord1 = 'id:49'
elif keyWord == 'galaxy':
   keyWord1 = 'id:51'
elif keyWord == 'metroid':
   keyWord1 = 'id:52'
elif keyWord == 'samus aran':
   keyWord1 = 'id:53'
elif keyWord == 'video games':
   keyWord1 = 'id:55'
elif keyWord == 'dinosaurs':
   keyWord1 = 'id:56'
elif keyWord == 'science fiction':
   keyWord1 = 'id:57'
elif keyWord == 'aliens':
   keyWord1 = 'id:58'
elif keyWord == 'monster hunter':
   keyWord1 = 'id:59'
elif keyWord == 'rathalos':
   keyWord1 = 'id:60'
elif keyWord == 'colorful':
   keyWord1 = 'id:61'
elif keyWord == 'tiger':
   keyWord1 = 'id:62'
elif keyWord == 'elves':
   keyWord1 = 'id:63'
elif keyWord == 'sunset':
   keyWord1 = 'id:64'
elif keyWord == 'dark souls':
   keyWord1 = 'id:67'
elif keyWord == 'pokémon':
   keyWord1 = 'id:68'
elif keyWord == 'mewtwo':
   keyWord1 = 'id:69'
elif keyWord == 'mechwarrior':
   keyWord1 = 'id:70'
elif keyWord == 'godzilla':
   keyWord1 = 'id:72'
elif keyWord == 'space invaders':
   keyWord1 = 'id:73'
elif keyWord == 'abstract':
   keyWord1 = 'id:74'
elif keyWord == 'cgi':
   keyWord1 = 'id:75'
elif keyWord == 'nujabes':
   keyWord1 = 'id:76'
elif keyWord == 'graffiti':
   keyWord1 = 'id:77'
elif keyWord == 'star wars':
   keyWord1 = 'id:78'
elif keyWord == 'spaceship':
   keyWord1 = 'id:79'
elif keyWord == 'monogatari series':
   keyWord1 = 'id:80'
elif keyWord == 'awesome face':
   keyWord1 = 'id:81'
elif keyWord == 'animals':
   keyWord1 = 'id:82'
elif keyWord == 'fox':
   keyWord1 = 'id:83'
elif keyWord == 'snow':
   keyWord1 = 'id:84'
elif keyWord == 'kill la kill':
   keyWord1 = 'id:85'
elif keyWord == 'clannad':
   keyWord1 = 'id:86'
elif keyWord == 'fujibayashi kyou':
   keyWord1 = 'id:87'
elif keyWord == 'fujibayashi ryou':
   keyWord1 = 'id:88'
elif keyWord == 'bioshock':
   keyWord1 = 'id:89'
elif keyWord == 'nebula':
   keyWord1 = 'id:90'
elif keyWord == 'wolf':
   keyWord1 = 'id:91'
elif keyWord == 'okami':
   keyWord1 = 'id:92'
elif keyWord == 'sword':
   keyWord1 = 'id:93'
elif keyWord == 'mythology':
   keyWord1 = 'id:96'
elif keyWord == 'gengar':
   keyWord1 = 'id:97'
elif keyWord == 'team fortress 2':
   keyWord1 = 'id:101'
elif keyWord == 'memes':
   keyWord1 = 'id:102'
elif keyWord == 'middle-earth: shadow of mordor':
   keyWord1 = 'id:104'
elif keyWord == 'eagle':
   keyWord1 = 'id:106'
elif keyWord == 'skeleton':
   keyWord1 = 'id:107'
elif keyWord == 'leaves':
   keyWord1 = 'id:108'
elif keyWord == 'photography':
   keyWord1 = 'id:109'
elif keyWord == 'riots':
   keyWord1 = 'id:110'
elif keyWord == 'police':
   keyWord1 = 'id:111'
elif keyWord == 'protestors':
   keyWord1 = 'id:112'
elif keyWord == 'heart':
   keyWord1 = 'id:113'
elif keyWord == 'brain':
   keyWord1 = 'id:114'
elif keyWord == 'trees':
   keyWord1 = 'id:115'
elif keyWord == 'lights':
   keyWord1 = 'id:118'
elif keyWord == 'depth of field':
   keyWord1 = 'id:119'
elif keyWord == 'wheat':
   keyWord1 = 'id:120'
elif keyWord == 'cave':
   keyWord1 = 'id:121'
elif keyWord == 'sunlight':
   keyWord1 = 'id:122'
elif keyWord == 'matoi ryuuko':
   keyWord1 = 'id:123'
elif keyWord == 'kingdom hearts':
   keyWord1 = 'id:126'
elif keyWord == 'poké balls':
   keyWord1 = 'id:128'
elif keyWord == 'nisekoi':
   keyWord1 = 'id:131'
elif keyWord == 'monogatari series':
   keyWord1 = 'id:132'
elif keyWord == 'megurine luka':
   keyWord1 = 'id:133'
elif keyWord == 'zatsune miku':
   keyWord1 = 'id:134'
elif keyWord == 'ia (vocaloid)':
   keyWord1 = 'id:135'
elif keyWord == 'touhou':
   keyWord1 = 'id:136'
elif keyWord == 'cirno':
   keyWord1 = 'id:137'
elif keyWord == 'tonari no kaibutsu':
   keyWord1 = 'id:138'
elif keyWord == 'oshino shinobu':
   keyWord1 = 'id:139'
elif keyWord == 'shingeki no kyojin':
   keyWord1 = 'id:140'
elif keyWord == 'aizawa inori':
   keyWord1 = 'id:141'
elif keyWord == 'chibi':
   keyWord1 = 'id:142'
elif keyWord == 'internet explorer':
   keyWord1 = 'id:143'
elif keyWord == 'tine kim':
   keyWord1 = 'id:144'
elif keyWord == 'christmas':
   keyWord1 = 'id:145'
elif keyWord == 'chinese clothing':
   keyWord1 = 'id:146'
elif keyWord == 'underwear':
   keyWord1 = 'id:147'
elif keyWord == 'thigh-highs':
   keyWord1 = 'id:148'
elif keyWord == 'kuroshitsuji':
   keyWord1 = 'id:149'
elif keyWord == 'k-on!':
   keyWord1 = 'id:150'
elif keyWord == 'nakano azusa':
   keyWord1 = 'id:151'
elif keyWord == 'hirasawa yui':
   keyWord1 = 'id:152'
elif keyWord == 'black rock shooter':
   keyWord1 = 'id:153'
elif keyWord == 'train station':
   keyWord1 = 'id:154'
elif keyWord == 'kudou asuka':
   keyWord1 = 'id:157'
elif keyWord == 'mikeneko':
   keyWord1 = 'id:158'
elif keyWord == 'sakamaki izayoi':
   keyWord1 = 'id:159'
elif keyWord == 'animal ears':
   keyWord1 = 'id:160'
elif keyWord == 'nekomimi':
   keyWord1 = 'id:161'
elif keyWord == 'tail':
   keyWord1 = 'id:162'
elif keyWord == 'short hair':
   keyWord1 = 'id:163'
elif keyWord == 'blonde':
   keyWord1 = 'id:164'
elif keyWord == 'blushing':
   keyWord1 = 'id:165'
elif keyWord == 'open mouth':
   keyWord1 = 'id:166'
elif keyWord == 'green eyes':
   keyWord1 = 'id:167'
elif keyWord == 'apron':
   keyWord1 = 'id:168'
elif keyWord == 'long hair':
   keyWord1 = 'id:169'
elif keyWord == 'dark hair':
   keyWord1 = 'id:170'
elif keyWord == 'sword art online':
   keyWord1 = 'id:171'
elif keyWord == 'braids':
   keyWord1 = 'id:172'
elif keyWord == 'swimwear':
   keyWord1 = 'id:173'
elif keyWord == 'bikini':
   keyWord1 = 'id:174'
elif keyWord == 'pink hair':
   keyWord1 = 'id:178'
elif keyWord == 'pink eyes':
   keyWord1 = 'id:181'
elif keyWord == 'brunette':
   keyWord1 = 'id:182'
elif keyWord == 'inumimi':
   keyWord1 = 'id:183'
elif keyWord == 'dragon':
   keyWord1 = 'id:184'
elif keyWord == 'pointed ears':
   keyWord1 = 'id:185'
elif keyWord == 'ponytail':
   keyWord1 = 'id:186'
elif keyWord == 'blue eyes':
   keyWord1 = 'id:188'
elif keyWord == 'fishing rod':
   keyWord1 = 'id:189'
elif keyWord == 'clouds':
   keyWord1 = 'id:190'
elif keyWord == 'inflatable rings':
   keyWord1 = 'id:192'
elif keyWord == 'kirigaya kazuto':
   keyWord1 = 'id:193'
elif keyWord == 'ayano keiko':
   keyWord1 = 'id:194'
elif keyWord == 'yuuki asuna':
   keyWord1 = 'id:195'
elif keyWord == 'senjougahara hitagi':
   keyWord1 = 'id:196'
elif keyWord == 'orange background':
   keyWord1 = 'id:197'
elif keyWord == 'simple background':
   keyWord1 = 'id:198'
elif keyWord == 'to aru kagaku no railgun':
   keyWord1 = 'id:199'
elif keyWord == 'misaka mikoto':
   keyWord1 = 'id:200'
elif keyWord == 'paris':
   keyWord1 = 'id:201'
elif keyWord == 'eiffel tower':
   keyWord1 = 'id:202'
elif keyWord == 'tilt shift':
   keyWord1 = 'id:203'
elif keyWord == 'golden ratio':
   keyWord1 = 'id:204'
elif keyWord == 'mathematics':
   keyWord1 = 'id:205'
elif keyWord == 'coffee':
   keyWord1 = 'id:206'
elif keyWord == 'movies':
   keyWord1 = 'id:208'
elif keyWord == 'fight club':
   keyWord1 = 'id:209'
elif keyWord == 'frozen (movie)':
   keyWord1 = 'id:210'
elif keyWord == 'kantai collection':
   keyWord1 = 'id:211'
elif keyWord == 'i-58 (kancolle)':
   keyWord1 = 'id:212'
elif keyWord == 'school swimsuits':
   keyWord1 = 'id:213'
elif keyWord == 'wo-class':
   keyWord1 = 'id:214'
elif keyWord == 'love live!':
   keyWord1 = 'id:215'
elif keyWord == 'hoshizora rin':
   keyWord1 = 'id:216'
elif keyWord == 'nishikino maki':
   keyWord1 = 'id:217'
elif keyWord == 'yazawa nico':
   keyWord1 = 'id:218'
elif keyWord == 'japanese clothes':
   keyWord1 = 'id:219'
elif keyWord == 'kimono':
   keyWord1 = 'id:220'
elif keyWord == 'shakira':
   keyWord1 = 'id:221'
elif keyWord == 'women':
   keyWord1 = 'id:222'
elif keyWord == 'rihanna':
   keyWord1 = 'id:223'
elif keyWord == 'panda':
   keyWord1 = 'id:224'
elif keyWord == 'sleeping':
   keyWord1 = 'id:225'
elif keyWord == 'green':
   keyWord1 = 'id:226'
elif keyWord == 'dota':
   keyWord1 = 'id:227'
elif keyWord == 'dota 2':
   keyWord1 = 'id:228'
elif keyWord == 'lina inverse':
   keyWord1 = 'id:229'
elif keyWord == 'valve corporation':
   keyWord1 = 'id:230'
elif keyWord == 'aperture laboratories':
   keyWord1 = 'id:231'
elif keyWord == 'breaking bad':
   keyWord1 = 'id:232'
elif keyWord == 'walter white':
   keyWord1 = 'id:233'
elif keyWord == 'summer glau':
   keyWord1 = 'id:234'
elif keyWord == '2pac':
   keyWord1 = 'id:235'
elif keyWord == 'brown':
   keyWord1 = 'id:236'
elif keyWord == 'troll face':
   keyWord1 = 'id:238'
elif keyWord == 'life':
   keyWord1 = 'id:239'
elif keyWord == 'white':
   keyWord1 = 'id:240'
elif keyWord == 'sun':
   keyWord1 = 'id:241'
elif keyWord == 'fez':
   keyWord1 = 'id:243'
elif keyWord == 'stars':
   keyWord1 = 'id:245'
elif keyWord == 'blueprints':
   keyWord1 = 'id:246'
elif keyWord == 'ford mustang':
   keyWord1 = 'id:247'
elif keyWord == 'muscle cars':
   keyWord1 = 'id:249'
elif keyWord == 'horse':
   keyWord1 = 'id:250'
elif keyWord == 'tuning':
   keyWord1 = 'id:252'
elif keyWord == 'yellow':
   keyWord1 = 'id:253'
elif keyWord == 'blurred':
   keyWord1 = 'id:254'
elif keyWord == 'engines':
   keyWord1 = 'id:256'
elif keyWord == 'shelby':
   keyWord1 = 'id:258'
elif keyWord == 'shelby gt':
   keyWord1 = 'id:259'
elif keyWord == 'rims':
   keyWord1 = 'id:260'
elif keyWord == 'lowrider':
   keyWord1 = 'id:261'
elif keyWord == 'facets':
   keyWord1 = 'id:262'
elif keyWord == 'burnout':
   keyWord1 = 'id:263'
elif keyWord == 'amber heard':
   keyWord1 = 'id:264'
elif keyWord == 'miley cyrus':
   keyWord1 = 'id:265'
elif keyWord == 'selena gomez':
   keyWord1 = 'id:266'
elif keyWord == 'ford':
   keyWord1 = 'id:267'
elif keyWord == 'stockings':
   keyWord1 = 'id:271'
elif keyWord == 'legs':
   keyWord1 = 'id:274'
elif keyWord == 'ass':
   keyWord1 = 'id:275'
elif keyWord == 'boobs':
   keyWord1 = 'id:276'
elif keyWord == 'big boobs':
   keyWord1 = 'id:277'
elif keyWord == 'nude':
   keyWord1 = 'id:278'
elif keyWord == 'nipples':
   keyWord1 = 'id:279'
elif keyWord == 'pink floyd':
   keyWord1 = 'id:280'
elif keyWord == 'blue':
   keyWord1 = 'id:282'
elif keyWord == 'purple':
   keyWord1 = 'id:283'
elif keyWord == 'glasses':
   keyWord1 = 'id:284'
elif keyWord == 'old car':
   keyWord1 = 'id:286'
elif keyWord == 'topless':
   keyWord1 = 'id:287'
elif keyWord == 'rainbows':
   keyWord1 = 'id:294'
elif keyWord == 'high heels':
   keyWord1 = 'id:296'
elif keyWord == 'lingerie':
   keyWord1 = 'id:297'
elif keyWord == 'tattoo':
   keyWord1 = 'id:299'
elif keyWord == 'bed':
   keyWord1 = 'id:300'
elif keyWord == 'lesbians':
   keyWord1 = 'id:301'
elif keyWord == 'the sopranos':
   keyWord1 = 'id:302'
elif keyWord == 'james gandolfini':
   keyWord1 = 'id:303'
elif keyWord == 'mafia':
   keyWord1 = 'id:304'
elif keyWord == 'television sets':
   keyWord1 = 'id:305'
elif keyWord == 'playboy':
   keyWord1 = 'id:306'
elif keyWord == 'sea':
   keyWord1 = 'id:307'
elif keyWord == 'mirror':
   keyWord1 = 'id:308'
elif keyWord == 'joker':
   keyWord1 = 'id:309'
elif keyWord == 'red':
   keyWord1 = 'id:311'
elif keyWord == 'black':
   keyWord1 = 'id:312'
elif keyWord == 'eyes':
   keyWord1 = 'id:313'
elif keyWord == 'car':
   keyWord1 = 'id:314'
elif keyWord == 'alone':
   keyWord1 = 'id:316'
elif keyWord == 'men':
   keyWord1 = 'id:317'
elif keyWord == 'cyborg':
   keyWord1 = 'id:318'
elif keyWord == 'stoya':
   keyWord1 = 'id:322'
elif keyWord == 'artwork':
   keyWord1 = 'id:323'
elif keyWord == 'birds':
   keyWord1 = 'id:324'
elif keyWord == 'the matrix':
   keyWord1 = 'id:325'
elif keyWord == 'frost':
   keyWord1 = 'id:326'
elif keyWord == 'winter':
   keyWord1 = 'id:327'
elif keyWord == 'mountains':
   keyWord1 = 'id:328'
elif keyWord == 'air gear':
   keyWord1 = 'id:329'
elif keyWord == 'manga':
   keyWord1 = 'id:330'
elif keyWord == 'leah xoxo':
   keyWord1 = 'id:331'
elif keyWord == 'zafira':
   keyWord1 = 'id:332'
elif keyWord == 'fallout':
   keyWord1 = 'id:333'
elif keyWord == 'fallout: new vegas':
   keyWord1 = 'id:334'
elif keyWord == 'nina dobrev':
   keyWord1 = 'id:335'
elif keyWord == 'rain':
   keyWord1 = 'id:336'
elif keyWord == 'night':
   keyWord1 = 'id:338'
elif keyWord == 'spotlights':
   keyWord1 = 'id:339'
elif keyWord == 'lindsey stirling':
   keyWord1 = 'id:341'
elif keyWord == 'violin':
   keyWord1 = 'id:342'
elif keyWord == 'hdr':
   keyWord1 = 'id:343'
elif keyWord == 'linux':
   keyWord1 = 'id:344'
elif keyWord == 'debian':
   keyWord1 = 'id:345'
elif keyWord == 'women with glasses':
   keyWord1 = 'id:347'
elif keyWord == 'jacket':
   keyWord1 = 'id:348'
elif keyWord == 'road':
   keyWord1 = 'id:349'
elif keyWord == 'modern':
   keyWord1 = 'id:350'
elif keyWord == 'vintage':
   keyWord1 = 'id:351'
elif keyWord == 'yin':
   keyWord1 = 'id:353'
elif keyWord == 'darker than black':
   keyWord1 = 'id:354'
elif keyWord == 'pornstar':
   keyWord1 = 'id:355'
elif keyWord == 'emmanuelle chriqui':
   keyWord1 = 'id:357'
elif keyWord == 'ice':
   keyWord1 = 'id:358'
elif keyWord == 'glaciers':
   keyWord1 = 'id:359'
elif keyWord == 'pakistan':
   keyWord1 = 'id:360'
elif keyWord == 'university':
   keyWord1 = 'id:362'
elif keyWord == 'mercedes-benz s class':
   keyWord1 = 'id:364'
elif keyWord == 'audi':
   keyWord1 = 'id:367'
elif keyWord == 'audi a6':
   keyWord1 = 'id:368'
elif keyWord == 'dark':
   keyWord1 = 'id:369'
elif keyWord == 'audi rs7':
   keyWord1 = 'id:370'
elif keyWord == 'spiderwebs':
   keyWord1 = 'id:371'
elif keyWord == 'water drops':
   keyWord1 = 'id:372'
elif keyWord == 'lara croft':
   keyWord1 = 'id:374'
elif keyWord == 'terrorist':
   keyWord1 = 'id:375'
elif keyWord == 'cyberpunk':
   keyWord1 = 'id:376'
elif keyWord == 'undead':
   keyWord1 = 'id:382'
elif keyWord == 'dracolich':
   keyWord1 = 'id:383'
elif keyWord == 'abs':
   keyWord1 = 'id:387'
elif keyWord == 'shorts':
   keyWord1 = 'id:388'
elif keyWord == 'bra':
   keyWord1 = 'id:390'
elif keyWord == 'selfies':
   keyWord1 = 'id:393'
elif keyWord == 'stacy keibler':
   keyWord1 = 'id:395'
elif keyWord == 'wwe':
   keyWord1 = 'id:396'
elif keyWord == 't-shirt':
   keyWord1 = 'id:397'
elif keyWord == 'lake':
   keyWord1 = 'id:398'
elif keyWord == 'matterhorn':
   keyWord1 = 'id:399'
elif keyWord == 'arch':
   keyWord1 = 'id:400'
elif keyWord == 'desert':
   keyWord1 = 'id:401'
elif keyWord == '3d':
   keyWord1 = 'id:403'
elif keyWord == 'internet':
   keyWord1 = 'id:405'
elif keyWord == 'nitroplus':
   keyWord1 = 'id:406'
elif keyWord == 'super sonico':
   keyWord1 = 'id:408'
elif keyWord == 'profile':
   keyWord1 = 'id:409'
elif keyWord == 'jessica biel':
   keyWord1 = 'id:410'
elif keyWord == 'katrina bowden':
   keyWord1 = 'id:411'
elif keyWord == 'gemma arterton':
   keyWord1 = 'id:412'
elif keyWord == 'miranda kerr':
   keyWord1 = 'id:413'
elif keyWord == 'kate beckinsale':
   keyWord1 = 'id:414'
elif keyWord == 'emma watson':
   keyWord1 = 'id:415'
elif keyWord == 'lily collins':
   keyWord1 = 'id:416'
elif keyWord == 'emily blunt':
   keyWord1 = 'id:417'
elif keyWord == 'ign':
   keyWord1 = 'id:418'
elif keyWord == 'eva mendes':
   keyWord1 = 'id:419'
elif keyWord == 'olivia wilde':
   keyWord1 = 'id:420'
elif keyWord == 'katy perry':
   keyWord1 = 'id:421'
elif keyWord == 'mila kunis':
   keyWord1 = 'id:422'
elif keyWord == 'lauren cohan':
   keyWord1 = 'id:423'
elif keyWord == 'model':
   keyWord1 = 'id:424'
elif keyWord == 'barbara palvin':
   keyWord1 = 'id:425'
elif keyWord == 'yvonne strahovski':
   keyWord1 = 'id:426'
elif keyWord == 'emmy rossum':
   keyWord1 = 'id:427'
elif keyWord == 'maggie q':
   keyWord1 = 'id:428'
elif keyWord == 'kate upton':
   keyWord1 = 'id:429'
elif keyWord == 'alexis bledel':
   keyWord1 = 'id:431'
elif keyWord == 'rachel mcadams':
   keyWord1 = 'id:432'
elif keyWord == 'kate mara':
   keyWord1 = 'id:433'
elif keyWord == 'karlie kloss':
   keyWord1 = 'id:434'
elif keyWord == 'opeth':
   keyWord1 = 'id:435'
elif keyWord == 'planet':
   keyWord1 = 'id:436'
elif keyWord == 'world':
   keyWord1 = 'id:437'
elif keyWord == 'samurai champloo':
   keyWord1 = 'id:438'
elif keyWord == 'sasha grey':
   keyWord1 = 'id:441'
elif keyWord == 'rock':
   keyWord1 = 'id:444'
elif keyWord == 'city':
   keyWord1 = 'id:445'
elif keyWord == 'sunglasses':
   keyWord1 = 'id:447'
elif keyWord == 'gymnastics':
   keyWord1 = 'id:448'
elif keyWord == 'asian':
   keyWord1 = 'id:449'
elif keyWord == 'quote':
   keyWord1 = 'id:451'
elif keyWord == 'shoes':
   keyWord1 = 'id:453'
elif keyWord == 'lamborghini':
   keyWord1 = 'id:454'
elif keyWord == 'lamborghini murcielago':
   keyWord1 = 'id:455'
elif keyWord == 'actor':
   keyWord1 = 'id:456'
elif keyWord == 'olga kurylenko':
   keyWord1 = 'id:457'
elif keyWord == 'bioshock infinite':
   keyWord1 = 'id:462'
elif keyWord == 'hills':
   keyWord1 = 'id:465'
elif keyWord == 'emma mae':
   keyWord1 = 'id:466'
elif keyWord == 'metal gear rising: revengeance':
   keyWord1 = 'id:467'
elif keyWord == 'sunny leone':
   keyWord1 = 'id:468'
elif keyWord == 'poland':
   keyWord1 = 'id:470'
elif keyWord == 'orange':
   keyWord1 = 'id:471'
elif keyWord == 'coast':
   keyWord1 = 'id:476'
elif keyWord == 'sports':
   keyWord1 = 'id:477'
elif keyWord == 'digital art':
   keyWord1 = 'id:479'
elif keyWord == 'cinema 4d':
   keyWord1 = 'id:480'
elif keyWord == 'anus':
   keyWord1 = 'id:482'
elif keyWord == 'valley':
   keyWord1 = 'id:483'
elif keyWord == 'rose':
   keyWord1 = 'id:485'
elif keyWord == 'face':
   keyWord1 = 'id:486'
elif keyWord == 'tv':
   keyWord1 = 'id:487'
elif keyWord == 'arrow':
   keyWord1 = 'id:488'
elif keyWord == 'dc comics':
   keyWord1 = 'id:489'
elif keyWord == 'moss':
   keyWord1 = 'id:490'
elif keyWord == 'lego':
   keyWord1 = 'id:491'
elif keyWord == 'miniatures':
   keyWord1 = 'id:492'
elif keyWord == 'lococycle':
   keyWord1 = 'id:493'
elif keyWord == 'twisted pixel':
   keyWord1 = 'id:494'
elif keyWord == 'i.r.i.s.':
   keyWord1 = 'id:495'
elif keyWord == 'pablo':
   keyWord1 = 'id:496'
elif keyWord == 'motorcycle':
   keyWord1 = 'id:497'
elif keyWord == 'fighting':
   keyWord1 = 'id:498'
elif keyWord == 'helicopters':
   keyWord1 = 'id:499'
else:
    keyWord1 = keyWord
    
class Spider():
    def __init__(self):        
        self.headers = {
        "User-Agent": "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
        }
        self.proxies = {
		"http": "http://61.178.238.122:63000",
	    }
        if (os.name == 'nt'):
            self.filePath = ('.\\'+ keyWord + "\\" ) # Here to change the location(Windows Edition)
        else:
            self.filePath = ('./'+ keyWord + "/" ) # Here to change the location(Mac Edition)
    def creat_File(self):
        filePath = self.filePath
        if not os.path.exists(filePath):
            os.makedirs(filePath)

    def get_pageNum(self):
        total = ""
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc").format(keyWord1)
        html = requests.get(url,headers = self.headers,proxies = self.proxies)
        selector = etree.HTML(html.text)
        pageInfo = selector.xpath('//header[@class="listing-header"]/h1[1]/text()')
        string = str(pageInfo[0])
        numlist = list(filter(str.isdigit,string))
        for item in numlist:
            total += item
        totalPagenum = int(total)
        return totalPagenum

    def main_fuction(self):
        self.creat_File()
        count = self.get_pageNum()
        print("We have found:{} images!\n".format(count))
        time.sleep(1)
        times = input(f"{'How many pages do you wanna download? (24 pics per page) '}")
        print('\n')
        print('Cool! ', 24 * int(times), 'photos will be downloaded for you. Sit tight, have a cup of coffee. It will finish in no time.')
        print('\n')
        print('好哒！', 24 * int(times), '张照片将很快下载到您的电脑上。稍安勿躁，很快就能下完！')
        print('\n')
        j = 1
        times = int(times)
        start = time.time()
        widgets = ['Progress: ',Percentage(), ' ', Bar('>'),' ', Timer()]
        pbar = ProgressBar(widgets=widgets, maxval=100).start()
        cc = 0
        for i in range(times):
            pic_Urls = self.getLinks(i+1)
            threads = []
            for item in pic_Urls:
                t = Thread(target = self.download, args = [item,j])
                t.start()
                threads.append(t)
                j += 1
               
            for t in threads:
                cc += 100/(24 * times)
                if cc > 100:
                    cc = 100
                t.join() 
                pbar.update(cc)
        pbar.finish()
        end = time.time()

    def getLinks(self,number):
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc&page={}").format(keyWord1,number)
        try:
            html = requests.get(url,headers = self.headers,proxies = self.proxies)
            selector = etree.HTML(html.text)
            pic_Linklist = selector.xpath('//a[@class="jsAnchor thumb-tags-toggle tagged"]/@href')
        except Exception as e:
            print(repr(e))
        return pic_Linklist

    def download(self,url,count):
        string = url.strip('/thumbTags').strip('https://alpha.wallhaven.cc/wallpaper/')
        html = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-' + string + '.jpg'
        pic_path = (self.filePath + keyWord + str(count) + '.jpg' )
        try:
            pic = requests.get(html,headers = self.headers)
            f = open(pic_path,'wb')
            f.write(pic.content)
            f.close()
        except Exception as e:
            print(repr(e))


spider = Spider()
spider.main_fuction()
print('This software will automatically exit in 5 seconds.\n')
print('本软件将于5秒后自动关闭。')
time.sleep(6)