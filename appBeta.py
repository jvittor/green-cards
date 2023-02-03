# Change the variable max_commits, on line 6, to the desired number of commits

import os
import random

counter = 0
max_commits = 10000

def gen_date():
    year = random.randint(2022, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 31)
    date = f"{year}-{month}-{day}"
    
    return date
                    
def gen_commits(counter, max_commits):
    while counter < max_commits:
        date = gen_date()
        counter = counter + 1
        print(date)
        os.system(f"echo {date} > commits.yml")
        os.system(f"git add commits.yml")
        os.system(f'git commit -m "{date}" --date "{date}" > dates.log') #I used dates.log instead of dev null to be able to run on windows
    os.system('git push')

def main():
    gen_commits(counter, max_commits)

if __name__ == '__main__':
    main()
