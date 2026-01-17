NAME_READ_PATH="Path to text file containing names of invitees"
LETTER_READ_PATH="Path to letter template.txt"
LETTER_SAVE_PATH="Path for letter to be saved."
PLACEHOLDER="[name]"
with open(LETTER_READ_PATH,'r') as letter:
    current_letter=letter.read()
with open(NAME_READ_PATH,'r') as names:
    for new_name in names:
        modified_new_name=new_name.replace('\n','')
        new_letter=current_letter.replace(PLACEHOLDER,modified_new_name)
        with open(f"{LETTER_SAVE_PATH}/{modified_new_name}.txt",'w') as new_file:
            new_file.write(new_letter)

    
