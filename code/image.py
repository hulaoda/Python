from easygui import*

while True:
    choices_ =  ["TC"
               ,"TCRF"
               ]
    msg_    = "Complex thinking, simple operation"
    title_  = "C919"
    image_  = "b.gif"

    choice_ = choicebox(msg_, title_, choices, image=iamge_)
    if not choice:return
    if choice == "TC": createTC()
             
    
    
    
