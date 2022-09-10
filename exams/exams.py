""" Program written by: Bosco Muthini
    All Rights Reserved. No part of this code may be copied, changed or altered without my Permission.
    Failure to comply with this simple terms itafanya tukosane!!! VIBAYA SANA!!!! """
# Write a program that calculates the examination results of a single student.
print('*'*30,'ENG  BMK   @RU', '*'*30)
for i in range(1):

    # The program accepts student name, index number and number of subjects the student is studying.
    # Student name is first name and last name.

    f_name = input('**********Enter the student\'s first name: ')
    l_name = input('**********Enter your student\'s last name: ')
    stud_name = f_name+l_name
    # The program displays an error message if the student name contains numbers or special characters.
    if stud_name.isalpha():
        sec = input('**********Enter the name of your secondary school: ')
        index = int(input('**********Enter this student\'s index number: '))
    else:
        print('INVALID NAME!! Please check the correct spelling of this Student Name.')
        break   # The program is terminated if the Student Name contains numbers or special characters.

    # The program displays an error message if the students enters the number of subjects is less than or exceeding 11.
    subj = int(input('**********How many subjects are you taking? '))
    if subj!=11:
        print('INVALID DATA!!! A student is allowed to take 11 subjects. Please try again.')
    else:   # If the number of subjects is 11, the program allows the user to enter scores in each subject.
        mat = int(input('**********Enter your score in Mathematics: '))
        # The score of each subject ranges from 0-100.
        if mat<0 or mat>100:
            """ An error message is displayed if the  range is not 0 or 100. """
            print('ERROR!! this score is out of range. Please try again.')
            break   # The program is terminated if the range is less than 0 or greater than 100.
        # If the score for each subjects lies within the range, your score will be displayed in the next statement.
        else:
            print('**********Your score in Mathematics is: ', mat)
        eng = int(input('**********Enter your score in English: '))
        if eng<0 or eng>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('**********Your score in English is: ', eng)
        kisw = int(input('**********Enter your score in Kiswahili: '))
        if kisw<0 or kisw>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('**********Your score in Kiswahili is: ', kisw)
        chem = int(input('**********Enter your score in Chemistry: '))
        if chem<0 or chem>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('**********Your score in Chemistry is: ', chem)
        bio = int(input('**********Enter your score in Biology: '))
        if bio<0 or bio>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('**********Your score in Biology is: ', bio)
        phy = int(input('**********Enter your score in Physics: '))
        if phy<0 or phy>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('**********Your score in Physics is: ', phy)
        hist = int(input('**********Enter your score in History: '))
        if hist<0 or hist>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('**********Your score in History is: ', hist)
        geo = int(input('**********Enter your score in Geography: '))
        if geo<0 or geo>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('**********Your score in Geography is: ', geo)
        cre = int(input('**********Enter your in CRE: '))
        if cre<0 or cre>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('**********Your score in CRE is: ', cre)
        comp = int(input('**********Enter your score in Computer Studies: '))
        if comp<0 or comp>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('**********Your score in Computer Studies is: ', comp)
        bis = int(input('**********Enter your score in Business Studies: '))
        if bis<0 or bis>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('**********Your score in Business Studies is: ', bis)

        # This next program single-dashed line to separate the output from the input. The line is 28 dashes long.
        print('---'*29)
        print('---'*9, sec.upper(), 'HIGH SCHOOL', '---'*11,'-')
        print('---'*9, 'MOTTO: Education For Bright Future', '---'*8)
        # To calculate total score, the variable total will do the math.
        total = (mat+eng+kisw+chem+bio+phy+hist+geo+cre+comp+bis)

        # To calculate the average of the student, the variable avg will do the math.
        avg = (total)/11 # To get average, the program divides total by 11.

        """ If the average is greater than or equal to 80 and less than or equal to 100, the program will display 
            student name, index number, score per subject, total, average and assign the student grade A. """
        if avg>=80 and avg<=100:
            print('**********Student Name: ',  f_name+' '+l_name, '\n**********Index Number: ', index,  '\n**********No. of Subjects: ', subj)

            # The program print a line 15 dashes long below Student name, Index Number and the number of subjects.
            print('---'*29)     # The line separates student details from scores per subject.
            print('\n**********Mathematics: ', mat, '\n**********English: ', eng, '\n**********Kiswahili: ', kisw, '\n**********Chemistry: ', chem,
                  '\n**********Biology: ', bio, '\n**********Physics: ', phy, '\n**********History: ', hist, '\n**********Geography: ', geo,
                  '\n**********CRE: ', cre, '\n**********Computer Studies: ', comp, '\n**********Business Studies: ', bis, '\n**********Total: ', total)
            print('**********Average: ', round(avg, 2))     # The program displays the average.
            print('**********Grade: A')   # The program assigns the grade depending on the average. In this case grade A.
            print('---'*29)     # This line encloses teacher's comment based on the student's performance.
            print('Class Teacher Comment:  A Bright student. Keep it up!')

            """ If the average is greater than or equal to 60 and less than 80, the program will display student name,
             index number, score per subject, total, average and assign the student grade B. """
        elif avg>=60:
            print('**********Student Name: ', f_name+' '+l_name, '\n**********Index Number: ', index, '\n**********No. of Subjects: ', subj)
            print('---'*29)      # The line separates student details from scores per subject.
            print('\n**********Mathematics: ', mat, '\n**********English: ', eng, '\n**********Kiswahili: ', kisw, '\n**********Chemistry: ', chem,
                  '\n**********Biology: ', bio, '\n**********Physics: ', phy, '\n**********History: ', hist, '\n**********Geography: ', geo,
                  '\n**********CRE: ', cre, '\n**********Computer Studies: ', comp, '\n**********Business Studies: ', bis, '\n**********Total: ', total)
            print('**********Average: ', round(avg, 2))     # The program displays the average.
            print('**********Grade: B')   # The program assigns the grade depending on the average. In this case grade B.
            print('---'*29)     # This line encloses teacher's comment based on the student's performance.
            print('Class Teacher Comment: Above average. Good Work. Keep it up!!')

            """ If the average is greater than or equal to 40 and less than 60, the program will display student name, 
                index number, score per subject, total, average and assign the student grade C. """
        elif avg>=40:
            print('**********Student Name: ', f_name+' '+l_name, '\n**********Index Number: ', index, '\n**********No. of Subjects: ', subj)
            print('---'*29)     # The line separates student details from scores per subject.
            print('\n**********Mathematics: ', mat, '\n**********English: ', eng, '\n**********Kiswahili: ', kisw, '\n**********Chemistry: ', chem,
                  '\n**********Biology: ', bio, '\n**********Physics: ', phy, '\n**********History: ', hist, '\n**********Geography: ', geo,
                  '\n**********CRE: ', cre, '\n**********Computer Studies: ', comp, '\n**********Business Studies: ',  bis, '\n**********Total: ', total)
            print('**********Average: ', round(avg, 2))    # The program displays the average.
            print('**********Grade: C')   # The program assigns the grade depending on the average. In this case grade C.
            print('---'*29)     # This line encloses teacher's comment based on the student's performance.
            print('Class Teacher Comment: An Average Student. Improve.')

            """ If the average is greater than or equal to 20, the program will display student name, index number, 
                score per subject, total, average and assign the student grade D. """
        elif avg>=20:
            print('**********Student Name: ', f_name+' '+l_name, '\n**********Index Number: ', index, '\n**********No. of Subjects: ', subj)
            print('---'*29)     # The line separates student details from scores per subject.
            print('\n**********Mathematics: ', mat, '\n**********English: ', eng, '\n**********Kiswahili: ', kisw, '\n**********Chemistry: ', chem,
                  '\n**********Biology: ', bio, '\n**********Physics: ', phy, '\n**********History: ', hist, '\n**********Geography: ', geo,
                  '\n**********CRE: ', cre, '\n**********Computer Studies: ', comp, '\n**********Business Studies: ',  bis, '\n**********Total: ', total)
            print('**********Average: ', round(avg, 2))     # The program displays the average.
            print('**********Grade: D')   # The program assigns a grade depending on the average. In this case grade D.
            print('---'*29)     # This line encloses teacher's comment based on the student's performance.
            print('Class Teacher Comment: Below Average. Work Hard.')

            """ If the average is less than 20, the program will display student name, index number, score per 
                         subject, total, average and assign the student grade E. """
        else:
            print('Student Name: ', f_name+' '+l_name, '\nIndex Number: ', index, '\nNo. of Subjects: ', subj)
            print('---'*29)     # The line separates student details from scores per subject.
            print('\n**********Mathematics: ', mat, '\n**********English: ', eng, '\n**********Kiswahili: ', kisw, '\n**********Chemistry: ', chem,
                  '\n**********Biology: ', bio, '\n**********Physics: ', phy, '\n**********History: ', hist, '\n**********Geography: ', geo,
                  '\n**********CRE: ', cre, '\n**********Computer Studies: ', comp, '**********\nBusiness Studies: ',  bis, '\n**********Total: ', total)
            print('**********Average: ', round(avg, 2))     # The program displays the average.
            print('**********Grade: E')   # The program assigns a grade depending on the average. In this case grade E.
            print('---'*29)     # This line encloses teacher's comment based on the student's performance.
            print('Class Teacher\'s Comment: Poor Performance. Read your Books thoroughly.')

    # The program prints double-dashed line to signify end of loop. The lines are 29 dashes long.
    print('---'*29)
    print('---'*29)

    # The program prints the student name and index number after the two dashed lines.
    pass
    print('Student Name: ', f_name+' '+l_name, 'Index Number: ', index)
    print('---'*29)



