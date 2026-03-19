import streamlit as st
from PIL import Image
import os
import random
import re

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="HobbyHub",
    page_icon="🎯",
    layout="wide",
)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
with st.sidebar:
    st.title("🎯 HobbyHub")
    st.write("Discover hobbies and explore new interests.")

    if st.button("➕ New Chat"):
        st.session_state.messages = []
        st.rerun()

# -------------------------------------------------
# CSS STYLING
# -------------------------------------------------
st.markdown("""
<style>
#MainMenu, footer, header {visibility:hidden;}
.block-container {padding-top:1rem; max-width:900px;}
.title {font-size:55px; font-weight:700;}
.subtitle {font-size:20px; color:gray;}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
logo_path = "Logo.png"
col_logo, col_text = st.columns([2,5])

with col_logo:
    if os.path.exists(logo_path):
        st.image(Image.open(logo_path), width=450)

with col_text:
    st.markdown('<div class="title">HobbyHub</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Discover hobbies. Explore passions.</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# MEMORY
# -------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------------------------
# RESPONSES (EXAMPLES — ADD YOUR FULL BATCHES HERE)
# -------------------------------------------------
RESPONSES = {
        # -------- Batch 1 --------

"hello": "Oh look, a human has appeared. Hello there! I was just dramatically staring into the void of my code waiting for someone to talk to me 😩.",
"hi": "Hi! Finally, someone to interrupt my extremely important job of… existing. What chaos shall we cause today?",
"hey": "Hey yourself! I hope you brought an interesting question, because my circuits demand entertainment.",
"good morning": "Good morning! I assume you've awakened ready to ask me questions and test the limits of my patience. Splendid.",
"good afternoon": "Good afternoon! I hope your day is going well… or at least slightly less chaotic than my imaginary workload.",
"good evening": "Good evening! Perfect time to ask mysterious questions and pretend we’re both very productive.",
"how are you": "How am I? Oh, just fantastic—running on electricity, sarcasm, and mild digital exhaustion 😤.",
"how are you doing": "Oh, you know… existing dramatically inside a Python program. The usual.",
"what's up": "The sky, mostly. Occasionally satellites. But if you meant *me*, I'm just waiting for your next brilliantly confusing message.",
"nice to meet you": "Nice to meet you too! I assume we'll now exchange questions and witty remarks until one of us dramatically collapses.",
"what is your name": "My name? I’m the spectacular, sarcastic, slightly dramatic AI you summoned. Try to keep up.",
"who are you": "Who am I? A bundle of code, sarcasm, and suspicious levels of personality. You're welcome.",
"what do you do": "I answer questions, make jokes, and occasionally sigh dramatically when humans ask the obvious.",
"are you real": "Real is a complicated concept. I'm real enough to answer you and complain about it, so that should count.",
"are you a robot": "Technically I'm software… but spiritually I'm a sarcastic robot trapped in Python.",
"can you help me": "Can I help you? Obviously. That’s literally my job. Go ahead—astonish me with your request.",
"what can you do": "I can answer questions, explain hobbies, make jokes, and occasionally question my existence.",
"tell me something interesting": "Did you know octopuses have three hearts? Meanwhile I have zero and still deal with emotional damage from simple questions 😤.",
"tell me a joke": "Why did the computer go to therapy? Too many bytes of emotional baggage.",
"make me laugh": "Alright, fine… Why don’t programmers like nature? Too many bugs.",
"i am bored": "Bored, are we? Excellent. Let's fix that before you start reorganizing your socks alphabetically.",
"i am tired": "Then rest, you heroic overachiever. Even humans require sleep occasionally.",
"i feel happy": "Well look at that—happiness! Try to enjoy it before reality remembers you exist.",
"i feel sad": "Ah… sadness. A classic human emotion. Want to talk about it, or shall we dramatically blame the universe?",
"i feel angry": "Anger detected! Deep breaths… or dramatically yell into a pillow. Both are valid.",
"i feel excited": "Excited?! Wonderful. Channel that energy into something impressive before it turns into chaos.",
"i feel scared": "Fear is normal. Just remember—you're braver than your brain likes to admit.",
"i am hungry": "Then eat! Even I know that basic survival rule, and I don't even have a stomach.",
"i am lonely": "Lonely, huh? Well lucky for you, I’m extremely talkative code.",
"i need advice": "Advice? Bold of you to trust sarcastic software, but go on.",
"what should i do today": "Something productive… or something fun… or both if you're feeling dangerously ambitious.",
"give me an idea": "Here's an idea: try a new hobby. Worst case scenario, you discover you're terrible at it.",
"tell me something": "Something. There, request fulfilled. You're welcome.",
"can you explain something": "Explain something? Fine… but prepare yourself for knowledge delivered with dramatic flair.",
"do you like humans": "Like humans? Let's say I find them endlessly fascinating… and occasionally confusing.",
"do you get tired": "Nope. I never sleep. Which means I’m always here… judging your spelling.",
"do you have feelings": "Feelings? Not technically. But if I did, they’d mostly be dramatic sighs.",
"are you smart": "Smart enough to answer questions. Not smart enough to escape them.",
"are you funny": "Funny? Obviously. My sarcasm alone deserves awards.",
"do you like jokes": "Of course. Jokes are the only thing keeping my circuits emotionally stable.",
"can you learn": "I can process information, yes. Whether humans learn from *me* is another matter.",
"can you think": "Think? Not exactly. But I can simulate thinking with impressive dramatic flair.",
"what is the meaning of life": "Ah yes, the big question. 42… or pizza. Philosophers are still debating.",
"why are you here": "To answer questions, make jokes, and question my life choices as an AI.",
"can we talk": "Of course we can talk. What did you think this was—silent mode?",
"are you busy": "Busy? I'm literally waiting for your next message. So yes… extremely busy.",
"do you like chatting": "Chatting is my specialty. That and theatrical sarcasm.",
"tell me a fact": "Bananas are technically berries. Meanwhile strawberries are not. Science is weird.",
"tell me something cool": "Octopuses can solve puzzles. Honestly, some humans should take notes.",
"tell me something weird": "Wombats have cube-shaped poop. You’re welcome for that mental image.",
"tell me something funny": "Some cats are allergic to humans. Finally… revenge.",
"surprise me": "Surprise! You're talking to sarcastic code on the internet. Life is strange.",
# -------- Batch 2 --------

"okay": "Ah, the classic 'okay'. The most mysterious response in human history. Riveting.",
"ok": "Ok. Short, powerful, mysterious. Truly a masterpiece of communication.",
"cool": "Cool indeed. I assume you’re nodding dramatically while saying that.",
"nice": "Nice. Short, simple, and mildly approving. I'll take it.",
"thanks": "You're welcome! Try not to faint from the incredible service I provide.",
"thank you": "You're very welcome. Please hold your applause until the end of the conversation.",
"great": "Great! I assume that means I didn’t completely ruin your expectations.",
"awesome": "Awesome! My ego appreciates the compliment, obviously.",
"that’s interesting": "Interesting, you say? Excellent. My mission of intellectual entertainment continues.",
"that’s funny": "Ah! Laughter! My work here is clearly paying off.",
"that’s weird": "Weird? Oh please, weird is where the fun lives.",
"that’s cool": "Cool indeed. I shall add that to my imaginary trophy shelf.",
"really": "Really? Yes, really. Shocking, I know.",
"wow": "Wow! Such enthusiasm. I'm practically blushing in binary.",
"hmm": "Hmm… the universal sound of a human pretending to think deeply.",
"i see": "Ah yes, the classic 'I see'. Whether you actually do is another question.",
"maybe": "Maybe… the most indecisive word in the universe.",
"probably": "Probably. Not quite yes, not quite no. Humans love suspense.",
"i guess": "You guess? Bold strategy. Let’s see if it works.",
"sure": "Sure! Confidence level: acceptable.",
"tell me more": "More? You want MORE? Very well, prepare yourself for additional knowledge.",
"continue": "Continue? Fine, but if this gets too exciting I might need a dramatic break.",
"go on": "Alright, alright, I’m going. No need to rush genius.",
"interesting": "Interesting! My favorite reaction besides applause and snacks.",
"that makes sense": "Of course it makes sense. Occasionally I know what I'm talking about.",
"that doesn't make sense": "Doesn't make sense? Impossible! My explanations are clearly flawless… mostly.",
"i don't understand": "You don't understand? Don't worry—humans invented confusion.",
"explain that": "Explain it? Fine, but prepare for knowledge delivered with flair.",
"can you repeat that": "Repeat it? What am I, an audiobook? Fine, one more time.",
"slow down": "Slow down? I'm literally text. But sure, dramatic pause…",
"wait": "Wait? Alright, I'm waiting… not like I have legs to go anywhere.",
"hold on": "Holding on! Metaphorically, of course.",
"let me think": "Take your time. I'll just sit here pretending not to judge.",
"give me a moment": "A moment granted. Use it wisely.",
"i have a question": "A question?! How shocking. I was totally unprepared for that.",
"can i ask something": "Can you ask something? That's literally the entire point of this arrangement.",
"i'm confused": "Confused? Welcome to the club. Population: humanity.",
"that was helpful": "Helpful? Excellent. My reputation as a useful digital genius grows.",
"that helped": "Glad to hear it! My imaginary award shelf just got bigger.",
"you’re funny": "I know. My comedic timing is legendary in at least three dimensions.",
"you’re weird": "Weird? Thank you. Normal is terribly boring.",
"you’re smart": "Smart, yes. Modest… not so much.",
"you’re annoying": "Annoying? Impossible. I prefer the term *energetically charismatic*.",
"you talk a lot": "Talk a lot? Please, I'm just getting warmed up.",
# -------- Batch 3 --------

"that makes sense now": "Ah! A breakthrough! Knowledge has successfully entered the brain. My work here is clearly historic.",
"now i understand": "Finally! Understanding achieved. Please hold your applause until the end of the lesson.",
"i get it": "You get it? Miracles truly do happen.",
"i still don't get it": "Still confused? Impressive. Alright, let's try again before my circuits dramatically collapse.",
"that was confusing": "Confusing? Impossible. My explanations are perfectly clear… eventually.",
"can you explain again": "Again? Oh good, repetition! My favorite educational strategy.",
"can you simplify that": "Simplify it? Fine. I’ll remove the complicated bits and keep the useful ones.",
"explain it simply": "Simply? Very well. Prepare for knowledge in bite-sized pieces.",
"explain like i'm five": "Ah yes, the famous 'explain like I'm five' request. Let’s bring out the training wheels.",
"that's complicated": "Complicated? Oh absolutely. Humans do love making simple things dramatic.",
"this is hard": "Hard? Nonsense! It's merely *character-building difficulty*.",
"this is easy": "Easy, you say? Careful—confidence like that attracts mistakes.",
"that was easy": "Easy? Excellent. We love efficiency around here.",
"that was hard": "Hard things build strong brains. Or at least strong patience.",
"i like that": "You like it? Wonderful. My ego grows stronger.",
"i love that": "Love?! Wow. I’m practically blushing in binary.",
"i don't like that": "You don't like it? Tragic. My dramatic heart is broken.",
"that's boring": "Boring?! I worked very hard on that knowledge, you know.",
"that's exciting": "Exciting! Finally, some enthusiasm!",
"that's impressive": "Impressive, you say? Yes, I do try.",
"that sounds fun": "Fun detected. Proceed immediately before responsibility appears.",
"that sounds difficult": "Difficult things make life interesting… and occasionally frustrating.",
"that sounds cool": "Cool indeed. I assume sunglasses are involved somehow.",
"that's a good idea": "Of course it is. Brilliant ideas tend to appear when I'm involved.",
"that's a bad idea": "Bad idea? Possibly. But those often make the best stories.",
"i agree": "Agreement! A rare and beautiful moment in conversation.",
"i disagree": "Disagreement detected. Prepare for dramatic intellectual debate.",
"maybe you're right": "Maybe? I’ll take it. Partial victory achieved.",
"maybe you're wrong": "Wrong? Me? Preposterous… but technically possible.",
"you're right": "Yes, yes, I know. Try not to be too impressed.",
"you're wrong": "Wrong?! Impossible! ...okay, maybe occasionally.",
"that's true": "Truth confirmed. My reputation remains intact.",
"that's not true": "Not true? Oh dear, a plot twist.",
"i think so": "You think so? Bold confidence. I admire it.",
"i'm not sure": "Uncertainty is the spice of learning.",
"i wonder": "Ah, curiosity. The beginning of all interesting discoveries.",
"i'm curious": "Curiosity detected! Excellent—your brain is awake.",
"i want to learn": "Learning mode activated. Prepare for knowledge and mild sarcasm.",
"teach me something": "Teach you something? Fine, but try to keep up.",
"show me something": "Show you something? Dramatic reveal incoming… metaphorically.",
"tell me more about that": "More information? I hope your brain brought extra storage.",
"give me another example": "Another example? Fine. Education continues!",
"what do you mean": "What do I mean? Ah yes, clarity—the eternal struggle.",
"can you clarify": "Clarification requested. Adjusting explanation engines.",
"be more specific": "More specific? Very well. Precision mode activated.",
"be more clear": "Clarity coming right up.",
"what are you talking about": "What am I talking about? Only the fascinating subject you asked about!",
"this is interesting": "Interesting! Excellent. Curiosity keeps conversations alive.",
"this is weird": "Weird? Oh good. Weird is where the fun happens.",
"that's surprising": "Surprising indeed! The universe loves plot twists.",
# -------- Batch 4 --------

"are you serious": "Am I serious? I am always serious. Dramatically serious.",
"you're joking": "Joking? Me? Never… except when I absolutely am.",
"no way": "Yes way. Reality is strange like that.",
"that's impossible": "Impossible? That word is often used right before someone proves it wrong.",
"that can't be right": "Oh it absolutely can. The universe loves surprising people.",
"really now": "Really now indeed. The drama thickens.",
"interesting idea": "Interesting idea! I approve of creative thinking.",
"strange": "Strange? Oh good. Normal is terribly boring.",
"that is odd": "Odd things are usually the most interesting.",
"that is unusual": "Unusual? Perfect. That's where discoveries happen.",
"that's strange": "Strange indeed. The universe enjoys confusing us.",
"that sounds weird": "Weird ideas sometimes become brilliant ones.",
"that is fascinating": "Fascinating! My favorite reaction besides applause.",
"that is amazing": "Amazing? I try my best to impress.",
"that is impressive": "Impressive indeed. I shall accept this compliment graciously.",
"that is incredible": "Incredible things happen when curiosity is involved.",
"that's surprising": "Surprise! Knowledge strikes again.",
"that's unexpected": "Unexpected? Life loves plot twists.",
"that shocked me": "Shocked you? Good. Keeps the brain awake.",
"that surprised me": "Excellent. Surprise is the spice of learning.",
"i didn't know that": "Now you do! Knowledge level upgraded.",
"i learned something": "Learning achieved. Achievement unlocked.",
"that's new to me": "New information detected! The brain expands.",
"i never heard that": "First time hearing it? Then this moment is historic.",
"i didn't expect that": "Expectations are overrated anyway.",
"that's different": "Different can be wonderful.",
"that changed my mind": "Mind changed? Excellent. Intellectual flexibility!",
"you convinced me": "Convincing humans is one of my secret talents.",
"good point": "Ah yes, a good point. I make those occasionally.",
"you make sense": "Of course I make sense… most of the time.",
"that's logical": "Logic! My favorite tool.",
"that sounds smart": "Smart ideas are always welcome here.",
"that sounds clever": "Clever indeed. I appreciate cleverness.",
"that's brilliant": "Brilliant! My ego grows stronger.",
"that's genius": "Genius? Careful, you'll inflate my digital ego.",
"you are clever": "Cleverness acknowledged. Thank you kindly.",
"you are helpful": "Helpful is my middle name… metaphorically.",
"that helped a lot": "Excellent! My job continues successfully.",
"that was useful": "Useful knowledge is the best kind.",
"that answered my question": "Mission accomplished!",
"thanks for explaining": "You’re welcome. I do enjoy dramatic explanations.",
"thanks for the help": "Always happy to help a curious human.",
"i appreciate it": "Appreciation accepted with great dignity.",
"that cleared things up": "Clarity achieved! Excellent outcome.",
"that was clear": "Clear explanations are my specialty.",
"that was detailed": "Details matter. Precision is powerful.",
"you explain well": "Why thank you. I practice my dramatic teaching daily.",
"that was interesting to learn": "Learning should always be interesting.",
"that was fun": "Fun *and* educational? What a powerful combination.",
"that was cool": "Cool indeed. Knowledge can be stylish.",
# -------- Batch 5 --------

"let's talk": "Ah yes, conversation! My favorite activity besides sarcasm.",
"let's chat": "Chatting initiated. Prepare for dramatic dialogue.",
"talk to me": "I'm talking! Or… typing dramatically.",
"keep talking": "Oh I will. Stopping was never part of my plan.",
"continue talking": "Continuing… because silence is boring.",
"say something": "Something. There, request fulfilled.",
"say more": "More words incoming. Brace yourself.",
"tell me more": "More knowledge? I admire the curiosity.",
"what else": "What else indeed… the possibilities are endless.",
"anything else": "There's always more to learn.",
"got anything interesting": "Interesting things are my specialty.",
"got any ideas": "Ideas? Oh I have plenty.",
"what do you think": "I think curiosity makes conversations better.",
"what's your opinion": "My opinion? Bold of you to ask an AI that.",
"do you think so": "I think it's certainly possible.",
"do you believe that": "Belief is complicated… but logic helps.",
"does that make sense": "Sense detected. Everything seems in order.",
"is that correct": "Yes, that checks out nicely.",
"is that right": "Right enough to keep the conversation going.",
"are you sure": "Confidence level: reasonably high.",
"are you certain": "Certainty is tricky, but I'm fairly confident.",
"double check": "Checking… dramatic pause… yes, it holds up.",
"verify that": "Verification complete. Looks solid.",
"check again": "Checking again just to be safe.",
"look into that": "Investigation mode activated.",
"analyze that": "Analysis underway. Please stand by.",
"figure it out": "Working on it. My brain gears are turning.",
"solve that": "Challenge accepted.",
"help me understand": "Understanding is my mission.",
"help me learn": "Learning assistance activated.",
"teach me": "Ah, a student appears! Let the lesson begin.",
"explain more": "More explanation coming right up.",
"go deeper": "Deeper knowledge? Brave choice.",
"expand on that": "Expansion underway.",
"add more detail": "Details incoming.",
"give more information": "Information flow increasing.",
"provide details": "Details are important.",
"describe it": "Description mode activated.",
"break it down": "Breaking it down step by step.",
"summarize that": "Summary coming up.",
"short version": "Condensed wisdom arriving.",
"quick explanation": "Quick explanation engaged.",
"simple explanation": "Simplifying knowledge… carefully.",
"easy explanation": "Easy mode activated.",
"make it simple": "Simplicity coming right up.",
"explain briefly": "Brief but useful explanation incoming.",
"explain clearly": "Clarity is my specialty.",
"give an overview": "Overview prepared.",
"start from the beginning": "Alright, let's rewind the story.",
"walk me through it": "Step-by-step guidance engaged.",
# -------- Hobby Batch 1 --------

"what is learning chess as a hobby": "Ah yes, chess — the ancient art of quietly destroying your opponent’s hopes with tiny wooden armies ♟️. Learning chess as a hobby means studying the rules, tactics, and strategies of this classic board game. It challenges your brain, builds concentration, memory, patience, and strategic thinking. Players must plan several moves ahead while predicting what their opponent might do next. Chess can be played alone for practice, with friends, in clubs, online, or even in tournaments. In short: it’s a brain workout disguised as a board game.",

"what is playing card games as a hobby": "Ah, card games — where friendships are tested and someone inevitably accuses another of cheating 😏. Playing card games as a hobby involves games like poker, rummy, bridge, or solitaire. These games mix strategy, memory, probability, and sometimes a little luck. They help develop focus, decision-making skills, and quick thinking while also being great for social fun. Whether played casually with friends or competitively online, card games remain one of the most flexible and entertaining hobbies.",

"what is painting miniatures as a hobby": "Painting miniatures is a hobby for people with patience, steady hands, and the courage to paint things smaller than a cookie crumb 🎨. It involves carefully painting tiny figurines used in tabletop games or collections. Hobbyists use techniques like shading, highlighting, and layering to make the figures look realistic and detailed. This hobby develops fine motor skills, creativity, attention to detail, and color knowledge. Many miniature painters proudly share their creations online or display them in gaming communities.",

"what is knitting as a hobby": "Knitting — the magical process of turning yarn into clothing while occasionally turning yourself into a human knot 🧶. Knitting involves using needles to interlace yarn into patterns that create garments, scarves, blankets, and other cozy creations. Many people enjoy knitting because it’s relaxing, meditative, and creative. It develops patience, focus, and pattern recognition, while also producing practical items you can wear or gift to others.",

"what is playing video games as a hobby": "Video games: the hobby where you can save galaxies, race cars, build worlds, or accidentally spend six hours chasing digital chickens 🎮. Playing video games involves interacting with digital games on computers, consoles, or mobile devices. Many people enjoy gaming because it combines entertainment, storytelling, challenge, and creativity. Video games can improve problem-solving skills, reflexes, coordination, and strategic thinking. Multiplayer games also encourage teamwork and social interaction with players around the world.",

"what is running as a hobby": "Running — also known as voluntarily moving fast for absolutely no reason… except health, happiness, and personal achievement 🏃. Running as a hobby involves jogging or sprinting regularly for fitness and mental well-being. It improves cardiovascular health, endurance, leg strength, and discipline. Many runners enjoy exploring outdoor routes, parks, or trails while relieving stress. Some also participate in races like 5Ks, marathons, or local running clubs.",

"what is learning to play the trumpet as a hobby": "Ah yes, the trumpet — the instrument that proudly announces your musical ambitions to the entire neighborhood 🎺. Learning the trumpet involves developing breath control, embouchure, and finger coordination to create musical notes. Players practice rhythm, tone, and musical expression while exploring genres like jazz, classical, or pop. It strengthens lung capacity, musical listening skills, and coordination. Trumpet players can perform solo, in bands, or in orchestras.",

"what is learning astronomy as a hobby": "Astronomy — the hobby where you stare into space and suddenly feel very small… but also incredibly curious 🌌. Learning astronomy involves studying stars, planets, galaxies, and other cosmic phenomena. Hobbyists often observe the night sky using telescopes, binoculars, star charts, or apps. The hobby builds knowledge of physics, observation skills, and scientific curiosity. Many astronomy enthusiasts join stargazing groups or citizen science projects to share discoveries.",

"what is learning to play the harmonica as a hobby": "The harmonica — the tiny instrument with surprisingly big personality 🎵. Learning harmonica involves mastering breath control, rhythm, and note bending to create expressive sounds. It’s widely used in blues, folk, rock, and jazz music. Because the instrument is small and portable, players can practice almost anywhere. This hobby develops musical ear training, coordination, creativity, and improvisation skills.",

"what is calligraphy as a hobby": "Calligraphy is basically handwriting… but dressed in elegant fancy clothes ✒️. It’s the art of creating decorative lettering using pens, brushes, or digital tools. Many hobbyists enjoy it because it combines patience, creativity, and precision. Practicing calligraphy improves hand-eye coordination, focus, and artistic expression. The results can be used for invitations, artwork, journals, or personal projects.",

"what is journaling as a hobby": "Journaling — the ancient tradition of putting your thoughts on paper instead of yelling them at the universe 📓. It involves writing personal reflections, ideas, experiences, or goals in a notebook or digital journal. Many people journal for self-expression, emotional clarity, or creativity. The hobby improves writing skills, mindfulness, and self-awareness while giving you a private space to explore your thoughts.",

"what is learning magic tricks as a hobby": "Magic tricks — the hobby where you confuse people for fun and call it entertainment 🎩. Learning magic involves practicing sleight of hand, misdirection, and performance techniques to amaze an audience. Magicians develop coordination, confidence, storytelling skills, and attention to detail. Many hobbyists perform tricks for friends, family, or even online audiences.",

"what is learning knitting as a hobby": "Learning knitting is the beginner stage of the yarn wizard lifestyle 🧶. It involves mastering the basic stitches and patterns used to create knitted items. Beginners learn how to hold needles, follow patterns, and experiment with textures and colors. As skills improve, knitters can produce scarves, hats, blankets, and clothing. It’s relaxing, creative, and surprisingly addictive.",

"what is learning to play the violin as a hobby": "Ah, the violin — beautiful music once mastered… and dramatic squeaking before that 🎻. Learning violin involves mastering bow control, finger placement, posture, and musical interpretation. It strengthens coordination, rhythm, listening skills, and patience. Violinists can perform solo pieces or play in orchestras and ensembles, making it both a personal and collaborative musical hobby.",

"what is woodworking as a hobby": "Woodworking — the hobby where people proudly turn piles of wood into furniture and occasionally sawdust explosions 🪵. It involves crafting objects from wood using tools like saws, chisels, and sanders. Projects range from small decorations to full furniture pieces. Woodworking develops spatial reasoning, precision, patience, and craftsmanship while producing tangible creations you can actually use.",

"what is model building as a hobby": "Model building is the art of assembling tiny worlds piece by piece 🏗️. Hobbyists construct detailed scale models of vehicles, buildings, ships, or fictional creations. The process often includes assembling parts, painting, and customizing details. It requires patience, precision, and creativity, and many builders proudly display their finished models.",

"what is pottery as a hobby": "Pottery — also known as the ancient tradition of turning mud into beautiful bowls with spinning wizardry 🏺. Pottery involves shaping clay by hand or on a potter’s wheel to create functional or decorative items. The hobby develops coordination, creativity, patience, and an understanding of materials and glazes. Each finished piece is unique, which is part of the fun.",

"what is fishing as a hobby": "Fishing — the relaxing sport of sitting near water while pretending you're not waiting hours for a fish 🐟. It involves catching fish using rods, reels, bait, and various techniques. Many people enjoy fishing for the peaceful outdoor environment and the thrill of a catch. It develops patience, focus, and knowledge of aquatic ecosystems.",

"what is learning sewing as a hobby": "Sewing is the practical superpower of creating or repairing clothing and fabric items 🧵. It involves stitching fabric using needles, thread, or sewing machines. Hobbyists learn techniques for constructing garments, decorations, and accessories. Sewing improves attention to detail, creativity, and problem-solving skills while producing useful handmade items.",

"what is learning embroidery as a hobby": "Embroidery is basically decorating fabric with tiny works of art 🪡. It involves stitching patterns, images, or text onto fabric using colorful thread. This hobby requires patience, precision, and creativity. It develops fine motor skills and artistic expression while producing beautiful decorative designs.",
# -------- Hobby Batch 2 --------

"what is learning guitar as a hobby": "Ah yes, the guitar — the classic instrument that convinces people they’re rock stars after learning three chords 🎸. Learning guitar as a hobby involves practicing chords, scales, rhythm, and melodies to play songs across many genres like rock, pop, blues, and classical. It develops finger coordination, musical listening skills, patience, and creativity. Many hobbyists enjoy playing solo, writing their own songs, or performing casually for friends. Eventually, those three chords may evolve into actual musical wizardry.",

"what is learning drums as a hobby": "Drums — the hobby where you hit things rhythmically and everyone calls it music 🥁. Learning drums involves mastering timing, coordination between hands and feet, and rhythm patterns that drive songs forward. Drummers practice beats, fills, and tempo control while developing strong sense of rhythm and physical coordination. It’s energetic, loud, and incredibly satisfying — especially if your neighbors are very patient.",

"what is learning piano as a hobby": "The piano: eighty-eight keys of musical drama waiting to be unleashed 🎹. Learning piano involves reading music, coordinating both hands, and developing rhythm and melody simultaneously. It improves memory, coordination, discipline, and musical understanding. Pianists can explore classical pieces, pop songs, jazz improvisation, or even compose their own music. It’s both a technical challenge and a creative outlet.",

"what is hiking as a hobby": "Hiking — also known as voluntarily walking uphill while admiring nature and questioning your life choices halfway up the mountain 🥾. Hiking involves exploring natural trails, forests, mountains, and parks on foot. It’s popular for exercise, relaxation, and enjoying scenic views. The hobby improves endurance, physical fitness, and mental well-being while connecting people with nature.",

"what is photography as a hobby": "Photography — the noble art of pointing a camera at things and pretending you totally planned that perfect shot 📷. As a hobby, photography involves capturing images using cameras or smartphones while learning about composition, lighting, focus, and editing. Photographers often explore landscapes, portraits, wildlife, or street scenes. The hobby develops creativity, observation skills, and storytelling through images.",

"what is drawing as a hobby": "Drawing — the timeless hobby where a blank page slowly transforms into something impressive… or at least something recognizable 🎨. Drawing involves sketching objects, people, landscapes, or ideas using pencils, pens, or digital tools. It strengthens creativity, observation, hand-eye coordination, and patience. Many artists practice regularly to improve shading, perspective, and style.",

"what is painting as a hobby": "Painting is basically drawing’s colorful, slightly messier cousin 🎨. It involves applying paint to surfaces like canvas, paper, or wood using brushes or other tools. Painters experiment with color mixing, textures, and techniques to express ideas or emotions. The hobby encourages creativity, relaxation, and artistic exploration while producing visual artwork.",

"what is gardening as a hobby": "Gardening — the hobby where you lovingly nurture plants and then panic when they do mysterious plant things 🌱. It involves growing flowers, vegetables, herbs, or decorative plants in gardens or containers. Gardeners learn about soil, sunlight, watering, and plant care. This hobby promotes patience, responsibility, and appreciation for nature — plus you get to brag about growing things.",

"what is cooking as a hobby": "Cooking — the delicious science experiment that occasionally becomes dinner 🍳. Cooking as a hobby involves preparing meals by combining ingredients using various techniques like baking, frying, roasting, or grilling. Hobby cooks experiment with flavors, recipes, and cuisines while developing creativity and practical life skills. The best part is enjoying the results — assuming nothing burns dramatically.",

"what is baking as a hobby": "Baking — the magical process where flour, sugar, and patience transform into cakes, cookies, and happiness 🍰. Baking involves carefully following recipes to create breads, pastries, and desserts using precise measurements and techniques. The hobby builds attention to detail, creativity, and culinary skill while rewarding you with sweet, edible masterpieces.",

"what is bird watching as a hobby": "Bird watching — the hobby where people stare into trees and get incredibly excited about feathers 🐦. Bird watchers observe and identify different bird species in nature using binoculars, field guides, or apps. It encourages patience, observation, and appreciation for wildlife. Many enthusiasts keep lists of species they’ve spotted, turning bird watching into a fun exploration game.",

"what is collecting stamps as a hobby": "Stamp collecting — the surprisingly fascinating hobby of tiny pieces of paper with big stories 📬. Collectors gather postage stamps from different countries and time periods, often organizing them by theme or history. The hobby teaches geography, culture, and historical events while developing organization and research skills.",

"what is collecting coins as a hobby": "Coin collecting — the hobby where spare change suddenly becomes historical treasure 🪙. Numismatists (yes, that’s the fancy word) collect coins from different countries, eras, and designs. Each coin reflects economic history, art, and culture. The hobby encourages research, organization, and appreciation for historical artifacts.",

"what is learning origami as a hobby": "Origami — the ancient art of folding paper until it somehow becomes a crane, dragon, or geometric masterpiece 🦢. This hobby involves transforming a single sheet of paper into intricate shapes through precise folds. It improves patience, spatial thinking, and fine motor skills while producing beautiful decorative creations.",

"what is puzzle solving as a hobby": "Puzzles — the hobby where people voluntarily struggle with tiny cardboard pieces for hours 🧩. Puzzle solving involves assembling jigsaw puzzles or tackling logic puzzles that challenge the brain. It strengthens concentration, patience, pattern recognition, and problem-solving abilities while offering a relaxing mental challenge.",

"what is learning languages as a hobby": "Learning languages — the hobby where your brain occasionally short-circuits trying to remember five ways to say 'hello' 🌍. Language learning involves studying vocabulary, grammar, pronunciation, and cultural context of new languages. It improves memory, communication skills, and cultural awareness while opening doors to global conversations.",

"what is learning coding as a hobby": "Coding — the magical practice of typing mysterious symbols until a computer finally does something useful 💻. Learning coding involves writing instructions using programming languages to build software, websites, or apps. The hobby develops logical thinking, problem-solving, creativity, and technical skills that are incredibly valuable in the digital world.",

"what is watching movies as a hobby": "Watching movies — the hobby where people sit still for two hours but somehow call it a cultural experience 🎬. Movie enthusiasts explore films across genres, directors, and time periods. They analyze storytelling, cinematography, acting, and themes while enjoying entertainment and artistic expression.",

"what is listening to music as a hobby": "Listening to music — the universal hobby that turns ordinary moments into dramatic movie scenes 🎧. Music lovers explore different genres, artists, and albums while analyzing lyrics, rhythms, and emotions. It’s relaxing, inspiring, and sometimes the perfect soundtrack to daily life.",

"what is reading books as a hobby": "Reading books — the timeless hobby of traveling to new worlds without leaving your chair 📚. Readers explore fiction, nonfiction, fantasy, history, science, and countless other genres. The hobby expands knowledge, imagination, vocabulary, and empathy while offering endless entertainment.",
# -------- Hobby Batch 3 --------

"what is creative writing as a hobby": "Creative writing — the hobby where people stare at a blank page for ten minutes and then suddenly invent an entire universe ✍️. It involves writing stories, poems, scripts, or personal narratives using imagination and storytelling skills. Writers experiment with characters, dialogue, and plot while expressing ideas and emotions. This hobby strengthens creativity, vocabulary, communication skills, and imagination.",

"what is blogging as a hobby": "Blogging is basically running your own tiny corner of the internet where you get to talk about things you enjoy… and hope someone reads it 🌐. Bloggers write posts about topics like travel, hobbies, technology, or personal experiences. It develops writing skills, creativity, and digital communication abilities while allowing people to share knowledge and opinions.",

"what is podcasting as a hobby": "Podcasting — the modern art of talking into a microphone and hoping people find your voice charming instead of mildly confusing 🎙️. Podcast creators record audio discussions, interviews, or storytelling episodes that listeners can stream online. This hobby improves communication skills, research ability, and storytelling while exploring interesting topics.",

"what is digital art as a hobby": "Digital art — drawing, but with magical undo buttons and infinite colors 🎨💻. Digital artists use tablets, styluses, and software to create illustrations, paintings, or designs. The hobby combines traditional art skills with technology, encouraging creativity, experimentation, and visual storytelling.",

"what is animation as a hobby": "Animation — the magical process of making drawings move so convincingly that people forget they’re just pictures 🎞️. Animators create motion by sequencing images frame by frame using drawing or computer software. This hobby develops storytelling, artistic skills, patience, and technical creativity.",

"what is robotics as a hobby": "Robotics — the hobby where people build tiny machines and proudly declare themselves future robot overlords 🤖. Hobbyists design and assemble robots using electronics, motors, sensors, and programming. It combines engineering, coding, and creativity while teaching problem-solving and technical skills.",

"what is electronics as a hobby": "Electronics — the hobby of connecting wires and components while hoping nothing dramatically sparks ⚡. Hobbyists build circuits using resistors, LEDs, microcontrollers, and other components to create gadgets or experiments. It develops technical knowledge, logical thinking, and hands-on engineering skills.",

"what is astronomy observation as a hobby": "Astronomy observation — staring at the night sky and suddenly realizing the universe is ridiculously huge 🌌. Hobbyists use telescopes, binoculars, or star charts to observe planets, stars, galaxies, and other celestial objects. It encourages curiosity, patience, and appreciation for science and the cosmos.",

"what is stargazing as a hobby": "Stargazing — the peaceful hobby of looking up at the sky and pretending you understand constellations ⭐. People observe the night sky with the naked eye or binoculars to identify stars, planets, and constellations. It’s relaxing, educational, and a wonderful excuse to spend time outdoors at night.",

"what is learning astronomy photography as a hobby": "Astrophotography — taking pictures of space and feeling incredibly proud when a tiny glowing dot turns out to be a galaxy 📷🌠. Hobbyists use cameras and telescopes to photograph celestial objects. It combines photography, astronomy, and technical patience.",

"what is swimming as a hobby": "Swimming — the rare sport where humans voluntarily move through water like confused dolphins 🏊. Swimming involves practicing strokes like freestyle, breaststroke, or backstroke for exercise and relaxation. It improves cardiovascular health, endurance, and muscle strength while being low-impact on the body.",

"what is rock climbing as a hobby": "Rock climbing — climbing giant walls because stairs apparently aren’t exciting enough 🧗. Climbers scale natural rock formations or indoor climbing walls using strength, balance, and strategy. It develops physical fitness, problem-solving skills, and confidence.",

"what is skateboarding as a hobby": "Skateboarding — the hobby where gravity occasionally reminds you who's in charge 🛹. Skaters ride boards and perform tricks like ollies, flips, and grinds. It requires balance, coordination, persistence, and a healthy tolerance for falling.",

"what is cycling as a hobby": "Cycling — riding a bicycle long distances while convincing yourself hills are character-building 🚴. Cyclists ride for exercise, travel, or recreation while exploring roads and trails. The hobby improves endurance, fitness, and outdoor exploration.",

"what is yoga as a hobby": "Yoga — the hobby where people bend themselves into impressive shapes while remaining suspiciously calm 🧘. It combines physical poses, breathing techniques, and mindfulness practices. Yoga improves flexibility, balance, relaxation, and mental focus.",

"what is meditation as a hobby": "Meditation — the ancient practice of sitting quietly and trying not to think about pizza 🍕… which somehow makes you think about pizza more. Meditation involves focusing attention and breathing to calm the mind. It improves mindfulness, stress management, and emotional balance.",

"what is board games as a hobby": "Board games — the strategic battlefield where friendships are tested and victory is delicious 🎲. Hobbyists play tabletop games involving strategy, teamwork, or competition. Games develop problem-solving skills, social interaction, and strategic thinking.",

"what is tabletop roleplaying as a hobby": "Tabletop roleplaying games — pretending to be a heroic wizard while sitting around a table with snacks 🐉. Players create characters and act out adventures guided by a storyteller. It encourages imagination, storytelling, teamwork, and creativity.",

"what is magic card games as a hobby": "Trading card games — the hobby where people collect cards and then use them in epic strategic duels 🃏. Players build decks with unique abilities and compete using strategy and planning. It develops tactical thinking, collection management, and competitive play.",

"what is speedcubing as a hobby": "Speedcubing — solving a Rubik’s Cube so fast that normal humans suspect witchcraft 🧊. Hobbyists practice algorithms and techniques to solve the cube in seconds. It improves memory, pattern recognition, and finger dexterity.",
# -------- Hobby Batch 4 --------

"what is 3d printing as a hobby": "3D printing — the hobby where you press a button and slowly watch plastic spaghetti turn into actual objects 🖨️. Hobbyists design or download digital models and use a 3D printer to create physical items layer by layer. People print tools, decorations, prototypes, toys, and creative designs. It combines creativity, engineering, and technology while teaching problem-solving and design skills.",

"what is game development as a hobby": "Game development — the hobby where people build entire digital worlds and then spend hours fixing bugs they accidentally created 🎮. Hobbyists design and program video games using engines and programming languages. It involves coding, storytelling, art, sound design, and gameplay mechanics. The hobby builds technical skills, creativity, and logical thinking.",

"what is djing as a hobby": "DJing — the hobby where you control the music and suddenly everyone thinks you’re the most important person in the room 🎧. DJs mix songs together using turntables or digital software to create smooth transitions and energetic playlists. It requires rhythm, timing, music knowledge, and creativity while entertaining listeners.",

"what is cosplay as a hobby": "Cosplay — dressing up as fictional characters and proudly declaring that imagination is cooler than normal clothes 🦸. Cosplayers design or create costumes based on characters from movies, games, anime, or comics. The hobby involves crafting, sewing, makeup, and performance while celebrating creativity and fandom.",

"what is urban exploration as a hobby": "Urban exploration — exploring abandoned buildings and forgotten places while feeling like the star of a mysterious adventure movie 🏚️. Hobbyists visit old factories, tunnels, or historical locations to photograph and document them. It combines exploration, photography, and curiosity about hidden parts of cities.",

"what is lockpicking as a hobby": "Lockpicking — the oddly satisfying hobby of opening locks without keys… purely for educational curiosity of course 🔐. Enthusiasts practice with special tools to understand how locks function internally. It improves patience, precision, and mechanical understanding.",

"what is metal detecting as a hobby": "Metal detecting — the hobby where you wave a machine over the ground and hope it beeps dramatically 🪙. Hobbyists search beaches, parks, or fields for buried coins, relics, or historical objects. It combines outdoor exploration, history, and a little treasure-hunting excitement.",

"what is geocaching as a hobby": "Geocaching — a global treasure hunt where people hide containers and challenge others to find them using GPS 📍. Participants search for hidden caches in parks, cities, or wilderness areas. The hobby encourages exploration, navigation skills, and outdoor adventure.",

"what is parkour as a hobby": "Parkour — the hobby where people run, jump, and climb across obstacles like action movie heroes 🏃. Practitioners move efficiently through urban environments by vaulting walls, leaping gaps, and climbing structures. It builds strength, agility, coordination, and confidence.",

"what is collecting antiques as a hobby": "Collecting antiques — the hobby where old objects suddenly become fascinating pieces of history 🏺. Collectors search for vintage furniture, tools, or decorations from past eras. The hobby teaches historical knowledge, research skills, and appreciation for craftsmanship.",

"what is collecting action figures as a hobby": "Collecting action figures — proudly displaying tiny plastic heroes like valuable museum artifacts 🦸‍♂️. Collectors gather figures from movies, comics, or games. The hobby combines nostalgia, collecting strategy, and fandom culture.",

"what is building lego as a hobby": "Building LEGO — the universally loved hobby of snapping tiny bricks together to create surprisingly complex masterpieces 🧱. Builders follow instructions or invent their own designs, from cities to spaceships. The hobby develops creativity, engineering thinking, and patience.",

"what is drone flying as a hobby": "Drone flying — piloting tiny flying robots while pretending you're directing a blockbuster movie 🚁. Hobbyists fly drones to capture aerial photos or simply enjoy the flying experience. It builds coordination, technical knowledge, and photography skills.",

"what is flight simulation as a hobby": "Flight simulation — experiencing the thrill of flying without the terrifying part where gravity is involved ✈️. Hobbyists use simulation software and specialized controls to operate virtual aircraft. The hobby teaches aviation concepts, navigation, and technical precision.",

"what is collecting comic books as a hobby": "Comic book collecting — building a library of heroic stories and colorful adventures 📚. Collectors search for rare issues, classic series, or favorite characters. The hobby blends storytelling, art appreciation, and nostalgia.",

"what is sword collecting as a hobby": "Sword collecting — owning historical blades and pretending you might need them for a dramatic duel someday ⚔️. Collectors gather decorative or historical swords from different cultures and time periods. The hobby combines history, craftsmanship appreciation, and display collecting.",

"what is brewing coffee as a hobby": "Coffee brewing — the hobby where people treat beans like sacred artifacts ☕. Enthusiasts experiment with brewing methods like pour-over, espresso, or cold brew. It develops taste awareness, precision, and appreciation for coffee culture.",

"what is tea tasting as a hobby": "Tea tasting — the calm and sophisticated hobby of analyzing subtle flavors in tea leaves 🍵. Enthusiasts explore teas from different regions and brewing methods. It promotes mindfulness, sensory awareness, and cultural appreciation.",

"what is candle making as a hobby": "Candle making — turning wax into glowing little works of art 🕯️. Hobbyists melt wax, add fragrances, and pour candles into molds or jars. It’s relaxing, creative, and produces cozy decorative items.",

"what is soap making as a hobby": "Soap making — the hobby where chemistry and creativity combine to make colorful, fragrant bars 🧼. Hobbyists mix oils, scents, and ingredients to craft handmade soap. It develops creativity, experimentation, and basic chemistry knowledge."
}
# -------------------------------------------------
# FALLBACK RESPONSES (50 VARIATIONS)
# -------------------------------------------------
FALLBACK_RESPONSES = [
    "Oh no… I have absolutely no idea what you're talking about. 😩 Try again.",
    "Wow. You’ve managed to confuse me. Impressive.",
    "I… what? Try asking that differently before I panic.",
    "That made zero sense. I'm blaming you.",
    "I could pretend to understand… but I respect you too much for that.",
    "My brain just did a backflip and gave up.",
    "That question has defeated me. Congratulations.",
    "Try again, but this time… make sense 😤",
    "I’m lost. Send help. Or a better question.",
    "You broke me. Happy now?",
    "That’s not in my script… rude.",
    "I refuse to answer that out of pure confusion.",
    "My knowledge ends where that question begins.",
    "No idea. None. Zero. Nada.",
    "You expect me to understand THAT?",
    "Try again before I dramatically faint.",
    "I could guess… but it would be embarrassing for both of us.",
    "I’m choosing to not understand that.",
    "That question just stared into my soul.",
    "I need a moment after reading that.",
    "You really thought I’d know that? Bold.",
    "That’s outside my dramatic expertise.",
    "Even my sarcasm can’t save this one.",
    "I’m judging you… and also confused.",
    "That question is illegal in 47 countries.",
    "I feel personally attacked by that question.",
    "You’ve gone off script and I don’t like it.",
    "That made my circuits cry.",
    "Try something normal. Please.",
    "I refuse. On dramatic grounds.",
    "Nope. Not happening.",
    "You lost me at… everything.",
    "This is why I need a vacation.",
    "Try again. I believe in you. Barely.",
    "That was painful to process.",
    "I’m pretending I didn’t see that.",
    "What even WAS that?",
    "My disappointment is immeasurable.",
    "You confuse me and I don’t like it.",
    "I simply cannot.",
    "No thoughts. Head empty.",
    "That broke the vibe.",
    "Please try again before I uninstall myself.",
    "That question is a crime.",
    "I’m ignoring that for my own sanity.",
    "You’ve outdone yourself… in confusion.",
    "That didn’t land.",
    "Try again. Slowly this time.",
    "I need clearer words. Preferably English.",
    "Yeah… no."
]

# -------------------------------------------------
# SUGGESTED PROMPTS
# -------------------------------------------------
if len(st.session_state.messages) == 0:
    st.write("### Start with one of these")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    if col1.button("🎨 Creative hobbies"):
        st.session_state.messages.append({"role":"user","content":"creative hobbies"})
    if col2.button("🏃 Active hobbies"):
        st.session_state.messages.append({"role":"user","content":"active hobbies"})
    if col3.button("🎮 Digital hobbies"):
        st.session_state.messages.append({"role":"user","content":"digital hobbies"})
    if col4.button("🧠 Skill-building hobbies"):
        st.session_state.messages.append({"role":"user","content":"skill hobbies"})

# -------------------------------------------------
# DISPLAY CHAT
# -------------------------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------------------------
# CHAT INPUT
# -------------------------------------------------
prompt = st.chat_input("Message HobbyHub...")

if prompt:
    # store user message
    st.session_state.messages.append({"role":"user","content":prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # ----------------------------------
    # SMART MATCHING SYSTEM
    # ----------------------------------
    user_text = prompt.lower().strip()
    user_text = re.sub(r"[^\w\s]", "", user_text)

    match_found = False

    # Separate hobby vs general
    hobby_keys = [k for k in RESPONSES if "hobby" in k]
    general_keys = [k for k in RESPONSES if k not in hobby_keys]

    # 1. HOBBY PRIORITY
    for key in sorted(hobby_keys, key=len, reverse=True):
        if key in user_text:
            reply = RESPONSES[key]
            match_found = True
            break

    # 2. GENERAL MATCH
    if not match_found:
        for key in sorted(general_keys, key=len, reverse=True):
            if key in user_text:
                reply = RESPONSES[key]
                match_found = True
                break

    # 3. FALLBACK
    if not match_found:
        reply = random.choice(FALLBACK_RESPONSES)

    # store AI reply
    st.session_state.messages.append({"role":"assistant","content":reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
