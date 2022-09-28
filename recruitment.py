# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills():
    return ["Java","Python","C++"]
    

#print(get_skills())


# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    num=1
    print("Skills: ")
    for skill in skills:
        print(f"{num}.{skill}")
        num=num+1
        




# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    
    print(show_skills(get_skills()))
    first_skill=int(input("Choose a skill from above by entering its number: "))
    second_skill=int(input("Choose another skill from above by entering its number: "))
    user_skills=[skills[first_skill-1],skills[second_skill-1]]
    #print(user_skills)
    return user_skills
    





# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv={}
    cv["name"]=input("What's your name? ")
    cv["age"]=int(input("How old are you? "))
    cv["experience"]=int(input("How many years of experience do you have? "))
    cv["skills"]=get_user_skills(get_skills())
    #print(cv)
    return cv



# This function checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if 25<= cv["age"] <= 40 and cv["experience"] >3 and  desired_skill in cv["skills"]:
        return True
    else:
        return False



def main():
    print("Welcome to the special recruitment program, please answer the following questions:")
    skills=get_skills
    user_cv=get_user_cv(skills)
    is_accepted=check_acceptance(user_cv,"C++")
    if is_accepted:
        print(f"You have been accepted, {user_cv['name']}.")
    else: 
        print("You have been rejected")



if __name__ == "__main__":
    main()
