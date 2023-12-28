import os
import os
import subprocess
import glob


# # List of cusswords
# cusswords = ['frigger', 'fucking', 'cunt', 'shitty', 'piss', 'bugger', 'shitter,', 'dick', 'whore',
#               'fuckin,', 'slut', 'arsehole', 'shit', 'shitter.', 'horseshit', 'pain in the neck', 
#               'whore.', 'damn', 'fuckin', 'fucker', 'bastards', 'dickhead', 'cock', 'bitch', 'hell',
#                 'motherfucker', 'shag', 'jerk', 'dipshit,', 'fool', 'godsdamn', 'stupid', 'dick head', 
#                 'brotherfucker', 'shite', 'taking a piss', 'big-ass', 'ass', 'whore,', 'goddamn', 
#                 'dipshit.', 'bitch.', 'jesus mary and joseph', 'christ on a bike', 'bloody', 'fuck you,', 
#                 'pussy', 'piss off', 'arsehead', 'jesus h. christ', 'fuck you', 'shity', 'fatherfucker', 
#                 'dyke', 'bastard', 'asshole', 'bimbo', 'son of a bitch', 'shitter', 'shit.', 'nigra', 
#                 'idiot', 'cocksucker', 'asshole,', 'holy-shit', 'crap', 'son of a whore', 'fucking,', 
#                 'shit,', 'bullshit', "nigga's", 'damn it', 'wanker', 'twat', 'big-ass.', 'holy-hell', 
#                 'fuck', 'sisterfucker', 'asshole.', 'dumb', 'sweet jesus', 'shit', 'child-fucker', 'bullshit.', 
#                 'loser', 'dipshit', 'retard', 'rubbish', 'bitch,', 'arse', 'niggas', 'bollocks', "shit's", 
#                 'prick', 'shit?', 'lame', 'shitty,', 'jesus harold  christ', 'nigga', 'fuck you.', 'big-ass,',
#                 'bullshit,', 'wimp', 'jesus christ', 'kike']


#audio file that will be processed
mp3_files = glob.glob("*.mp3")

for input_audio_file in mp3_files:
    
#directory for the output text file that will be processed
  output_directory = os.path.join(os.path.expanduser("~"), "Desktop")

# Check if the text file already exists
text_file_path = os.path.join(output_directory, f"{os.path.splitext(input_audio_file)[0]}.txt")
if not os.path.exists(text_file_path):
  # Construct the command
  command = ["whisperx", input_audio_file, "--compute_type", "int8", "--output_format", "txt", "--output_dir", output_directory]

  # Run the command
  try:
    subprocess.run(command, check=True)
  except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
else:
  print("\n\nText file already exists. Skipping subprocess.\n")

# Load the text file
text_file_path = os.path.join(output_directory, f"{os.path.splitext(input_audio_file)[0]}.txt")
with open(text_file_path, "r") as text_file:
  data = text_file.read()





pg_cusswords = ['arse', 'bugger', 'crap', 'darn', 'heck']
pg13_cusswords = ['ass', 'damn', 'dick', 'piss', 'twat']
r_cusswords = ['bastard', 'bitch', 'fuck', 'motherfucker', 'shit', 'cunt']



#function to separate cusswords by pg label
def is_cussword_pg(data, pg_cusswords):
  for word in pg_cusswords:
    if word in data:
       return "PG"
  return "General audiences"

#function to separate cusswords by pg13 label
def is_cussword_pg13 (data, pg13_cusswords):
    for word in pg13_cusswords:
       if word in data:
        return "PG-13"
    return "General audiences"

#function to separate cusswrods by R label
def is_cussword_r (data, r_cusswords):
    for word in r_cusswords:
       if word in data:
        return "General audiences"

#main funcion for the processing
def content_rating (data):
    if is_cussword_r(data, r_cusswords):
        return "R"
    
    elif is_cussword_pg13(data, pg13_cusswords):
      return "PG-13"
  
    elif is_cussword_pg(data, pg_cusswords):
        return "PG"
    
    else:
      return "Not Categorized (or G)"


#this is a placeholder until i can pass a json file to check    
content_to_check = data
episode_rating = content_rating(content_to_check)
    
if episode_rating != "Not Categorized (or G)":
  for word in r_cusswords + pg13_cusswords + pg_cusswords:
    if word in data:
      print(f"Found word: {word}")
print(f"\nYour episode received a {episode_rating} rating\n")
