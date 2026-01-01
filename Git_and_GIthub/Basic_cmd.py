
""" 
/// Basic Cmd \\\


1> git init : -- >  Turns your folder into a Git project.


2> git status : -- >  Shows:
                1. changed files
                2. staged files
                3. untracked files


3> git add file.txt  -- > one particular file 




--------------------------------------------------- >>>  

4> git add .         -- > entier project 




5> git commit -m "message"    ---- > saves a snapshot of your code.
                                  (in short what are you doing / or changing)



6> git log --oneline  : --->   History tracking




7> git remote add origin https://github.com/username/repo-name.git    
: ---- > Connect Local Repo to GitHub



8> git push -u origin main  
:---- >   Uploads your code to GitHub.


git push -f origin main   
< ---- if not working try this lol 


9> git pull origin main





//// Branch Commands (Very Important) \\\\


1 >  Check Branch ---- > git branch

2 >  Create New Branch --- > git branch feature/login

3 >  Switch Branch --- > git checkout feature/login 
                   --- > git switch feature/login

4 > Create + Switch Together  --- > git checkout -b feature/login


---->  Branching (parallel work) < --- 

5 > Merge Branch
      --- > git checkout main
      --- > git merge feature/login



      //// : 
 
      1 > git rm --cached Py_Oops/file name    ---- >  Remove the file and then Push ok 

      
"""