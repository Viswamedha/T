# 8 functions 120 line limit
# 1st function Keep adding until they enter 0 //
# 2nd function Keep multiplying until they enter 0 //
# 3rd and 4th login system, sign up system /
# 5th online find a word list, enter 1 letter pick a random word starting with it
# 6th a to the power of b no power symbols, must be done manually
# 7th all of the returns in 1-6 functions print them out im one line
# 8th seperate file running 1-7 //
def adder():
    num1 = 0
    num2 = int(input("Please enter another number. "))
    while num2 != 0:
        num1 = num1 + num2
        num2 = int(input("Please enter another number. "))
    return str(num1)
def multiplier():
    num1 = 1
    num2 = 1
    while num2 != 0:
        num1 = num1 * num2
        num2 = int(input("Please enter another number. "))
    return str(num1)

def wordList():
    words = ("rice","bridge","perfectly","trail","settlers","weight","needs","rubbed","stiff","her","lungs","famous","mighty","score","passage","political","see","needle","please","familiar","track","paragraph","important","give","start","spread","coach","command","camera","definition","horse","roll","clothes","within","gentle","flight","favorite","kept","variety","harder","corner","accident","young","signal","receive","make","speech","faster","draw","stage","successful","stomach","aware","slowly","jet","cutting","off","society","empty","due","wool","happen","whom","question","brought","blanket","atom","planned","journey","money","both","flame","gun","crack","teeth","north","gravity","average","rhyme","develop","personal","report","package","monkey","twenty","anywhere","so","bigger","fort","vast","standard","lady","your","group","understanding","chief","accurate","instance","honor","simple","fill","heat","instrument","nature","cake","tower","held","hung","house","more","barn","having","compass","route","truth","effect","home","to","but","actual","upper","saved","ran","brick","below","although","extra","doubt","triangle","entirely","bet","club","reader","bright","office","chamber","calm","take","usual","stronger","bone","belt","giant","national","except","divide","nearer","happy","occur","melted","foot","bit","species","cost","sold","ruler","tide","pocket","motion","wonder","old","greater","four","moment","oil","replace","solution","fastened","tool","nuts","life","official","chair","hospital","fully","exist","nails","satisfied","describe","dirty","be","action","paper","team","numeral","stranger","door","business","fact","area","buried","talk","wife","troops","helpful","shine","probably","force","top","fur","finest","thy","realize","hidden","press","somehow","cloth","source","nest","condition","manufacturing","chapter","like","leader","catch","gold","original","interior","everybody","smell","strong","sense","neighborhood","anyone","there","frequently","whether","facing","leaf","laid","in","composed","song","pet","comfortable","require","dish","wing","stairs","final","opportunity","teach","vessels","vote","just","path","lonely","military","above","box","join","lot","cast","bell","news","prize","guard","cup","fine","test","fun","throw","steel","luck","slipped","rope","floor","pass","tin","salmon","trouble","chain","thrown","type","attention","throat","radio","string","his","usually","provide","twice","sudden","coming","quite","circle","independent","income","husband","should","dried","social","statement","represent","customs","market","arrive","sun","congress","eleven","escape","judge","active","plates","meal","musical","purpose","enjoy","still","as","sat","fallen","beauty","manner","rock","fog","offer","fast","exciting","leave","completely","past","breathing","measure","late","industry","perhaps","major","brave","date","primitive","rest","correct","have","limited","came","atomic","finish","detail","name","any","zoo","sail","direct","whispered","softly","positive","toy","dear","beautiful","finger","fight","locate","class","fuel","send","line","prove","town","forty","dream","syllable","forgot","those","believed","space","nine","deal","climb","present","printed","could","lay","language","anybody","continued","adjective","day","create","plenty","act","spoken","quick","itself","cloud","cow","add","possible","wire","element","pole","cross","unusual","pour","allow","guess","tired","yes","closely","law","up","produce","fox","land","sad","easier","plain","level","function","come","railroad","huge","wish","done","satellites","teacher","sides","that","oxygen","cat","light","speed","pot","show","taught","round","whistle","sport","wore","general","ill","visitor","call","wood","college","appropriate","use","atmosphere","excited","history","rod","ready","either","additional","hungry","chicken","large","health","branch","battle","left","road","letter","ought","zero","spider","rate","none","lake","studying","hot","burn","slave","everything","yard","owner","whale","carry","airplane","pleasure","movie","range","central","instead","share","school","little","must","shelter","blank","captured","mysterious","eat","material","reason","therefore","floating","sell","shore","difference","grew","stove","youth","has","build","available","afraid","process","hide","least","disappear","practical","rays","voyage","football","mean","underline","lucky","compare","tune","several","position","select","tone","noted","early","amount","bare","pale","nor","pilot","careful","evidence","told","exact","tried","lost","theory","wet","excellent","found","universe","organization","each","grass","camp","bee","because","chest","roof","around","drink","let","means","fruit","laugh","western","fish","seeing","express","possibly","bear","tent","subject","nose","setting","cannot","building","victory","shoulder","policeman","constantly","putting","degree","television","die","him","plant","individual","vertical","fifteen","fireplace","wear","pond","look","instant","person","cool","pleasant","furniture","coast","sent","last","porch","particles","getting","thou","refer","nothing","enemy","which","idea","hello","motor","silence","swim","world","transportation","farm","its","making","yesterday","audience","development","fire","planet","seven","alike","merely","tape","aboard","corn","stream","warm","she","border","balance","forest","tax","soil","remain","other","brain","attack","too","it","drew","mathematics","perfect","belong","nervous","also","plate","product","topic","unknown","through","common","silly","program","shallow","entire","eaten","declared","selection","system","shadow","chart","does","after","wait","elephant","wrong","whenever","desert","importance","put","wrapped","six","you","donkey","expression","poor","station","best","third","mine","wild","stick","again","month","horn","married","machine","bean","nearly","dull","neighbor","do","foreign","earth","without","women","try","feature","brief","dark","man","will","tomorrow","doll","sharp","pupil","mouth","heard","fresh","ball","lovely","somebody","result","key","tube","good","raw","shoot","factory","colony","full","appearance","stopped","parent","fall","these","everyone","height","bicycle","shade","east","pictured","tears","wolf","met","remember","safe","lift","meant","human","model","color","some","volume","dig","throughout","though","why","desk","lips","couple","tight","shown","gather","ranch","weak","burst","forgotten","father","property","inch","observe","car","along","help","glad","orbit","cheese","wheel","city","adventure","thing","form","suppose","once","pure","breath","lose","got","finally","fewer","younger","involved","bat","listen","birth","collect","speak","total","waste","shinning","ever","was","across","combine","dug")
    letter = str(input("Enter a letter, I will find you a random word beggining with that. "))
    wordCounter = 0
    while wordCounter < len(words):
        wordLetter = words[wordCounter]
        if letter == wordLetter[0]:
            words = wordLetter
            return str(words)
        else:
            wordCounter = wordCounter + 1
def manualSquarer(num1, num2):
   
    num2 = num2 - 1
    num3 = num1
    while num2 != 0:
        num1 = num1 * num3
        num2 = num2 - 1
    return str(num1)
def printer(one, two, three, four):
    print ("Here are the results " + one + ", " + two + ", " + three + ", " + four)
    return
f = wordList()
print(f)
