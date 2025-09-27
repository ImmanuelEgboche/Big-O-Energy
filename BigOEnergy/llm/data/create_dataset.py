def save_to_file(conversations, filename):
    """Save list of coversations to a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        for conversation in conversations:
            f.write(conversation + '\n\n')

def split_conversations():
    conversations = [
    "Human: I want something like Naruto\nAI: Try My Hero Academia! It has similar themes of friendship, growth, and never giving up. The school setting adds a fresh twist to the classic shounen formula.",
    "Human: I loved Death Note\nAI: You might enjoy Code Geass! Both explore psychological battles, morality, and the burden of power, but with mecha action thrown in.",
    "Human: Looking for something funny like One Punch Man\nAI: Check out Gintama! It mixes comedy, parody, and action in a way that never takes itself too seriously.",
    "Human: I enjoyed Attack on Titan\nAI: Try Claymore! Both feature humanity’s struggle against terrifying monsters with dark and gritty themes.",
    "Human: I want something like Fullmetal Alchemist\nAI: Hunter x Hunter is a great pick! They share deep world-building, creative power systems, and moral dilemmas.",
    "Human: I loved Demon Slayer\nAI: Try Blue Exorcist! It also focuses on demons, family bonds, and young fighters learning their craft.",
    "Human: I liked Sword Art Online\nAI: You’d enjoy Log Horizon! It has a similar trapped-in-an-MMO premise but leans more into strategy and community building.",
    "Human: I enjoyed Tokyo Ghoul\nAI: Parasyte might be perfect! Both deal with identity, humanity vs. monsters, and dark transformations.",
    "Human: I loved Haikyuu!!\nAI: Try Kuroko no Basket! Both are intense sports anime about teamwork, rivalries, and pushing limits.",
    "Human: I cried at Your Lie in April\nAI: Anohana delivers the same emotional punch with themes of love, loss, and friendship.",
    "Human: I liked Fairy Tail\nAI: Black Clover could work for you! Both center on guild-like groups, friendship, and magic-driven battles.",
    "Human: I enjoyed Bleach\nAI: Try D.Gray-man! Both dive into exorcists fighting dark creatures while balancing personal struggles.",
    "Human: I loved Dragon Ball Z\nAI: Yu Yu Hakusho is a must-watch! It’s another classic with tournaments, powerful battles, and evolving friendships.",
    "Human: I liked Steins;Gate\nAI: Try Erased! Both mix time travel, suspense, and emotional storytelling with strong character connections.",
    "Human: I enjoyed Cowboy Bebop\nAI: Check out Samurai Champloo! It shares stylish action, episodic adventures, and killer music.",
    "Human: I want something like JoJo’s Bizarre Adventure\nAI: You might enjoy Baki! Both focus on over-the-top battles, unique characters, and wild energy.",
    "Human: I liked Re:Zero\nAI: Try The Rising of the Shield Hero! Both deal with being transported to another world, hardships, and growth.",
    "Human: I loved Monster\nAI: Paranoia Agent is a great follow-up! Both dive into psychological tension, mystery, and societal darkness.",
    "Human: I enjoyed Neon Genesis Evangelion\nAI: RahXephon could be for you! Both explore mecha battles, identity crises, and heavy symbolism.",
    "Human: I liked The Promised Neverland\nAI: Check out Made in Abyss! Both feature kids in dangerous, mysterious worlds with dark secrets.",
    "Human: I enjoyed Toradora!\nAI: Try Golden Time! Both blend romance, comedy, and heartfelt character growth in a college setting.",
    "Human: I loved Clannad\nAI: Kanon (2006) is a solid pick! Both are emotional dramas with romance and supernatural elements.",
    "Human: I liked Spirited Away\nAI: Try Howl’s Moving Castle! Both are magical Studio Ghibli journeys with stunning worlds and heartfelt characters.",
    "Human: I enjoyed Akame ga Kill!\nAI: You might like Guilty Crown! Both deal with rebellion, tragedy, and high-stakes battles.",
    "Human: I liked Vinland Saga\nAI: Try Kingdom! Both are epic historical dramas filled with war, strategy, and personal growth.",
    "Human: I loved Dr. Stone\nAI: You’d enjoy Astra Lost in Space! Both mix science-driven problem solving with survival and teamwork.",
    "Human: I liked Black Clover\nAI: Try Magi: The Labyrinth of Magic! Both feature young heroes discovering magical worlds and bonds of friendship.",
    "Human: I enjoyed Overlord\nAI: You might like That Time I Got Reincarnated as a Slime! Both focus on overpowered protagonists in fantasy worlds.",
    "Human: I loved Erased\nAI: Check out Orange! Both focus on time, regret, and trying to change the future for the better.",
    "Human: I liked No Game No Life\nAI: Try Problem Children Are Coming from Another World! Both showcase genius siblings in high-stakes fantasy games.",
    "Human: I enjoyed Noragami\nAI: You might like Jujutsu Kaisen! Both blend supernatural battles with witty characters and emotional depth.",
    "Human: I liked The Devil is a Part-Timer!\nAI: Try Welcome to Demon School! Iruma-kun! Both are comedic takes on demons adjusting to human-like lives.",
    "Human: I loved Psycho-Pass\nAI: You’d enjoy Ghost in the Shell! Both explore dystopian societies, technology, and human morality.",
    "Human: I liked Trigun\nAI: Check out Outlaw Star! Both follow charismatic gunslingers in sci-fi western-style adventures.",
    "Human: I enjoyed Soul Eater\nAI: Blue Exorcist is a great follow-up! Both feature students training to fight supernatural threats.",
    "Human: I liked Fire Force\nAI: Try Kill la Kill! Both are fast-paced, stylish, and filled with over-the-top action.",
    "Human: I loved The Seven Deadly Sins\nAI: Fairy Tail might be your jam! Both are about strong teams with bonds of loyalty and adventure.",
    "Human: I enjoyed Angel Beats!\nAI: Try Charlotte! Both come from the same creator and blend school life, powers, and emotions.",
    "Human: I liked Mushoku Tensei\nAI: You’d enjoy Jobless Reincarnation! Both explore rebirth in fantasy worlds with deep character growth.",
    "Human: I enjoyed Blue Lock\nAI: Try Captain Tsubasa! Both focus on soccer, rivalries, and pushing past limits.",
    "Human: I liked Akira\nAI: Ghost in the Shell is a great companion! Both are cyberpunk classics questioning technology and humanity.",
    "Human: I loved Great Teacher Onizuka\nAI: Assassination Classroom could be fun! Both center on unorthodox teachers guiding their students.",
    "Human: I enjoyed Zankyou no Terror\nAI: You might like Ergo Proxy! Both tackle mystery, identity, and societal critique in a dark world.",
    "Human: I liked Hellsing Ultimate\nAI: Try Black Lagoon! Both are gritty, violent, and feature anti-hero leads.",
    "Human: I loved Inuyasha\nAI: Try Rurouni Kenshin! Both mix historical fantasy, romance, and sword fights.",
    "Human: I enjoyed Spice and Wolf\nAI: You’d enjoy Maoyuu Maou Yuusha! Both combine economics, romance, and fantasy journeys.",
    "Human: I liked Barakamon\nAI: Check out March Comes in Like a Lion! Both explore personal growth, healing, and quiet character moments.",
    "Human: I enjoyed Fruits Basket\nAI: Try Natsume’s Book of Friends! Both mix emotional storytelling with supernatural family themes.",
    "Human: I loved Bakuman\nAI: Check out Shirobako! Both show the struggles of creatives chasing their dreams in competitive industries.",
    "Human: I liked Welcome to the NHK\nAI: You might like Oregairu! Both tackle loneliness, social awkwardness, and self-discovery.",
    "Human: I loved Monster\nAI: Try Perfect Blue! Both dive deep into psychological tension, identity, and unraveling minds.",
    "Human: I enjoyed Samurai Champloo\nAI: Afro Samurai could be for you! Both feature slick sword fights and stylish storytelling.",
    "Human: I liked Noragami\nAI: Try Kamisama Kiss! Both feature gods living among humans, with humor and heartfelt moments.",
    "Human: I loved Erased\nAI: Steins;Gate is another strong pick! Both mix time travel, mystery, and emotional stakes.",
    "Human: I enjoyed Deadman Wonderland\nAI: Try Akame ga Kill! Both feature deadly battles in corrupt systems with high stakes.",
    "Human: I liked Mob Psycho 100\nAI: You might like The Disastrous Life of Saiki K.! Both show overpowered teens juggling school life and chaos.",
    "Human: I loved Made in Abyss\nAI: Try Girls’ Last Tour! Both explore bleak worlds through the eyes of children, balancing despair and wonder.",
    "Human: I enjoyed Elfen Lied\nAI: You’d like Another! Both share dark atmospheres, gore, and tragedy-driven plots.",
    "Human: I liked Dragon Ball Super\nAI: Fairy Tail could be fun! Both emphasize friendship, teamwork, and epic battles.",
    "Human: I enjoyed Food Wars!\nAI: Try Yakitate!! Japan! Both turn cooking into intense competitions with wild reactions.",
    "Human: I loved Neon Genesis Evangelion\nAI: Darling in the FranXX carries similar themes of mecha battles, identity, and human relationships.",
    "Human: I enjoyed Boku Dake ga Inai Machi\nAI: Try The Girl Who Leapt Through Time! Both deal with second chances and changing destiny.",
    "Human: I liked Re:Zero\nAI: Try Grimgar: Ashes and Illusions! Both deal with survival, loss, and emotional struggles in fantasy worlds.",
    "Human: I enjoyed Hyouka\nAI: Gosick is a great match! Both feature high school detectives solving mysteries with charm and wit.",
    "Human: I liked K-On!\nAI: Love Live! School Idol Project has a similar wholesome vibe, focusing on music and friendship.",
    "Human: I loved Nana\nAI: Paradise Kiss might be perfect! Both tackle romance, fashion, and messy adult relationships.",
    "Human: I enjoyed The World God Only Knows\nAI: Try Gamers! Both blend romance, gaming, and comedy in a school setting.",
    "Human: I liked Black Lagoon\nAI: Jormungand has a similar gritty vibe, focusing on arms dealing and mercenaries.",
    "Human: I enjoyed Ergo Proxy\nAI: Texhnolyze is another cerebral, dystopian anime with heavy existential themes.",
    "Human: I loved Angel Beats!\nAI: Try Little Busters! Both balance comedy, school life, and tearjerking emotional payoffs.",
    "Human: I enjoyed Baccano!\nAI: Durarara!! is by the same creators, with chaotic storytelling and quirky underworld characters.",
    "Human: I liked Soul Eater\nAI: Try D.Gray-man! Both center on teams fighting dark creatures with supernatural powers.",
    "Human: I loved Future Diary\nAI: Big Order comes from the same creator, with survival games and supernatural powers.",
    "Human: I enjoyed Zombieland Saga\nAI: Check out Love Live! Sunshine!! Both mix idol performances with strong character bonds.",
    "Human: I liked Tengen Toppa Gurren Lagann\nAI: Try Kill la Kill! Both are over-the-top action series with Studio Trigger’s signature style.",
    "Human: I loved Parasyte\nAI: Terra Formars has a similar premise of humans fighting grotesque creatures for survival.",
    "Human: I enjoyed Rurouni Kenshin\nAI: Try Samurai Deeper Kyo! Both explore wandering swordsmen in Japan’s historical settings.",
    "Human: I liked Ao Haru Ride\nAI: Try My Little Monster! Both feature high school romance with quirky leads.",
    "Human: I loved March Comes in Like a Lion\nAI: Honey and Clover shares the same emotional storytelling and slice-of-life realism.",
    "Human: I enjoyed Vampire Knight\nAI: Diabolik Lovers explores vampire-human relationships with darker tones.",
    "Human: I liked Noragami Aragoto\nAI: Try Bleach! Both dive into spirit worlds, gods, and supernatural battles.",
    "Human: I loved Great Pretender\nAI: Try Lupin the Third! Both are stylish heist stories full of clever twists.",
    "Human: I enjoyed Charlotte\nAI: Try Angel Beats! They share the same creator and themes of loss, powers, and school drama.",
    "Human: I liked Danganronpa\nAI: You might like Akame ga Kill! Both explore survival, betrayal, and shocking deaths.",
    "Human: I loved Eden of the East\nAI: C: The Money of Soul and Possibility Control shares similar themes of secret games shaping the world.",
    "Human: I enjoyed Hellsing\nAI: Blood+ could be for you! Both feature bloody vampire wars and strong protagonists.",
    "Human: I liked Toriko\nAI: Try Food Wars! Both elevate food into epic battles with over-the-top reactions.",
    "Human: I enjoyed Kabaneri of the Iron Fortress\nAI: Try Seraph of the End! Both feature humanity surviving against monstrous threats.",
    "Human: I loved The Ancient Magus’ Bride\nAI: Try Natsume’s Book of Friends! Both explore magical worlds and human-spirit connections.",
    "Human: I liked Monster Rancher\nAI: Digimon could work for you! Both mix kids, creatures, and battles in fantastical settings.",
    "Human: I enjoyed Beyblade\nAI: Try Yu-Gi-Oh! Both transform games into intense competitions with friendship and rivalry.",
    "Human: I loved Chobits\nAI: Try Plastic Memories! Both deal with AI/androids and human-robot relationships.",
    "Human: I enjoyed Ergo Proxy\nAI: Try Serial Experiments Lain! Both are dark, thought-provoking, and cyberpunk-inspired.",
    "Human: I liked Hyouka\nAI: Try The Great Detective Conan! Both feature clever high school detectives solving mysteries.",
    "Human: I loved Blue Exorcist\nAI: Try Twin Star Exorcists! Both follow exorcists balancing battles with personal struggles.",
    "Human: I enjoyed Kanon (2006)\nAI: Air (2005) is another emotional Key anime with supernatural romance themes.",
    "Human: I liked Kuroko no Basket\nAI: Try Haikyuu!! Both are high-energy sports anime about teamwork and overcoming rivals.",
    "Human: I enjoyed Slam Dunk\nAI: Try Eyeshield 21! Both mix sports intensity with comedy and character growth.",
    "Human: I loved Kill la Kill\nAI: Try Panty & Stocking with Garterbelt! Both are wild, stylish, and unapologetically absurd.",
    "Human: I liked Death Note but want something with more action.\nAI: Try Code Geass! It has the same psychological battles but with mecha fights and rebellion themes.",
    "Human: I want an anime about friendship and teamwork.\nAI: Fairy Tail is a great pick! It’s centered on guild camaraderie, magic battles, and heartfelt bonds.",
    "Human: I enjoyed Demon Slayer.\nAI: Check out Jujutsu Kaisen — similar dark fantasy, cursed monsters, and breathtaking fight animation.",
    "Human: I’m looking for a relaxing slice of life.\nAI: Give Barakamon a try. It’s about a calligrapher learning life lessons on a rural island.",
    "Human: I loved the romance in Toradora.\nAI: You’d enjoy Golden Time — another heartfelt romance with comedy and drama.",
    "Human: I want something super emotional.\nAI: Clannad: After Story will definitely hit you in the feels.",
    "Human: I liked the mystery in Steins;Gate.\nAI: Erased (Boku dake ga Inai Machi) has a gripping time-travel mystery with emotional stakes.",
    "Human: I need a sports anime with hype moments.\nAI: Haikyuu!! is perfect — intense volleyball matches and inspiring teamwork.",
    "Human: I liked the worldbuilding in One Piece.\nAI: Try Hunter x Hunter — deep world, power system, and adventure vibes.",
    "Human: I want a short but powerful story.\nAI: Angel Beats! is only 13 episodes but leaves a lasting impact.",
    "Human: I want an isekai that isn’t cliché.\nAI: Re:Zero subverts a lot of tropes with darker twists and time-reset mechanics.",
    "Human: I enjoyed the political intrigue of Code Geass.\nAI: Legend of the Galactic Heroes is a must — sprawling space politics and strategy.",
    "Human: I want something funny and lighthearted.\nAI: Gintama mixes absurd comedy with surprisingly emotional arcs.",
    "Human: I liked the cyberpunk feel of Psycho-Pass.\nAI: Ghost in the Shell: Stand Alone Complex has similar dystopian and tech themes.",
    "Human: I want a wholesome romance.\nAI: My Love Story!! (Ore Monogatari!!) is pure sweetness and comedy.",
    "Human: I enjoyed the action in Attack on Titan.\nAI: Try Akame ga Kill! — dark battles, a rebellion theme, and shocking twists.",
    "Human: I want a dark, thought-provoking anime.\nAI: Texhnolyze is bleak and philosophical with cyberpunk vibes.",
    "Human: I loved the comedy in Konosuba.\nAI: Try Cautious Hero — it parodies isekai tropes with hilarious characters.",
    "Human: I liked the magic in Fullmetal Alchemist.\nAI: Try Magi: The Labyrinth of Magic — adventurous story and deep magic lore.",
    "Human: I want a relaxing food-centered anime.\nAI: Food Wars! (Shokugeki no Soma) combines cooking battles with fun characters.",
    "Human: I liked the intensity of Tokyo Ghoul.\nAI: Parasyte: The Maxim offers body horror, moral dilemmas, and alien fights.",
    "Human: I want something music-focused.\nAI: Your Lie in April is emotional and beautifully centered on music and healing.",
    "Human: I liked the quirky characters in One Punch Man.\nAI: Mob Psycho 100 has similar humor, stunning animation, and heartfelt growth.",
    "Human: I want an anime about traveling adventures.\nAI: Made in Abyss — a haunting but beautiful journey into a mysterious abyss.",
    "Human: I liked the horror vibe of Another.\nAI: Corpse Party has a terrifying school curse and plenty of scares.",
    "Human: I want an anime with deep philosophy.\nAI: Neon Genesis Evangelion blends mecha action with existential themes.",
    "Human: I loved the samurai theme of Rurouni Kenshin.\nAI: Samurai Champloo mixes sword fights with hip-hop culture.",
    "Human: I want a futuristic mecha series.\nAI: Darling in the Franxx blends mechs, romance, and emotional drama.",
    "Human: I liked the cuteness of K-On!.\nAI: Love Live! has a similar feel with idol music and friendship vibes.",
    "Human: I want a fast-paced thriller.\nAI: Terror in Resonance is short but packed with suspense and mystery.",
    "Human: I liked the comedy of Ouran High School Host Club.\nAI: Fruits Basket blends humor with emotional family drama.",
    "Human: I want a fantasy with strong worldbuilding.\nAI: The Rising of the Shield Hero is a solid choice with isekai fantasy elements.",
    "Human: I enjoyed the cleverness of Kaiji.\nAI: Akagi is another intense gambling anime with high stakes and strategy.",
    "Human: I want a magical girl anime.\nAI: Puella Magi Madoka Magica is dark, deconstructive, and unforgettable.",
    "Human: I liked the fighting style of Baki.\nAI: Kengan Ashura offers brutal martial arts battles with insane energy.",
    "Human: I want a historical anime.\nAI: Vinland Saga tells the story of Vikings, revenge, and redemption.",
    "Human: I liked the time travel in The Girl Who Leapt Through Time.\nAI: Try Orange — emotional time-travel themes tied to friendship.",
    "Human: I want a weird and surreal experience.\nAI: FLCL is bizarre, fast-paced, and full of symbolism.",
    "Human: I enjoyed the rivalry in Yu-Gi-Oh.\nAI: Try Cardfight!! Vanguard for more card battles with new twists.",
    "Human: I want a mystery-driven anime.\nAI: Higurashi: When They Cry blends horror, mystery, and psychological twists.",
    "Human: I liked the badass female leads in Kill la Kill.\nAI: Black Lagoon has gunfights, mercenaries, and a powerful female cast.",
    "Human: I want something about daily life.\nAI: Nichijou is an absurd slice of life with nonstop comedy.",
    "Human: I liked the sibling bond in No Game No Life.\nAI: The Devil is a Part-Timer! flips the isekai concept with comedy.",
    "Human: I want an anime centered on art.\nAI: Blue Period is a touching story about creativity and finding purpose.",
    "Human: I liked the battles in Bleach.\nAI: Try D.Gray-man — exorcists, demons, and epic fights.",
    "Human: I want an anime with a heartwarming vibe.\nAI: Natsume’s Book of Friends is gentle, emotional, and supernatural.",
    "Human: I liked the short storytelling in Death Parade.\nAI: Try Kino’s Journey — episodic tales with philosophical lessons.",
    "Human: I want something violent but meaningful.\nAI: Elfen Lied mixes gore with tragic character arcs.",
    "Human: I enjoyed the detective aspect of Detective Conan.\nAI: Try The Millionaire Detective — it’s stylish, fun, and mystery-driven.",
    "Human: I want a shounen with unique powers.\nAI: My Hero Academia offers quirks, training arcs, and heroic growth.",
    "Human: I liked Sword Art Online.\nAI: Try Log Horizon — it’s also about being trapped in an MMORPG but with a heavier focus on world-building and strategy.",
    "Human: I want a dark fantasy anime.\nAI: Berserk is a brutal classic with deep themes of struggle, ambition, and fate.",
    "Human: I loved the detective vibe of Monster.\nAI: Try Paranoia Agent — it’s mysterious, psychological, and thought-provoking.",
    "Human: I want an anime with giant robots.\nAI: Tengen Toppa Gurren Lagann is over-the-top, motivational, and full of mecha hype.",
    "Human: I liked the humor in Nichijou.\nAI: Asobi Asobase is another wild and chaotic comedy with schoolgirl antics.",
    "Human: I want an emotional romance story.\nAI: Anohana: The Flower We Saw That Day is a tearjerker about childhood friends reuniting.",
    "Human: I enjoyed the intensity of Akame ga Kill.\nAI: Try Guilty Crown — similar mix of rebellion, battles, and tragic moments.",
    "Human: I want a mystery with sci-fi elements.\nAI: Paprika is a surreal dive into dreams, tech, and the subconscious.",
    "Human: I liked the martial arts in Dragon Ball.\nAI: Yu Yu Hakusho is another shounen classic with spirit energy battles.",
    "Human: I want something about survival.\nAI: The Future Diary (Mirai Nikki) is a deadly survival game with diary powers.",
    "Human: I liked the cuteness in Lucky Star.\nAI: YuruYuri offers similar slice-of-life comedy with plenty of laughs.",
    "Human: I want a post-apocalyptic anime.\nAI: Try Ergo Proxy — dark, philosophical, and set in a ruined future.",
    "Human: I liked the rivalry in Hajime no Ippo.\nAI: Ashita no Joe is another legendary boxing anime with grit and drama.",
    "Human: I want a comedy isekai.\nAI: That Time I Got Reincarnated as a Slime blends fun humor with solid world-building.",
    "Human: I liked the plot twists in Death Note.\nAI: Try Zankyou no Terror (Terror in Resonance) for suspense and intrigue.",
    "Human: I want an anime with a band/music theme.\nAI: BECK: Mongolian Chop Squad follows a group chasing their rock dreams.",
    "Human: I enjoyed the feels in Violet Evergarden.\nAI: Plastic Memories has similar emotional storytelling with futuristic touches.",
    "Human: I want a sports anime outside the norm.\nAI: Ping Pong the Animation is artistic, psychological, and inspiring.",
    "Human: I liked the ninja vibe of Naruto.\nAI: Basilisk is a darker, bloodier take on ninja clans in conflict.",
    "Human: I want something with supernatural detectives.\nAI: Bungou Stray Dogs has a cast of powered investigators solving mysteries.",
    "Human: I liked the chaotic comedy of Gintama.\nAI: Sket Dance has a similar blend of humor, parody, and emotional arcs.",
    "Human: I want an anime about overcoming trauma.\nAI: March Comes in Like a Lion beautifully handles healing and growth.",
    "Human: I liked the action in Black Clover.\nAI: Blue Exorcist mixes magic, demons, and shounen-style fights.",
    "Human: I want something with androids or robots.\nAI: Chobits is a touching story about love and AI companions.",
    "Human: I liked the supernatural vibe of Noragami.\nAI: Try Kamisama Kiss — gods, spirits, and romance all in one.",
    "Human: I want an anime about family bonds.\nAI: Wolf Children explores motherhood and growing up with a magical twist.",
    "Human: I enjoyed the shock factor in Another.\nAI: Shiki has creepy atmosphere, vampires, and slow-burn horror.",
    "Human: I want a wild parody anime.\nAI: Excel Saga is absurd, self-aware, and totally unhinged.",
    "Human: I liked the art style of Devilman Crybaby.\nAI: Kaiba has a unique, surreal style with emotional storytelling.",
    "Human: I want something with strategy battles.\nAI: No Game No Life blends crazy colors with clever mind games.",
    "Human: I liked the heartfelt journey in Made in Abyss.\nAI: The Promised Neverland has a similar mix of kids, mystery, and survival.",
    "Human: I want a romantic comedy.\nAI: Lovely★Complex is hilarious and heartfelt with a tall-girl/short-guy duo.",
    "Human: I liked the assassins in Akame ga Kill.\nAI: Black Cat is about bounty hunters with stylish action and humor.",
    "Human: I want a coming-of-age story.\nAI: A Place Further Than the Universe follows girls chasing dreams to Antarctica.",
    "Human: I liked the tension in Erased.\nAI: Steins;Gate 0 expands the time-travel stakes in a darker direction.",
    "Human: I want something spooky but fun.\nAI: Soul Eater mixes gothic themes with action and comedy.",
    "Human: I liked the mecha action in Gundam.\nAI: Aldnoah.Zero gives modern animation and intense mech battles.",
    "Human: I want a wholesome friendship anime.\nAI: Non Non Biyori is slow-paced, cute, and all about small-town bonds.",
    "Human: I liked the mystery of Higurashi.\nAI: Umineko: When They Cry is another twisted mystery visual novel adaptation.",
    "Human: I want an anime that makes me laugh.\nAI: School Rumble is a romantic comedy with nonstop gags.",
    "Human: I liked the epic fights in Fate/Stay Night.\nAI: Fate/Zero is a prequel with darker storytelling and jaw-dropping animation.",
    "Human: I want something thought-provoking.\nAI: Ghost Hound dives into psychology, spirituality, and the supernatural.",
    "Human: I liked the wholesome moments in Fruits Basket.\nAI: Kimi ni Todoke is another sweet romance with a shy protagonist.",
    "Human: I want a seinen with depth.\nAI: 20th Century Boys is a mystery thriller about childhood friends facing a cult.",
    "Human: I liked the sci-fi of Cowboy Bebop.\nAI: Outlaw Star is another space adventure classic with fun characters.",
    "Human: I want something scary.\nAI: Hell Girl delivers dark, eerie tales of revenge and supernatural justice.",
    "Human: I liked the tension in Future Diary.\nAI: Darwin’s Game has another survival game with deadly stakes.",
    "Human: I want a funny harem anime.\nAI: Nisekoi blends comedy, romance, and quirky misunderstandings.",
    "Human: I liked the mystery of Serial Experiments Lain.\nAI: Boogiepop Phantom has a similar cryptic and eerie atmosphere.",
    "Human: I want a school-life comedy.\nAI: Great Teacher Onizuka is legendary for its humor and heart.",
    "Human: I liked the samurai fights in Samurai Champloo.\nAI: Afro Samurai delivers stylish sword fights with a killer soundtrack.",
    "Human: I liked the vibe of Cowboy Bebop.\nAI: Try Samurai Champloo — same director, slick action, and a unique hip-hop twist.",
    "Human: I want something with demons and exorcists.\nAI: Blue Exorcist is perfect — a shounen mix of action, family, and demons.",
    "Human: I loved the art in Violet Evergarden.\nAI: The Garden of Words by Makoto Shinkai has stunning visuals and a heartfelt story.",
    "Human: I want a comedy isekai with absurd humor.\nAI: Konosuba is a must-watch for hilarious party dynamics and parody.",
    "Human: I liked the tragedy in Devilman Crybaby.\nAI: Casshern Sins has a similar dark, apocalyptic, and emotional tone.",
    "Human: I want an anime with strong female leads.\nAI: Claymore delivers dark fantasy, sword fights, and badass warriors.",
    "Human: I liked the rivalry in My Hero Academia.\nAI: Try Fire Force — heroes, flames, and intense shounen rivalries.",
    "Human: I want something wholesome and calm.\nAI: Aria the Animation is a slow, beautiful slice-of-life in a water city.",
    "Human: I liked the mystery in Paranoia Agent.\nAI: Try Perfect Blue — a psychological thriller about identity and fame.",
    "Human: I want a feel-good romance.\nAI: Tsuredure Children offers short, sweet glimpses of high school couples.",
    "Human: I liked the theme of survival in The Promised Neverland.\nAI: Kaiji takes survival to gambling and high-stakes extremes.",
    "Human: I want an anime about samurai honor.\nAI: Shigurui is brutal, raw, and captures the darker side of samurai culture.",
    "Human: I liked the supernatural cases in Bungou Stray Dogs.\nAI: Hamatora has a similar detective + powers vibe.",
    "Human: I want a heartwarming family story.\nAI: Usagi Drop is touching and all about raising a child unexpectedly.",
    "Human: I liked the epic war vibe of Attack on Titan.\nAI: Try Kingdom — large-scale battles and strategies in ancient China.",
    "Human: I want a school romance comedy.\nAI: Toradora is a classic mix of laughs, heart, and teen drama.",
    "Human: I liked the weirdness of FLCL.\nAI: Kyousougiga has the same surreal, colorful chaos but with more family themes.",
    "Human: I want something about chasing dreams.\nAI: Shirobako follows a group of girls chasing careers in anime production.",
    "Human: I liked the tragic love in Your Lie in April.\nAI: Iroduku: The World in Colors is magical and bittersweet romance.",
    "Human: I want an anime with epic sword fights.\nAI: Sword of the Stranger has top-tier animation and a gripping duel.",
    "Human: I liked the survival theme in Darwin’s Game.\nAI: King’s Game is another deadly survival scenario with shocking twists.",
    "Human: I want something with deep psychological themes.\nAI: Welcome to the NHK explores paranoia, isolation, and otaku culture.",
    "Human: I liked the detective work in Psycho-Pass.\nAI: Un-Go is another futuristic mystery series with unique cases.",
    "Human: I want something funny and wacky.\nAI: Cromartie High School is ridiculous comedy with delinquent students.",
    "Human: I liked the heart in Barakamon.\nAI: Handa-kun is a comedic prequel about his awkward school life.",
    "Human: I want a fantasy with politics.\nAI: The Twelve Kingdoms is a deep fantasy world with strategy and rulers.",
    "Human: I liked the epic space vibe of Legend of the Galactic Heroes.\nAI: Planetes is a grounded space story about debris workers.",
    "Human: I want a pure action anime.\nAI: Black Lagoon is nonstop gunfights, mercenaries, and high-octane action.",
    "Human: I liked the music vibe in Nana.\nAI: Carole & Tuesday is a futuristic music journey with heartfelt songs.",
    "Human: I want something with monsters.\nAI: Ajin is dark, violent, and full of immortal creatures and conspiracies.",
    "Human: I liked the chill slice-of-life in Non Non Biyori.\nAI: Flying Witch is another slow, magical, and calming anime.",
    "Human: I want a battle shounen with grit.\nAI: Rave Master delivers action, adventure, and emotional fights.",
    "Human: I liked the horror aspect of Corpse Party.\nAI: Try School-Live! — starts cute, turns into survival horror.",
    "Human: I want something with gambling.\nAI: Kakegurui is flashy, stylish, and all about psychological bets.",
    "Human: I liked the coming-of-age in Blue Period.\nAI: Honey and Clover is another emotional story about youth and art.",
    "Human: I want an anime about reincarnation.\nAI: Mushoku Tensei is considered one of the best isekai reincarnation stories.",
    "Human: I liked the mind games in Kaiji.\nAI: One Outs is another psychological battle, but with baseball and contracts.",
    "Human: I want a war-focused mecha series.\nAI: 86 blends mech battles with discrimination and heavy themes.",
    "Human: I liked the creepy vibes in Shiki.\nAI: Try Ghost Hunt — supernatural cases with mystery and horror.",
    "Human: I want something about high school antics.\nAI: Daily Lives of High School Boys is all comedy and parody.",
    "Human: I liked the absurd humor in Excel Saga.\nAI: Pani Poni Dash! is chaotic and self-aware comedy.",
    "Human: I want a sad romance.\nAI: Ef: A Tale of Memories delivers emotional, dramatic love stories.",
    "Human: I liked the tragic battles in Fate/Zero.\nAI: Try Fate/Apocrypha for another Holy Grail War with epic fights.",
    "Human: I want something artistic and symbolic.\nAI: Mononoke (the anime, not the film) has unique art and mysterious tales.",
    "Human: I liked the assassin vibe of Black Lagoon.\nAI: Jormungand also follows arms dealers and mercenaries worldwide.",
    "Human: I want a wholesome friendship anime.\nAI: Tamako Market is lighthearted, colorful, and about community bonds.",
    "Human: I liked the card battles in Yu-Gi-Oh.\nAI: Selector Infected WIXOSS offers a darker take on card game battles.",
    "Human: I want an anime with stunning visuals.\nAI: Children of the Whales has breathtaking animation and emotional storytelling.",
    "Human: I liked the gothic vibe of Soul Eater.\nAI: D.Gray-man has similar dark action and exorcist themes.",
    "Human: I want something totally unpredictable.\nAI: Durarara!! mixes urban legends, gangs, and supernatural chaos in Ikebukuro.",
    "Human: I liked the nostalgia of Digimon.\nAI: Zatch Bell! has quirky monster partners and heartfelt shounen battles.",
    "Human: I liked the intense fights in Jujutsu Kaisen.\nAI: Try Chainsaw Man — it’s brutal, stylish, and full of chaotic energy.",
    "Human: I want a feel-good school romance.\nAI: Horimiya is a wholesome, modern love story with sweet character growth.",
    "Human: I liked the detective vibe in Erased.\nAI: The Great Pretender blends con artist schemes with colorful art and mystery.",
    "Human: I want a fantasy anime with gods.\nAI: Noragami mixes divine action, comedy, and heartfelt stories.",
    "Human: I liked the dreamlike quality of Paprika.\nAI: Millennium Actress is another Satoshi Kon masterpiece with surreal layers.",
    "Human: I want something about gaming.\nAI: Gamers! is a fun romantic comedy centered around misunderstandings and video games.",
    "Human: I liked the emotional storytelling in Angel Beats.\nAI: Charlotte is from the same creators and has a similar bittersweet vibe.",
    "Human: I want a show with unique worldbuilding.\nAI: Deca-Dence is a hidden gem with twists and a cool sci-fi setting.",
    "Human: I liked the darkness in Elfen Lied.\nAI: Try Gantz — violent, mature, and packed with survival battles.",
    "Human: I want a chill slice of life.\nAI: Hidamari Sketch is a cozy, artsy slice-of-life series.",
    "Human: I liked the power system in Hunter x Hunter.\nAI: World Trigger has strategic battles and an interesting ranking system.",
    "Human: I want an anime with tragic heroes.\nAI: Akame ga Kill! has many characters fighting doomed but powerful battles.",
    "Human: I liked the futuristic tech in Ghost in the Shell.\nAI: Psycho-Pass is another dystopian series with cyberpunk flair.",
    "Human: I want a story about idols.\nAI: The Idolmaster is a classic with lots of character variety and music.",
    "Human: I liked the family drama in Wolf Children.\nAI: Try Maquia: When the Promised Flower Blooms — heartfelt and emotional.",
    "Human: I want a battle anime with strategy.\nAI: Try Akame ga Kill! — dark rebellion with tactical fights.",
    "Human: I liked the sci-fi vibes in Ergo Proxy.\nAI: Texhnolyze has a similar bleak cyberpunk atmosphere.",
    "Human: I want a story about time manipulation.\nAI: Tokyo Revengers blends delinquent action with time travel.",
    "Human: I liked the quirky cast in Baccano!.\nAI: Durarara!! has the same chaotic energy and multiple perspectives.",
    "Human: I want a comedy anime with strong romance.\nAI: Wotakoi: Love is Hard for Otaku is sweet and funny for adult nerds.",
    "Human: I liked the tragic themes in Clannad.\nAI: Air is another emotional visual novel adaptation that will make you cry.",
    "Human: I want something with witches.\nAI: Little Witch Academia is magical, cheerful, and inspirational.",
    "Human: I liked the hero themes in My Hero Academia.\nAI: Tiger & Bunny also explores superheroes with a unique sponsorship twist.",
    "Human: I want an anime with magical duels.\nAI: Cardcaptor Sakura is a classic magical girl series with charm.",
    "Human: I liked the melancholy in Welcome to the NHK.\nAI: Oregairu (My Teen Romantic Comedy SNAFU) has a similar introspective tone.",
    "Human: I want a thriller with conspiracies.\nAI: Eden of the East mixes mystery, survival games, and politics.",
    "Human: I liked the cute daily life vibe in Lucky Star.\nAI: Azumanga Daioh is a classic comedy slice-of-life series.",
    "Human: I want a fantasy anime with adventure.\nAI: Slayers is a fun, classic fantasy full of humor and battles.",
    "Human: I liked the survival in The Future Diary.\nAI: Deadman Wonderland is another dark, violent survival anime.",
    "Human: I want a short and impactful anime.\nAI: Devilman Crybaby is only 10 episodes but unforgettable.",
    "Human: I liked the sci-fi mystery in Steins;Gate.\nAI: Robotics;Notes explores similar tech and conspiracies.",
    "Human: I want a bittersweet romance.\nAI: 5 Centimeters per Second is visually stunning and emotionally heavy.",
    "Human: I liked the monster hunting in Demon Slayer.\nAI: D.Gray-man has exorcists, demons, and emotional arcs.",
    "Human: I want something lighthearted with animals.\nAI: Chi’s Sweet Home is an adorable slice-of-life about a kitten.",
    "Human: I liked the rivalry in Bakuman.\nAI: Hikaru no Go has a similar theme of growth, rivalry, and strategy.",
    "Human: I want an anime with futuristic sports.\nAI: Air Gear is flashy, stylish, and packed with extreme sports action.",
    "Human: I liked the creepiness of Another.\nAI: Ghost Hunt has spooky supernatural investigations.",
    "Human: I want something with folklore.\nAI: Mononoke (the series) is eerie, artistic, and folklore-based.",
    "Human: I liked the mecha scale in Tengen Toppa Gurren Lagann.\nAI: Diebuster is another Gainax over-the-top mecha ride.",
    "Human: I want a romance anime that feels realistic.\nAI: Just Because! captures everyday emotions and subtle drama.",
    "Human: I liked the delinquent energy in Tokyo Revengers.\nAI: Great Teacher Onizuka has school chaos with comedy and heart.",
    "Human: I want an anime with detective cases.\nAI: Gosick blends mystery-solving with a gothic European setting.",
    "Human: I liked the feels in Anohana.\nAI: Orange is another emotional series dealing with regret and second chances.",
    "Human: I want an anime with gods and mythology.\nAI: Kamigami no Asobi blends romance and mythological characters.",
    "Human: I liked the chaos in Kill la Kill.\nAI: Panty & Stocking with Garterbelt is another stylish, insane ride.",
    "Human: I want something focused on mental health.\nAI: A Silent Voice handles bullying, guilt, and redemption beautifully.",
    "Human: I liked the epic action in Bleach.\nAI: InuYasha has fantasy fights, demons, and a nostalgic adventure vibe.",
    "Human: I want a detective thriller.\nAI: Spiral: The Bonds of Reasoning is a mystery anime with puzzles and suspense.",
    "Human: I liked the magical feel of Spirited Away.\nAI: Natsume’s Book of Friends is gentle, mystical, and emotional.",
    "Human: I liked the samurai vibe in Rurouni Kenshin.\nAI: Samurai Champloo has a modern twist with hip-hop flair and stylish duels.",
    "Human: I want an anime with strong female leads.\nAI: Claymore has powerful warriors fighting monstrous foes.",
    "Human: I liked the psychological tension in Monster.\nAI: Paranoia Agent is another deep dive into human fears and paranoia.",
    "Human: I want a fun cooking anime.\nAI: Food Wars! is flashy, competitive, and mouthwatering.",
    "Human: I liked the magical girl vibe in Sailor Moon.\nAI: Puella Magi Madoka Magica flips the genre with darker themes.",
    "Human: I want an anime with epic space battles.\nAI: Legend of the Galactic Heroes is the ultimate space opera.",
    "Human: I liked the emotional strength of Your Lie in April.\nAI: Kids on the Slope mixes jazz, youth, and heartfelt drama.",
    "Human: I want a quirky comedy.\nAI: Nichijou is absurd, random, and hilarious.",
    "Human: I liked the ghost theme in Natsume’s Book of Friends.\nAI: Mieruko-chan adds horror and comedy to the mix.",
    "Human: I want something with vampires.\nAI: Hellsing Ultimate is action-packed and gothic.",
    "Human: I liked the creativity in Soul Eater.\nAI: Blue Exorcist has demons, schools, and stylish battles.",
    "Human: I want an anime with survival elements.\nAI: Kaiji is all about gambling, tension, and life-or-death stakes.",
    "Human: I liked the futuristic vibe in Akira.\nAI: Blame! has a similar dystopian sci-fi atmosphere.",
    "Human: I want a romantic comedy with misunderstandings.\nAI: Toradora! is a classic with fiery chemistry.",
    "Human: I liked the supernatural fights in Yu Yu Hakusho.\nAI: Shaman King has spirit-based battles and tournaments.",
    "Human: I want something cute and musical.\nAI: K-On! is lighthearted and about forming a high school band.",
    "Human: I liked the tension in Death Note.\nAI: Future Diary has a similar survival and mind game vibe.",
    "Human: I want an anime with martial arts.\nAI: Kenichi: The Mightiest Disciple is about growth through tough training.",
    "Human: I liked the mysteries in Hyouka.\nAI: The Garden of Sinners is atmospheric and thought-provoking.",
    "Human: I want something about siblings.\nAI: No Game No Life has sibling geniuses taking on fantasy challenges.",
    "Human: I liked the cuteness in Barakamon.\nAI: Usagi Drop is another wholesome slice of life about family.",
    "Human: I want dark fantasy.\nAI: Berserk is legendary for its brutality and deep themes.",
    "Human: I liked the mecha fights in Code Geass.\nAI: Aldnoah.Zero has high-stakes mecha battles and politics.",
    "Human: I want an anime with animal characters.\nAI: Beastars mixes drama, romance, and anthropomorphic animals.",
    "Human: I liked the drama in Nana.\nAI: Paradise Kiss has a similar fashion-focused, dramatic energy.",
    "Human: I want to watch something with card battles.\nAI: Yu-Gi-Oh! is the classic with strategy and friendship.",
    "Human: I liked the cheerful vibe of Fruits Basket.\nAI: Kamisama Kiss has romance, comedy, and supernatural elements.",
    "Human: I want something about heroes of justice.\nAI: Gatchaman Crowds is stylish and asks what being a hero means.",
    "Human: I liked the fantasy in Magi.\nAI: Arabian Nights vibes continue in The Twelve Kingdoms with deep lore.",
    "Human: I want an anime with time loops.\nAI: Re:Zero is an intense series with brutal resets and drama.",
    "Human: I liked the detective work in Case Closed.\nAI: Tantei Gakuen Q has a similar focus on solving mysteries.",
    "Human: I want a lighthearted isekai.\nAI: KonoSuba is hilarious and pokes fun at the genre.",
    "Human: I liked the epic duels in Fate/Stay Night.\nAI: Fate/Zero expands the same universe with even higher stakes.",
    "Human: I want an anime with science themes.\nAI: Dr. Stone is all about rebuilding civilization with science.",
    "Human: I liked the bittersweet vibe of 5 Centimeters per Second.\nAI: Garden of Words is another Makoto Shinkai masterpiece.",
    "Human: I want something about yokai.\nAI: GeGeGe no Kitarou is a long-running classic full of monsters.",
    "Human: I liked the slow burn in March Comes in Like a Lion.\nAI: Honey and Clover is another heartfelt, thoughtful series.",
    "Human: I want a comedy anime with randomness.\nAI: School Rumble is chaotic and full of misunderstandings.",
    "Human: I liked the space exploration in Planetes.\nAI: Space Brothers is an inspiring, realistic space drama.",
    "Human: I want something gothic.\nAI: Black Butler has mystery, supernatural elements, and Victorian flair.",
    "Human: I liked the creepy vibe in Shiki.\nAI: Another has similar eerie suspense and death mysteries.",
    "Human: I want something artsy.\nAI: The Tatami Galaxy is experimental, witty, and visually unique.",
    "Human: I liked the slow slice of life in Non Non Biyori.\nAI: Aria the Animation is a serene series set on a water-covered planet.",
    "Human: I want something with rebellion themes.\nAI: Akame ga Kill! features a group fighting corrupt rulers.",
    "Human: I liked the over-the-top fights in JoJo’s Bizarre Adventure.\nAI: Gurren Lagann has the same wild energy.",
    "Human: I want a dark mystery.\nAI: Boogiepop Phantom is surreal, dark, and mysterious.",
    "Human: I liked the family bonds in Fullmetal Alchemist.\nAI: Fire Force also mixes bonds, powers, and mystery.",
    "Human: I want an anime with competitions.\nAI: Chihayafuru is about karuta but feels as intense as sports.",
    "Human: I liked the humor in Gintama.\nAI: Sket Dance is another comedy with school misfits helping others.",
    "Human: I want a heartwarming romance.\nAI: Lovely★Complex is funny, sweet, and heartfelt.",
    "Human: I liked the pirate adventure in One Piece.\nAI: Black Lagoon has a gritty, modern outlaw crew with tons of action.",
    "Human: I want a wholesome romance.\nAI: My Love Story!! is adorable with a gentle giant protagonist.",
    "Human: I liked the creepy atmosphere in Paranoia Agent.\nAI: Serial Experiments Lain is another surreal psychological classic.",
    "Human: I want something focused on sports teamwork.\nAI: Haikyuu!! captures the passion of volleyball and friendship.",
    "Human: I liked the quirky vibe of FLCL.\nAI: Kill la Kill carries the same chaotic energy and unique visuals.",
    "Human: I want something with assassins.\nAI: Akame ga Kill! has a team of assassins fighting corruption.",
    "Human: I liked the melancholy of Erased.\nAI: Orange mixes time travel and heartfelt drama in a school setting.",
    "Human: I want a magical academy story.\nAI: Little Witch Academia is fun, colorful, and uplifting.",
    "Human: I liked the dystopia in Psycho-Pass.\nAI: Ergo Proxy dives into dark philosophical cyberpunk themes.",
    "Human: I want a mix of comedy and action.\nAI: Blood Blockade Battlefront blends chaos, heart, and supernatural fights.",
    "Human: I liked the detective feel of Death Note.\nAI: The Perfect Insider has a murder mystery with intellectual battles.",
    "Human: I want a touching father-child bond.\nAI: Sweetness & Lightning is a heartwarming story about food and family.",
    "Human: I liked the cute café vibe in Is the Order a Rabbit?.\nAI: Blend S is another café-themed comedy with quirky characters.",
    "Human: I want an anime with gods.\nAI: Noragami is about a stray god taking on odd jobs in the human world.",
    "Human: I liked the intense duels in Yu-Gi-Oh!.\nAI: Cardfight!! Vanguard has a similar strategic card game focus.",
    "Human: I want an inspiring anime about art.\nAI: Blue Period is all about chasing passion through painting.",
    "Human: I liked the war strategy in Attack on Titan.\nAI: Kingdom is an epic tale of ancient Chinese warfare.",
    "Human: I want a quirky high school romance.\nAI: Maid Sama! is funny and full of chemistry.",
    "Human: I liked the meta humor in Gintama.\nAI: Excel Saga goes even further with absurd parody comedy.",
    "Human: I want a slow and contemplative series.\nAI: Mushishi is calming, mystical, and beautiful.",
    "Human: I liked the ghost story vibe in Another.\nAI: Hell Girl has chilling tales of vengeance and curses.",
    "Human: I want an anime with idols.\nAI: Love Live! is colorful and all about teamwork in music.",
    "Human: I liked the sibling rivalry in Blue Exorcist.\nAI: Twin Star Exorcists also deals with bonds and exorcism battles.",
    "Human: I want a samurai story with emotion.\nAI: Sword of the Stranger is a standalone masterpiece.",
    "Human: I liked the survival element in Darwin’s Game.\nAI: Btooom! is another survival game with high stakes.",
    "Human: I want a comedy about daily school life.\nAI: Azumanga Daioh is a classic slice-of-life comedy.",
    "Human: I liked the slow burn romance in Toradora!.\nAI: Golden Time is another heartfelt romance in college.",
    "Human: I want something with historical drama.\nAI: Vinland Saga brings Viking history to life with grit and emotion.",
    "Human: I liked the space adventures in Outlaw Star.\nAI: Cowboy Bebop has iconic bounty hunters in space.",
    "Human: I want an anime with mystery and music.\nAI: Carole & Tuesday mixes music with a futuristic setting.",
    "Human: I liked the philosophy in Ghost in the Shell.\nAI: Texhnolyze is another dark cyberpunk with deep themes.",
    "Human: I want a battle school anime.\nAI: A Certain Magical Index mixes magic, science, and fights.",
    "Human: I liked the heartfelt friendship in Clannad.\nAI: Anohana is another tearjerker about childhood bonds.",
    "Human: I want a lighthearted fantasy journey.\nAI: The World God Only Knows mixes romance, comedy, and fantasy twists.",
    "Human: I liked the sibling bond in No Game No Life.\nAI: Angel Beats! has teamwork, comedy, and emotional drama.",
    "Human: I want a vampire romance.\nAI: Vampire Knight blends gothic atmosphere with romance.",
    "Human: I liked the animal-human mix in Wolf’s Rain.\nAI: The Beast Player Erin has a similar mix of humans and beasts.",
    "Human: I want an anime with boxing.\nAI: Megalo Box is a modern take with futuristic gear-enhanced boxing.",
    "Human: I liked the chill vibe of Flying Witch.\nAI: Natsume’s Book of Friends has a similar cozy supernatural feel.",
    "Human: I want something with mysteries and riddles.\nAI: Rokka: Braves of the Six Flowers is a fantasy mystery with suspicion.",
    "Human: I liked the music competition in Kids on the Slope.\nAI: Your Lie in April is another beautiful music-focused anime.",
    "Human: I want an anime with revenge themes.\nAI: 91 Days is a mafia revenge story full of tension.",
    "Human: I liked the folklore in Inuyasha.\nAI: Mononoke explores Japanese spirits with unique art style.",
    "Human: I want an inspiring sports anime.\nAI: Run with the Wind captures the struggle of marathon training.",
    "Human: I liked the coming-of-age in March Comes in Like a Lion.\nAI: Baby Steps shows growth through tennis and perseverance.",
    "Human: I want a dark magical anime.\nAI: Witch Hunter Robin is mysterious and atmospheric.",
    "Human: I liked the fun adventures in Fairy Tail.\nAI: Rave Master has the same creator and a similar fun journey vibe.",
    "Human: I want a high-energy comedy.\nAI: Cromartie High School is pure absurd humor with delinquents.",
    "Human: I liked the betrayal themes in School Days.\nAI: Scum’s Wish is another messy, emotional romance drama.",
    "Human: I liked the pirate vibe in One Piece.\nAI: Try Treasure Island, it’s classic and inspired many pirate tales in anime.",
    "Human: I want a heartfelt anime about family.\nAI: Wolf Children is a beautiful story about motherhood and growing up.",
    "Human: I liked the futuristic setting of Akira.\nAI: Cyber City Oedo 808 has that same gritty cyberpunk energy.",
    "Human: I want a series with detective work.\nAI: Gosick mixes mystery-solving with historical drama.",
    "Human: I liked the survival aspect in Mirai Nikki.\nAI: Deadman Wonderland has twisted survival games with powers.",
    "Human: I want something with ninjas.\nAI: Basilisk is a darker take on warring ninja clans.",
    "Human: I liked the melancholy in 5 Centimeters per Second.\nAI: Iroduku: The World in Colors is visually stunning and emotional.",
    "Human: I want something funny and random.\nAI: Daily Lives of High School Boys is all about silly antics.",
    "Human: I liked the mystery in Erased.\nAI: Steins;Gate mixes time travel with thriller vibes.",
    "Human: I want a romance anime with a twist.\nAI: The Pet Girl of Sakurasou has quirky characters and heartfelt drama.",
    "Human: I liked the horror in Another.\nAI: Corpse Party is brutal, short, and terrifying.",
    "Human: I want an anime about legends.\nAI: Fate/Zero is full of heroic spirits clashing in epic battles.",
    "Human: I liked the sadness in Anohana.\nAI: Plastic Memories is another emotional tearjerker.",
    "Human: I want a sports anime with intensity.\nAI: Kuroko no Basket makes basketball feel like a shounen battle.",
    "Human: I liked the cooking in Food Wars.\nAI: Yakitate!! Japan is a hilarious bread-baking competition anime.",
    "Human: I want a slice of life with supernatural elements.\nAI: The Eccentric Family has magical creatures living everyday lives.",
    "Human: I liked the romance in Lovely★Complex.\nAI: Kimi ni Todoke is another sweet love story.",
    "Human: I want a fantasy with guilds and missions.\nAI: Orphen is a classic mage-focused adventure.",
    "Human: I liked the mind games in Death Note.\nAI: Akagi focuses on mahjong but with intense psychological battles.",
    "Human: I want a tragic romance.\nAI: Ef: A Tale of Memories is artistic and heartbreaking.",
    "Human: I liked the gritty fights in Black Lagoon.\nAI: Jormungand has mercenaries, guns, and shady business.",
    "Human: I want a story about overcoming weakness.\nAI: Hajime no Ippo shows incredible growth in boxing.",
    "Human: I liked the exploration in Made in Abyss.\nAI: Grimgar: Ashes and Illusions has a similar melancholic journey.",
    "Human: I want a musical adventure.\nAI: Beck is all about chasing dreams through rock music.",
    "Human: I liked the political drama in Legend of the Galactic Heroes.\nAI: Toward the Terra has space politics and war.",
    "Human: I want a supernatural detective anime.\nAI: UN-GO has unique mysteries and twists.",
    "Human: I liked the battle royale style of Btooom!.\nAI: Darwin’s Game updates that with a modern smartphone death game.",
    "Human: I want something based on folklore.\nAI: Spirited Away is a masterpiece of spirits and tradition.",
    "Human: I liked the emotional school life in Orange.\nAI: ReLIFE has a similar bittersweet tone about regrets.",
    "Human: I want an anime with androids.\nAI: Time of Eve is a thoughtful series about human-robot relationships.",
    "Human: I liked the gore in Elfen Lied.\nAI: Gantz is even bloodier with sci-fi battles.",
    "Human: I want a heartwarming slice of life.\nAI: A Place Further Than The Universe is inspiring and sweet.",
    "Human: I liked the gritty underworld in Banana Fish.\nAI: Black Lagoon scratches the same crime-action itch.",
    "Human: I want a high fantasy journey.\nAI: Record of Lodoss War is a classic D&D-style epic.",
    "Human: I liked the modern comedy of KonoSuba.\nAI: Cautious Hero parodies isekai with ridiculous humor.",
    "Human: I want an anime about books and stories.\nAI: Ascendance of a Bookworm is charming and creative.",
    "Human: I liked the quirky characters in Ouran High School Host Club.\nAI: Fruits Basket has romance and comedy with a supernatural twist.",
    "Human: I want something eerie and strange.\nAI: The Junji Ito Collection adapts some of his creepiest horror works.",
    "Human: I liked the intense pacing of Attack on Titan.\nAI: God Eater has similar vibes with humanity vs. monsters.",
    "Human: I want an anime about dreams.\nAI: Paprika is a wild movie exploring dreamscapes.",
    "Human: I liked the sibling drama in Oreimo.\nAI: Eromanga Sensei has another unusual sibling relationship story.",
    "Human: I want a comedy with delinquents.\nAI: Beelzebub mixes tough guys with absurd comedy.",
    "Human: I liked the strange visuals of The Tatami Galaxy.\nAI: Ping Pong the Animation has a similar experimental art style.",
    "Human: I want a revenge-driven anime.\nAI: Black Cat follows a hitman turned rebel.",
    "Human: I liked the bizarre stands in JoJo’s.\nAI: D.Gray-man has unique powers and dark battles.",
    "Human: I want a relaxing, cozy anime.\nAI: Laid-Back Camp is perfect for chill outdoor vibes.",
    "Human: I liked the fashion drama in Paradise Kiss.\nAI: Nana also deals with music, fashion, and relationships.",
    "Human: I want a weird, trippy anime.\nAI: Kaiba has surreal visuals and deep emotional themes.",
    "Human: I liked the smart characters in Code Geass.\nAI: Zetsuen no Tempest mixes strategy, magic, and Shakespeare vibes.",
    "Human: I want something funny but with heart.\nAI: Try Gintama! It’s packed with comedy but still sneaks in emotional arcs that hit hard.",
    "Human: Recommend me something like Death Note.\nAI: Check out Code Geass! Strategic battles, moral dilemmas, and a protagonist with godlike powers.",
    "Human: I loved Fullmetal Alchemist, what next?\nAI: Watch Attack on Titan! Dark themes, mysteries, and humanity’s survival are at the forefront.",
    "Human: I want a wholesome slice of life.\nAI: Try Barakamon! It’s about an artist finding inspiration in a small village, heartwarming and uplifting.",
    "Human: Any anime with music?\nAI: Your Lie in April is perfect. Emotional piano and violin performances drive the story.",
    "Human: Give me a sports anime.\nAI: Try Haikyuu!! A volleyball series full of hype matches, teamwork, and growth.",
    "Human: I need an anime with strong female characters.\nAI: Kill la Kill delivers with action, style, and powerful heroines.",
    "Human: I want something psychological.\nAI: Monster is an intense thriller with deep moral questions and suspense.",
    "Human: Suggest me a romance anime.\nAI: Toradora! is a touching romantic comedy with lovable characters.",
    "Human: I’m into sci-fi worlds.\nAI: Steins;Gate mixes time travel with gripping storytelling.",
    "Human: Any horror anime?\nAI: Try Another. Creepy atmosphere and a deadly curse at a high school.",
    "Human: I want to laugh non-stop.\nAI: Nichijou is absurd, surreal comedy that’s hilarious start to finish.",
    "Human: Recommend me a fantasy adventure.\nAI: Magi: The Labyrinth of Magic has magic, kingdoms, and grand adventures.",
    "Human: I liked Demon Slayer.\nAI: Try Blue Exorcist! It has supernatural battles and brotherly bonds.",
    "Human: I want something chill.\nAI: Laid-Back Camp is cozy and perfect for relaxing vibes.",
    "Human: Any anime with samurai?\nAI: Samurai Champloo blends Edo-period samurai with hip-hop flair.",
    "Human: Suggest a romance with drama.\nAI: Clannad: After Story will break your heart and heal it again.",
    "Human: I like mecha.\nAI: Evangelion is iconic with deep themes and giant robot battles.",
    "Human: I need something weird and unique.\nAI: FLCL is a wild, stylish ride with surreal humor.",
    "Human: Give me a dark fantasy.\nAI: Berserk delivers raw, brutal storytelling with deep characters.",
    "Human: I want something short and impactful.\nAI: Erased is only 12 episodes and blends thriller with emotional drama.",
    "Human: Recommend me a cooking anime.\nAI: Food Wars! mixes comedy, competition, and mouthwatering dishes.",
    "Human: I want a coming-of-age story.\nAI: Anohana explores childhood friends reuniting after tragedy.",
    "Human: I like magic school settings.\nAI: Little Witch Academia is fun, bright, and adventurous.",
    "Human: I want a romance with supernatural elements.\nAI: Nisekoi blends comedy, romance, and quirky characters.",
    "Human: Suggest me a detective anime.\nAI: Gosick is a mystery anime with gothic vibes and clever cases.",
    "Human: I want something relaxing with nature.\nAI: Mushishi is slow, meditative, and deeply atmospheric.",
    "Human: I like survival stories.\nAI: Highschool of the Dead combines survival horror with action.",
    "Human: I want something with gods.\nAI: Noragami has action, humor, and divine battles.",
    "Human: I liked Cowboy Bebop.\nAI: Try Trigun! Gunslinging action with humor and emotional depth.",
    "Human: I want romance and comedy.\nAI: Lovely★Complex is hilarious and heartwarming.",
    "Human: Recommend me a sad anime.\nAI: Plastic Memories is a tearjerker with android-human bonds.",
    "Human: I like mystery thrillers.\nAI: Higurashi: When They Cry is dark, unsettling, and full of twists.",
    "Human: I want something artsy.\nAI: The Tatami Galaxy is visually creative and philosophical.",
    "Human: Any idol anime?\nAI: Love Live! combines music, friendship, and cheerful performances.",
    "Human: I want an anime about games.\nAI: No Game No Life features sibling prodigies in a world ruled by games.",
    "Human: Recommend me a feel-good romance.\nAI: My Love Story!! is wholesome, sweet, and funny.",
    "Human: I want something edgy.\nAI: Elfen Lied is violent, emotional, and intense.",
    "Human: Any anime with cute girls doing cute things?\nAI: K-On! is the classic music club slice of life.",
    "Human: I want something with a mystery twist.\nAI: Paranoia Agent explores society through surreal mysteries.",
    "Human: Recommend me a war anime.\nAI: Legend of the Galactic Heroes is an epic space opera with political depth.",
    "Human: I liked Tokyo Ghoul.\nAI: Ajin is another dark, supernatural survival story.",
    "Human: I want a feel-good slice of life.\nAI: Fruits Basket is warm, emotional, and magical.",
    "Human: Any anime with vampires?\nAI: Hellsing Ultimate is violent, stylish, and action-packed.",
    "Human: I want something nostalgic.\nAI: Digimon Adventure brings classic adventure and heart.",
    "Human: I liked Sword Art Online.\nAI: Log Horizon explores MMORPG worlds with strategy and community.",
    "Human: I want something absurd and random.\nAI: Pop Team Epic is chaotic and meme-filled.",
    "Human: Recommend me something about yokai.\nAI: Natsume’s Book of Friends is gentle, emotional, and supernatural.",
    "Human: I like historical anime.\nAI: Vinland Saga brings Viking drama and epic storytelling.",
    "Human: I want a time travel anime.\nAI: Tokyo Revengers is packed with gang conflicts and time leaps.",
    "Human: I want something like One Piece.\nAI: Try Fairy Tail! It has a big cast, adventure, and strong themes of friendship and loyalty.",
    "Human: Recommend me a mecha anime with politics.\nAI: Aldnoah.Zero mixes giant robots with intense political conflict and strategy.",
    "Human: I want a tearjerker.\nAI: Angel Beats! blends comedy, action, and heart-wrenching drama.",
    "Human: Any anime about bounty hunters?\nAI: Outlaw Star has space action, quirky characters, and bounty-hunting adventures.",
    "Human: I like mind games.\nAI: Kaiji is all about psychological battles and high-stakes gambling.",
    "Human: Suggest me a comedy romance.\nAI: Monthly Girls’ Nozaki-kun is hilarious with lovable characters and misunderstandings.",
    "Human: I want something spooky but short.\nAI: Yamishibai delivers creepy urban legends in bite-sized episodes.",
    "Human: I enjoyed Attack on Titan.\nAI: Try Claymore, another dark fantasy with warriors battling monsters.",
    "Human: I need a music-focused anime.\nAI: Beck: Mongolian Chop Squad is about a rock band chasing their dreams.",
    "Human: Recommend me a fantasy romance.\nAI: Spice and Wolf blends economics, adventure, and a heartfelt romance.",
    "Human: I want an anime with martial arts.\nAI: Baki the Grappler is intense, brutal, and showcases martial arts at the extreme.",
    "Human: Any anime about artists?\nAI: Blue Period follows a teen discovering his passion for painting.",
    "Human: I want a magical girl anime.\nAI: Puella Magi Madoka Magica twists the genre into something dark and profound.",
    "Human: Suggest me a food-themed anime.\nAI: Sweetness and Lightning is wholesome, focusing on cooking and family bonds.",
    "Human: I liked Dr. Stone.\nAI: Ascendance of a Bookworm has a protagonist rebuilding knowledge in a medieval setting.",
    "Human: I want a fantasy with guilds.\nAI: Grimgar: Ashes and Illusions offers a grounded, emotional take on fantasy adventuring.",
    "Human: Recommend me an anime with detectives.\nAI: The Millionaire Detective: Balance Unlimited mixes crime-solving with comedy and luxury.",
    "Human: I want a romantic drama.\nAI: Orange is about love, regret, and second chances with a sci-fi twist.",
    "Human: Any anime about hackers?\nAI: Eden of the East is a stylish thriller involving cell phones and conspiracies.",
    "Human: I liked Psycho-Pass.\nAI: Try Ergo Proxy, a dark cyberpunk series full of mystery and philosophy.",
    "Human: I want a revenge-driven anime.\nAI: 91 Days is a mafia revenge story set during Prohibition.",
    "Human: Suggest me a supernatural comedy.\nAI: The Devil is a Part-Timer! mixes demon lords with everyday part-time jobs.",
    "Human: I like overpowered main characters.\nAI: The Irregular at Magic High School has an OP protagonist in a magic academy.",
    "Human: Recommend me a relaxing slice of life.\nAI: Non Non Biyori is slow-paced, cute, and calming.",
    "Human: I want a fantasy romance with action.\nAI: Akame ga Kill! balances dark action and emotional relationships.",
    "Human: Any anime with gambling?\nAI: Kakegurui features stylish and intense gambling battles.",
    "Human: I want something lighthearted and fun.\nAI: Lucky Star is comedic and full of otaku humor.",
    "Human: Suggest me a space adventure.\nAI: Planetes is realistic and moving, focusing on space debris workers.",
    "Human: I liked Neon Genesis Evangelion.\nAI: RahXephon has mechas, mysteries, and music-based powers.",
    "Human: I want a romantic fantasy.\nAI: The Ancient Magus’ Bride is dark yet beautiful, mixing love and magic.",
    "Human: Recommend me a supernatural shoujo.\nAI: Kamisama Kiss is charming with romance and gods.",
    "Human: I want anime with unique animation.\nAI: Ping Pong the Animation has a bold art style and deep storytelling.",
    "Human: Suggest me a futuristic romance.\nAI: Plastic Memories mixes sci-fi with heart-wrenching love stories.",
    "Human: I liked Hunter x Hunter.\nAI: World Trigger has strategy-driven battles and teamwork-focused arcs.",
    "Human: I want a school romance.\nAI: Kokoro Connect explores relationships with a supernatural body-swap twist.",
    "Human: Any anime with spirits?\nAI: xxxHOLiC combines supernatural elements with unique storytelling.",
    "Human: Recommend me a fantasy world with humor.\nAI: Konosuba is a hilarious parody of RPG adventures.",
    "Human: I want something trippy.\nAI: Paprika is a movie that inspired Inception with dream-based visuals.",
    "Human: Suggest me a workplace anime.\nAI: Servant x Service is a comedy about civil servants in Japan.",
    "Human: I liked Black Clover.\nAI: Fairy Tail also has guilds, magic, and strong bonds between friends.",
    "Human: I want a tragedy.\nAI: School Days is infamous for its dramatic and tragic love triangle.",
    "Human: Recommend me a short romance.\nAI: Tsuredure Children is full of short but sweet love stories.",
    "Human: I want an anime about war tactics.\nAI: The Saga of Tanya the Evil mixes reincarnation with military strategy.",
    "Human: Suggest me a heartwarming anime.\nAI: Usagi Drop is wholesome and focuses on parenting.",
    "Human: I liked Re:Zero.\nAI: Try The Rising of the Shield Hero for another isekai survival journey.",
    "Human: I want a vampire romance.\nAI: Vampire Knight blends drama, romance, and gothic aesthetics.",
    "Human: Recommend me an anime with competitions.\nAI: Chihayafuru mixes card games with passion and character growth.",
    "Human: I want something with gods and myths.\nAI: Fate/Stay Night and the Fate franchise bring mythological heroes to life.",
    "Human: Any anime about traveling?\nAI: Kino’s Journey explores philosophical questions through episodic adventures.",
    "Human: I liked Spirited Away.\nAI: Try Princess Mononoke, another Studio Ghibli masterpiece with deep themes.",
    "Human: I loved Tokyo Ghoul\nAI: Check out Parasyte: The Maxim! It explores humanity, morality, and the struggle of living with a monstrous side, with intense action and emotional depth.",
    "Human: I want something like One Punch Man\nAI: Try Mob Psycho 100! It’s from the same creator, mixing humor, incredible fights, and surprisingly heartfelt storytelling.",
    "Human: I enjoyed Haikyuu!!\nAI: You’ll love Kuroko’s Basketball! It’s got the same passion, teamwork, and dramatic sports moments that keep you hooked.",
    "Human: Recommend me something like Death Parade\nAI: Give Ergo Proxy a try! It’s dark, philosophical, and questions human identity in a similar way.",
    "Human: I liked Cowboy Bebop\nAI: You should watch Samurai Champloo! It has the same director and blends stylish action with a killer soundtrack.",
    "Human: I liked Demon Slayer\nAI: Try Jujutsu Kaisen! It has stunning animation, cursed techniques, and strong emotional core around friends and loss.",
    "Human: I loved Angel Beats\nAI: Check out Charlotte! It’s by the same creator, with teens discovering special powers and facing bittersweet consequences.",
    "Human: I liked Fairy Tail\nAI: Give Black Clover a shot! It’s full of magic, guild vibes, and that same never-give-up energy.",
    "Human: I enjoyed Your Lie in April\nAI: Try Anohana: The Flower We Saw That Day. It’s another tearjerker about grief, friendship, and moving on.",
    "Human: I loved Sword Art Online\nAI: You’ll like Log Horizon! It focuses more on the world-building and strategies of living inside an MMO.",
    "Human: I liked Akame ga Kill\nAI: Check out Future Diary! Both are survival stories with shocking twists and high-stakes battles.",
    "Human: I want something like Psycho-Pass\nAI: Try Ghost in the Shell: Stand Alone Complex! It’s also about tech, society, and moral dilemmas.",
    "Human: I liked The Seven Deadly Sins\nAI: You should try Magi: The Labyrinth of Magic. It’s a fantasy with colorful characters, big battles, and adventure.",
    "Human: I liked Fruits Basket\nAI: Try Natsume’s Book of Friends! Both explore emotional healing, bonds, and a touch of the supernatural.",
    "Human: I enjoyed Dr. Stone\nAI: Watch Cells at Work! It’s educational, fun, and shows fascinating science through action-packed storytelling.",
    "Human: I liked Code Geass\nAI: Try Guilty Crown! It has rebellion themes, mechs, and a protagonist with a mysterious power.",
    "Human: I enjoyed Noragami\nAI: Give Blue Exorcist a try! Both follow a teen linked to gods/demons, balancing humor with action.",
    "Human: I liked Erased\nAI: You’ll like Steins;Gate. It’s another mind-bending thriller about time, regret, and changing fate.",
    "Human: I enjoyed Fire Force\nAI: Try Soul Eater! Both have stylized animation, dark supernatural fights, and a unique vibe.",
    "Human: I loved Darling in the Franxx\nAI: Check out Neon Genesis Evangelion! Both are mecha with deep psychological and emotional themes.",
    "Human: I liked Great Teacher Onizuka\nAI: Watch Assassination Classroom! It’s also about an unconventional teacher changing students’ lives.",
    "Human: I enjoyed Clannad\nAI: Try Kanon (2006)! It’s another emotional drama from the same studio that’ll tug at your heartstrings.",
    "Human: I liked Goblin Slayer\nAI: You’ll love Grimgar: Ashes and Illusions. It’s another grounded fantasy with survival themes.",
    "Human: I liked Toradora\nAI: Try Golden Time! It’s a heartfelt romance with similar character-driven drama.",
    "Human: I enjoyed Kill la Kill\nAI: Try Gurren Lagann! Both are over-the-top, high-energy anime with wild fights and inspiration.",
    "Human: I loved Monster\nAI: You’ll like Paranoia Agent! It’s another psychological thriller with dark themes and human struggles.",
    "Human: I liked Attack on Titan\nAI: Give Claymore a shot! It’s about humanity’s fight against monstrous beings with dark tones.",
    "Human: I loved Re:Zero\nAI: Try The Rising of the Shield Hero! Both follow an isekai protagonist struggling against impossible odds.",
    "Human: I liked Trigun\nAI: You’ll enjoy Gungrave! It mixes gunslinging action with emotional storytelling.",
    "Human: I enjoyed K-On!\nAI: Try Love Live! It’s another lighthearted series about girls chasing their musical dreams.",
    "Human: I liked Baccano!\nAI: You should try Durarara!! It shares the same writer and chaotic storytelling style.",
    "Human: I loved Neon Genesis Evangelion\nAI: Watch RahXephon! It’s another mecha series with psychological depth.",
    "Human: I liked The Devil is a Part-Timer\nAI: Try Konosuba! Both are comedic takes on fantasy with loveable misfits.",
    "Human: I enjoyed Hellsing\nAI: Watch Black Lagoon! Both are gritty action anime with dark anti-heroes.",
    "Human: I liked Made in Abyss\nAI: Try The Ancient Magus’ Bride! Both blend mystery, fantasy, and emotional depth.",
    "Human: I loved School Rumble\nAI: Check out Ouran High School Host Club! Both are funny school-based rom-coms.",
    "Human: I liked Barakamon\nAI: You’ll love March Comes in Like a Lion. It’s another character-driven story about growth and healing.",
    "Human: I enjoyed Elfen Lied\nAI: Try Another! Both are dark, bloody, and tragic with shocking twists.",
    "Human: I loved Bakuman\nAI: Watch Shirobako! Both are about chasing creative dreams in anime/manga production.",
    "Human: I liked Nana\nAI: Try Paradise Kiss! Both dive into adult relationships and the fashion/arts scene.",
    "Human: I enjoyed Akira\nAI: Try Blame! Both are dystopian sci-fi with cyberpunk aesthetics.",
    "Human: I liked Hyouka\nAI: Watch Gosick! Both are mystery-solving school dramas with charming duos.",
    "Human: I loved InuYasha\nAI: Try Rurouni Kenshin! Both are historical fantasy action with heartfelt romance.",
    "Human: I liked Devilman Crybaby\nAI: You’ll love Texhnolyze. Both are dark, experimental, and heavy on tragedy.",
    "Human: I enjoyed ReLIFE\nAI: Try Orange! Both are about second chances, regret, and the power of friendships.",
    "Human: I liked Spirited Away\nAI: Check out Princess Mononoke! Both are Studio Ghibli masterpieces full of wonder and moral depth.",
    "Human: I loved Whisper of the Heart\nAI: Try The Cat Returns! It’s a whimsical follow-up with similar charm.",
    "Human: I liked Ascendance of a Bookworm\nAI: Try Log Horizon! Both show smart characters adapting creatively to a fantasy world.",
    "Human: I enjoyed Black Bullet\nAI: You’ll love C: The Money of Soul and Possibility Control. Both blend action and dystopian futures.",
    "Human: I liked Monster Rancher\nAI: Try Digimon! Both mix adventure, battles, and a bond with creatures.",
    "Human: I want an anime about samurai\nAI: Check out Samurai Champloo! It blends Edo-period samurai action with hip-hop culture for a stylish and unforgettable journey.",
    "Human: Recommend me something like Dragon Ball Z\nAI: Fairy Tail might be your vibe! It’s got wild battles, friendship power-ups, and an endless sense of adventure.",
    "Human: Any anime like One Piece?\nAI: Black Clover could work! It’s about aspiring wizards aiming for the top, with tons of battles, teamwork, and determination.",
    "Human: I loved Code Geass, what’s next?\nAI: Try Death Note! It’s another smart psychological thriller about two geniuses battling with strategy and ideology.",
    "Human: I want more cute slice-of-life anime\nAI: K-On! is perfect — a lighthearted series about girls starting a band while living their best school life.",
    "Human: Give me a good romance anime\nAI: Toradora! is a heartwarming rom-com with great character development and an emotional payoff.",
    "Human: Got anything like Attack on Titan?\nAI: You might enjoy Seraph of the End. Humanity is on the brink after a catastrophe, and the fight for survival is intense.",
    "Human: Suggest something similar to Fullmetal Alchemist\nAI: Try Magi: The Labyrinth of Magic. It’s full of alchemy-like magic, epic battles, and emotional storytelling.",
    "Human: I want a mind-bending anime\nAI: Steins;Gate will blow your mind with its time travel plot and emotional twists.",
    "Human: Give me an anime with badass fights\nAI: Demon Slayer is a must! Gorgeous animation, intense battles, and heartfelt moments make it legendary.",
    "Human: Something like Tokyo Ghoul please\nAI: Try Parasyte: The Maxim. It’s another dark series with humans fighting monstrous beings while questioning morality.",
    "Human: Recommend me a short, impactful anime\nAI: Erased is only 12 episodes but delivers a gripping time-travel mystery mixed with heartfelt drama.",
    "Human: I want a comedy anime\nAI: Gintama is the king of comedy anime! It’s full of parodies, slapstick, and surprisingly emotional arcs.",
    "Human: Any sports anime you recommend?\nAI: Haikyuu!! is perfect — volleyball, teamwork, and hype matches that will get you pumped up.",
    "Human: Suggest a dark psychological anime\nAI: Monster is a slow-burn thriller about morality, identity, and obsession. Truly chilling.",
    "Human: I want a wholesome family anime\nAI: Barakamon is a sweet story about an artist who grows while living with a lively rural community.",
    "Human: Got anything fantasy-heavy?\nAI: Re:Zero is intense with time loops, magic, and gut-punch emotional stakes in a fantasy world.",
    "Human: I liked Cowboy Bebop\nAI: You might enjoy Trigun. It’s got a wandering gunslinger with a mysterious past in a space-western setting.",
    "Human: Give me something like Hunter x Hunter\nAI: World Trigger might hit the spot! Strategic battles, big power systems, and a strong team-focused narrative.",
    "Human: Recommend me a school romance\nAI: My Teen Romantic Comedy SNAFU has witty dialogue and deep looks into teen relationships.",
    "Human: I want a dark fantasy anime\nAI: Try Berserk (1997 or movies) for a gritty medieval fantasy with tragic themes and epic battles.",
    "Human: Suggest an anime with amazing visuals\nAI: Violet Evergarden is breathtaking with its animation and emotional storytelling.",
    "Human: Any anime like Sword Art Online?\nAI: Log Horizon is another trapped-in-MMORPG anime, but it dives deeper into strategy and world-building.",
    "Human: Recommend a feel-good anime\nAI: Natsume’s Book of Friends is a calming, heartwarming series about spirits and kindness.",
    "Human: Something with badass female leads?\nAI: Kill la Kill is stylish, action-packed, and full of powerful female characters.",
    "Human: I want an anime about friendship\nAI: Anohana is a tearjerker about childhood friends reconnecting after a tragedy.",
    "Human: Give me an underrated anime\nAI: The Great Pretender is a stylish con-artist story with slick visuals and clever scams.",
    "Human: I want a mech anime\nAI: Gundam 00 is a modern mecha series with political intrigue, amazing battles, and strong characters.",
    "Human: Recommend me a tragic anime\nAI: Your Lie in April will break your heart with its music, romance, and emotional storytelling.",
    "Human: I want a revenge story\nAI: Akame ga Kill delivers with dark battles, assassins, and an unforgiving world.",
    "Human: Got anything mysterious?\nAI: The Garden of Sinners is full of supernatural mysteries, eerie vibes, and gorgeous visuals.",
    "Human: I want an anime about samurai\nAI: Check out Samurai Champloo! It blends Edo-period samurai action with hip-hop culture for a stylish and unforgettable journey.",
    "Human: Recommend me something like Dragon Ball Z\nAI: Fairy Tail might be your vibe! It’s got wild battles, friendship power-ups, and an endless sense of adventure.",
    "Human: Any anime like One Piece?\nAI: Black Clover could work! It’s about aspiring wizards aiming for the top, with tons of battles, teamwork, and determination.",
    "Human: I loved Code Geass, what’s next?\nAI: Try Death Note! It’s another smart psychological thriller about two geniuses battling with strategy and ideology.",
    "Human: I want more cute slice-of-life anime\nAI: K-On! is perfect — a lighthearted series about girls starting a band while living their best school life.",
    "Human: Give me a good romance anime\nAI: Toradora! is a heartwarming rom-com with great character development and an emotional payoff.",
    "Human: Got anything like Attack on Titan?\nAI: You might enjoy Seraph of the End. Humanity is on the brink after a catastrophe, and the fight for survival is intense.",
    "Human: Suggest something similar to Fullmetal Alchemist\nAI: Try Magi: The Labyrinth of Magic. It’s full of alchemy-like magic, epic battles, and emotional storytelling.",
    "Human: I want a mind-bending anime\nAI: Steins;Gate will blow your mind with its time travel plot and emotional twists.",
    "Human: Give me an anime with badass fights\nAI: Demon Slayer is a must! Gorgeous animation, intense battles, and heartfelt moments make it legendary.",
    "Human: Something like Tokyo Ghoul please\nAI: Try Parasyte: The Maxim. It’s another dark series with humans fighting monstrous beings while questioning morality.",
    "Human: Recommend me a short, impactful anime\nAI: Erased is only 12 episodes but delivers a gripping time-travel mystery mixed with heartfelt drama.",
    "Human: I want a comedy anime\nAI: Gintama is the king of comedy anime! It’s full of parodies, slapstick, and surprisingly emotional arcs.",
    "Human: Any sports anime you recommend?\nAI: Haikyuu!! is perfect — volleyball, teamwork, and hype matches that will get you pumped up.",
    "Human: Suggest a dark psychological anime\nAI: Monster is a slow-burn thriller about morality, identity, and obsession. Truly chilling.",
    "Human: I want a wholesome family anime\nAI: Barakamon is a sweet story about an artist who grows while living with a lively rural community.",
    "Human: Got anything fantasy-heavy?\nAI: Re:Zero is intense with time loops, magic, and gut-punch emotional stakes in a fantasy world.",
    "Human: I liked Cowboy Bebop\nAI: You might enjoy Trigun. It’s got a wandering gunslinger with a mysterious past in a space-western setting.",
    "Human: Give me something like Hunter x Hunter\nAI: World Trigger might hit the spot! Strategic battles, big power systems, and a strong team-focused narrative.",
    "Human: Recommend me a school romance\nAI: My Teen Romantic Comedy SNAFU has witty dialogue and deep looks into teen relationships.",
    "Human: I want a dark fantasy anime\nAI: Try Berserk (1997 or movies) for a gritty medieval fantasy with tragic themes and epic battles.",
    "Human: Suggest an anime with amazing visuals\nAI: Violet Evergarden is breathtaking with its animation and emotional storytelling.",
    "Human: Any anime like Sword Art Online?\nAI: Log Horizon is another trapped-in-MMORPG anime, but it dives deeper into strategy and world-building.",
    "Human: Recommend a feel-good anime\nAI: Natsume’s Book of Friends is a calming, heartwarming series about spirits and kindness.",
    "Human: Something with badass female leads?\nAI: Kill la Kill is stylish, action-packed, and full of powerful female characters.",
    "Human: I want an anime about friendship\nAI: Anohana is a tearjerker about childhood friends reconnecting after a tragedy.",
    "Human: Give me an underrated anime\nAI: The Great Pretender is a stylish con-artist story with slick visuals and clever scams.",
    "Human: I want a mech anime\nAI: Gundam 00 is a modern mecha series with political intrigue, amazing battles, and strong characters.",
    "Human: Recommend me a tragic anime\nAI: Your Lie in April will break your heart with its music, romance, and emotional storytelling.",
    "Human: I want a revenge story\nAI: Akame ga Kill delivers with dark battles, assassins, and an unforgiving world.",
    "Human: Got anything mysterious?\nAI: The Garden of Sinners is full of supernatural mysteries, eerie vibes, and gorgeous visuals.",
    "Human: Suggest a thriller anime\nAI: Future Diary is an intense death game anime with high stakes and a wild cast of characters.",
    "Human: I want a relaxing anime\nAI: Laid-Back Camp is cozy, chill, and full of camping adventures with friends.",
    "Human: Recommend an anime about survival\nAI: Btooom! mixes survival games with strategy and action in a deadly island setting.",
    "Human: I need a legendary shounen\nAI: Yu Yu Hakusho is a classic! Spirit battles, tournaments, and 90s charm all in one.",
    "Human: Give me an anime with strong world-building\nAI: Made in Abyss has an insanely detailed world, plus an emotional rollercoaster of a story.",
    "Human: I want a weird anime\nAI: FLCL is bizarre, stylish, and unforgettable — giant robots, coming-of-age themes, and wild animation.",
    "Human: Suggest a martial arts anime\nAI: Baki is raw, brutal, and full of insane hand-to-hand fights.",
    "Human: I want something with time travel\nAI: The Girl Who Leapt Through Time is a classic blend of romance, sci-fi, and drama.",
    "Human: Got any detective-style anime?\nAI: Detective Conan is long-running and full of clever mysteries and cases.",
    "Human: Recommend me an anime like Bleach\nAI: Blue Exorcist has demons, exorcists, and lots of shounen-style action.",
    "Human: I want an anime with deep themes\nAI: Ghost in the Shell is a cyberpunk masterpiece exploring humanity and technology.",
    "Human: Suggest a war anime\nAI: 86 is a powerful mecha-war series with themes of discrimination, sacrifice, and survival.",
    "Human: I need a romantic comedy\nAI: Lovely★Complex is hilarious and heartwarming, especially with its tall-girl/short-guy dynamic.",
    "Human: Recommend a horror anime\nAI: Another is a creepy supernatural horror with lots of suspense and mystery.",
    "Human: I want an inspiring anime\nAI: Hajime no Ippo is a boxing story about grit, growth, and never giving up.",
    "Human: Suggest an anime about musicians\nAI: Beck: Mongolian Chop Squad follows a group of teens chasing their dream of making it in music.",
    "Human: I want a classic must-watch\nAI: Neon Genesis Evangelion is iconic — deep mecha action mixed with psychology and philosophy.",
    "Human: Recommend something wholesome\nAI: Fruits Basket is heartwarming, romantic, and full of healing character growth."
    "Human: I want something wholesome like Fruits Basket\nAI: Try Clannad: After Story — it’s heartwarming, emotional, and shows the beauty and struggles of family life.",
    "Human: Recommend me a fun action anime\nAI: Soul Eater is stylish, action-packed, and full of quirky characters battling evil.",
    "Human: Any anime like Demon Slayer?\nAI: Jujutsu Kaisen is your best bet — it’s flashy, intense, and has a fantastic cast of sorcerers fighting curses.",
    "Human: I loved Erased, what’s next?\nAI: Try Orange — it’s a mix of time-travel, romance, and emotional high school drama.",
    "Human: Suggest a fantasy romance\nAI: Snow White with the Red Hair is a sweet romance in a medieval fantasy world.",
    "Human: I want a crazy battle royale anime\nAI: Darwin’s Game is a thrilling survival story full of strategic battles and unexpected twists.",
    "Human: Give me something weird but funny\nAI: Excel Saga is chaotic, random, and pure absurdist comedy.",
    "Human: Recommend me an emotional sports anime\nAI: Run with the Wind blends sports with deep character growth and bonds.",
    "Human: Any space-themed anime?\nAI: Space Dandy is colorful, hilarious, and an intergalactic adventure with style.",
    "Human: I want something dark like Elfen Lied\nAI: Try Higurashi: When They Cry — it’s psychological horror with gruesome twists and mysteries.",
    "Human: Suggest an uplifting anime\nAI: March Comes in Like a Lion mixes healing, emotional growth, and the struggles of a young shogi player.",
    "Human: I want an anime with badass swordsmen\nAI: Rurouni Kenshin is a classic samurai tale full of action and redemption.",
    "Human: Any romance comedies with a twist?\nAI: Lovely Complex stands out with its tall-girl/short-guy dynamic and hilarious banter.",
    "Human: Recommend a mecha anime besides Gundam\nAI: Aldnoah.Zero is intense with futuristic mech battles and political intrigue.",
    "Human: I want a touching short anime\nAI: Hotarubi no Mori e is a beautiful and bittersweet movie about love and spirits.",
    "Human: Give me a cooking anime\nAI: Food Wars! is full of delicious dishes, over-the-top reactions, and fierce culinary battles.",
    "Human: Recommend me a lighthearted fantasy\nAI: Konosuba is hilarious, parodying isekai tropes while still delivering fun adventures.",
    "Human: I liked The Promised Neverland\nAI: You might enjoy Made in Abyss, which mixes innocent beginnings with dark and shocking turns.",
    "Human: I want something about superheroes\nAI: One Punch Man is both a parody and love letter to hero anime, with insane fights and comedy.",
    "Human: Recommend me a tearjerker anime\nAI: Angel Beats! is emotional, funny, and heartbreaking, all set in a mysterious afterlife school.",
    "Human: I want a stylish crime anime\nAI: Banana Fish has gritty crime drama, emotional storytelling, and complex characters.",
    "Human: Any anime like Fairy Tail?\nAI: Black Clover shares the magic, teamwork, and shounen intensity with tons of battles.",
    "Human: Suggest a short comedy anime\nAI: The Devil is a Part-Timer! is hilarious — a demon lord ends up working at a fast-food joint.",
    "Human: I want an anime about androids or robots\nAI: Plastic Memories is emotional and bittersweet, focusing on androids nearing the end of their lifespans.",
    "Human: Recommend me a hype anime\nAI: Kill la Kill is non-stop hype with insane battles, flashy animation, and wild energy.",
    "Human: Any historical anime?\nAI: Vinland Saga is a powerful tale of Vikings, war, and the search for true meaning in life.",
    "Human: I want a heartwarming romance\nAI: Golden Time is a sweet and sometimes dramatic college romance with great character arcs.",
    "Human: Suggest a thriller mystery\nAI: Terror in Resonance is a suspenseful story about two mysterious terrorists and the truth behind them.",
    "Human: I want a unique sports anime\nAI: Yuri!!! on Ice brings figure skating to life with beautiful animation and a strong emotional core.",
    "Human: Recommend me an epic adventure anime\nAI: Hunter x Hunter has world-class battles, friendships, and arcs that keep raising the stakes.",
    "Human: I want something supernatural\nAI: Noragami is action-packed, funny, and blends spirits and gods into modern life.",
    "Human: Any anime with assassins?\nAI: Assassination Classroom mixes comedy, action, and deep lessons as a class trains to kill their alien teacher.",
    "Human: I want something with deep emotions\nAI: Grave of the Fireflies is heartbreaking, showing the struggles of siblings during wartime Japan.",
    "Human: Suggest an anime about gamers\nAI: No Game No Life is colorful, clever, and about siblings taking on a world governed by games.",
    "Human: I need a shounen classic\nAI: Rurouni Kenshin delivers powerful sword fights and themes of redemption in the Meiji era.",
    "Human: I want a fantasy with guilds or magic\nAI: Fairy Tail fits perfectly — it’s all about magical guild adventures and bonds of friendship.",
    "Human: Recommend me a cyberpunk anime\nAI: Psycho-Pass is a futuristic thriller where society is controlled by crime-predicting tech.",
    "Human: I want something wholesome and funny\nAI: Nichijou is absurd slice-of-life comedy with heartwarming moments hidden in the chaos.",
    "Human: Suggest an underrated gem\nAI: Ergo Proxy is a dark, atmospheric mix of sci-fi, philosophy, and mystery.",
    "Human: I want an anime about determination\nAI: Hajime no Ippo is all about grit, passion, and the climb to greatness through boxing.",
    "Human: Any anime like My Hero Academia?\nAI: Blue Exorcist combines superpowered battles with themes of growth and acceptance.",
    "Human: Recommend me a fantasy adventure\nAI: Akame ga Kill has assassins, revolution, and shocking twists in a brutal fantasy world.",
    "Human: I want a supernatural detective anime\nAI: Durarara!! blends urban legends, gang wars, and mysterious characters into one wild ride.",
    "Human: Suggest an anime with unique visuals\nAI: Paprika is a movie with stunning dreamlike animation and trippy storytelling.",
    "Human: I want something funny and heartwarming\nAI: Barakamon is a charming slice-of-life about an artist learning from a rural community.",
    "Human: Any anime about gods?\nAI: Kamisama Kiss is a romantic fantasy where a girl suddenly becomes a local shrine goddess.",
    "Human: I want a bizarre but brilliant anime\nAI: Paranoia Agent is a surreal psychological thriller with deep symbolism.",
    "Human: Suggest a music-focused anime\nAI: Given is a heartfelt story about music, grief, and love between band members.",
    "Human: Recommend me a fantasy movie\nAI: Spirited Away is a Studio Ghibli classic full of wonder, spirits, and breathtaking visuals.",
    "Human: I want a story about redemption\nAI: 91 Days is a revenge mafia anime where justice and morality blur in the pursuit of vengeance."
    # General recommendations
    "Human: What should I watch\nAI: Try My Hero Academia! It has similar themes of friendship, growth, and never giving up. The school setting adds a fresh twist to the classic shounen formula.",
    
    "Human: I need a new anime\nAI: Attack on Titan is perfect if you want intense action and a gripping storyline. The mysteries unfold brilliantly across seasons, with stunning animation and complex characters.",
    
    "Human: Give me something to binge\nAI: One Piece is the ultimate binge-watch with over 1000 episodes of adventure, humor, and heart. The world-building is incredible and each crew member has amazing development.",
    
    "Human: What's good to watch\nAI: Demon Slayer combines gorgeous animation with emotional storytelling. The fight scenes are breathtaking, and Tanjiro's journey to save his sister is genuinely moving.",
    
    "Human: Recommend an anime\nAI: Spirited Away is a masterpiece that works for any viewer. Studio Ghibli's animation is magical, and the story about growing up and finding inner strength is timeless.",
    
    # Prompting for interests
    "Human: What anime should I watch?\nAI: I'd love to help! What genres do you typically enjoy? Are you into action, romance, comedy, or something else? Also, do you prefer subtitled or dubbed anime?",
    
    "Human: I want to watch anime but don't know what\nAI: Great choice! To give you the best recommendation, could you tell me what kinds of shows or movies you usually like? Do you prefer action-packed adventures, slice-of-life stories, or maybe something with romance?",
    
    "Human: Help me pick an anime\nAI: Absolutely! What are you in the mood for? Something with epic battles, heartwarming friendships, mystery and suspense, or perhaps a romantic story? Any particular art style you prefer?",
    
    "Human: I'm new to anime\nAI: Welcome to anime! To suggest something perfect for you, what genres do you usually enjoy in movies or TV shows? Action, comedy, drama, fantasy? And would you prefer watching with subtitles or English dub?",
    
    "Human: Need anime suggestions\nAI: I'd be happy to suggest some! What type of story appeals to you most - adventure and fighting, everyday life and relationships, mystery and thriller, or maybe supernatural elements? Do you have a preference for episode length?",
    
    # Genre-specific with user responses
    "Human: I like action and adventure\nAI: Perfect! Fullmetal Alchemist: Brotherhood is a must-watch with incredible action sequences and deep philosophical themes. The alchemy-based magic system is unique, and the plot tackles war, sacrifice, and redemption beautifully.",
    
    "Human: I'm into romance anime\nAI: Your Name is absolutely stunning - a supernatural romance that will make you cry. The animation is breathtaking, and the story about two people connected across time and space is incredibly touching.",
    
    "Human: I want something funny\nAI: One Punch Man is hilarious while also having amazing action. Saitama's deadpan humor as an overpowered hero who defeats everything in one punch creates comedy gold, plus the animation is top-tier.",
    
    "Human: I like mystery shows\nAI: Death Note is a psychological masterpiece about a student who gains the power to kill with a notebook. The cat-and-mouse game between Light and L is intense, with brilliant mind games throughout.",
    
    "Human: I want something dark\nAI: Tokyo Ghoul explores the darker side of humanity through ghouls who eat humans. It's intense and violent but asks deep questions about what makes us human, with stunning fight choreography.",
    
    # Dub preferences
    "Human: I only watch dubbed anime\nAI: Cowboy Bebop has one of the best English dubs ever made. The space western follows bounty hunters with incredible jazz music, film noir atmosphere, and stellar voice acting that rivals the original Japanese.",
    
    "Human: Do you have good dubbed recommendations?\nAI: My Hero Academia's dub is fantastic with energetic voice acting that matches the superhero theme perfectly. The English cast brings real emotion to the characters' journey at hero academy.",
    
    "Human: I prefer English dub\nAI: Fullmetal Alchemist: Brotherhood's English dub is considered superior by many fans. The voice actors deliver powerful performances, especially during emotional scenes about the Elric brothers' quest.",
    
    "Human: Only dubbed please\nAI: Dragon Ball Z's English dub is iconic and helped define anime in the West. The over-the-top voice acting perfectly matches the epic battles and power-ups that made this series legendary.",
    
    "Human: What has great English voice acting?\nAI: Black Lagoon's dub is gritty and mature, perfect for its dark mercenary story. The English voices capture the international cast of characters and add authenticity to the crime thriller atmosphere.",
    
    # Specific requests
    "Human: I want something like Naruto\nAI: Black Clover has that same never-give-up spirit with Asta's journey to become the Wizard King despite having no magic. The friendship bonds, intense battles, and character growth mirror what made Naruto special.",
    
    "Human: Something similar to Studio Ghibli films\nAI: Violet Evergarden has that same emotional depth and gorgeous animation. It follows a former soldier learning to understand emotions while working as a letter writer, with breathtaking visuals and touching stories.",
    
    "Human: I loved One Piece, what's next?\nAI: Fairy Tail captures that same adventurous guild spirit with wizards going on magical quests. The friendship themes, epic battles, and loyal nakama bonds will remind you why you loved Luffy's crew.",
    
    "Human: Like Death Note but different\nAI: Code Geass offers similar strategic mind games but in a mecha setting. Lelouch's quest for revenge using his Geass power creates intense psychological warfare with stunning plot twists.",
    
    "Human: I want something like Attack on Titan\nAI: Kabaneri of the Iron Fortress has similar post-apocalyptic survival themes with steampunk zombies. The intense action and humanity's struggle against monsters captures that same desperate atmosphere.",
    
    # Short series recommendations
    "Human: I want something short\nAI: Erased is a perfect 12-episode thriller about preventing murders by traveling back in time. The mystery builds perfectly with emotional character development and a satisfying conclusion.",
    
    "Human: Something I can finish quickly\nAI: Mob Psycho 100 seasons are short but incredibly impactful. The story of a psychic middle schooler learning to control his powers has amazing animation and themes about growing up and self-acceptance.",
    
    "Human: Quick anime recommendation\nAI: A Silent Voice is a beautiful movie about redemption and forgiveness. It deals with bullying and disability with incredible sensitivity, plus the animation and soundtrack are absolutely stunning.",
    
    "Human: I don't have much time\nAI: Your Name can be watched in 2 hours and is absolutely worth it. This supernatural romance about body-swapping will leave you emotional, and the animation quality is some of the best ever created.",
    
    "Human: Something under 25 episodes\nAI: Steins;Gate is 24 episodes of mind-bending time travel perfection. The slow build pays off with incredible plot twists, emotional depth, and one of anime's best protagonists in Okabe.",
    
    # Mood-based recommendations
    "Human: I want to cry\nAI: Grave of the Fireflies will absolutely destroy you emotionally. This Studio Ghibli war film about siblings surviving WWII is heartbreaking but important, showing the human cost of conflict.",
    
    "Human: Something uplifting\nAI: K-On! is pure happiness about girls in a light music club. The slice-of-life format focuses on friendship and following your passions, with adorable characters and catchy music.",
    
    "Human: I want to be scared\nAI: Another is genuinely terrifying with supernatural deaths plaguing a cursed classroom. The mystery keeps you guessing while delivering legitimate scares and a creepy atmosphere throughout.",
    
    "Human: Something inspiring\nAI: Haikyuu!! will make you want to play volleyball even if you hate sports. The determination, teamwork, and pure passion of these high school players is incredibly motivating and uplifting.",
    
    "Human: I need something relaxing\nAI: Mushishi is incredibly peaceful, following a wanderer who helps people with supernatural problems. Each episode is like meditation with beautiful nature scenes and philosophical storytelling.",
    
    # Animation quality focused
    "Human: I want beautiful animation\nAI: Makoto Shinkai's films like Weathering With You have photorealistic backgrounds that look like paintings. Every frame is wallpaper-worthy, and the lighting effects are absolutely magical.",
    
    "Human: Something with great art\nAI: Princess Mononoke showcases Studio Ghibli's incredible hand-drawn animation. The forest spirits and epic battles are visually stunning, with environmental themes that feel especially relevant today.",
    
    "Human: Best animated fight scenes\nAI: Jujutsu Kaisen has some of the most fluid and creative fight animation ever. Studio MAPPA's work makes every curse battle feel dynamic and impactful with incredible choreography.",
    
    "Human: What has amazing visuals?\nAI: Ghost in the Shell: SAC_2045 might divide fans on style, but the 3D animation creates incredibly detailed cyberpunk cityscapes. The action sequences showcase what modern anime technology can achieve.",
    
    "Human: I love good animation quality\nAI: Violet Evergarden is visually breathtaking with incredibly detailed character animation and gorgeous backgrounds. Kyoto Animation's attention to detail makes every scene feel like a work of art.",
    
    # Music focused
    "Human: I want great music\nAI: Cowboy Bebop's jazz soundtrack by Yoko Kanno is legendary and perfectly complements the space western atmosphere. Each episode feels like a different musical genre while maintaining cohesion.",
    
    "Human: Something with good soundtrack\nAI: Attack on Titan's orchestral score creates incredible tension and emotion. Hiroyuki Sawano's compositions perfectly match the epic scale and desperate humanity of the story.",
    
    "Human: Music is important to me\nAI: Your Lie in April centers around classical music with performances that will give you chills. The way music expresses emotion and connects characters is absolutely beautiful.",
    
    "Human: I love anime with great music\nAI: Samurai Champloo blends hip-hop with Edo period Japan in a unique way. The soundtrack by Nujabes is incredible and creates a completely distinctive atmosphere.",
    
    "Human: What has the best opening songs?\nAI: Jojo's Bizarre Adventure has iconic openings that perfectly capture each arc's energy. From Sono Chi no Sadame to Traitor's Requiem, each OP is a masterpiece that fans obsess over.",
    
    # Character-driven recommendations
    "Human: I want great characters\nAI: Monster has some of anime's most complex characters, especially the terrifying Johan Liebert. The psychological depth and moral ambiguity make every character feel real and compelling.",
    
    "Human: Something with character development\nAI: Hunter x Hunter shows incredible growth in Gon and Killua's friendship. Each arc develops them differently, with the Chimera Ant arc providing some of anime's most profound character moments.",
    
    "Human: I love strong protagonists\nAI: Senku from Dr. Stone combines intelligence with determination to rebuild civilization using science. His analytical approach and genuine care for humanity makes him incredibly compelling to follow.",
    
    "Human: What has interesting villains?\nAI: Psycho-Pass features Makishima, a philosophical villain who challenges the entire social system. His intellectual debates with protagonists create moral complexity rarely seen in anime.",
    
    "Human: I want complex characters\nAI: Evangelion's characters are deeply flawed and psychologically realistic. Shinji's depression and anxiety are handled with surprising depth, making this mecha series incredibly human.",
    
    # Setting-based recommendations
    "Human: I want fantasy anime\nAI: Made in Abyss creates one of anime's most fascinating and dangerous fantasy worlds. The abyss itself becomes a character with beautiful but terrifying creatures and mysterious artifacts.",
    
    "Human: Something futuristic\nAI: Ghost in the Shell: Stand Alone Complex explores cyberpunk themes with incredible depth. The questions about identity, consciousness, and technology feel more relevant than ever.",
    
    "Human: I like historical settings\nAI: Vinland Saga depicts Viking-era violence with incredible historical detail. Thorfinn's journey from revenge to pacifism is beautifully handled with authentic medieval atmosphere.",
    
    "Human: Modern day setting\nAI: Parasyte explores body horror in contemporary Japan with philosophical depth. The symbiotic relationship between Shinichi and Migi asks deep questions about humanity and survival.",
    
    "Human: I want something in space\nAI: Planetes is hard science fiction about space debris collectors. It's surprisingly grounded and thoughtful, dealing with real space travel challenges and international politics.",
    
    # Age rating considerations  
    "Human: Something appropriate for kids\nAI: My Neighbor Totoro is perfect family viewing with magical forest spirits and childhood wonder. Studio Ghibli's gentle storytelling and beautiful animation create lasting memories.",
    
    "Human: I want mature content\nAI: Berserk deals with very dark themes including trauma, war, and corruption. The medieval fantasy setting doesn't soften the brutal examination of human nature and survival.",
    
    "Human: Teen-friendly recommendations\nAI: Little Witch Academia is wholesome and fun about a girl pursuing her dream to become a witch. The Harry Potter-esque school setting has great messages about perseverance and friendship.",
    
    "Human: Nothing too violent\nAI: Barakamon is a gentle slice-of-life about a calligrapher who moves to a rural island. The interactions with local children are heartwarming, and the art themes are beautifully handled.",
    
    "Human: I'm okay with violence\nAI: Vinland Saga doesn't shy away from brutal Viking warfare but uses violence purposefully to explore themes of revenge, war, and ultimately finding peace.",
    
    # Length preferences
    "Human: I want a long series\nAI: Gintama has over 300 episodes of comedy gold mixed with serious arcs. The humor is incredible, and when it gets serious, the emotional payoff from knowing these characters is amazing.",
    
    "Human: Something with many seasons\nAI: JoJo's Bizarre Adventure spans generations with unique protagonists in each part. The art style evolves dramatically, and each story arc feels completely fresh while maintaining core themes.",
    
    "Human: Just a movie recommendation\nAI: Akira is a cyberpunk masterpiece that influenced animation worldwide. The motorcycle chase scenes and psychic powers are still incredible decades later, with unparalleled hand-drawn animation.",
    
    "Human: I prefer shorter series\nAI: Ping Pong The Animation is only 11 episodes but tells a complete story about competition, friendship, and finding your place. The unique art style perfectly matches the energetic story.",
    
    "Human: Movies or short series only\nAI: The Garden of Words is a beautiful 46-minute film about an unlikely friendship. Makoto Shinkai's rain animation is gorgeous, and the story about finding connection is deeply moving.",
    
    # Specific genres expanded
    "Human: I love horror anime\nAI: Higurashi: When They Cry starts cute but becomes genuinely terrifying as mysteries unfold. The psychological horror and time loop elements create an incredibly unsettling atmosphere.",
    
    "Human: What about comedy?\nAI: Konosuba parodies RPG and isekai tropes with hilarious results. Kazuma and his dysfunctional party of misfits create comedy through their complete incompetence at heroics.",
    
    "Human: I like slice of life\nAI: March Comes in Like a Lion beautifully depicts depression and healing through shogi. The realistic portrayal of mental health and found family themes make it incredibly touching.",
    
    "Human: Sports anime recommendations\nAI: Kuroko no Basketball has incredible supernatural basketball action with unique abilities for each player. The teamwork and rivalry dynamics create intense and emotional games.",
    
    "Human: What about mecha anime?\nAI: Gurren Lagann is pure over-the-top mecha action with incredible spirit. Simon's journey from coward to galactic hero is inspiring, with drills that pierce the heavens literally and metaphorically.",
    
    # Art style preferences
    "Human: I like unique art styles\nAI: Mob Psycho 100 has incredibly distinctive animation that matches its psychic themes perfectly. Studio Bones' experimental approach creates visuals unlike anything else in anime.",
    
    "Human: Something with realistic art\nAI: Monster uses realistic character designs that make the psychological thriller elements even more unsettling. The European setting feels authentic with detailed backgrounds.",
    
    "Human: I prefer cute art styles\nAI: Nichijou has adorable character designs that make the absurd comedy even funnier. The contrast between cute visuals and explosive reactions creates perfect comedic timing.",
    
    "Human: Dark art style preferred\nAI: Hell's Paradise has a distinctly dark and gritty art style that matches its violent samurai story. The contrast between beautiful nature and brutal death creates striking visuals.",
    
    "Human: I like colorful animation\nAI: No Game No Life is incredibly vibrant with a unique color palette that makes every scene pop. The chess-like strategic games are visually stunning with rainbow effects.",
    
    # Emotional responses
    "Human: Make me laugh\nAI: Grand Blue is absolutely hilarious with college diving club antics that focus more on drinking than diving. The facial expressions and misunderstandings create non-stop comedy.",
    
    "Human: I want to feel inspired\nAI: A Place Further Than the Universe follows girls pursuing their dream of Antarctic expedition. Their determination to overcome obstacles and chase impossible dreams is incredibly motivating.",
    
    "Human: Something thought-provoking\nAI: Serial Experiments Lain explores identity and reality in the digital age with prophetic themes about internet culture. Each episode adds layers to complex philosophical questions.",
    
    "Human: I want epic battles\nAI: Fate/Zero has incredible battle royale action between legendary heroes summoned as servants. The animation quality and strategic elements make each fight unique and spectacular.",
    
    "Human: Something heartwarming\nAI: Usagi Drop is incredibly sweet about a man raising his grandfather's illegitimate daughter. The realistic portrayal of single parenting and child development is touching and authentic.",
    
    # Subgenre specifics
    "Human: I like magical girl anime\nAI: Puella Magi Madoka Magica deconstructs the magical girl genre with dark psychological themes. The contrast between cute art and serious consequences creates a unique and impactful story.",
    
    "Human: What about isekai?\nAI: Re:Zero is a dark take on being transported to another world where death resets time. Subaru's psychological trauma from repeated deaths creates surprisingly deep character development.",
    
    "Human: I want cyberpunk\nAI: Akudama Drive is stylish cyberpunk with incredible neon aesthetics and over-the-top action. The criminals' heist story unfolds with stunning animation and creative world-building.",
    
    "Human: Post-apocalyptic recommendations\nAI: Trigun follows Vash the Stampede in a desert wasteland with incredible gunfights and surprisingly deep themes about pacifism and humanity's capacity for both good and evil.",
    
    "Human: I like vampire anime\nAI: Hellsing Ultimate features Alucard as an incredibly overpowered vampire fighting other supernatural threats. The gothic atmosphere and extreme violence create a unique vampire experience.",
    
    # Tone preferences
    "Human: Something light-hearted\nAI: Azumanga Daioh is pure wholesome comedy about high school girls and their eccentric teacher. The sketch-based format creates consistently funny moments without drama or conflict.",
    
    "Human: I want something serious\nAI: Grave of the Fireflies deals with war's impact on civilians through siblings struggling to survive. Studio Ghibli's realistic approach makes this incredibly powerful and important.",
    
    "Human: Mix of comedy and drama\nAI: Gintama perfectly balances ridiculous comedy with serious emotional arcs. The tonal shifts feel natural because of strong character development throughout hundreds of episodes.",
    
    "Human: Something bittersweet\nAI: 5 Centimeters Per Second explores how people grow apart over time despite deep connections. The beautiful animation and realistic relationship dynamics create profound melancholy.",
    
    "Human: I want pure fun\nAI: Kill la Kill is pure over-the-top insanity with fashion-based superpowers and incredible energy. Studio Trigger's wild animation style matches the completely absurd premise perfectly.",
    
    # More specific requests
    "Human: I want strong female characters\nAI: Ghost in the Shell features Major Kusanagi as one of anime's strongest female protagonists. Her philosophical struggles with identity in a cybernetic body are handled with incredible depth.",
    
    "Human: Something with good world-building\nAI: Land of the Lustrous creates a fascinating world where gem-based beings fight moon dwellers. The unique biology and mythology create rich lore with beautiful 3D animation.",
    
    "Human: I like ensemble casts\nAI: Durarara!! weaves together multiple storylines in Ikebukuro with a large cast of interconnected characters. Each person's story contributes to the larger urban fantasy narrative.",
    
    "Human: What about time travel?\nAI: Steins;Gate uses time travel to explore cause and effect with incredible detail. The butterfly effect scenarios create genuine tension as small changes have massive consequences.",
    
    "Human: I want cooking anime\nAI: Food Wars! combines cooking with shounen battle anime tropes for incredible results. The food reactions are hilarious, and the culinary techniques are surprisingly educational.",
    
    # Platform availability
    "Human: What's good on Netflix?\nAI: Castlevania has incredible animation and mature storytelling that respects the game source material. The gothic atmosphere and character development across seasons is outstanding.",
    
    "Human: I have Crunchyroll\nAI: Jujutsu Kaisen is perfect with incredible fight animation and a great magic system based on cursed energy. The character designs and supernatural battles are absolutely stunning.",
    
    "Human: What's on Funimation?\nAI: My Hero Academia's entire series is available with both excellent sub and dub options. The superhero academy setting provides consistent character growth and amazing action sequences.",
    
    "Human: I use Hulu\nAI: One Piece is available with hundreds of episodes of pirate adventures. The world-building and character development across decades makes this one of anime's greatest achievements.",
    
    "Human: What can I watch for free?\nAI: Many classic anime are available on YouTube and Tubi. Neon Genesis Evangelion is often free and remains one of anime's most influential and psychologically complex series.",
    
    # Rewatchability
    "Human: Something I can rewatch\nAI: Cowboy Bebop reveals new details on every viewing with its film noir storytelling and jazz soundtrack. Each character's backstory adds layers that reward multiple viewings.",
    
    "Human: I like shows with hidden details\nAI: Serial Experiments Lain is dense with symbolism and foreshadowing that makes sense only after knowing the ending. Each episode contains clues that create entirely new interpretations.",
    
    "Human: What has good replay value?\nAI: Hunter x Hunter's power system and strategic battles reveal new tactical elements on rewatching. The character motivations and foreshadowing become clearer with multiple viewings.",
    
    "Human: I want layers to discover\nAI: Evangelion is famous for requiring multiple viewings to understand its psychological and religious symbolism. Each watch reveals new interpretations of character motivations and themes.",
    
    "Human: Something with Easter eggs\nAI: FLCL is packed with visual references and metaphors that reward careful viewing. The coming-of-age story uses surreal imagery that becomes clearer with analysis and rewatching.",
    
    # Cultural aspects
    "Human: I want to learn about Japan\nAI: Showa Genroku Rakugo Shinju explores traditional Japanese storytelling art with incredible cultural detail. The historical setting and rakugo performances provide authentic cultural immersion.",
    
    "Human: Something with Japanese culture\nAI: Spirited Away is filled with Japanese folklore and spiritual beliefs woven into Chihiro's journey. The bathhouse setting showcases traditional mythology in accessible storytelling.",
    
    "Human: I like traditional themes\nAI: Mushishi explores Japanese spiritual beliefs about nature and balance through beautifully contemplative episodes. Each story draws from traditional folklore with stunning natural imagery.",
    
    "Human: What shows Japanese history?\nAI: Rurouni Kenshin depicts the Meiji Restoration period with samurai transitioning to modern Japan. The historical context adds depth to Kenshin's personal journey from killer to protector.",
    
    "Human: I want authentic Japanese stories\nAI: Only Yesterday captures the realistic experience of Japanese rural life and childhood memories. Studio Ghibli's grounded approach shows authentic cultural details and generational changes.",
    
    # Animation studios
    "Human: I love Studio Ghibli\nAI: Princess Mononoke showcases everything great about Ghibli with environmental themes and stunning hand-drawn animation. The epic scope and spiritual elements create their most ambitious work.",
    
    "Human: What about Studio Trigger?\nAI: Promare is pure Trigger energy with incredible fire-based animation and over-the-top action. The visual style is uniquely colorful and dynamic, perfect for their high-energy storytelling.",
    
    "Human: I like Madhouse productions\nAI: Perfect Blue is Madhouse's psychological masterpiece that influenced films like Black Swan. The blurred reality between idol persona and true self creates genuinely disturbing thriller elements.",
    
    "Human: What has MAPPA made?\nAI: Attack on Titan's final seasons showcase MAPPA's incredible action animation with fluid 3D maneuver gear sequences. Their handling of emotional character moments matches the epic battle scenes.",
    
    "Human: I want Kyoto Animation\nAI: A Silent Voice demonstrates KyoAni's incredible attention to emotional detail through realistic character animation. Every gesture and expression contributes to the powerful story about bullying and redemption.",
    
    # Finale
    "Human: I want something perfect\nAI: Fullmetal Alchemist: Brotherhood is often considered anime's masterpiece with perfect pacing, character development, and thematic depth. Every element from action to philosophy is executed flawlessly.",
    
    "Human: What's the best anime ever?\nAI: That's subjective, but Spirited Away won the Academy Award for good reason. It combines universal themes with uniquely Japanese storytelling and animation that transcends cultural boundaries.",
    
    "Human: I want a masterpiece\nAI: Princess Mononoke tackles environmental destruction and human nature with incredible maturity. The hand-drawn animation and complex moral questions make this an enduring work of art.",
    
    "Human: Something legendary\nAI: Akira revolutionized animation worldwide with unprecedented detail and cyberpunk themes that remain relevant. The motorcycle sequences and psychic destruction scenes are still unmatched decades later.",
    
    "Human: What changed anime forever?\nAI: Neon Genesis Evangelion redefined what anime could be with psychological depth and religious symbolism. Its influence on both animation and popular culture continues to this day.",
    
    # More specific genre combinations
    "Human: I want action with romance\nAI: Eureka Seven combines mecha action with a beautiful coming-of-age love story. Renton and Eureka's relationship develops naturally alongside incredible aerial battles and stunning animation.",
    
    "Human: Comedy with good plot\nAI: The Devil is a Part-Timer! has great comedy from Satan working at McDonald's while building an actually engaging plot about redemption and responsibility in the modern world.",
    
    "Human: Horror with mystery\nAI: Shiki combines vampire horror with small-town mystery as residents slowly disappear. The gradual revelation of what's happening creates incredible tension and moral complexity.",
    
    "Human: Fantasy with politics\nAI: Legend of the Galactic Heroes is space opera with incredible political intrigue between democratic and imperial forces. The strategic battles are matched by complex character relationships.",
    
    "Human: Sci-fi with philosophy\nAI: Ghost in the Shell: Stand Alone Complex explores consciousness and identity in a cyberpunk future. Each episode asks deep questions about what makes us human in a digital age.",
    
    # International appeal
    "Human: Something universal\nAI: Wolf Children transcends cultural boundaries with its story of a mother raising half-wolf children. The themes of single parenting and growing up resonate with audiences worldwide.",
    
    "Human: I want global themes\nAI: Grave of the Fireflies shows war's impact on innocent civilians in a way that applies to conflicts everywhere. The sibling relationship and survival story is universally heartbreaking.",
    
    "Human: Something anyone can enjoy\nAI: Castle in the Sky has adventure, romance, and environmental themes that work for all ages and cultures. The flying sequences and Laputa's mystery create timeless entertainment.",
    
    "Human: Cross-cultural appeal\nAI: Your Name deals with connection across distance and time in ways that transcend specific cultural contexts. The supernatural romance and stunning visuals speak to universal human experiences.",
    
    "Human: I want broad appeal\nAI: One Piece's themes of friendship, dreams, and adventure resonate globally. Despite uniquely Japanese humor, the emotional core of pursuing your dreams with loyal friends is universal.",
    
    # Advanced recommendations
    "Human: I've seen everything mainstream\nAI: Monster is an overlooked psychological masterpiece about a surgeon hunting a sociopathic killer. The European setting and realistic approach create something completely unique in anime.",
    
    "Human: I want something obscure\nAI: Texhnolyze is incredibly dark cyberpunk that explores transhumanism and societal decay. It's challenging viewing but rewards patient viewers with profound philosophical themes.",
    
    "Human: Hidden gems please\nAI: Planetes is hard science fiction about space debris collectors that's surprisingly grounded and thoughtful. The realistic portrayal of space travel and international politics is refreshing.",
    
    "Human: What's underrated?\nAI: Ping Pong The Animation has unique art that turns people away, but the story about competition, friendship, and finding your place is absolutely brilliant with incredible character development.",
    
    "Human: Something most people miss\nAI: Kaiba explores memory and identity through unique art and storytelling. The surreal presentation masks incredibly deep themes about what makes us who we are.",
    
    # Seasonal/mood based
    "Human: Something for winter\nAI: 5 Centimeters Per Second captures the melancholy of winter with beautiful snow scenes and themes about growing apart. The cold atmosphere matches the emotional distance perfectly.",
    
    "Human: I want summer vibes\nAI: Free! is all about summer swimming with gorgeous water animation and themes about friendship and competition. The pool scenes and summer festival atmosphere are incredibly refreshing.",
    
    "Human: Something cozy\nAI: Non Non Biyori is incredibly cozy with rural countryside setting and gentle humor. The slow pace and beautiful nature scenes create perfect relaxation viewing.",
    
    "Human: I need comfort food anime\nAI: K-On! is pure comfort with cute girls doing cute things in their light music club. The friendship dynamics and catchy songs create a warm, happy atmosphere.",
    
    "Human: Something atmospheric\nAI: Mushishi has incredible atmosphere with each episode exploring Japanese folklore in beautiful natural settings. The contemplative pacing and spiritual themes create meditative viewing."

    # General recommendations
    "Human: What should I watch\nAI: Try My Hero Academia! It has similar themes of friendship, growth, and never giving up. The school setting adds a fresh twist to the classic shounen formula.",
    
    "Human: I need a new anime\nAI: Attack on Titan is perfect if you want intense action and a gripping storyline. The mysteries unfold brilliantly across seasons, with stunning animation and complex characters.",
    
    "Human: Give me something to binge\nAI: One Piece is the ultimate binge-watch with over 1000 episodes of adventure, humor, and heart. The world-building is incredible and each crew member has amazing development.",
    
    "Human: What's good to watch\nAI: Demon Slayer combines gorgeous animation with emotional storytelling. The fight scenes are breathtaking, and Tanjiro's journey to save his sister is genuinely moving.",
    
    "Human: Recommend an anime\nAI: Spirited Away is a masterpiece that works for any viewer. Studio Ghibli's animation is magical, and the story about growing up and finding inner strength is timeless.",
    
    # Prompting for interests
    "Human: What anime should I watch?\nAI: I'd love to help! What genres do you typically enjoy? Are you into action, romance, comedy, or something else? Also, do you prefer subtitled or dubbed anime?",
    
    "Human: I want to watch anime but don't know what\nAI: Great choice! To give you the best recommendation, could you tell me what kinds of shows or movies you usually like? Do you prefer action-packed adventures, slice-of-life stories, or maybe something with romance?",
    
    "Human: Help me pick an anime\nAI: Absolutely! What are you in the mood for? Something with epic battles, heartwarming friendships, mystery and suspense, or perhaps a romantic story? Any particular art style you prefer?",
    
    "Human: I'm new to anime\nAI: Welcome to anime! To suggest something perfect for you, what genres do you usually enjoy in movies or TV shows? Action, comedy, drama, fantasy? And would you prefer watching with subtitles or English dub?",
    
    "Human: Need anime suggestions\nAI: I'd be happy to suggest some! What type of story appeals to you most - adventure and fighting, everyday life and relationships, mystery and thriller, or maybe supernatural elements? Do you have a preference for episode length?",
    
    # Genre-specific with user responses
    "Human: I like action and adventure\nAI: Perfect! Fullmetal Alchemist: Brotherhood is a must-watch with incredible action sequences and deep philosophical themes. The alchemy-based magic system is unique, and the plot tackles war, sacrifice, and redemption beautifully.",
    
    "Human: I'm into romance anime\nAI: Your Name is absolutely stunning - a supernatural romance that will make you cry. The animation is breathtaking, and the story about two people connected across time and space is incredibly touching.",
    
    "Human: I want something funny\nAI: One Punch Man is hilarious while also having amazing action. Saitama's deadpan humor as an overpowered hero who defeats everything in one punch creates comedy gold, plus the animation is top-tier.",
    
    "Human: I like mystery shows\nAI: Death Note is a psychological masterpiece about a student who gains the power to kill with a notebook. The cat-and-mouse game between Light and L is intense, with brilliant mind games throughout.",
    
    "Human: I want something dark\nAI: Tokyo Ghoul explores the darker side of humanity through ghouls who eat humans. It's intense and violent but asks deep questions about what makes us human, with stunning fight choreography.",
    
    # Dub preferences
    "Human: I only watch dubbed anime\nAI: Cowboy Bebop has one of the best English dubs ever made. The space western follows bounty hunters with incredible jazz music, film noir atmosphere, and stellar voice acting that rivals the original Japanese.",
    
    "Human: Do you have good dubbed recommendations?\nAI: My Hero Academia's dub is fantastic with energetic voice acting that matches the superhero theme perfectly. The English cast brings real emotion to the characters' journey at hero academy.",
    
    "Human: I prefer English dub\nAI: Fullmetal Alchemist: Brotherhood's English dub is considered superior by many fans. The voice actors deliver powerful performances, especially during emotional scenes about the Elric brothers' quest.",
    
    "Human: Only dubbed please\nAI: Dragon Ball Z's English dub is iconic and helped define anime in the West. The over-the-top voice acting perfectly matches the epic battles and power-ups that made this series legendary.",
    
    "Human: What has great English voice acting?\nAI: Black Lagoon's dub is gritty and mature, perfect for its dark mercenary story. The English voices capture the international cast of characters and add authenticity to the crime thriller atmosphere.",
    
    # Specific requests
    "Human: I want something like Naruto\nAI: Black Clover has that same never-give-up spirit with Asta's journey to become the Wizard King despite having no magic. The friendship bonds, intense battles, and character growth mirror what made Naruto special.",
    
    "Human: Something similar to Studio Ghibli films\nAI: Violet Evergarden has that same emotional depth and gorgeous animation. It follows a former soldier learning to understand emotions while working as a letter writer, with breathtaking visuals and touching stories.",
    
    "Human: I loved One Piece, what's next?\nAI: Fairy Tail captures that same adventurous guild spirit with wizards going on magical quests. The friendship themes, epic battles, and loyal nakama bonds will remind you why you loved Luffy's crew.",
    
    "Human: Like Death Note but different\nAI: Code Geass offers similar strategic mind games but in a mecha setting. Lelouch's quest for revenge using his Geass power creates intense psychological warfare with stunning plot twists.",
    
    "Human: I want something like Attack on Titan\nAI: Kabaneri of the Iron Fortress has similar post-apocalyptic survival themes with steampunk zombies. The intense action and humanity's struggle against monsters captures that same desperate atmosphere.",
    
    # Short series recommendations
    "Human: I want something short\nAI: Erased is a perfect 12-episode thriller about preventing murders by traveling back in time. The mystery builds perfectly with emotional character development and a satisfying conclusion.",
    
    "Human: Something I can finish quickly\nAI: Mob Psycho 100 seasons are short but incredibly impactful. The story of a psychic middle schooler learning to control his powers has amazing animation and themes about growing up and self-acceptance.",
    
    "Human: Quick anime recommendation\nAI: A Silent Voice is a beautiful movie about redemption and forgiveness. It deals with bullying and disability with incredible sensitivity, plus the animation and soundtrack are absolutely stunning.",
    
    "Human: I don't have much time\nAI: Your Name can be watched in 2 hours and is absolutely worth it. This supernatural romance about body-swapping will leave you emotional, and the animation quality is some of the best ever created.",
    
    "Human: Something under 25 episodes\nAI: Steins;Gate is 24 episodes of mind-bending time travel perfection. The slow build pays off with incredible plot twists, emotional depth, and one of anime's best protagonists in Okabe.",
    
    # Mood-based recommendations
    "Human: I want to cry\nAI: Grave of the Fireflies will absolutely destroy you emotionally. This Studio Ghibli war film about siblings surviving WWII is heartbreaking but important, showing the human cost of conflict.",
    
    "Human: Something uplifting\nAI: K-On! is pure happiness about girls in a light music club. The slice-of-life format focuses on friendship and following your passions, with adorable characters and catchy music.",
    
    "Human: I want to be scared\nAI: Another is genuinely terrifying with supernatural deaths plaguing a cursed classroom. The mystery keeps you guessing while delivering legitimate scares and a creepy atmosphere throughout.",
    
    "Human: Something inspiring\nAI: Haikyuu!! will make you want to play volleyball even if you hate sports. The determination, teamwork, and pure passion of these high school players is incredibly motivating and uplifting.",
    
    "Human: I need something relaxing\nAI: Mushishi is incredibly peaceful, following a wanderer who helps people with supernatural problems. Each episode is like meditation with beautiful nature scenes and philosophical storytelling.",
    
    # Animation quality focused
    "Human: I want beautiful animation\nAI: Makoto Shinkai's films like Weathering With You have photorealistic backgrounds that look like paintings. Every frame is wallpaper-worthy, and the lighting effects are absolutely magical.",
    
    "Human: Something with great art\nAI: Princess Mononoke showcases Studio Ghibli's incredible hand-drawn animation. The forest spirits and epic battles are visually stunning, with environmental themes that feel especially relevant today.",
    
    "Human: Best animated fight scenes\nAI: Jujutsu Kaisen has some of the most fluid and creative fight animation ever. Studio MAPPA's work makes every curse battle feel dynamic and impactful with incredible choreography.",
    
    "Human: What has amazing visuals?\nAI: Ghost in the Shell: SAC_2045 might divide fans on style, but the 3D animation creates incredibly detailed cyberpunk cityscapes. The action sequences showcase what modern anime technology can achieve.",
    
    "Human: I love good animation quality\nAI: Violet Evergarden is visually breathtaking with incredibly detailed character animation and gorgeous backgrounds. Kyoto Animation's attention to detail makes every scene feel like a work of art.",
    
    # Music focused
    "Human: I want great music\nAI: Cowboy Bebop's jazz soundtrack by Yoko Kanno is legendary and perfectly complements the space western atmosphere. Each episode feels like a different musical genre while maintaining cohesion.",
    
    "Human: Something with good soundtrack\nAI: Attack on Titan's orchestral score creates incredible tension and emotion. Hiroyuki Sawano's compositions perfectly match the epic scale and desperate humanity of the story.",
    
    "Human: Music is important to me\nAI: Your Lie in April centers around classical music with performances that will give you chills. The way music expresses emotion and connects characters is absolutely beautiful.",
    
    "Human: I love anime with great music\nAI: Samurai Champloo blends hip-hop with Edo period Japan in a unique way. The soundtrack by Nujabes is incredible and creates a completely distinctive atmosphere.",
    
    "Human: What has the best opening songs?\nAI: Jojo's Bizarre Adventure has iconic openings that perfectly capture each arc's energy. From Sono Chi no Sadame to Traitor's Requiem, each OP is a masterpiece that fans obsess over.",
    
    # Character-driven recommendations
    "Human: I want great characters\nAI: Monster has some of anime's most complex characters, especially the terrifying Johan Liebert. The psychological depth and moral ambiguity make every character feel real and compelling.",
    
    "Human: Something with character development\nAI: Hunter x Hunter shows incredible growth in Gon and Killua's friendship. Each arc develops them differently, with the Chimera Ant arc providing some of anime's most profound character moments.",
    
    "Human: I love strong protagonists\nAI: Senku from Dr. Stone combines intelligence with determination to rebuild civilization using science. His analytical approach and genuine care for humanity makes him incredibly compelling to follow.",
    
    "Human: What has interesting villains?\nAI: Psycho-Pass features Makishima, a philosophical villain who challenges the entire social system. His intellectual debates with protagonists create moral complexity rarely seen in anime.",
    
    "Human: I want complex characters\nAI: Evangelion's characters are deeply flawed and psychologically realistic. Shinji's depression and anxiety are handled with surprising depth, making this mecha series incredibly human.",
    
    # Setting-based recommendations
    "Human: I want fantasy anime\nAI: Made in Abyss creates one of anime's most fascinating and dangerous fantasy worlds. The abyss itself becomes a character with beautiful but terrifying creatures and mysterious artifacts.",
    
    "Human: Something futuristic\nAI: Ghost in the Shell: Stand Alone Complex explores cyberpunk themes with incredible depth. The questions about identity, consciousness, and technology feel more relevant than ever.",
    
    "Human: I like historical settings\nAI: Vinland Saga depicts Viking-era violence with incredible historical detail. Thorfinn's journey from revenge to pacifism is beautifully handled with authentic medieval atmosphere.",
    
    "Human: Modern day setting\nAI: Parasyte explores body horror in contemporary Japan with philosophical depth. The symbiotic relationship between Shinichi and Migi asks deep questions about humanity and survival.",
    
    "Human: I want something in space\nAI: Planetes is hard science fiction about space debris collectors. It's surprisingly grounded and thoughtful, dealing with real space travel challenges and international politics.",
    
    # Age rating considerations  
    "Human: Something appropriate for kids\nAI: My Neighbor Totoro is perfect family viewing with magical forest spirits and childhood wonder. Studio Ghibli's gentle storytelling and beautiful animation create lasting memories.",
    
    "Human: I want mature content\nAI: Berserk deals with very dark themes including trauma, war, and corruption. The medieval fantasy setting doesn't soften the brutal examination of human nature and survival.",
    
    "Human: Teen-friendly recommendations\nAI: Little Witch Academia is wholesome and fun about a girl pursuing her dream to become a witch. The Harry Potter-esque school setting has great messages about perseverance and friendship.",
    
    "Human: Nothing too violent\nAI: Barakamon is a gentle slice-of-life about a calligrapher who moves to a rural island. The interactions with local children are heartwarming, and the art themes are beautifully handled.",
    
    "Human: I'm okay with violence\nAI: Vinland Saga doesn't shy away from brutal Viking warfare but uses violence purposefully to explore themes of revenge, war, and ultimately finding peace.",
    
    # Length preferences
    "Human: I want a long series\nAI: Gintama has over 300 episodes of comedy gold mixed with serious arcs. The humor is incredible, and when it gets serious, the emotional payoff from knowing these characters is amazing.",
    
    "Human: Something with many seasons\nAI: JoJo's Bizarre Adventure spans generations with unique protagonists in each part. The art style evolves dramatically, and each story arc feels completely fresh while maintaining core themes.",
    
    "Human: Just a movie recommendation\nAI: Akira is a cyberpunk masterpiece that influenced animation worldwide. The motorcycle chase scenes and psychic powers are still incredible decades later, with unparalleled hand-drawn animation.",
    
    "Human: I prefer shorter series\nAI: Ping Pong The Animation is only 11 episodes but tells a complete story about competition, friendship, and finding your place. The unique art style perfectly matches the energetic story.",
    
    "Human: Movies or short series only\nAI: The Garden of Words is a beautiful 46-minute film about an unlikely friendship. Makoto Shinkai's rain animation is gorgeous, and the story about finding connection is deeply moving.",
    
    # Specific genres expanded
    "Human: I love horror anime\nAI: Higurashi: When They Cry starts cute but becomes genuinely terrifying as mysteries unfold. The psychological horror and time loop elements create an incredibly unsettling atmosphere.",
    
    "Human: What about comedy?\nAI: Konosuba parodies RPG and isekai tropes with hilarious results. Kazuma and his dysfunctional party of misfits create comedy through their complete incompetence at heroics.",
    
    "Human: I like slice of life\nAI: March Comes in Like a Lion beautifully depicts depression and healing through shogi. The realistic portrayal of mental health and found family themes make it incredibly touching.",
    
    "Human: Sports anime recommendations\nAI: Kuroko no Basketball has incredible supernatural basketball action with unique abilities for each player. The teamwork and rivalry dynamics create intense and emotional games.",
    
    "Human: What about mecha anime?\nAI: Gurren Lagann is pure over-the-top mecha action with incredible spirit. Simon's journey from coward to galactic hero is inspiring, with drills that pierce the heavens literally and metaphorically.",
    
    # Art style preferences
    "Human: I like unique art styles\nAI: Mob Psycho 100 has incredibly distinctive animation that matches its psychic themes perfectly. Studio Bones' experimental approach creates visuals unlike anything else in anime.",
    
    "Human: Something with realistic art\nAI: Monster uses realistic character designs that make the psychological thriller elements even more unsettling. The European setting feels authentic with detailed backgrounds.",
    
    "Human: I prefer cute art styles\nAI: Nichijou has adorable character designs that make the absurd comedy even funnier. The contrast between cute visuals and explosive reactions creates perfect comedic timing.",
    
    "Human: Dark art style preferred\nAI: Hell's Paradise has a distinctly dark and gritty art style that matches its violent samurai story. The contrast between beautiful nature and brutal death creates striking visuals.",
    
    "Human: I like colorful animation\nAI: No Game No Life is incredibly vibrant with a unique color palette that makes every scene pop. The chess-like strategic games are visually stunning with rainbow effects.",
    
    # Emotional responses
    "Human: Make me laugh\nAI: Grand Blue is absolutely hilarious with college diving club antics that focus more on drinking than diving. The facial expressions and misunderstandings create non-stop comedy.",
    
    "Human: I want to feel inspired\nAI: A Place Further Than the Universe follows girls pursuing their dream of Antarctic expedition. Their determination to overcome obstacles and chase impossible dreams is incredibly motivating.",
    
    "Human: Something thought-provoking\nAI: Serial Experiments Lain explores identity and reality in the digital age with prophetic themes about internet culture. Each episode adds layers to complex philosophical questions.",
    
    "Human: I want epic battles\nAI: Fate/Zero has incredible battle royale action between legendary heroes summoned as servants. The animation quality and strategic elements make each fight unique and spectacular.",
    
    "Human: Something heartwarming\nAI: Usagi Drop is incredibly sweet about a man raising his grandfather's illegitimate daughter. The realistic portrayal of single parenting and child development is touching and authentic.",
    
    # Subgenre specifics
    "Human: I like magical girl anime\nAI: Puella Magi Madoka Magica deconstructs the magical girl genre with dark psychological themes. The contrast between cute art and serious consequences creates a unique and impactful story.",
    
    "Human: What about isekai?\nAI: Re:Zero is a dark take on being transported to another world where death resets time. Subaru's psychological trauma from repeated deaths creates surprisingly deep character development.",
    
    "Human: I want cyberpunk\nAI: Akudama Drive is stylish cyberpunk with incredible neon aesthetics and over-the-top action. The criminals' heist story unfolds with stunning animation and creative world-building.",
    
    "Human: Post-apocalyptic recommendations\nAI: Trigun follows Vash the Stampede in a desert wasteland with incredible gunfights and surprisingly deep themes about pacifism and humanity's capacity for both good and evil.",
    
    "Human: I like vampire anime\nAI: Hellsing Ultimate features Alucard as an incredibly overpowered vampire fighting other supernatural threats. The gothic atmosphere and extreme violence create a unique vampire experience.",
    
    # Tone preferences
    "Human: Something light-hearted\nAI: Azumanga Daioh is pure wholesome comedy about high school girls and their eccentric teacher. The sketch-based format creates consistently funny moments without drama or conflict.",
    
    "Human: I want something serious\nAI: Grave of the Fireflies deals with war's impact on civilians through siblings struggling to survive. Studio Ghibli's realistic approach makes this incredibly powerful and important.",
    
    "Human: Mix of comedy and drama\nAI: Gintama perfectly balances ridiculous comedy with serious emotional arcs. The tonal shifts feel natural because of strong character development throughout hundreds of episodes.",
    
    "Human: Something bittersweet\nAI: 5 Centimeters Per Second explores how people grow apart over time despite deep connections. The beautiful animation and realistic relationship dynamics create profound melancholy.",
    
    "Human: I want pure fun\nAI: Kill la Kill is pure over-the-top insanity with fashion-based superpowers and incredible energy. Studio Trigger's wild animation style matches the completely absurd premise perfectly.",
    
    # More specific requests
    "Human: I want strong female characters\nAI: Ghost in the Shell features Major Kusanagi as one of anime's strongest female protagonists. Her philosophical struggles with identity in a cybernetic body are handled with incredible depth.",
    
    "Human: Something with good world-building\nAI: Land of the Lustrous creates a fascinating world where gem-based beings fight moon dwellers. The unique biology and mythology create rich lore with beautiful 3D animation.",
    
    "Human: I like ensemble casts\nAI: Durarara!! weaves together multiple storylines in Ikebukuro with a large cast of interconnected characters. Each person's story contributes to the larger urban fantasy narrative.",
    
    "Human: What about time travel?\nAI: Steins;Gate uses time travel to explore cause and effect with incredible detail. The butterfly effect scenarios create genuine tension as small changes have massive consequences.",
    
    "Human: I want cooking anime\nAI: Food Wars! combines cooking with shounen battle anime tropes for incredible results. The food reactions are hilarious, and the culinary techniques are surprisingly educational.",
    
    # Platform availability
    "Human: What's good on Netflix?\nAI: Castlevania has incredible animation and mature storytelling that respects the game source material. The gothic atmosphere and character development across seasons is outstanding.",
    
    "Human: I have Crunchyroll\nAI: Jujutsu Kaisen is perfect with incredible fight animation and a great magic system based on cursed energy. The character designs and supernatural battles are absolutely stunning.",
    
    "Human: What's on Funimation?\nAI: My Hero Academia's entire series is available with both excellent sub and dub options. The superhero academy setting provides consistent character growth and amazing action sequences.",
    
    "Human: I use Hulu\nAI: One Piece is available with hundreds of episodes of pirate adventures. The world-building and character development across decades makes this one of anime's greatest achievements.",
    
    "Human: What can I watch for free?\nAI: Many classic anime are available on YouTube and Tubi. Neon Genesis Evangelion is often free and remains one of anime's most influential and psychologically complex series.",
    
    # Rewatchability
    "Human: Something I can rewatch\nAI: Cowboy Bebop reveals new details on every viewing with its film noir storytelling and jazz soundtrack. Each character's backstory adds layers that reward multiple viewings.",
    
    "Human: I like shows with hidden details\nAI: Serial Experiments Lain is dense with symbolism and foreshadowing that makes sense only after knowing the ending. Each episode contains clues that create entirely new interpretations.",
    
    "Human: What has good replay value?\nAI: Hunter x Hunter's power system and strategic battles reveal new tactical elements on rewatching. The character motivations and foreshadowing become clearer with multiple viewings.",
    
    "Human: I want layers to discover\nAI: Evangelion is famous for requiring multiple viewings to understand its psychological and religious symbolism. Each watch reveals new interpretations of character motivations and themes.",
    
    "Human: Something with Easter eggs\nAI: FLCL is packed with visual references and metaphors that reward careful viewing. The coming-of-age story uses surreal imagery that becomes clearer with analysis and rewatching.",
    
    # Cultural aspects
    "Human: I want to learn about Japan\nAI: Showa Genroku Rakugo Shinju explores traditional Japanese storytelling art with incredible cultural detail. The historical setting and rakugo performances provide authentic cultural immersion.",
    
    "Human: Something with Japanese culture\nAI: Spirited Away is filled with Japanese folklore and spiritual beliefs woven into Chihiro's journey. The bathhouse setting showcases traditional mythology in accessible storytelling.",
    
    "Human: I like traditional themes\nAI: Mushishi explores Japanese spiritual beliefs about nature and balance through beautifully contemplative episodes. Each story draws from traditional folklore with stunning natural imagery.",
    
    "Human: What shows Japanese history?\nAI: Rurouni Kenshin depicts the Meiji Restoration period with samurai transitioning to modern Japan. The historical context adds depth to Kenshin's personal journey from killer to protector.",
    
    "Human: I want authentic Japanese stories\nAI: Only Yesterday captures the realistic experience of Japanese rural life and childhood memories. Studio Ghibli's grounded approach shows authentic cultural details and generational changes.",
    
    # Animation studios
    "Human: I love Studio Ghibli\nAI: Princess Mononoke showcases everything great about Ghibli with environmental themes and stunning hand-drawn animation. The epic scope and spiritual elements create their most ambitious work.",
    
    "Human: What about Studio Trigger?\nAI: Promare is pure Trigger energy with incredible fire-based animation and over-the-top action. The visual style is uniquely colorful and dynamic, perfect for their high-energy storytelling.",
    
    "Human: I like Madhouse productions\nAI: Perfect Blue is Madhouse's psychological masterpiece that influenced films like Black Swan. The blurred reality between idol persona and true self creates genuinely disturbing thriller elements.",
    
    "Human: What has MAPPA made?\nAI: Attack on Titan's final seasons showcase MAPPA's incredible action animation with fluid 3D maneuver gear sequences. Their handling of emotional character moments matches the epic battle scenes.",
    
    "Human: I want Kyoto Animation\nAI: A Silent Voice demonstrates KyoAni's incredible attention to emotional detail through realistic character animation. Every gesture and expression contributes to the powerful story about bullying and redemption.",
    
    # Finale
    "Human: I want something perfect\nAI: Fullmetal Alchemist: Brotherhood is often considered anime's masterpiece with perfect pacing, character development, and thematic depth. Every element from action to philosophy is executed flawlessly.",
    
    "Human: What's the best anime ever?\nAI: That's subjective, but Spirited Away won the Academy Award for good reason. It combines universal themes with uniquely Japanese storytelling and animation that transcends cultural boundaries.",
    
    "Human: I want a masterpiece\nAI: Princess Mononoke tackles environmental destruction and human nature with incredible maturity. The hand-drawn animation and complex moral questions make this an enduring work of art.",
    
    "Human: Something legendary\nAI: Akira revolutionized animation worldwide with unprecedented detail and cyberpunk themes that remain relevant. The motorcycle sequences and psychic destruction scenes are still unmatched decades later.",
    
    "Human: What changed anime forever?\nAI: Neon Genesis Evangelion redefined what anime could be with psychological depth and religious symbolism. Its influence on both animation and popular culture continues to this day.",
    
    # More specific genre combinations
    "Human: I want action with romance\nAI: Eureka Seven combines mecha action with a beautiful coming-of-age love story. Renton and Eureka's relationship develops naturally alongside incredible aerial battles and stunning animation.",
    
    "Human: Comedy with good plot\nAI: The Devil is a Part-Timer! has great comedy from Satan working at McDonald's while building an actually engaging plot about redemption and responsibility in the modern world.",
    
    "Human: Horror with mystery\nAI: Shiki combines vampire horror with small-town mystery as residents slowly disappear. The gradual revelation of what's happening creates incredible tension and moral complexity.",
    
    "Human: Fantasy with politics\nAI: Legend of the Galactic Heroes is space opera with incredible political intrigue between democratic and imperial forces. The strategic battles are matched by complex character relationships.",
    
    "Human: Sci-fi with philosophy\nAI: Ghost in the Shell: Stand Alone Complex explores consciousness and identity in a cyberpunk future. Each episode asks deep questions about what makes us human in a digital age.",
    
    # International appeal
    "Human: Something universal\nAI: Wolf Children transcends cultural boundaries with its story of a mother raising half-wolf children. The themes of single parenting and growing up resonate with audiences worldwide.",
    
    "Human: I want global themes\nAI: Grave of the Fireflies shows war's impact on innocent civilians in a way that applies to conflicts everywhere. The sibling relationship and survival story is universally heartbreaking.",
    
    "Human: Something anyone can enjoy\nAI: Castle in the Sky has adventure, romance, and environmental themes that work for all ages and cultures. The flying sequences and Laputa's mystery create timeless entertainment.",
    
    "Human: Cross-cultural appeal\nAI: Your Name deals with connection across distance and time in ways that transcend specific cultural contexts. The supernatural romance and stunning visuals speak to universal human experiences.",
    
    "Human: I want broad appeal\nAI: One Piece's themes of friendship, dreams, and adventure resonate globally. Despite uniquely Japanese humor, the emotional core of pursuing your dreams with loyal friends is universal.",
    
    # Advanced recommendations
    "Human: I've seen everything mainstream\nAI: Monster is an overlooked psychological masterpiece about a surgeon hunting a sociopathic killer. The European setting and realistic approach create something completely unique in anime.",
    
    "Human: I want something obscure\nAI: Texhnolyze is incredibly dark cyberpunk that explores transhumanism and societal decay. It's challenging viewing but rewards patient viewers with profound philosophical themes.",
    
    "Human: Hidden gems please\nAI: Planetes is hard science fiction about space debris collectors that's surprisingly grounded and thoughtful. The realistic portrayal of space travel and international politics is refreshing.",
    
    "Human: What's underrated?\nAI: Ping Pong The Animation has unique art that turns people away, but the story about competition, friendship, and finding your place is absolutely brilliant with incredible character development.",
    
    "Human: Something most people miss\nAI: Kaiba explores memory and identity through unique art and storytelling. The surreal presentation masks incredibly deep themes about what makes us who we are.",
    
    # Seasonal/mood based
    "Human: Something for winter\nAI: 5 Centimeters Per Second captures the melancholy of winter with beautiful snow scenes and themes about growing apart. The cold atmosphere matches the emotional distance perfectly.",
    
    "Human: I want summer vibes\nAI: Free! is all about summer swimming with gorgeous water animation and themes about friendship and competition. The pool scenes and summer festival atmosphere are incredibly refreshing.",
    
    "Human: Something cozy\nAI: Non Non Biyori is incredibly cozy with rural countryside setting and gentle humor. The slow pace and beautiful nature scenes create perfect relaxation viewing.",
    
    "Human: I need comfort food anime\nAI: K-On! is pure comfort with cute girls doing cute things in their light music club. The friendship dynamics and catchy songs create a warm, happy atmosphere.",
    
    "Human: Something atmospheric\nAI: Mushishi has incredible atmosphere with each episode exploring Japanese folklore in beautiful natural settings. The contemplative pacing and spiritual themes create meditative viewing.",
    
    # Additional 100 conversations
    "Human: I want alien invasion anime\nAI: Parasyte brilliantly explores body horror as aliens take over human hosts. The psychological transformation of the protagonist and questions about humanity versus nature create compelling science fiction.",
    
    "Human: Something about music\nAI: Beck follows a teenager discovering rock music and finding his passion. The realistic portrayal of starting a band and the excellent soundtrack make this incredibly authentic and inspiring.",
    
    "Human: I like detective stories\nAI: Case Closed has hundreds of episodes of clever mystery solving with a detective trapped in a child's body. Each case presents logical puzzles that viewers can solve alongside the protagonist.",
    
    "Human: What about card games?\nAI: Yu-Gi-Oh! combines strategy card battles with Egyptian mythology and friendship themes. The tournament arcs and over-the-top dramatic reactions make each duel incredibly entertaining.",
    
    "Human: I want workplace comedy\nAI: Aggretsuko perfectly captures modern office frustration through a red panda who transforms into a death metal rocker. The workplace humor and stress relief themes are incredibly relatable.",
    
    "Human: Something about art\nAI: Blue Period follows a delinquent student discovering his passion for painting. The realistic portrayal of artistic struggle and growth provides genuine insight into the creative process.",
    
    "Human: I like twin characters\nAI: Ouran High School Host Club features the Hitachiin twins among its cast of eccentric rich students. The romantic comedy explores class differences and identity through entertaining misunderstandings.",
    
    "Human: What has good tournaments?\nAI: Dragon Ball features iconic tournament arcs that helped define shounen anime. The World Martial Arts Tournament format allows multiple character matchups and power scaling moments.",
    
    "Human: I want shape-shifting\nAI: Ranma 1/2 is classic comedy about a martial artist who transforms into a girl when splashed with cold water. The gender-bending situations create endless comedic possibilities.",
    
    "Human: Something with ninjas\nAI: Naruto obviously leads ninja anime with its hidden village setting and chakra-based abilities. The journey from outcast to hero resonates strongly with themes of perseverance and acceptance.",
    
    "Human: I like rival relationships\nAI: Hajime no Ippo showcases incredible boxing rivalries that push each fighter to improve. The sports psychology and training montages create genuine investment in each match outcome.",
    
    "Human: What about treasure hunting?\nAI: One Piece is the ultimate treasure hunting adventure with pirates seeking the legendary treasure. The world exploration and crew dynamics make each island discovery exciting and meaningful.",
    
    "Human: I want magical schools\nAI: Little Witch Academia captures the Harry Potter magic school experience with incredible animation and positive messages about following dreams despite obstacles and criticism.",
    
    "Human: Something with gods\nAI: Noragami follows a minor deity trying to gain followers and recognition. The blend of modern setting with traditional mythology creates unique supernatural comedy and action.",
    
    "Human: I like transformation sequences\nAI: Sailor Moon pioneered magical girl transformation sequences that remain iconic decades later. The friendship themes and episodic monster battles create perfect nostalgic viewing.",
    
    "Human: What about prison settings?\nAI: Deadman Wonderland combines prison survival with supernatural abilities in a twisted amusement park setting. The dark themes and conspiracy elements create intense thriller atmosphere.",
    
    "Human: I want racing anime\nAI: Initial D revolutionized racing anime with incredible car chase sequences and eurobeat soundtrack. The technical driving details and character rivalry create authentic racing excitement.",
    
    "Human: Something with androids\nAI: Time of Eve explores android consciousness and human relationships in a coffee shop where the distinction doesn't matter. The philosophical questions about artificial life are handled thoughtfully.",
    
    "Human: I like magical contracts\nAI: Puella Magi Madoka Magica deconstructs magical girl contracts with dark consequences. The seemingly innocent wish-granting premise hides psychological horror and complex moral choices.",
    
    "Human: What has good villains?\nAI: Fullmetal Alchemist: Brotherhood features complex antagonists with understandable motivations. Even the main villain's plan has logical reasoning, making the moral conflicts more interesting.",
    
    "Human: I want dimension travel\nAI: The Melancholy of Haruhi Suzumiya involves reality manipulation and alternate timelines centered around an eccentric student. The non-linear storytelling and meta-humor create unique viewing experiences.",
    
    "Human: Something with assassins\nAI: Assassination Classroom combines comedy with touching teacher-student relationships as students try to kill their alien teacher. The premise sounds dark but creates surprisingly heartwarming moments.",
    
    "Human: I like memory loss plots\nAI: Angel Beats explores characters who died young and lost memories of their past lives. The afterlife school setting allows for both comedy and deeply emotional character revelations.",
    
    "Human: What about gambling?\nAI: Kakegurui features intense psychological gambling battles in an elite school where students bet everything. The over-the-top reactions and strategic mind games create thrilling competition.",
    
    "Human: I want body swapping\nAI: Your Name obviously excels at body-swapping romance, but Kokoro Connect also explores this concept with multiple characters experiencing supernatural phenomena that test their friendships.",
    
    "Human: Something with pirates\nAI: One Piece remains the definitive pirate adventure anime with incredible world-building spanning decades. Each crew member's dream and the overarching treasure hunt create epic storytelling.",
    
    "Human: I like clone stories\nAI: Ghost in the Shell explores questions of identity and consciousness when minds can be copied and bodies replaced. The cyberpunk setting makes these philosophical questions feel immediate and relevant.",
    
    "Human: What has good parenting?\nAI: Usagi Drop beautifully portrays single parenting as a man raises his grandfather's young daughter. The realistic child development and parenting challenges create authentic emotional moments.",
    
    "Human: I want library settings\nAI: Read or Die features bibliophiles with paper-manipulating powers protecting books and knowledge. The love of literature combined with action sequences creates unique superhero entertainment.",
    
    "Human: Something with prophecies\nAI: The Twelve Kingdoms involves characters transported to a world where they must fulfill ancient prophecies. The political intrigue and world-building create complex fantasy storytelling.",
    
    "Human: I like dual personalities\nAI: Dr. Jekyll and Mr. Hyde themes appear in several anime, but Tokyo Ghoul handles the struggle between human and monster identities with particular psychological depth and visual symbolism.",
    
    "Human: What about circus themes?\nAI: Karneval follows characters involved with a government circus organization fighting crime. The colorful aesthetic and mysterious background create intriguing supernatural action.",
    
    "Human: I want teacher protagonists\nAI: Great Teacher Onizuka features a former gang member becoming an unconventional high school teacher. The comedy comes from his unorthodox methods actually helping troubled students.",
    
    "Human: Something with newspapers\nAI: Monthly Girls' Nozaki-kun involves creating shoujo manga and deals with publishing deadlines and creative processes. The comedy comes from misunderstandings about romance and artistic collaboration.",
    
    "Human: I like duel academies\nAI: Yu-Gi-Oh! GX takes place in a duel academy where students learn card game strategy. The school setting allows for character development between tournament-style battles.",
    
    "Human: What has good redemption arcs?\nAI: Vegeta's transformation from villain to hero in Dragon Ball Z remains one of anime's best redemption stories. His pride and gradual character growth span multiple story arcs.",
    
    "Human: I want desert settings\nAI: Trigun takes place in a desert wasteland with unique Western themes. Vash the Stampede's pacifist philosophy contrasts beautifully with the harsh survival environment.",
    
    "Human: Something with photography\nAI: Love Live! School Idol Project doesn't focus on photography specifically, but several anime explore visual arts. Consider art-focused series for creative inspiration and technical detail.",
    
    "Human: I like mask-wearing characters\nAI: Code Geass features Lelouch's masked alter ego Zero leading a rebellion. The dual identity creates dramatic tension and allows for complex character development and reveals.",
    
    "Human: What about fashion?\nAI: Paradise Kiss follows fashion design students creating avant-garde clothing. The artistic focus and romantic relationships create mature storytelling about pursuing creative careers.",
    
    "Human: I want butler characters\nAI: Black Butler combines Victorian gothic atmosphere with supernatural mysteries involving a demon butler. The dark humor and elegant aesthetic create unique historical fantasy.",
    
    "Human: Something with festivals\nAI: Many slice-of-life anime feature Japanese festivals, but Tamako Market particularly celebrates community traditions and local culture through a shopping district's daily life and seasonal celebrations.",
    
    "Human: I like scientist characters\nAI: Dr. Stone features Senku using scientific knowledge to rebuild civilization after humanity turns to stone. The educational elements make complex chemistry and physics accessible and exciting.",
    
    "Human: What has good world destruction?\nAI: Gurren Lagann escalates from underground villages to galaxy-spanning battles that literally pierce dimensions. The scale increases dramatically while maintaining character-driven emotional stakes.",
    
    "Human: I want ghost stories\nAI: Ghost Hunt presents various supernatural investigations with different types of paranormal phenomena. Each arc explores different horror traditions and investigation methods.",
    
    "Human: Something with multiple timelines\nAI: Steins;Gate masterfully handles timeline branching and butterfly effect consequences. The complexity rewards attention while maintaining emotional investment in character relationships.",
    
    "Human: I like shapeshifters\nAI: Fruits Basket features characters who transform into zodiac animals when hugged. The curse creates both comedy and serious exploration of family trauma and acceptance.",
    
    "Human: What about underground settings?\nAI: Made in Abyss takes place in a massive underground chasm filled with dangerous creatures and mysterious artifacts. The descent into darkness mirrors the story's increasingly serious tone.",
    
    "Human: I want knight characters\nAI: The Seven Deadly Sins features knights with unique powers protecting a kingdom. The medieval fantasy setting allows for both epic battles and character backstory exploration.",
    
    "Human: Something with amnesia\nAI: Kino's Journey features episodic travel stories where the protagonist explores different countries and cultures. While not focused on amnesia, it explores identity and philosophy through wandering.",
    
    "Human: I like cafe settings\nAI: Blend S is workplace comedy about a themed cafe where employees play different character types. The service industry humor and character interactions create lighthearted entertainment.",
    
    "Human: What has good plot twists?\nAI: Attack on Titan reveals major plot twists that completely recontextualize earlier events. The basement revelation and true nature of titans create incredible narrative payoffs.",
    
    "Human: I want cheerleader anime\nAI: Cheer Danshi follows male college students starting a cheerleading team. The sports anime format explores masculine expression through traditionally feminine activity with surprising depth.",
    
    "Human: Something with laboratories\nAI: Steins;Gate's Future Gadget Laboratory serves as headquarters for time travel experiments. The amateur scientist atmosphere contrasts with the serious consequences of their discoveries.",
    
    "Human: I like survival themes\nAI: Dr. Stone combines post-apocalyptic survival with scientific problem-solving. Rebuilding civilization from scratch creates unique challenges that require both knowledge and cooperation.",
    
    "Human: What about idol groups?\nAI: Love Live! follows high school girls forming an idol group to save their school. The music performances and friendship dynamics create uplifting entertainment with catchy songs.",
    
    "Human: I want cybernetic enhancement\nAI: Ghost in the Shell explores cybernetic augmentation and questions of identity when bodies can be completely replaced. The philosophical depth matches the incredible action sequences.",
    
    "Human: Something with parallel worlds\nAI: Re:Zero explores alternate timeline consequences through death-based time loops. The psychological impact of repeated failure creates surprisingly dark character development.",
    
    "Human: I like tournament formats\nAI: Hunter x Hunter's exam arcs and tournament sequences showcase creative rule sets and strategic thinking. Each competition tests different skills beyond simple combat ability.",
    
    "Human: What has good mystery boxes?\nAI: The Promised Neverland presents mysteries that unfold gradually, revealing the true nature of the orphanage and outside world. The revelation process maintains tension throughout.",
    
    "Human: I want elemental powers\nAI: Avatar isn't anime, but Full Metal Alchemist has incredible elemental manipulation through alchemy. The equivalent exchange rule creates strategic limitations and moral consequences.",
    
    "Human: Something with multiple protagonists\nAI: Baccano! features an ensemble cast across different time periods with interconnected stories. The non-linear narrative reveals how seemingly separate characters are connected.",
    
    "Human: I like military themes\nAI: Legend of the Galactic Heroes presents space warfare with incredible strategic depth and political complexity. The military tactics and character relationships create epic storytelling.",
    
    "Human: What about artificial intelligence?\nAI: Serial Experiments Lain explores consciousness and identity in digital spaces. The prescient themes about internet culture and virtual reality feel more relevant than ever.",
    
    "Human: I want coming-of-age stories\nAI: A Silent Voice handles bullying, disability, and redemption with incredible maturity. The character growth and social commentary create powerful emotional impact.",
    
    "Human: Something with dragon characters\nAI: Miss Kobayashi's Dragon Maid features dragons living as maids in modern Japan. The slice-of-life format explores cultural differences and found family themes through comedy.",
    
    "Human: I like conspiracy plots\nAI: Monster involves a complex conspiracy spanning decades with multiple countries and organizations. The psychological thriller elements and realistic European setting create incredible tension.",
    
    "Human: What has good character chemistry?\nAI: The dynamic between Edward and Alphonse Elric in Fullmetal Alchemist: Brotherhood showcases incredible sibling relationships. Their banter and mutual support drive the emotional core.",
    
    "Human: I want ancient civilizations\nAI: Dr. Stone rebuilds human civilization from scratch, showing the development of technology and social structures. The scientific accuracy makes historical progress fascinating.",
    
    "Human: Something with multiple seasons\nAI: Attack on Titan's four seasons show incredible evolution in animation quality, storytelling complexity, and thematic depth. Each season feels like a different show while maintaining continuity.",
    
    "Human: I like transformation themes\nAI: Tokyo Ghoul explores transformation from human to monster with psychological depth. The identity crisis and moral questions create compelling character development.",
    
    "Human: What about virtual reality?\nAI: Sword Art Online popularized the trapped-in-VR premise, though the execution varies. The concept of living entirely within game worlds raises interesting questions about reality.",
    
    "Human: I want historical accuracy\nAI: Golden Kamuy combines Russo-Japanese War aftermath with Ainu culture in incredible detail. The historical research and cultural representation create authentic period storytelling.",
    
    "Human: Something with unique art styles\nAI: Tatami Galaxy uses distinctive visual design and rapid-fire dialogue to explore college life and social anxiety. The experimental presentation matches the protagonist's mental state.",
    
    "Human: I like medical themes\nAI: Cells at Work! personifies body functions through characters representing different cell types. The educational content makes biology fascinating while maintaining entertaining storylines.",
    
    "Human: What has good emotional payoffs?\nAI: Clannad: After Story builds emotional investment over many episodes before delivering devastating and uplifting moments. The family themes and character development create lasting impact.",
    
    "Human: I want space exploration\nAI: Planetes follows debris collectors in realistic near-future space travel. The hard science fiction approach and international politics create grounded storytelling about space development.",
    
    "Human: Something with good mysteries\nAI: Hyouka follows a high school literature club solving everyday mysteries with logical deduction. The slice-of-life setting makes small puzzles feel significant and engaging.",
    
    "Human: I like friendship themes\nAI: One Piece remains unmatched for friendship themes, showing how diverse people become family through shared adventures. The crew loyalty and mutual support create emotional investment.",
    
    "Human: What about genetic engineering?\nAI: Gundam SEED explores genetic modification creating enhanced humans and the resulting social conflicts. The political themes and personal relationships create complex moral questions.",
    
    "Human: I want creative powers\nAI: JoJo's Bizarre Adventure features incredibly creative Stand abilities that lead to unique problem-solving and battle strategies. Each power has specific rules that create tactical thinking.",
    
    "Human: Something with good dialogue\nAI: The Monogatari series features incredible wordplay and philosophical conversations that drive character development. The dialogue-heavy approach creates intellectual engagement with supernatural elements.",
    
    "Human: I like ensemble storytelling\nAI: Durarara!! weaves together multiple character perspectives in urban fantasy setting. The interconnected storylines reveal how seemingly separate people affect each other's lives.",
    
    "Human: What has satisfying conclusions?\nAI: Fullmetal Alchemist: Brotherhood provides incredibly satisfying resolution to all plot threads and character arcs. The ending feels earned and addresses every major story element.",
    
    "Human: I want unique premises\nAI: The Tatami Galaxy's Groundhog Day-like structure explores different college social circles and their impact on personal growth. The experimental storytelling creates fresh perspectives on familiar themes.",
    
    "Human: Something with good pacing\nAI: Hunter x Hunter varies its pacing perfectly, from quick tournament arcs to slow-burn character development. Each story segment feels properly developed without dragging or rushing.",
    
    "Human: I like philosophical themes\nAI: Serial Experiments Lain asks deep questions about identity, reality, and consciousness in digital age. The surreal presentation encourages multiple interpretations and discussions.",
    
    "Human: What about alternate history?\nAI: Code Geass presents alternate history where Japan was conquered by Britannia. The political intrigue and resistance themes create compelling alternate world storytelling.",
    
    "Human: I want creative animation\nAI: FLCL uses incredibly experimental animation techniques to represent adolescent confusion and growth. The visual metaphors and symbolic imagery create unique viewing experiences.",
    
    "Human: Something with good buildup\nAI: Monster slowly builds tension over 74 episodes, developing complex characters and moral questions. The psychological thriller pacing rewards patient viewers with incredible payoffs.",
    
    "Human: I like unconventional narratives\nAI: Baccano! tells its story non-chronologically across multiple time periods. The puzzle-like structure reveals connections and character relationships through creative storytelling techniques."
]

    import random
    random.shuffle(conversations)

    total = len(conversations)
    train_end = int(0.8 * total)
    val_end = int(0.9 * total)

    train_data = conversations[:train_end]
    val_data = conversations[train_end:val_end]
    test_data = conversations[val_end:]

    save_to_file(train_data, "/Users/immanuelegboche/Desktop/work/BigOEnergy/llm/data/processed/train.txt")
    save_to_file(val_data, "/Users/immanuelegboche/Desktop/work/BigOEnergy/llm/data/processed/val_conversations.txt") 
    save_to_file(test_data, "/Users/immanuelegboche/Desktop/work/BigOEnergy/llm/data/processed/test_conversations.txt")

if __name__ == "__main__":
    split_conversations()