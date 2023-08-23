import random

# New feature
# If the game is lost show the user the word they had to guess
# Also store in the letter that was guessed but not correct so the user won't need to try them again


dictionary = ["aback", "abaft", "abandoned", "abashed", "aberrant", "abhorrent", "abiding", "abject", "ablaze", "able",
              "abnormal", "aboard", "aboriginal", "abortive", "abounding", "abrasive", "abrupt", "absent", "absorbed",
              "absorbing", "abstracted", "absurd", "abundant", "abusive", "accept", "acceptable", "accessible",
              "accidental",
              "account", "accurate", "achiever", "acid", "acidic", "acoustic", "acoustics", "acrid", "act", "action",
              "activity", "actor", "actually", "ad hoc", "adamant", "adaptable", "add", "addicted", "addition",
              "adhesive",
              "adjoining", "adjustment", "admire", "admit", "adorable", "adventurous", "advertisement", "advice",
              "advise",
              "afford", "afraid", "aftermath", "afternoon", "afterthought", "aggressive", "agonizing", "agree",
              "agreeable",
              "agreement", "ahead", "air", "airplane", "airport", "ajar", "alarm", "alcoholic", "alert", "alike",
              "alive",
              "alleged", "allow", "alluring", "aloof", "amazing", "ambiguous", "ambitious", "amount", "amuck", "amuse",
              "amused", "amusement", "amusing", "analyze", "ancient", "anger", "angle", "angry", "animal", "animated",
              "announce", "annoy", "annoyed", "annoying", "answer", "ants", "anxious", "apathetic", "apologise",
              "apparatus",
              "apparel", "appear", "applaud", "appliance", "appreciate", "approval", "approve", "aquatic", "arch",
              "argue",
              "argument", "arithmetic", "arm", "army", "aromatic", "arrange", "arrest", "arrive", "arrogant", "art",
              "ashamed", "ask", "aspiring", "assorted", "astonishing", "attach", "attack", "attempt", "attend",
              "attract",
              "attraction", "attractive", "aunt", "auspicious", "authority", "automatic", "available", "average",
              "avoid",
              "awake", "aware", "awesome", "awful", "axiomatic", "babies", "baby", "back", "bad", "badge", "bag",
              "bait",
              "bake", "balance", "ball", "ban", "bang", "barbarous", "bare", "base", "baseball", "bashful", "basin",
              "basket", "basketball", "bat", "bath", "bathe", "battle", "bawdy", "bead", "beam", "bear", "beautiful",
              "bed",
              "bedroom", "beds", "bee", "beef", "befitting", "beg", "beginner", "behave", "behavior", "belief",
              "believe",
              "bell", "belligerent", "bells", "belong", "beneficial", "bent", "berry", "berserk", "best", "better",
              "bewildered", "big", "bike", "bikes", "billowy", "bird", "birds", "birth", "birthday", "bit", "bite",
              "bitter", "bizarre", "black", "blade", "bleach", "bless", "blind", "blink",
              "blood", "bloody", "blot", "blow", "blue", "blush", "blushing", "board", "boast", "boat", "boil",
              "boiling", "bolt", "bomb", "bone", "book", "books", "boorish", "boot", "border", "bore", "bored",
              "boring",
              "borrow", "bottle", "bounce", "bouncy", "boundary", "boundless", "bow", "box", "boy", "brainy", "brake",
              "branch", "brash", "brass", "brave", "brawny", "breakable", "breath", "breathe", "breezy", "brick",
              "bridge",
              "brief", "bright", "broad", "broken", "brother", "brown", "bruise", "brush", "bubble", "bucket",
              "building",
              "bulb", "bump", "bumpy", "burly", "burn", "burst", "bury", "bushes", "business", "bustling", "busy",
              "butter",
              "button", "buzz", "cabbage", "cable", "cactus", "cagey", "cake", "cakes", "calculate", "calculating",
              "calculator", "calendar", "call", "callous", "calm", "camera", "camp", "can", "cannon", "canvas", "cap",
              "capable", "capricious", "caption", "car", "card", "care", "careful", "careless", "caring", "carpenter",
              "carriage", "carry", "cars", "cart", "carve", "cast", "cat", "cats", "cattle", "cause", "cautious",
              "cave",
              "ceaseless", "celery", "cellar", "cemetery", "cent", "certain", "chalk", "challenge", "chance", "change",
              "changeable", "channel", "charge", "charming", "chase", "cheap", "cheat", "check", "cheer", "cheerful",
              "cheese", "chemical", "cherries", "cherry", "chess", "chew", "chicken", "chickens", "chief", "childlike",
              "children", "chilly", "chin", "chivalrous", "choke", "chop", "chubby", "chunky", "church", "circle",
              "claim",
              "clam", "clammy", "clap", "class", "classy", "clean", "clear", "clever", "clip", "cloistered", "close",
              "closed", "cloth", "cloudy", "clover", "club", "clumsy", "cluttered", "coach", "coal", "coast", "coat",
              "cobweb", "coherent", "coil", "cold", "collar", "collect", "color", "colorful", "colossal", "colour",
              "comb",
              "combative", "comfortable", "command", "committee", "common", "communicate", "company", "compare",
              "comparison", "compete", "competition", "complain", "complete", "complex", "concentrate", "concern",
              "concerned", "condemned", "condition", "confess", "confuse", "confused", "connect", "connection",
              "conscious",
              "consider", "consist", "contain", "continue", "control", "cooing", "cook", "cool", "cooperative",
              "coordinated", "copper", "copy", "corn", "correct", "cough", "count", "country", "courageous", "cover",
              "cow",
              "cowardly", "cows", "crabby", "crack", "cracker", "crash", "crate", "craven", "crawl", "crayon", "crazy",
              "cream", "creator", "creature", "credit", "creepy", "crib", "crime", "crook", "crooked", "cross", "crow",
              "crowd", "crowded", "crown", "cruel", "crush", "cry", "cub", "cuddly", "cultured", "cumbersome", "cup",
              "cure",
              "curious", "curl", "curly", "current", "curtain", "curve", "curved", "curvy", "cushion", "cut", "cute",
              "cycle", "cynical", "dad", "daffy", "daily", "dam", "damage", "damaged", "damaging", "damp", "dance",
              "dangerous", "dapper", "dare", "dark", "dashing", "daughter", "day", "dazzling", "dead", "deadpan",
              "deafening", "dear", "death", "debonair", "debt", "decay", "deceive", "decide", "decision", "decisive",
              "decorate", "decorous", "deep", "deeply", "deer", "defeated", "defective", "defiant", "degree", "delay",
              "delicate", "delicious", "delight", "delightful", "delirious", "deliver", "demonic", "depend",
              "dependent",
              "depressed", "deranged", "describe", "descriptive", "desert", "deserted", "deserve", "design", "desire",
              "desk", "destroy", "destruction", "detail", "detailed", "detect", "determined", "develop", "development",
              "devilish", "didactic", "different", "difficult", "digestion", "diligent", "dime", "dinner", "dinosaurs",
              "direction", "direful", "dirt", "dirty", "disagree", "disagreeable", "disappear", "disapprove", "disarm",
              "disastrous", "discover", "discovery", "discreet", "discussion", "disgusted", "disgusting",
              "disillusioned",
              "dislike", "dispensable", "distance", "distinct", "distribution", "disturbed", "divergent", "divide",
              "division", "dizzy", "dock", "doctor", "dog", "dogs", "doll", "dolls", "domineering", "donkey", "door",
              "double", "doubt", "doubtful", "downtown", "drab", "draconian", "drag", "drain", "dramatic", "drawer",
              "dream",
              "dreary", "dress", "drink", "drip", "driving", "drop", "drown", "drum", "drunk", "dry", "duck", "ducks",
              "dull", "dust", "dusty", "dynamic", "dysfunctional", "eager", "ear", "early", "earn", "earsplitting",
              "earth",
              "earthquake", "earthy", "easy", "eatable", "economic", "edge", "educate", "educated", "education",
              "effect",
              "efficacious", "efficient", "egg", "eggnog", "eggs", "eight", "elastic", "elated", "elbow", "elderly",
              "electric", "elegant", "elfin", "elite", "embarrass", "embarrassed", "eminent", "employ", "empty",
              "enchanted",
              "enchanting", "encourage", "encouraging", "end", "endurable", "energetic", "engine", "enjoy", "enormous",
              "enter", "entertain", "entertaining", "enthusiastic", "envious", "equable", "equal", "erect", "erratic",
              "error", "escape", "ethereal", "evanescent", "evasive", "even", "event", "examine", "example",
              "excellent",
              "exchange", "excite", "excited", "exciting", "exclusive", "excuse", "exercise", "exist", "existence",
              "exotic",
              "expand", "expansion", "expect", "expensive", "experience", "expert", "explain", "explode", "extend",
              "exuberant", "exultant", "eye", "eyes", "fabulous", "face", "fact", "fade",
              "faded", "fail", "faint", "fair", "fairies", "faithful", "fall", "fallacious", "false", "familiar",
              "famous",
              "fanatical", "fancy", "fang", "fantastic", "far", "farm", "fascinated", "fast", "fasten", "fat",
              "faulty", "fax", "fear", "fearful", "fearless", "feeble", "feeling", "feigned", "female", "fence",
              "fertile",
              "festive", "fetch", "few", "field", "fierce", "file", "fill", "film", "filthy", "fine", "finger",
              "finicky",
              "fire", "fireman", "first", "fish", "fit", "five", "fix", "fixed", "flag", "flagrant", "flaky", "flame",
              "flap", "flash", "flashy", "flat", "flavor", "flawless", "flesh", "flight", "flimsy", "flippant", "float",
              "flock", "flood", "floor", "flow", "flower", "flowers", "flowery", "fluffy", "fluttering", "fly", "foamy",
              "fog", "fold", "follow", "food", "fool", "foolish", "foot", "force", "foregoing", "forgetful", "fork",
              "form",
              "fortunate", "found", "four", "fowl", "fragile", "frail", "frame", "frantic", "free", "freezing",
              "frequent",
              "fresh", "fretful", "friction", "friend", "friendly", "friends", "frighten", "frightened", "frightening",
              "frog", "frogs", "front", "fruit", "fry", "fuel", "full", "fumbling", "functional", "funny", "furniture",
              "furry", "furtive", "future", "futuristic", "fuzzy", "gabby", "gainful", "gamy", "gaping", "garrulous",
              "gate",
              "gather", "gaudy", "gaze", "geese", "general", "gentle", "ghost", "giant", "giants", "giddy", "gifted",
              "gigantic", "giraffe", "girl", "girls", "glamorous", "glass", "gleaming", "glib", "glistening",
              "glorious",
              "glossy", "glove", "glow", "glue", "godly", "gold", "good", "goofy", "gorgeous", "government", "governor",
              "grab", "graceful", "grade", "grain", "grandfather", "grandiose", "grandmother", "grape", "grass",
              "grate",
              "grateful", "gratis", "gray", "grease", "greasy", "great", "greedy", "green", "greet", "grey", "grieving",
              "grin", "grip", "groan", "groovy", "grotesque", "grouchy", "ground", "group", "growth", "grubby",
              "gruesome",
              "grumpy", "guarantee", "guard", "guarded", "guess", "guide", "guiltless", "guitar", "gullible", "gun",
              "gusty",
              "guttural", "habitual", "hair", "haircut", "half", "hall", "hallowed", "halting", "hammer", "hand",
              "handle",
              "hands", "handsome", "handsomely", "handy", "hang", "hanging", "hapless", "happen", "happy", "harass",
              "harbor", "hard", "harm", "harmonious", "harmony", "harsh", "hat", "hate", "hateful", "haunt",
              "head", "heady", "heal", "health", "healthy", "heap", "heartbreaking", "heat", "heavenly", "heavy",
              "hellish",
              "help", "helpful", "helpless", "hesitant", "hideous", "high", "highfalutin", "hilarious",
              "hill", "hissing", "historical", "history", "hobbies", "hole", "holiday", "holistic", "hollow", "home",
              "homeless", "homely", "honey", "honorable", "hook", "hop", "hope", "horn", "horrible", "horse", "horses",
              "hose", "hospitable", "hospital", "hot", "hour", "house", "houses", "hover", "hug", "huge", "hulking",
              "hum",
              "humdrum", "humor", "humorous", "hungry", "hunt", "hurried", "hurry", "hurt", "hushed", "husky",
              "hydrant",
              "hypnotic", "hysterical", "ice", "icicle", "icky", "icy", "idea", "identify", "idiotic", "ignorant",
              "ignore",
              "ill", "illegal", "illustrious", "imaginary", "imagine", "immense", "imminent",
              "impartial", "imperfect", "impolite", "important", "imported", "impossible", "impress", "improve",
              "impulse",
              "incandescent", "include", "income", "incompetent", "inconclusive", "increase", "incredible",
              "industrious",
              "industry", "inexpensive", "infamous", "influence", "inform", "inject", "injure", "ink", "innate",
              "innocent",
              "inquisitive", "insect", "insidious", "instinctive", "instruct", "instrument", "insurance", "intelligent",
              "intend", "interest", "interesting", "interfere", "internal", "interrupt", "introduce", "invent",
              "invention",
              "invincible", "invite", "irate", "iron", "irritate", "irritating", "island", "itch", "itchy", "jaded",
              "jagged", "jail", "jam", "jar", "jazzy", "jealous", "jeans", "jelly", "jellyfish", "jewel", "jittery",
              "jobless", "jog", "join", "joke", "jolly", "joyous", "judge", "judicious", "juggle", "juice", "juicy",
              "jumbled", "jump", "jumpy", "juvenile", "kaput", "keen", "kettle", "key", "kick", "kill", "kind",
              "kindhearted", "kindly", "kiss", "kittens", "kitty", "knee", "kneel", "knife", "knit", "knock", "knot",
              "knotty", "knowing", "knowledge", "knowledgeable", "known", "label", "labored", "laborer", "lace",
              "lackadaisical", "lacking", "ladybug", "lake", "lame", "lamentable", "lamp", "land", "language",
              "languid",
              "large", "last", "late", "laugh", "laughable", "launch", "lavish", "lazy", "lean", "learn", "learned",
              "leather", "left", "leg", "legal", "legs", "lethal", "letter", "letters", "lettuce", "level", "lewd",
              "library", "license", "lick", "lie", "light", "lighten", "like", "likeable", "limit", "limping", "line",
              "linen", "lip", "liquid", "list", "listen", "literate", "little", "live", "lively", "living", "load",
              "loaf",
              "lock", "locket", "lonely", "long", "longing", "look", "loose", "lopsided", "loss", "loud",
              "loutish", "love", "lovely", "loving", "low", "lowly", "lucky", "ludicrous", "lumber", "lumpy", "lunch",
              "lunchroom", "lush", "luxuriant", "lying", "lyrical", "macabre", "machine", "macho", "maddening", "madly",
              "magenta", "magic", "magical", "magnificent", "maid", "mailbox", "majestic", "makeshift", "male",
              "malicious",
              "mammoth", "man", "manage", "maniacal", "many", "marble", "march", "mark", "marked", "market", "married",
              "marry", "marvelous", "mask", "mass", "massive", "match", "mate", "material", "materialistic", "matter",
              "mature", "meal", "mean", "measly", "measure", "meat", "meaty", "meddle", "medical", "meek", "meeting",
              "mellow", "melodic", "melt", "melted", "memorize", "memory", "men", "mend", "merciful", "mere", "mess up",
              "messy", "metal", "mice", "middle", "mighty", "military", "milk", "milky", "mind", "mindless", "mine",
              "miniature", "minister", "minor", "mint", "minute", "miscreant", "miss", "mist", "misty", "mitten", "mix",
              "mixed", "moan", "moaning", "modern", "moldy", "mom", "momentous", "money", "monkey", "month", "moon",
              "moor",
              "morning", "mother", "motion", "motionless", "mountain", "mountainous", "mourn", "mouth", "move",
              "muddle",
              "muddled", "mug", "multiply", "mundane", "murder", "murky", "muscle", "mushy", "mute", "mysterious",
              "nail",
              "naive", "name", "nappy", "narrow", "nasty", "nation", "natural", "naughty", "nauseating", "near", "neat",
              "nebulous", "necessary", "neck", "need", "needle", "needless", "needy", "neighborly", "nerve", "nervous",
              "nest", "new", "next", "nice", "nifty", "night", "nimble", "nine", "nippy", "nod", "noise", "noiseless",
              "noisy", "nonchalant", "nondescript", "nonstop", "normal", "north", "nose", "nostalgic", "nosy", "note",
              "notebook", "notice", "noxious", "null", "number", "numberless", "numerous", "nut", "nutritious", "nutty",
              "oafish", "oatmeal", "obedient", "obeisant", "obese", "obey", "object", "obnoxious", "obscene",
              "obsequious",
              "observant", "observation", "observe", "obsolete", "obtain", "obtainable", "occur", "ocean", "oceanic",
              "odd",
              "offbeat", "offend", "offer", "office", "oil", "old", "omniscient", "one", "onerous", "open",
              "opposite", "optimal", "orange", "oranges", "order", "ordinary", "organic", "ossified", "outgoing",
              "outrageous", "outstanding", "oval", "oven", "overconfident", "overflow", "overjoyed", "overrated",
              "overt",
              "overwrought", "owe", "own", "pack", "paddle", "page", "pail", "painful", "painstaking", "paint", "pale",
              "paltry", "pan", "pancake", "panicky", "panoramic", "paper", "parallel", "parcel", "parched", "park",
              "parsimonious", "part", "partner", "party", "pass", "passenger", "past", "paste", "pastoral", "pat",
              "pathetic", "pause", "payment", "peace", "peaceful", "pear", "peck", "pedal", "peel", "peep", "pen",
              "pencil",
              "penitent", "perfect", "perform", "periodic", "permissible", "permit", "perpetual", "person", "pest",
              "pet",
              "petite", "pets", "phobic", "phone", "physical", "picayune", "pick", "pickle", "picture", "pie", "pies",
              "pig",
              "pigs", "pin", "pinch", "pine", "pink", "pipe", "piquant", "pizzas", "place", "placid", "plain", "plan",
              "plane", "planes", "plant", "plantation", "plants", "plastic", "plate", "plausible", "play", "playground",
              "pleasant", "please", "pleasure", "plot", "plough", "plucky", "plug", "pocket", "point", "pointless",
              "poised",
              "poison", "poke", "polish", "polite", "political", "pollution", "poor", "pop", "popcorn", "porter",
              "position",
              "possess", "possessive", "possible", "post", "pot", "potato", "pour", "powder", "power", "powerful",
              "practice", "pray", "preach", "precede", "precious", "prefer", "premium", "prepare", "present",
              "preserve",
              "press", "pretend", "pretty", "prevent", "previous", "price", "pricey", "prick", "prickly", "print",
              "private",
              "probable", "produce", "productive", "profit", "profuse", "program", "promise", "property", "prose",
              "protect",
              "protective", "protest", "proud", "provide", "psychedelic", "psychotic", "public", "puffy", "pull",
              "pump",
              "pumped", "punch", "puncture", "punish", "punishment", "puny", "purple", "purpose", "purring", "push",
              "pushy",
              "puzzled", "puzzling", "quack", "quaint", "quarrelsome", "quarter", "quartz", "queen", "question",
              "questionable", "queue", "quick", "quickest", "quicksand", "quiet", "quill", "quilt", "quince", "quirky",
              "quiver", "quixotic", "quizzical", "rabbit", "rabbits", "rabid", "race", "racial", "radiate", "ragged",
              "rail",
              "railway", "rain", "rainstorm", "rainy", "raise", "rake", "rambunctious", "rampant", "range", "rapid",
              "rare",
              "raspy", "rat", "rate", "ratty", "ray", "reach", "reaction", "reading", "ready", "real", "realize",
              "reason",
              "rebel", "receipt", "receive", "receptive", "recess", "recognise", "recondite", "record", "red", "reduce",
              "redundant", "reflect", "reflective", "refuse", "regret", "regular", "reign", "reject", "rejoice",
              "relation",
              "relax", "release", "relieved", "religion", "rely", "remain", "remarkable", "remember", "remind",
              "reminiscent", "remove", "repair", "repeat", "replace", "reply", "report", "representative", "reproduce",
              "repulsive", "request", "rescue", "resolute", "resonant", "respect", "responsible", "rest", "retire",
              "return",
              "reward", "rhetorical", "rhyme", "rhythm", "rice", "rich", "riddle", "rifle", "right", "righteous",
              "rightful",
              "rigid", "ring", "rings", "rinse", "ripe", "risk", "ritzy", "river", "road", "roasted", "rob", "robin",
              "robust", "rock", "rod", "roll", "romantic", "roof", "room", "roomy", "root", "rose", "rot", "rotten",
              "rough",
              "round", "route", "royal", "rub", "ruddy", "rude", "ruin", "rule", "run", "rural", "rush", "rustic",
              "ruthless", "sable", "sack", "sad", "safe", "sail", "salt", "salty", "same", "sand", "sassy", "satisfy",
              "satisfying", "save", "savory", "saw", "scale", "scandalous", "scarce", "scare", "scarecrow", "scared",
              "scarf", "scary", "scatter", "scattered", "scene", "scent", "school", "science", "scientific",
              "scintillating",
              "scissors", "scold", "scorch", "scrape", "scratch", "scrawny", "scream", "screeching", "screw",
              "scribble",
              "scrub", "sea", "seal", "search", "seashore", "seat", "second", "secret", "secretary",
              "secretive", "sedate", "seed", "seemly", "selection", "selective", "self", "selfish", "sense", "separate",
              "serious", "servant", "serve", "settle", "shade", "shaggy", "shake", "shaky", "shallow", "shame", "shape",
              "share", "sharp", "shave", "sheep", "sheet", "shelf", "shelter", "shiny", "ship", "shirt", "shiver",
              "shivering", "shock", "shocking", "shoe", "shoes", "shop", "short", "show", "shrill", "shrug", "shut",
              "shy",
              "sick", "side", "sidewalk", "sigh", "sign", "signal", "silent", "silk", "silky", "silly", "silver",
              "simple",
              "simplistic", "sin", "sincere", "sink", "sip", "sister", "sisters", "six", "size", "skate", "ski",
              "skillful",
              "skin", "skinny", "skip", "skirt", "sky", "slap", "slave", "sleep", "sleepy", "sleet", "slim", "slimy",
              "slip",
              "slippery", "slope", "sloppy", "slow", "small", "smart", "smash", "smell", "smelly", "smile", "smiling",
              "smoggy", "smoke", "smooth", "snail", "snails", "snake", "snakes", "snatch", "sneaky", "sneeze", "sniff",
              "snobbish", "snore", "snotty", "snow", "soak", "soap", "society", "sock", "soda", "sofa", "soft", "soggy",
              "solid", "somber", "son", "song", "songs", "soothe", "sophisticated", "sordid", "sore", "sort", "sound",
              "soup", "sour", "space", "spade", "spare", "spark", "sparkle", "sparkling", "special", "spectacular",
              "spell",
              "spicy", "spiders", "spiffy", "spiky", "spill", "spiritual", "spiteful", "splendid", "spoil", "sponge",
              "spooky", "spoon", "spot", "spotless", "spotted", "spotty", "spray", "spring", "sprout", "spurious",
              "spy",
              "squalid", "square", "squash", "squeak", "squeal", "squealing", "squeamish", "squeeze", "squirrel",
              "stage",
              "stain", "staking", "stale", "stamp", "standing", "star", "stare", "start", "statement", "station",
              "statuesque", "stay", "steadfast", "steady", "steam", "steel", "steep", "steer", "stem", "step",
              "stereotyped",
              "stew", "stick", "sticks", "sticky", "stiff", "stimulating", "stingy", "stir", "stitch", "stocking",
              "stomach",
              "stone", "stop", "store", "stormy", "story", "stove", "straight", "strange", "stranger", "strap", "straw",
              "stream", "street", "strengthen", "stretch", "string", "strip", "striped", "stroke", "strong",
              "structure",
              "stuff", "stupendous", "stupid", "sturdy", "subdued", "subsequent", "substance", "substantial",
              "subtract",
              "succeed", "successful", "succinct", "suck", "sudden", "suffer", "sugar", "suggest", "suggestion", "suit",
              "sulky", "summer", "sun", "super", "superb", "superficial", "supply", "support", "suppose", "supreme",
              "surprise", "surround", "suspect", "suspend", "swanky", "sweater", "sweet", "sweltering", "swift", "swim",
              "swing", "switch", "symptomatic", "synonymous", "system", "table", "taboo", "tacit", "tacky", "tail",
              "talented", "talk", "tall", "tame", "tan", "tangible", "tangy", "tank", "tap", "tart", "taste",
              "tasteful",
              "tasteless", "tasty", "tawdry", "tax", "teaching", "team", "tearful", "tease", "tedious", "teeny",
              "teeth", "telephone", "telling", "temper", "temporary", "tempt", "ten", "tendency", "tender",
              "tense", "tent", "tenuous", "terrible", "terrific", "terrify", "territory", "test", "tested", "testy",
              "texture", "thank", "thankful", "thaw", "theory", "therapeutic", "thick", "thin", "thing", "things",
              "thinkable", "third", "thirsty", "thought", "thoughtful", "thoughtless", "thread", "threatening", "three",
              "thrill", "throat", "throne", "thumb", "thunder", "thundering", "tick", "ticket", "tickle", "tidy", "tie",
              "tiger", "tight", "tightfisted", "time", "tin", "tiny", "tip", "tire", "tired", "tiresome", "title",
              "toad",
              "toe", "toes", "tomatoes", "tongue", "tooth", "toothbrush", "toothpaste", "toothsome", "top", "torpid",
              "touch", "tough", "tour", "tow", "towering", "town", "toy", "toys", "trace", "trade", "trail", "train",
              "trains", "tramp", "tranquil", "transport", "trap", "trashy", "travel", "tray", "treat", "treatment",
              "tree",
              "trees", "tremble", "tremendous", "trick", "tricky", "trip", "trite", "trot", "trouble", "troubled",
              "trousers", "truck", "trucks", "truculent", "true", "trust", "truthful", "try", "tub", "tug", "tumble",
              "turkey", "turn", "twig", "twist", "two", "type", "typical", "ubiquitous", "ugliest", "ugly", "ultra",
              "umbrella", "unable", "unaccountable", "unadvised", "unarmed", "unbecoming", "unbiased", "uncle",
              "uncovered",
              "understood", "underwear", "undesirable", "undress", "unequal", "unequaled", "uneven", "unfasten",
              "unhealthy",
              "uninterested", "unique", "unit", "unite", "unkempt", "unknown", "unlock", "unnatural", "unpack",
              "unruly",
              "unsightly", "unsuitable", "untidy", "unused", "unusual", "unwieldy", "unwritten", "upbeat", "uppity",
              "upset",
              "uptight", "use", "used", "useful", "useless", "utopian", "utter", "uttermost", "vacation", "vacuous",
              "vagabond", "vague", "valuable", "value", "van", "vanish", "various", "vase", "vast", "vegetable", "veil",
              "vein", "vengeful", "venomous", "verdant", "verse", "versed", "vessel", "vest", "victorious", "view",
              "vigorous", "violent", "violet", "visit", "visitor", "vivacious", "voice", "voiceless", "volatile",
              "volcano",
              "volleyball", "voracious", "voyage", "vulgar", "wacky", "waggish", "wail", "wait", "waiting", "wakeful",
              "walk", "wall", "wander", "wandering", "want", "wanting", "war", "warlike", "warm", "warn", "wary",
              "wash",
              "waste", "wasteful", "watch", "water", "watery", "wave", "waves", "wax", "way", "weak", "wealth",
              "wealthy",
              "weary", "weather", "week", "weigh", "weight", "welcome", "wet", "wheel", "whimsical", "whine", "whip",
              "whirl",
              "whisper", "whispering", "whistle",
              "white", "whole", "wholesale", "wicked", "wide", "wiggly", "wild", "wilderness", "willing",
              "wind", "window", "windy", "wine", "wing", "wink", "winter", "wipe", "wire", "wiry", "wise", "wish",
              "wistful",
              "witty", "wobble", "woebegone", "woman", "womanly", "women", "wonder", "wonderful", "wood", "wooden",
              "wool",
              "woozy", "word", "work", "workable", "worm", "worried", "worry", "worthless", "wound", "wrap", "wrathful",
              "wreck", "wren", "wrench", "wrestle", "wretched", "wriggle", "wrist", "writer", "writing", "wrong", "wry",
              "yak", "yam", "yard", "yarn", "yawn", "year", "yell", "yellow", "yielding", "yoke", "young",
              "youthful", "yummy", "zany", "zealous", "zebra", "zephyr", "zesty", "zinc", "zip", "zipper", "zippy",
              "zonked",
              "zoo", "zoom"]


class Hangman:

    def __init__(self, words):
        self.words = words
        self.stored_word = random.choice(self.words)
        self.guessed_word = None
        self.guessed_letter = None
        self.number_of_tries = 10
        self.obj = {}
        self.won = False
        self.used_letters = []
        self.used_words = []

    @staticmethod
    def logo_title():
        print("")
        print("                                    WELCOME TO                                                  ")
        print("-----------  |        |   |-------    |       |         / \\         |\\      |       ________  ")
        print("     |       |        |   |           |       |        /   \\        | \\     |      /          ")
        print("     |       |        |   |           |       |       /     \\       |  \\    |     /           ")
        print("     |       |--------|   |-------    |-------|      /-------\\      |   \\   |    |       _____")
        print("     |       |        |   |           |       |     /         \\     |    \\  |    \\          /")
        print("     |       |        |   |           |       |    /           \\    |     \\ |     \\        / ")
        print("     |       |        |   |-------    |       |   /             \\   |      \\|      \\______/  ")

    def check_used(self):
        if self.used_words or self.used_letters:
            return ' or show used letters and words(type S) '
        else:
            return ""

    def display_used(self):
        all_letters_used: str = ''
        all_words_used: str = ''
        for letter in self.used_letters:
            all_letters_used += letter + " "
        for word in self.used_words:
            all_words_used += word + " "

        if self.used_letters: print("Letters used are: " + all_letters_used)
        if self.used_words: print("Words used are: " + all_words_used)

    def display_word(self):
        if self.guessed_word and self.check_word(self.guessed_word):
            print("You guessed the word!!!")
            print("The word is " + self.stored_word)
            self.won = True
            return
        elif self.guessed_letter and self.check_letter(self.guessed_letter):
            print("")
        self.format_displayed_word()

    def format_displayed_word(self):
        length = len(self.stored_word)
        found_word = ""
        if len(self.obj) > 0:
            for i in range(len(self.stored_word)):
                found_word += self.obj[i]
        else:
            print("")
            print("This is the word! Can you guess what is is?")
            print("")
            print("_ " * length)
            print("")
            return
        if "_" not in found_word:
            self.won = True
        print("")
        print("This is the word! Can you guess what is is?")
        print(found_word)
        print("")

    def check_word(self, word):
        if isinstance(word, str) and len(word) > 1:
            self.guessed_word = None
            if word == self.stored_word:
                return True
            else:
                self.number_of_tries -= 1
                return False
        else:
            print('This is not a word!')
            self.guessed_word = None
            return False

    def check_letter(self, letter):
        if isinstance(letter, str) and len(letter) == 1:
            for i in range(len(self.stored_word)):
                if letter == self.stored_word[i]:
                    print("You're getting close!")
                    self.obj.update({i: self.stored_word[i]})
                else:
                    if i not in self.obj:
                        self.obj.update({i: '_'})

            if letter not in self.stored_word:
                self.number_of_tries -= 1
            self.guessed_letter = None
            return True
        else:
            print('This is not a letter!')
            self.guessed_letter = None
            return False

    def get_decision_from_user(self):
        self.display_word()
        if not self.won:
            print('You have ' + str(self.number_of_tries) + ' number of tries left!')
            decision = input('Do you want to guess the word(type W) or a letter(type L) ?' + self.check_used() + '-> ')

            if decision.capitalize() == "W":
                self.guessed_word = input("What is the word? ")
                self.used_words.append(self.guessed_word)
            elif decision.capitalize() == "L":
                self.guessed_letter = input("Guess a letter: ")
                self.used_letters.append(self.guessed_letter)
            elif decision.capitalize() == "S":
                self.display_used()
        if self.won:
            print("Congratulation you've won!")
            return
        elif not self.won and self.number_of_tries == 1:
            print("Game Over!")
            print("The word was " + self.stored_word)
        else:
            self.get_decision_from_user()


game = Hangman(dictionary)
game.logo_title()
game.get_decision_from_user()

